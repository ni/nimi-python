NI-SWITCH Functions
===================

.. py:currentmodule:: niswitch

.. function:: _abort_scan()

.. function:: can_connect(channel1, channel2, path_capability)

    :param channel1:

    :type channel1: ViConstString
    :param channel2:

    :type channel2: ViConstString

    :rtype: ViInt32


.. function:: _clear_error()

.. function:: clear_interchange_warnings()

.. function:: commit()

.. function:: configure_scan_list(scanlist, scan_mode)

    :param scanlist:

    :type scanlist: ViConstString
    :param scan_mode:

    :type scan_mode: ViInt32

.. function:: configure_scan_trigger(scan_delay, trigger_input, scan_advanced_output)

    :param scan_delay:

    :type scan_delay: ViReal64
    :param trigger_input:

    :type trigger_input: ViInt32
    :param scan_advanced_output:

    :type scan_advanced_output: ViInt32

.. function:: connect(channel1, channel2)

    :param channel1:

    :type channel1: ViConstString
    :param channel2:

    :type channel2: ViConstString

.. function:: connect_multiple(connection_list)

    :param connection_list:

    :type connection_list: ViConstString

.. function:: disable()

.. function:: disconnect(channel1, channel2)

    :param channel1:

    :type channel1: ViConstString
    :param channel2:

    :type channel2: ViConstString

.. function:: disconnect_all()

.. function:: disconnect_multiple(disconnection_list)

    :param disconnection_list:

    :type disconnection_list: ViConstString

.. function:: _get_attribute_vi_boolean(channel_name, attribute_id, attribute_value)

    :param channel_name:

    :type channel_name: ViConstString
    :param attribute_id:

    :type attribute_id: ViAttr

    :rtype: ViBoolean


.. function:: _get_attribute_vi_int32(channel_name, attribute_id, attribute_value)

    :param channel_name:

    :type channel_name: ViConstString
    :param attribute_id:

    :type attribute_id: ViAttr

    :rtype: ViInt32


.. function:: _get_attribute_vi_real64(channel_name, attribute_id, attribute_value)

    :param channel_name:

    :type channel_name: ViConstString
    :param attribute_id:

    :type attribute_id: ViAttr

    :rtype: ViReal64


.. function:: _get_attribute_vi_session(channel_name, attribute_id, attribute_value)

    :param channel_name:

    :type channel_name: ViConstString
    :param attribute_id:

    :type attribute_id: ViAttr

    :rtype: ViSession


.. function:: _get_attribute_vi_string(channel_name, attribute_id, array_size, attribute_value)

    :param channel_name:

    :type channel_name: ViConstString
    :param attribute_id:

    :type attribute_id: ViAttr
    :param array_size:

    :type array_size: ViInt32

.. function:: get_channel_name(index, buffer_size, channel_name_buffer)

    :param index:

    :type index: ViInt32
    :param buffer_size:

    :type buffer_size: ViInt32

.. function:: _get_error(code, buffersize, description)

    :param buffersize:

    :type buffersize: ViInt32

    :rtype: ViStatus


.. function:: get_next_coercion_record(buffer_size, coercion_record)

    :param buffer_size:

    :type buffer_size: ViInt32

.. function:: get_next_interchange_warning(buffer_size, interchange_warning)

    :param buffer_size:

    :type buffer_size: ViInt32

.. function:: get_path(channel1, channel2, buffer_size, path)

    :param channel1:

    :type channel1: ViConstString
    :param channel2:

    :type channel2: ViConstString
    :param buffer_size:

    :type buffer_size: ViInt32

.. function:: get_relay_count(relay_name, relay_count)

    :param relay_name:

    :type relay_name: ViConstString

    :rtype: ViInt32


.. function:: get_relay_name(index, relay_name_buffer_size, relay_name_buffer)

    :param index:

    :type index: ViInt32
    :param relay_name_buffer_size:

    :type relay_name_buffer_size: ViInt32

.. function:: get_relay_position(relay_name, relay_position)

    :param relay_name:

    :type relay_name: ViConstString

    :rtype: ViInt32


.. function:: _init_with_options(resource_name, id_query, reset_device, options_string)

    :param resource_name:

    :type resource_name: ViRsrc
    :param id_query:

    :type id_query: ViBoolean
    :param reset_device:

    :type reset_device: ViBoolean
    :param options_string:

    :type options_string: ViConstString

    :rtype: ViSession


.. function:: init_with_topology(resource_name, topology, simulate, reset_device)

    :param resource_name:

    :type resource_name: ViRsrc
    :param topology:

    :type topology: ViConstString
    :param simulate:

    :type simulate: ViBoolean
    :param reset_device:

    :type reset_device: ViBoolean

    :rtype: ViSession


.. function:: _initiate_scan()

.. function:: is_debounced(is_debounced)

    :rtype: ViBoolean


.. function:: is_scanning(is_scanning)

    :rtype: ViBoolean


.. function:: _lock_session(caller_has_lock)

    :rtype: ViBoolean


.. function:: relay_control(relay_name, relay_action)

    :param relay_name:

    :type relay_name: ViConstString
    :param relay_action:

    :type relay_action: ViInt32

.. function:: reset_interchange_check()

.. function:: reset_with_defaults()

.. function:: route_scan_advanced_output(scan_advanced_output_connector, scan_advanced_output_bus_line, invert)

    :param scan_advanced_output_connector:

    :type scan_advanced_output_connector: ViInt32
    :param scan_advanced_output_bus_line:

    :type scan_advanced_output_bus_line: ViInt32
    :param invert:

    :type invert: ViBoolean

.. function:: route_trigger_input(trigger_input_connector, trigger_input_bus_line, invert)

    :param trigger_input_connector:

    :type trigger_input_connector: ViInt32
    :param trigger_input_bus_line:

    :type trigger_input_bus_line: ViInt32
    :param invert:

    :type invert: ViBoolean

.. function:: scan(scanlist, initiation)

    :param scanlist:

    :type scanlist: ViConstString
    :param initiation:

    :type initiation: ViInt16

.. function:: send_software_trigger()

.. function:: _set_attribute_vi_boolean(channel_name, attribute_id, attribute_value)

    :param channel_name:

    :type channel_name: ViConstString
    :param attribute_id:

    :type attribute_id: ViAttr
    :param attribute_value:

    :type attribute_value: ViBoolean

.. function:: _set_attribute_vi_int32(channel_name, attribute_id, attribute_value)

    :param channel_name:

    :type channel_name: ViConstString
    :param attribute_id:

    :type attribute_id: ViAttr
    :param attribute_value:

    :type attribute_value: ViInt32

.. function:: _set_attribute_vi_real64(channel_name, attribute_id, attribute_value)

    :param channel_name:

    :type channel_name: ViConstString
    :param attribute_id:

    :type attribute_id: ViAttr
    :param attribute_value:

    :type attribute_value: ViReal64

.. function:: _set_attribute_vi_session(channel_name, attribute_id, attribute_value)

    :param channel_name:

    :type channel_name: ViConstString
    :param attribute_id:

    :type attribute_id: ViAttr
    :param attribute_value:

    :type attribute_value: ViSession

.. function:: _set_attribute_vi_string(channel_name, attribute_id, attribute_value)

    :param channel_name:

    :type channel_name: ViConstString
    :param attribute_id:

    :type attribute_id: ViAttr
    :param attribute_value:

    :type attribute_value: ViChar

.. function:: set_continuous_scan(continuous_scan)

    :param continuous_scan:

    :type continuous_scan: ViBoolean

.. function:: set_path(path_list)

    :param path_list:

    :type path_list: ViConstString

.. function:: _unlock_session(caller_has_lock)

    :rtype: ViBoolean


.. function:: wait_for_debounce(maximum_time_ms)

    :param maximum_time_ms:

    :type maximum_time_ms: ViInt32

.. function:: wait_for_scan_complete(maximum_time_ms)

    :param maximum_time_ms:

    :type maximum_time_ms: ViInt32

.. function:: _close()

.. function:: error_message(error_code, error_message)

    :param error_code:

    :type error_code: ViStatus

    :rtype: ViString


.. function:: error_query(error_code, error_message)

    :rtype: tuple (error_code, error_message)

        WHERE

        error_code (ViInt32):

        error_message (ViString):


.. function:: reset()

.. function:: revision_query(instrument_driver_revision, firmware_revision)

    :rtype: tuple (instrument_driver_revision, firmware_revision)

        WHERE

        instrument_driver_revision (ViString):

        firmware_revision (ViChar):


.. function:: self_test(self_test_result, self_test_message)

    :rtype: tuple (self_test_result, self_test_message)

        WHERE

        self_test_result (ViInt16):

        self_test_message (ViString):



