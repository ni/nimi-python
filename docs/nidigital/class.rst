.. py:module:: nidigital

Session
=======

.. py:class:: Session(self, resource_name: str, id_query: 'bool' = False, reset_device: 'bool' = False, options={})

    

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

    .. py:method:: apply_levels_and_timing(levels_sheet, timing_sheet, initial_state_high_pins=None, initial_state_low_pins=None, initial_state_tristate_pins=None)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param levels_sheet:


                


            :type levels_sheet: str
            :param timing_sheet:


                


            :type timing_sheet: str
            :param initial_state_high_pins:


                Pins or pin groups to initialize to a high state.

                


            :type initial_state_high_pins: basic sequence types or str
            :param initial_state_low_pins:


                Pins or pin groups to initialize to a low state.

                


            :type initial_state_low_pins: basic sequence types or str
            :param initial_state_tristate_pins:


                Pins or pin groups to initialize to a non-drive state (X).

                


            :type initial_state_tristate_pins: basic sequence types or str

apply_tdr_offsets
-----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: apply_tdr_offsets(offsets)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param offsets:


                


            :type offsets: basic sequence of hightime.timedelta, datetime.timedelta, or float in seconds

burst_pattern
-------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: burst_pattern(start_label, select_digital_function=True, wait_until_done=True, timeout=hightime.timedelta(seconds=10.0))

            Uses the start_label you specify to burst the pattern on the sites you specify. If you
            specify wait_until_done as True, waits for the burst to complete, and returns comparison results for each site.

            Digital pins retain their state at the end of a pattern burst until the first vector of the pattern burst, a call to
            :py:meth:`nidigital.Session.write_static`, or a call to :py:meth:`nidigital.Session.apply_levels_and_timing`.

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param start_label:


                


            :type start_label: str
            :param select_digital_function:


                


            :type select_digital_function: bool
            :param wait_until_done:


                


            :type wait_until_done: bool
            :param timeout:


                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: { int: bool, int: bool, ... }
            :return:


                    Dictionary where each key is a site number and value is pass/fail,
                    if wait_until_done is specified as True. Else, None.

                    



clock_generator_abort
---------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: clock_generator_abort()

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


clock_generator_generate_clock
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: clock_generator_generate_clock(frequency, select_digital_function=True)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param frequency:


                


            :type frequency: float
            :param select_digital_function:


                


            :type select_digital_function: bool

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

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param iol:


                


            :type iol: float
            :param ioh:


                


            :type ioh: float
            :param vcom:


                


            :type vcom: float

configure_pattern_burst_sites
-----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_pattern_burst_sites()

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


configure_time_set_compare_edges_strobe
---------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_compare_edges_strobe(time_set_name, strobe_edge)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param time_set_name:


                


            :type time_set_name: str
            :param strobe_edge:


                


            :type strobe_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_compare_edges_strobe2x
-----------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_compare_edges_strobe2x(time_set_name, strobe_edge, strobe2_edge)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param time_set_name:


                


            :type time_set_name: str
            :param strobe_edge:


                


            :type strobe_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param strobe2_edge:


                


            :type strobe2_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_drive_edges
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_edges(time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param time_set_name:


                


            :type time_set_name: str
            :param format:


                


            :type format: :py:data:`nidigital.DriveFormat`
            :param drive_on_edge:


                


            :type drive_on_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_data_edge:


                


            :type drive_data_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_return_edge:


                


            :type drive_return_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_off_edge:


                


            :type drive_off_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_drive_edges2x
--------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_edges2x(time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param time_set_name:


                


            :type time_set_name: str
            :param format:


                


            :type format: :py:data:`nidigital.DriveFormat`
            :param drive_on_edge:


                


            :type drive_on_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_data_edge:


                


            :type drive_data_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_return_edge:


                


            :type drive_return_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_off_edge:


                


            :type drive_off_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_data2_edge:


                


            :type drive_data2_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_return2_edge:


                


            :type drive_return2_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_drive_format
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_format(time_set_name, drive_format)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param time_set_name:


                


            :type time_set_name: str
            :param drive_format:


                


            :type drive_format: :py:data:`nidigital.DriveFormat`

configure_time_set_edge
-----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_edge(time_set_name, edge, time)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param time_set_name:


                


            :type time_set_name: str
            :param edge:


                


            :type edge: :py:data:`nidigital.TimeSetEdgeType`
            :param time:


                


            :type time: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_edge_multiplier
----------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_edge_multiplier(time_set_name, edge_multiplier)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param time_set_name:


                


            :type time_set_name: str
            :param edge_multiplier:


                


            :type edge_multiplier: int

configure_time_set_period
-------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_period(time_set_name, period)

            TBD

            



            :param time_set_name:


                


            :type time_set_name: str
            :param period:


                


            :type period: hightime.timedelta, datetime.timedelta, or float in seconds

configure_voltage_levels
------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_voltage_levels(vil, vih, vol, voh, vterm)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


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

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param waveform_name:


                


            :type waveform_name: str

create_capture_waveform_serial
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_capture_waveform_serial(waveform_name, sample_width, bit_order)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param waveform_name:


                


            :type waveform_name: str
            :param sample_width:


                


            :type sample_width: int
            :param bit_order:


                


            :type bit_order: :py:data:`nidigital.BitOrder`

create_source_waveform_from_file_tdms
-------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_source_waveform_from_file_tdms(waveform_name, waveform_file_path, write_waveform_data=True)

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

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param waveform_name:


                


            :type waveform_name: str
            :param data_mapping:


                


            :type data_mapping: :py:data:`nidigital.SourceDataMapping`

create_source_waveform_serial
-----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_source_waveform_serial(waveform_name, data_mapping, sample_width, bit_order)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param waveform_name:


                


            :type waveform_name: str
            :param data_mapping:


                


            :type data_mapping: :py:data:`nidigital.SourceDataMapping`
            :param sample_width:


                


            :type sample_width: int
            :param bit_order:


                


            :type bit_order: :py:data:`nidigital.BitOrder`

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

    .. py:method:: disable_sites()

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


enable_sites
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: enable_sites()

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


fetch_capture_waveform
----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: fetch_capture_waveform(waveform_name, samples_to_read, timeout=hightime.timedelta(seconds=10.0))

            Returns dictionary where each key is a site number and value is a collection of digital states representing capture waveform data

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param waveform_name:


                


            :type waveform_name: str
            :param samples_to_read:


                


            :type samples_to_read: int
            :param timeout:


                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: { int: memoryview of array.array of unsigned int, int: memoryview of array.array of unsigned int, ... }
            :return:


                    Dictionary where each key is a site number and value is a collection of digital states representing capture waveform data

                    



fetch_history_ram_cycle_information
-----------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: fetch_history_ram_cycle_information(position, samples_to_read)

            Returns the pattern information acquired for the specified cycles.

            If the pattern is using the edge multiplier feature, cycle numbers represent tester cycles, each of which may
            consist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return
            :py:data:`~nidigital.PinState.PIN_STATE_NOT_ACQUIRED` for DUT cycles where those pins do not have edges defined.

            Site number on which to retrieve pattern information must be specified via sites repeated capability.
            The method returns an error if more than one site is specified.

            Pins for which to retrieve pattern information must be specified via pins repeated capability.
            If pins are not specified, pin list from the pattern containing the start label is used. Call
            :py:meth:`nidigital.Session.get_pattern_pin_names` with the start label to retrieve the pins associated with the pattern burst:

            .. code:: python

             session.sites[0].pins['PinA', 'PinB'].fetch_history_ram_cycle_information(0, -1)

            

            .. note:: Before bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire.

                :py:attr:`nidigital.Session.history_ram_trigger_type` should be used to specify the trigger condition on which History RAM
                starts acquiring pattern information.

                If History RAM trigger is configured as :py:data:`~nidigital.HistoryRAMTriggerType.CYCLE_NUMBER`,
                :py:attr:`nidigital.Session.cycle_number_history_ram_trigger_cycle_number` should be used to specify the cycle number on which
                History RAM starts acquiring pattern information.

                If History RAM trigger is configured as :py:data:`~nidigital.HistoryRAMTriggerType.PATTERN_LABEL`,
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_label` should be used to specify the pattern label from which to
                start acquiring pattern information.
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_vector_offset` should be used to specify the number of vectors
                following the specified pattern label from which to start acquiring pattern information.
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_cycle_offset` should be used to specify the number of cycles
                following the specified pattern label and vector offset from which to start acquiring pattern information.

                For all History RAM trigger conditions, :py:attr:`nidigital.Session.history_ram_pretrigger_samples` should be used to specify
                the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
                acquire failed cycles, you must set :py:attr:`nidigital.Session.history_ram_pretrigger_samples` to 0.

                :py:attr:`nidigital.Session.history_ram_cycles_to_acquire` should be used to specify which cycles History RAM acquires after
                the trigger conditions are met.


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


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
                    -  **expected_pin_states** (list of list of enums.PinState) Pin states as expected by the loaded
                       pattern in the order specified in the pin list. Pins without defined edges in the specified DUT cycle
                       will have a value of :py:data:`~nidigital.PinState.PIN_STATE_NOT_ACQUIRED`.
                       Length of the outer list will be equal to the value of edge multiplier for the given vector.
                       Length of the inner list will be equal to the number of pins requested.
                    -  **actual_pin_states** (list of list of enums.PinState) Pin states acquired by History RAM in the
                       order specified in the pin list. Pins without defined edges in the specified DUT cycle will have a
                       value of :py:data:`~nidigital.PinState.PIN_STATE_NOT_ACQUIRED`.
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

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :rtype: list of float
            :return:


                    



get_channel_names
-----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_channel_names(indices)

            Returns a list of channel names for given channel indices.

            This is useful in multi-instrument sessions, where channels are expected to be
            referenced by their fully-qualified names, for example, PXI1Slot3/0.

            



            :param indices:


                Specifies indices for the channels in the session.
                Valid values are from zero to the total number of channels in the session minus one.
                The following types and formats are supported:
                  - int - example: 0
                  - Basic sequence - example: [0, range(2, 4)]
                  - str - example: "0, 2, 3, 1", "0-3", "0:3"

                The input can contain any combination of above types. Both out-of-order and repeated indices are
                supported ([2,3,0], [1,2,2,3]). White space characters, including spaces, tabs, feeds, and
                carriage returns, are allowed within strings. Ranges can be incrementing or decrementing.

                


            :type indices: basic sequence types or str or int

            :rtype: list of str
            :return:


                    Channel names

                    



get_fail_count
--------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_fail_count()

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :rtype: list of int
            :return:


                    



get_history_ram_sample_count
----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_history_ram_sample_count()

            Returns the number of samples History RAM acquired on the last pattern burst.

            

            .. note:: Before bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire.

                :py:attr:`nidigital.Session.history_ram_trigger_type` should be used to specify the trigger condition on which History RAM
                starts acquiring pattern information.

                If History RAM trigger is configured as :py:data:`~nidigital.HistoryRAMTriggerType.CYCLE_NUMBER`,
                :py:attr:`nidigital.Session.cycle_number_history_ram_trigger_cycle_number` should be used to specify the cycle number on which
                History RAM starts acquiring pattern information.

                If History RAM trigger is configured as :py:data:`~nidigital.HistoryRAMTriggerType.PATTERN_LABEL`,
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_label` should be used to specify the pattern label from which to
                start acquiring pattern information.
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_vector_offset` should be used to specify the number of vectors
                following the specified pattern label from which to start acquiring pattern information.
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_cycle_offset` should be used to specify the number of cycles
                following the specified pattern label and vector offset from which to start acquiring pattern information.

                For all History RAM trigger conditions, :py:attr:`nidigital.Session.history_ram_pretrigger_samples` should be used to specify
                the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
                acquire failed cycles, you must set :py:attr:`nidigital.Session.history_ram_pretrigger_samples` to 0.

                :py:attr:`nidigital.Session.history_ram_cycles_to_acquire` should be used to specify which cycles History RAM acquires after
                the trigger conditions are met.


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


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


                    



get_pattern_pin_names
---------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_pattern_pin_names(start_label)

            TBD

            



            :param start_label:


                


            :type start_label: str

            :rtype: list of str
            :return:


                    



get_pin_results_pin_information
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_pin_results_pin_information()

            Returns a list of named tuples (PinInfo) that <FILL IN THE BLANK HERE>

            Fields in PinInfo:

            - **pin_name** (str)
            - **site_number** (int)
            - **channel_name** (str)

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :rtype: list of PinInfo
            :return:


                    List of named tuples with fields:

                    - **pin_name** (str)
                    - **site_number** (int)
                    - **channel_name** (str)

                    



get_site_pass_fail
------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_site_pass_fail()

            Returns dictionary where each key is a site number and value is pass/fail

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :rtype: { int: bool, int: bool, ... }
            :return:


                    Dictionary where each key is a site number and value is pass/fail

                    



get_time_set_drive_format
-------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_drive_format(time_set_name)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param time_set_name:


                


            :type time_set_name: str

            :rtype: :py:data:`nidigital.DriveFormat`
            :return:


                    



get_time_set_edge
-----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_edge(time_set_name, edge)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param time_set_name:


                


            :type time_set_name: str
            :param edge:


                


            :type edge: :py:data:`nidigital.TimeSetEdgeType`

            :rtype: hightime.timedelta
            :return:


                    



get_time_set_edge_multiplier
----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_edge_multiplier(time_set_name)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param time_set_name:


                


            :type time_set_name: str

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

    .. py:method:: get_time_set_period(time_set_name)

            TBD

            



            :param time_set_name:


                


            :type time_set_name: str

            :rtype: hightime.timedelta
            :return:


                    



initiate
--------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: initiate()

            Starts bursting the pattern configured by :py:attr:`nidigital.Session.start_label`,
            causing the NI-Digital sessionto be committed. To stop the
            pattern burst, call :py:meth:`nidigital.Session.abort`. If keep alive pattern is
            bursting when :py:meth:`nidigital.Session.abort` is called or upon exiting the
            context manager, keep alive pattern will not be stopped. To
            stop the keep alive pattern, call :py:meth:`nidigital.Session.abort_keep_alive`.

            

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

    .. py:method:: is_site_enabled()

            TBD

            

            .. note:: The method returns an error if more than one site is specified.


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :rtype: bool
            :return:


                    



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

    .. py:method:: load_pin_map(file_path)

            TBD

            



            :param file_path:


                


            :type file_path: str

load_specifications_levels_and_timing
-------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: load_specifications_levels_and_timing(specifications_file_paths=None, levels_file_paths=None, timing_file_paths=None)

            Loads settings in specifications, levels, and timing sheets. These settings are not
            applied to the digital pattern instrument until :py:meth:`nidigital.Session.apply_levels_and_timing` is called.

            If the levels and timing sheets contains formulas, they are evaluated at load time.
            If the formulas refer to variables, the specifications sheets that define those
            variables must be loaded either first, or at the same time as the levels and timing sheets.

            



            :param specifications_file_paths:


                Absolute file path of one or more specifications files.

                


            :type specifications_file_paths: str or basic sequence of str
            :param levels_file_paths:


                Absolute file path of one or more levels sheet files.

                


            :type levels_file_paths: str or basic sequence of str
            :param timing_file_paths:


                Absolute file path of one or more timing sheet files.

                


            :type timing_file_paths: str or basic sequence of str

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

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param measurement_type:


                


            :type measurement_type: :py:data:`nidigital.PPMUMeasurementType`

            :rtype: list of float
            :return:


                    



ppmu_source
-----------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: ppmu_source()

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


read_sequencer_flag
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_sequencer_flag(flag)

            TBD

            



            :param flag:


                


            :type flag: :py:data:`nidigital.SequencerFlag`

            :rtype: bool
            :return:


                    



read_sequencer_register
-----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_sequencer_register(reg)

            TBD

            



            :param reg:


                


            :type reg: :py:data:`nidigital.SequencerRegister`

            :rtype: int
            :return:


                    



read_static
-----------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_static()

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :rtype: list of :py:data:`nidigital.PinState`
            :return:


                    



reset
-----

    .. py:currentmodule:: nidigital.Session

    .. py:method:: reset()

            TBD

            



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

            Forces a particular edge-based trigger to occur regardless of how the
            specified trigger is configured. You can use this method as a software override.

            



            :param trigger:


                Trigger specifies the trigger you want to override.

                +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
                | Defined Values                                         |                                                                                                                                 |
                +========================================================+=================================================================================================================================+
                | :py:data:`~nidigital.SoftwareTrigger.START`            | Overrides the Start trigger. You must specify an empty string in the trigger_identifier parameter.                              |
                +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidigital.SoftwareTrigger.CONDITIONAL_JUMP` | Specifies to route a conditional jump trigger. You must specify a conditional jump trigger in the trigger_identifier parameter. |
                +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger: :py:data:`nidigital.SoftwareTrigger`
            :param trigger_identifier:


                Trigger Identifier specifies the instance of the trigger you want to override.
                If trigger is specified as :py:data:`~nidigital.NIDIGITAL_VAL_START_TRIGGER`, this parameter must be an empty string. If trigger is
                specified as :py:data:`~nidigital.NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER`, allowed values are conditionalJumpTrigger0,
                conditionalJumpTrigger1, conditionalJumpTrigger2, and conditionalJumpTrigger3.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger_identifier: str

tdr
---

    .. py:currentmodule:: nidigital.Session

    .. py:method:: tdr(apply_offsets=True)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param apply_offsets:


                


            :type apply_offsets: bool

            :rtype: list of hightime.timedelta
            :return:


                    



unload_all_patterns
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: unload_all_patterns(unload_keep_alive_pattern=False)

            TBD

            



            :param unload_keep_alive_pattern:


                


            :type unload_keep_alive_pattern: bool

unload_specifications
---------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: unload_specifications(file_paths)

            Unloads the given specifications sheets present in the previously loaded
            specifications files that you select.

            You must call :py:meth:`nidigital.Session.load_specifications_levels_and_timing` to reload the files with updated
            specifications values. You must then call :py:meth:`nidigital.Session.apply_levels_and_timing` in order to apply
            the levels and timing values that reference the updated specifications values.

            



            :param file_paths:


                Absolute file path of one or more loaded specifications files.

                


            :type file_paths: str or basic sequence of str

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

    .. py:method:: wait_until_done(timeout=hightime.timedelta(seconds=10.0))

            TBD

            



            :param timeout:


                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

write_sequencer_flag
--------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_sequencer_flag(flag, value)

            TBD

            



            :param flag:


                


            :type flag: :py:data:`nidigital.SequencerFlag`
            :param value:


                


            :type value: bool

write_sequencer_register
------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_sequencer_register(reg, value)

            TBD

            



            :param reg:


                


            :type reg: :py:data:`nidigital.SequencerRegister`
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


                Dictionary where each key is a site number and value is a collection of samples to use as source data

                


            :type waveform_data: { int: basic sequence of unsigned int, int: basic sequence of unsigned int, ... }

write_static
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_static(state)

            TBD

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                nidigital.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nidigital.Session repeated capabilities container, and calling this method on the result.


            :param state:


                


            :type state: :py:data:`nidigital.WriteStaticPinState`


Properties
==========

active_load_ioh
---------------

    .. py:attribute:: active_load_ioh

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.TriggerType |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | Yes               |
            +----------------+-------------------+
            | Resettable     | Yes               |
            +----------------+-------------------+

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-------------------------------------------------------------+
            | Characteristic | Value                                                       |
            +================+=============================================================+
            | Datatype       | hightime.timedelta, datetime.timedelta, or float in seconds |
            +----------------+-------------------------------------------------------------+
            | Permissions    | read-write                                                  |
            +----------------+-------------------------------------------------------------+
            | Channel Based  | Yes                                                         |
            +----------------+-------------------------------------------------------------+
            | Resettable     | Yes                                                         |
            +----------------+-------------------------------------------------------------+

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

            +----------------+---------------------------------+
            | Characteristic | Value                           |
            +================+=================================+
            | Datatype       | enums.HistoryRAMCyclesToAcquire |
            +----------------+---------------------------------+
            | Permissions    | read-write                      |
            +----------------+---------------------------------+
            | Channel Based  | No                              |
            +----------------+---------------------------------+
            | Resettable     | Yes                             |
            +----------------+---------------------------------+

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

            +----------------+-----------------------------+
            | Characteristic | Value                       |
            +================+=============================+
            | Datatype       | enums.HistoryRAMTriggerType |
            +----------------+-----------------------------+
            | Permissions    | read-write                  |
            +----------------+-----------------------------+
            | Channel Based  | No                          |
            +----------------+-----------------------------+
            | Resettable     | Yes                         |
            +----------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_TRIGGER_TYPE**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------+
            | Characteristic | Value                       |
            +================+=============================+
            | Datatype       | enums.PPMUApertureTimeUnits |
            +----------------+-----------------------------+
            | Permissions    | read-write                  |
            +----------------+-----------------------------+
            | Channel Based  | Yes                         |
            +----------------+-----------------------------+
            | Resettable     | Yes                         |
            +----------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS**

ppmu_current_level
------------------

    .. py:attribute:: ppmu_current_level

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+--------------------------------+
            | Characteristic | Value                          |
            +================+================================+
            | Datatype       | enums.PPMUCurrentLimitBehavior |
            +----------------+--------------------------------+
            | Permissions    | read-write                     |
            +----------------+--------------------------------+
            | Channel Based  | Yes                            |
            +----------------+--------------------------------+
            | Resettable     | Yes                            |
            +----------------+--------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_BEHAVIOR**

ppmu_current_limit_range
------------------------

    .. py:attribute:: ppmu_current_limit_range

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.TriggerType |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | No                |
            +----------------+-------------------+
            | Resettable     | Yes               |
            +----------------+-------------------+

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-------------------------------------------------------------+
            | Characteristic | Value                                                       |
            +================+=============================================================+
            | Datatype       | hightime.timedelta, datetime.timedelta, or float in seconds |
            +----------------+-------------------------------------------------------------+
            | Permissions    | read-write                                                  |
            +----------------+-------------------------------------------------------------+
            | Channel Based  | Yes                                                         |
            +----------------+-------------------------------------------------------------+
            | Resettable     | Yes                                                         |
            +----------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TDR_OFFSET**

termination_mode
----------------

    .. py:attribute:: termination_mode

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-------------------------------------------------------------+
            | Characteristic | Value                                                       |
            +================+=============================================================+
            | Datatype       | hightime.timedelta, datetime.timedelta, or float in seconds |
            +----------------+-------------------------------------------------------------+
            | Permissions    | read-write                                                  |
            +----------------+-------------------------------------------------------------+
            | Channel Based  | No                                                          |
            +----------------+-------------------------------------------------------------+
            | Resettable     | Yes                                                         |
            +----------------+-------------------------------------------------------------+

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            nidigital.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nidigital.Session repeated capabilities container, and calling set/get value on the result.

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


