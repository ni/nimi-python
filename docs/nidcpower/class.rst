nidcpower.Session
=================

.. py:module:: nidcpower

.. py:class:: Session(self, resource_name, channels=None, reset=False, options={})

    

    Creates and returns a new NI-DCPower session to the power supply or SMU
    specified in **resource name** to be used in all subsequent NI-DCPower
    method calls. With this method, you can optionally set the initial
    state of the following session properties:

    -  :py:data:`nidcpower.Session.simulate`
    -  :py:data:`nidcpower.Session.driver_setup`

    After calling this method, the session will be in the Uncommitted
    state. Refer to the `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
    details about specific software states.

    To place the device in a known start-up state when creating a new
    session, set **reset** to True. This action is equivalent to using
    the :py:meth:`nidcpower.Session.reset` method immediately after initializing the
    session.

    To open a session and leave the device in its existing configuration
    without passing through a transitional output state, set **reset** to
    False. Then configure the device as in the previous session,
    changing only the desired settings, and then call the
    :py:meth:`nidcpower.Session.initiate` method.

    **Related Topics:**

    `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

    



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

        


    :type channels: str

    :param reset:
        

        Specifies whether to reset the device during the initialization
        procedure.

        


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


    :type options: str


    **Properties**

    +-----------------------------------------------------------------+----------------------------------------+
    | Property                                                        | Datatype                               |
    +=================================================================+========================================+
    | :py:attr:`aperture_time`                                        | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`aperture_time_units`                                  | :py:data:`ApertureTimeUnits`           |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`auto_zero`                                            | :py:data:`AutoZero`                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`auxiliary_power_source_available`                     | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`channel_count`                                        | int                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`compliance_limit_symmetry`                            | :py:data:`ComplianceLimitSymmetry`     |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`current_compensation_frequency`                       | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`current_gain_bandwidth`                               | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`current_level`                                        | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`current_level_autorange`                              | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`current_level_range`                                  | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`current_limit`                                        | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`current_limit_autorange`                              | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`current_limit_high`                                   | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`current_limit_low`                                    | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`current_limit_range`                                  | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`current_pole_zero_ratio`                              | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`dc_noise_rejection`                                   | :py:data:`DCNoiseRejection`            |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`digital_edge_measure_trigger_edge`                    | :py:data:`DigitalEdge`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`digital_edge_measure_trigger_input_terminal`          | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`digital_edge_pulse_trigger_edge`                      | :py:data:`DigitalEdge`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`digital_edge_pulse_trigger_input_terminal`            | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`digital_edge_sequence_advance_trigger_edge`           | :py:data:`DigitalEdge`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`digital_edge_sequence_advance_trigger_input_terminal` | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`digital_edge_source_trigger_edge`                     | :py:data:`DigitalEdge`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`digital_edge_source_trigger_input_terminal`           | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`digital_edge_start_trigger_edge`                      | :py:data:`DigitalEdge`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`digital_edge_start_trigger_input_terminal`            | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`driver_setup`                                         | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`exported_measure_trigger_output_terminal`             | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`exported_pulse_trigger_output_terminal`               | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`exported_sequence_advance_trigger_output_terminal`    | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`exported_source_trigger_output_terminal`              | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`exported_start_trigger_output_terminal`               | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`fetch_backlog`                                        | int                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`instrument_firmware_revision`                         | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`instrument_manufacturer`                              | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`instrument_model`                                     | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`interlock_input_open`                                 | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`io_resource_descriptor`                               | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`logical_name`                                         | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`measure_buffer_size`                                  | int                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`measure_complete_event_delay`                         | float in seconds or datetime.timedelta |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`measure_complete_event_output_terminal`               | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`measure_complete_event_pulse_polarity`                | :py:data:`Polarity`                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`measure_complete_event_pulse_width`                   | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`measure_record_delta_time`                            | float in seconds or datetime.timedelta |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`measure_record_length`                                | int                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`measure_record_length_is_finite`                      | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`measure_trigger_type`                                 | :py:data:`TriggerType`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`measure_when`                                         | :py:data:`MeasureWhen`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`output_capacitance`                                   | :py:data:`OutputCapacitance`           |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`output_connected`                                     | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`output_enabled`                                       | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`output_function`                                      | :py:data:`OutputFunction`              |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`output_resistance`                                    | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`overranging_enabled`                                  | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`ovp_enabled`                                          | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`ovp_limit`                                            | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`power_line_frequency`                                 | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`power_source`                                         | :py:data:`PowerSource`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`power_source_in_use`                                  | :py:data:`PowerSourceInUse`            |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_bias_current_level`                             | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_bias_current_limit`                             | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_bias_current_limit_high`                        | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_bias_current_limit_low`                         | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_bias_delay`                                     | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_bias_voltage_level`                             | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_bias_voltage_limit`                             | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_bias_voltage_limit_high`                        | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_bias_voltage_limit_low`                         | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_complete_event_output_terminal`                 | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_complete_event_pulse_polarity`                  | :py:data:`Polarity`                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_complete_event_pulse_width`                     | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_current_level`                                  | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_current_level_range`                            | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_current_limit`                                  | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_current_limit_high`                             | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_current_limit_low`                              | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_current_limit_range`                            | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_off_time`                                       | float in seconds or datetime.timedelta |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_on_time`                                        | float in seconds or datetime.timedelta |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_trigger_type`                                   | :py:data:`TriggerType`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_voltage_level`                                  | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_voltage_level_range`                            | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_voltage_limit`                                  | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_voltage_limit_high`                             | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_voltage_limit_low`                              | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`pulse_voltage_limit_range`                            | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`query_instrument_status`                              | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`ready_for_pulse_trigger_event_output_terminal`        | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`ready_for_pulse_trigger_event_pulse_polarity`         | :py:data:`Polarity`                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`ready_for_pulse_trigger_event_pulse_width`            | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`reset_average_before_measurement`                     | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`samples_to_average`                                   | int                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`self_calibration_persistence`                         | :py:data:`SelfCalibrationPersistence`  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`sense`                                                | :py:data:`Sense`                       |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`sequence_advance_trigger_type`                        | :py:data:`TriggerType`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`sequence_engine_done_event_output_terminal`           | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`sequence_engine_done_event_pulse_polarity`            | :py:data:`Polarity`                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`sequence_engine_done_event_pulse_width`               | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`sequence_iteration_complete_event_output_terminal`    | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`sequence_iteration_complete_event_pulse_polarity`     | :py:data:`Polarity`                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`sequence_iteration_complete_event_pulse_width`        | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`sequence_loop_count`                                  | int                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`sequence_loop_count_is_finite`                        | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`simulate`                                             | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`source_complete_event_output_terminal`                | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`source_complete_event_pulse_polarity`                 | :py:data:`Polarity`                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`source_complete_event_pulse_width`                    | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`source_delay`                                         | float in seconds or datetime.timedelta |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`source_mode`                                          | :py:data:`SourceMode`                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`source_trigger_type`                                  | :py:data:`TriggerType`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`specific_driver_description`                          | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`specific_driver_prefix`                               | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`specific_driver_revision`                             | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`specific_driver_vendor`                               | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`start_trigger_type`                                   | :py:data:`TriggerType`                 |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`supported_instrument_models`                          | str                                    |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`transient_response`                                   | :py:data:`TransientResponse`           |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`voltage_compensation_frequency`                       | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`voltage_gain_bandwidth`                               | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`voltage_level`                                        | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`voltage_level_autorange`                              | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`voltage_level_range`                                  | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`voltage_limit`                                        | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`voltage_limit_autorange`                              | bool                                   |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`voltage_limit_high`                                   | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`voltage_limit_low`                                    | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`voltage_limit_range`                                  | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+
    | :py:attr:`voltage_pole_zero_ratio`                              | float                                  |
    +-----------------------------------------------------------------+----------------------------------------+

    **Public methods**

    +------------------------------------------------------------+
    | Method name                                                |
    +============================================================+
    | :py:func:`abort`                                           |
    +------------------------------------------------------------+
    | :py:func:`commit`                                          |
    +------------------------------------------------------------+
    | :py:func:`configure_aperture_time`                         |
    +------------------------------------------------------------+
    | :py:func:`configure_digital_edge_measure_trigger`          |
    +------------------------------------------------------------+
    | :py:func:`configure_digital_edge_pulse_trigger`            |
    +------------------------------------------------------------+
    | :py:func:`configure_digital_edge_sequence_advance_trigger` |
    +------------------------------------------------------------+
    | :py:func:`configure_digital_edge_source_trigger`           |
    +------------------------------------------------------------+
    | :py:func:`configure_digital_edge_start_trigger`            |
    +------------------------------------------------------------+
    | :py:func:`disable`                                         |
    +------------------------------------------------------------+
    | :py:func:`fetch_multiple`                                  |
    +------------------------------------------------------------+
    | :py:func:`get_channel_name`                                |
    +------------------------------------------------------------+
    | :py:func:`get_ext_cal_last_date_and_time`                  |
    +------------------------------------------------------------+
    | :py:func:`get_ext_cal_last_temp`                           |
    +------------------------------------------------------------+
    | :py:func:`get_ext_cal_recommended_interval`                |
    +------------------------------------------------------------+
    | :py:func:`get_self_cal_last_date_and_time`                 |
    +------------------------------------------------------------+
    | :py:func:`get_self_cal_last_temp`                          |
    +------------------------------------------------------------+
    | :py:func:`measure`                                         |
    +------------------------------------------------------------+
    | :py:func:`measure_multiple`                                |
    +------------------------------------------------------------+
    | :py:func:`query_in_compliance`                             |
    +------------------------------------------------------------+
    | :py:func:`query_max_current_limit`                         |
    +------------------------------------------------------------+
    | :py:func:`query_max_voltage_level`                         |
    +------------------------------------------------------------+
    | :py:func:`query_min_current_limit`                         |
    +------------------------------------------------------------+
    | :py:func:`query_output_state`                              |
    +------------------------------------------------------------+
    | :py:func:`read_current_temperature`                        |
    +------------------------------------------------------------+
    | :py:func:`reset`                                           |
    +------------------------------------------------------------+
    | :py:func:`reset_device`                                    |
    +------------------------------------------------------------+
    | :py:func:`reset_with_defaults`                             |
    +------------------------------------------------------------+
    | :py:func:`self_cal`                                        |
    +------------------------------------------------------------+
    | :py:func:`self_test`                                       |
    +------------------------------------------------------------+
    | :py:func:`send_software_edge_trigger`                      |
    +------------------------------------------------------------+
    | :py:func:`set_sequence`                                    |
    +------------------------------------------------------------+
    | :py:func:`wait_for_event`                                  |
    +------------------------------------------------------------+


Properties
----------

aperture_time
~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: aperture_time

        Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by  the :py:data:`nidcpower.Session.aperture_time_units` property.
        for information about supported devices.
        Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about how to configure  your measurements and for information about valid values.
        Default Value: 0.01666666 seconds



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            aperture_time.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            aperture_time.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].aperture_time = var
                var = session['0,1'].aperture_time

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Aperture Time**
                - C Attribute: **NIDCPOWER_ATTR_APERTURE_TIME**

aperture_time_units
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: aperture_time_units

        Specifies the units of the :py:data:`nidcpower.Session.aperture_time` property for the channel configuration.
        for information about supported devices.
        Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about  how to configure your measurements and for information about valid values.
        Default Value: :py:data:`~nidcpower.ApertureTimeUnits.SECONDS`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            aperture_time_units.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            aperture_time_units.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].aperture_time_units = var
                var = session['0,1'].aperture_time_units

        The following table lists the characteristics of this property.

            +----------------+-------------------------+
            | Characteristic | Value                   |
            +================+=========================+
            | Datatype       | enums.ApertureTimeUnits |
            +----------------+-------------------------+
            | Permissions    | read-write              |
            +----------------+-------------------------+
            | Channel Based  | True                    |
            +----------------+-------------------------+
            | Resettable     | No                      |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Aperture Time Units**
                - C Attribute: **NIDCPOWER_ATTR_APERTURE_TIME_UNITS**

auto_zero
~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: auto_zero

        Specifies the auto-zero method to use on the device.
        Refer to the NI PXI-4132 Measurement Configuration and Timing and Auto Zero topics for more information  about how to configure your measurements.
        Default Value: The default value for the NI PXI-4132 is :py:data:`~nidcpower.AutoZero.ON`. The default value for  all other devices is :py:data:`~nidcpower.AutoZero.OFF`, which is the only supported value for these devices.




        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            auto_zero.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            auto_zero.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].auto_zero = var
                var = session['0,1'].auto_zero

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.AutoZero |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+
            | Channel Based  | True           |
            +----------------+----------------+
            | Resettable     | No             |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Auto Zero**
                - C Attribute: **NIDCPOWER_ATTR_AUTO_ZERO**

auxiliary_power_source_available
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: auxiliary_power_source_available

        Indicates whether an auxiliary power source is connected to the device.
        A value of False may indicate that the auxiliary input fuse has blown.  Refer to the Detecting Internal/Auxiliary Power topic in the NI DC Power Supplies and SMUs Help for  more information about internal and auxiliary power.
        power source to generate power. Use the :py:data:`nidcpower.Session.power_source_in_use` property to retrieve this information.



        .. note:: This property does not necessarily indicate if the device is using the auxiliary

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Advanced:Auxiliary Power Source Available**
                - C Attribute: **NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE**

channel_count
~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: channel_count

        Indicates the number of channels that NI-DCPower supports for the instrument that was chosen when  the current session was opened. For channel-based properties, the IVI engine maintains a separate  cache value for each channel.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Channel Count**
                - C Attribute: **NIDCPOWER_ATTR_CHANNEL_COUNT**

compliance_limit_symmetry
~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: compliance_limit_symmetry

        Specifies whether compliance limits for current generation and voltage
        generation for the device are applied symmetrically about 0 V and 0 A or
        asymmetrically with respect to 0 V and 0 A.
        When set to **Symmetric**, voltage limits and current limits are set
        using a single property with a positive value. The resulting range is
        bounded by this positive value and its opposite.
        When set to **Asymmetric**, you must separately set a limit high and a
        limit low using distinct properties.
        For asymmetric limits, the range bounded by the limit high and limit low
        must include zero.
        **Default Value:** Symmetric
        **Related Topics:**
        `Compliance <NI_DC_Power_Supplies_Help.chm::/compliance.html>`__
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: Refer to `Supported Properties by
            Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
            information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            compliance_limit_symmetry.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            compliance_limit_symmetry.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].compliance_limit_symmetry = var
                var = session['0,1'].compliance_limit_symmetry

        The following table lists the characteristics of this property.

            +----------------+-------------------------------+
            | Characteristic | Value                         |
            +================+===============================+
            | Datatype       | enums.ComplianceLimitSymmetry |
            +----------------+-------------------------------+
            | Permissions    | read-write                    |
            +----------------+-------------------------------+
            | Channel Based  | True                          |
            +----------------+-------------------------------+
            | Resettable     | No                            |
            +----------------+-------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Compliance Limit Symmetry**
                - C Attribute: **NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY**

current_compensation_frequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: current_compensation_frequency

        The frequency at which a pole-zero pair is added to the system when the channel is in  Constant Current mode.
        for information about supported devices.
        Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the  :py:data:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            current_compensation_frequency.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            current_compensation_frequency.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].current_compensation_frequency = var
                var = session['0,1'].current_compensation_frequency

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Current:Compensation Frequency**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY**

current_gain_bandwidth
~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: current_gain_bandwidth

        The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes.  This property takes effect when the channel is in Constant Current mode.
        for information about supported devices.
        Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the  :py:data:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            current_gain_bandwidth.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            current_gain_bandwidth.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].current_gain_bandwidth = var
                var = session['0,1'].current_gain_bandwidth

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Current:Gain Bandwidth**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH**

current_level
~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: current_level

        Specifies the current level, in amps, that the device attempts to generate on the specified channel(s).
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        Valid Values: The valid values for this property are defined by the values to which the  :py:data:`nidcpower.Session.current_level_range` property is set.



        .. note:: The channel must be enabled for the specified current level to take effect. Refer to the


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            current_level.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            current_level.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].current_level = var
                var = session['0,1'].current_level

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Current Level**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL**

current_level_autorange
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: current_level_autorange

        Specifies whether NI-DCPower automatically selects the current level range based on the desired current level for  the specified channels.
        If you set this property to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the  :py:data:`nidcpower.Session.current_level_range` property. If you change the :py:data:`nidcpower.Session.current_level_autorange` property from  :py:data:`~nidcpower.AutoZero.ON` to :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:data:`nidcpower.Session.current_level_range`  property was set to (or the default value if the property was never set) and uses that value as the  current level range.
        Query the :py:data:`nidcpower.Session.current_level_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method for  information about which range NI-DCPower automatically selects.
        The :py:data:`nidcpower.Session.current_level_autorange` property is applicable only if the :py:data:`nidcpower.Session.output_function` property  is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        Default Value: :py:data:`~nidcpower.AutoZero.OFF`




        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            current_level_autorange.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            current_level_autorange.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].current_level_autorange = var
                var = session['0,1'].current_level_autorange

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Current Level Autorange**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE**

current_level_range
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: current_level_range

        Specifies the current level range, in amps, for the specified channel(s).
        The range defines the valid value to which the current level can be set. Use the  :py:data:`nidcpower.Session.current_level_autorange` property to enable automatic selection of the current level range.
        The :py:data:`nidcpower.Session.current_level_range` property is applicable only if the :py:data:`nidcpower.Session.output_function` property is  set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.



        .. note:: The channel must be enabled for the specified current level range to take effect. Refer to the


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            current_level_range.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            current_level_range.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].current_level_range = var
                var = session['0,1'].current_level_range

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Current Level Range**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE**

current_limit
~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: current_limit

        Specifies the current limit, in amps, that the output cannot exceed when generating the desired voltage level  on the specified channel(s).
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to  :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE` and the :py:data:`nidcpower.Session.compliance_limit_symmetry` property is set to  :py:data:`~nidcpower.NIDCPOWER_VAL_SYMMETRIC`.
        :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        Valid Values: The valid values for this property are defined by the values to which  :py:data:`nidcpower.Session.current_limit_range` property is set.



        .. note:: The channel must be enabled for the specified current limit to take effect. Refer to the

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            current_limit.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            current_limit.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].current_limit = var
                var = session['0,1'].current_limit

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Current Limit**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT**

current_limit_autorange
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: current_limit_autorange

        Specifies whether NI-DCPower automatically selects the current limit range based on the desired current limit for the  specified channel(s).
        If you set this property to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the  :py:data:`nidcpower.Session.current_limit_range` property. If you change this property from :py:data:`~nidcpower.AutoZero.ON` to  :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:data:`nidcpower.Session.current_limit_range` property was set to  (or the default value if the property was never set) and uses that value as the current limit range.
        Query the :py:data:`nidcpower.Session.current_limit_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method for  information about which range NI-DCPower automatically selects.
        The :py:data:`nidcpower.Session.current_limit_autorange` property is applicable only if the :py:data:`nidcpower.Session.output_function` property  is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        Default Value: :py:data:`~nidcpower.AutoZero.OFF`




        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            current_limit_autorange.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            current_limit_autorange.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].current_limit_autorange = var
                var = session['0,1'].current_limit_autorange

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Current Limit Autorange**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE**

current_limit_high
~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: current_limit_high

        Specifies the maximum current, in amps, that the output can produce when
        generating the desired voltage on the specified channel(s).
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **DC
        Voltage**.
        You must also specify a `Current Limit
        Low <p:py:meth:`nidcpower.Session.CurrentLimitLow`.html>`__ to complete the asymmetric
        range.
        **Valid Values:** [1% of `Current Limit
        Range <p:py:meth:`nidcpower.Session.CurrentLimitRange`.html>`__, `Current Limit
        Range <p:py:meth:`nidcpower.Session.CurrentLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            current_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            current_limit_high.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].current_limit_high = var
                var = session['0,1'].current_limit_high

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Current Limit High**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH**

current_limit_low
~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: current_limit_low

        Specifies the minimum current, in amps, that the output can produce when
        generating the desired voltage on the specified channel(s).
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **DC
        Voltage**.
        You must also specify a `Current Limit
        High <p:py:meth:`nidcpower.Session.CurrentLimitHigh`.html>`__ to complete the asymmetric
        range.
        **Valid Values:** [-`Current Limit
        Range <p:py:meth:`nidcpower.Session.CurrentLimitRange`.html>`__, -1% of `Current Limit
        Range <p:py:meth:`nidcpower.Session.CurrentLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            current_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            current_limit_low.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].current_limit_low = var
                var = session['0,1'].current_limit_low

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Current Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_LOW**

current_limit_range
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: current_limit_range

        Specifies the current limit range, in amps, for the specified channel(s).
        The range defines the valid value to which the current limit can be set. Use the :py:data:`nidcpower.Session.current_limit_autorange`  property to enable automatic selection of the current limit range.
        The :py:data:`nidcpower.Session.current_limit_range` property is applicable only if the :py:data:`nidcpower.Session.output_function` property  is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.



        .. note:: The channel must be enabled for the specified current limit to take effect. Refer to the


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            current_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            current_limit_range.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].current_limit_range = var
                var = session['0,1'].current_limit_range

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Current Limit Range**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE**

current_pole_zero_ratio
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: current_pole_zero_ratio

        The ratio of the pole frequency to the zero frequency when the channel is in  Constant Current mode.
        for information about supported devices.
        Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the :py:data:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            current_pole_zero_ratio.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            current_pole_zero_ratio.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].current_pole_zero_ratio = var
                var = session['0,1'].current_pole_zero_ratio

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Current:Pole-Zero Ratio**
                - C Attribute: **NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO**

dc_noise_rejection
~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: dc_noise_rejection

        Determines the relative weighting of samples in a measurement. Refer to the NI PXIe-4140/4141 DC Noise Rejection,  NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic in the NI DC Power Supplies  and SMUs Help for more information about noise rejection.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.TransientResponse.NORMAL`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------------------+
            | Characteristic | Value                  |
            +================+========================+
            | Datatype       | enums.DCNoiseRejection |
            +----------------+------------------------+
            | Permissions    | read-write             |
            +----------------+------------------------+
            | Channel Based  | False                  |
            +----------------+------------------------+
            | Resettable     | No                     |
            +----------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:DC Noise Rejection**
                - C Attribute: **NIDCPOWER_ATTR_DC_NOISE_REJECTION**

digital_edge_measure_trigger_edge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: digital_edge_measure_trigger_edge

        Specifies whether to configure the Measure trigger to assert on the rising or falling edge.
        :py:data:`nidcpower.Session.source_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.DigitalEdge.RISING`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.DigitalEdge |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Measure Trigger:Digital Edge:Edge**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE**

digital_edge_measure_trigger_input_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: digital_edge_measure_trigger_input_terminal

        Specifies the input terminal for the Measure trigger. This property is used only when the  :py:data:`nidcpower.Session.measure_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
        for this property.
        You can specify any valid input terminal for this property. Valid terminals are listed in  Measurement & Automation Explorer under the Device Routes tab.
        Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input  terminal on Dev1 to be /Dev2/SourceCompleteEvent.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Measure Trigger:Digital Edge:Input Terminal**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL**

digital_edge_pulse_trigger_edge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: digital_edge_pulse_trigger_edge

        Specifies whether to configure the Pulse trigger to assert on the rising or falling edge.
        Default Value: :py:data:`~nidcpower.DigitalEdge.RISING`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.DigitalEdge |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Pulse Trigger:Digital Edge:Edge**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE**

digital_edge_pulse_trigger_input_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: digital_edge_pulse_trigger_input_terminal

        Specifies the input terminal for the Pulse trigger. This property is used only when the :py:data:`nidcpower.Session.pulse_trigger_type` property is set to digital edge.
        You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
        Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Pulse Trigger:Digital Edge:Input Terminal**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL**

digital_edge_sequence_advance_trigger_edge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: digital_edge_sequence_advance_trigger_edge

        Specifies whether to configure the Sequence Advance trigger to assert on the rising or falling edge.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.DigitalEdge.RISING`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.DigitalEdge |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Sequence Advance Trigger:Digital Edge:Edge**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE**

digital_edge_sequence_advance_trigger_input_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: digital_edge_sequence_advance_trigger_input_terminal

        Specifies the input terminal for the Sequence Advance trigger. Use this property only when the  :py:data:`nidcpower.Session.sequence_advance_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
        the NI DC Power Supplies and SMUs Help for information about supported devices.
        You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
        Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can  specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the  input terminal on Dev1 to be /Dev2/SourceCompleteEvent.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic in

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL**

digital_edge_source_trigger_edge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: digital_edge_source_trigger_edge

        Specifies whether to configure the Source trigger to assert on the rising or falling edge.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.DigitalEdge.RISING`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.DigitalEdge |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Source Trigger:Digital Edge:Edge**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE**

digital_edge_source_trigger_input_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: digital_edge_source_trigger_input_terminal

        Specifies the input terminal for the Source trigger. Use this property only when the  :py:data:`nidcpower.Session.source_trigger_type` property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
        for information about supported devices.
        You can specify any valid input terminal for this property. Valid terminals are listed  in Measurement & Automation Explorer under the Device Routes tab.
        Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input  terminal on Dev1 to be /Dev2/SourceCompleteEvent.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Source Trigger:Digital Edge:Input Terminal**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL**

digital_edge_start_trigger_edge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: digital_edge_start_trigger_edge

        Specifies whether to configure the Start trigger to assert on the rising or falling edge.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.DigitalEdge.RISING`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.DigitalEdge |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start Trigger:Digital Edge:Edge**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

digital_edge_start_trigger_input_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: digital_edge_start_trigger_input_terminal

        Specifies the input terminal for the Start trigger. Use this property only when the :py:data:`nidcpower.Session.start_trigger_type`  property is set to :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`.
        for information about supported devices.
        You can specify any valid input terminal for this property. Valid terminals are listed in Measurement & Automation  Explorer under the Device Routes tab.
        Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can  specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal  on Dev1 to be /Dev2/SourceCompleteEvent.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start Trigger:Digital Edge:Input Terminal**
                - C Attribute: **NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL**

driver_setup
~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: driver_setup

        Indicates the Driver Setup string that you specified when initializing the driver.
        Some cases exist where you must specify the instrument driver options at initialization  time. An example of this case is specifying a particular device model from among a family  of devices that the driver supports. This property is useful when simulating a device.  You can specify the driver-specific options through the DriverSetup keyword in the optionsString  parameter in the :py:meth:`nidcpower.Session.__init__` method or through the  IVI Configuration Utility.
        You can specify  driver-specific options through the DriverSetup keyword in the  optionsString parameter in the :py:meth:`nidcpower.Session.__init__` method. If you do not specify a Driver Setup string, this property returns an empty string.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Driver Setup**
                - C Attribute: **NIDCPOWER_ATTR_DRIVER_SETUP**

exported_measure_trigger_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: exported_measure_trigger_output_terminal

        Specifies the output terminal for exporting the Measure trigger.
        Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals  available on your device.
        for information about supported devices.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Measure Trigger:Export Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL**

exported_pulse_trigger_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: exported_pulse_trigger_output_terminal

        Specifies the output terminal for exporting the Pulse trigger.
        Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Pulse Trigger:Export Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL**

exported_sequence_advance_trigger_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: exported_sequence_advance_trigger_output_terminal

        Specifies the output terminal for exporting the Sequence Advance trigger.
        Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals  available on your device.
        for information about supported devices.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Sequence Advance Trigger:Export Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL**

exported_source_trigger_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: exported_source_trigger_output_terminal

        Specifies the output terminal for exporting the Source trigger.
        Refer to the Device Routes tab in MAX for a list of the terminals available on your device.
        for information about supported devices.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Source Trigger:Export Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: exported_start_trigger_output_terminal

        Specifies the output terminal for exporting the Start trigger.
        Refer to the Device Routes tab in Measurement & Automation Explorer (MAX) for a list of the terminals available  on your device.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0.
        for information about supported devices.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start Trigger:Export Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

fetch_backlog
~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: fetch_backlog

        Returns the number of measurements acquired that have not been fetched yet.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Fetch Backlog**
                - C Attribute: **NIDCPOWER_ATTR_FETCH_BACKLOG**

instrument_firmware_revision
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: instrument_firmware_revision

        Contains the firmware revision information for the device you are currently using.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Firmware Revision**
                - C Attribute: **NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: instrument_manufacturer

        Contains the name of the manufacturer for the device you are currently using.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Manufacturer**
                - C Attribute: **NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: instrument_model

        Contains the model number or name of the device that you are currently using.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Model**
                - C Attribute: **NIDCPOWER_ATTR_INSTRUMENT_MODEL**

interlock_input_open
~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: interlock_input_open

        Indicates whether the safety interlock circuit is open.
        Refer to the Safety Interlock topic in the NI DC Power Supplies and SMUs Help for more information about  the safety interlock circuit.
        about supported devices.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Advanced:Interlock Input Open**
                - C Attribute: **NIDCPOWER_ATTR_INTERLOCK_INPUT_OPEN**

io_resource_descriptor
~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: io_resource_descriptor

        Indicates the resource descriptor NI-DCPower uses to identify the physical device.
        If you initialize NI-DCPower with a logical name, this property contains the resource descriptor  that corresponds to the entry in the IVI Configuration utility.
        If you initialize NI-DCPower with the resource descriptor, this property contains that value.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Resource Descriptor**
                - C Attribute: **NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR**

logical_name
~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: logical_name

        Contains the logical name you specified when opening the current IVI session.
        You can pass a logical name to the :py:meth:`nidcpower.Session.__init__` method.  The IVI Configuration utility must contain an entry for the logical name. The logical name entry  refers to a method section in the IVI Configuration file. The method section specifies a physical  device and initial user options.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NIDCPOWER_ATTR_LOGICAL_NAME**

measure_buffer_size
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: measure_buffer_size

        Specifies the number of samples that the active channel measurement buffer can hold.
        The default value is the maximum number of samples that a device is capable of recording in one second.
        for information about supported devices.
        Valid Values: 1000 to 2147483647
        Default Value: Varies by device. Refer to Supported Properties by Device topic in  the NI DC Power Supplies and SMUs Help for more information about default values.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Measure Buffer Size**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE**

measure_complete_event_delay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: measure_complete_event_delay

        Specifies the amount of time to delay the generation of the Measure Complete event, in seconds.
        for information about supported devices.
        Valid Values: 0 to 167 seconds
        Default Value: The NI PXI-4132 and NI PXIe-4140/4141/4142/4143/4144/4145/4154 supports values from  0 seconds to 167 seconds.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | False                                  |
            +----------------+----------------------------------------+
            | Resettable     | No                                     |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Measure Complete Event:Event Delay**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY**

measure_complete_event_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: measure_complete_event_output_terminal

        Specifies the output terminal for exporting the Measure Complete event.
        for information about supported devices.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Measure Complete Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL**

measure_complete_event_pulse_polarity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: measure_complete_event_pulse_polarity

        Specifies the behavior of the Measure Complete event.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.Polarity |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+
            | Channel Based  | False          |
            +----------------+----------------+
            | Resettable     | No             |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Measure Complete Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY**

measure_complete_event_pulse_width
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: measure_complete_event_pulse_width

        Specifies the width of the Measure Complete event, in seconds.
        The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse  width value for PXI Express devices is 250 ns.
        The maximum event pulse width value for all devices is 1.6 microseconds.
        for information about supported devices.
        Valid Values: 1.5e-7 to 1.6e-6
        Default Value: The default value for PXI devices is 150 ns. The default value  for PXI Express devices is 250 ns.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Measure Complete Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH**

measure_record_delta_time
~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: measure_record_delta_time

        Queries the amount of time, in seconds, between between the start of two consecutive measurements in a measure record.  Only query this property after the desired measurement settings are committed.
        for information about supported devices.
        two measurements and the rest would differ.



        .. note:: This property is not available when Auto Zero is configured to Once because the amount of time between the first

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read only                              |
            +----------------+----------------------------------------+
            | Channel Based  | False                                  |
            +----------------+----------------------------------------+
            | Resettable     | No                                     |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Measure Record Delta Time**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME**

measure_record_length
~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: measure_record_length

        Specifies how many measurements compose a measure record. When this property is set to a value greater than 1, the  :py:data:`nidcpower.Session.measure_when` property must be set to :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE` or  :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`.
        for information about supported devices.
        Valid Values: 1 to 16,777,216
        Default Value: 1



        .. note:: This property is not available in a session involving multiple channels.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Measure Record Length**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH**

measure_record_length_is_finite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: measure_record_length_is_finite

        Specifies whether to take continuous measurements. Call the :py:meth:`nidcpower.Session.abort` method to stop continuous measurements.  When this property is set to False and the :py:data:`nidcpower.Session.source_mode` property is set to  :py:data:`~nidcpower.SourceMode.SINGLE_POINT`, the :py:data:`nidcpower.Session.measure_when` property must be set to  :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE` or :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`. When this property is set to  False and the :py:data:`nidcpower.Session.source_mode` property is set to :py:data:`~nidcpower.SourceMode.SEQUENCE`, the :py:data:`nidcpower.Session.measure_when`  property must be set to :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`.
        for information about supported devices.
        Default Value: True



        .. note:: This property is not available in a session involving multiple channels.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Measure Record Length Is Finite**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE**

measure_trigger_type
~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: measure_trigger_type

        Specifies the behavior of the Measure trigger.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.TriggerType.DIGITAL_EDGE`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.TriggerType |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Measure Trigger:Trigger Type**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE**

measure_when
~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: measure_when

        Specifies when the measure unit should acquire measurements. Unless this property is configured to  :py:data:`~nidcpower.MeasureWhen.ON_MEASURE_TRIGGER`, the :py:data:`nidcpower.Session.measure_trigger_type` property is ignored.
        Refer to the Acquiring Measurements topic in the NI DC Power Supplies and SMUs Help for more information about how to  configure your measurements.
        Default Value: If the :py:data:`nidcpower.Session.source_mode` property is set to :py:data:`~nidcpower.SourceMode.SINGLE_POINT`, the default value is  :py:data:`~nidcpower.MeasureWhen.ON_DEMAND`. This value supports only the :py:meth:`nidcpower.Session.measure` method and :py:meth:`nidcpower.Session.measure_multiple`  method. If the :py:data:`nidcpower.Session.source_mode` property is set to :py:data:`~nidcpower.SourceMode.SEQUENCE`, the default value is  :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE`. This value supports only the :py:meth:`nidcpower.Session.fetch_multiple` method.

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.MeasureWhen |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Measure When**
                - C Attribute: **NIDCPOWER_ATTR_MEASURE_WHEN**

output_capacitance
~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: output_capacitance

        Specifies whether to use a low or high capacitance on the output for the specified channel(s).
        for information about supported devices.
        Refer to the NI PXI-4130 Output Capacitance Selection topic in the NI DC Power Supplies and SMUs Help for more  information about capacitance.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            output_capacitance.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            output_capacitance.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].output_capacitance = var
                var = session['0,1'].output_capacitance

        The following table lists the characteristics of this property.

            +----------------+-------------------------+
            | Characteristic | Value                   |
            +================+=========================+
            | Datatype       | enums.OutputCapacitance |
            +----------------+-------------------------+
            | Permissions    | read-write              |
            +----------------+-------------------------+
            | Channel Based  | True                    |
            +----------------+-------------------------+
            | Resettable     | No                      |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Output Capacitance**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CAPACITANCE**

output_connected
~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: output_connected

        Specifies whether the output relay is connected (closed) or disconnected (open). The :py:data:`nidcpower.Session.output_enabled`  property does not change based on this property; they are independent of each other.
        about supported devices.
        Set this property to False to disconnect the output terminal from the output.
        to the output terminal might discharge unless the relay is disconnected. Excessive connecting and disconnecting of the  output can cause premature wear on the relay.
        Default Value: True



        .. note:: Only disconnect the output when disconnecting is necessary for your application. For example, a battery connected


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            output_connected.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            output_connected.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].output_connected = var
                var = session['0,1'].output_connected

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Connected**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_CONNECTED**

output_enabled
~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: output_enabled

        Specifies whether the output is enabled (True) or disabled (False).
        Depending on the value you specify for the :py:data:`nidcpower.Session.output_function` property, you also must set the  voltage level or current level in addition to  enabling the output
        the :py:meth:`nidcpower.Session.initiate` method. Refer to the Programming States topic in the NI DC Power Supplies and SMUs Help for  more information about NI-DCPower programming states.
        Default Value: The default value is True if you use the :py:meth:`nidcpower.Session.__init__` method to open  the session. Otherwise the default value is False, including when you use a calibration session or the deprecated programming model.



        .. note:: If the session is in the Committed or Uncommitted states, enabling the output does not take effect until you call


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            output_enabled.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            output_enabled.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].output_enabled = var
                var = session['0,1'].output_enabled

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Enabled**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_ENABLED**

output_function
~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: output_function

        Configures the method to generate on the specified channel(s).
        When :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE` is selected, the device generates the desired voltage level on the output as long as the  output current is below the current limit. You can use the following properties to configure the channel when  :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE` is selected:
        :py:data:`nidcpower.Session.voltage_level`
        :py:data:`nidcpower.Session.current_limit`
        :py:data:`nidcpower.Session.current_limit_high`
        :py:data:`nidcpower.Session.current_limit_low`
        :py:data:`nidcpower.Session.voltage_level_range`
        :py:data:`nidcpower.Session.current_limit_range`
        When :py:data:`~nidcpower.OutputFunction.DC_CURRENT` is selected, the device generates the desired current level on the output as long as the  output voltage is below the voltage limit. You can use the following properties to configure the channel when  :py:data:`~nidcpower.OutputFunction.DC_CURRENT` is selected:
        :py:data:`nidcpower.Session.current_level`
        :py:data:`nidcpower.Session.voltage_limit`
        :py:data:`nidcpower.Session.voltage_limit_high`
        :py:data:`nidcpower.Session.voltage_limit_low`
        :py:data:`nidcpower.Session.current_level_range`
        :py:data:`nidcpower.Session.voltage_limit_range`
        Default Value: :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`




        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            output_function.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            output_function.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].output_function = var
                var = session['0,1'].output_function

        The following table lists the characteristics of this property.

            +----------------+----------------------+
            | Characteristic | Value                |
            +================+======================+
            | Datatype       | enums.OutputFunction |
            +----------------+----------------------+
            | Permissions    | read-write           |
            +----------------+----------------------+
            | Channel Based  | True                 |
            +----------------+----------------------+
            | Resettable     | No                   |
            +----------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Function**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_FUNCTION**

output_resistance
~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: output_resistance

        Specifies the output resistance that the device attempts to generate for the specified channel(s). This property is  available only when you set the :py:data:`nidcpower.Session.output_function` property on a support device. Refer to a supported device's topic about output resistance for more information about selecting an output resistance.
        about supported devices.
        Default Value: 0.0



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic for information


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            output_resistance.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            output_resistance.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].output_resistance = var
                var = session['0,1'].output_resistance

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Output Resistance**
                - C Attribute: **NIDCPOWER_ATTR_OUTPUT_RESISTANCE**

overranging_enabled
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: overranging_enabled

        Specifies whether NI-DCPower allows setting the voltage level, current level, voltage limit and current limit outside the  device specification limits. True means that overranging is enabled.
        Refer to the Ranges topic in the NI DC Power Supplies and SMUs Help for more information about overranging.
        Default Value: False

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Overranging Enabled**
                - C Attribute: **NIDCPOWER_ATTR_OVERRANGING_ENABLED**

ovp_enabled
~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: ovp_enabled

        Enables (True) or disables (False) overvoltage protection (OVP).
        Refer to the Output Overvoltage Protection topic in the NI DC Power Supplies and SMUs Help for more information about  overvoltage protection.
        for information about supported devices.
        Default Value: False



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:OVP Enabled**
                - C Attribute: **NIDCPOWER_ATTR_OVP_ENABLED**

ovp_limit
~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: ovp_limit

        Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages.
        for information about supported devices.
        Valid Values: 2 V to 210 V
        Default Value: 210 V



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:OVP Limit**
                - C Attribute: **NIDCPOWER_ATTR_OVP_LIMIT**

power_line_frequency
~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: power_line_frequency

        Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the  :py:data:`nidcpower.Session.aperture_time` property in power line cycles (PLCs).
        in the NI DC Power Supplies and SMUs Help for information about supported devices.
        Default Value: :py:data:`~nidcpower.NIDCPOWER_VAL_60_HERTZ`



        .. note:: This property is not supported by all devices. Refer to the Supported Properties by Device topic

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            power_line_frequency.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            power_line_frequency.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].power_line_frequency = var
                var = session['0,1'].power_line_frequency

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Power Line Frequency**
                - C Attribute: **NIDCPOWER_ATTR_POWER_LINE_FREQUENCY**

power_source
~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: power_source

        Specifies the power source to use. NI-DCPower switches the power source used by the  device to the specified value.
        Default Value: :py:data:`~nidcpower.PowerSource.AUTOMATIC`
        is set to :py:data:`~nidcpower.PowerSource.AUTOMATIC`. However, if the session is in the Committed or Uncommitted state  when you set this property, the power source selection only occurs after you call the  :py:meth:`nidcpower.Session.initiate` method.



        .. note:: Automatic selection is not persistent and occurs only at the time this property

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.PowerSource |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Advanced:Power Source**
                - C Attribute: **NIDCPOWER_ATTR_POWER_SOURCE**

power_source_in_use
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: power_source_in_use

        Indicates whether the device is using the internal or auxiliary power source to generate power.

        The following table lists the characteristics of this property.

            +----------------+------------------------+
            | Characteristic | Value                  |
            +================+========================+
            | Datatype       | enums.PowerSourceInUse |
            +----------------+------------------------+
            | Permissions    | read only              |
            +----------------+------------------------+
            | Channel Based  | False                  |
            +----------------+------------------------+
            | Resettable     | No                     |
            +----------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Advanced:Power Source In Use**
                - C Attribute: **NIDCPOWER_ATTR_POWER_SOURCE_IN_USE**

pulse_bias_current_level
~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_bias_current_level

        Specifies the pulse bias current level, in amps, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_current_level_range` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_bias_current_level.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_bias_current_level.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_bias_current_level = var
                var = session['0,1'].pulse_bias_current_level

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Bias Current Level**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL**

pulse_bias_current_limit
~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_bias_current_limit

        Specifies the pulse bias current limit, in amps, that the output cannot exceed when generating the desired pulse bias voltage on the specified channel(s) during the off phase of a pulse.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_current_limit_range` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_bias_current_limit.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_bias_current_limit.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_bias_current_limit = var
                var = session['0,1'].pulse_bias_current_limit

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Current Limit**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT**

pulse_bias_current_limit_high
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_bias_current_limit_high

        Specifies the maximum current, in amps, that the output can produce when
        generating the desired pulse voltage on the specified channel(s) during
        the *off* phase of a pulse.
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
        Voltage**.
        You must also specify a `Pulse Bias Current Limit
        Low <p:py:meth:`nidcpower.Session.PulseBiasCurrentLimitLow`.html>`__ to complete the
        asymmetric range.
        **Valid Values:** [1% of `Pulse Current Limit
        Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__, `Pulse Current Limit
        Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE or if the `Output
            Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
            pulsing method.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_bias_current_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_bias_current_limit_high.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_bias_current_limit_high = var
                var = session['0,1'].pulse_bias_current_limit_high

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Current Limit High**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH**

pulse_bias_current_limit_low
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_bias_current_limit_low

        Specifies the minimum current, in amps, that the output can produce when
        generating the desired pulse voltage on the specified channel(s) during
        the *off* phase of a pulse.
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
        Voltage**.
        You must also specify a `Pulse Bias Current Limit
        High <p:py:meth:`nidcpower.Session.PulseBiasCurrentLimitHigh`.html>`__ to complete the
        asymmetric range.
        **Valid Values:** [-`Pulse Current Limit
        Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__, -1% of `Pulse Current
        Limit Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE or if the `Output
            Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
            pulsing method.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_bias_current_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_bias_current_limit_low.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_bias_current_limit_low = var
                var = session['0,1'].pulse_bias_current_limit_low

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Current Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW**

pulse_bias_delay
~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_bias_delay

        Determines when, in seconds, the device generates the Pulse Complete event after generating the off level of a pulse.
        Valid Values: 0 to 167 seconds
        Default Value: 16.67 milliseconds



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_bias_delay.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_bias_delay.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_bias_delay = var
                var = session['0,1'].pulse_bias_delay

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Pulse Bias Delay**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_DELAY**

pulse_bias_voltage_level
~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_bias_voltage_level

        Specifies the pulse bias voltage level, in volts, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_voltage_level_range` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_bias_voltage_level.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_bias_voltage_level.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_bias_voltage_level = var
                var = session['0,1'].pulse_bias_voltage_level

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Bias Voltage Level**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL**

pulse_bias_voltage_limit
~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_bias_voltage_limit

        Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_voltage_limit_range` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_bias_voltage_limit.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_bias_voltage_limit.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_bias_voltage_limit = var
                var = session['0,1'].pulse_bias_voltage_limit

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Bias Voltage Limit**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT**

pulse_bias_voltage_limit_high
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_bias_voltage_limit_high

        Specifies the maximum voltage, in volts, that the output can produce
        when generating the desired pulse current on the specified channel(s)
        during the *off* phase of a pulse.
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
        Current**.
        You must also specify a `Pulse Bias Voltage Limit
        Low <p:py:meth:`nidcpower.Session.PulseBiasVoltageLimitLow`.html>`__ to complete the
        asymmetric range.
        **Valid Values:** [1% of `Pulse Voltage Limit
        Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__, `Pulse Voltage Limit
        Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE or if the `Output
            Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
            pulsing method.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_bias_voltage_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_bias_voltage_limit_high.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_bias_voltage_limit_high = var
                var = session['0,1'].pulse_bias_voltage_limit_high

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Bias Voltage Limit High**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH**

pulse_bias_voltage_limit_low
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_bias_voltage_limit_low

        Specifies the minimum voltage, in volts, that the output can produce
        when generating the desired pulse current on the specified channel(s)
        during the *off* phase of a pulse.
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
        Current**.
        You must also specify a `Pulse Bias Voltage Limit
        High <p:py:meth:`nidcpower.Session.PulseBiasVoltageLimitHigh`.html>`__ to complete the
        asymmetric range.
        **Valid Values:** [-`Pulse Voltage Limit
        Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__, -1% of `Pulse Voltage
        Limit Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE or if the `Output
            Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
            pulsing method.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_bias_voltage_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_bias_voltage_limit_low.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_bias_voltage_limit_low = var
                var = session['0,1'].pulse_bias_voltage_limit_low

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Bias Voltage Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW**

pulse_complete_event_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_complete_event_output_terminal

        Specifies the output terminal for exporting the Pulse Complete event.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.
        Default Value:The default value for PXI Express devices is 250 ns.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Pulse Complete Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL**

pulse_complete_event_pulse_polarity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_complete_event_pulse_polarity

        Specifies the behavior of the Pulse Complete event.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.Polarity |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+
            | Channel Based  | False          |
            +----------------+----------------+
            | Resettable     | No             |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Pulse Complete Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY**

pulse_complete_event_pulse_width
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_complete_event_pulse_width

        Specifies the width of the Pulse Complete event, in seconds.
        The minimum event pulse width value for PXI Express devices is 250 ns.
        The maximum event pulse width value for PXI Express devices is 1.6 microseconds.
        Default Value: The default value for PXI Express devices is 250 ns.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Pulse Complete Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH**

pulse_current_level
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_current_level

        Specifies the pulse current level, in amps, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_current_level_range` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_current_level.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_current_level.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_current_level = var
                var = session['0,1'].pulse_current_level

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Current Level**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL**

pulse_current_level_range
~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_current_level_range

        Specifies the pulse current level range, in amps, for the specified channel(s).
        The range defines the valid values to which you can set the pulse current level and pulse bias current level.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_current_level_range.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_current_level_range.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_current_level_range = var
                var = session['0,1'].pulse_current_level_range

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Current Level Range**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE**

pulse_current_limit
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_current_limit

        Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE` and the :py:data:`nidcpower.Session.compliance_limit_symmetry`  property is set to :py:data:`~nidcpower.NIDCPOWER_VAL_SYMMETRIC`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_current_limit_range` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_current_limit.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_current_limit.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_current_limit = var
                var = session['0,1'].pulse_current_limit

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT**

pulse_current_limit_high
~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_current_limit_high

        Specifies the maximum current, in amps, that the output can produce when
        generating the desired pulse voltage on the specified channel(s) during
        the *on* phase of a pulse.
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
        Voltage**.
        You must also specify a `Pulse Current Limit
        Low <p:py:meth:`nidcpower.Session.PulseCurrentLimitLow`.html>`__ to complete the asymmetric
        range.
        **Valid Values:** [1% of `Pulse Current Limit
        Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__, `Pulse Current Limit
        Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE or if the `Output
            Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
            pulsing method.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_current_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_current_limit_high.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_current_limit_high = var
                var = session['0,1'].pulse_current_limit_high

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit High**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH**

pulse_current_limit_low
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_current_limit_low

        Specifies the minimum current, in amps, that the output can produce when
        generating the desired pulse voltage on the specified channel(s) during
        the *on* phase of a pulse.
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
        Voltage**.
        You must also specify a `Pulse Current Limit
        High <p:py:meth:`nidcpower.Session.PulseCurrentLimitHigh`.html>`__ to complete the
        asymmetric range.
        **Valid Values:** [-`Pulse Current Limit
        Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__, -1% of `Pulse Current
        Limit Range <p:py:meth:`nidcpower.Session.PulseCurrentLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE or if the `Output
            Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
            pulsing method.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_current_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_current_limit_low.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_current_limit_low = var
                var = session['0,1'].pulse_current_limit_low

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW**

pulse_current_limit_range
~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_current_limit_range

        Specifies the pulse current limit range, in amps, for the specified channel(s).
        The range defines the valid values to which you can set the pulse current limit and pulse bias current limit.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_current_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_current_limit_range.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_current_limit_range = var
                var = session['0,1'].pulse_current_limit_range

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Current Limit Range**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE**

pulse_off_time
~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_off_time

        Determines the length, in seconds, of the off phase of a pulse.
        Valid Values: 10 microseconds to 167 seconds
        Default Value: 34 milliseconds



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_off_time.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_off_time.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_off_time = var
                var = session['0,1'].pulse_off_time

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | True                                   |
            +----------------+----------------------------------------+
            | Resettable     | No                                     |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Pulse Off Time**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_OFF_TIME**

pulse_on_time
~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_on_time

        Determines the length, in seconds, of the on phase of a pulse.
        Valid Values: 10 microseconds to 167 seconds
        Default Value: 34 milliseconds



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_on_time.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_on_time.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_on_time = var
                var = session['0,1'].pulse_on_time

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | True                                   |
            +----------------+----------------------------------------+
            | Resettable     | No                                     |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Pulse On Time**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_ON_TIME**

pulse_trigger_type
~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_trigger_type

        Specifies the behavior of the Pulse trigger.
        Default Value: :py:data:`~nidcpower.TriggerType.NONE`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.TriggerType |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Pulse Trigger:Trigger Type**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE**

pulse_voltage_level
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_voltage_level

        Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_current_limit_range` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_voltage_level.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_voltage_level.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_voltage_level = var
                var = session['0,1'].pulse_voltage_level

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Voltage Level**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL**

pulse_voltage_level_range
~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_voltage_level_range

        Specifies the pulse voltage level range, in volts, for the specified channel(s).
        The range defines the valid values at which you can set the pulse voltage level and pulse bias voltage level.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_VOLTAGE`.
        For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_voltage_level_range.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_voltage_level_range.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_voltage_level_range = var
                var = session['0,1'].pulse_voltage_level_range

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Voltage:Pulse Voltage Level Range**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE**

pulse_voltage_limit
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_voltage_limit

        Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current on the specified channel(s) during the on phase of a pulse.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT` and the :py:data:`nidcpower.Session.compliance_limit_symmetry` property  is set to :py:data:`~nidcpower.NIDCPOWER_VAL_SYMMETRIC`.
        Valid Values: The valid values for this property are defined by the values you specify for the :py:data:`nidcpower.Session.pulse_voltage_limit_range` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_voltage_limit.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_voltage_limit.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_voltage_limit = var
                var = session['0,1'].pulse_voltage_limit

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT**

pulse_voltage_limit_high
~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_voltage_limit_high

        Specifies the maximum voltage, in volts, that the output can produce
        when generating the desired pulse current on the specified channel(s)
        during the *on* phase of a pulse.
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
        Current**.
        You must also specify a `Pulse Voltage Limit
        Low <p:py:meth:`nidcpower.Session.PulseVoltageLimitLow`.html>`__ to complete the asymmetric
        range.
        **Valid Values:** [1% of `Pulse Voltage Limit
        Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__, `Pulse Voltage Limit
        Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE or if the `Output
            Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
            pulsing method.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_voltage_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_voltage_limit_high.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_voltage_limit_high = var
                var = session['0,1'].pulse_voltage_limit_high

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit High**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH**

pulse_voltage_limit_low
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_voltage_limit_low

        Specifies the minimum voltage, in volts, that the output can produce
        when generating the desired pulse current on the specified channel(s)
        during the *on* phase of a pulse.
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **Pulse
        Current**.
        You must also specify a `Pulse Voltage Limit
        High <p:py:meth:`nidcpower.Session.PulseVoltageLimitHigh`.html>`__ to complete the
        asymmetric range.
        **Valid Values:** [-`Pulse Voltage Limit
        Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__, -1% of `Pulse Voltage
        Limit Range <p:py:meth:`nidcpower.Session.PulseVoltageLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE or if the `Output
            Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to a
            pulsing method.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_voltage_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_voltage_limit_low.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_voltage_limit_low = var
                var = session['0,1'].pulse_voltage_limit_low

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW**

pulse_voltage_limit_range
~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: pulse_voltage_limit_range

        Specifies the pulse voltage limit range, in volts, for the specified channel(s).
        The range defines the valid values to which you can set the pulse voltage limit and pulse bias voltage limit.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.PULSE_CURRENT`.
        For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.



        .. note:: The channel must be enabled for the specified current limit to take effect. Refer to the :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            pulse_voltage_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            pulse_voltage_limit_range.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].pulse_voltage_limit_range = var
                var = session['0,1'].pulse_voltage_limit_range

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Pulse Current:Pulse Voltage Limit Range**
                - C Attribute: **NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE**

query_instrument_status
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: query_instrument_status

        Specifies whether NI-DCPower queries the device status after each operation.
        Querying the device status is useful for debugging. After you validate your program, you can set this  property to False to disable status checking and maximize performance.
        NI-DCPower ignores status checking for particular properties regardless of the setting of this property.
        Use the :py:meth:`nidcpower.Session.__init__` method to override this value.
        Default Value: True

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Query Instrument Status**
                - C Attribute: **NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS**

ready_for_pulse_trigger_event_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: ready_for_pulse_trigger_event_output_terminal

        Specifies the output terminal for exporting the Ready For Pulse Trigger event.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Pulse Trigger Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL**

ready_for_pulse_trigger_event_pulse_polarity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: ready_for_pulse_trigger_event_pulse_polarity

        Specifies the behavior of the Ready For Pulse Trigger event.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.Polarity |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+
            | Channel Based  | False          |
            +----------------+----------------+
            | Resettable     | No             |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Pulse Trigger Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY**

ready_for_pulse_trigger_event_pulse_width
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: ready_for_pulse_trigger_event_pulse_width

        Specifies the width of the Ready For Pulse Trigger event, in seconds.
        The minimum event pulse width value for PXI Express devices is 250 ns.
        The maximum event pulse width value for all devices is 1.6 microseconds.
        Default Value: The default value for PXI Express devices is 250 ns



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information about supported devices.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Pulse Trigger Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH**

reset_average_before_measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: reset_average_before_measurement

        Specifies whether the measurement returned from any measurement call starts with a new measurement call (True) or  returns a measurement that has already begun or completed(False).
        for information about supported devices.
        When you set the :py:data:`nidcpower.Session.samples_to_average` property in the Running state, the output channel measurements might  move out of synchronization. While NI-DCPower automatically synchronizes measurements upon the initialization of a  session, you can force a synchronization in the running state before you run the :py:meth:`nidcpower.Session.measure_multiple` method. To  force a synchronization in the running state, set this property to True, and then run the :py:meth:`nidcpower.Session.measure_multiple`  method, specifying all channels in the channel name parameter. You can set the  :py:data:`nidcpower.Session.reset_average_before_measurement` property to False after the :py:meth:`nidcpower.Session.measure_multiple` method  completes.
        Default Value: True



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            reset_average_before_measurement.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            reset_average_before_measurement.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].reset_average_before_measurement = var
                var = session['0,1'].reset_average_before_measurement

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Advanced:Reset Average Before Measurement**
                - C Attribute: **NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT**

samples_to_average
~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: samples_to_average

        Specifies the number of samples to average when you take a measurement.
        Increasing the number of samples to average decreases measurement noise but increases the time required to take  a measurement. Refer to the NI PXI-4110, NI PXI-4130, NI PXI-4132, or NI PXIe-4154 Averaging topic for  optional property settings to improve immunity to certain noise types, or refer to the NI PXIe-4140/4141  DC Noise Rejection, NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic for  information about improving noise immunity for those devices.
        Default Value:
        NI PXI-4110 or NI PXI-4130—10
        NI PXI-4132—1
        NI PXIe-4112—1
        NI PXIe-4113—1
        NI PXIe-4140/4141—1
        NI PXIe-4142/4143—1
        NI PXIe-4144/4145—1
        NI PXIe-4154—500




        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            samples_to_average.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            samples_to_average.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].samples_to_average = var
                var = session['0,1'].samples_to_average

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Samples To Average**
                - C Attribute: **NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE**

self_calibration_persistence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: self_calibration_persistence

        Specifies whether the values calculated during self-calibration should be written to hardware to be used until the  next self-calibration or only used until the :py:meth:`nidcpower.Session.reset_device` method is called or the machine  is powered down.
        This property affects the behavior of the :py:meth:`nidcpower.Session.self_cal` method. When set to  :py:data:`~nidcpower.SelfCalibrationPersistence.KEEP_IN_MEMORY`, the values calculated by the :py:meth:`nidcpower.Session.self_cal` method are used in  the existing session, as well as in all further sessions until you call the :py:meth:`nidcpower.Session.reset_device` method  or restart the machine. When you set this property to :py:data:`~nidcpower.SelfCalibrationPersistence.WRITE_TO_EEPROM`, the values calculated  by the :py:meth:`nidcpower.Session.self_cal` method are written to hardware and used in the existing session and  in all subsequent sessions until another call to the :py:meth:`nidcpower.Session.self_cal` method is made.
        about supported devices.
        Default Value: :py:data:`~nidcpower.SelfCalibrationPersistence.KEEP_IN_MEMORY`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device for information

        The following table lists the characteristics of this property.

            +----------------+----------------------------------+
            | Characteristic | Value                            |
            +================+==================================+
            | Datatype       | enums.SelfCalibrationPersistence |
            +----------------+----------------------------------+
            | Permissions    | read-write                       |
            +----------------+----------------------------------+
            | Channel Based  | False                            |
            +----------------+----------------------------------+
            | Resettable     | No                               |
            +----------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Advanced:Self-Calibration Persistence**
                - C Attribute: **NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE**

sense
~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: sense

        Selects either local or remote sensing of the output voltage for the specified channel(s).
        Refer to the Local and Remote Sense topic in the NI DC Power Supplies and SMUs Help for more  information about sensing voltage on supported channels and about devices that support local and/or remote sensing.
        Default Value: The default value is :py:data:`~nidcpower.Sense.LOCAL` if the device supports local sense.  Otherwise, the default and only supported value is :py:data:`~nidcpower.Sense.REMOTE`.




        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            sense.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            sense.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].sense = var
                var = session['0,1'].sense

        The following table lists the characteristics of this property.

            +----------------+-------------+
            | Characteristic | Value       |
            +================+=============+
            | Datatype       | enums.Sense |
            +----------------+-------------+
            | Permissions    | read-write  |
            +----------------+-------------+
            | Channel Based  | True        |
            +----------------+-------------+
            | Resettable     | No          |
            +----------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Measurement:Sense**
                - C Attribute: **NIDCPOWER_ATTR_SENSE**

sequence_advance_trigger_type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: sequence_advance_trigger_type

        Specifies the behavior of the Sequence Advance trigger.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.TriggerType.NONE`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.TriggerType |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Sequence Advance Trigger:Trigger Type**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE**

sequence_engine_done_event_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: sequence_engine_done_event_output_terminal

        Specifies the output terminal for exporting the Sequence Engine Done Complete event.
        for information about supported devices.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Engine Done Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL**

sequence_engine_done_event_pulse_polarity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: sequence_engine_done_event_pulse_polarity

        Specifies the behavior of the Sequence Engine Done event.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.Polarity |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+
            | Channel Based  | False          |
            +----------------+----------------+
            | Resettable     | No             |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Engine Done Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY**

sequence_engine_done_event_pulse_width
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: sequence_engine_done_event_pulse_width

        Specifies the width of the Sequence Engine Done event, in seconds.
        The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value  for PXI Express devices is 250 ns.
        The maximum event pulse width value for all devices is 1.6 microseconds.
        for information about supported devices.
        Valid Values: 1.5e-7 to 1.6e-6 seconds
        Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Engine Done Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH**

sequence_iteration_complete_event_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: sequence_iteration_complete_event_output_terminal

        Specifies the output terminal for exporting the Sequence Iteration Complete event.
        for information about supported devices.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Iteration Complete Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL**

sequence_iteration_complete_event_pulse_polarity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: sequence_iteration_complete_event_pulse_polarity

        Specifies the behavior of the Sequence Iteration Complete event.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.Polarity |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+
            | Channel Based  | False          |
            +----------------+----------------+
            | Resettable     | No             |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Iteration Complete Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY**

sequence_iteration_complete_event_pulse_width
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: sequence_iteration_complete_event_pulse_width

        Specifies the width of the Sequence Iteration Complete event, in seconds.
        The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width  value for PXI Express devices is 250 ns.
        The maximum event pulse width value for all devices is 1.6 microseconds.
        the NI DC Power Supplies and SMUs Help for information about supported devices.
        Valid Values: 1.5e-7 to 1.6e-6 seconds
        Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic in

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Sequence Iteration Complete Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH**

sequence_loop_count
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: sequence_loop_count

        Specifies the number of times a sequence is run after initiation.
        Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about the sequence  loop count.
        for information about supported devices. When the :py:data:`nidcpower.Session.sequence_loop_count_is_finite` property  is set to False, the :py:data:`nidcpower.Session.sequence_loop_count` property is ignored.
        Valid Range: 1 to 134217727
        Default Value: 1



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Sequence Loop Count**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT**

sequence_loop_count_is_finite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: sequence_loop_count_is_finite

        Specifies whether a sequence should repeat indefinitely.
        Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about  infinite sequencing.
        :py:data:`nidcpower.Session.sequence_loop_count_is_finite` property is set to False,  the :py:data:`nidcpower.Session.sequence_loop_count` property is ignored.
        Default Value: True



        .. note:: This property is not supported by all devices. When the

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Sequence Loop Count Is Finite**
                - C Attribute: **NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE**

simulate
~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: simulate

        Specifies whether to simulate NI-DCPower I/O operations. True specifies that operation is simulated.
        Default Value: False

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NIDCPOWER_ATTR_SIMULATE**

source_complete_event_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: source_complete_event_output_terminal

        Specifies the output terminal for exporting the Source Complete event.
        for information about supported devices.
        Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Source Complete Event:Output Terminal**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL**

source_complete_event_pulse_polarity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: source_complete_event_pulse_polarity

        Specifies the behavior of the Source Complete event.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.Polarity.HIGH`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.Polarity |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+
            | Channel Based  | False          |
            +----------------+----------------+
            | Resettable     | No             |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Source Complete Event:Pulse:Polarity**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY**

source_complete_event_pulse_width
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: source_complete_event_pulse_width

        Specifies the width of the Source Complete event, in seconds.
        for information about supported devices.
        The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value  for PXI Express devices is 250 ns.
        The maximum event pulse width value for all devices is 1.6 microseconds
        Valid Values: 1.5e-7 to 1.6e-6 seconds
        Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | False      |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Source Complete Event:Pulse:Width**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH**

source_delay
~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: source_delay

        Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the  :py:data:`nidcpower.Session.measure_when` property is set to :py:data:`~nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE`.
        Refer to the Single Point Source Mode and Sequence Source Mode topics for more information.
        Valid Values: 0 to 167 seconds
        Default Value: 0.01667 seconds



        .. note:: Refer to Supported Properties by Device for information about supported devices.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            source_delay.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            source_delay.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].source_delay = var
                var = session['0,1'].source_delay

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | True                                   |
            +----------------+----------------------------------------+
            | Resettable     | No                                     |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Advanced:Source Delay**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_DELAY**

source_mode
~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: source_mode

        Specifies whether to run a single output point or a sequence. Refer to the Single Point Source Mode and Sequence Source  Mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes.
        Default value: :py:data:`~nidcpower.SourceMode.SINGLE_POINT`

        The following table lists the characteristics of this property.

            +----------------+------------------+
            | Characteristic | Value            |
            +================+==================+
            | Datatype       | enums.SourceMode |
            +----------------+------------------+
            | Permissions    | read-write       |
            +----------------+------------------+
            | Channel Based  | False            |
            +----------------+------------------+
            | Resettable     | No               |
            +----------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Source Mode**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_MODE**

source_trigger_type
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: source_trigger_type

        Specifies the behavior of the Source trigger.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.TriggerType.NONE`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.TriggerType |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Source Trigger:Trigger Type**
                - C Attribute: **NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE**

specific_driver_description
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: specific_driver_description

        Contains a brief description of the specific driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Description**
                - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_prefix
~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: specific_driver_prefix

        Contains the prefix for NI-DCPower. The name of each user-callable  method in NI-DCPower begins with this prefix.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Prefix**
                - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_PREFIX**

specific_driver_revision
~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: specific_driver_revision

        Contains additional version information about NI-DCPower.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Revision**
                - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: specific_driver_vendor

        Contains the name of the vendor that supplies NI-DCPower.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Vendor**
                - C Attribute: **NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR**

start_trigger_type
~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: start_trigger_type

        Specifies the behavior of the Start trigger.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.TriggerType.NONE`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.TriggerType |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | False             |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start Trigger:Trigger Type**
                - C Attribute: **NIDCPOWER_ATTR_START_TRIGGER_TYPE**

supported_instrument_models
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: supported_instrument_models

        Contains a comma-separated (,) list of supported NI-DCPower device models.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | False     |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS**

transient_response
~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: transient_response

        Specifies the transient response. Refer to the Transient Response topic in the NI DC Power Supplies and SMUs Help  for more information about transient response.
        for information about supported devices.
        Default Value: :py:data:`~nidcpower.TransientResponse.NORMAL`



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            transient_response.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            transient_response.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].transient_response = var
                var = session['0,1'].transient_response

        The following table lists the characteristics of this property.

            +----------------+-------------------------+
            | Characteristic | Value                   |
            +================+=========================+
            | Datatype       | enums.TransientResponse |
            +----------------+-------------------------+
            | Permissions    | read-write              |
            +----------------+-------------------------+
            | Channel Based  | True                    |
            +----------------+-------------------------+
            | Resettable     | No                      |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Transient Response**
                - C Attribute: **NIDCPOWER_ATTR_TRANSIENT_RESPONSE**

voltage_compensation_frequency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: voltage_compensation_frequency

        The frequency at which a pole-zero pair is added to the system when the channel is in  Constant Voltage mode.
        for information about supported devices.
        Default value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of  the :py:data:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            voltage_compensation_frequency.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            voltage_compensation_frequency.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].voltage_compensation_frequency = var
                var = session['0,1'].voltage_compensation_frequency

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Voltage:Compensation Frequency**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY**

voltage_gain_bandwidth
~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: voltage_gain_bandwidth

        The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This property takes effect when the channel is in Constant Voltage mode.
        for information about supported devices.
        Default Value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the  :py:data:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            voltage_gain_bandwidth.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            voltage_gain_bandwidth.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].voltage_gain_bandwidth = var
                var = session['0,1'].voltage_gain_bandwidth

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Voltage:Gain Bandwidth**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH**

voltage_level
~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: voltage_level

        Specifies the voltage level, in volts, that the device attempts to generate on the specified channel(s).
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        Valid Values: The valid values for this property are defined by the values you specify for the  :py:data:`nidcpower.Session.voltage_level_range` property.



        .. note:: The channel must be enabled for the specified voltage level to take effect. Refer to the


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            voltage_level.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            voltage_level.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].voltage_level = var
                var = session['0,1'].voltage_level

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Voltage Level**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL**

voltage_level_autorange
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: voltage_level_autorange

        Specifies whether NI-DCPower automatically selects the voltage level range based on the desired voltage level  for the specified channel(s).
        If you set this property to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the  :py:data:`nidcpower.Session.voltage_level_range` property. If you change the :py:data:`nidcpower.Session.voltage_level_autorange` property from  :py:data:`~nidcpower.AutoZero.ON` to :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:data:`nidcpower.Session.voltage_level_range`  property was set to (or the default value if the property was never set) and uses that value as  the voltage level range.
        Query the :py:data:`nidcpower.Session.voltage_level_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method for  information about which range NI-DCPower automatically selects.
        The :py:data:`nidcpower.Session.voltage_level_autorange` property is applicable only if the :py:data:`nidcpower.Session.output_function` property  is set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        Default Value: :py:data:`~nidcpower.AutoZero.OFF`




        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            voltage_level_autorange.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            voltage_level_autorange.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].voltage_level_autorange = var
                var = session['0,1'].voltage_level_autorange

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Voltage Level Autorange**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE**

voltage_level_range
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: voltage_level_range

        Specifies the voltage level range, in volts, for the specified channel(s).
        The range defines the valid values to which the voltage level can be set. Use the :py:data:`nidcpower.Session.voltage_level_autorange`  property to enable automatic selection of the voltage level range.
        The :py:data:`nidcpower.Session.voltage_level_range` property is applicable only if the :py:data:`nidcpower.Session.output_function` property is  set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`.
        :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.



        .. note:: The channel must be enabled for the specified voltage level range to take effect. Refer to the


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            voltage_level_range.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            voltage_level_range.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].voltage_level_range = var
                var = session['0,1'].voltage_level_range

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Voltage:Voltage Level Range**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE**

voltage_limit
~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: voltage_limit

        Specifies the voltage limit, in volts, that the output cannot exceed when generating the desired current level  on the specified channels.
        This property is applicable only if the :py:data:`nidcpower.Session.output_function` property is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`  and the :py:data:`nidcpower.Session.compliance_limit_symmetry` property is set to :py:data:`~nidcpower.NIDCPOWER_VAL_SYMMETRIC`.
        :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        Valid Values: The valid values for this property are defined by the values to which the  :py:data:`nidcpower.Session.voltage_limit_range` property is set.



        .. note:: The channel must be enabled for the specified current level to take effect. Refer to the

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            voltage_limit.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            voltage_limit.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].voltage_limit = var
                var = session['0,1'].voltage_limit

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Voltage Limit**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT**

voltage_limit_autorange
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: voltage_limit_autorange

        Specifies whether NI-DCPower automatically selects the voltage limit range based on the desired voltage limit for  the specified channel(s).
        If this property is set to :py:data:`~nidcpower.AutoZero.ON`, NI-DCPower ignores any changes you make to the  :py:data:`nidcpower.Session.voltage_limit_range` property. If you change the :py:data:`nidcpower.Session.voltage_limit_autorange` property from  :py:data:`~nidcpower.AutoZero.ON` to :py:data:`~nidcpower.AutoZero.OFF`, NI-DCPower retains the last value the :py:data:`nidcpower.Session.voltage_limit_range`  property was set to (or the default value if the property was never set) and uses that value as the voltage limit  range.
        Query the :py:data:`nidcpower.Session.voltage_limit_range` property by using the :py:meth:`nidcpower.Session._get_attribute_vi_int32` method to find out  which range NI-DCPower automatically selects.
        The :py:data:`nidcpower.Session.voltage_limit_autorange` property is applicable only if the :py:data:`nidcpower.Session.output_function` property  is set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        Default Value: :py:data:`~nidcpower.AutoZero.OFF`




        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            voltage_limit_autorange.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            voltage_limit_autorange.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].voltage_limit_autorange = var
                var = session['0,1'].voltage_limit_autorange

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Voltage Limit Autorange**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE**

voltage_limit_high
~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: voltage_limit_high

        Specifies the maximum voltage, in volts, that the output can produce
        when generating the desired current on the specified channel(s).
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **DC
        Current**.
        You must also specify a `Voltage Limit
        Low <p:py:meth:`nidcpower.Session.VoltageLimitLow`.html>`__ to complete the asymmetric
        range.
        **Valid Values:** [1% of `Voltage Limit
        Range <p:py:meth:`nidcpower.Session.VoltageLimitRange`.html>`__, `Voltage Limit
        Range <p:py:meth:`nidcpower.Session.VoltageLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            voltage_limit_high.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            voltage_limit_high.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].voltage_limit_high = var
                var = session['0,1'].voltage_limit_high

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Voltage Limit High**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH**

voltage_limit_low
~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: voltage_limit_low

        Specifies the minimum voltage, in volts, that the output can produce
        when generating the desired current on the specified channel(s).
        This property is applicable only if the `Compliance Limit
        Symmetry <p:py:meth:`nidcpower.Session.ComplianceLimitSymmetry`.html>`__ property is set to
        **Asymmetric** and the `Output
        Method <p:py:meth:`nidcpower.Session.OutputFunction`.html>`__ property is set to **DC
        Current**.
        You must also specify a `Voltage Limit
        High <p:py:meth:`nidcpower.Session.VoltageLimitHigh`.html>`__ to complete the asymmetric
        range.
        **Valid Values:** [-`Voltage Limit
        Range <p:py:meth:`nidcpower.Session.VoltageLimitRange`.html>`__, -1% of `Voltage Limit
        Range <p:py:meth:`nidcpower.Session.VoltageLimitRange`.html>`__]
        The range bounded by the limit high and limit low must include zero.
        **Default Value:** Refer to `Supported Properties by
        Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
        the default value by device.
        **Related Topics:**
        `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
        `Changing
        Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
        `Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__



        .. note:: The limit may be extended beyond the selected limit range if the
            `Overranging Enabled <p:py:meth:`nidcpower.Session.OverrangingEnabled`.html>`__ property is
            set to TRUE.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            voltage_limit_low.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            voltage_limit_low.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].voltage_limit_low = var
                var = session['0,1'].voltage_limit_low

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Voltage Limit Low**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW**

voltage_limit_range
~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: voltage_limit_range

        Specifies the voltage limit range, in volts, for the specified channel(s).
        The range defines the valid values to which the voltage limit can be set. Use the :py:data:`nidcpower.Session.voltage_limit_autorange`  property to enable automatic selection of the voltage limit range.
        The :py:data:`nidcpower.Session.voltage_limit_range` property is applicable only if the :py:data:`nidcpower.Session.output_function` property is  set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`.
        :py:data:`nidcpower.Session.output_enabled` property for more information about enabling the output channel.
        For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.



        .. note:: The channel must be enabled for the specified voltage limit range to take effect. Refer to the


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            voltage_limit_range.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            voltage_limit_range.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].voltage_limit_range = var
                var = session['0,1'].voltage_limit_range

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:DC Current:Voltage Limit Range**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE**

voltage_pole_zero_ratio
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:attribute:: voltage_pole_zero_ratio

        The ratio of the pole frequency to the zero frequency when the channel is in  Constant Voltage mode.
        for information about supported devices.
        Default value: Determined by the value of the :py:data:`~nidcpower.TransientResponse.NORMAL` setting of the  :py:data:`nidcpower.Session.transient_response` property.



        .. note:: This property is not supported by all devices. Refer to Supported Properties by Device topic


        .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
            voltage_pole_zero_ratio.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            voltage_pole_zero_ratio.Session instance, and calling set/get value on the result.:

            .. code:: python

                session['0,1'].voltage_pole_zero_ratio = var
                var = session['0,1'].voltage_pole_zero_ratio

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | True       |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Source:Custom Transient Response:Voltage:Pole-Zero Ratio**
                - C Attribute: **NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO**


Methods
-------


abort
~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: abort()

            Transitions the NI-DCPower session from the Running state to the
            Committed state. If a sequence is running, it is stopped. Any
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



commit
~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: commit()

            Applies previously configured settings to the device. Calling this
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

            



configure_aperture_time
~~~~~~~~~~~~~~~~~~~~~~~

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

            

            .. note:: This method is not supported on all devices. Refer to `Supported
                Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].configure_aperture_time(aperture_time, units=nidcpower.ApertureTimeUnits.SECONDS)


            :param aperture_time:


                Specifies the aperture time. Refer to the *Aperture Time* topic for your
                device in the *NI DC Power Supplies and SMUs Help* for more information.

                


            :type aperture_time: float
            :param units:


                Specifies the units for **apertureTime**.
                **Defined Values**:

                +------------------------------------------------------------------+------------------------------+
                | :py:data:`~nidcpower.ApertureTimeUnits.SECONDS` (1028)           | Specifies seconds.           |
                +------------------------------------------------------------------+------------------------------+
                | :py:data:`~nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES` (1029) | Specifies Power Line Cycles. |
                +------------------------------------------------------------------+------------------------------+


            :type units: :py:data:`nidcpower.ApertureTimeUnits`

configure_digital_edge_measure_trigger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: configure_digital_edge_measure_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

            Configures the Measure trigger for digital edge triggering.

            

            .. note:: This method is not supported on all devices. Refer to `Supported
                Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.



            :param input_terminal:


                Specifies the input terminal for the digital edge Measure trigger.

                You can specify any valid input terminal for this method. Valid
                terminals are listed in MAX under the **Device Routes** tab. For
                PXIe-4162/4163, refer to the Signal Routing topic for the device to
                determine which routes are available. This information is not available
                on a Device Routes tab in MAX.

                Input terminals can be specified in one of two ways. If the device is
                named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
                with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
                shortened terminal name, PXI_Trig0. The input terminal can also be a
                terminal from another device. For example, you can set the input
                terminal on Dev1 to be /Dev2/SourceCompleteEvent.

                


            :type input_terminal: str
            :param edge:


                Specifies whether to configure the Measure trigger to assert on the
                rising or falling edge.
                **Defined Values:**

                +--------------------------------------------------+----------------------------------------------------------------+
                | :py:data:`~nidcpower.DigitalEdge.RISING` (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +--------------------------------------------------+----------------------------------------------------------------+
                | :py:data:`~nidcpower.DigitalEdge.FALLING` (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +--------------------------------------------------+----------------------------------------------------------------+


            :type edge: :py:data:`nidcpower.DigitalEdge`

configure_digital_edge_pulse_trigger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: configure_digital_edge_pulse_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

            Configures the Pulse trigger for digital edge triggering.

            

            .. note:: This method is not supported on all devices. Refer to `Supported
                Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.



            :param input_terminal:


                Specifies the input terminal for the digital edge Pulse trigger.

                You can specify any valid input terminal for this method. Valid
                terminals are listed in MAX under the **Device Routes** tab.

                Input terminals can be specified in one of two ways. If the device is
                named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
                with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
                shortened terminal name, PXI_Trig0. The input terminal can also be a
                terminal from another device. For example, you can set the input
                terminal on Dev1 to be /Dev2/SourceCompleteEvent.

                


            :type input_terminal: str
            :param edge:


                Specifies whether to configure the Pulse trigger to assert on the rising
                or falling edge.
                **Defined Values:**

                +--------------------------------------------------+----------------------------------------------------------------+
                | :py:data:`~nidcpower.DigitalEdge.RISING` (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +--------------------------------------------------+----------------------------------------------------------------+
                | :py:data:`~nidcpower.DigitalEdge.FALLING` (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +--------------------------------------------------+----------------------------------------------------------------+


            :type edge: :py:data:`nidcpower.DigitalEdge`

configure_digital_edge_sequence_advance_trigger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: configure_digital_edge_sequence_advance_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

            Configures the Sequence Advance trigger for digital edge triggering.

            

            .. note:: This method is not supported on all devices. Refer to `Supported
                Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.



            :param input_terminal:


                Specifies the input terminal for the digital edge Sequence Advance
                trigger.

                You can specify any valid input terminal for this method. Valid
                terminals are listed in MAX under the **Device Routes** tab. For
                PXIe-4162/4163, refer to the Signal Routing topic for the device to
                determine which routes are available. This information is not available
                on a Device Routes tab in MAX.

                Input terminals can be specified in one of two ways. If the device is
                named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
                with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
                shortened terminal name, PXI_Trig0. The input terminal can also be a
                terminal from another device. For example, you can set the input
                terminal on Dev1 to be /Dev2/SourceCompleteEvent.

                


            :type input_terminal: str
            :param edge:


                Specifies whether to configure the Sequence Advance trigger to assert on
                the rising or falling edge.
                **Defined Values:**

                +--------------------------------------------------+----------------------------------------------------------------+
                | :py:data:`~nidcpower.DigitalEdge.RISING` (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +--------------------------------------------------+----------------------------------------------------------------+
                | :py:data:`~nidcpower.DigitalEdge.FALLING` (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +--------------------------------------------------+----------------------------------------------------------------+


            :type edge: :py:data:`nidcpower.DigitalEdge`

configure_digital_edge_source_trigger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: configure_digital_edge_source_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

            Configures the Source trigger for digital edge triggering.

            

            .. note:: This method is not supported on all devices. Refer to `Supported
                Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.



            :param input_terminal:


                Specifies the input terminal for the digital edge Source trigger.

                You can specify any valid input terminal for this method. Valid
                terminals are listed in MAX under the **Device Routes** tab. For
                PXIe-4162/4163, refer to the Signal Routing topic for the device to
                determine which routes are available. This information is not available
                on a Device Routes tab in MAX.

                Input terminals can be specified in one of two ways. If the device is
                named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
                with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
                shortened terminal name, PXI_Trig0. The input terminal can also be a
                terminal from another device. For example, you can set the input
                terminal on Dev1 to be /Dev2/SourceCompleteEvent.

                


            :type input_terminal: str
            :param edge:


                Specifies whether to configure the Source trigger to assert on the
                rising or falling edge.
                **Defined Values:**

                +--------------------------------------------------+----------------------------------------------------------------+
                | :py:data:`~nidcpower.DigitalEdge.RISING` (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +--------------------------------------------------+----------------------------------------------------------------+
                | :py:data:`~nidcpower.DigitalEdge.FALLING` (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +--------------------------------------------------+----------------------------------------------------------------+


            :type edge: :py:data:`nidcpower.DigitalEdge`

configure_digital_edge_start_trigger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: configure_digital_edge_start_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

            Configures the Start trigger for digital edge triggering.

            

            .. note:: This method is not supported on all devices. Refer to `Supported
                Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.



            :param input_terminal:


                Specifies the input terminal for the digital edge Start trigger.

                You can specify any valid input terminal for this method. Valid
                terminals are listed in MAX under the **Device Routes** tab. For
                PXIe-4162/4163, refer to the Signal Routing topic for the device to
                determine which routes are available. This information is not available
                on a Device Routes tab in MAX.

                Input terminals can be specified in one of two ways. If the device is
                named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
                with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
                shortened terminal name, PXI_Trig0. The input terminal can also be a
                terminal from another device. For example, you can set the input
                terminal on Dev1 to be /Dev2/SourceCompleteEvent.

                


            :type input_terminal: str
            :param edge:


                Specifies whether to configure the Start trigger to assert on the rising
                or falling edge.
                **Defined Values:**

                +--------------------------------------------------+----------------------------------------------------------------+
                | :py:data:`~nidcpower.DigitalEdge.RISING` (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
                +--------------------------------------------------+----------------------------------------------------------------+
                | :py:data:`~nidcpower.DigitalEdge.FALLING` (1017) | Asserts the trigger on the falling edge of the digital signal. |
                +--------------------------------------------------+----------------------------------------------------------------+


            :type edge: :py:data:`nidcpower.DigitalEdge`

disable
~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: disable()

            This method performs the same actions as the :py:meth:`nidcpower.Session.reset`
            method, except that this method also immediately sets the
            :py:data:`nidcpower.Session.output_enabled` property to False.

            This method opens the output relay on devices that have an output
            relay.

            



fetch_multiple
~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: fetch_multiple(count, timeout=datetime.timedelta(seconds=1.0))

            Returns a list of named tuples (Measurement) that were
            previously taken and are stored in the NI-DCPower buffer. This method
            should not be used when the :py:data:`nidcpower.Session.measure_when` property is
            set to :py:data:`~nidcpower.MeasureWhen.ON_DEMAND`. You must first call
            :py:meth:`nidcpower.Session.initiate` before calling this method.

            Fields in Measurement:

            - **voltage** (float)
            - **current** (float)
            - **in_compliance** (bool)

            

            .. note:: This method is not supported on all devices. Refer to `Supported Methods by Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm, supportedfunctions)>`__ for more information about supported devices.


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].fetch_multiple(count, timeout=datetime.timedelta(seconds=1.0))


            :param count:


                Specifies the number of measurements to fetch.

                


            :type count: int
            :param timeout:


                Specifies the maximum time allowed for this method to complete. If the method does not complete within this time interval, NI-DCPower returns an error.

                

                .. note:: When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.


            :type timeout: float in seconds or datetime.timedelta

            :rtype: list of Measurement
            :return:


                    List of named tuples with fields:

                    - **voltage** (float)
                    - **current** (float)
                    - **in_compliance** (bool)

                    



get_channel_name
~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_channel_name(index)

            Retrieves the output **channelName** that corresponds to the requested
            **index**. Use the :py:data:`nidcpower.Session.channel_count` property to
            determine the upper bound of valid values for **index**.

            


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].get_channel_name(index)


            :param index:


                Specifies which output channel name to return. The index values begin at
                1.

                


            :type index: int

get_ext_cal_last_date_and_time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_ext_cal_last_date_and_time()

            Returns the date and time of the last successful calibration.

            



            :rtype: datetime.datetime
            :return:


                    Indicates date and time of the last calibration.

                    



get_ext_cal_last_temp
~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_ext_cal_last_temp()

            Returns the onboard **temperature** of the device, in degrees Celsius,
            during the last successful external calibration.

            



            :rtype: float
            :return:


                    Returns the onboard **temperature** of the device, in degrees Celsius,
                    during the last successful external calibration.

                    



get_ext_cal_recommended_interval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_ext_cal_recommended_interval()

            Returns the recommended maximum interval, in **months**, between
            external calibrations.

            



            :rtype: datetime.timedelta
            :return:


                    Specifies the recommended maximum interval, in **months**, between
                    external calibrations.

                    



get_self_cal_last_date_and_time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: get_self_cal_last_date_and_time()

            Returns the date and time of the oldest successful self-calibration from among the channels in the session.

            

            .. note:: This method is not supported on all devices.



            :rtype: datetime.datetime
            :return:


                    Returns the date and time the device was last calibrated.

                    



get_self_cal_last_temp
~~~~~~~~~~~~~~~~~~~~~~

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

            

            .. note:: This method is not supported on all devices. Refer to `Supported
                Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.



            :rtype: float
            :return:


                    Returns the onboard **temperature** of the device, in degrees Celsius,
                    during the oldest successful calibration.

                    



measure
~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: measure(measurement_type)

            Returns the measured value of either the voltage or current on the
            specified output channel. Each call to this method blocks other
            method calls until the hardware returns the **measurement**. To
            measure multiple output channels, use the :py:meth:`nidcpower.Session.measure_multiple`
            method.

            


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].measure(measurement_type)


            :param measurement_type:


                Specifies whether a voltage or current value is measured.
                **Defined Values**:

                +----------------------------------------------------+------------------------------+
                | :py:data:`~nidcpower.MeasurementTypes.VOLTAGE` (1) | The device measures voltage. |
                +----------------------------------------------------+------------------------------+
                | :py:data:`~nidcpower.MeasurementTypes.CURRENT` (0) | The device measures current. |
                +----------------------------------------------------+------------------------------+


            :type measurement_type: :py:data:`nidcpower.MeasurementTypes`

            :rtype: float
            :return:


                    Returns the value of the measurement, either in volts for voltage or
                    amps for current.

                    



measure_multiple
~~~~~~~~~~~~~~~~

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

            

            .. note:: This method is not supported on all devices. Refer to `Supported Methods by Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm, supportedfunctions)>`__ for more information about supported devices.


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].measure_multiple()


            :rtype: list of Measurement
            :return:


                    List of named tuples with fields:

                    - **voltage** (float)
                    - **current** (float)
                    - **in_compliance** (bool) - Always None

                    



query_in_compliance
~~~~~~~~~~~~~~~~~~~

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


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].query_in_compliance()


            :rtype: bool
            :return:


                    Returns whether the device output channel is in compliance.

                    



query_max_current_limit
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: query_max_current_limit(voltage_level)

            Queries the maximum current limit on an output channel if the output
            channel is set to the specified **voltageLevel**.

            


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].query_max_current_limit(voltage_level)


            :param voltage_level:


                Specifies the voltage level to use when calculating the
                **maxCurrentLimit**.

                


            :type voltage_level: float

            :rtype: float
            :return:


                    Returns the maximum current limit that can be set with the specified
                    **voltageLevel**.

                    



query_max_voltage_level
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: query_max_voltage_level(current_limit)

            Queries the maximum voltage level on an output channel if the output
            channel is set to the specified **currentLimit**.

            


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].query_max_voltage_level(current_limit)


            :param current_limit:


                Specifies the current limit to use when calculating the
                **maxVoltageLevel**.

                


            :type current_limit: float

            :rtype: float
            :return:


                    Returns the maximum voltage level that can be set on an output channel
                    with the specified **currentLimit**.

                    



query_min_current_limit
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: query_min_current_limit(voltage_level)

            Queries the minimum current limit on an output channel if the output
            channel is set to the specified **voltageLevel**.

            


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].query_min_current_limit(voltage_level)


            :param voltage_level:


                Specifies the voltage level to use when calculating the
                **minCurrentLimit**.

                


            :type voltage_level: float

            :rtype: float
            :return:


                    Returns the minimum current limit that can be set on an output channel
                    with the specified **voltageLevel**.

                    



query_output_state
~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: query_output_state(output_state)

            Queries the specified output channel to determine if the output channel
            is currently in the state specified by **outputState**.

            **Related Topics:**

            `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

            


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].query_output_state(output_state)


            :param output_state:


                Specifies the output state of the output channel that is being queried.
                **Defined Values**:

                +------------------------------------------------+-------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputStates.VOLTAGE` (0) | The device maintains a constant voltage by adjusting the current. |
                +------------------------------------------------+-------------------------------------------------------------------+
                | :py:data:`~nidcpower.OutputStates.CURRENT` (1) | The device maintains a constant current by adjusting the voltage. |
                +------------------------------------------------+-------------------------------------------------------------------+


            :type output_state: :py:data:`nidcpower.OutputStates`

            :rtype: bool
            :return:


                    Returns whether the device output channel is in the specified output
                    state.

                    



read_current_temperature
~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: read_current_temperature()

            Returns the current onboard **temperature**, in degrees Celsius, of the
            device.

            



            :rtype: float
            :return:


                    Returns the onboard **temperature**, in degrees Celsius, of the device.

                    



reset
~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: reset()

            Resets the device to a known state. This method disables power
            generation, resets session properties to their default values, commits
            the session properties, and leaves the session in the Uncommitted state.
            Refer to the `Programming
            States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
            more information about NI-DCPower software states.

            



reset_device
~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: self_cal()

            Performs a self-calibration upon the specified channel(s).

            This method disables the output, performs several internal
            calculations, and updates calibration values. The updated calibration
            values are written to the device hardware if the
            :py:data:`nidcpower.Session.self_calibration_persistence` property is set to
            :py:data:`~nidcpower.SelfCalibrationPersistence.WRITE_TO_EEPROM`. Refer to the
            :py:data:`nidcpower.Session.self_calibration_persistence` property topic for more
            information about the settings for this property.

            When calling :py:meth:`nidcpower.Session.self_cal` with the PXIe-4162/4163,
            specify all channels of your PXIe-4162/4163 with the channelName input.
            You cannot self-calibrate a subset of PXIe-4162/4163 channels.

            Refer to the
            `Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__ topic for
            more information about this method.

            **Related Topics:**

            `Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__

            

            .. note:: This method is not supported on all devices. Refer to `Supported
                Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].self_cal()


self_test
~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: send_software_edge_trigger(trigger)

            Asserts the specified trigger. This method can override an external
            edge trigger.

            **Related Topics:**

            `Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__

            

            .. note:: This method is not supported on all devices. Refer to `Supported
                Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.



            :param trigger:


                Specifies which trigger to assert.
                **Defined Values:**

                +---------------------------------------------------------------------+---------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_START_TRIGGER` (1034)            | Asserts the Start trigger.            |
                +---------------------------------------------------------------------+---------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_SOURCE_TRIGGER` (1035)           | Asserts the Source trigger.           |
                +---------------------------------------------------------------------+---------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_MEASURE_TRIGGER` (1036)          | Asserts the Measure trigger.          |
                +---------------------------------------------------------------------+---------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER` (1037) | Asserts the Sequence Advance trigger. |
                +---------------------------------------------------------------------+---------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_PULSE_TRIGGER` (1053             | Asserts the Pulse trigger.            |
                +---------------------------------------------------------------------+---------------------------------------+

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger: :py:data:`nidcpower.SendSoftwareEdgeTriggerType`

set_sequence
~~~~~~~~~~~~

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

            

            .. note:: This method is not supported on all devices. Refer to `Supported
                Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.


            .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
                nidcpower.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidcpower.Session instance, and calling this method on the result.:

                .. code:: python

                    session.channels['0,1'].set_sequence(values, source_delays)


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

wait_for_event
~~~~~~~~~~~~~~

    .. py:currentmodule:: nidcpower.Session

    .. py:method:: wait_for_event(event_id, timeout=datetime.timedelta(seconds=10.0))

            Waits until the device has generated the specified event.

            The session monitors whether each type of event has occurred at least
            once since the last time this method or the :py:meth:`nidcpower.Session.initiate`
            method were called. If an event has only been generated once and you
            call this method successively, the method times out. Individual
            events must be generated between separate calls of this method.

            

            .. note:: Refer to `Supported Methods by
                Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
                for more information about supported devices.



            :param event_id:


                Specifies which event to wait for.
                **Defined Values:**

                +------------------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT` (1030)             | Waits for the Source Complete event.             |
                +------------------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT` (1031)            | Waits for the Measure Complete event.            |
                +------------------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT` (1032) | Waits for the Sequence Iteration Complete event. |
                +------------------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT` (1033)        | Waits for the Sequence Engine Done event.        |
                +------------------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_PULSE_COMPLETE_EVENT` (1051 )             | Waits for the Pulse Complete event.              |
                +------------------------------------------------------------------------------+--------------------------------------------------+
                | :py:data:`~nidcpower.NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT` (1052)     | Waits for the Ready for Pulse Trigger event.     |
                +------------------------------------------------------------------------------+--------------------------------------------------+

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type event_id: :py:data:`nidcpower.Event`
            :param timeout:


                Specifies the maximum time allowed for this method to complete, in
                seconds. If the method does not complete within this time interval,
                NI-DCPower returns an error.

                

                .. note:: When setting the timeout interval, ensure you take into account any
                    triggers so that the timeout interval is long enough for your
                    application.


            :type timeout: float in seconds or datetime.timedelta



Properties
----------

+-----------------------------------------------------------------------------------+----------------------------------------+
| Property                                                                          | Datatype                               |
+===================================================================================+========================================+
| :py:attr:`nidcpower.Session.aperture_time`                                        | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.aperture_time_units`                                  | :py:data:`ApertureTimeUnits`           |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.auto_zero`                                            | :py:data:`AutoZero`                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.auxiliary_power_source_available`                     | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.channel_count`                                        | int                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.compliance_limit_symmetry`                            | :py:data:`ComplianceLimitSymmetry`     |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.current_compensation_frequency`                       | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.current_gain_bandwidth`                               | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.current_level`                                        | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.current_level_autorange`                              | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.current_level_range`                                  | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.current_limit`                                        | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.current_limit_autorange`                              | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.current_limit_high`                                   | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.current_limit_low`                                    | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.current_limit_range`                                  | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.current_pole_zero_ratio`                              | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.dc_noise_rejection`                                   | :py:data:`DCNoiseRejection`            |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.digital_edge_measure_trigger_edge`                    | :py:data:`DigitalEdge`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.digital_edge_measure_trigger_input_terminal`          | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.digital_edge_pulse_trigger_edge`                      | :py:data:`DigitalEdge`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.digital_edge_pulse_trigger_input_terminal`            | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.digital_edge_sequence_advance_trigger_edge`           | :py:data:`DigitalEdge`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.digital_edge_sequence_advance_trigger_input_terminal` | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.digital_edge_source_trigger_edge`                     | :py:data:`DigitalEdge`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.digital_edge_source_trigger_input_terminal`           | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.digital_edge_start_trigger_edge`                      | :py:data:`DigitalEdge`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.digital_edge_start_trigger_input_terminal`            | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.driver_setup`                                         | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.exported_measure_trigger_output_terminal`             | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.exported_pulse_trigger_output_terminal`               | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.exported_sequence_advance_trigger_output_terminal`    | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.exported_source_trigger_output_terminal`              | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.exported_start_trigger_output_terminal`               | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.fetch_backlog`                                        | int                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.instrument_firmware_revision`                         | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.instrument_manufacturer`                              | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.instrument_model`                                     | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.interlock_input_open`                                 | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.io_resource_descriptor`                               | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.logical_name`                                         | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.measure_buffer_size`                                  | int                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.measure_complete_event_delay`                         | float in seconds or datetime.timedelta |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.measure_complete_event_output_terminal`               | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.measure_complete_event_pulse_polarity`                | :py:data:`Polarity`                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.measure_complete_event_pulse_width`                   | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.measure_record_delta_time`                            | float in seconds or datetime.timedelta |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.measure_record_length`                                | int                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.measure_record_length_is_finite`                      | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.measure_trigger_type`                                 | :py:data:`TriggerType`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.measure_when`                                         | :py:data:`MeasureWhen`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.output_capacitance`                                   | :py:data:`OutputCapacitance`           |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.output_connected`                                     | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.output_enabled`                                       | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.output_function`                                      | :py:data:`OutputFunction`              |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.output_resistance`                                    | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.overranging_enabled`                                  | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.ovp_enabled`                                          | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.ovp_limit`                                            | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.power_line_frequency`                                 | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.power_source`                                         | :py:data:`PowerSource`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.power_source_in_use`                                  | :py:data:`PowerSourceInUse`            |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_bias_current_level`                             | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_bias_current_limit`                             | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_bias_current_limit_high`                        | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_bias_current_limit_low`                         | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_bias_delay`                                     | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_bias_voltage_level`                             | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_bias_voltage_limit`                             | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_bias_voltage_limit_high`                        | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_bias_voltage_limit_low`                         | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_complete_event_output_terminal`                 | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_complete_event_pulse_polarity`                  | :py:data:`Polarity`                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_complete_event_pulse_width`                     | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_current_level`                                  | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_current_level_range`                            | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_current_limit`                                  | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_current_limit_high`                             | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_current_limit_low`                              | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_current_limit_range`                            | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_off_time`                                       | float in seconds or datetime.timedelta |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_on_time`                                        | float in seconds or datetime.timedelta |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_trigger_type`                                   | :py:data:`TriggerType`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_voltage_level`                                  | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_voltage_level_range`                            | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_voltage_limit`                                  | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_voltage_limit_high`                             | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_voltage_limit_low`                              | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.pulse_voltage_limit_range`                            | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.query_instrument_status`                              | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.ready_for_pulse_trigger_event_output_terminal`        | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.ready_for_pulse_trigger_event_pulse_polarity`         | :py:data:`Polarity`                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.ready_for_pulse_trigger_event_pulse_width`            | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.reset_average_before_measurement`                     | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.samples_to_average`                                   | int                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.self_calibration_persistence`                         | :py:data:`SelfCalibrationPersistence`  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.sense`                                                | :py:data:`Sense`                       |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.sequence_advance_trigger_type`                        | :py:data:`TriggerType`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.sequence_engine_done_event_output_terminal`           | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.sequence_engine_done_event_pulse_polarity`            | :py:data:`Polarity`                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.sequence_engine_done_event_pulse_width`               | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.sequence_iteration_complete_event_output_terminal`    | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.sequence_iteration_complete_event_pulse_polarity`     | :py:data:`Polarity`                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.sequence_iteration_complete_event_pulse_width`        | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.sequence_loop_count`                                  | int                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.sequence_loop_count_is_finite`                        | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.simulate`                                             | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.source_complete_event_output_terminal`                | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.source_complete_event_pulse_polarity`                 | :py:data:`Polarity`                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.source_complete_event_pulse_width`                    | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.source_delay`                                         | float in seconds or datetime.timedelta |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.source_mode`                                          | :py:data:`SourceMode`                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.source_trigger_type`                                  | :py:data:`TriggerType`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.specific_driver_description`                          | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.specific_driver_prefix`                               | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.specific_driver_revision`                             | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.specific_driver_vendor`                               | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.start_trigger_type`                                   | :py:data:`TriggerType`                 |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.supported_instrument_models`                          | str                                    |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.transient_response`                                   | :py:data:`TransientResponse`           |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.voltage_compensation_frequency`                       | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.voltage_gain_bandwidth`                               | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.voltage_level`                                        | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.voltage_level_autorange`                              | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.voltage_level_range`                                  | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.voltage_limit`                                        | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.voltage_limit_autorange`                              | bool                                   |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.voltage_limit_high`                                   | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.voltage_limit_low`                                    | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.voltage_limit_range`                                  | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+
| :py:attr:`nidcpower.Session.voltage_pole_zero_ratio`                              | float                                  |
+-----------------------------------------------------------------------------------+----------------------------------------+

Methods
-------

+------------------------------------------------------------------------------+
| Method name                                                                  |
+==============================================================================+
| :py:func:`nidcpower.Session.abort`                                           |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.commit`                                          |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.configure_aperture_time`                         |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.configure_digital_edge_measure_trigger`          |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.configure_digital_edge_pulse_trigger`            |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.configure_digital_edge_sequence_advance_trigger` |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.configure_digital_edge_source_trigger`           |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.configure_digital_edge_start_trigger`            |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.disable`                                         |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.fetch_multiple`                                  |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.get_channel_name`                                |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.get_ext_cal_last_date_and_time`                  |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.get_ext_cal_last_temp`                           |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.get_ext_cal_recommended_interval`                |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.get_self_cal_last_date_and_time`                 |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.get_self_cal_last_temp`                          |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.measure`                                         |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.measure_multiple`                                |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.query_in_compliance`                             |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.query_max_current_limit`                         |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.query_max_voltage_level`                         |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.query_min_current_limit`                         |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.query_output_state`                              |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.read_current_temperature`                        |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.reset`                                           |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.reset_device`                                    |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.reset_with_defaults`                             |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.self_cal`                                        |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.self_test`                                       |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.send_software_edge_trigger`                      |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.set_sequence`                                    |
+------------------------------------------------------------------------------+
| :py:func:`nidcpower.Session.wait_for_event`                                  |
+------------------------------------------------------------------------------+

