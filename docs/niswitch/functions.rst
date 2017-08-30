niswitch.Session methods
========================

.. py:currentmodule:: niswitch

.. function:: can_connect(channel1, channel2, path_capability)

    :param channel1:

    :type channel1: str
    :param channel2:

    :type channel2: str

    :rtype: enums.PathCapability


.. function:: clear_interchange_warnings()

.. function:: commit()

.. function:: configure_scan_list(scanlist, scan_mode)

    :param scanlist:

    :type scanlist: str
    :param scan_mode:

    :type scan_mode: :py:data:`niswitch.ScanMode`

.. function:: configure_scan_trigger(scan_delay, trigger_input, scan_advanced_output)

    :param scan_delay:

    :type scan_delay: float
    :param trigger_input:

    :type trigger_input: :py:data:`niswitch.TriggerInputConfigureScanTrigger`
    :param scan_advanced_output:

    :type scan_advanced_output: :py:data:`niswitch.ScanAdvancedOutputConfigureScanTrigger`

.. function:: connect(channel1, channel2)

    :param channel1:

    :type channel1: str
    :param channel2:

    :type channel2: str

.. function:: connect_multiple(connection_list)

    :param connection_list:

    :type connection_list: str

.. function:: disable()

.. function:: disconnect(channel1, channel2)

    :param channel1:

    :type channel1: str
    :param channel2:

    :type channel2: str

.. function:: disconnect_all()

.. function:: disconnect_multiple(disconnection_list)

    :param disconnection_list:

    :type disconnection_list: str

.. function:: get_channel_name(index, buffer_size, channel_name_buffer)

    :param index:

    :type index: int
    :param buffer_size:

    :type buffer_size: int

.. function:: get_next_coercion_record(buffer_size, coercion_record)

    :param buffer_size:

    :type buffer_size: int

.. function:: get_next_interchange_warning(buffer_size, interchange_warning)

    :param buffer_size:

    :type buffer_size: int

.. function:: get_path(channel1, channel2, buffer_size, path)

    :param channel1:

    :type channel1: str
    :param channel2:

    :type channel2: str
    :param buffer_size:

    :type buffer_size: int

.. function:: get_relay_count(relay_name, relay_count)

    :param relay_name:

    :type relay_name: str

    :rtype: ViInt32


.. function:: get_relay_name(index, relay_name_buffer_size, relay_name_buffer)

    :param index:

    :type index: int
    :param relay_name_buffer_size:

    :type relay_name_buffer_size: int

.. function:: get_relay_position(relay_name, relay_position)

    :param relay_name:

    :type relay_name: str

    :rtype: enums.RelayPosition


.. function:: init_with_topology(resource_name, topology, simulate, reset_device)

    :param resource_name:

    :type resource_name: str
    :param topology:

    :type topology: str
    :param simulate:

    :type simulate: bool
    :param reset_device:

    :type reset_device: bool

    :rtype: ViSession


.. function:: is_debounced(is_debounced)

    :rtype: ViBoolean


.. function:: is_scanning(is_scanning)

    :rtype: ViBoolean


.. function:: relay_control(relay_name, relay_action)

    :param relay_name:

    :type relay_name: str
    :param relay_action:

    :type relay_action: :py:data:`niswitch.RelayAction`

.. function:: reset_interchange_check()

.. function:: reset_with_defaults()

.. function:: route_scan_advanced_output(scan_advanced_output_connector, scan_advanced_output_bus_line, invert)

    :param scan_advanced_output_connector:

    :type scan_advanced_output_connector: :py:data:`niswitch.TriggerInputConnector`
    :param scan_advanced_output_bus_line:

    :type scan_advanced_output_bus_line: :py:data:`niswitch.TriggerInputBusLine`
    :param invert:

    :type invert: bool

.. function:: route_trigger_input(trigger_input_connector, trigger_input_bus_line, invert)

    :param trigger_input_connector:

    :type trigger_input_connector: :py:data:`niswitch.TriggerInputConnector`
    :param trigger_input_bus_line:

    :type trigger_input_bus_line: :py:data:`niswitch.TriggerInputBusLine`
    :param invert:

    :type invert: bool

.. function:: scan(scanlist, initiation)

    :param scanlist:

    :type scanlist: str
    :param initiation:

    :type initiation: int

.. function:: send_software_trigger()

.. function:: set_continuous_scan(continuous_scan)

    :param continuous_scan:

    :type continuous_scan: bool

.. function:: set_path(path_list)

    :param path_list:

    :type path_list: str

.. function:: wait_for_debounce(maximum_time_ms)

    :param maximum_time_ms:

    :type maximum_time_ms: int

.. function:: wait_for_scan_complete(maximum_time_ms)

    :param maximum_time_ms:

    :type maximum_time_ms: int

.. function:: error_message(error_code, error_message)

    :param error_code:

    :type error_code: int

    :rtype: ViChar


.. function:: error_query(error_code, error_message)

    :rtype: tuple (error_code, error_message)

        WHERE

        error_code (ViInt32): 

        error_message (ViChar): 


.. function:: reset()

.. function:: revision_query(instrument_driver_revision, firmware_revision)

    :rtype: tuple (instrument_driver_revision, firmware_revision)

        WHERE

        instrument_driver_revision (ViChar): 

        firmware_revision (ViChar): 


.. function:: self_test(self_test_result, self_test_message)

    :rtype: tuple (self_test_result, self_test_message)

        WHERE

        self_test_result (ViInt16): 

        self_test_message (ViChar): 



