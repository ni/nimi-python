.. py:module:: nidcpower

Session
=======

.. py:class:: Session(self, resource_name, channels=None, reset=False, options={}, independent_channels=True)

    

    Creates and returns a new NI-DCPower session to the instrument(s) and channel(s) specified
    in **resource name** to be used in all subsequent NI-DCPower method calls. With this method,
    you can optionally set the initial state of the following session properties:

    -  :py:attr:`nidcpower.Session.simulate`
    -  :py:attr:`nidcpower.Session.driver_setup`

    After calling this method, the specified channel or channels will be in the Uncommitted
    state.

    To place channel(s) in a known start-up state when creating a new session, set **reset** to
    True. This action is equivalent to using the :py:meth:`nidcpower.Session.reset` method immediately after initializing the
    session.

    To open a session and leave the channel(s) in an existing configuration without passing
    through a transitional output state, set **reset** to False. Next, configure the channel(s)
    as in the previous session, change the desired settings, and then call the :py:meth:`nidcpower.Session.initiate` method
    to write both settings.

    **Details of Independent Channel Operation**

    With this method and channel-based NI-DCPower methods and properties, you can use any
    channels in the session independently. For example, you can initiate a subset of channels in
    the session with :py:meth:`nidcpower.Session.initiate`, and the other channels in the session remain in the Uncommitted
    state.

    When you initialize with independent channels, each channel steps through the NI-DCPower
    programming state model independently of all other channels, and you can specify a subset of
    channels for most operations.

    **Note** You can make concurrent calls to a session from multiple threads, but the session
    executes the calls one at a time. If you specify multiple channels for a method or property,
    the session may perform the operation on multiple channels in parallel, though this is not
    guaranteed, and some operations may execute sequentially.

    



    :param resource_name:
        

        Specifies the **resource name** as seen in Measurement
        & Automation Explorer (MAX) or lsni, for example "PXI1Slot3" where "PXI1Slot3" is an
        instrument's **resource name**. If independent_channels is False, **resource name**
        can also be a logical IVI name.

        If independent_channels is True, **resource name** can be names of the instrument(s)
        and the channel(s) to initialize. Specify the instrument(s) and channel(s) using the
        form "PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or
        PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3", where "PXI1Slot3" and "PXI1Slot4" are
        instrument resource names followed by channels. If you exclude a channels string
        after an instrument resource name, all channels of the instrument(s) are included in
        the session.

        


    :type resource_name: str, list, tuple

    :param channels:
        

        For new applications, use the default value of None
        and specify the channels in **resource name**.

        Specifies which output channel(s) to include in a new session. Specify multiple
        channels by using a channel list or a channel range. A channel list is a comma (,)
        separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).
        A channel range is a lower bound channel followed by a hyphen (-) or colon (:)
        followed by an upper bound channel (for example, 0-2 specifies channels 0, 1,
        and 2).

        If independent_channels is False, this argument specifies which channels to include
        in a legacy synchronized channels session. If you do not specify any channels, by
        default all channels on the device are included in the session.

        If independent_channels is True, this argument combines with **resource name** to
        specify which channels to include in an independent channels session. Initializing
        an independent channels session with a channels argument is deprecated.

        


    :type channels: str, list, range, tuple

    :param reset:
        

        Specifies whether to reset channel(s) during the initialization procedure.

        


    :type reset: bool

    :param options:
        

        Specifies the initial value of certain properties for the session. The
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


    :type options: dict

    :param independent_channels:
        

        Specifies whether to initialize the session with
        independent channels. Set this argument to False on legacy applications or if you
        are unable to upgrade your NI-DCPower driver runtime to 20.6 or higher.

        


    :type independent_channels: bool


Methods
=======

abort
-----

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: abort()

            Transitions the specified channel(s) from the Running state to the
            Uncommitted state. If a sequence is running, it is stopped. Any
            configuration methods called after this method are not applied until
            the :py:meth:`nidcpower.Session.initiate` method is called. If power output is enabled
            when you call the :py:meth:`nidcpower.Session.abort` method, the output channels remain
            in their current state and continue providing power.

            Use the :py:meth:`nidcpower.Session.ConfigureOutputEnabled` method to disable power
            output on a per channel basis. Use the :py:meth:`nidcpower.Session.reset` method to
            disable output on all channels.

            Refer to the `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
            the *NI DC Power Supplies and SMUs Help* for information about the
            specific NI-DCPower software states.

            **Related Topics:**

            `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].abort`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.abort`


clear_latched_output_cutoff_state
---------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: clear_latched_output_cutoff_state(output_cutoff_reason)

            Clears the state of an output cutoff that was engaged.
            To clear the state for all output cutoff reasons, use :py:data:`~nidcpower.OutputCutoffReason.ALL`.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].clear_latched_output_cutoff_state`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.clear_latched_output_cutoff_state`


            :param output_cutoff_reason:


                Specifies the reasons for which to clear the output cutoff state.

                +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.ALL`                  | Clears all output cutoff conditions                                                                             |
                +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_OUTPUT_HIGH`  | Clears cutoffs caused when the output exceeded the high cutoff limit for voltage output                         |
                +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_OUTPUT_LOW`   | Clears cutoffs caused when the output fell below the low cutoff limit for voltage output                        |
                +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.CURRENT_MEASURE_HIGH` | Clears cutoffs caused when the measured current exceeded the high cutoff limit for current output               |
                +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.CURRENT_MEASURE_LOW`  | Clears cutoffs caused when the measured current fell below the low cutoff limit for current output              |
                +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_CHANGE_HIGH`  | Clears cutoffs caused when the voltage slew rate increased beyond the positive change cutoff for voltage output |
                +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_CHANGE_LOW`   | Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for voltage output |
                +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.CURRENT_CHANGE_HIGH`  | Clears cutoffs caused when the current slew rate increased beyond the positive change cutoff for current output |
                +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.CURRENT_CHANGE_LOW`   | Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for current output |
                +---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+


            :type output_cutoff_reason: :py:data:`nidcpower.OutputCutoffReason`

close
-----

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: close()

            Closes the session specified in **vi** and deallocates the resources
            that NI-DCPower reserves. If power output is enabled when you call this
            method, the output channels remain in their existing state and
            continue providing power. Use the :py:meth:`nidcpower.Session.ConfigureOutputEnabled`
            method to disable power output on a per channel basis. Use the
            :py:meth:`nidcpower.Session.reset` method to disable power output on all channel(s).

            **Related Topics:**

            `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: commit()

            Applies previously configured settings to the specified channel(s). Calling this
            method moves the NI-DCPower session from the Uncommitted state into
            the Committed state. After calling this method, modifying any
            property reverts the NI-DCPower session to the Uncommitted state. Use
            the :py:meth:`nidcpower.Session.initiate` method to transition to the Running state.
            Refer to the `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
            the *NI DC Power Supplies and SMUs Help* for details about the specific
            NI-DCPower software states.

            **Related Topics:**

            `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].commit`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.commit`


configure_aperture_time
-----------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: configure_aperture_time(aperture_time, units=nidcpower.ApertureTimeUnits.SECONDS)

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

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_aperture_time`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.configure_aperture_time`


            :param aperture_time:


                Specifies the aperture time. Refer to the *Aperture Time* topic for your
                device in the *NI DC Power Supplies and SMUs Help* for more information.

                


            :type aperture_time: float
            :param units:


                Specifies the units for **apertureTime**.
                **Defined Values**:

                +-----------------------------------------------------------+------------------------------+
                | :py:data:`~nidcpower.ApertureTimeUnits.SECONDS`           | Specifies seconds.           |
                +-----------------------------------------------------------+------------------------------+
                | :py:data:`~nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES` | Specifies Power Line Cycles. |
                +-----------------------------------------------------------+------------------------------+


            :type units: :py:data:`nidcpower.ApertureTimeUnits`

configure_lcr_custom_cable_compensation
---------------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: configure_lcr_custom_cable_compensation(custom_cable_compensation_data)

            Applies previously generated open and short custom cable compensation data to LCR measurements.

            This method applies custom cable compensation data when you have set :py:attr:`nidcpower.Session.cable_length` property to :py:data:`~nidcpower.CableLength.CUSTOM_AS_CONFIGURED`.

            Call this method after you have obtained custom cable compensation data.

            If :py:attr:`nidcpower.Session.lcr_short_custom_cable_compensation_enabled` property is set to True, you must generate data with both :py:meth:`nidcpower.Session.perform_lcr_open_custom_cable_compensation` and :py:meth:`nidcpower.Session.perform_lcr_short_custom_cable_compensation`;
            if False, you must only use :py:meth:`nidcpower.Session.perform_lcr_open_custom_cable_compensation`, and NI-DCPower uses default short data.

            Call :py:meth:`nidcpower.Session.get_lcr_custom_cable_compensation_data` and pass the **custom cable compensation data** to this method.

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_lcr_custom_cable_compensation`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.configure_lcr_custom_cable_compensation`


            :param custom_cable_compensation_data:


                The open and short custom cable compensation data to apply.

                


            :type custom_cable_compensation_data: bytes

create_advanced_sequence
------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: create_advanced_sequence(sequence_name, property_names, set_as_active_sequence=True)

            Creates an empty advanced sequence. Call the
            :py:meth:`nidcpower.Session.create_advanced_sequence_step` method to add steps to the
            active advanced sequence.

            You can create multiple advanced sequences in a session.

            **Support for this method**

            You must set the source mode to Sequence to use this method.

            Using the :py:meth:`nidcpower.Session.set_sequence` method with Advanced Sequence
            methods is unsupported.

            Use this method in the Uncommitted or Committed programming states.
            Refer to the `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
            the *NI DC Power Supplies and SMUs Help* for more information about
            NI-DCPower programming states.

            **Related Topics**:

            `Advanced Sequence
            Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

            `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

            :py:meth:`nidcpower.Session.create_advanced_sequence_step`

            

            .. note:: This method is not supported on all devices. Refer to `Supported
                Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].create_advanced_sequence`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.create_advanced_sequence`


            :param sequence_name:


                Specifies the name of the sequence to create.

                


            :type sequence_name: str
            :param property_names:


                Specifies the names of the properties you reconfigure per step in the advanced sequence. The following table lists which properties can be configured in an advanced sequence for each NI-DCPower device that supports advanced sequencing. A Yes indicates that the property can be configured in advanced sequencing. An No indicates that the property cannot be configured in advanced sequencing.

                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | Property                                                    | PXIe-4135 | PXIe-4136 | PXIe-4137 | PXIe-4138 | PXIe-4139 | PXIe-4140/4142/4144 | PXIe-4141/4143/4145 | PXIe-4162/4163 |
                +=============================================================+===========+===========+===========+===========+===========+=====================+=====================+================+
                | :py:attr:`nidcpower.Session.dc_noise_rejection`             | Yes       | No        | Yes       | No        | Yes       | No                  | No                  | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.aperture_time`                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.measure_record_length`          | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.sense`                          | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.ovp_enabled`                    | Yes       | Yes       | Yes       | No        | No        | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.ovp_limit`                      | Yes       | Yes       | Yes       | No        | No        | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_bias_delay`               | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_off_time`                 | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_on_time`                  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.source_delay`                   | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.current_compensation_frequency` | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.current_gain_bandwidth`         | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.current_pole_zero_ratio`        | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.voltage_compensation_frequency` | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.voltage_gain_bandwidth`         | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.voltage_pole_zero_ratio`        | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.current_level`                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.current_level_range`            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.voltage_limit`                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.voltage_limit_high`             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.voltage_limit_low`              | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.voltage_limit_range`            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.current_limit`                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.current_limit_high`             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.current_limit_low`              | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.current_limit_range`            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.voltage_level`                  | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.voltage_level_range`            | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.output_enabled`                 | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.output_function`                | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.output_resistance`              | Yes       | No        | Yes       | No        | Yes       | No                  | Yes                 | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_bias_current_level`       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_bias_voltage_limit`       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_bias_voltage_limit_high`  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_bias_voltage_limit_low`   | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_current_level`            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_current_level_range`      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_voltage_limit`            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_voltage_limit_high`       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_voltage_limit_low`        | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_voltage_limit_range`      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_bias_current_limit`       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_bias_current_limit_high`  | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_bias_current_limit_low`   | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_bias_voltage_level`       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_current_limit`            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_current_limit_high`       | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_current_limit_low`        | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_current_limit_range`      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_voltage_level`            | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.pulse_voltage_level_range`      | Yes       | Yes       | Yes       | Yes       | Yes       | No                  | No                  | No             |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+
                | :py:attr:`nidcpower.Session.transient_response`             | Yes       | Yes       | Yes       | Yes       | Yes       | Yes                 | Yes                 | Yes            |
                +-------------------------------------------------------------+-----------+-----------+-----------+-----------+-----------+---------------------+---------------------+----------------+


            :type property_names: list of str
            :param set_as_active_sequence:


                Specifies that this current sequence is active.

                


            :type set_as_active_sequence: bool

create_advanced_sequence_commit_step
------------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: create_advanced_sequence_commit_step(set_as_active_step=True)

            Creates a Commit step in the Active advanced sequence. A Commit step
            configures channels to a user-defined known state before starting the advanced sequence.
            When a Commit step exists in the Active advanced sequence, you cannot
            set the output method to Pulse Voltage or Pulse Current in either
            the Commit step (-1) or step 0. When you create an advanced sequence
            step, each property you passed to the :py:meth:`nidcpower.Session.create_advanced_sequence`
            method is reset to its default value for that step unless otherwise specified.

            **Support for this Method**

            You must set the source mode to Sequence to use this method.

            Using the :py:meth:`nidcpower.Session.set_sequence` method with Advanced Sequence
            methods is unsupported.

            **Related Topics**:

            `Advanced Sequence
            Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

            `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

            :py:meth:`nidcpower.Session.create_advanced_sequence`

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].create_advanced_sequence_commit_step`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.create_advanced_sequence_commit_step`


            :param set_as_active_step:


                Specifies whether the step created with this method is active in the Active advanced sequence.

                


            :type set_as_active_step: bool

create_advanced_sequence_step
-----------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: create_advanced_sequence_step(set_as_active_step=True)

            Creates a new advanced sequence step in the advanced sequence specified
            by the Active advanced sequence. When you create an advanced sequence
            step, each property you passed to the :py:meth:`nidcpower.Session.create_advanced_sequence`
            method is reset to its default value for that step unless otherwise
            specified.

            **Support for this Method**

            You must set the source mode to Sequence to use this method.

            Using the :py:meth:`nidcpower.Session.set_sequence` method with Advanced Sequence
            methods is unsupported.

            **Related Topics**:

            `Advanced Sequence
            Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

            `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

            :py:meth:`nidcpower.Session.create_advanced_sequence`

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].create_advanced_sequence_step`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.create_advanced_sequence_step`


            :param set_as_active_step:


                Specifies whether the step created with this method is active in the Active advanced sequence.

                


            :type set_as_active_step: bool

delete_advanced_sequence
------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: delete_advanced_sequence(sequence_name)

            Deletes a previously created advanced sequence and all the advanced
            sequence steps in the advanced sequence.

            **Support for this Method**

            You must set the source mode to Sequence to use this method.

            Using the :py:meth:`nidcpower.Session.set_sequence` method with Advanced Sequence
            methods is unsupported.

            **Related Topics**:

            `Advanced Sequence
            Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

            `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].delete_advanced_sequence`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.delete_advanced_sequence`


            :param sequence_name:


                specifies the name of the sequence to delete.

                


            :type sequence_name: str

disable
-------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: disable()

            This method performs the same actions as the :py:meth:`nidcpower.Session.reset`
            method, except that this method also immediately sets the
            :py:attr:`nidcpower.Session.output_enabled` property to False.

            This method opens the output relay on devices that have an output
            relay.

            



export_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: export_attribute_configuration_buffer()

            Exports the property configuration of the session to the specified
            configuration buffer.

            You can export and import session property configurations only between
            devices with identical model numbers and the same number of configured
            channels.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑DCPower returns
            an error.

            **Support for this Method**

            Calling this method in `Sequence Source
            Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

            **Channel Mapping Behavior for Multichannel Sessions**

            When importing and exporting session property configurations between
            NI‑DCPower sessions that were initialized with different channels, the
            configurations of the exporting channels are mapped to the importing
            channels in the order you specify in the **channelName** input to the
            :py:meth:`nidcpower.Session.__init__` method.

            For example, if your entry for **channelName** is 0,1 for the exporting
            session and 1,2 for the importing session:

            -  The configuration exported from channel 0 is imported into channel 1.
            -  The configuration exported from channel 1 is imported into channel 2.

            **Related Topics:**

            `Using Properties and
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

            `Setting Properties and Properties Before Reading
            Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            

            .. note:: This method will return an error if the total number of channels
                initialized for the exporting session is not equal to the total number
                of channels initialized for the importing session.



            :rtype: bytes
            :return:


                    Specifies the byte array buffer to be populated with the exported
                    property configuration.

                    



export_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: export_attribute_configuration_file(file_path)

            Exports the property configuration of the session to the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers and the same number of configured
            channels.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑DCPower returns
            an error.

            **Support for this Method**

            Calling this method in `Sequence Source
            Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

            **Channel Mapping Behavior for Multichannel Sessions**

            When importing and exporting session property configurations between
            NI‑DCPower sessions that were initialized with different channels, the
            configurations of the exporting channels are mapped to the importing
            channels in the order you specify in the **channelName** input to the
            :py:meth:`nidcpower.Session.__init__` method.

            For example, if your entry for **channelName** is 0,1 for the exporting
            session and 1,2 for the importing session:

            -  The configuration exported from channel 0 is imported into channel 1.
            -  The configuration exported from channel 1 is imported into channel 2.

            **Related Topics:**

            `Using Properties and
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

            `Setting Properties and Properties Before Reading
            Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            

            .. note:: This method will return an error if the total number of channels
                initialized for the exporting session is not equal to the total number
                of channels initialized for the importing session.



            :param file_path:


                Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .nidcpowerconfig

                


            :type file_path: str

fetch_multiple
--------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: fetch_multiple(count, timeout=hightime.timedelta(seconds=1.0))

            Returns a list of named tuples (Measurement) that were
            previously taken and are stored in the NI-DCPower buffer. This method
            should not be used when the :py:attr:`nidcpower.Session.measure_when` property is
            set to :py:data:`~nidcpower.MeasureWhen.ON_DEMAND`. You must first call
            :py:meth:`nidcpower.Session.initiate` before calling this method.

            Fields in Measurement:

            - **voltage** (float)
            - **current** (float)
            - **in_compliance** (bool)
            - **channel** (str)

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].fetch_multiple`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.fetch_multiple`


            :param count:


                Specifies the number of measurements to fetch.

                


            :type count: int
            :param timeout:


                Specifies the maximum time allowed for this method to complete. If the method does not complete within this time interval, NI-DCPower returns an error.

                

                .. note:: When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: list of Measurement
            :return:


                    List of named tuples with fields:

                    - **voltage** (float)
                    - **current** (float)
                    - **in_compliance** (bool)
                    - **channel** (str)

                    



get_channel_name
----------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_channel_name(index)

            Retrieves the output **channelName** that corresponds to the requested
            **index**. Use the :py:attr:`nidcpower.Session.channel_count` property to
            determine the upper bound of valid values for **index**.

            



            :param index:


                Specifies which output channel name to return. The index values begin at
                1.

                


            :type index: int

            :rtype: str
            :return:


                    Returns the output channel name that corresponds to **index**.

                    



get_channel_names
-----------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_channel_names(indices)

            Returns a list of channel names for the given channel indices.

            



            :param indices:


                Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.

                


            :type indices: basic sequence types or str or int

            :rtype: list of str
            :return:


                    The channel name(s) at the specified indices.

                    



get_ext_cal_last_date_and_time
------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_ext_cal_last_date_and_time()

            Returns the date and time of the last successful calibration.

            



            :rtype: hightime.datetime
            :return:


                    Indicates date and time of the last calibration.

                    



get_ext_cal_last_temp
---------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_ext_cal_last_temp()

            Returns the onboard **temperature** of the device, in degrees Celsius,
            during the last successful external calibration.

            



            :rtype: float
            :return:


                    Returns the onboard **temperature** of the device, in degrees Celsius,
                    during the last successful external calibration.

                    



get_ext_cal_recommended_interval
--------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_ext_cal_recommended_interval()

            Returns the recommended maximum interval, in **months**, between
            external calibrations.

            



            :rtype: hightime.timedelta
            :return:


                    Specifies the recommended maximum interval, in **months**, between
                    external calibrations.

                    



get_lcr_compensation_last_date_and_time
---------------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_lcr_compensation_last_date_and_time(compensation_type)

            Returns the date and time the specified type of compensation data for LCR measurements was most recently generated.

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_lcr_compensation_last_date_and_time`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.get_lcr_compensation_last_date_and_time`


            :param compensation_type:


                Specifies the type of compensation for LCR measurements.

                


            :type compensation_type: :py:data:`nidcpower.LCRCompensationType`

            :rtype: hightime.datetime
            :return:


                    Returns the date and time the specified type of compensation data for LCR measurements was most recently generated.

                    



get_lcr_custom_cable_compensation_data
--------------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_lcr_custom_cable_compensation_data()

            Collects previously generated open and short custom cable compensation data so you can then apply it to LCR measurements with :py:meth:`nidcpower.Session.configure_lcr_custom_cable_compensation`.

            Call this method after you have obtained open and short custom cable compensation data. Pass the **custom cable compensation data** to :py:meth:`nidcpower.Session.configure_lcr_custom_cable_compensation`

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_lcr_custom_cable_compensation_data`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.get_lcr_custom_cable_compensation_data`


            :rtype: bytes
            :return:


                    The open and short custom cable compensation data to retrieve.

                    



get_self_cal_last_date_and_time
-------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_self_cal_last_date_and_time()

            Returns the date and time of the oldest successful self-calibration from among the channels in the session.

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.



            :rtype: hightime.datetime
            :return:


                    Returns the date and time the device was last calibrated.

                    



get_self_cal_last_temp
----------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_self_cal_last_temp()

            Returns the onboard temperature of the device, in degrees Celsius,
            during the oldest successful self-calibration from among the channels in
            the session.

            For example, if you have a session using channels 1 and 2, and you
            perform a self-calibration on channel 1 with a device temperature of 25
            degrees Celsius at 2:00, and a self-calibration was performed on channel
            2 at 27 degrees Celsius at 3:00 on the same day, this method returns
            25 for the **temperature** parameter.

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.



            :rtype: float
            :return:


                    Returns the onboard **temperature** of the device, in degrees Celsius,
                    during the oldest successful calibration.

                    



import_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: import_attribute_configuration_buffer(configuration)

            Imports a property configuration to the session from the specified
            configuration buffer.

            You can export and import session property configurations only between
            devices with identical model numbers and the same number of configured
            channels.

            **Support for this Method**

            Calling this method in `Sequence Source
            Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

            **Channel Mapping Behavior for Multichannel Sessions**

            When importing and exporting session property configurations between
            NI‑DCPower sessions that were initialized with different channels, the
            configurations of the exporting channels are mapped to the importing
            channels in the order you specify in the **channelName** input to the
            :py:meth:`nidcpower.Session.__init__` method.

            For example, if your entry for **channelName** is 0,1 for the exporting
            session and 1,2 for the importing session:

            -  The configuration exported from channel 0 is imported into channel 1.
            -  The configuration exported from channel 1 is imported into channel 2.

            **Related Topics:**

            `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

            `Using Properties and
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

            `Setting Properties and Properties Before Reading
            Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            

            .. note:: This method will return an error if the total number of channels
                initialized for the exporting session is not equal to the total number
                of channels initialized for the importing session.



            :param configuration:


                Specifies the byte array buffer that contains the property
                configuration to import.

                


            :type configuration: bytes

import_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: import_attribute_configuration_file(file_path)

            Imports a property configuration to the session from the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers and the same number of configured
            channels.

            **Support for this Method**

            Calling this method in `Sequence Source
            Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

            **Channel Mapping Behavior for Multichannel Sessions**

            When importing and exporting session property configurations between
            NI‑DCPower sessions that were initialized with different channels, the
            configurations of the exporting channels are mapped to the importing
            channels in the order you specify in the **channelName** input to the
            :py:meth:`nidcpower.Session.__init__` method.

            For example, if your entry for **channelName** is 0,1 for the exporting
            session and 1,2 for the importing session:

            -  The configuration exported from channel 0 is imported into channel 1.
            -  The configuration exported from channel 1 is imported into channel 2.

            **Related Topics:**

            `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

            `Using Properties and
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

            `Setting Properties and Properties Before Reading
            Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            

            .. note:: This method will return an error if the total number of channels
                initialized for the exporting session is not equal to the total number
                of channels initialized for the importing session.



            :param file_path:


                Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .nidcpowerconfig

                


            :type file_path: str

initiate
--------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: initiate()

            Starts generation or acquisition, causing the specified channel(s) to
            leave the Uncommitted state or Committed state and enter the Running
            state. To return to the Uncommitted state call the :py:meth:`nidcpower.Session.abort`
            method. Refer to the `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
            the *NI DC Power Supplies and SMUs Help* for information about the
            specific NI-DCPower software states.

            **Related Topics:**

            `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].initiate`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.initiate`


lock
----

    .. py:currentmodule:: nidcpower.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`nidcpower.Session.lock` method.
        -  A call to NI-DCPower locked the session.
        -  After a call to the :py:meth:`nidcpower.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`nidcpower.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`nidcpower.Session.lock` method and the
           :py:meth:`nidcpower.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nidcpower.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nidcpower.Session.lock` method with a call to
    the :py:meth:`nidcpower.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with nidcpower.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`nidcpower.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited


measure
-------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: measure(measurement_type)

            Returns the measured value of either the voltage or current on the
            specified output channel. Each call to this method blocks other
            method calls until the hardware returns the **measurement**. To
            measure multiple output channels, use the :py:meth:`nidcpower.Session.measure_multiple`
            method.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].measure`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.measure`


            :param measurement_type:


                Specifies whether a voltage or current value is measured.
                **Defined Values**:

                +------------------------------------------------+------------------------------+
                | :py:data:`~nidcpower.MeasurementTypes.VOLTAGE` | The device measures voltage. |
                +------------------------------------------------+------------------------------+
                | :py:data:`~nidcpower.MeasurementTypes.CURRENT` | The device measures current. |
                +------------------------------------------------+------------------------------+


            :type measurement_type: :py:data:`nidcpower.MeasurementTypes`

            :rtype: float
            :return:


                    Returns the value of the measurement, either in volts for voltage or
                    amps for current.

                    



measure_multiple
----------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: measure_multiple()

            Returns a list of named tuples (Measurement) containing the measured voltage
            and current values on the specified output channel(s). Each call to this method
            blocks other method calls until the measurements are returned from the device.
            The order of the measurements returned in the array corresponds to the order
            on the specified output channel(s).

            Fields in Measurement:

            - **voltage** (float)
            - **current** (float)
            - **in_compliance** (bool) - Always None
            - **channel** (str)

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].measure_multiple`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.measure_multiple`


            :rtype: list of Measurement
            :return:


                    List of named tuples with fields:

                    - **voltage** (float)
                    - **current** (float)
                    - **in_compliance** (bool) - Always None
                    - **channel** (str)

                    



perform_lcr_open_compensation
-----------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: perform_lcr_open_compensation(additional_frequencies=None)

            Generates open compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.

            You must physically configure an open LCR circuit to use this method to generate valid open compensation data.

            When you call this method:

            -  The open compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
            -  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

            To apply the open compensation data you generate with this method to your LCR measurements, set the :py:attr:`nidcpower.Session.lcr_open_compensation_enabled` property to True.

            Corrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

            .. note:: Default Open Compensation Frequencies:
                By default, NI-DCPower uses the following frequencies for LCR open compensation:

                -  10 logarithmic steps at 1 kHz frequency decade
                -  10 logarithmic steps at 10 kHz frequency decade
                -  100 logarithmic steps at 100 kHz frequency decade
                -  100 logarithmic steps at 1 MHz frequency decade

                The actual frequencies used depend on the bandwidth of your instrument.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].perform_lcr_open_compensation`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.perform_lcr_open_compensation`


            :param additional_frequencies:


                Defines a further set of frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies.

                


            :type additional_frequencies: list of float

perform_lcr_open_custom_cable_compensation
------------------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: perform_lcr_open_custom_cable_compensation()

            Generates open custom cable compensation data for LCR measurements.

            To use this method, you must physically configure an open LCR circuit to generate valid open custom cable compensation data.

            When you call this method:

            -  The open compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
            -  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].perform_lcr_open_custom_cable_compensation`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.perform_lcr_open_custom_cable_compensation`


perform_lcr_short_compensation
------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: perform_lcr_short_compensation(additional_frequencies=None)

            Generates short compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.

            You must physically configure your LCR circuit with a short to use this method to generate valid short compensation data.

            When you call this method:

            -  The short compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
            - Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

            To apply the short compensation data you generate with this method to your LCR measurements, set the :py:attr:`nidcpower.Session.lcr_short_compensation_enabled` property to True.

            Corrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

            .. note:: Default Short Compensation Frequencies:
                By default, NI-DCPower uses the following frequencies for LCR short compensation:

                -  10 logarithmic steps at 1 kHz frequency decade
                -  10 logarithmic steps at 10 kHz frequency decade
                -  100 logarithmic steps at 100 kHz frequency decade
                -  100 logarithmic steps at 1 MHz frequency decade

                The actual frequencies used depend on the bandwidth of your instrument.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].perform_lcr_short_compensation`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.perform_lcr_short_compensation`


            :param additional_frequencies:


                Defines a further set of frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies.

                


            :type additional_frequencies: list of float

perform_lcr_short_custom_cable_compensation
-------------------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: perform_lcr_short_custom_cable_compensation()

            Generates short custom cable compensation data for LCR measurements.

            To use this method:

            -  You must physically configure your LCR circuit with a short to generate valid short custom cable compensation data.
            -  Set :py:attr:`nidcpower.Session.lcr_short_custom_cable_compensation_enabled` property to True

            When you call this method:

            -  The short compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
            -  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].perform_lcr_short_custom_cable_compensation`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.perform_lcr_short_custom_cable_compensation`


query_in_compliance
-------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: query_in_compliance()

            Queries the specified output device to determine if it is operating at
            the `compliance <REPLACE_DRIVER_SPECIFIC_URL_2(compliance)>`__ limit.

            The compliance limit is the current limit when the output method is
            set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`. If the output is operating at the
            compliance limit, the output reaches the current limit before the
            desired voltage level. Refer to the :py:meth:`nidcpower.Session.ConfigureOutputFunction`
            method and the :py:meth:`nidcpower.Session.ConfigureCurrentLimit` method for more
            information about output method and current limit, respectively.

            The compliance limit is the voltage limit when the output method is
            set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`. If the output is operating at the
            compliance limit, the output reaches the voltage limit before the
            desired current level. Refer to the :py:meth:`nidcpower.Session.ConfigureOutputFunction`
            method and the :py:meth:`nidcpower.Session.ConfigureVoltageLimit` method for more
            information about output method and voltage limit, respectively.

            **Related Topics:**

            `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].query_in_compliance`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.query_in_compliance`


            :rtype: bool
            :return:


                    Returns whether the device output channel is in compliance.

                    



query_latched_output_cutoff_state
---------------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: query_latched_output_cutoff_state(output_cutoff_reason)

            Discovers if an output cutoff limit was exceeded for the specified reason. When an output cutoff is engaged, the output of the channel(s) is disconnected.
            If a limit was exceeded, the state is latched until you clear it with the :py:meth:`nidcpower.Session.clear_latched_output_cutoff_state` method or the :py:meth:`nidcpower.Session.reset` method.

            outputCutoffReason specifies the conditions for which an output is disconnected.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].query_latched_output_cutoff_state`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.query_latched_output_cutoff_state`


            :param output_cutoff_reason:


                Specifies which output cutoff conditions to query.

                +---------------------------------------------------------------+--------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.ALL`                  | Any output cutoff condition was met                                                  |
                +---------------------------------------------------------------+--------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_OUTPUT_HIGH`  | The output exceeded the high cutoff limit for voltage output                         |
                +---------------------------------------------------------------+--------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_OUTPUT_LOW`   | The output fell below the low cutoff limit for voltage output                        |
                +---------------------------------------------------------------+--------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.CURRENT_MEASURE_HIGH` | The measured current exceeded the high cutoff limit for current output               |
                +---------------------------------------------------------------+--------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.CURRENT_MEASURE_LOW`  | The measured current fell below the low cutoff limit for current output              |
                +---------------------------------------------------------------+--------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_CHANGE_HIGH`  | The voltage slew rate increased beyond the positive change cutoff for voltage output |
                +---------------------------------------------------------------+--------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_CHANGE_LOW`   | The voltage slew rate decreased beyond the negative change cutoff for voltage output |
                +---------------------------------------------------------------+--------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.CURRENT_CHANGE_HIGH`  | The current slew rate increased beyond the positive change cutoff for current output |
                +---------------------------------------------------------------+--------------------------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputCutoffReason.CURRENT_CHANGE_LOW`   | The current slew rate decreased beyond the negative change cutoff for current output |
                +---------------------------------------------------------------+--------------------------------------------------------------------------------------+


            :type output_cutoff_reason: :py:data:`nidcpower.OutputCutoffReason`

            :rtype: bool
            :return:


                    Specifies whether an output cutoff has engaged.

                    +-------+------------------------------------------------------------------------------+
                    | True  | An output cutoff has engaged for the conditions in **output cutoff reason**. |
                    +-------+------------------------------------------------------------------------------+
                    | False | No output cutoff has engaged.                                                |
                    +-------+------------------------------------------------------------------------------+



query_max_current_limit
-----------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: query_max_current_limit(voltage_level)

            Queries the maximum current limit on an output channel if the output
            channel is set to the specified **voltageLevel**.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].query_max_current_limit`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.query_max_current_limit`


            :param voltage_level:


                Specifies the voltage level to use when calculating the
                **maxCurrentLimit**.

                


            :type voltage_level: float

            :rtype: float
            :return:


                    Returns the maximum current limit that can be set with the specified
                    **voltageLevel**.

                    



query_max_voltage_level
-----------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: query_max_voltage_level(current_limit)

            Queries the maximum voltage level on an output channel if the output
            channel is set to the specified **currentLimit**.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].query_max_voltage_level`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.query_max_voltage_level`


            :param current_limit:


                Specifies the current limit to use when calculating the
                **maxVoltageLevel**.

                


            :type current_limit: float

            :rtype: float
            :return:


                    Returns the maximum voltage level that can be set on an output channel
                    with the specified **currentLimit**.

                    



query_min_current_limit
-----------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: query_min_current_limit(voltage_level)

            Queries the minimum current limit on an output channel if the output
            channel is set to the specified **voltageLevel**.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].query_min_current_limit`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.query_min_current_limit`


            :param voltage_level:


                Specifies the voltage level to use when calculating the
                **minCurrentLimit**.

                


            :type voltage_level: float

            :rtype: float
            :return:


                    Returns the minimum current limit that can be set on an output channel
                    with the specified **voltageLevel**.

                    



query_output_state
------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: query_output_state(output_state)

            Queries the specified output channel to determine if the output channel
            is currently in the state specified by **outputState**.

            **Related Topics:**

            `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].query_output_state`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.query_output_state`


            :param output_state:


                Specifies the output state of the output channel that is being queried.
                **Defined Values**:

                +--------------------------------------------+-------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputStates.VOLTAGE` | The device maintains a constant voltage by adjusting the current. |
                +--------------------------------------------+-------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputStates.CURRENT` | The device maintains a constant current by adjusting the voltage. |
                +--------------------------------------------+-------------------------------------------------------------------+


            :type output_state: :py:data:`nidcpower.OutputStates`

            :rtype: bool
            :return:


                    Returns whether the device output channel is in the specified output
                    state.

                    



read_current_temperature
------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: read_current_temperature()

            Returns the current onboard **temperature**, in degrees Celsius, of the
            device.

            



            :rtype: float
            :return:


                    Returns the onboard **temperature**, in degrees Celsius, of the device.

                    



reset
-----

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: reset()

            Resets the specified channel(s) to a known state. This method disables power
            generation, resets session properties to their default values, commits
            the session properties, and leaves the session in the Uncommitted state.
            Refer to the `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
            more information about NI-DCPower software states.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].reset`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.reset`


reset_device
------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: reset_device()

            Resets the device to a known state. The method disables power
            generation, resets session properties to their default values, clears
            errors such as overtemperature and unexpected loss of auxiliary power,
            commits the session properties, and leaves the session in the
            Uncommitted state. This method also performs a hard reset on the
            device and driver software. This method has the same functionality as
            using reset in Measurement & Automation Explorer. Refer to the
            `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
            more information about NI-DCPower software states.

            This will also open the output relay on devices that have an output
            relay.

            



reset_with_defaults
-------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: reset_with_defaults()

            Resets the device to a known state. This method disables power
            generation, resets session properties to their default values, commits
            the session properties, and leaves the session in the
            `Running <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#running')>`__
            state. In addition to exhibiting the behavior of the :py:meth:`nidcpower.Session.reset`
            method, this method can assign user-defined default values for
            configurable properties from the IVI configuration.

            



self_cal
--------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: self_cal()

            Performs a self-calibration upon the specified channel(s).

            This method disables the output, performs several internal
            calculations, and updates calibration values. The updated calibration
            values are written to the device hardware if the
            :py:attr:`nidcpower.Session.self_calibration_persistence` property is set to
            :py:data:`~nidcpower.SelfCalibrationPersistence.WRITE_TO_EEPROM`. Refer to the
            :py:attr:`nidcpower.Session.self_calibration_persistence` property topic for more
            information about the settings for this property.

            When calling :py:meth:`nidcpower.Session.self_cal` with the PXIe-4162/4163,
            specify all channels of your PXIe-4162/4163 with the channelName input.
            You cannot self-calibrate a subset of PXIe-4162/4163 channels.

            Refer to the
            `Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__ topic for
            more information about this method.

            **Related Topics:**

            `Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].self_cal`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.self_cal`


self_test
---------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: self_test()

            Performs the device self-test routine and returns the test result(s).
            Calling this method implicitly calls the :py:meth:`nidcpower.Session.reset` method.

            When calling :py:meth:`nidcpower.Session.self_test` with the PXIe-4162/4163, specify all
            channels of your PXIe-4162/4163 with the channels input of
            :py:meth:`nidcpower.Session.__init__`. You cannot self test a subset of
            PXIe-4162/4163 channels.

            Raises `SelfTestError` on self test failure. Properties on exception object:

            - code - failure code from driver
            - message - status message from driver

            +----------------+-------------------+
            | Self-Test Code | Description       |
            +================+===================+
            | 0              | Self test passed. |
            +----------------+-------------------+
            | 1              | Self test failed. |
            +----------------+-------------------+



send_software_edge_trigger
--------------------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: send_software_edge_trigger(trigger)

            Asserts the specified trigger. This method can override an external
            edge trigger.

            **Related Topics:**

            `Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].send_software_edge_trigger`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.send_software_edge_trigger`


            :param trigger:


                Specifies which trigger to assert.
                **Defined Values:**

                +--------------------------------------------------------------+---------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_START_TRIGGER`            | Asserts the Start trigger.            |
                +--------------------------------------------------------------+---------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_SOURCE_TRIGGER`           | Asserts the Source trigger.           |
                +--------------------------------------------------------------+---------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_MEASURE_TRIGGER`          | Asserts the Measure trigger.          |
                +--------------------------------------------------------------+---------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER` | Asserts the Sequence Advance trigger. |
                +--------------------------------------------------------------+---------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_PULSE_TRIGGER`            | Asserts the Pulse trigger.            |
                +--------------------------------------------------------------+---------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_SHUTDOWN_TRIGGER`         | Asserts the Shutdown trigger.         |
                +--------------------------------------------------------------+---------------------------------------+

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger: :py:data:`nidcpower.SendSoftwareEdgeTriggerType`

set_sequence
------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: set_sequence(values, source_delays)

            Configures a series of voltage or current outputs and corresponding
            source delays. The source mode must be set to
            `Sequence <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ for this
            method to take effect.

            Refer to the `Configuring the Source
            Unit <REPLACE_DRIVER_SPECIFIC_URL_1(configuringthesourceunit)>`__ topic
            in the *NI DC Power Supplies and SMUs Help* for more information about
            how to configure your device.

            Use this method in the Uncommitted or Committed programming states.
            Refer to the `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
            the *NI DC Power Supplies and SMUs Help* for more information about
            NI-DCPower programming states.

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].set_sequence`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.set_sequence`


            :param values:


                Specifies the series of voltage levels or current levels, depending on
                the configured `output
                method <REPLACE_DRIVER_SPECIFIC_URL_1(programming_output)>`__.
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

unlock
------

    .. py:currentmodule:: nidcpower.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`nidcpower.Session.lock`. Refer to :py:meth:`nidcpower.Session.unlock` for additional
    information on session locks.



wait_for_event
--------------

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: wait_for_event(event_id, timeout=hightime.timedelta(seconds=10.0))

            Waits until the specified channel(s) have generated the specified event.

            The session monitors whether each type of event has occurred at least
            once since the last time this method or the :py:meth:`nidcpower.Session.initiate`
            method were called. If an event has only been generated once and you
            call this method successively, the method times out. Individual
            events must be generated between separate calls of this method.

            

            .. note:: This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.


            .. tip:: This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].wait_for_event`

                To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

                Example: :py:meth:`my_session.wait_for_event`


            :param event_id:


                Specifies which event to wait for.
                **Defined Values:**

                +-----------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT`             | Waits for the Source Complete event.             |
                +-----------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT`            | Waits for the Measure Complete event.            |
                +-----------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT` | Waits for the Sequence Iteration Complete event. |
                +-----------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT`        | Waits for the Sequence Engine Done event.        |
                +-----------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_PULSE_COMPLETE_EVENT`              | Waits for the Pulse Complete event.              |
                +-----------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT`     | Waits for the Ready for Pulse Trigger event.     |
                +-----------------------------------------------------------------------+--------------------------------------------------+

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type event_id: :py:data:`nidcpower.Event`
            :param timeout:


                Specifies the maximum time allowed for this method to complete, in
                seconds. If the method does not complete within this time interval,
                NI-DCPower returns an error.

                

                .. note:: When setting the timeout interval, ensure you take into account any
                    triggers so that the timeout interval is long enough for your
                    application.


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds


Properties
==========

active_advanced_sequence
------------------------

    .. py:attribute:: active_advanced_sequence

        Specifies the advanced sequence to configure or generate.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].active_advanced_sequence`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.active_advanced_sequence`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Active Advanced Sequence**
                - C Attribute: **NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE**

active_advanced_sequence_step
-----------------------------

    .. py:attribute:: active_advanced_sequence_step

        Specifies the advanced sequence step to configure.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].active_advanced_sequence_step`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.active_advanced_sequence_step`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Active Advanced Sequence Step**
                - C Attribute: **NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP**

actual_power_allocation
-----------------------

    .. py:attribute:: actual_power_allocation

        Returns the power, in watts, the device is sourcing on each active channel if the :py:attr:`nidcpower.Session.power_allocation_mode` property is set to :py:data:`~nidcpower.PowerAllocationMode.AUTOMATIC` or :py:data:`~nidcpower.PowerAllocationMode.MANUAL`.

         Valid Values: [0, device per-channel maximum power]

         Default Value: Refer to the Supported Properties by Device topic for the default value by device.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

             This property returns -1 when the :py:attr:`nidcpower.Session.power_allocation_mode` property is set to :py:data:`~nidcpower.PowerAllocationMode.DISABLED`.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].actual_power_allocation`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.actual_power_allocation`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Actual Power Allocation**
                - C Attribute: **NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION**

aperture_time
-------------

    .. py:attribute:: aperture_time

        Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by the :py:attr:`nidcpower.Session.aperture_time_units` property.
        Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about how to configure your measurements and for information about valid values.
        Default Value: 0.01666666 seconds



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].aperture_time`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.aperture_time`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Aperture Time**
                - C Attribute: **NIDCPOWER_ATTR_APERTURE_TIME**

aperture_time_auto_mode
-----------------------

    .. py:attribute:: aperture_time_auto_mode

        Automatically optimizes the measurement aperture time according to the actual current range when measurement autorange is enabled.
        Optimization accounts for power line frequency when the :py:attr:`nidcpower.Session.aperture_time_units` property is set to :py:data:`~nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES`.

        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE` and the :py:attr:`nidcpower.Session.autorange` property is enabled.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].aperture_time_auto_mode`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.aperture_time_auto_mode`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ApertureTimeAutoMode |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | channels                   |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Aperture Time Auto Mode**
                - C Attribute: **NIDCPOWER_ATTR_APERTURE_TIME_AUTO_MODE**

aperture_time_units
-------------------

    .. py:attribute:: aperture_time_units

        Specifies the units of the :py:attr:`nidcpower.Session.aperture_time` property for the channel configuration.
        Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about how to configure your measurements and for information about valid values.
        Default Value: :py:data:`~nidcpower.ApertureTimeUnits.SECONDS`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].aperture_time_units`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.aperture_time_units`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.ApertureTimeUnits |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | channels                |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Aperture Time Units**
                - C Attribute: **NIDCPOWER_ATTR_APERTURE_TIME_UNITS**

autorange
---------

    .. py:attribute:: autorange

        Specifies whether the hardware automatically selects the best range to measure the signal. Note the highest range the algorithm uses is dependent on the corresponding limit range property. The algorithm the hardware uses can be controlled using the :py:attr:`nidcpower.Session.autorange_aperture_time_mode` property.



        .. note:: Autoranging begins at module startup and remains active until the module is reconfigured or reset. This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].autorange`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.autorange`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Autorange**
                - C Attribute: **NIDCPOWER_ATTR_AUTORANGE**

autorange_aperture_time_mode
----------------------------

    .. py:attribute:: autorange_aperture_time_mode

        Specifies whether the aperture time used for the measurement autorange algorithm is determined automatically or customized using the :py:attr:`nidcpower.Session.autorange_minimum_aperture_time` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].autorange_aperture_time_mode`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.autorange_aperture_time_mode`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.AutorangeApertureTimeMode |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | channels                        |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Autorange Aperture Time Mode**
                - C Attribute: **NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE**

autorange_behavior
------------------

    .. py:attribute:: autorange_behavior

        Specifies the algorithm the hardware uses for measurement autoranging.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].autorange_behavior`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.autorange_behavior`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.AutorangeBehavior |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | channels                |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Autorange Behavior**
                - C Attribute: **NIDCPOWER_ATTR_AUTORANGE_BEHAVIOR**

autorange_maximum_delay_after_range_change
------------------------------------------

    .. py:attribute:: autorange_maximum_delay_after_range_change

        Balances between settling time and maximum measurement time by specifying the maximum time delay between when a range change occurs and when measurements resume.
        **Valid Values:**The minimum and maximum values of this property are hardware-dependent. PXIe-4135/4136/4137: 0 to 9 seconds PXIe-4138/4139: 0 to 9 seconds PXIe-4163: 0 to 0.1 seconds.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].autorange_maximum_delay_after_range_change`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.autorange_maximum_delay_after_range_change`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels                                                    |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Autorange Maximum Delay After Range Change**
                - C Attribute: **NIDCPOWER_ATTR_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE**

autorange_minimum_aperture_time
-------------------------------

    .. py:attribute:: autorange_minimum_aperture_time

        Specifies the measurement autorange aperture time used for the measurement autorange algorithm. The aperture time is specified in the units set by the :py:attr:`nidcpower.Session.autorange_minimum_aperture_time_units` property. This value will typically be smaller than the aperture time used for measurements.



        .. note:: For smaller ranges, the value is scaled up to account for noise. The factor used to scale the value is derived from the module capabilities. This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].autorange_minimum_aperture_time`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.autorange_minimum_aperture_time`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Autorange Minimum Aperture Time**
                - C Attribute: **NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME**

autorange_minimum_aperture_time_units
-------------------------------------

    .. py:attribute:: autorange_minimum_aperture_time_units

        Specifies the units of the :py:attr:`nidcpower.Session.autorange_minimum_aperture_time` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].autorange_minimum_aperture_time_units`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.autorange_minimum_aperture_time_units`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.ApertureTimeUnits |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | channels                |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Autorange Minimum Aperture Time Units**
                - C Attribute: **NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS**

autorange_minimum_current_range
-------------------------------

    .. py:attribute:: autorange_minimum_current_range

        Specifies the lowest range used during measurement autoranging. Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and minimize frequent and unpredictable range changes for noisy signals.



        .. note:: The maximum range used is the range that includes the value specified in the compliance limit property, :py:attr:`nidcpower.Session.voltage_limit_range` property or :py:attr:`nidcpower.Session.current_limit_range` property, depending on the selected :py:attr:`nidcpower.Session.output_function`. This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].autorange_minimum_current_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.autorange_minimum_current_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Autorange Minimum Current Range**
                - C Attribute: **NIDCPOWER_ATTR_AUTORANGE_MINIMUM_CURRENT_RANGE**

autorange_minimum_voltage_range
-------------------------------

    .. py:attribute:: autorange_minimum_voltage_range

        Specifies the lowest range used during measurement autoranging. The maximum range used is range that includes the value specified in the compliance limit property. Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and/or minimize thrashing between ranges for noisy signals.



        .. note:: The maximum range used is the range that includes the value specified in the compliance limit property, :py:attr:`nidcpower.Session.voltage_limit_range` property or :py:attr:`nidcpower.Session.current_limit_range` property, depending on the selected :py:attr:`nidcpower.Session.output_function`. This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].autorange_minimum_voltage_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.autorange_minimum_voltage_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Autorange Minimum Voltage Range**
                - C Attribute: **NIDCPOWER_ATTR_AUTORANGE_MINIMUM_VOLTAGE_RANGE**

autorange_threshold_mode
------------------------

    .. py:attribute:: autorange_threshold_mode

        Specifies thresholds used during autoranging to determine when range changing occurs.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].autorange_threshold_mode`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.autorange_threshold_mode`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------+
            | Characteristic        | Value                        |
            +=======================+==============================+
            | Datatype              | enums.AutorangeThresholdMode |
            +-----------------------+------------------------------+
            | Permissions           | read-write                   |
            +-----------------------+------------------------------+
            | Repeated Capabilities | channels                     |
            +-----------------------+------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Autorange Threshold Mode**
                - C Attribute: **NIDCPOWER_ATTR_AUTORANGE_THRESHOLD_MODE**

auto_zero
---------

    .. py:attribute:: auto_zero

        Specifies the auto-zero method to use on the device.
        Refer to the NI PXI-4132 Measurement Configuration and Timing and Auto Zero topics for more information about how to configure your measurements.
        Default Value: The default value for the NI PXI-4132 is :py:data:`~nidcpower.AutoZero.ON`. The default value for all other devices is :py:data:`~nidcpower.AutoZero.OFF`, which is the only supported value for these devices.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].auto_zero`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.auto_zero`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.AutoZero |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels       |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Auto Zero**
                - C Attribute: **NIDCPOWER_ATTR_AUTO_ZERO**

auxiliary_power_source_available
--------------------------------

    .. py:attribute:: auxiliary_power_source_available

        Indicates whether an auxiliary power source is connected to the device.
        A value of False may indicate that the auxiliary input fuse has blown. Refer to the Detecting Internal/Auxiliary Power topic in the NI DC Power Supplies and SMUs Help for more information about internal and auxiliary power.
        power source to generate power. Use the :py:attr:`nidcpower.Session.power_source_in_use` property to retrieve this information.



        .. note:: This property does not necessarily indicate if the device is using the auxiliary

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Advanced:Auxiliary Power Source Available**
                - C Attribute: **NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE**

cable_length
------------

    .. py:attribute:: cable_length

        Specifies how to apply cable compensation data for instruments that support LCR functionality.
        Supported instruments use cable compensation for the following operations:

        SMU mode: to stabilize DC current sourcing in the two smallest current ranges.
        LCR mode: to compensate for the effects of cabling on LCR measurements.

        For NI standard options, select the length of your NI cable to apply compensation data for a typical cable of that type.
        For custom options, choose the source of the custom cable compensation data. You must then generate the custom cable compensation data.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].cable_length`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.cable_length`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.CableLength |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | channels          |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:LCR:Cable Length**
                - C Attribute: **NIDCPOWER_ATTR_CABLE_LENGTH**

channel_count
-------------

    .. py:attribute:: channel_count

        Indicates the number of channels that NI-DCPower supports for the instrument that was chosen when the current session was opened. For channel-based properties, the IVI engine maintains a separate cache value for each channel.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Channel Count**
                - C Attribute: **NIDCPOWER_ATTR_CHANNEL_COUNT**

compliance_limit_symmetry
-------------------------

    .. py:attribute:: compliance_limit_symmetry

        Specifies whether compliance limits for current generation and voltage
        generation for the device are applied symmetrically about 0 V and 0 A or
        asymmetrically with respect to 0 V and 0 A.
        When set to :py:data:`~nidcpower.ComplianceLimitSymmetry.SYMMETRIC`, voltage limits and current limits are set
        using a single property with a positive value. The resulting range is
        bounded by this positive value and its opposite.
        When set to :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC`, you must separately set a limit high and a
        limit low using distinct properties.
        For asymmetric limits, the range bounded by the limit high and limit low
        must include zero.
        **Default Value:** Symmetric
        **Related Topics:**
        Compliance;
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].compliance_limit_symmetry`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.compliance_limit_symmetry`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------+
            | Characteristic        | Value                         |
            +=======================+===============================+
            | Datatype              | enums.ComplianceLimitSymmetry |
            +-----------------------+-------------------------------+
            | Permissions           | read-write                    |
            +-----------------------+-------------------------------+
            | Repeated Capabilities | channels                      |
            +-----------------------+-------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Compliance Limit Symmetry**
                - C Attribute: **NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY**

current_compensation_frequency
------------------------------

    .. py:attribute:: current_compensation_frequency

        The frequency at which a pole-zero pair is added to the system when the channel is in Constant Current mode.
        Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the :py:attr:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_compensation_frequency`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_compensation_frequency`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Current:Compensation Frequency**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY**

current_gain_bandwidth
----------------------

    .. py:attribute:: current_gain_bandwidth

        The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in Constant Current mode.
        Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the :py:attr:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_gain_bandwidth`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_gain_bandwidth`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Current:Gain Bandwidth**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH**

current_level
-------------

    .. py:attribute:: current_level

        Specifies the current level, in amps, that the device attempts to generate on the specified channel(s).
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        Valid Values: The valid values for this property are defined by the values to which the :py:attr:`nidcpower.Session.current_level_range` property is set.



        .. note:: The channel must be enabled for the specified current level to take effect. Refer to the :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_level`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Current Level**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL**

current_level_autorange
-----------------------

    .. py:attribute:: current_level_autorange

        Specifies whether NI-DCPower automatically selects the current level range based on the desired current level for the specified channels.
        If you set this property to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the :py:attr:`nidcpower.Session.current_level_range` property. If you change the :py:attr:`nidcpower.Session.current_level_autorange` property from :py:data:`~nidcpower.AutoZero.ON` to :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:attr:`nidcpower.Session.current_level_range` property was set to (or the default value if the property was never set) and uses that value as the current level range.
        Query the :py:attr:`nidcpower.Session.current_level_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method for information about which range NI-DCPower automatically selects.
        The :py:attr:`nidcpower.Session.current_level_autorange` property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        Default Value: :py:data:`~nidcpower.AutoZero.OFF`




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_level_autorange`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_level_autorange`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Current Level Autorange**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE**

current_level_range
-------------------

    .. py:attribute:: current_level_range

        Specifies the current level range, in amps, for the specified channel(s).
        The range defines the valid values to which you can set the current level. Use the :py:attr:`nidcpower.Session.current_level_autorange` property to enable automatic selection of the current level range.
        The :py:attr:`nidcpower.Session.current_level_range` property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        For valid ranges, refer to the specifications for your instrument.



        .. note:: The channel must be enabled for the specified current level range to take effect. Refer to the :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_level_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_level_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Current Level Range**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE**

current_limit
-------------

    .. py:attribute:: current_limit

        Specifies the current limit, in amps, that the output cannot exceed when generating the desired voltage level on the specified channel(s).
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE` and the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to :py:data:`~nidcpower.ComplianceLimitSymmetry.SYMMETRIC`.
        :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        Valid Values: The valid values for this property are defined by the values to which :py:attr:`nidcpower.Session.current_limit_range` property is set.



        .. note:: The channel must be enabled for the specified current limit to take effect. Refer to the :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_limit`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_limit`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Current Limit**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT**

current_limit_autorange
-----------------------

    .. py:attribute:: current_limit_autorange

        Specifies whether NI-DCPower automatically selects the current limit range based on the desired current limit for the specified channel(s).
        If you set this property to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the :py:attr:`nidcpower.Session.current_limit_range` property. If you change this property from :py:data:`~nidcpower.AutoZero.ON` to :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:attr:`nidcpower.Session.current_limit_range` property was set to (or the default value if the property was never set) and uses that value as the current limit range.
        Query the :py:attr:`nidcpower.Session.current_limit_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method for information about which range NI-DCPower automatically selects.
        The :py:attr:`nidcpower.Session.current_limit_autorange` property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        Default Value: :py:data:`~nidcpower.AutoZero.OFF`




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_limit_autorange`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_limit_autorange`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Current Limit Autorange**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE**

current_limit_behavior
----------------------

    .. py:attribute:: current_limit_behavior

        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_limit_behavior`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_limit_behavior`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_BEHAVIOR**

current_limit_high
------------------

    .. py:attribute:: current_limit_high

        Specifies the maximum current, in amps, that the output can produce when
        generating the desired voltage on the specified channel(s).
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        You must also specify a :py:attr:`nidcpower.Session.current_limit_low` to complete the asymmetric
        range.
        **Valid Values:** [1% of :py:attr:`nidcpower.Session.current_limit_range`, :py:attr:`nidcpower.Session.current_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_limit_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_limit_high`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Current Limit High**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH**

current_limit_low
-----------------

    .. py:attribute:: current_limit_low

        Specifies the minimum current, in amps, that the output can produce when
        generating the desired voltage on the specified channel(s).
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        You must also specify a :py:attr:`nidcpower.Session.current_limit_high` to complete the asymmetric
        range.
        **Valid Values:** [-:py:attr:`nidcpower.Session.current_limit_range`, -1% of :py:attr:`nidcpower.Session.current_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_limit_low`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_limit_low`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Current Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_LOW**

current_limit_range
-------------------

    .. py:attribute:: current_limit_range

        Specifies the current limit range, in amps, for the specified channel(s).
        The range defines the valid values to which you can set the current limit. Use the :py:attr:`nidcpower.Session.current_limit_autorange` property to enable automatic selection of the current limit range.
        The :py:attr:`nidcpower.Session.current_limit_range` property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        For valid ranges, refer to the specifications for your instrument.



        .. note:: The channel must be enabled for the specified current limit to take effect. Refer to the :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_limit_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_limit_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Current Limit Range**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE**

current_pole_zero_ratio
-----------------------

    .. py:attribute:: current_pole_zero_ratio

        The ratio of the pole frequency to the zero frequency when the channel is in Constant Current mode.
        Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the :py:attr:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].current_pole_zero_ratio`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.current_pole_zero_ratio`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Current:Pole-Zero Ratio**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO**

dc_noise_rejection
------------------

    .. py:attribute:: dc_noise_rejection

        Determines the relative weighting of samples in a measurement. Refer to the NI PXIe-4140/4141 DC Noise Rejection, NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic in the NI DC Power Supplies and SMUs Help for more information about noise rejection.
        Default Value: :py:data:`~nidcpower.TransientResponse.NORMAL`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].dc_noise_rejection`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.dc_noise_rejection`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.DCNoiseRejection |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | channels               |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:DC Noise Rejection**
                - C Attribute: **NIDCPOWER_ATTR_DC_NOISE_REJECTION**

digital_edge_measure_trigger_input_terminal
-------------------------------------------

    .. py:attribute:: digital_edge_measure_trigger_input_terminal

        Specifies the input terminal for the Measure trigger. This property is used only when the :py:attr:`nidcpower.Session.measure_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
        for this property.
        You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
        Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].digital_edge_measure_trigger_input_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.digital_edge_measure_trigger_input_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Measure Trigger:Digital Edge:Input Terminal**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL**

digital_edge_pulse_trigger_input_terminal
-----------------------------------------

    .. py:attribute:: digital_edge_pulse_trigger_input_terminal

        Specifies the input terminal for the Pulse trigger. This property is used only when the :py:attr:`nidcpower.Session.pulse_trigger_type` property is set to digital edge.
        You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
        Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].digital_edge_pulse_trigger_input_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.digital_edge_pulse_trigger_input_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Pulse Trigger:Digital Edge:Input Terminal**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL**

digital_edge_sequence_advance_trigger_input_terminal
----------------------------------------------------

    .. py:attribute:: digital_edge_sequence_advance_trigger_input_terminal

        Specifies the input terminal for the Sequence Advance trigger. Use this property only when the :py:attr:`nidcpower.Session.sequence_advance_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
        the NI DC Power Supplies and SMUs Help for information about supported devices.
        You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
        Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].digital_edge_sequence_advance_trigger_input_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.digital_edge_sequence_advance_trigger_input_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL**

digital_edge_shutdown_trigger_input_terminal
--------------------------------------------

    .. py:attribute:: digital_edge_shutdown_trigger_input_terminal

        Specifies the input terminal for the Shutdown trigger. This property is used only when the :py:attr:`nidcpower.Session.shutdown_trigger_type` property is set to digital edge.
        You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
        Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].digital_edge_shutdown_trigger_input_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.digital_edge_shutdown_trigger_input_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Shutdown Trigger:Digital Edge:Input Terminal**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL**

digital_edge_source_trigger_input_terminal
------------------------------------------

    .. py:attribute:: digital_edge_source_trigger_input_terminal

        Specifies the input terminal for the Source trigger. Use this property only when the :py:attr:`nidcpower.Session.source_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
        You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
        Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].digital_edge_source_trigger_input_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.digital_edge_source_trigger_input_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Source Trigger:Digital Edge:Input Terminal**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL**

digital_edge_start_trigger_input_terminal
-----------------------------------------

    .. py:attribute:: digital_edge_start_trigger_input_terminal

        Specifies the input terminal for the Start trigger. Use this property only when the :py:attr:`nidcpower.Session.start_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
        You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
        Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].digital_edge_start_trigger_input_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.digital_edge_start_trigger_input_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start Trigger:Digital Edge:Input Terminal**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL**

driver_setup
------------

    .. py:attribute:: driver_setup

        Indicates the Driver Setup string that you specified when initializing the driver.
        Some cases exist where you must specify the instrument driver options at initialization time. An example of this case is specifying a particular device model from among a family of devices that the driver supports. This property is useful when simulating a device. You can specify the driver-specific options through the DriverSetup keyword in the optionsString parameter in the :py:meth:`nidcpower.Session.__init__` method or through the IVI Configuration Utility.
        You can specify driver-specific options through the DriverSetup keyword in the optionsString parameter in the :py:meth:`nidcpower.Session.__init__` method. If you do not specify a Driver Setup string, this property returns an empty string.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Driver Setup**
                - C Attribute: **NIDCPOWER_ATTR_DRIVER_SETUP**

exported_measure_trigger_output_terminal
----------------------------------------

    .. py:attribute:: exported_measure_trigger_output_terminal

        Specifies the output terminal for exporting the Measure trigger.
        Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].exported_measure_trigger_output_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.exported_measure_trigger_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Measure Trigger:Export Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL**

exported_pulse_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_pulse_trigger_output_terminal

        Specifies the output terminal for exporting the Pulse trigger.
        Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].exported_pulse_trigger_output_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.exported_pulse_trigger_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Pulse Trigger:Export Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL**

exported_sequence_advance_trigger_output_terminal
-------------------------------------------------

    .. py:attribute:: exported_sequence_advance_trigger_output_terminal

        Specifies the output terminal for exporting the Sequence Advance trigger.
        Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].exported_sequence_advance_trigger_output_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.exported_sequence_advance_trigger_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Sequence Advance Trigger:Export Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL**

exported_source_trigger_output_terminal
---------------------------------------

    .. py:attribute:: exported_source_trigger_output_terminal

        Specifies the output terminal for exporting the Source trigger.
        Refer to the Device Routes tab in MAX for a list of the terminals available on your device.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].exported_source_trigger_output_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.exported_source_trigger_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Source Trigger:Export Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_start_trigger_output_terminal

        Specifies the output terminal for exporting the Start trigger.
        Refer to the Device Routes tab in Measurement & Automation Explorer (MAX) for a list of the terminals available on your device.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].exported_start_trigger_output_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.exported_start_trigger_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start Trigger:Export Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

fetch_backlog
-------------

    .. py:attribute:: fetch_backlog

        Returns the number of measurements acquired that have not been fetched yet.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].fetch_backlog`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.fetch_backlog`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Fetch Backlog**
                - C Attribute: **NIDCPOWER_ATTR_FETCH_BACKLOG**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        Contains the firmware revision information for the device you are currently using.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].instrument_firmware_revision`

            To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.instrument_firmware_revision`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | str         |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | instruments |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Firmware Revision**
                - C Attribute: **NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        Contains the name of the manufacturer for the device you are currently using.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].instrument_manufacturer`

            To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.instrument_manufacturer`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | str         |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | instruments |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Manufacturer**
                - C Attribute: **NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER**

instrument_mode
---------------

    .. py:attribute:: instrument_mode

        Specifies the mode of operation for an instrument channel for instruments that support multiple modes.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].instrument_mode`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.instrument_mode`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.InstrumentMode |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | channels             |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Instrument Mode**
                - C Attribute: **NIDCPOWER_ATTR_INSTRUMENT_MODE**

instrument_model
----------------

    .. py:attribute:: instrument_model

        Contains the model number or name of the device that you are currently using.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].instrument_model`

            To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.instrument_model`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | str         |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | instruments |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Model**
                - C Attribute: **NIDCPOWER_ATTR_INSTRUMENT_MODEL**

interlock_input_open
--------------------

    .. py:attribute:: interlock_input_open

        Indicates whether the safety interlock circuit is open.
        Refer to the Safety Interlock topic in the NI DC Power Supplies and SMUs Help for more information about the safety interlock circuit.
        about supported devices.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].interlock_input_open`

            To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.interlock_input_open`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | bool        |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | instruments |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Advanced:Interlock Input Open**
                - C Attribute: **NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Indicates the resource descriptor NI-DCPower uses to identify the physical device.
        If you initialize NI-DCPower with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration utility.
        If you initialize NI-DCPower with the resource descriptor, this property contains that value.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Resource Descriptor**
                - C Attribute: **NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR**

isolation_state
---------------

    .. py:attribute:: isolation_state

        Defines whether the channel is isolated.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].isolation_state`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.isolation_state`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Advanced:Isolation State**
                - C Attribute: **NIDCPOWER_ATTR_ISOLATION_STATE**

lcr_actual_load_reactance
-------------------------

    .. py:attribute:: lcr_actual_load_reactance

        Specifies the actual reactance, in ohms, of the load used for load LCR compensation.
        This property applies when :py:attr:`nidcpower.Session.lcr_open_short_load_compensation_data_source` is set to :py:data:`~nidcpower.LCROpenShortLoadCompensationDataSource.AS_DEFINED`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_actual_load_reactance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_actual_load_reactance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:LCR Actual Load Reactance**
                - C Attribute: **NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_REACTANCE**

lcr_actual_load_resistance
--------------------------

    .. py:attribute:: lcr_actual_load_resistance

        Specifies the actual resistance, in ohms, of the load used for load LCR compensation.
        This property applies when :py:attr:`nidcpower.Session.lcr_open_short_load_compensation_data_source` is set to :py:data:`~nidcpower.LCROpenShortLoadCompensationDataSource.AS_DEFINED`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_actual_load_resistance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_actual_load_resistance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:LCR Actual Load Resistance**
                - C Attribute: **NIDCPOWER_ATTR_LCR_ACTUAL_LOAD_RESISTANCE**

lcr_automatic_level_control
---------------------------

    .. py:attribute:: lcr_automatic_level_control

        Specifies whether the channel actively attempts to maintain a constant test voltage or current across the DUT for LCR measurements.
        The use of voltage or current depends on the test signal you configure with the :py:attr:`nidcpower.Session.lcr_stimulus_function` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_automatic_level_control`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_automatic_level_control`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:AC Stimulus:Automatic Level Control**
                - C Attribute: **NIDCPOWER_ATTR_LCR_AUTOMATIC_LEVEL_CONTROL**

lcr_current_amplitude
---------------------

    .. py:attribute:: lcr_current_amplitude

        Specifies the amplitude, in amps RMS, of the AC current test signal applied to the DUT for LCR measurements.
        This property applies when the :py:attr:`nidcpower.Session.lcr_stimulus_function` property is set to :py:data:`~nidcpower.LCRStimulusFunction.CURRENT`.

        Valid Values: 7.08e-9 A RMS to 0.707 A RMS

        Instrument specifications affect the valid values you can program. Refer to the specifications for your instrument for more information.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_current_amplitude`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_current_amplitude`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:AC Stimulus:Current Amplitude**
                - C Attribute: **NIDCPOWER_ATTR_LCR_CURRENT_AMPLITUDE**

lcr_custom_measurement_time
---------------------------

    .. py:attribute:: lcr_custom_measurement_time

        Specifies the LCR measurement aperture time for a channel, in seconds,
        when the :py:attr:`nidcpower.Session.lcr_measurement_time` property is set to :py:data:`~nidcpower.LCRMeasurementTime.CUSTOM`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_custom_measurement_time`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_custom_measurement_time`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels                                                    |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Custom Measurement Time**
                - C Attribute: **NIDCPOWER_ATTR_LCR_CUSTOM_MEASUREMENT_TIME**

lcr_dc_bias_automatic_level_control
-----------------------------------

    .. py:attribute:: lcr_dc_bias_automatic_level_control

        Specifies whether the channel actively maintains a constant DC bias voltage or current across the DUT for LCR measurements.
        To use this property, you must configure a DC bias by 1) selecting an :py:attr:`nidcpower.Session.lcr_dc_bias_source` and 2) depending on the DC bias source you choose, setting either the :py:attr:`nidcpower.Session.lcr_dc_bias_voltage_level` or :py:attr:`nidcpower.Session.lcr_dc_bias_current_level`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_dc_bias_automatic_level_control`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_dc_bias_automatic_level_control`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:DC Bias:Automatic Level Control**
                - C Attribute: **NIDCPOWER_ATTR_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL**

lcr_dc_bias_current_level
-------------------------

    .. py:attribute:: lcr_dc_bias_current_level

        Specifies the DC bias current level, in amps, when the :py:attr:`nidcpower.Session.lcr_dc_bias_source` property is set to :py:data:`~nidcpower.LCRDCBiasSource.CURRENT`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_dc_bias_current_level`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_dc_bias_current_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:DC Bias:Current Level**
                - C Attribute: **NIDCPOWER_ATTR_LCR_DC_BIAS_CURRENT_LEVEL**

lcr_dc_bias_source
------------------

    .. py:attribute:: lcr_dc_bias_source

        Specifies how to apply DC bias for LCR measurements.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_dc_bias_source`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_dc_bias_source`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.LCRDCBiasSource |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | channels              |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:DC Bias:Source**
                - C Attribute: **NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE**

lcr_dc_bias_voltage_level
-------------------------

    .. py:attribute:: lcr_dc_bias_voltage_level

        Specifies the DC bias voltage level, in volts, when the :py:attr:`nidcpower.Session.lcr_dc_bias_source` property is set to :py:data:`~nidcpower.LCRDCBiasSource.VOLTAGE`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_dc_bias_voltage_level`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_dc_bias_voltage_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:DC Bias:Voltage Level**
                - C Attribute: **NIDCPOWER_ATTR_LCR_DC_BIAS_VOLTAGE_LEVEL**

lcr_frequency
-------------

    .. py:attribute:: lcr_frequency

        Specifies the frequency of the AC test signal applied to the DUT for LCR measurements.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_frequency`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_frequency`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:AC Stimulus:Frequency**
                - C Attribute: **NIDCPOWER_ATTR_LCR_FREQUENCY**

lcr_impedance_range
-------------------

    .. py:attribute:: lcr_impedance_range

        Specifies the impedance range the channel uses for LCR measurements.

        Valid Values: 0 ohms to +inf ohms

        Default Value: Search ni.com for Supported Properties by Device for the default value by instrument.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_impedance_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_impedance_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Impedance Range:Impedance Range**
                - C Attribute: **NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE**

lcr_impedance_range_source
--------------------------

    .. py:attribute:: lcr_impedance_range_source

        Specifies how the impedance range for LCR measurements is determined.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_impedance_range_source`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_impedance_range_source`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------+
            | Characteristic        | Value                         |
            +=======================+===============================+
            | Datatype              | enums.LCRImpedanceRangeSource |
            +-----------------------+-------------------------------+
            | Permissions           | read-write                    |
            +-----------------------+-------------------------------+
            | Repeated Capabilities | channels                      |
            +-----------------------+-------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Impedance Range:Advanced:Impedance Range Source**
                - C Attribute: **NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE**

lcr_load_capacitance
--------------------

    .. py:attribute:: lcr_load_capacitance

        Specifies the load capacitance, in farads and assuming a series model, of the DUT in order to compute the impedance range when the :py:attr:`nidcpower.Session.lcr_impedance_range_source` property is set to :py:data:`~nidcpower.LCRImpedanceRangeSource.LOAD_CONFIGURATION`.

        Valid values: (0 farads, +inf farads)
        0 is a special value that signifies +inf farads.

        Default Value: Search ni.com for Supported Properties by Device for the default value by instrument



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_load_capacitance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_load_capacitance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Impedance Range:Advanced:Load Capacitance**
                - C Attribute: **NIDCPOWER_ATTR_LCR_LOAD_CAPACITANCE**

lcr_load_compensation_enabled
-----------------------------

    .. py:attribute:: lcr_load_compensation_enabled

        Specifies whether to apply load LCR compensation data to LCR measurements.
        Both the :py:attr:`nidcpower.Session.lcr_open_compensation_enabled` and :py:attr:`nidcpower.Session.lcr_short_compensation_enabled` properties must be set to True in order to set this property to True.

        Use the :py:attr:`nidcpower.Session.lcr_open_short_load_compensation_data_source` property to define where the load compensation data that is applied to LCR measurements comes from.



        .. note:: Load compensation data are applied only for those specific frequencies you define with :py:meth:`nidcpower.Session.perform_lcr_load_compensation`;
            load compensation is not interpolated from the specific frequencies you define and applied to other frequencies.

            This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_load_compensation_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_load_compensation_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:Load:Enabled**
                - C Attribute: **NIDCPOWER_ATTR_LCR_LOAD_COMPENSATION_ENABLED**

lcr_load_inductance
-------------------

    .. py:attribute:: lcr_load_inductance

        Specifies the load inductance, in henrys and assuming a series model, of the DUT in order to compute the impedance range when the :py:attr:`nidcpower.Session.lcr_impedance_range_source` property is set to :py:data:`~nidcpower.LCRImpedanceRangeSource.LOAD_CONFIGURATION`.

        Valid values: [0 henrys, +inf henrys)

        Default Value: Search ni.com for Supported Properties by Device for the default value by instrument



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_load_inductance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_load_inductance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Impedance Range:Advanced:Load Inductance**
                - C Attribute: **NIDCPOWER_ATTR_LCR_LOAD_INDUCTANCE**

lcr_load_resistance
-------------------

    .. py:attribute:: lcr_load_resistance

        Specifies the load resistance, in ohms and assuming a series model, of the DUT in order to compute the impedance range when the :py:attr:`nidcpower.Session.lcr_impedance_range_source` property is set to :py:data:`~nidcpower.LCRImpedanceRangeSource.LOAD_CONFIGURATION`.

        Valid values: [0 ohms, +inf ohms)

        Default Value: Search ni.com for Supported Properties by Device for the default value by instrument



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_load_resistance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_load_resistance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Impedance Range:Advanced:Load Resistance**
                - C Attribute: **NIDCPOWER_ATTR_LCR_LOAD_RESISTANCE**

lcr_measured_load_reactance
---------------------------

    .. py:attribute:: lcr_measured_load_reactance

        Specifies the reactance, in ohms, of the load used for load LCR compensation as measured by the instrument.
        This property applies when :py:attr:`nidcpower.Session.lcr_open_short_load_compensation_data_source` is set to :py:data:`~nidcpower.LCROpenShortLoadCompensationDataSource.AS_DEFINED`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_measured_load_reactance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_measured_load_reactance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:Load:Measured Reactance**
                - C Attribute: **NIDCPOWER_ATTR_LCR_MEASURED_LOAD_REACTANCE**

lcr_measured_load_resistance
----------------------------

    .. py:attribute:: lcr_measured_load_resistance

        Specifies the resistance, in ohms, of the load used for load LCR compensation as measured by the instrument.
        This property applies when :py:attr:`nidcpower.Session.lcr_open_short_load_compensation_data_source` is set to :py:data:`~nidcpower.LCROpenShortLoadCompensationDataSource.AS_DEFINED`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_measured_load_resistance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_measured_load_resistance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:Load:Measured Resistance**
                - C Attribute: **NIDCPOWER_ATTR_LCR_MEASURED_LOAD_RESISTANCE**

lcr_measurement_time
--------------------

    .. py:attribute:: lcr_measurement_time

        Selects a general aperture time profile for LCR measurements. The actual duration of each profile depends on the frequency of the LCR test signal.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_measurement_time`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_measurement_time`

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.LCRMeasurementTime |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | channels                 |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Measurement Time**
                - C Attribute: **NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME**

lcr_open_compensation_enabled
-----------------------------

    .. py:attribute:: lcr_open_compensation_enabled

        Specifies whether to apply open LCR compensation data to LCR measurements.
        Use the :py:attr:`nidcpower.Session.lcr_open_short_load_compensation_data_source` property to define where the open compensation data that is applied to LCR measurements comes from.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_open_compensation_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_open_compensation_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:Open:Enabled**
                - C Attribute: **NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED**

lcr_open_conductance
--------------------

    .. py:attribute:: lcr_open_conductance

        Specifies the conductance, in siemens, of the circuit used for open LCR compensation.
        This property applies when :py:attr:`nidcpower.Session.lcr_open_short_load_compensation_data_source` is set to :py:data:`~nidcpower.LCROpenShortLoadCompensationDataSource.AS_DEFINED`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_open_conductance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_open_conductance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:Open:Conductance**
                - C Attribute: **NIDCPOWER_ATTR_LCR_OPEN_CONDUCTANCE**

lcr_open_short_load_compensation_data_source
--------------------------------------------

    .. py:attribute:: lcr_open_short_load_compensation_data_source

        Specifies the source of the LCR compensation data NI-DCPower applies to LCR measurements.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_open_short_load_compensation_data_source`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_open_short_load_compensation_data_source`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------------------+
            | Characteristic        | Value                                        |
            +=======================+==============================================+
            | Datatype              | enums.LCROpenShortLoadCompensationDataSource |
            +-----------------------+----------------------------------------------+
            | Permissions           | read-write                                   |
            +-----------------------+----------------------------------------------+
            | Repeated Capabilities | channels                                     |
            +-----------------------+----------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:LCR Open/Short/Load Compensation Data Source**
                - C Attribute: **NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE**

lcr_open_susceptance
--------------------

    .. py:attribute:: lcr_open_susceptance

        Specifies the susceptance, in siemens, of the circuit used for open LCR compensation.
        This property applies when :py:attr:`nidcpower.Session.lcr_open_short_load_compensation_data_source` is set to :py:data:`~nidcpower.LCROpenShortLoadCompensationDataSource.AS_DEFINED`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_open_susceptance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_open_susceptance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:Open:Susceptance**
                - C Attribute: **NIDCPOWER_ATTR_LCR_OPEN_SUSCEPTANCE**

lcr_short_compensation_enabled
------------------------------

    .. py:attribute:: lcr_short_compensation_enabled

        Specifies whether to apply short LCR compensation data to LCR measurements.
        Use the :py:attr:`nidcpower.Session.lcr_open_short_load_compensation_data_source` property to define where the short compensation data that is applied to LCR measurements comes from.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_short_compensation_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_short_compensation_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:Short:Enabled**
                - C Attribute: **NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED**

lcr_short_custom_cable_compensation_enabled
-------------------------------------------

    .. py:attribute:: lcr_short_custom_cable_compensation_enabled

        Defines how to apply short custom cable compensation in LCR mode when :py:attr:`nidcpower.Session.cable_length` property is set to :py:data:`~nidcpower.CableLength.CUSTOM_ONBOARD_STORAGE` or :py:data:`~nidcpower.CableLength.CUSTOM_AS_CONFIGURED`.

        LCR custom cable compensation uses compensation data for both an open and short configuration.
        For open custom cable compensation, you must supply your own data from a call to :py:meth:`nidcpower.Session.perform_lcr_open_custom_cable_compensation`.
        For short custom cable compensation, you can supply your own data from a call to :py:meth:`nidcpower.Session.perform_lcr_short_custom_cable_compensation` or NI-DCPower can apply a default set of short compensation data.

        +-------+----------------------------------------------------------------------------------------------------------------------------------+
        | False | Uses default short compensation data.                                                                                            |
        +-------+----------------------------------------------------------------------------------------------------------------------------------+
        | True  | Uses short custom cable compensation data generated by :py:meth:`nidcpower.Session.perform_lcr_short_custom_cable_compensation`. |
        +-------+----------------------------------------------------------------------------------------------------------------------------------+

        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_short_custom_cable_compensation_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_short_custom_cable_compensation_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:LCR Short Custom Cable Compensation Enabled**
                - C Attribute: **NIDCPOWER_ATTR_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED**

lcr_short_reactance
-------------------

    .. py:attribute:: lcr_short_reactance

        Specifies the reactance, in ohms, of the circuit used for short LCR compensation.
        This property applies when :py:attr:`nidcpower.Session.lcr_open_short_load_compensation_data_source` is set to :py:data:`~nidcpower.LCROpenShortLoadCompensationDataSource.AS_DEFINED`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_short_reactance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_short_reactance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:Short:Reactance**
                - C Attribute: **NIDCPOWER_ATTR_LCR_SHORT_REACTANCE**

lcr_short_resistance
--------------------

    .. py:attribute:: lcr_short_resistance

        Specifies the resistance, in ohms, of the circuit used for short LCR compensation.
        This property applies when :py:attr:`nidcpower.Session.lcr_open_short_load_compensation_data_source` is set to :py:data:`~nidcpower.LCROpenShortLoadCompensationDataSource.AS_DEFINED`.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_short_resistance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_short_resistance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Compensation:Short:Resistance**
                - C Attribute: **NIDCPOWER_ATTR_LCR_SHORT_RESISTANCE**

lcr_source_delay_mode
---------------------

    .. py:attribute:: lcr_source_delay_mode

        For instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the source delay or applies a source delay you set manually.

        You can return the source delay duration for either option by reading :py:attr:`nidcpower.Session.source_delay`.

        When you use this property to manually set the source delay, it is possible to set source delays short enough to unbalance the bridge and affect measurement accuracy. LCR measurement methods report whether the bridge is unbalanced.

        Default Value: :py:data:`~nidcpower.LCRSourceDelayMode.AUTOMATIC`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_source_delay_mode`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_source_delay_mode`

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.LCRSourceDelayMode |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | channels                 |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:Source Delay Mode**
                - C Attribute: **NIDCPOWER_ATTR_LCR_SOURCE_DELAY_MODE**

lcr_stimulus_function
---------------------

    .. py:attribute:: lcr_stimulus_function

        Specifies the type of test signal to apply to the DUT for LCR measurements.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_stimulus_function`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_stimulus_function`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | enums.LCRStimulusFunction |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | channels                  |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:AC Stimulus:Function**
                - C Attribute: **NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION**

lcr_voltage_amplitude
---------------------

    .. py:attribute:: lcr_voltage_amplitude

        Specifies the amplitude, in volts RMS, of the AC voltage test signal applied to the DUT for LCR measurements.
        This property applies when the :py:attr:`nidcpower.Session.lcr_stimulus_function` property is set to :py:data:`~nidcpower.LCRStimulusFunction.VOLTAGE`.

        Valid Values: 7.08e-4 V RMS to 7.07 V RMS

        Instrument specifications affect the valid values you can program. Refer to the specifications for your instrument for more information.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].lcr_voltage_amplitude`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.lcr_voltage_amplitude`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **LCR:AC Stimulus:Voltage Amplitude**
                - C Attribute: **NIDCPOWER_ATTR_LCR_VOLTAGE_AMPLITUDE**

logical_name
------------

    .. py:attribute:: logical_name

        Contains the logical name you specified when opening the current IVI session.
        You can pass a logical name to the :py:meth:`nidcpower.Session.__init__` method. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a method section in the IVI Configuration file. The method section specifies a physical device and initial user options.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NIDCPOWER_ATTR_LOGICAL_NAME**

measure_buffer_size
-------------------

    .. py:attribute:: measure_buffer_size

        Specifies the number of samples that the active channel measurement buffer can hold.
        The default value is the maximum number of samples that a device is capable of recording in one second.
        Valid Values: 1000 to 2147483647
        Default Value: Varies by device. Refer to Supported Properties by Device topic in the NI DC Power Supplies and SMUs Help for more information about default values.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].measure_buffer_size`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.measure_buffer_size`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Measure Buffer Size**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE**

measure_complete_event_delay
----------------------------

    .. py:attribute:: measure_complete_event_delay

        Specifies the amount of time to delay the generation of the Measure Complete event, in seconds.
        Valid Values: 0 to 167 seconds
        Default Value: The NI PXI-4132 and NI PXIe-4140/4141/4142/4143/4144/4145/4154 supports values from  0 seconds to 167 seconds.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].measure_complete_event_delay`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.measure_complete_event_delay`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels                                                    |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Measure Complete Event:Event Delay**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY**

measure_complete_event_output_terminal
--------------------------------------

    .. py:attribute:: measure_complete_event_output_terminal

        Specifies the output terminal for exporting the Measure Complete event.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].measure_complete_event_output_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.measure_complete_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Measure Complete Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL**

measure_complete_event_pulse_polarity
-------------------------------------

    .. py:attribute:: measure_complete_event_pulse_polarity

        Specifies the behavior of the Measure Complete event.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].measure_complete_event_pulse_polarity`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.measure_complete_event_pulse_polarity`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.Polarity |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels       |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Measure Complete Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY**

measure_complete_event_pulse_width
----------------------------------

    .. py:attribute:: measure_complete_event_pulse_width

        Specifies the width of the Measure Complete event, in seconds.
        The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.
        The maximum event pulse width value for all devices is 1.6 microseconds.
        Valid Values: 1.5e-7 to 1.6e-6
        Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].measure_complete_event_pulse_width`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.measure_complete_event_pulse_width`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Measure Complete Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH**

measure_record_delta_time
-------------------------

    .. py:attribute:: measure_record_delta_time

        Queries the amount of time, in seconds, between between the start of two consecutive measurements in a measure record. Only query this property after the desired measurement settings are committed.
        two measurements and the rest would differ.



        .. note:: This property is not available when Auto Zero is configured to Once because the amount of time between the first


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].measure_record_delta_time`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.measure_record_delta_time`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read only                                                   |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels                                                    |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Measure Record Delta Time**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME**

measure_record_length
---------------------

    .. py:attribute:: measure_record_length

        Specifies how many measurements compose a measure record. When this property is set to a value greater than 1, the :py:attr:`nidcpower.Session.measure_when` property must be set to :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE` or :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`.
        Valid Values: 1 to 16,777,216
        Default Value: 1



        .. note:: This property is not available in a session involving multiple channels.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].measure_record_length`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.measure_record_length`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Measure Record Length**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH**

measure_record_length_is_finite
-------------------------------

    .. py:attribute:: measure_record_length_is_finite

        Specifies whether to take continuous measurements. Call the :py:meth:`nidcpower.Session.abort` method to stop continuous measurements. When this property is set to False and the :py:attr:`nidcpower.Session.source_mode` property is set to :py:data:`~nidcpower.SourceMode.SINGLE_POINT`, the :py:attr:`nidcpower.Session.measure_when` property must be set to :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE` or :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`. When this property is set to False and the :py:attr:`nidcpower.Session.source_mode` property is set to :py:data:`~nidcpower.SourceMode.SEQUENCE`, the :py:attr:`nidcpower.Session.measure_when` property must be set to :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`.
        Default Value: True



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device. This property is not available in a session involving multiple channels.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].measure_record_length_is_finite`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.measure_record_length_is_finite`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Measure Record Length Is Finite**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE**

measure_trigger_type
--------------------

    .. py:attribute:: measure_trigger_type

        Specifies the behavior of the Measure trigger.
        Default Value: :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].measure_trigger_type`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.measure_trigger_type`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.TriggerType |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | channels          |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Measure Trigger:Trigger Type**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE**

measure_when
------------

    .. py:attribute:: measure_when

        Specifies when the measure unit should acquire measurements. Unless this property is configured to :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`, the :py:attr:`nidcpower.Session.measure_trigger_type` property is ignored.
        Refer to the Acquiring Measurements topic in the NI DC Power Supplies and SMUs Help for more information about how to configure your measurements.
        Default Value: If the :py:attr:`nidcpower.Session.source_mode` property is set to :py:data:`~nidcpower.SourceMode.SINGLE_POINT`, the default value is :py:data:`~nidcpower.MeasureWhen.ON_DEMAND`. This value supports only the :py:meth:`nidcpower.Session.measure` method and :py:meth:`nidcpower.Session.measure_multiple` method. If the :py:attr:`nidcpower.Session.source_mode` property is set to :py:data:`~nidcpower.SourceMode.SEQUENCE`, the default value is :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE`. This value supports only the :py:meth:`nidcpower.Session.fetch_multiple` method.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].measure_when`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.measure_when`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.MeasureWhen |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | channels          |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Measure When**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_WHEN**

merged_channels
---------------

    .. py:attribute:: merged_channels

        Specifies the channel(s) to merge with a designated primary channel of an SMU in order to increase the maximum current you can source from the SMU.
        This property designates the merge channels to combine with a primary channel. To designate the primary channel, initialize the session to the primary channel only.
        Note: You cannot change the merge configuration with this property when the session is in the Running state.
        For complete information on using merged channels with this property, refer to Merged Channels in the NI DC Power Supplies and SMUs Help.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device. Devices that do not support this property behave as if no channels were merged.
            Default Value: Refer to the Supported Properties by Device topic for the default value by device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].merged_channels`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.merged_channels`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Merged Channels**
                - C Attribute: **NIDCPOWER_ATTR_MERGED_CHANNELS**

output_capacitance
------------------

    .. py:attribute:: output_capacitance

        Specifies whether to use a low or high capacitance on the output for the specified channel(s).
        Refer to the NI PXI-4130 Output Capacitance Selection topic in the NI DC Power Supplies and SMUs Help for more information about capacitance.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_capacitance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_capacitance`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.OutputCapacitance |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | channels                |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Output Capacitance**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CAPACITANCE**

output_connected
----------------

    .. py:attribute:: output_connected

        Specifies whether the output relay is connected (closed) or disconnected (open). The :py:attr:`nidcpower.Session.output_enabled` property does not change based on this property; they are independent of each other.
        about supported devices.
        Set this property to False to disconnect the output terminal from the output.
        to the output terminal might discharge unless the relay is disconnected. Excessive connecting and disconnecting of the output can cause premature wear on the relay.
        Default Value: True



        .. note:: Only disconnect the output when disconnecting is necessary for your application. For example, a battery connected


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_connected`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_connected`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Connected**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CONNECTED**

output_cutoff_current_change_limit_high
---------------------------------------

    .. py:attribute:: output_cutoff_current_change_limit_high

        Specifies a limit for positive current slew rate, in amps per microsecond, for output cutoff.
        If the current increases at a rate that exceeds this limit, the output is disconnected.

        To find out whether an output has exceeded this limit, call the :py:meth:`nidcpower.Session.query_latched_output_cutoff_state` method with :py:data:`~nidcpower.OutputCutoffReason.CURRENT_CHANGE_HIGH` as the output cutoff reason.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_cutoff_current_change_limit_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_cutoff_current_change_limit_high`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Cutoff:Current Change Limit High**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH**

output_cutoff_current_change_limit_low
--------------------------------------

    .. py:attribute:: output_cutoff_current_change_limit_low

        Specifies a limit for negative current slew rate, in amps per microsecond, for output cutoff.
        If the current decreases at a rate that exceeds this limit, the output is disconnected.

        To find out whether an output has exceeded this limit, call the :py:meth:`nidcpower.Session.query_latched_output_cutoff_state` method with :py:data:`~nidcpower.OutputCutoffReason.CURRENT_CHANGE_LOW` as the output cutoff reason.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_cutoff_current_change_limit_low`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_cutoff_current_change_limit_low`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Cutoff:Current Change Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW**

output_cutoff_current_measure_limit_high
----------------------------------------

    .. py:attribute:: output_cutoff_current_measure_limit_high

        Specifies a high limit current value, in amps, for output cutoff.
        If the measured current exceeds this limit, the output is disconnected.

        To find out whether an output has exceeded this limit, call the :py:meth:`nidcpower.Session.query_latched_output_cutoff_state` method with :py:data:`~nidcpower.OutputCutoffReason.CURRENT_MEASURE_HIGH` as the output cutoff reason.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_cutoff_current_measure_limit_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_cutoff_current_measure_limit_high`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Cutoff:Current Measure Limit High**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH**

output_cutoff_current_measure_limit_low
---------------------------------------

    .. py:attribute:: output_cutoff_current_measure_limit_low

        Specifies a low limit current value, in amps, for output cutoff.
        If the measured current falls below this limit, the output is disconnected.

        To find out whether an output has fallen below this limit, call the :py:meth:`nidcpower.Session.query_latched_output_cutoff_state` method with :py:data:`~nidcpower.OutputCutoffReason.CURRENT_MEASURE_LOW` as the output cutoff reason.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_cutoff_current_measure_limit_low`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_cutoff_current_measure_limit_low`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Cutoff:Current Measure Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW**

output_cutoff_current_overrange_enabled
---------------------------------------

    .. py:attribute:: output_cutoff_current_overrange_enabled

        Enables or disables current overrange functionality for output cutoff. If enabled, the output is disconnected when the measured current saturates the current range.

        To find out whether an output has exceeded this limit, call the :py:meth:`nidcpower.Session.query_latched_output_cutoff_state` method with :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_OUTPUT_HIGH` as the output cutoff reason.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_cutoff_current_overrange_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_cutoff_current_overrange_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Cutoff:Current Overrange Enabled**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED**

output_cutoff_delay
-------------------

    .. py:attribute:: output_cutoff_delay

        Delays disconnecting the output by the time you specify, in seconds, when a limit is exceeded.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_cutoff_delay`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_cutoff_delay`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels                                                    |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Cutoff:Delay**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CUTOFF_DELAY**

output_cutoff_enabled
---------------------

    .. py:attribute:: output_cutoff_enabled

        Enables or disables output cutoff functionality. If enabled, you can define output cutoffs that, if exceeded, cause the output of the specified channel(s) to be disconnected.
        When this property is disabled, all other output cutoff properties are ignored.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.
             Instruments that do not support this property behave as if this property were set to False.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_cutoff_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_cutoff_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Cutoff:Enabled**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CUTOFF_ENABLED**

output_cutoff_voltage_change_limit_high
---------------------------------------

    .. py:attribute:: output_cutoff_voltage_change_limit_high

        Specifies a limit for positive voltage slew rate, in volts per microsecond, for output cutoff.
        If the voltage increases at a rate that exceeds this limit, the output is disconnected.

        To find out whether an output has exceeded this limit, call the :py:meth:`nidcpower.Session.query_latched_output_cutoff_state` with :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_CHANGE_HIGH` as the output cutoff reason.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_cutoff_voltage_change_limit_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_cutoff_voltage_change_limit_high`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Cutoff:Voltage Change Limit High**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH**

output_cutoff_voltage_change_limit_low
--------------------------------------

    .. py:attribute:: output_cutoff_voltage_change_limit_low

        Specifies a limit for negative voltage slew rate, in volts per microsecond, for output cutoff.
        If the voltage decreases at a rate that exceeds this limit, the output is disconnected.

        To find out whether an output has exceeded this limit, call the :py:meth:`nidcpower.Session.query_latched_output_cutoff_state` with :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_CHANGE_LOW` as the output cutoff reason.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_cutoff_voltage_change_limit_low`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_cutoff_voltage_change_limit_low`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Cutoff:Voltage Change Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW**

output_cutoff_voltage_output_limit_high
---------------------------------------

    .. py:attribute:: output_cutoff_voltage_output_limit_high

        Specifies a high limit voltage value, in volts, for output cutoff.
        If the voltage output exceeds this limit, the output is disconnected.

        To find out whether an output has exceeded this limit, call the :py:meth:`nidcpower.Session.query_latched_output_cutoff_state` method with :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_OUTPUT_HIGH` as the output cutoff reason.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_cutoff_voltage_output_limit_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_cutoff_voltage_output_limit_high`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Cutoff:Voltage Output Limit High**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH**

output_cutoff_voltage_output_limit_low
--------------------------------------

    .. py:attribute:: output_cutoff_voltage_output_limit_low

        Specifies a low limit voltage value, in volts, for output cutoff.
        If the voltage output falls below this limit, the output is disconnected.

        To find out whether an output has fallen below this limit, call the :py:meth:`nidcpower.Session.query_latched_output_cutoff_state` method with :py:data:`~nidcpower.OutputCutoffReason.VOLTAGE_OUTPUT_LOW` as the output cutoff reason.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_cutoff_voltage_output_limit_low`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_cutoff_voltage_output_limit_low`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Cutoff:Voltage Output Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW**

output_enabled
--------------

    .. py:attribute:: output_enabled

        Specifies whether the output is enabled (True) or disabled (False).
        Depending on the value you specify for the :py:attr:`nidcpower.Session.output_function` property, you also must set the voltage level or current level in addition to enabling the output
        the :py:meth:`nidcpower.Session.initiate` method. Refer to the Programming States topic in the NI DC Power Supplies and SMUs Help for more information about NI-DCPower programming states.
        Default Value: The default value is True if you use the :py:meth:`nidcpower.Session.__init__` method to open the session. Otherwise the default value is False, including when you use a calibration session or the deprecated programming model.



        .. note:: If the session is in the Committed or Uncommitted states, enabling the output does not take effect until you call


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Enabled**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_ENABLED**

output_function
---------------

    .. py:attribute:: output_function

        Configures the method to generate on the specified channel(s).
        When :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE` is selected, the device generates the desired voltage level on the output as long as the output current is below the current limit. You can use the following properties to configure the channel when :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE` is selected:
        :py:attr:`nidcpower.Session.voltage_level`
        :py:attr:`nidcpower.Session.current_limit`
        :py:attr:`nidcpower.Session.current_limit_high`
        :py:attr:`nidcpower.Session.current_limit_low`
        :py:attr:`nidcpower.Session.voltage_level_range`
        :py:attr:`nidcpower.Session.current_limit_range`
        :py:attr:`nidcpower.Session.compliance_limit_symmetry`
        When :py:data:`~nidcpower.OutputFunction.DC_CURRENT` is selected, the device generates the desired current level on the output as long as the output voltage is below the voltage limit. You can use the following properties to configure the channel when :py:data:`~nidcpower.OutputFunction.DC_CURRENT` is selected:
        :py:attr:`nidcpower.Session.current_level`
        :py:attr:`nidcpower.Session.voltage_limit`
        :py:attr:`nidcpower.Session.voltage_limit_high`
        :py:attr:`nidcpower.Session.voltage_limit_low`
        :py:attr:`nidcpower.Session.current_level_range`
        :py:attr:`nidcpower.Session.voltage_limit_range`
        :py:attr:`nidcpower.Session.compliance_limit_symmetry`




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_function`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_function`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.OutputFunction |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | channels             |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Function**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_FUNCTION**

output_resistance
-----------------

    .. py:attribute:: output_resistance

        Specifies the output resistance that the device attempts to generate for the specified channel(s). This property is available only when you set the :py:attr:`nidcpower.Session.output_function` property on a support device. Refer to a supported device's topic about output resistance for more information about selecting an output resistance.
        about supported devices.
        Default Value: 0.0



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_resistance`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.output_resistance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Resistance**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_RESISTANCE**

overranging_enabled
-------------------

    .. py:attribute:: overranging_enabled

        Specifies whether NI-DCPower allows setting the voltage level, current level, voltage limit and current limit outside the device specification limits. True means that overranging is enabled.
        Refer to the Ranges topic in the NI DC Power Supplies and SMUs Help for more information about overranging.
        Default Value: False




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].overranging_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.overranging_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Overranging Enabled**
                - C Attribute: **NIDCPOWER_ATTR_OVERRANGING_ENABLED**

ovp_enabled
-----------

    .. py:attribute:: ovp_enabled

        Enables (True) or disables (False) overvoltage protection (OVP).
        Refer to the Output Overvoltage Protection topic in the NI DC Power Supplies and SMUs Help for more information about overvoltage protection.
        Default Value: False



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ovp_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.ovp_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:OVP Enabled**
                - C Attribute: **NIDCPOWER_ATTR_OVP_ENABLED**

ovp_limit
---------

    .. py:attribute:: ovp_limit

        Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages.
        Valid Values: 2 V to 210 V
        Default Value: 210 V



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ovp_limit`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.ovp_limit`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:OVP Limit**
                - C Attribute: **NIDCPOWER_ATTR_OVP_LIMIT**

power_allocation_mode
---------------------

    .. py:attribute:: power_allocation_mode

        Determines whether the device sources the power its source configuration requires or a specific wattage you request; determines whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device.

         When this property configures NI-DCPower to perform a sourcing power check, a device is not permitted to source power in excess of its maximum per-channel or overall sourcing power. If the check determines a source configuration or power request would require the device to do so, NI-DCPower returns an error.

         When this property does not configure NI-DCPower to perform a sourcing power check, a device can attempt to fulfill source configurations that would require it to source power in excess of its maximum per-channel or overall sourcing power and may shut down to prevent damage.

         Default Value: Refer to the Supported Properties by Device topic for the default value by device.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device. Devices that do not support this property behave as if this property were set to :py:data:`~nidcpower.PowerAllocationMode.DISABLED`.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].power_allocation_mode`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.power_allocation_mode`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | enums.PowerAllocationMode |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | channels                  |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Power Allocation Mode**
                - C Attribute: **NIDCPOWER_ATTR_POWER_ALLOCATION_MODE**

power_line_frequency
--------------------

    .. py:attribute:: power_line_frequency

        Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the :py:attr:`nidcpower.Session.aperture_time` property in power line cycles (PLCs).
        in the NI DC Power Supplies and SMUs Help for information about supported devices.
        Default Value: :py:data:`~nidcpower.NIDCPOWER_VAL_60_HERTZ`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].power_line_frequency`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.power_line_frequency`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Power Line Frequency**
                - C Attribute: **NIDCPOWER_ATTR_POWER_LINE_FREQUENCY**

power_source
------------

    .. py:attribute:: power_source

        Specifies the power source to use. NI-DCPower switches the power source used by the device to the specified value.
        Default Value: :py:data:`~nidcpower.PowerSource.AUTOMATIC`
        is set to :py:data:`~nidcpower.PowerSource.AUTOMATIC`. However, if the session is in the Committed or Uncommitted state when you set this property, the power source selection only occurs after you call the :py:meth:`nidcpower.Session.initiate` method.



        .. note:: Automatic selection is not persistent and occurs only at the time this property

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.PowerSource |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Advanced:Power Source**
                - C Attribute: **NIDCPOWER_ATTR_POWER_SOURCE**

power_source_in_use
-------------------

    .. py:attribute:: power_source_in_use

        Indicates whether the device is using the internal or auxiliary power source to generate power.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.PowerSourceInUse |
            +-----------------------+------------------------+
            | Permissions           | read only              |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Advanced:Power Source In Use**
                - C Attribute: **NIDCPOWER_ATTR_POWER_SOURCE_IN_USE**

pulse_bias_current_level
------------------------

    .. py:attribute:: pulse_bias_current_level

        Specifies the pulse bias current level, in amps, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:attr:`nidcpower.Session.pulse_current_level_range` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_bias_current_level`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_bias_current_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Bias Current Level**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL**

pulse_bias_current_limit
------------------------

    .. py:attribute:: pulse_bias_current_limit

        Specifies the pulse bias current limit, in amps, that the output cannot exceed when generating the desired pulse bias voltage on the specified channel(s) during the off phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:attr:`nidcpower.Session.pulse_current_limit_range` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_bias_current_limit`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_bias_current_limit`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Current Limit**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT**

pulse_bias_current_limit_high
-----------------------------

    .. py:attribute:: pulse_bias_current_limit_high

        Specifies the maximum current, in amps, that the output can produce when
        generating the desired pulse voltage on the specified channel(s) during
        the *off* phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        You must also specify a :py:attr:`nidcpower.Session.pulse_bias_current_limit_low` to complete the
        asymmetric range.
        **Valid Values:** [1% of :py:attr:`nidcpower.Session.pulse_current_limit_range`, :py:attr:`nidcpower.Session.pulse_current_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True or if the :py:attr:`nidcpower.Session.output_function` property is set to a
            pulsing method.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_bias_current_limit_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_bias_current_limit_high`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Current Limit High**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH**

pulse_bias_current_limit_low
----------------------------

    .. py:attribute:: pulse_bias_current_limit_low

        Specifies the minimum current, in amps, that the output can produce when
        generating the desired pulse voltage on the specified channel(s) during
        the *off* phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        You must also specify a :py:attr:`nidcpower.Session.pulse_bias_current_limit_high` to complete the
        asymmetric range.
        **Valid Values:** [-:py:attr:`nidcpower.Session.pulse_current_limit_range`, -1% of :py:attr:`nidcpower.Session.pulse_current_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True or if the :py:attr:`nidcpower.Session.output_function` property is set to a
            pulsing method.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_bias_current_limit_low`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_bias_current_limit_low`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Current Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW**

pulse_bias_delay
----------------

    .. py:attribute:: pulse_bias_delay

        Determines when, in seconds, the device generates the Pulse Complete event after generating the off level of a pulse.
        Valid Values: 0 to 167 seconds
        Default Value: 16.67 milliseconds



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_bias_delay`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_bias_delay`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Pulse Bias Delay**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_DELAY**

pulse_bias_voltage_level
------------------------

    .. py:attribute:: pulse_bias_voltage_level

        Specifies the pulse bias voltage level, in volts, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:attr:`nidcpower.Session.pulse_voltage_level_range` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_bias_voltage_level`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_bias_voltage_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Voltage Level**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL**

pulse_bias_voltage_limit
------------------------

    .. py:attribute:: pulse_bias_voltage_limit

        Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:attr:`nidcpower.Session.pulse_voltage_limit_range` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_bias_voltage_limit`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_bias_voltage_limit`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Bias Voltage Limit**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT**

pulse_bias_voltage_limit_high
-----------------------------

    .. py:attribute:: pulse_bias_voltage_limit_high

        Specifies the maximum voltage, in volts, that the output can produce
        when generating the desired pulse current on the specified channel(s)
        during the *off* phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        You must also specify a :py:attr:`nidcpower.Session.pulse_bias_voltage_limit_low` to complete the
        asymmetric range.
        **Valid Values:** [1% of :py:attr:`nidcpower.Session.pulse_voltage_limit_range`, :py:attr:`nidcpower.Session.pulse_voltage_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True or if the :py:attr:`nidcpower.Session.output_function` property is set to a
            pulsing method.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_bias_voltage_limit_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_bias_voltage_limit_high`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Bias Voltage Limit High**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH**

pulse_bias_voltage_limit_low
----------------------------

    .. py:attribute:: pulse_bias_voltage_limit_low

        Specifies the minimum voltage, in volts, that the output can produce
        when generating the desired pulse current on the specified channel(s)
        during the *off* phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        You must also specify a :py:attr:`nidcpower.Session.pulse_bias_voltage_limit_high` to complete the
        asymmetric range.
        **Valid Values:** [-:py:attr:`nidcpower.Session.pulse_voltage_limit_range`, -1% of :py:attr:`nidcpower.Session.pulse_voltage_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True or if the :py:attr:`nidcpower.Session.output_function` property is set to a
            pulsing method.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_bias_voltage_limit_low`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_bias_voltage_limit_low`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Bias Voltage Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW**

pulse_complete_event_output_terminal
------------------------------------

    .. py:attribute:: pulse_complete_event_output_terminal

        Specifies the output terminal for exporting the Pulse Complete event.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.
        Default Value:The default value for PXI Express devices is 250 ns.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_complete_event_output_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_complete_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Pulse Complete Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL**

pulse_complete_event_pulse_polarity
-----------------------------------

    .. py:attribute:: pulse_complete_event_pulse_polarity

        Specifies the behavior of the Pulse Complete event.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_complete_event_pulse_polarity`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_complete_event_pulse_polarity`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.Polarity |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels       |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Pulse Complete Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY**

pulse_complete_event_pulse_width
--------------------------------

    .. py:attribute:: pulse_complete_event_pulse_width

        Specifies the width of the Pulse Complete event, in seconds.
        The minimum event pulse width value for PXI Express devices is 250 ns.
        The maximum event pulse width value for PXI Express devices is 1.6 microseconds.
        Default Value: The default value for PXI Express devices is 250 ns.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_complete_event_pulse_width`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_complete_event_pulse_width`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Pulse Complete Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH**

pulse_current_level
-------------------

    .. py:attribute:: pulse_current_level

        Specifies the pulse current level, in amps, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:attr:`nidcpower.Session.pulse_current_level_range` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_current_level`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_current_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Current Level**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL**

pulse_current_level_range
-------------------------

    .. py:attribute:: pulse_current_level_range

        Specifies the pulse current level range, in amps, for the specified channel(s).
        The range defines the valid values to which you can set the pulse current level and pulse bias current level.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        For valid ranges, refer to the specifications for your instrument.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_current_level_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_current_level_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Current Level Range**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE**

pulse_current_limit
-------------------

    .. py:attribute:: pulse_current_limit

        Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE` and the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to :py:data:`~nidcpower.ComplianceLimitSymmetry.SYMMETRIC`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:attr:`nidcpower.Session.pulse_current_limit_range` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_current_limit`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_current_limit`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT**

pulse_current_limit_high
------------------------

    .. py:attribute:: pulse_current_limit_high

        Specifies the maximum current, in amps, that the output can produce when
        generating the desired pulse voltage on the specified channel(s) during
        the *on* phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        You must also specify a :py:attr:`nidcpower.Session.pulse_current_limit_low` to complete the asymmetric
        range.
        **Valid Values:** [1% of :py:attr:`nidcpower.Session.pulse_current_limit_range`, :py:attr:`nidcpower.Session.pulse_current_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True or if the :py:attr:`nidcpower.Session.output_function` property is set to a
            pulsing method.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_current_limit_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_current_limit_high`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit High**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH**

pulse_current_limit_low
-----------------------

    .. py:attribute:: pulse_current_limit_low

        Specifies the minimum current, in amps, that the output can produce when
        generating the desired pulse voltage on the specified channel(s) during
        the *on* phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        You must also specify a :py:attr:`nidcpower.Session.pulse_current_limit_high` to complete the
        asymmetric range.
        **Valid Values:** [-:py:attr:`nidcpower.Session.pulse_current_limit_range`, -1% of :py:attr:`nidcpower.Session.pulse_current_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True or if the :py:attr:`nidcpower.Session.output_function` property is set to a
            pulsing method.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_current_limit_low`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_current_limit_low`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW**

pulse_current_limit_range
-------------------------

    .. py:attribute:: pulse_current_limit_range

        Specifies the pulse current limit range, in amps, for the specified channel(s).
        The range defines the valid values to which you can set the pulse current limit and pulse bias current limit.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        For valid ranges, refer to the specifications for your instrument.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_current_limit_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_current_limit_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit Range**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE**

pulse_off_time
--------------

    .. py:attribute:: pulse_off_time

        Determines the length, in seconds, of the off phase of a pulse.
        Valid Values: 10 microseconds to 167 seconds
        Default Value: 34 milliseconds



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_off_time`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_off_time`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels                                                    |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Pulse Off Time**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_OFF_TIME**

pulse_on_time
-------------

    .. py:attribute:: pulse_on_time

        Determines the length, in seconds, of the on phase of a pulse.
        Valid Values: 10 microseconds to 167 seconds
        Default Value: 34 milliseconds



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_on_time`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_on_time`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels                                                    |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Pulse On Time**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_ON_TIME**

pulse_trigger_type
------------------

    .. py:attribute:: pulse_trigger_type

        Specifies the behavior of the Pulse trigger.
        Default Value: :py:data:`~nidcpower.TriggerType.NONE`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_trigger_type`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_trigger_type`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.TriggerType |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | channels          |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Pulse Trigger:Trigger Type**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE**

pulse_voltage_level
-------------------

    .. py:attribute:: pulse_voltage_level

        Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:attr:`nidcpower.Session.pulse_current_limit_range` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_level`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_voltage_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Voltage Level**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL**

pulse_voltage_level_range
-------------------------

    .. py:attribute:: pulse_voltage_level_range

        Specifies the pulse voltage level range, in volts, for the specified channel(s).
        The range defines the valid values at which you can set the pulse voltage level and pulse bias voltage level.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        For valid ranges, refer to the specifications for your instrument.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_level_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_voltage_level_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Voltage Level Range**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE**

pulse_voltage_limit
-------------------

    .. py:attribute:: pulse_voltage_limit

        Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current on the specified channel(s) during the on phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT` and the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to :py:data:`~nidcpower.ComplianceLimitSymmetry.SYMMETRIC`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:attr:`nidcpower.Session.pulse_voltage_limit_range` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_limit`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_voltage_limit`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT**

pulse_voltage_limit_high
------------------------

    .. py:attribute:: pulse_voltage_limit_high

        Specifies the maximum voltage, in volts, that the output can produce
        when generating the desired pulse current on the specified channel(s)
        during the *on* phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        You must also specify a :py:attr:`nidcpower.Session.pulse_voltage_limit_low` to complete the asymmetric
        range.
        **Valid Values:** [1% of :py:attr:`nidcpower.Session.pulse_voltage_limit_range`, :py:attr:`nidcpower.Session.pulse_voltage_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True or if the :py:attr:`nidcpower.Session.output_function` property is set to a
            pulsing method.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_limit_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_voltage_limit_high`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit High**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH**

pulse_voltage_limit_low
-----------------------

    .. py:attribute:: pulse_voltage_limit_low

        Specifies the minimum voltage, in volts, that the output can produce
        when generating the desired pulse current on the specified channel(s)
        during the *on* phase of a pulse.
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        You must also specify a :py:attr:`nidcpower.Session.pulse_voltage_limit_high` to complete the
        asymmetric range.
        **Valid Values:** [-:py:attr:`nidcpower.Session.pulse_voltage_limit_range`, -1% of :py:attr:`nidcpower.Session.pulse_voltage_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True or if the :py:attr:`nidcpower.Session.output_function` property is set to a
            pulsing method.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_limit_low`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_voltage_limit_low`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW**

pulse_voltage_limit_range
-------------------------

    .. py:attribute:: pulse_voltage_limit_range

        Specifies the pulse voltage limit range, in volts, for the specified channel(s).
        The range defines the valid values to which you can set the pulse voltage limit and pulse bias voltage limit.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        For valid ranges, refer to the specifications for your instrument.



        .. note:: The channel must be enabled for the specified current limit to take effect. Refer to the :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].pulse_voltage_limit_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.pulse_voltage_limit_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit Range**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE**

query_instrument_status
-----------------------

    .. py:attribute:: query_instrument_status

        Specifies whether NI-DCPower queries the device status after each operation.
        Querying the device status is useful for debugging. After you validate your program, you can set this property to False to disable status checking and maximize performance.
        NI-DCPower ignores status checking for particular properties regardless of the setting of this property.
        Use the :py:meth:`nidcpower.Session.__init__` method to override this value.
        Default Value: True

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Query Instrument Status**
                - C Attribute: **NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS**

ready_for_pulse_trigger_event_output_terminal
---------------------------------------------

    .. py:attribute:: ready_for_pulse_trigger_event_output_terminal

        Specifies the output terminal for exporting the Ready For Pulse Trigger event.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ready_for_pulse_trigger_event_output_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.ready_for_pulse_trigger_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Pulse Trigger Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL**

ready_for_pulse_trigger_event_pulse_polarity
--------------------------------------------

    .. py:attribute:: ready_for_pulse_trigger_event_pulse_polarity

        Specifies the behavior of the Ready For Pulse Trigger event.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ready_for_pulse_trigger_event_pulse_polarity`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.ready_for_pulse_trigger_event_pulse_polarity`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.Polarity |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels       |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Pulse Trigger Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY**

ready_for_pulse_trigger_event_pulse_width
-----------------------------------------

    .. py:attribute:: ready_for_pulse_trigger_event_pulse_width

        Specifies the width of the Ready For Pulse Trigger event, in seconds.
        The minimum event pulse width value for PXI Express devices is 250 ns.
        The maximum event pulse width value for all devices is 1.6 microseconds.
        Default Value: The default value for PXI Express devices is 250 ns



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ready_for_pulse_trigger_event_pulse_width`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.ready_for_pulse_trigger_event_pulse_width`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Pulse Trigger Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH**

requested_power_allocation
--------------------------

    .. py:attribute:: requested_power_allocation

        Specifies the power, in watts, to request the device to source from each active channel.
         This property defines the power to source from the device only if the :py:attr:`nidcpower.Session.power_allocation_mode` property is set to :py:data:`~nidcpower.PowerAllocationMode.MANUAL`.

         The power you request with this property may be incompatible with the power a given source configuration requires or the power the device can provide:
         If the requested power is less than the power required for the source configuration, the device does not exceed the requested power, and NI-DCPower returns an error.
         If the requested power is greater than the maximum per-channel or overall sourcing power, the device does not exceed the allowed power, and NI-DCPower returns an error.

        Valid Values: [0, device per-channel maximum power]
         Default Value: Refer to the Supported Properties by Device topic for the default value by device.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].requested_power_allocation`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.requested_power_allocation`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Requested Power Allocation**
                - C Attribute: **NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION**

reset_average_before_measurement
--------------------------------

    .. py:attribute:: reset_average_before_measurement

        Specifies whether the measurement returned from any measurement call starts with a new measurement call (True) or returns a measurement that has already begun or completed(False).
        When you set the :py:attr:`nidcpower.Session.samples_to_average` property in the Running state, the output channel measurements might move out of synchronization. While NI-DCPower automatically synchronizes measurements upon the initialization of a session, you can force a synchronization in the running state before you run the :py:meth:`nidcpower.Session.measure_multiple` method. To force a synchronization in the running state, set this property to True, and then run the :py:meth:`nidcpower.Session.measure_multiple` method, specifying all channels in the channel name parameter. You can set the :py:attr:`nidcpower.Session.reset_average_before_measurement` property to False after the :py:meth:`nidcpower.Session.measure_multiple` method completes.
        Default Value: True



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].reset_average_before_measurement`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.reset_average_before_measurement`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Reset Average Before Measurement**
                - C Attribute: **NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT**

samples_to_average
------------------

    .. py:attribute:: samples_to_average

        Specifies the number of samples to average when you take a measurement.
        Increasing the number of samples to average decreases measurement noise but increases the time required to take a measurement. Refer to the NI PXI-4110, NI PXI-4130, NI PXI-4132, or NI PXIe-4154 Averaging topic for optional property settings to improve immunity to certain noise types, or refer to the NI PXIe-4140/4141  DC Noise Rejection, NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic for information about improving noise immunity for those devices.
        Default Value:
        NI PXI-4110 or NI PXI-4130—10
        NI PXI-4132—1
        NI PXIe-4112—1
        NI PXIe-4113—1
        NI PXIe-4140/4141—1
        NI PXIe-4142/4143—1
        NI PXIe-4144/4145—1
        NI PXIe-4154—500




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].samples_to_average`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.samples_to_average`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Samples To Average**
                - C Attribute: **NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE**

self_calibration_persistence
----------------------------

    .. py:attribute:: self_calibration_persistence

        Specifies whether the values calculated during self-calibration should be written to hardware to be used until the next self-calibration or only used until the :py:meth:`nidcpower.Session.reset_device` method is called or the machine is powered down.
        This property affects the behavior of the :py:meth:`nidcpower.Session.self_cal` method. When set to :py:data:`~nidcpower.SelfCalibrationPersistence.KEEP_IN_MEMORY`, the values calculated by the :py:meth:`nidcpower.Session.self_cal` method are used in the existing session, as well as in all further sessions until you call the :py:meth:`nidcpower.Session.reset_device` method or restart the machine. When you set this property to :py:data:`~nidcpower.SelfCalibrationPersistence.WRITE_TO_EEPROM`, the values calculated by the :py:meth:`nidcpower.Session.self_cal` method are written to hardware and used in the existing session and in all subsequent sessions until another call to the :py:meth:`nidcpower.Session.self_cal` method is made.
        about supported devices.
        Default Value: :py:data:`~nidcpower.SelfCalibrationPersistence.KEEP_IN_MEMORY`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].self_calibration_persistence`

            To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.self_calibration_persistence`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.SelfCalibrationPersistence |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | instruments                      |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Advanced:Self-Calibration Persistence**
                - C Attribute: **NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE**

sense
-----

    .. py:attribute:: sense

        Selects either local or remote sensing of the output voltage for the specified channel(s).
        Refer to the Local and Remote Sense topic in the NI DC Power Supplies and SMUs Help for more information about sensing voltage on supported channels and about devices that support local and/or remote sensing.
        Default Value: The default value is :py:data:`~nidcpower.Sense.LOCAL` if the device supports local sense. Otherwise, the default and only supported value is :py:data:`~nidcpower.Sense.REMOTE`.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sense`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sense`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | enums.Sense |
            +-----------------------+-------------+
            | Permissions           | read-write  |
            +-----------------------+-------------+
            | Repeated Capabilities | channels    |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Sense**
                - C Attribute: **NIDCPOWER_ATTR_SENSE**

sequence_advance_trigger_type
-----------------------------

    .. py:attribute:: sequence_advance_trigger_type

        Specifies the behavior of the Sequence Advance trigger.
        Default Value: :py:data:`~nidcpower.TriggerType.NONE`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sequence_advance_trigger_type`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sequence_advance_trigger_type`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.TriggerType |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | channels          |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Sequence Advance Trigger:Trigger Type**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE**

sequence_engine_done_event_output_terminal
------------------------------------------

    .. py:attribute:: sequence_engine_done_event_output_terminal

        Specifies the output terminal for exporting the Sequence Engine Done Complete event.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sequence_engine_done_event_output_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sequence_engine_done_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Engine Done Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL**

sequence_engine_done_event_pulse_polarity
-----------------------------------------

    .. py:attribute:: sequence_engine_done_event_pulse_polarity

        Specifies the behavior of the Sequence Engine Done event.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sequence_engine_done_event_pulse_polarity`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sequence_engine_done_event_pulse_polarity`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.Polarity |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels       |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Engine Done Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY**

sequence_engine_done_event_pulse_width
--------------------------------------

    .. py:attribute:: sequence_engine_done_event_pulse_width

        Specifies the width of the Sequence Engine Done event, in seconds.
        The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.
        The maximum event pulse width value for all devices is 1.6 microseconds.
        Valid Values: 1.5e-7 to 1.6e-6 seconds
        Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sequence_engine_done_event_pulse_width`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sequence_engine_done_event_pulse_width`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Engine Done Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH**

sequence_iteration_complete_event_output_terminal
-------------------------------------------------

    .. py:attribute:: sequence_iteration_complete_event_output_terminal

        Specifies the output terminal for exporting the Sequence Iteration Complete event.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sequence_iteration_complete_event_output_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sequence_iteration_complete_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Iteration Complete Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL**

sequence_iteration_complete_event_pulse_polarity
------------------------------------------------

    .. py:attribute:: sequence_iteration_complete_event_pulse_polarity

        Specifies the behavior of the Sequence Iteration Complete event.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sequence_iteration_complete_event_pulse_polarity`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sequence_iteration_complete_event_pulse_polarity`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.Polarity |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels       |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Iteration Complete Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY**

sequence_iteration_complete_event_pulse_width
---------------------------------------------

    .. py:attribute:: sequence_iteration_complete_event_pulse_width

        Specifies the width of the Sequence Iteration Complete event, in seconds.
        The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.
        The maximum event pulse width value for all devices is 1.6 microseconds.
        the NI DC Power Supplies and SMUs Help for information about supported devices.
        Valid Values: 1.5e-7 to 1.6e-6 seconds
        Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sequence_iteration_complete_event_pulse_width`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sequence_iteration_complete_event_pulse_width`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Iteration Complete Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH**

sequence_loop_count
-------------------

    .. py:attribute:: sequence_loop_count

        Specifies the number of times a sequence is run after initiation.
        Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about the sequence loop count.
        When the :py:attr:`nidcpower.Session.sequence_loop_count_is_finite` property is set to False, the :py:attr:`nidcpower.Session.sequence_loop_count` property is ignored.
        Valid Range: 1 to 134217727
        Default Value: 1



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sequence_loop_count`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sequence_loop_count`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Sequence Loop Count**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT**

sequence_loop_count_is_finite
-----------------------------

    .. py:attribute:: sequence_loop_count_is_finite

        Specifies whether a sequence should repeat indefinitely.
        Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about infinite sequencing.
        When the :py:attr:`nidcpower.Session.sequence_loop_count_is_finite` property is set to False, the :py:attr:`nidcpower.Session.sequence_loop_count` property is ignored.
        Default Value: True



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sequence_loop_count_is_finite`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sequence_loop_count_is_finite`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Sequence Loop Count Is Finite**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE**

sequence_step_delta_time
------------------------

    .. py:attribute:: sequence_step_delta_time

        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sequence_step_delta_time`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sequence_step_delta_time`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME**

sequence_step_delta_time_enabled
--------------------------------

    .. py:attribute:: sequence_step_delta_time_enabled

        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].sequence_step_delta_time_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.sequence_step_delta_time_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_STEP_DELTA_TIME_ENABLED**

serial_number
-------------

    .. py:attribute:: serial_number

        Contains the serial number for the device you are currently using.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].serial_number`

            To set/get on all instruments, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.serial_number`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | str         |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | instruments |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Serial Number**
                - C Attribute: **NIDCPOWER_ATTR_SERIAL_NUMBER**

shutdown_trigger_type
---------------------

    .. py:attribute:: shutdown_trigger_type

        Specifies the behavior of the Shutdown trigger.
        Default Value: :py:data:`~nidcpower.TriggerType.NONE`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].shutdown_trigger_type`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.shutdown_trigger_type`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.TriggerType |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | channels          |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Shutdown Trigger:Trigger Type**
                - C Attribute: **NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE**

simulate
--------

    .. py:attribute:: simulate

        Specifies whether to simulate NI-DCPower I/O operations. True specifies that operation is simulated.
        Default Value: False

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NIDCPOWER_ATTR_SIMULATE**

source_complete_event_output_terminal
-------------------------------------

    .. py:attribute:: source_complete_event_output_terminal

        Specifies the output terminal for exporting the Source Complete event.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].source_complete_event_output_terminal`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.source_complete_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Source Complete Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL**

source_complete_event_pulse_polarity
------------------------------------

    .. py:attribute:: source_complete_event_pulse_polarity

        Specifies the behavior of the Source Complete event.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].source_complete_event_pulse_polarity`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.source_complete_event_pulse_polarity`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.Polarity |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels       |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Source Complete Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY**

source_complete_event_pulse_width
---------------------------------

    .. py:attribute:: source_complete_event_pulse_width

        Specifies the width of the Source Complete event, in seconds.
        The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.
        The maximum event pulse width value for all devices is 1.6 microseconds
        Valid Values: 1.5e-7 to 1.6e-6 seconds
        Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].source_complete_event_pulse_width`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.source_complete_event_pulse_width`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Source Complete Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH**

source_delay
------------

    .. py:attribute:: source_delay

        Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the :py:attr:`nidcpower.Session.measure_when` property is set to :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE`.
        Refer to the Single Point Source Mode and Sequence Source Mode topics for more information.
        Valid Values: 0 to 167 seconds
        Default Value: 0.01667 seconds



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].source_delay`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.source_delay`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels                                                    |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Source Delay**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_DELAY**

source_mode
-----------

    .. py:attribute:: source_mode

        Specifies whether to run a single output point or a sequence. Refer to the Single Point Source Mode and Sequence Source Mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes.
        Default value: :py:data:`~nidcpower.SourceMode.SINGLE_POINT`




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].source_mode`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.source_mode`

        The following table lists the characteristics of this property.

            +-----------------------+------------------+
            | Characteristic        | Value            |
            +=======================+==================+
            | Datatype              | enums.SourceMode |
            +-----------------------+------------------+
            | Permissions           | read-write       |
            +-----------------------+------------------+
            | Repeated Capabilities | channels         |
            +-----------------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Source Mode**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_MODE**

source_trigger_type
-------------------

    .. py:attribute:: source_trigger_type

        Specifies the behavior of the Source trigger.
        Default Value: :py:data:`~nidcpower.TriggerType.NONE`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].source_trigger_type`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.source_trigger_type`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.TriggerType |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | channels          |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Source Trigger:Trigger Type**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        Contains a brief description of the specific driver.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Description**
                - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_prefix
----------------------

    .. py:attribute:: specific_driver_prefix

        Contains the prefix for NI-DCPower. The name of each user-callable method in NI-DCPower begins with this prefix.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Prefix**
                - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        Contains additional version information about NI-DCPower.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Revision**
                - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        Contains the name of the vendor that supplies NI-DCPower.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Vendor**
                - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR**

start_trigger_type
------------------

    .. py:attribute:: start_trigger_type

        Specifies the behavior of the Start trigger.
        Default Value: :py:data:`~nidcpower.TriggerType.NONE`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].start_trigger_type`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.start_trigger_type`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.TriggerType |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | channels          |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start Trigger:Trigger Type**
                - C Attribute: **NIDCPOWER_ATTR_START_TRIGGER_TYPE**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        Contains a comma-separated (,) list of supported NI-DCPower device models.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS**

transient_response
------------------

    .. py:attribute:: transient_response

        Specifies the transient response. Refer to the Transient Response topic in the NI DC Power Supplies and SMUs Help for more information about transient response.
        Default Value: :py:data:`~nidcpower.TransientResponse.NORMAL`



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].transient_response`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.transient_response`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.TransientResponse |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | channels                |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Transient Response**
                - C Attribute: **NIDCPOWER_ATTR_TRANSIENT_RESPONSE**

voltage_compensation_frequency
------------------------------

    .. py:attribute:: voltage_compensation_frequency

        The frequency at which a pole-zero pair is added to the system when the channel is in Constant Voltage mode.
        Default value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the :py:attr:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voltage_compensation_frequency`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.voltage_compensation_frequency`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Voltage:Compensation Frequency**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY**

voltage_gain_bandwidth
----------------------

    .. py:attribute:: voltage_gain_bandwidth

        The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in Constant Voltage mode.
        Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the :py:attr:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voltage_gain_bandwidth`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.voltage_gain_bandwidth`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Voltage:Gain Bandwidth**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH**

voltage_level
-------------

    .. py:attribute:: voltage_level

        Specifies the voltage level, in volts, that the device attempts to generate on the specified channel(s).
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:attr:`nidcpower.Session.voltage_level_range` property.



        .. note:: The channel must be enabled for the specified voltage level to take effect. Refer to the :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voltage_level`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.voltage_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Voltage Level**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL**

voltage_level_autorange
-----------------------

    .. py:attribute:: voltage_level_autorange

        Specifies whether NI-DCPower automatically selects the voltage level range based on the desired voltage level for the specified channel(s).
        If you set this property to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the :py:attr:`nidcpower.Session.voltage_level_range` property. If you change the :py:attr:`nidcpower.Session.voltage_level_autorange` property from :py:data:`~nidcpower.AutoZero.ON` to :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:attr:`nidcpower.Session.voltage_level_range` property was set to (or the default value if the property was never set) and uses that value as the voltage level range.
        Query the :py:attr:`nidcpower.Session.voltage_level_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method for information about which range NI-DCPower automatically selects.
        The :py:attr:`nidcpower.Session.voltage_level_autorange` property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        Default Value: :py:data:`~nidcpower.AutoZero.OFF`




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voltage_level_autorange`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.voltage_level_autorange`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Voltage Level Autorange**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE**

voltage_level_range
-------------------

    .. py:attribute:: voltage_level_range

        Specifies the voltage level range, in volts, for the specified channel(s).
        The range defines the valid values to which the voltage level can be set. Use the :py:attr:`nidcpower.Session.voltage_level_autorange` property to enable automatic selection of the voltage level range.
        The :py:attr:`nidcpower.Session.voltage_level_range` property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        For valid ranges, refer to the specifications for your instrument.



        .. note:: The channel must be enabled for the specified voltage level range to take effect. Refer to the :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voltage_level_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.voltage_level_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Voltage Level Range**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE**

voltage_limit
-------------

    .. py:attribute:: voltage_limit

        Specifies the voltage limit, in volts, that the output cannot exceed when generating the desired current level on the specified channels.
        This property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT` and the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to :py:data:`~nidcpower.ComplianceLimitSymmetry.SYMMETRIC`.
        :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        Valid Values: The valid values for this property are defined by the values to which the :py:attr:`nidcpower.Session.voltage_limit_range` property is set.



        .. note:: The channel must be enabled for the specified current level to take effect. Refer to the :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voltage_limit`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.voltage_limit`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Voltage Limit**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT**

voltage_limit_autorange
-----------------------

    .. py:attribute:: voltage_limit_autorange

        Specifies whether NI-DCPower automatically selects the voltage limit range based on the desired voltage limit for the specified channel(s).
        If this property is set to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the :py:attr:`nidcpower.Session.voltage_limit_range` property. If you change the :py:attr:`nidcpower.Session.voltage_limit_autorange` property from :py:data:`~nidcpower.AutoZero.ON` to :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:attr:`nidcpower.Session.voltage_limit_range` property was set to (or the default value if the property was never set) and uses that value as the voltage limit range.
        Query the :py:attr:`nidcpower.Session.voltage_limit_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method to find out which range NI-DCPower automatically selects.
        The :py:attr:`nidcpower.Session.voltage_limit_autorange` property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        Default Value: :py:data:`~nidcpower.AutoZero.OFF`




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voltage_limit_autorange`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.voltage_limit_autorange`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Voltage Limit Autorange**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE**

voltage_limit_high
------------------

    .. py:attribute:: voltage_limit_high

        Specifies the maximum voltage, in volts, that the output can produce
        when generating the desired current on the specified channel(s).
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        You must also specify a :py:attr:`nidcpower.Session.voltage_limit_low` to complete the asymmetric
        range.
        **Valid Values:** [1% of :py:attr:`nidcpower.Session.voltage_limit_range`, :py:attr:`nidcpower.Session.voltage_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voltage_limit_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.voltage_limit_high`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Voltage Limit High**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH**

voltage_limit_low
-----------------

    .. py:attribute:: voltage_limit_low

        Specifies the minimum voltage, in volts, that the output can produce
        when generating the desired current on the specified channel(s).
        This property is applicable only if the :py:attr:`nidcpower.Session.compliance_limit_symmetry` property is set to
        :py:data:`~nidcpower.ComplianceLimitSymmetry.ASYMMETRIC` and the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        You must also specify a :py:attr:`nidcpower.Session.voltage_limit_high` to complete the asymmetric
        range.
        **Valid Values:** [-:py:attr:`nidcpower.Session.voltage_limit_range`, -1% of :py:attr:`nidcpower.Session.voltage_limit_range`]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Search ni.com for Supported Properties by Device for the default value by device.
        **Related Topics:**
        Ranges;
        Changing Ranges;
        Overranging



        .. note:: The limit may be extended beyond the selected limit range if the
            :py:attr:`nidcpower.Session.overranging_enabled` property is
            set to True.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voltage_limit_low`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.voltage_limit_low`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Voltage Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW**

voltage_limit_range
-------------------

    .. py:attribute:: voltage_limit_range

        Specifies the voltage limit range, in volts, for the specified channel(s).
        The range defines the valid values to which the voltage limit can be set. Use the :py:attr:`nidcpower.Session.voltage_limit_autorange` property to enable automatic selection of the voltage limit range.
        The :py:attr:`nidcpower.Session.voltage_limit_range` property is applicable only if the :py:attr:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        For valid ranges, refer to the specifications for your instrument.



        .. note:: The channel must be enabled for the specified voltage limit range to take effect. Refer to the :py:attr:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voltage_limit_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.voltage_limit_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Voltage Limit Range**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE**

voltage_pole_zero_ratio
-----------------------

    .. py:attribute:: voltage_pole_zero_ratio

        The ratio of the pole frequency to the zero frequency when the channel is in Constant Voltage mode.
        Default value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the :py:attr:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported on all devices. For more information about supported devices, search ni.com for Supported Properties by Device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidcpower.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voltage_pole_zero_ratio`

            To set/get on all channels, you can call the property directly on the :py:class:`nidcpower.Session`.

            Example: :py:attr:`my_session.voltage_pole_zero_ratio`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Voltage:Pole-Zero Ratio**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO**


.. contents:: Session


