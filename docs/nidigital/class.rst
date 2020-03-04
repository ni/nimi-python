.. py:module:: nidigital

Session
=======

.. py:class:: Session(self, resource_name, id_query=False, reset_device=False, options={})

    

    TBD

    



    :param resource_name:
        

        


    :type resource_name: str

    :param id_query:
        

        


    :type id_query: bool

    :param reset_device:
        

        


    :type reset_device: bool

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


Methods
=======

abort
-----

    .. py:currentmodule:: nidigital.Session

    .. py:method:: abort()

            TBD

            



abort_keep_alive
----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: abort_keep_alive()

            TBD

            



apply_levels_and_timing
-----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: apply_levels_and_timing(site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins)

            TBD

            



            :param site_list:


                


            :type site_list: str
            :param levels_sheet:


                


            :type levels_sheet: str
            :param timing_sheet:


                


            :type timing_sheet: str
            :param initial_state_high_pins:


                


            :type initial_state_high_pins: str
            :param initial_state_low_pins:


                


            :type initial_state_low_pins: str
            :param initial_state_tristate_pins:


                


            :type initial_state_tristate_pins: str

apply_tdr_offsets
-----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: apply_tdr_offsets(offsets)

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].apply_tdr_offsets(offsets)


            :param offsets:


                


            :type offsets: list of float

burst_pattern
-------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: burst_pattern(site_list, start_label, select_digital_function, wait_until_done, timeout)

            TBD

            



            :param site_list:


                


            :type site_list: str
            :param start_label:


                


            :type start_label: str
            :param select_digital_function:


                


            :type select_digital_function: bool
            :param wait_until_done:


                


            :type wait_until_done: bool
            :param timeout:


                


            :type timeout: float

clear_error
-----------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: clear_error()

            TBD

            



clock_generator_abort
---------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: clock_generator_abort()

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].clock_generator_abort()


clock_generator_generate_clock
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: clock_generator_generate_clock(frequency, select_digital_function)

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].clock_generator_generate_clock(frequency, select_digital_function)


            :param frequency:


                


            :type frequency: float
            :param select_digital_function:


                


            :type select_digital_function: bool

clock_generator_initiate
------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: clock_generator_initiate()

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].clock_generator_initiate()


close
-----

    .. py:currentmodule:: nidigital.Session

    .. py:method:: close()

            TBD

            

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: commit()

            TBD

            



configure_active_load_levels
----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_active_load_levels(iol, ioh, vcom)

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].configure_active_load_levels(iol, ioh, vcom)


            :param iol:


                


            :type iol: float
            :param ioh:


                


            :type ioh: float
            :param vcom:


                


            :type vcom: float

configure_pattern_burst_sites
-----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_pattern_burst_sites(site_list)

            TBD

            



            :param site_list:


                


            :type site_list: str

configure_time_set_compare_edges_strobe
---------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_compare_edges_strobe(time_set, strobe_edge)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].configure_time_set_compare_edges_strobe(time_set, strobe_edge)


            :param time_set:


                


            :type time_set: str
            :param strobe_edge:


                


            :type strobe_edge: float

configure_time_set_compare_edges_strobe2x
-----------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_compare_edges_strobe2x(time_set, strobe_edge, strobe2_edge)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].configure_time_set_compare_edges_strobe2x(time_set, strobe_edge, strobe2_edge)


            :param time_set:


                


            :type time_set: str
            :param strobe_edge:


                


            :type strobe_edge: float
            :param strobe2_edge:


                


            :type strobe2_edge: float

configure_time_set_drive_edges
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_edges(time_set, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].configure_time_set_drive_edges(time_set, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)


            :param time_set:


                


            :type time_set: str
            :param format:


                


            :type format: int
            :param drive_on_edge:


                


            :type drive_on_edge: float
            :param drive_data_edge:


                


            :type drive_data_edge: float
            :param drive_return_edge:


                


            :type drive_return_edge: float
            :param drive_off_edge:


                


            :type drive_off_edge: float

configure_time_set_drive_edges2x
--------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_edges2x(time_set, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].configure_time_set_drive_edges2x(time_set, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)


            :param time_set:


                


            :type time_set: str
            :param format:


                


            :type format: int
            :param drive_on_edge:


                


            :type drive_on_edge: float
            :param drive_data_edge:


                


            :type drive_data_edge: float
            :param drive_return_edge:


                


            :type drive_return_edge: float
            :param drive_off_edge:


                


            :type drive_off_edge: float
            :param drive_data2_edge:


                


            :type drive_data2_edge: float
            :param drive_return2_edge:


                


            :type drive_return2_edge: float

configure_time_set_drive_format
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_format(time_set, drive_format)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].configure_time_set_drive_format(time_set, drive_format)


            :param time_set:


                


            :type time_set: str
            :param drive_format:


                


            :type drive_format: int

configure_time_set_edge
-----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_edge(time_set, edge, time)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].configure_time_set_edge(time_set, edge, time)


            :param time_set:


                


            :type time_set: str
            :param edge:


                


            :type edge: int
            :param time:


                


            :type time: float

configure_time_set_edge_multiplier
----------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_edge_multiplier(time_set, edge_multiplier)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].configure_time_set_edge_multiplier(time_set, edge_multiplier)


            :param time_set:


                


            :type time_set: str
            :param edge_multiplier:


                


            :type edge_multiplier: int

configure_time_set_period
-------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_period(time_set, period)

            TBD

            



            :param time_set:


                


            :type time_set: str
            :param period:


                


            :type period: float

configure_voltage_levels
------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_voltage_levels(vil, vih, vol, voh, vterm)

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].configure_voltage_levels(vil, vih, vol, voh, vterm)


            :param vil:


                


            :type vil: float
            :param vih:


                


            :type vih: float
            :param vol:


                


            :type vol: float
            :param voh:


                


            :type voh: float
            :param vterm:


                


            :type vterm: float

create_capture_waveform_from_file_digicapture
---------------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_capture_waveform_from_file_digicapture(waveform_name, waveform_file_path)

            TBD

            



            :param waveform_name:


                


            :type waveform_name: str
            :param waveform_file_path:


                


            :type waveform_file_path: str

create_capture_waveform_parallel
--------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_capture_waveform_parallel(waveform_name)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].create_capture_waveform_parallel(waveform_name)


            :param waveform_name:


                


            :type waveform_name: str

create_capture_waveform_serial
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_capture_waveform_serial(waveform_name, sample_width, bit_order)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].create_capture_waveform_serial(waveform_name, sample_width, bit_order)


            :param waveform_name:


                


            :type waveform_name: str
            :param sample_width:


                


            :type sample_width: int
            :param bit_order:


                


            :type bit_order: int

create_source_waveform_from_file_tdms
-------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_source_waveform_from_file_tdms(waveform_name, waveform_file_path, write_waveform_data)

            TBD

            



            :param waveform_name:


                


            :type waveform_name: str
            :param waveform_file_path:


                


            :type waveform_file_path: str
            :param write_waveform_data:


                


            :type write_waveform_data: bool

create_source_waveform_parallel
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_source_waveform_parallel(waveform_name, data_mapping)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].create_source_waveform_parallel(waveform_name, data_mapping)


            :param waveform_name:


                


            :type waveform_name: str
            :param data_mapping:


                


            :type data_mapping: int

create_source_waveform_serial
-----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_source_waveform_serial(waveform_name, data_mapping, sample_width, bit_order)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].create_source_waveform_serial(waveform_name, data_mapping, sample_width, bit_order)


            :param waveform_name:


                


            :type waveform_name: str
            :param data_mapping:


                


            :type data_mapping: int
            :param sample_width:


                


            :type sample_width: int
            :param bit_order:


                


            :type bit_order: int

create_time_set
---------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_time_set(name)

            TBD

            



            :param name:


                


            :type name: str

delete_all_time_sets
--------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: delete_all_time_sets()

            TBD

            



disable_sites
-------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: disable_sites(site_list)

            TBD

            



            :param site_list:


                


            :type site_list: str

enable_sites
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: enable_sites(site_list)

            TBD

            



            :param site_list:


                


            :type site_list: str

fetch_capture_waveform
----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: fetch_capture_waveform(site_list, waveform_name, samples_to_read, timeout)

            Returns dictionary where each key is the site number and the value is array.array of unsigned int

            



            :param site_list:


                


            :type site_list: str
            :param waveform_name:


                


            :type waveform_name: str
            :param samples_to_read:


                


            :type samples_to_read: int
            :param timeout:


                


            :type timeout: float or datetime.timedelta

            :rtype: { site: data, site: data, ... }
            :return:


                    Dictionary where each key is the site number and the value is array.array of unsigned int

                    



fetch_history_ram_cycle_information
-----------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: fetch_history_ram_cycle_information(site, position, samples_to_read)

            Returns the pattern information acquired for the specified cycles.

            If the pattern is using the edge multiplier feature, cycle numbers represent tester cycles, each of which may
            consist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return
            :py:data:`~nidigital.DigitalState.PIN_STATE_NOT_ACQUIRED` for DUT cycles where those pins do not have edges defined.

            If pins are not specified, pin list from the pattern containing the start label is used. Call
            :py:meth:`nidigital.Session.get_pattern_pin_names` with the start label to retrieve the pins
            associated with the pattern burst.

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].fetch_history_ram_cycle_information(site, position, samples_to_read)


            :param site:


                Site on which to retrieve History RAM data. Specify site as a string in the form of siteN,
                where N is the site number. The VI returns an error if more than one site is specified.

                


            :type site: str
            :param position:


                Sample index from which to start fetching pattern information.

                


            :type position: int
            :param samples_to_read:


                Number of samples to fetch. A value of -1 specifies to fetch all available samples.

                


            :type samples_to_read: int

            :rtype: list of HistoryRAMCycleInformation
            :return:


                    Returns a list of class instances with
                    the following information about each pattern cycle:

                    -  **pattern_name** (str)  Name of the pattern for the acquired cycle.
                    -  **time_set_name** (str) Time set for the acquired cycle.
                    -  **vector_number** (int) Vector number within the pattern for the acquired cycle. Vector numbers start
                       at 0 from the beginning of the pattern.
                    -  **cycle_number** (int) Cycle number acquired by this History RAM sample. Cycle numbers start at 0
                       from the beginning of the pattern burst.
                    -  **scan_cycle_number** (int) Scan cycle number acquired by this History RAM sample. Scan cycle numbers
                       start at 0 from the first cycle of the scan vector. Scan cycle numbers are -1 for cycles that do not
                       have a scan opcode.
                    -  **expected_pin_states** (list of list of enums.DigitalState) Pin states as expected by the loaded
                       pattern in the order specified in the pin list. Pins without defined edges in the specified DUT cycle
                       will have a value of :py:data:`~nidigital.DigitalState.PIN_STATE_NOT_ACQUIRED`.
                       Length of the outer list will be equal to the value of edge multiplier for the given vector.
                       Length of the inner list will be equal to the number of pins requested.
                    -  **actual_pin_states** (list of list of enums.DigitalState) Pin states acquired by History RAM in the
                       order specified in the pin list. Pins without defined edges in the specified DUT cycle will have a
                       value of :py:data:`~nidigital.DigitalState.PIN_STATE_NOT_ACQUIRED`.
                       Length of the outer list will be equal to the value of edge multiplier for the given vector.
                       Length of the inner list will be equal to the number of pins requested.
                    -  **per_pin_pass_fail** (list of list of bool) Pass fail information for pins in the order specified in
                       the pin list. Pins without defined edges in the specified DUT cycle will have a value of pass (True).
                       Length of the outer list will be equal to the value of edge multiplier for the given vector.
                       Length of the inner list will be equal to the number of pins requested.

                    



frequency_counter_measure_frequency
-----------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: frequency_counter_measure_frequency()

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].frequency_counter_measure_frequency()


            :rtype: list of float
            :return:


                    



get_channel_name
----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_channel_name(index)

            TBD

            



            :param index:


                


            :type index: int

            :rtype: str
            :return:


                    



get_channel_name_from_string
----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_channel_name_from_string(index)

            TBD

            



            :param index:


                


            :type index: str

            :rtype: str
            :return:


                    



get_fail_count
--------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_fail_count()

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].get_fail_count()


            :rtype: list of int
            :return:


                    



get_history_ram_sample_count
----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_history_ram_sample_count(site)

            TBD

            



            :param site:


                


            :type site: str

            :rtype: int
            :return:


                    



get_pattern_name
----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_pattern_name(pattern_index)

            TBD

            



            :param pattern_index:


                


            :type pattern_index: int

            :rtype: str
            :return:


                    



get_pattern_pin_list
--------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_pattern_pin_list(start_label)

            TBD

            



            :param start_label:


                


            :type start_label: str

            :rtype: str
            :return:


                    



get_pattern_pin_names
---------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_pattern_pin_names(start_label)

            Returns the names of the pins referenced by the pattern.

            



            :param start_label:


                Pattern name or exported pattern label from which to get the pin names referenced by the pattern.

                


            :type start_label: str

            :rtype: list of str
            :return:


                    List of pin names referenced by the pattern.

                    



get_pin_results_pin_information
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_pin_results_pin_information()

            Returns a list of named tuples (PinInfo) that <FILL IN THE BLANK HERE>

            Fields in PinInfo:

            - **pin_name** (str)
            - **site_number** (int)
            - **channel_name** (str)

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].get_pin_results_pin_information()


            :rtype: list of PinInfo
            :return:


                    List of named tuples with fields:

                    - **pin_name** (str)
                    - **site_number** (int)
                    - **channel_name** (str)

                    



get_site_pass_fail
------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_site_pass_fail(site_list)

            TBD

            



            :param site_list:


                


            :type site_list: str

            :rtype: list of bool
            :return:


                    



get_site_results_site_numbers
-----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_site_results_site_numbers(site_list, site_result_type)

            TBD

            



            :param site_list:


                


            :type site_list: str
            :param site_result_type:


                


            :type site_result_type: :py:data:`nidigital.SiteResult`

            :rtype: list of int
            :return:


                    



get_time_set_drive_format
-------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_drive_format(time_set)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].get_time_set_drive_format(time_set)


            :param time_set:


                


            :type time_set: str

            :rtype: int
            :return:


                    



get_time_set_edge
-----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_edge(time_set, edge)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].get_time_set_edge(time_set, edge)


            :param time_set:


                


            :type time_set: str
            :param edge:


                


            :type edge: int

            :rtype: float
            :return:


                    



get_time_set_edge_multiplier
----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_edge_multiplier(time_set)

            TBD

            


            .. tip:: This method requires repeated capabilities (pins). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.pins[0,1].get_time_set_edge_multiplier(time_set)


            :param time_set:


                


            :type time_set: str

            :rtype: int
            :return:


                    



get_time_set_name
-----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_name(time_set_index)

            TBD

            



            :param time_set_index:


                


            :type time_set_index: int

            :rtype: str
            :return:


                    



get_time_set_period
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_period(time_set)

            TBD

            



            :param time_set:


                


            :type time_set: str

            :rtype: float
            :return:


                    



initiate
--------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: initiate()

            TBD

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



is_done
-------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: is_done()

            TBD

            



            :rtype: bool
            :return:


                    



is_site_enabled
---------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: is_site_enabled(site)

            TBD

            



            :param site:


                


            :type site: str

            :rtype: bool
            :return:


                    



load_levels
-----------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: load_levels(levels_file_path)

            TBD

            



            :param levels_file_path:


                


            :type levels_file_path: str

load_pattern
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: load_pattern(file_path)

            TBD

            



            :param file_path:


                


            :type file_path: str

load_pin_map
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: load_pin_map(pin_map_file_path)

            TBD

            



            :param pin_map_file_path:


                


            :type pin_map_file_path: str

load_specifications
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: load_specifications(specifications_file_path)

            TBD

            



            :param specifications_file_path:


                


            :type specifications_file_path: str

load_timing
-----------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: load_timing(timing_file_path)

            TBD

            



            :param timing_file_path:


                


            :type timing_file_path: str

lock
----

    .. py:currentmodule:: nidigital.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`nidigital.Session.lock` method.
        -  A call to NI-Digital Pattern Driver locked the session.
        -  After a call to the :py:meth:`nidigital.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`nidigital.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`nidigital.Session.lock` method and the
           :py:meth:`nidigital.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nidigital.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nidigital.Session.lock` method with a call to
    the :py:meth:`nidigital.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with nidigital.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`nidigital.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited


ppmu_measure
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: ppmu_measure(measurement_type)

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].ppmu_measure(measurement_type)


            :param measurement_type:


                


            :type measurement_type: int

            :rtype: list of float
            :return:


                    



ppmu_source
-----------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: ppmu_source()

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].ppmu_source()


read_sequencer_flag
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_sequencer_flag(flag)

            TBD

            



            :param flag:


                


            :type flag: str

            :rtype: bool
            :return:


                    



read_sequencer_register
-----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_sequencer_register(reg)

            TBD

            



            :param reg:


                


            :type reg: str

            :rtype: int
            :return:


                    



read_static
-----------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_static()

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].read_static()


            :rtype: list of int
            :return:


                    



reset
-----

    .. py:currentmodule:: nidigital.Session

    .. py:method:: reset()

            TBD

            



reset_attribute
---------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: reset_attribute(attribute_id)

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].reset_attribute(attribute_id)


            :param attribute_id:


                


            :type attribute_id: int

reset_device
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: reset_device()

            TBD

            



self_calibrate
--------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: self_calibrate()

            TBD

            



self_test
---------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: self_test()

            TBD

            



send_software_edge_trigger
--------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: send_software_edge_trigger(trigger, trigger_identifier)

            TBD

            



            :param trigger:


                


            :type trigger: int
            :param trigger_identifier:


                


            :type trigger_identifier: str

tdr
---

    .. py:currentmodule:: nidigital.Session

    .. py:method:: tdr(apply_offsets)

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].tdr(apply_offsets)


            :param apply_offsets:


                


            :type apply_offsets: bool

            :rtype: list of float
            :return:


                    



unload_all_patterns
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: unload_all_patterns(unload_keep_alive_pattern)

            TBD

            



            :param unload_keep_alive_pattern:


                


            :type unload_keep_alive_pattern: bool

unload_specifications
---------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: unload_specifications(specifications_file_path)

            TBD

            



            :param specifications_file_path:


                


            :type specifications_file_path: str

unlock
------

    .. py:currentmodule:: nidigital.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`nidigital.Session.lock`. Refer to :py:meth:`nidigital.Session.unlock` for additional
    information on session locks.



wait_until_done
---------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: wait_until_done(timeout)

            TBD

            



            :param timeout:


                


            :type timeout: float

write_sequencer_flag
--------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_sequencer_flag(flag, value)

            TBD

            



            :param flag:


                


            :type flag: str
            :param value:


                


            :type value: bool

write_sequencer_register
------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_sequencer_register(reg, value)

            TBD

            



            :param reg:


                


            :type reg: str
            :param value:


                


            :type value: int

write_source_waveform_broadcast
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_source_waveform_broadcast(waveform_name, waveform_data)

            TBD

            



            :param waveform_name:


                


            :type waveform_name: str
            :param waveform_data:


                


            :type waveform_data: list of int

write_source_waveform_data_from_file_tdms
-----------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_source_waveform_data_from_file_tdms(waveform_name, waveform_file_path)

            TBD

            



            :param waveform_name:


                


            :type waveform_name: str
            :param waveform_file_path:


                


            :type waveform_file_path: str

write_source_waveform_site_unique
---------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_source_waveform_site_unique(waveform_name, waveform_data)

            TBD

            



            :param waveform_name:


                


            :type waveform_name: str
            :param waveform_data:


                Dictionary where each key is the site number and the value is array.array of unsigned int

                


            :type waveform_data: { site: data, site: data, ... }

write_static
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_static(state)

            TBD

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].write_static(state)


            :param state:


                


            :type state: int


.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`niDigital_SetAttributeViInt32()`.

    Repeated capbilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

channels
--------

    .. py:attribute:: nidigital.Session.channels[]

        .. code:: python

            session.channels['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


pins
----

    .. py:attribute:: nidigital.Session.pins[]

        .. code:: python

            session.pins['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


devices
-------

    .. py:attribute:: nidigital.Session.devices[]

        .. code:: python

            session.devices['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


pattern_opcode_events
---------------------

    .. py:attribute:: nidigital.Session.pattern_opcode_events[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.pattern_opcode_events['0-2'].channel_enabled = True

        passes a string of :python:`'patternOpcodeEvent0, patternOpcodeEvent1, patternOpcodeEvent2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.pattern_opcode_events['patternOpcodeEvent0-patternOpcodeEvent2'].channel_enabled = True

        passes a string of :python:`'patternOpcodeEvent0, patternOpcodeEvent1, patternOpcodeEvent2'` to the set attribute function.


conditional_jump_triggers
-------------------------

    .. py:attribute:: nidigital.Session.conditional_jump_triggers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.conditional_jump_triggers['0-2'].channel_enabled = True

        passes a string of :python:`'conditionalJumpTrigger0, conditionalJumpTrigger1, conditionalJumpTrigger2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.conditional_jump_triggers['conditionalJumpTrigger0-conditionalJumpTrigger2'].channel_enabled = True

        passes a string of :python:`'conditionalJumpTrigger0, conditionalJumpTrigger1, conditionalJumpTrigger2'` to the set attribute function.



Properties
==========

active_load_ioh
---------------

    .. py:attribute:: active_load_ioh

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].active_load_ioh = var
                var = session.channels[0,1].active_load_ioh

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_ACTIVE_LOAD_IOH**

active_load_iol
---------------

    .. py:attribute:: active_load_iol

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].active_load_iol = var
                var = session.channels[0,1].active_load_iol

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_ACTIVE_LOAD_IOL**

active_load_vcom
----------------

    .. py:attribute:: active_load_vcom

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].active_load_vcom = var
                var = session.channels[0,1].active_load_vcom

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_ACTIVE_LOAD_VCOM**

cache
-----

    .. py:attribute:: cache

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CACHE**

channel_count
-------------

    .. py:attribute:: channel_count

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CHANNEL_COUNT**

clock_generator_frequency
-------------------------

    .. py:attribute:: clock_generator_frequency

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].clock_generator_frequency = var
                var = session.channels[0,1].clock_generator_frequency

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CLOCK_GENERATOR_FREQUENCY**

clock_generator_is_running
--------------------------

    .. py:attribute:: clock_generator_is_running

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                var = session.channels[0,1].clock_generator_is_running

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CLOCK_GENERATOR_IS_RUNNING**

conditional_jump_trigger_terminal_name
--------------------------------------

    .. py:attribute:: conditional_jump_trigger_terminal_name

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                var = session.channels[0,1].conditional_jump_trigger_terminal_name

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME**

conditional_jump_trigger_type
-----------------------------

    .. py:attribute:: conditional_jump_trigger_type

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].conditional_jump_trigger_type = var
                var = session.channels[0,1].conditional_jump_trigger_type

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CONDITIONAL_JUMP_TRIGGER_TYPE**

cycle_number_history_ram_trigger_cycle_number
---------------------------------------------

    .. py:attribute:: cycle_number_history_ram_trigger_cycle_number

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER**

digital_edge_conditional_jump_trigger_edge
------------------------------------------

    .. py:attribute:: digital_edge_conditional_jump_trigger_edge

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].digital_edge_conditional_jump_trigger_edge = var
                var = session.channels[0,1].digital_edge_conditional_jump_trigger_edge

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.DigitalEdge |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | Yes               |
            +----------------+-------------------+
            | Resettable     | Yes               |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE**

digital_edge_conditional_jump_trigger_source
--------------------------------------------

    .. py:attribute:: digital_edge_conditional_jump_trigger_source

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].digital_edge_conditional_jump_trigger_source = var
                var = session.channels[0,1].digital_edge_conditional_jump_trigger_source

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE**

digital_edge_start_trigger_edge
-------------------------------

    .. py:attribute:: digital_edge_start_trigger_edge

        

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.DigitalEdge |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | No                |
            +----------------+-------------------+
            | Resettable     | Yes               |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

digital_edge_start_trigger_source
---------------------------------

    .. py:attribute:: digital_edge_start_trigger_source

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE**

driver_setup
------------

    .. py:attribute:: driver_setup

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DRIVER_SETUP**

exported_conditional_jump_trigger_output_terminal
-------------------------------------------------

    .. py:attribute:: exported_conditional_jump_trigger_output_terminal

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].exported_conditional_jump_trigger_output_terminal = var
                var = session.channels[0,1].exported_conditional_jump_trigger_output_terminal

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL**

exported_pattern_opcode_event_output_terminal
---------------------------------------------

    .. py:attribute:: exported_pattern_opcode_event_output_terminal

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].exported_pattern_opcode_event_output_terminal = var
                var = session.channels[0,1].exported_pattern_opcode_event_output_terminal

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_start_trigger_output_terminal

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

frequency_counter_measurement_time
----------------------------------

    .. py:attribute:: frequency_counter_measurement_time

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].frequency_counter_measurement_time = var
                var = session.channels[0,1].frequency_counter_measurement_time

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_TIME**

group_capabilities
------------------

    .. py:attribute:: group_capabilities

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_GROUP_CAPABILITIES**

halt_on_keep_alive_opcode
-------------------------

    .. py:attribute:: halt_on_keep_alive_opcode

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HALT_ON_KEEP_ALIVE_OPCODE**

history_ram_buffer_size_per_site
--------------------------------

    .. py:attribute:: history_ram_buffer_size_per_site

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_BUFFER_SIZE_PER_SITE**

history_ram_cycles_to_acquire
-----------------------------

    .. py:attribute:: history_ram_cycles_to_acquire

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_CYCLES_TO_ACQUIRE**

history_ram_max_samples_to_acquire_per_site
-------------------------------------------

    .. py:attribute:: history_ram_max_samples_to_acquire_per_site

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE**

history_ram_number_of_samples_is_finite
---------------------------------------

    .. py:attribute:: history_ram_number_of_samples_is_finite

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE**

history_ram_pretrigger_samples
------------------------------

    .. py:attribute:: history_ram_pretrigger_samples

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_PRETRIGGER_SAMPLES**

history_ram_trigger_type
------------------------

    .. py:attribute:: history_ram_trigger_type

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_TRIGGER_TYPE**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                var = session.channels[0,1].instrument_firmware_revision

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_INSTRUMENT_MODEL**

interchange_check
-----------------

    .. py:attribute:: interchange_check

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_INTERCHANGE_CHECK**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_IO_RESOURCE_DESCRIPTOR**

is_keep_alive_active
--------------------

    .. py:attribute:: is_keep_alive_active

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_IS_KEEP_ALIVE_ACTIVE**

logical_name
------------

    .. py:attribute:: logical_name

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_LOGICAL_NAME**

mask_compare
------------

    .. py:attribute:: mask_compare

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].mask_compare = var
                var = session.channels[0,1].mask_compare

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_MASK_COMPARE**

pattern_label_history_ram_trigger_cycle_offset
----------------------------------------------

    .. py:attribute:: pattern_label_history_ram_trigger_cycle_offset

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET**

pattern_label_history_ram_trigger_label
---------------------------------------

    .. py:attribute:: pattern_label_history_ram_trigger_label

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL**

pattern_label_history_ram_trigger_vector_offset
-----------------------------------------------

    .. py:attribute:: pattern_label_history_ram_trigger_vector_offset

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET**

pattern_opcode_event_terminal_name
----------------------------------

    .. py:attribute:: pattern_opcode_event_terminal_name

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                var = session.channels[0,1].pattern_opcode_event_terminal_name

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_OPCODE_EVENT_TERMINAL_NAME**

ppmu_allow_extended_voltage_range
---------------------------------

    .. py:attribute:: ppmu_allow_extended_voltage_range

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_allow_extended_voltage_range = var
                var = session.channels[0,1].ppmu_allow_extended_voltage_range

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE**

ppmu_aperture_time
------------------

    .. py:attribute:: ppmu_aperture_time

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_aperture_time = var
                var = session.channels[0,1].ppmu_aperture_time

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_APERTURE_TIME**

ppmu_aperture_time_units
------------------------

    .. py:attribute:: ppmu_aperture_time_units

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_aperture_time_units = var
                var = session.channels[0,1].ppmu_aperture_time_units

        The following table lists the characteristics of this property.

            +----------------+-------------------------+
            | Characteristic | Value                   |
            +================+=========================+
            | Datatype       | enums.ApertureTimeUnits |
            +----------------+-------------------------+
            | Permissions    | read-write              |
            +----------------+-------------------------+
            | Channel Based  | Yes                     |
            +----------------+-------------------------+
            | Resettable     | Yes                     |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS**

ppmu_current_level
------------------

    .. py:attribute:: ppmu_current_level

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_current_level = var
                var = session.channels[0,1].ppmu_current_level

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL**

ppmu_current_level_range
------------------------

    .. py:attribute:: ppmu_current_level_range

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_current_level_range = var
                var = session.channels[0,1].ppmu_current_level_range

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL_RANGE**

ppmu_current_limit
------------------

    .. py:attribute:: ppmu_current_limit

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_current_limit = var
                var = session.channels[0,1].ppmu_current_limit

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT**

ppmu_current_limit_behavior
---------------------------

    .. py:attribute:: ppmu_current_limit_behavior

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_current_limit_behavior = var
                var = session.channels[0,1].ppmu_current_limit_behavior

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_BEHAVIOR**

ppmu_current_limit_range
------------------------

    .. py:attribute:: ppmu_current_limit_range

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_current_limit_range = var
                var = session.channels[0,1].ppmu_current_limit_range

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_RANGE**

ppmu_current_limit_supported
----------------------------

    .. py:attribute:: ppmu_current_limit_supported

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                var = session.channels[0,1].ppmu_current_limit_supported

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_SUPPORTED**

ppmu_output_function
--------------------

    .. py:attribute:: ppmu_output_function

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_output_function = var
                var = session.channels[0,1].ppmu_output_function

        The following table lists the characteristics of this property.

            +----------------+--------------------------+
            | Characteristic | Value                    |
            +================+==========================+
            | Datatype       | enums.PPMUOutputFunction |
            +----------------+--------------------------+
            | Permissions    | read-write               |
            +----------------+--------------------------+
            | Channel Based  | Yes                      |
            +----------------+--------------------------+
            | Resettable     | Yes                      |
            +----------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION**

ppmu_voltage_level
------------------

    .. py:attribute:: ppmu_voltage_level

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_voltage_level = var
                var = session.channels[0,1].ppmu_voltage_level

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_VOLTAGE_LEVEL**

ppmu_voltage_limit_high
-----------------------

    .. py:attribute:: ppmu_voltage_limit_high

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_voltage_limit_high = var
                var = session.channels[0,1].ppmu_voltage_limit_high

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_HIGH**

ppmu_voltage_limit_low
----------------------

    .. py:attribute:: ppmu_voltage_limit_low

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].ppmu_voltage_limit_low = var
                var = session.channels[0,1].ppmu_voltage_limit_low

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_LOW**

query_instrument_status
-----------------------

    .. py:attribute:: query_instrument_status

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_QUERY_INSTRUMENT_STATUS**

range_check
-----------

    .. py:attribute:: range_check

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_RANGE_CHECK**

record_coercions
----------------

    .. py:attribute:: record_coercions

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_RECORD_COERCIONS**

selected_function
-----------------

    .. py:attribute:: selected_function

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].selected_function = var
                var = session.channels[0,1].selected_function

        The following table lists the characteristics of this property.

            +----------------+------------------------+
            | Characteristic | Value                  |
            +================+========================+
            | Datatype       | enums.SelectedFunction |
            +----------------+------------------------+
            | Permissions    | read-write             |
            +----------------+------------------------+
            | Channel Based  | Yes                    |
            +----------------+------------------------+
            | Resettable     | Yes                    |
            +----------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SELECTED_FUNCTION**

sequencer_flag_terminal_name
----------------------------

    .. py:attribute:: sequencer_flag_terminal_name

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SEQUENCER_FLAG_TERMINAL_NAME**

serial_number
-------------

    .. py:attribute:: serial_number

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SERIAL_NUMBER**

simulate
--------

    .. py:attribute:: simulate

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SIMULATE**

specific_driver_class_spec_major_version
----------------------------------------

    .. py:attribute:: specific_driver_class_spec_major_version

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION**

specific_driver_class_spec_minor_version
----------------------------------------

    .. py:attribute:: specific_driver_class_spec_minor_version

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_prefix
----------------------

    .. py:attribute:: specific_driver_prefix

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_PREFIX**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_VENDOR**

start_label
-----------

    .. py:attribute:: start_label

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_START_LABEL**

start_trigger_terminal_name
---------------------------

    .. py:attribute:: start_trigger_terminal_name

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_START_TRIGGER_TERMINAL_NAME**

start_trigger_type
------------------

    .. py:attribute:: start_trigger_type

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_START_TRIGGER_TYPE**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SUPPORTED_INSTRUMENT_MODELS**

tdr_endpoint_termination
------------------------

    .. py:attribute:: tdr_endpoint_termination

        

        The following table lists the characteristics of this property.

            +----------------+------------------------------+
            | Characteristic | Value                        |
            +================+==============================+
            | Datatype       | enums.TDREndpointTermination |
            +----------------+------------------------------+
            | Permissions    | read-write                   |
            +----------------+------------------------------+
            | Channel Based  | No                           |
            +----------------+------------------------------+
            | Resettable     | Yes                          |
            +----------------+------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TDR_ENDPOINT_TERMINATION**

tdr_offset
----------

    .. py:attribute:: tdr_offset

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].tdr_offset = var
                var = session.channels[0,1].tdr_offset

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TDR_OFFSET**

termination_mode
----------------

    .. py:attribute:: termination_mode

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].termination_mode = var
                var = session.channels[0,1].termination_mode

        The following table lists the characteristics of this property.

            +----------------+-----------------------+
            | Characteristic | Value                 |
            +================+=======================+
            | Datatype       | enums.TerminationMode |
            +----------------+-----------------------+
            | Permissions    | read-write            |
            +----------------+-----------------------+
            | Channel Based  | Yes                   |
            +----------------+-----------------------+
            | Resettable     | Yes                   |
            +----------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TERMINATION_MODE**

timing_absolute_delay
---------------------

    .. py:attribute:: timing_absolute_delay

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY**

timing_absolute_delay_enabled
-----------------------------

    .. py:attribute:: timing_absolute_delay_enabled

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED**

vih
---

    .. py:attribute:: vih

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].vih = var
                var = session.channels[0,1].vih

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_VIH**

vil
---

    .. py:attribute:: vil

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].vil = var
                var = session.channels[0,1].vil

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_VIL**

voh
---

    .. py:attribute:: voh

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].voh = var
                var = session.channels[0,1].voh

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_VOH**

vol
---

    .. py:attribute:: vol

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].vol = var
                var = session.channels[0,1].vol

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_VOL**

vterm
-----

    .. py:attribute:: vterm

        .. tip:: This property can use repeated capabilities (channels). If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.channels[0,1].vterm = var
                var = session.channels[0,1].vterm

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_VTERM**


NI-TClk Support
===============

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:attr:`nitclk.SessionReference` for a complete list of attributes.


.. contents:: Session


