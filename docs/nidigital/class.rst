.. py:module:: nidigital

Session
=======

.. py:class:: Session(self, resource_name, id_query=False, reset_device=False, options={})

    

    Creates and returns a new session to the specified digital pattern instrument to use in all subsequent method calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to True, which is equivalent to calling the :py:meth:`nidigital.Session.reset` method immediately after initializing the session.

    



    :param resource_name:
        

        The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. **resourceName** can also be a logical IVI name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where ``PXI1Slot2`` is one instrument resource name and ``PXI1Slot3`` is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map.

        +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | |Note| | Note   You only can specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and PXIe-6571. The instruments must be in the same chassis. |
        +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. |Note| image:: note.gif

        

        .. note:: 


    :type resource_name: str

    :param id_query:
        

        A Boolean that verifies that the digital pattern instrument you initialize is supported by NI-Digital. NI-Digital automatically performs this query, so setting this parameter is not necessary.

        


    :type id_query: bool

    :param reset_device:
        

        A Boolean that specifies whether to reset a digital pattern instrument to a known state when the session is initialized. Setting the **resetDevice** value to True is equivalent to calling the :py:meth:`nidigital.Session.reset` method immediately after initializing the session.

        


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

            Stops bursting the pattern.

            



abort_keep_alive
----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: abort_keep_alive()

            Stops the keep alive pattern if it is currently running. If a pattern burst is in progress, the method aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle.

            



apply_levels_and_timing
-----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: apply_levels_and_timing(levels_sheet, timing_sheet, initial_state_high_pins=None, initial_state_low_pins=None, initial_state_tristate_pins=None)

            Applies digital levels and timing values defined in previously loaded levels and timing sheets. When applying a levels sheet, only the levels specified in the sheet are affected. Any levels not specified in the sheet remain unchanged. When applying a timing sheet, all existing time sets are deleted before the new time sets are loaded.

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].apply_levels_and_timing`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.apply_levels_and_timing`


            :param levels_sheet:


                Name of the levels sheet to apply. Use the name of the sheet or pass the absolute file path you use in the :py:meth:`nidigital.Session.load_specifications_levels_and_timing` method. The name of the levels sheet is the file name without the directory and file extension.

                


            :type levels_sheet: str
            :param timing_sheet:


                Name of the timing sheet to apply. Use the name of the sheet or pass the absolute file path that you use in the :py:meth:`nidigital.Session.load_specifications_levels_and_timing` method. The name of the timing sheet is the file name without the directory and file extension.

                


            :type timing_sheet: str
            :param initial_state_high_pins:


                Comma-delimited list of pins, pin groups, or channels to initialize to a high state.

                


            :type initial_state_high_pins: basic sequence types or str
            :param initial_state_low_pins:


                Comma-delimited list of pins, pin groups, or channels to initialize to a low state.

                


            :type initial_state_low_pins: basic sequence types or str
            :param initial_state_tristate_pins:


                Comma-delimited list of pins, pin groups, or channels to initialize to a non-drive state (X)

                


            :type initial_state_tristate_pins: basic sequence types or str

apply_tdr_offsets
-----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: apply_tdr_offsets(offsets)

            Applies the correction for propagation delay offsets to a digital pattern instrument. Use this method to apply TDR offsets that are stored from a past measurement or are measured by means other than the :py:meth:`nidigital.Session.tdr` method. Also use this method to apply correction for offsets if the **applyOffsets** input of the :py:meth:`nidigital.Session.tdr` method was set to False at the time of measurement.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].apply_tdr_offsets`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.apply_tdr_offsets`


            :param offsets:


                TDR offsets to apply, in seconds. Specify an offset for each pin or channel in the repeated capabilities. If the repeated capabilities contain pin names, you must specify offsets for each site in the channel map per pin.

                


            :type offsets: basic sequence of hightime.timedelta, datetime.timedelta, or float in seconds

burst_pattern
-------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: burst_pattern(start_label, select_digital_function=True, wait_until_done=True, timeout=hightime.timedelta(seconds=10.0))

            Uses the start_label you specify to burst the pattern on the sites you specify. If you
            specify wait_until_done as True, waits for the burst to complete, and returns comparison results for each site.

            Digital pins retain their state at the end of a pattern burst until the first vector of the pattern burst, a call to
            :py:meth:`nidigital.Session.write_static`, or a call to :py:meth:`nidigital.Session.apply_levels_and_timing`.

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].burst_pattern`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.burst_pattern`


            :param start_label:


                Pattern name or exported pattern label from which to start bursting the pattern.

                


            :type start_label: str
            :param select_digital_function:


                A Boolean that specifies whether to select the digital method for the pins in the pattern prior to bursting.

                


            :type select_digital_function: bool
            :param wait_until_done:


                A Boolean that indicates whether to wait until the bursting is complete.

                


            :type wait_until_done: bool
            :param timeout:


                Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: { int: bool, int: bool, ... }
            :return:


                    Dictionary where each key is a site number and value is pass/fail,
                    if wait_until_done is specified as True. Else, None.

                    



clock_generator_abort
---------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: clock_generator_abort()

            Stops clock generation on the specified channel(s) or pin(s) and pin group(s).

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].clock_generator_abort`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.clock_generator_abort`


clock_generator_generate_clock
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: clock_generator_generate_clock(frequency, select_digital_function=True)

            Configures clock generator frequency and initiates clock generation on the specified channel(s) or pin(s) and pin group(s).

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].clock_generator_generate_clock`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.clock_generator_generate_clock`


            :param frequency:


                The frequency of the clock generation, in Hz.

                


            :type frequency: float
            :param select_digital_function:


                A Boolean that specifies whether to select the digital method for the pins specified prior to starting clock generation.

                


            :type select_digital_function: bool

close
-----

    .. py:currentmodule:: nidigital.Session

    .. py:method:: close()

            Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state.

            

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: commit()

            Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the :py:meth:`nidigital.Session.commit` method, then the initiate method or the :py:meth:`nidigital.Session.burst_pattern` method will implicitly call this method for you. Calling this method moves the session from the Uncommitted state to the Committed state.

            



configure_active_load_levels
----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_active_load_levels(iol, ioh, vcom)

            Configures I\ :sub:`OL`, I\ :sub:`OH`, and V\ :sub:`COM` levels for the active load on the pins you specify. The DUT sources or sinks current based on the level values. To enable active load, set the termination mode to :py:data:`~nidigital.TerminationMode.ACTIVE_LOAD`. To disable active load, set the termination mode of the instrument to :py:data:`~nidigital.TerminationMode.HIGH_Z` or :py:data:`~nidigital.TerminationMode.VTERM`.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_active_load_levels`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_active_load_levels`


            :param iol:


                Maximum current that the DUT sinks while outputting a voltage below V\ :sub:`COM`.

                


            :type iol: float
            :param ioh:


                Maximum current that the DUT sources while outputting a voltage above V\ :sub:`COM`.

                


            :type ioh: float
            :param vcom:


                Commutating voltage level at which the active load circuit switches between sourcing current and sinking current.

                


            :type vcom: float

configure_pattern_burst_sites
-----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_pattern_burst_sites()

            Configures which sites burst the pattern on the next call to the initiate method. The pattern burst sites can also be modified through the repeated capabilities for the :py:meth:`nidigital.Session.burst_pattern` method. If a site has been disabled through the :py:meth:`nidigital.Session.disable_sites` method, the site does not burst a pattern even if included in the pattern burst sites.

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].configure_pattern_burst_sites`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_pattern_burst_sites`


configure_time_set_compare_edges_strobe
---------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_compare_edges_strobe(time_set_name, strobe_edge)

            Configures the strobe edge time for the specified pins. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_compare_edges_strobe`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_compare_edges_strobe`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param strobe_edge:


                Time when the comparison happens within a vector period.

                


            :type strobe_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_compare_edges_strobe2x
-----------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_compare_edges_strobe2x(time_set_name, strobe_edge, strobe2_edge)

            Configures the compare strobes for the specified pins in the time set, including the 2x strobe. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_compare_edges_strobe2x`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_compare_edges_strobe2x`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param strobe_edge:


                Time when the comparison happens within a vector period.

                


            :type strobe_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param strobe2_edge:


                Time when the comparison happens for the second DUT cycle within a vector period.

                


            :type strobe2_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_drive_edges
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_edges(time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)

            Configures the drive format and drive edge placement for the specified pins. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_edges`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_drive_edges`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param format:


                Drive format of the time set.

                -   :py:data:`~nidigital.DriveFormat.NR`: Non-return.
                -   :py:data:`~nidigital.DriveFormat.RL`: Return to low.
                -   :py:data:`~nidigital.DriveFormat.RH`: Return to high.
                -   :py:data:`~nidigital.DriveFormat.SBC`: Surround by complement.

                


            :type format: :py:data:`nidigital.DriveFormat`
            :param drive_on_edge:


                Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.

                


            :type drive_on_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_data_edge:


                Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.

                


            :type drive_data_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_return_edge:


                Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

                


            :type drive_return_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_off_edge:


                Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).

                


            :type drive_off_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_drive_edges2x
--------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_edges2x(time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)

            Configures the drive edges of the pins in the time set, including 2x edges. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_edges2x`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_drive_edges2x`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param format:


                Drive format of the time set.

                -   :py:data:`~nidigital.DriveFormat.NR`: Non-return.
                -   :py:data:`~nidigital.DriveFormat.RL`: Return to low.
                -   :py:data:`~nidigital.DriveFormat.RH`: Return to high.
                -   :py:data:`~nidigital.DriveFormat.SBC`: Surround by complement.

                


            :type format: :py:data:`nidigital.DriveFormat`
            :param drive_on_edge:


                Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.

                


            :type drive_on_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_data_edge:


                Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.

                


            :type drive_data_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_return_edge:


                Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

                


            :type drive_return_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_off_edge:


                Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).

                


            :type drive_off_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_data2_edge:


                Delay, in seconds, from the beginning of the vector period until the pattern data in the second DUT cycle is driven to the pattern value.

                


            :type drive_data2_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_return2_edge:


                Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data in the second DUT cycle to the return value, as specified in the format.

                


            :type drive_return2_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_drive_format
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_format(time_set_name, drive_format)

            Configures the drive format for the pins specified in the **pinList**. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_format`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_drive_format`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param drive_format:


                Drive format of the time set.

                -   :py:data:`~nidigital.DriveFormat.NR`: Non-return.
                -   :py:data:`~nidigital.DriveFormat.RL`: Return to low.
                -   :py:data:`~nidigital.DriveFormat.RH`: Return to high.
                -   :py:data:`~nidigital.DriveFormat.SBC`: Surround by complement.

                


            :type drive_format: :py:data:`nidigital.DriveFormat`

configure_time_set_edge
-----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_edge(time_set_name, edge, time)

            Configures the edge placement for the pins specified in the pin list. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_edge`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_edge`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param edge:


                Name of the edge.

                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_ON`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_DATA`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_RETURN`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_OFF`
                -   :py:data:`~nidigital.TimeSetEdgeType.COMPARE_STROBE`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_DATA2`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_RETURN2`
                -   :py:data:`~nidigital.TimeSetEdgeType.COMPARE_STROBE2`

                


            :type edge: :py:data:`nidigital.TimeSetEdgeType`
            :param time:


                The time from the beginning of the vector period in which to place the edge.

                


            :type time: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_edge_multiplier
----------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_edge_multiplier(time_set_name, edge_multiplier)

            Configures the edge multiplier of the pins in the time set. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_edge_multiplier`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_edge_multiplier`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param edge_multiplier:


                The specified edge multiplier for the pins in the pin list.

                


            :type edge_multiplier: int

configure_time_set_period
-------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_period(time_set_name, period)

            Configures the period of a time set. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            



            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param period:


                Period for this time set, in seconds.

                


            :type period: hightime.timedelta, datetime.timedelta, or float in seconds

configure_voltage_levels
------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_voltage_levels(vil, vih, vol, voh, vterm)

            Configures voltage levels for the pins you specify.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_voltage_levels`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_voltage_levels`


            :param vil:


                Voltage that the instrument will apply to the input of the DUT when the pin driver drives a logic low (0).

                


            :type vil: float
            :param vih:


                Voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic high (1).

                


            :type vih: float
            :param vol:


                Output voltage below which the comparator on the pin driver interprets a logic low (L).

                


            :type vol: float
            :param voh:


                Output voltage above which the comparator on the pin driver interprets a logic high (H).

                


            :type voh: float
            :param vterm:


                Termination voltage the instrument applies during non-drive cycles when the termination mode is set to V\ :sub:`term`. The instrument applies the termination voltage through a 50 ohm parallel termination resistance.

                


            :type vterm: float

create_capture_waveform_from_file_digicapture
---------------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_capture_waveform_from_file_digicapture(waveform_name, waveform_file_path)

            Creates a capture waveform with the configuration information from a Digicapture file generated by the Digital Pattern Editor.

            



            :param waveform_name:


                Waveform name you want to use. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the capture_start opcode in your pattern.

                


            :type waveform_name: str
            :param waveform_file_path:


                Absolute file path to the capture waveform file (.digicapture) you want to load.

                


            :type waveform_file_path: str

create_capture_waveform_parallel
--------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_capture_waveform_parallel(waveform_name)

            Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].create_capture_waveform_parallel`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.create_capture_waveform_parallel`


            :param waveform_name:


                Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.

                


            :type waveform_name: str

create_capture_waveform_serial
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_capture_waveform_serial(waveform_name, sample_width, bit_order)

            Sets the capture waveform settings for serial acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].create_capture_waveform_serial`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.create_capture_waveform_serial`


            :param waveform_name:


                Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.

                


            :type waveform_name: str
            :param sample_width:


                Width in bits of each serial sample. Valid values are between 1 and 32.

                


            :type sample_width: int
            :param bit_order:


                Order in which to shift the bits.

                -   :py:data:`~nidigital.BitOrder.MSB`: Specifies the bit order by most significant bit first.
                -   :py:data:`~nidigital.BitOrder.LSB`: Specifies the bit order by least significant bit first.

                


            :type bit_order: :py:data:`nidigital.BitOrder`

create_source_waveform_from_file_tdms
-------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_source_waveform_from_file_tdms(waveform_name, waveform_file_path, write_waveform_data=True)

            Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file.

            



            :param waveform_name:


                The waveform name you want to use from the file. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the source_start opcode in your pattern.

                


            :type waveform_name: str
            :param waveform_file_path:


                Absolute file path to the load source waveform file (.tdms).

                


            :type waveform_file_path: str
            :param write_waveform_data:


                A Boolean that writes waveform data to source memory if True and the waveform data is in the file.

                


            :type write_waveform_data: bool

create_source_waveform_parallel
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_source_waveform_parallel(waveform_name, data_mapping)

            Sets the source waveform settings required for parallel sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].create_source_waveform_parallel`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.create_source_waveform_parallel`


            :param waveform_name:


                The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

                


            :type waveform_name: str
            :param data_mapping:


                Parameter that specifies how to map data on multiple sites.

                -   :py:data:`~nidigital.SourceDataMapping.BROADCAST`: Broadcasts the waveform you specify to all sites.
                -   :py:data:`~nidigital.SourceDataMapping.SITE_UNIQUE`: Sources unique waveform data to each site.

                


            :type data_mapping: :py:data:`nidigital.SourceDataMapping`

create_source_waveform_serial
-----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_source_waveform_serial(waveform_name, data_mapping, sample_width, bit_order)

            Sets the source waveform settings required for serial sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].create_source_waveform_serial`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.create_source_waveform_serial`


            :param waveform_name:


                The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

                


            :type waveform_name: str
            :param data_mapping:


                Parameter that specifies how to map data on multiple sites.

                -   :py:data:`~nidigital.SourceDataMapping.BROADCAST`: Broadcasts the waveform you specify to all sites.
                -   :py:data:`~nidigital.SourceDataMapping.SITE_UNIQUE`: Sources unique waveform data to each site.

                


            :type data_mapping: :py:data:`nidigital.SourceDataMapping`
            :param sample_width:


                Width in bits of each serial sample. Valid values are between 1 and 32.

                


            :type sample_width: int
            :param bit_order:


                Order in which to shift the bits.

                -   :py:data:`~nidigital.BitOrder.MSB`: Specifies the bit order by most significant bit first.
                -   :py:data:`~nidigital.BitOrder.LSB`: Specifies the bit order by least significant bit first.

                


            :type bit_order: :py:data:`nidigital.BitOrder`

create_time_set
---------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_time_set(name)

            Creates a time set with the name that you specify. Use this method when you want to create time sets programmatically rather than with a timing sheet.

            



            :param name:


                The specified name of the new time set.

                


            :type name: str

delete_all_time_sets
--------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: delete_all_time_sets()

            Deletes all time sets from instrument memory.

            



disable_sites
-------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: disable_sites()

            Disables specified sites. Disabled sites are not included in pattern bursts initiated by the initiate method or the :py:meth:`nidigital.Session.burst_pattern` method, even if the site is specified in the list of pattern burst sites in :py:meth:`nidigital.Session.configure_pattern_burst_sites` method or in the repeated capabilities for the :py:meth:`nidigital.Session.burst_pattern` method. Additionally, if you specify a list of pin or pin group names in repeated capabilities in any NI-Digital method, digital pattern instrument channels mapped to disabled sites are not affected by the method. The methods that return per-pin data, such as the :py:meth:`nidigital.Session.ppmu_measure` method, do not return data for channels mapped to disabled sites. The digital pattern instrument channels mapped to the sites specified are left in their current state. NI TestStand Semiconductor Module requires all sites to always be enabled, and manages the set of active sites without disabling the sites in the digital instrument session. Do not use this method with the Semiconductor Module.

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].disable_sites`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.disable_sites`


enable_sites
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: enable_sites()

            Enables the sites you specify. All sites are enabled by default.

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].enable_sites`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.enable_sites`


fetch_capture_waveform
----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: fetch_capture_waveform(waveform_name, samples_to_read, timeout=hightime.timedelta(seconds=10.0))

            Returns dictionary where each key is a site number and value is a collection of digital states representing capture waveform data

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].fetch_capture_waveform`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.fetch_capture_waveform`


            :param waveform_name:


                Waveform name you create with the create capture waveform method. Use the waveform_name parameter with capture_start opcode in your pattern.

                


            :type waveform_name: str
            :param samples_to_read:


                Number of samples to fetch.

                


            :type samples_to_read: int
            :param timeout:


                Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

                


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


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].fetch_history_ram_cycle_information`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.fetch_history_ram_cycle_information`


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

            Measures the frequency on the specified channel(s) over the specified measurement time. All channels in the repeated capabilities should have the same measurement time.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].frequency_counter_measure_frequency`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.frequency_counter_measure_frequency`


            :rtype: list of float
            :return:


                    The returned frequency counter measurement, in Hz.This method returns -1 if the measurement is invalid for the channel.

                    



get_channel_names
-----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_channel_names(indices)

            Returns a comma-separated list of channel names from a string index list.

            



            :param indices:


                Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.

                


            :type indices: basic sequence types or str or int

            :rtype: list of str
            :return:


                    The returned channel name(s) at the specified index.

                    



get_fail_count
--------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_fail_count()

            Returns the comparison fail count for pins in the repeated capabilities.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_fail_count`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_fail_count`


            :rtype: list of int
            :return:


                    Number of failures in an array. If a site is disabled or not enabled for burst, the method does not return data for that site. You can also use the :py:meth:`nidigital.Session.get_pin_results_pin_information` method to obtain a sorted list of returned sites and channels.

                    



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


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].get_history_ram_sample_count`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_history_ram_sample_count`


            :rtype: int
            :return:


                    The returned number of samples that History RAM acquired.

                    



get_pattern_pin_names
---------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_pattern_pin_names(start_label)

            Returns the pattern pin list.

            



            :param start_label:


                Pattern name or exported pattern label from which to get the pin names that the pattern references.

                


            :type start_label: str

            :rtype: list of str
            :return:


                    List of pins referenced by the pattern with the **startLabel**.

                    



get_pin_results_pin_information
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_pin_results_pin_information()

            Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The method returns pin information in the same order as values read using the :py:meth:`nidigital.Session.read_static` method, :py:meth:`nidigital.Session.ppmu_measure` method, and :py:meth:`nidigital.Session.get_fail_count` method. Use this method to match values the previously listed methods return with pins, sites, and instrument channels.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_pin_results_pin_information`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_pin_results_pin_information`


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

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].get_site_pass_fail`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_site_pass_fail`


            :rtype: { int: bool, int: bool, ... }
            :return:


                    Dictionary where each key is a site number and value is pass/fail

                    



get_time_set_drive_format
-------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_drive_format(time_set_name)

            Returns the drive format of a pin in the specified time set.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].get_time_set_drive_format`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_time_set_drive_format`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str

            :rtype: :py:data:`nidigital.DriveFormat`
            :return:


                    Returned drive format of the time set for the specified pin.

                    



get_time_set_edge
-----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_edge(time_set_name, edge)

            Returns the edge time of a pin in the specified time set.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].get_time_set_edge`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_time_set_edge`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param edge:


                Name of the edge.

                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_ON`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_DATA`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_RETURN`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_OFF`
                -   :py:data:`~nidigital.TimeSetEdgeType.COMPARE_STROBE`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_DATA2`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_RETURN2`
                -   :py:data:`~nidigital.TimeSetEdgeType.COMPARE_STROBE2`

                


            :type edge: :py:data:`nidigital.TimeSetEdgeType`

            :rtype: hightime.timedelta
            :return:


                    Time from the beginning of the vector period in which to place the edge.

                    



get_time_set_edge_multiplier
----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_edge_multiplier(time_set_name)

            Returns the edge multiplier of the specified time set.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].get_time_set_edge_multiplier`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_time_set_edge_multiplier`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str

            :rtype: int
            :return:


                    Returned edge multiplier of the time set for the specified pin.

                    



get_time_set_period
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_period(time_set_name)

            Returns the period of the specified time set.

            



            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str

            :rtype: hightime.timedelta
            :return:


                    Returned period, in seconds, that the edge is configured to.

                    



initiate
--------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: initiate()

            Starts bursting the pattern configured by :py:attr:`nidigital.Session.start_label`, causing the NI-Digital session to be committed. To stop the pattern burst, call :py:meth:`nidigital.Session.abort`. If keep alive pattern is bursting when :py:meth:`nidigital.Session.abort` is called or upon exiting the context manager, keep alive pattern will not be stopped. To stop the keep alive pattern, call :py:meth:`nidigital.Session.abort_keep_alive`.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



is_done
-------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: is_done()

            Checks the hardware to determine if the pattern burst has completed or if any errors have occurred.

            



            :rtype: bool
            :return:


                    A Boolean that indicates whether the pattern burst completed.

                    



is_site_enabled
---------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: is_site_enabled()

            Checks if a specified site is enabled.

            

            .. note:: The method returns an error if more than one site is specified.


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].is_site_enabled`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.is_site_enabled`


            :rtype: bool
            :return:


                    Boolean value that returns whether the site is enabled or disabled.

                    



load_pattern
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: load_pattern(file_path)

            Loads the specified pattern file.

            



            :param file_path:


                Absolute file path of the binary .digipat pattern file to load. Specify the pattern to burst using :py:attr:`nidigital.Session.start_label` or the start_label parameter of the :py:meth:`nidigital.Session.burst_pattern` method.

                


            :type file_path: str

load_pin_map
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: load_pin_map(file_path)

            Loads a pin map file. You can load only a single pin and channel map file during an NI-Digital Pattern Driver session. To switch pin maps, create a new session or call the :py:meth:`nidigital.Session.reset` method.

            



            :param file_path:


                Absolute file path to a pin map file created with the Digital Pattern Editor or the NI TestStand Semiconductor Module.

                


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

            Instructs the PPMU to measure voltage or current. This method can be called to take a voltage measurement even if the pin method is not set to PPMU.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].ppmu_measure`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.ppmu_measure`


            :param measurement_type:


                Parameter that specifies whether the PPMU measures voltage or current from the DUT.

                -   :py:data:`~nidigital.PPMUMeasurementType.CURRENT`: The PPMU measures current from the DUT.
                -   :py:data:`~nidigital.PPMUMeasurementType.VOLTAGE`: The PPMU measures voltage from the DUT.

                


            :type measurement_type: :py:data:`nidigital.PPMUMeasurementType`

            :rtype: list of float
            :return:


                    The returned array of measurements in the order you specify in the repeated capabilities. If a site is disabled, the method does not return data for that site. You can also use the :py:meth:`nidigital.Session.get_pin_results_pin_information` method to obtain a sorted list of returned sites and channels.

                    



ppmu_source
-----------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: ppmu_source()

            Starts sourcing voltage or current from the PPMU. This method automatically selects the PPMU method. Changes to PPMU source settings do not take effect until you call this method. If you modify source settings after you call this method, you must call this method again for changes in the configuration to take effect.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].ppmu_source`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.ppmu_source`


read_sequencer_flag
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_sequencer_flag(flag)

            Reads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

            



            :param flag:


                The pattern sequencer flag you want to read.

                -   :py:data:`~nidigital.SequencerFlag.FLAG0` ("seqflag0"): Reads pattern sequencer flag 0.
                -   :py:data:`~nidigital.SequencerFlag.FLAG1` ("seqflag1"): Reads pattern sequencer flag 1.
                -   :py:data:`~nidigital.SequencerFlag.FLAG2` ("seqflag2"): Reads pattern sequencer flag 2.
                -   :py:data:`~nidigital.SequencerFlag.FLAG3` ("seqflag3"): Reads pattern sequencer flag 3.

                


            :type flag: :py:data:`nidigital.SequencerFlag`

            :rtype: bool
            :return:


                    A Boolean that indicates the state of the pattern sequencer flag you specify.

                    



read_sequencer_register
-----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_sequencer_register(reg)

            Reads the value of a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. For example, you can use this method to read a register modified by the write_reg opcode during a pattern burst.

            



            :param reg:


                The sequencer register to read from.

                -   :py:data:`~nidigital.SequencerRegister.REGISTER0` ("reg0"): Reads sequencer register 0.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER1` ("reg1"): Reads sequencer register 1.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER2` ("reg2"): Reads sequencer register 2.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER3` ("reg3"): Reads sequencer register 3.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER4` ("reg4"): Reads sequencer register 4.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER5` ("reg5"): Reads sequencer register 5.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER6` ("reg6"): Reads sequencer register 6.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER7` ("reg7"): Reads sequencer register 7.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER8` ("reg8"): Reads sequencer register 8.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER9` ("reg9"): Reads sequencer register 9.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER10` ("reg10"): Reads sequencer register 10.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER11` ("reg11"): Reads sequencer register 11.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER12` ("reg12"): Reads sequencer register 12.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER13` ("reg13"): Reads sequencer register 13.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER14` ("reg14"): Reads sequencer register 14.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER15` ("reg15"): Reads sequencer register 15.

                


            :type reg: :py:data:`nidigital.SequencerRegister`

            :rtype: int
            :return:


                    Value read from the sequencer register.

                    



read_static
-----------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_static()

            Reads the current state of comparators for pins you specify in the repeated capabilities. If there are uncommitted changes to levels or the termination mode, this method commits the changes to the pins.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].read_static`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.read_static`


            :rtype: list of :py:data:`nidigital.PinState`
            :return:


                    The returned array of pin states read from the channels in the repeated capabilities. Data is returned in the order you specify in the repeated capabilities. If a site is disabled, the method does not return data for that site. You can also use the :py:meth:`nidigital.Session.get_pin_results_pin_information` method to obtain a sorted list of returned sites and channels.

                    -   :py:data:`~nidigital.PinState.L`: The comparators read a logic low pin state.
                    -   :py:data:`~nidigital.PinState.H`: The comparators read a logic high pin state.
                    -   :py:data:`~nidigital.PinState.M`: The comparators read a midband pin state.
                    -   :py:data:`~nidigital.PinState.V`: The comparators read a value that is above VOH and below VOL, which can occur when you set VOL higher than VOH.

                    



reset
-----

    .. py:currentmodule:: nidigital.Session

    .. py:method:: reset()

            Returns a digital pattern instrument to a known state. This method performs the following actions:

            - Aborts pattern execution.
            - Clears pin maps, time sets, source and capture waveforms, and patterns.
            - Resets all properties to default values, including the :py:attr:`nidigital.Session.selected_function` property that is set to :py:data:`~nidigital.SelectedFunction.DISCONNECT`, causing the I/O switches to open.
            - Stops exporting all external signals and events.

            



reset_device
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: reset_device()

            Returns a digital pattern instrument to a known state. This method performs the following actions:

            - Aborts pattern execution.
            - Clears pin maps, time sets, source and capture waveforms, and patterns.
            - Resets all properties to default values, including the :py:attr:`nidigital.Session.selected_function` property that is set to :py:data:`~nidigital.SelectedFunction.DISCONNECT`, causing the I/O switches to open.
            - Stops export of all external signals and events.
            - Clears over-temperature and over-power conditions.

            



self_calibrate
--------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: self_calibrate()

            Performs self-calibration on a digital pattern instrument.

            



self_test
---------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: self_test()

            Returns self test results from a digital pattern instrument. This test requires several minutes to execute.

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

    .. py:currentmodule:: nidigital.Session

    .. py:method:: send_software_edge_trigger(trigger, trigger_identifier)

            Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this method as a software override.

            



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

            Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR). Ensure that the channels and pins you select are connected to an open circuit.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].tdr`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.tdr`


            :param apply_offsets:


                A Boolean that specifies whether to apply the measured TDR offsets. If you need to adjust the measured offsets prior to applying, set this input to False, and call the :py:meth:`nidigital.Session.apply_tdr_offsets` method to specify the adjusted TDR offsets values.

                


            :type apply_offsets: bool

            :rtype: list of hightime.timedelta
            :return:


                    Measured TDR offsets specified in seconds.

                    



unload_all_patterns
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: unload_all_patterns(unload_keep_alive_pattern=False)

            Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument.

            



            :param unload_keep_alive_pattern:


                A Boolean that specifies whether to keep or unload the keep alive pattern.

                


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

            Waits until the pattern burst has completed or the timeout has expired.

            



            :param timeout:


                Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

write_sequencer_flag
--------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_sequencer_flag(flag, value)

            Writes the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

            



            :param flag:


                The pattern sequencer flag to write.

                -   :py:data:`~nidigital.SequencerFlag.FLAG0` ("seqflag0"): Writes pattern sequencer flag 0.
                -   :py:data:`~nidigital.SequencerFlag.FLAG1` ("seqflag1"): Writes pattern sequencer flag 1.
                -   :py:data:`~nidigital.SequencerFlag.FLAG2` ("seqflag2"): Writes pattern sequencer flag 2.
                -   :py:data:`~nidigital.SequencerFlag.FLAG3` ("seqflag3"): Writes pattern sequencer flag 3.

                


            :type flag: :py:data:`nidigital.SequencerFlag`
            :param value:


                A Boolean that assigns a state to the pattern sequencer flag you specify.

                


            :type value: bool

write_sequencer_register
------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_sequencer_register(reg, value)

            Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program.

            



            :param reg:


                The sequencer register you want to write to.

                -   :py:data:`~nidigital.SequencerRegister.REGISTER0` ("reg0"): Writes sequencer register 0.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER1` ("reg1"): Writes sequencer register 1.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER2` ("reg2"): Writes sequencer register 2.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER3` ("reg3"): Writes sequencer register 3.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER4` ("reg4"): Writes sequencer register 4.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER5` ("reg5"): Writes sequencer register 5.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER6` ("reg6"): Writes sequencer register 6.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER7` ("reg7"): Writes sequencer register 7.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER8` ("reg8"): Writes sequencer register 8.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER9` ("reg9"): Writes sequencer register 9.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER10` ("reg10"): Writes sequencer register 10.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER11` ("reg11"): Writes sequencer register 11.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER12` ("reg12"): Writes sequencer register 12.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER13` ("reg13"): Writes sequencer register 13.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER14` ("reg14"): Writes sequencer register 14.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER15` ("reg15"): Writes sequencer register 15.

                


            :type reg: :py:data:`nidigital.SequencerRegister`
            :param value:


                The value you want to write to the register.

                


            :type value: int

write_source_waveform_broadcast
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_source_waveform_broadcast(waveform_name, waveform_data)

            Writes the same waveform data to all sites. Use this write method if you set the data_mapping parameter of the create source waveform method to :py:data:`~nidigital.SourceDataMapping.BROADCAST`.

            



            :param waveform_name:


                The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

                


            :type waveform_name: str
            :param waveform_data:


                1D array of samples to use as source data to apply to all sites.

                


            :type waveform_data: list of int

write_source_waveform_data_from_file_tdms
-----------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_source_waveform_data_from_file_tdms(waveform_name, waveform_file_path)

            Writes a source waveform based on the waveform data and configuration information the file contains.

            



            :param waveform_name:


                The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

                


            :type waveform_name: str
            :param waveform_file_path:


                Absolute file path to the load source waveform file (.tdms).

                


            :type waveform_file_path: str

write_source_waveform_site_unique
---------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_source_waveform_site_unique(waveform_name, waveform_data)

            Writes one waveform per site. Use this write method if you set the parameter of the create source waveform method to Site Unique.

            



            :param waveform_name:


                The name to assign to the waveform. Use the waveform_name with source_start opcode in your pattern.

                


            :type waveform_name: str
            :param waveform_data:


                Dictionary where each key is a site number and value is a collection of samples to use as source data

                


            :type waveform_data: { int: basic sequence of unsigned int, int: basic sequence of unsigned int, ... }

write_static
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_static(state)

            Writes a static state to the specified pins. The selected pins remain in the specified state until the next pattern burst or call to this method. If there are uncommitted changes to levels or the termination mode, this method commits the changes to the pins. This method does not change the selected pin method. If you write a static state to a pin that does not have the Digital method selected, the new static state is stored by the instrument, and affects the state of the pin the next time you change the selected method to Digital.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].write_static`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.write_static`


            :param state:


                Parameter that specifies one of the following digital states to assign to the pin.

                -   :py:data:`~nidigital.WriteStaticPinState.ZERO`: Specifies to drive low.
                -   :py:data:`~nidigital.WriteStaticPinState.ONE`: Specifies to drive high.
                -   :py:data:`~nidigital.WriteStaticPinState.X`: Specifies to not drive.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type state: :py:data:`nidigital.WriteStaticPinState`


Properties
==========

active_load_ioh
---------------

    .. py:attribute:: active_load_ioh

        Specifies the current that the DUT sources to the active load while outputting a voltage above VCOM.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].active_load_ioh`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.active_load_ioh`

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

                - C Attribute: **NIDIGITAL_ATTR_ACTIVE_LOAD_IOH**

active_load_iol
---------------

    .. py:attribute:: active_load_iol

        Specifies the current that the DUT sinks from the active load while outputting a voltage below VCOM.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].active_load_iol`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.active_load_iol`

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

                - C Attribute: **NIDIGITAL_ATTR_ACTIVE_LOAD_IOL**

active_load_vcom
----------------

    .. py:attribute:: active_load_vcom

        Specifies the voltage level at which the active load circuit switches between sourcing current and sinking current.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].active_load_vcom`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.active_load_vcom`

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

                - C Attribute: **NIDIGITAL_ATTR_ACTIVE_LOAD_VCOM**

cache
-----

    .. py:attribute:: cache

        Specifies whether to cache the value of properties. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. This significantly increases execution speed. Caching is always enabled in the driver, regardless of the value of this property.

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

                - C Attribute: **NIDIGITAL_ATTR_CACHE**

channel_count
-------------

    .. py:attribute:: channel_count

        Returns the number of channels that the specific digital pattern instrument driver supports.

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

                - C Attribute: **NIDIGITAL_ATTR_CHANNEL_COUNT**

clock_generator_frequency
-------------------------

    .. py:attribute:: clock_generator_frequency

        Specifies the frequency for the clock generator.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].clock_generator_frequency`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.clock_generator_frequency`

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

                - C Attribute: **NIDIGITAL_ATTR_CLOCK_GENERATOR_FREQUENCY**

clock_generator_is_running
--------------------------

    .. py:attribute:: clock_generator_is_running

        Indicates whether the clock generator is running.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].clock_generator_is_running`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.clock_generator_is_running`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CLOCK_GENERATOR_IS_RUNNING**

conditional_jump_trigger_terminal_name
--------------------------------------

    .. py:attribute:: conditional_jump_trigger_terminal_name

        Specifies the terminal name from which the exported conditional jump trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the conditional jump trigger instance asserts on the digital pattern instrument.




        .. tip:: This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

            Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].conditional_jump_trigger_terminal_name`

            To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.conditional_jump_trigger_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | str                       |
            +-----------------------+---------------------------+
            | Permissions           | read only                 |
            +-----------------------+---------------------------+
            | Repeated Capabilities | conditional_jump_triggers |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME**

conditional_jump_trigger_type
-----------------------------

    .. py:attribute:: conditional_jump_trigger_type

        Disables the conditional jump trigger or configures it for either hardware triggering or software triggering.  The default value is :py:data:`~nidigital.TriggerType.NONE`.

        +------------------------------------------------+------------------------------------------------------------------+
        | Valid Values:                                  |                                                                  |
        +================================================+==================================================================+
        | :py:data:`~nidigital.TriggerType.NONE`         | Disables the conditional jump trigger.                           |
        +------------------------------------------------+------------------------------------------------------------------+
        | :py:data:`~nidigital.TriggerType.DIGITAL_EDGE` | Configures the conditional jump trigger for hardware triggering. |
        +------------------------------------------------+------------------------------------------------------------------+
        | :py:data:`~nidigital.TriggerType.SOFTWARE`     | Configures the conditional jump trigger for software triggering. |
        +------------------------------------------------+------------------------------------------------------------------+


        .. tip:: This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

            Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].conditional_jump_trigger_type`

            To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.conditional_jump_trigger_type`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | enums.TriggerType         |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | conditional_jump_triggers |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CONDITIONAL_JUMP_TRIGGER_TYPE**

cycle_number_history_ram_trigger_cycle_number
---------------------------------------------

    .. py:attribute:: cycle_number_history_ram_trigger_cycle_number

        Specifies the cycle number on which History RAM starts acquiring pattern information when configured for a cycle number trigger.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER**

digital_edge_conditional_jump_trigger_edge
------------------------------------------

    .. py:attribute:: digital_edge_conditional_jump_trigger_edge

        Configures the active edge of the incoming trigger signal for the conditional jump trigger instance. The default value is :py:data:`~nidigital.DigitalEdge.RISING`.

        +-------------------------------------------+---------------------------------------------------------------+
        | Valid Values:                             |                                                               |
        +===========================================+===============================================================+
        | :py:data:`~nidigital.DigitalEdge.RISING`  | Specifies the signal transition from low level to high level. |
        +-------------------------------------------+---------------------------------------------------------------+
        | :py:data:`~nidigital.DigitalEdge.FALLING` | Specifies the signal transition from high level to low level. |
        +-------------------------------------------+---------------------------------------------------------------+


        .. tip:: This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

            Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].digital_edge_conditional_jump_trigger_edge`

            To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.digital_edge_conditional_jump_trigger_edge`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | enums.DigitalEdge         |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | conditional_jump_triggers |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE**

digital_edge_conditional_jump_trigger_source
--------------------------------------------

    .. py:attribute:: digital_edge_conditional_jump_trigger_source

        Configures the digital trigger source terminal for a conditional jump trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/ConditionalJumpTrigger0. The default value is VI_NULL.

        +----------------------------------------------+
        | Valid Values:                                |
        +==============================================+
        | String identifier to any valid terminal name |
        +----------------------------------------------+


        .. tip:: This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

            Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].digital_edge_conditional_jump_trigger_source`

            To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.digital_edge_conditional_jump_trigger_source`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | str                       |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | conditional_jump_triggers |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE**

digital_edge_start_trigger_edge
-------------------------------

    .. py:attribute:: digital_edge_start_trigger_edge

        Specifies the active edge for the Start trigger. This property is used when the :py:attr:`nidigital.Session.start_trigger_type` property is set to Digital Edge.

        +-------------------------------------------+-------------------------------------------------------------------------------+
        | Defined Values:                           |                                                                               |
        +===========================================+===============================================================================+
        | :py:data:`~nidigital.DigitalEdge.RISING`  | Asserts the trigger when the signal transitions from low level to high level. |
        +-------------------------------------------+-------------------------------------------------------------------------------+
        | :py:data:`~nidigital.DigitalEdge.FALLING` | Asserts the trigger when the signal transitions from high level to low level. |
        +-------------------------------------------+-------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.DigitalEdge |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

digital_edge_start_trigger_source
---------------------------------

    .. py:attribute:: digital_edge_start_trigger_source

        Specifies the source terminal for the Start trigger. This property is used when the :py:attr:`nidigital.Session.start_trigger_type` property is set to Digital Edge. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/StartTrigger.

        +-----------------+--------------------+
        | Defined Values: |                    |
        +=================+====================+
        | PXI_Trig0       | PXI trigger line 0 |
        +-----------------+--------------------+
        | PXI_Trig1       | PXI trigger line 1 |
        +-----------------+--------------------+
        | PXI_Trig2       | PXI trigger line 2 |
        +-----------------+--------------------+
        | PXI_Trig3       | PXI trigger line 3 |
        +-----------------+--------------------+
        | PXI_Trig4       | PXI trigger line 4 |
        +-----------------+--------------------+
        | PXI_Trig5       | PXI trigger line 5 |
        +-----------------+--------------------+
        | PXI_Trig6       | PXI trigger line 6 |
        +-----------------+--------------------+
        | PXI_Trig7       | PXI trigger line 7 |
        +-----------------+--------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE**

driver_setup
------------

    .. py:attribute:: driver_setup

        This property returns initial values for NI-Digital Pattern Driver properties as a string.

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

                - C Attribute: **NIDIGITAL_ATTR_DRIVER_SETUP**

exported_conditional_jump_trigger_output_terminal
-------------------------------------------------

    .. py:attribute:: exported_conditional_jump_trigger_output_terminal

        Specifies the terminal to output the exported signal of the specified instance of the conditional jump trigger. The default value is VI_NULL.

        +---------------+-------------------------+
        | Valid Values: |                         |
        +===============+=========================+
        | VI_NULL ("")  | Returns an empty string |
        +---------------+-------------------------+
        | PXI_Trig0     | PXI trigger line 0      |
        +---------------+-------------------------+
        | PXI_Trig1     | PXI trigger line 1      |
        +---------------+-------------------------+
        | PXI_Trig2     | PXI trigger line 2      |
        +---------------+-------------------------+
        | PXI_Trig3     | PXI trigger line 3      |
        +---------------+-------------------------+
        | PXI_Trig4     | PXI trigger line 4      |
        +---------------+-------------------------+
        | PXI_Trig5     | PXI trigger line 5      |
        +---------------+-------------------------+
        | PXI_Trig6     | PXI trigger line 6      |
        +---------------+-------------------------+
        | PXI_Trig7     | PXI trigger line 7      |
        +---------------+-------------------------+


        .. tip:: This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

            Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].exported_conditional_jump_trigger_output_terminal`

            To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.exported_conditional_jump_trigger_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | str                       |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | conditional_jump_triggers |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL**

exported_pattern_opcode_event_output_terminal
---------------------------------------------

    .. py:attribute:: exported_pattern_opcode_event_output_terminal

        Specifies the destination terminal for exporting the Pattern Opcode Event. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

        +-----------------+--------------------+
        | Defined Values: |                    |
        +=================+====================+
        | PXI_Trig0       | PXI trigger line 0 |
        +-----------------+--------------------+
        | PXI_Trig1       | PXI trigger line 1 |
        +-----------------+--------------------+
        | PXI_Trig2       | PXI trigger line 2 |
        +-----------------+--------------------+
        | PXI_Trig3       | PXI trigger line 3 |
        +-----------------+--------------------+
        | PXI_Trig4       | PXI trigger line 4 |
        +-----------------+--------------------+
        | PXI_Trig5       | PXI trigger line 5 |
        +-----------------+--------------------+
        | PXI_Trig6       | PXI trigger line 6 |
        +-----------------+--------------------+
        | PXI_Trig7       | PXI trigger line 7 |
        +-----------------+--------------------+


        .. tip:: This property can be set/get on specific pattern_opcode_events within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container pattern_opcode_events to specify a subset.

            Example: :py:attr:`my_session.pattern_opcode_events[ ... ].exported_pattern_opcode_event_output_terminal`

            To set/get on all pattern_opcode_events, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.exported_pattern_opcode_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | str                   |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | pattern_opcode_events |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_start_trigger_output_terminal

        Specifies the destination terminal for exporting the Start trigger. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

        +----------------------+-----------------------------+
        | Defined Values:      |                             |
        +======================+=============================+
        | Do not export signal | The signal is not exported. |
        +----------------------+-----------------------------+
        | PXI_Trig0            | PXI trigger line 0          |
        +----------------------+-----------------------------+
        | PXI_Trig1            | PXI trigger line 1          |
        +----------------------+-----------------------------+
        | PXI_Trig2            | PXI trigger line 2          |
        +----------------------+-----------------------------+
        | PXI_Trig3            | PXI trigger line 3          |
        +----------------------+-----------------------------+
        | PXI_Trig4            | PXI trigger line 4          |
        +----------------------+-----------------------------+
        | PXI_Trig5            | PXI trigger line 5          |
        +----------------------+-----------------------------+
        | PXI_Trig6            | PXI trigger line 6          |
        +----------------------+-----------------------------+
        | PXI_Trig7            | PXI trigger line 7          |
        +----------------------+-----------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

frequency_counter_hysteresis_enabled
------------------------------------

    .. py:attribute:: frequency_counter_hysteresis_enabled

        Specifies whether hysteresis is enabled for the frequency counters of the digital pattern instrument.

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

                - C Attribute: **NIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLED**

frequency_counter_measurement_mode
----------------------------------

    .. py:attribute:: frequency_counter_measurement_mode

        Determines how the frequency counters of the digital pattern instrument make measurements.

        +---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Valid Values:                                           |                                                                                                                                                                                                                                                                                                                                                                                                  |
        +=========================================================+==================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nidigital.FrequencyMeasurementMode.BANKED`   | Each discrete frequency counter is mapped to specific channels and makes frequency measurements from only those channels. Use banked mode when you need access to the full measure frequency range of the instrument. **Note:** If you request frequency measurements from multiple channels within the same bank, the measurements are made in series for the channels in that bank.            |
        +---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.FrequencyMeasurementMode.PARALLEL` | All discrete frequency counters make frequency measurements from all channels in parallel with one another. Use parallel mode to increase the speed of frequency measurements if you do not need access to the full measure frequency range of the instrument; in parallel mode, you can also add :py:attr:`nidigital.Session.frequency_counter_hysteresis_enabled` to reduce measurement noise. |
        +---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------------+
            | Characteristic        | Value                          |
            +=======================+================================+
            | Datatype              | enums.FrequencyMeasurementMode |
            +-----------------------+--------------------------------+
            | Permissions           | read-write                     |
            +-----------------------+--------------------------------+
            | Repeated Capabilities | None                           |
            +-----------------------+--------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_MODE**

frequency_counter_measurement_time
----------------------------------

    .. py:attribute:: frequency_counter_measurement_time

        Specifies the measurement time for the frequency counter.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].frequency_counter_measurement_time`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.frequency_counter_measurement_time`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------------+
            | Characteristic        | Value                                  |
            +=======================+========================================+
            | Datatype              | float in seconds or datetime.timedelta |
            +-----------------------+----------------------------------------+
            | Permissions           | read-write                             |
            +-----------------------+----------------------------------------+
            | Repeated Capabilities | channels                               |
            +-----------------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_TIME**

group_capabilities
------------------

    .. py:attribute:: group_capabilities

        Returns a string that contains a comma-separated list of class-extension groups that the driver implements.

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

                - C Attribute: **NIDIGITAL_ATTR_GROUP_CAPABILITIES**

halt_on_keep_alive_opcode
-------------------------

    .. py:attribute:: halt_on_keep_alive_opcode

        Specifies whether keep_alive opcodes should behave like halt opcodes.

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

                - C Attribute: **NIDIGITAL_ATTR_HALT_ON_KEEP_ALIVE_OPCODE**

history_ram_buffer_size_per_site
--------------------------------

    .. py:attribute:: history_ram_buffer_size_per_site

        Specifies the size, in samples, of the host memory buffer. The default value is 32000.

        +---------------+
        | Valid Values: |
        +===============+
        | 0-INT64_MAX   |
        +---------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_BUFFER_SIZE_PER_SITE**

history_ram_cycles_to_acquire
-----------------------------

    .. py:attribute:: history_ram_cycles_to_acquire

        Configures which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.

        +--------------------------------------------------------+-----------------------------------------------------------------------------------+
        | Defined Values:                                        |                                                                                   |
        +========================================================+===================================================================================+
        | :py:data:`~nidigital.HistoryRAMCyclesToAcquire.FAILED` | Only acquires cycles that fail a compare after the triggering conditions are met. |
        +--------------------------------------------------------+-----------------------------------------------------------------------------------+
        | :py:data:`~nidigital.HistoryRAMCyclesToAcquire.ALL`    | Acquires all cycles after the triggering conditions are met.                      |
        +--------------------------------------------------------+-----------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.HistoryRAMCyclesToAcquire |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_CYCLES_TO_ACQUIRE**

history_ram_max_samples_to_acquire_per_site
-------------------------------------------

    .. py:attribute:: history_ram_max_samples_to_acquire_per_site

        Specifies the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE**

history_ram_number_of_samples_is_finite
---------------------------------------

    .. py:attribute:: history_ram_number_of_samples_is_finite

        Specifies whether the instrument acquires a finite number of History Ram samples or acquires continuously. The maximum number of samples that will be acquired when this property is set to True is determined by the instrument History RAM depth specification and the History RAM Max Samples to Acquire Per Site property. The default value is True.

        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Valid Values: |                                                                                                                                                      |
        +===============+======================================================================================================================================================+
        | True          | Specifies that History RAM results will not stream into the host buffer until a History RAM fetch API is called.                                     |
        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
        | False         | Specifies that History RAM results will automatically start streaming into a host buffer after a pattern is burst and the History RAM has triggered. |
        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

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

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE**

history_ram_pretrigger_samples
------------------------------

    .. py:attribute:: history_ram_pretrigger_samples

        Specifies the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_PRETRIGGER_SAMPLES**

history_ram_trigger_type
------------------------

    .. py:attribute:: history_ram_trigger_type

        Specifies the type of trigger condition on which History RAM starts acquiring pattern information.

        +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
        | Defined Values:                                           |                                                                                                                                     |
        +===========================================================+=====================================================================================================================================+
        | :py:data:`~nidigital.HistoryRAMTriggerType.FIRST_FAILURE` | Starts acquiring pattern information in History RAM on the first failed cycle in a pattern burst.                                   |
        +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.HistoryRAMTriggerType.CYCLE_NUMBER`  | Starts acquiring pattern information in History RAM starting from a specified cycle number.                                         |
        +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.HistoryRAMTriggerType.PATTERN_LABEL` | Starts acquiring pattern information in History RAM starting from a specified pattern label, augmented by vector and cycle offsets. |
        +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.HistoryRAMTriggerType |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_TRIGGER_TYPE**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        Returns a string that contains the firmware revision information for the digital pattern instrument.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].instrument_firmware_revision`

            To set/get on all instruments, you can call the property directly on the :py:class:`nidigital.Session`.

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

                - C Attribute: **NIDIGITAL_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        Returns a string ("National Instruments") that contains the name of the manufacturer of the digital pattern instrument.

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

                - C Attribute: **NIDIGITAL_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        Returns a string that contains the model number or name of the digital pattern instrument.

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

                - C Attribute: **NIDIGITAL_ATTR_INSTRUMENT_MODEL**

interchange_check
-----------------

    .. py:attribute:: interchange_check

        This property is not supported.

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

                - C Attribute: **NIDIGITAL_ATTR_INTERCHANGE_CHECK**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Returns a string that contains the resource descriptor that the NI-Digital Pattern Driver uses to identify the digital pattern instrument.

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

                - C Attribute: **NIDIGITAL_ATTR_IO_RESOURCE_DESCRIPTOR**

is_keep_alive_active
--------------------

    .. py:attribute:: is_keep_alive_active

        Returns True if the digital pattern instrument is driving the keep alive pattern.

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

                - C Attribute: **NIDIGITAL_ATTR_IS_KEEP_ALIVE_ACTIVE**

logical_name
------------

    .. py:attribute:: logical_name

        Returns a string containing the logical name that you specified when opening the current IVI session. This property is not supported.

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

                - C Attribute: **NIDIGITAL_ATTR_LOGICAL_NAME**

mask_compare
------------

    .. py:attribute:: mask_compare

        Specifies whether the pattern comparisons are masked or not. When set to True for a specified pin, failures on that pin will be masked.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].mask_compare`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.mask_compare`

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

                - C Attribute: **NIDIGITAL_ATTR_MASK_COMPARE**

pattern_label_history_ram_trigger_cycle_offset
----------------------------------------------

    .. py:attribute:: pattern_label_history_ram_trigger_cycle_offset

        Specifies the number of cycles that follow the specified pattern label and vector offset, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET**

pattern_label_history_ram_trigger_label
---------------------------------------

    .. py:attribute:: pattern_label_history_ram_trigger_label

        Specifies the pattern label, augmented by the vector and cycle offset, to determine the point where History RAM will start acquiring pattern information when configured for a pattern label trigger.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL**

pattern_label_history_ram_trigger_vector_offset
-----------------------------------------------

    .. py:attribute:: pattern_label_history_ram_trigger_vector_offset

        Specifies the number of vectors that follow the specified pattern label, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET**

pattern_opcode_event_terminal_name
----------------------------------

    .. py:attribute:: pattern_opcode_event_terminal_name

        Specifies the terminal name for the output trigger signal of the specified instance of a Pattern Opcode Event. You can use this terminal name as an input signal source for another trigger.




        .. tip:: This property can be set/get on specific pattern_opcode_events within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container pattern_opcode_events to specify a subset.

            Example: :py:attr:`my_session.pattern_opcode_events[ ... ].pattern_opcode_event_terminal_name`

            To set/get on all pattern_opcode_events, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.pattern_opcode_event_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | str                   |
            +-----------------------+-----------------------+
            | Permissions           | read only             |
            +-----------------------+-----------------------+
            | Repeated Capabilities | pattern_opcode_events |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_OPCODE_EVENT_TERMINAL_NAME**

ppmu_allow_extended_voltage_range
---------------------------------

    .. py:attribute:: ppmu_allow_extended_voltage_range

        Enables the instrument to operate in additional voltage ranges where instrument specifications may differ from standard ranges. When set to True, this property enables extended voltage range operation. Review specification deviations for application suitability before using this property. NI recommends setting this property to False when not using the extended voltage range to avoid unintentional use of this range. The extended voltage range is supported only for PPMU, with the output method set to DC Voltage. A voltage glitch may occur when you change the PPMU output voltage from a standard range to the extended voltage range, or vice-versa, while the PPMU is sourcing. NI recommends temporarily changing the :py:attr:`nidigital.Session.selected_function` property to Off before sourcing a voltage level that requires a range change.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_allow_extended_voltage_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_allow_extended_voltage_range`

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

                - C Attribute: **NIDIGITAL_ATTR_PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE**

ppmu_aperture_time
------------------

    .. py:attribute:: ppmu_aperture_time

        Specifies the measurement aperture time for the PPMU. The :py:attr:`nidigital.Session.ppmu_aperture_time_units` property sets the units of the PPMU aperture time.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_aperture_time`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_aperture_time`

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

                - C Attribute: **NIDIGITAL_ATTR_PPMU_APERTURE_TIME**

ppmu_aperture_time_units
------------------------

    .. py:attribute:: ppmu_aperture_time_units

        Specifies the units of the measurement aperture time for the PPMU.

        +-----------------------------------------------------+-----------------------------------------+
        | Defined Values:                                     |                                         |
        +=====================================================+=========================================+
        | :py:data:`~nidigital.PPMUApertureTimeUnits.SECONDS` | Specifies the aperture time in seconds. |
        +-----------------------------------------------------+-----------------------------------------+


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_aperture_time_units`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_aperture_time_units`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.PPMUApertureTimeUnits |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | channels                    |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS**

ppmu_current_level
------------------

    .. py:attribute:: ppmu_current_level

        Specifies the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Current. Specify valid values for the current level using the :py:meth:`nidigital.Session.PPMU_ConfigureCurrentLevelRange` method.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_level`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_level`

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

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL**

ppmu_current_level_range
------------------------

    .. py:attribute:: ppmu_current_level_range

        Specifies the range of valid values for the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Current.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_level_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_level_range`

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

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL_RANGE**

ppmu_current_limit
------------------

    .. py:attribute:: ppmu_current_limit

        Specifies the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Voltage. The PXIe-6570/6571 does not support the :py:attr:`nidigital.Session.ppmu_current_limit` property and only allows configuration of the :py:attr:`nidigital.Session.ppmu_current_limit_range` property.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_limit`

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

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT**

ppmu_current_limit_behavior
---------------------------

    .. py:attribute:: ppmu_current_limit_behavior

        Specifies how the output should behave when the current limit is reached.

        +---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | Defined Values:                                         |                                                                                                                                         |
        +=========================================================+=========================================================================================================================================+
        | :py:data:`~nidigital.PPMUCurrentLimitBehavior.REGULATE` | Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached. |
        +---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_behavior`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_limit_behavior`

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------------+
            | Characteristic        | Value                          |
            +=======================+================================+
            | Datatype              | enums.PPMUCurrentLimitBehavior |
            +-----------------------+--------------------------------+
            | Permissions           | read-write                     |
            +-----------------------+--------------------------------+
            | Repeated Capabilities | channels                       |
            +-----------------------+--------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_BEHAVIOR**

ppmu_current_limit_range
------------------------

    .. py:attribute:: ppmu_current_limit_range

        Specifies the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Voltage.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_range`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_limit_range`

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

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_RANGE**

ppmu_current_limit_supported
----------------------------

    .. py:attribute:: ppmu_current_limit_supported

        Returns whether the device supports configuration of a current limit when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Voltage.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_supported`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_limit_supported`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_SUPPORTED**

ppmu_output_function
--------------------

    .. py:attribute:: ppmu_output_function

        Specifies whether the PPMU forces voltage or current to the DUT.

        +--------------------------------------------------+--------------------------------------------+
        | Defined Values:                                  |                                            |
        +==================================================+============================================+
        | :py:data:`~nidigital.PPMUOutputFunction.VOLTAGE` | Specifies the output method to DC Voltage. |
        +--------------------------------------------------+--------------------------------------------+
        | :py:data:`~nidigital.PPMUOutputFunction.CURRENT` | Specifies the output method to DC Current. |
        +--------------------------------------------------+--------------------------------------------+


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_output_function`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_output_function`

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.PPMUOutputFunction |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | channels                 |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION**

ppmu_voltage_level
------------------

    .. py:attribute:: ppmu_voltage_level

        Specifies the voltage level, in volts, that the PPMU forces to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Voltage.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_level`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_voltage_level`

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

                - C Attribute: **NIDIGITAL_ATTR_PPMU_VOLTAGE_LEVEL**

ppmu_voltage_limit_high
-----------------------

    .. py:attribute:: ppmu_voltage_limit_high

        Specifies the maximum voltage limit, or high clamp voltage (V :sub:`CH` ), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Current.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_limit_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_voltage_limit_high`

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

                - C Attribute: **NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_HIGH**

ppmu_voltage_limit_low
----------------------

    .. py:attribute:: ppmu_voltage_limit_low

        Specifies the minimum voltage limit, or low clamp voltage (V :sub:`CL` ), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Current.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_limit_low`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_voltage_limit_low`

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

                - C Attribute: **NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_LOW**

query_instrument_status
-----------------------

    .. py:attribute:: query_instrument_status

        Specifies whether the NI-Digital Pattern Driver queries the digital pattern instrument status after each operation. The instrument status is always queried, regardless of the property setting.

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

                - C Attribute: **NIDIGITAL_ATTR_QUERY_INSTRUMENT_STATUS**

range_check
-----------

    .. py:attribute:: range_check

        Checks the range and validates parameter and property values you pass to NI-Digital Pattern Driver methods. Ranges are always checked, regardless of the property setting.

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

                - C Attribute: **NIDIGITAL_ATTR_RANGE_CHECK**

record_coercions
----------------

    .. py:attribute:: record_coercions

        Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties. Enabling record value coercions is not supported.

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

                - C Attribute: **NIDIGITAL_ATTR_RECORD_COERCIONS**

selected_function
-----------------

    .. py:attribute:: selected_function

        .. caution:: In the Disconnect state, some I/O protection and sensing circuitry remains exposed. Do not subject the instrument to voltage beyond its operating range.

        Specifies whether digital pattern instrument channels are controlled by the pattern sequencer or PPMU, disconnected, or off.

        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Defined Values:                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
        +===================================================+==================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nidigital.SelectedFunction.DIGITAL`    | The pin is connected to the driver, comparator, and active load methods. The PPMU is not sourcing, but can make voltage measurements. The state of the digital pin driver when you change the :py:attr:`nidigital.Session.selected_function` to Digital is determined by the most recent call to the :py:meth:`nidigital.Session.write_static` method or the last vector of the most recently executed pattern burst, whichever happened last. Use the :py:meth:`nidigital.Session.write_static` method to control the state of the digital pin driver through software. Use the :py:meth:`nidigital.Session.burst_pattern` method to control the state of the digital pin driver through a pattern. Set the **selectDigitalFunction** parameter of the :py:meth:`nidigital.Session.burst_pattern` method to True to automatically switch the :py:attr:`nidigital.Session.selected_function` of the pins in the pattern burst to :py:data:`~nidigital.SelectedFunction.DIGITAL`. |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.SelectedFunction.PPMU`       | The pin is connected to the PPMU. The driver, comparator, and active load are off while this method is selected. Call the :py:meth:`nidigital.Session.ppmu_source` method to source a voltage or current. The :py:meth:`nidigital.Session.ppmu_source` method automatically switches the :py:attr:`nidigital.Session.selected_function` to the PPMU state and starts sourcing from the PPMU. Changing the :py:attr:`nidigital.Session.selected_function` to :py:data:`~nidigital.SelectedFunction.DISCONNECT`, :py:data:`~nidigital.SelectedFunction.OFF`, or :py:data:`~nidigital.SelectedFunction.DIGITAL` causes the PPMU to stop sourcing. If you set the :py:attr:`nidigital.Session.selected_function` property to PPMU, the PPMU is initially not sourcing.                                                                                                                                                                                                               |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.SelectedFunction.OFF`        | The pin is electrically connected, and the PPMU and digital pin driver are off while this method is selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.SelectedFunction.DISCONNECT` | The pin is electrically disconnected from instrument methods. Selecting this method causes the PPMU to stop sourcing prior to disconnecting the pin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: You can make PPMU voltage measurements using the :py:meth:`nidigital.Session.ppmu_measure` method from within any :py:attr:`nidigital.Session.selected_function`.


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].selected_function`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.selected_function`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.SelectedFunction |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | channels               |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SELECTED_FUNCTION**

sequencer_flag_terminal_name
----------------------------

    .. py:attribute:: sequencer_flag_terminal_name

        Specifies the terminal name for the output trigger signal of the Sequencer Flags trigger. You can use this terminal name as an input signal source for another trigger.

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

                - C Attribute: **NIDIGITAL_ATTR_SEQUENCER_FLAG_TERMINAL_NAME**

serial_number
-------------

    .. py:attribute:: serial_number

        Returns the serial number of the device.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].serial_number`

            To set/get on all instruments, you can call the property directly on the :py:class:`nidigital.Session`.

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

                - C Attribute: **NIDIGITAL_ATTR_SERIAL_NUMBER**

simulate
--------

    .. py:attribute:: simulate

        Simulates I/O operations. After you open a session, you cannot change the simulation state. Use the :py:meth:`nidigital.Session.__init__` method to enable simulation.

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

                - C Attribute: **NIDIGITAL_ATTR_SIMULATE**

specific_driver_class_spec_major_version
----------------------------------------

    .. py:attribute:: specific_driver_class_spec_major_version

        Returns the major version number of the class specification with which NI-Digital is compliant. This property is not supported.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION**

specific_driver_class_spec_minor_version
----------------------------------------

    .. py:attribute:: specific_driver_class_spec_minor_version

        Returns the minor version number of the class specification with which NI-Digital is compliant. This property is not supported.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        Returns a string that contains a brief description of the NI-Digital Pattern driver.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_prefix
----------------------

    .. py:attribute:: specific_driver_prefix

        Returns a string that contains the prefix for the NI-Digital Pattern driver.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_PREFIX**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        Returns a string that contains additional version information about the NI-Digital Pattern Driver. For example, the driver can return Driver: NI-Digital 16.0 as the value of this property.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        Returns a string ("National Instruments") that contains the name of the vendor that supplies the NI-Digital Pattern Driver.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_VENDOR**

start_label
-----------

    .. py:attribute:: start_label

        Specifies the pattern name or exported pattern label from which to start bursting the pattern.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_START_LABEL**

start_trigger_terminal_name
---------------------------

    .. py:attribute:: start_trigger_terminal_name

        Specifies the terminal name for the output trigger signal of the Start trigger. You can use this terminal name as an input signal source for another trigger.

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

                - C Attribute: **NIDIGITAL_ATTR_START_TRIGGER_TERMINAL_NAME**

start_trigger_type
------------------

    .. py:attribute:: start_trigger_type

        Specifies the Start trigger type. The digital pattern instrument waits for this trigger after you call the :py:meth:`nidigital.Session.init` method or the :py:meth:`nidigital.Session.burst_pattern` method, and does not burst a pattern until this trigger is received.

        +------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Defined Values:                                |                                                                                                                                                                                                                                                                                                                                     |
        +================================================+=====================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nidigital.TriggerType.NONE`         | Disables the Start trigger. Pattern bursting starts immediately after you call the :py:meth:`nidigital.Session.init` method or the :py:meth:`nidigital.Session.burst_pattern` method.                                                                                                                                               |
        +------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.TriggerType.DIGITAL_EDGE` | Pattern bursting does not start until the digital pattern instrument detects a digital edge.                                                                                                                                                                                                                                        |
        +------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.TriggerType.SOFTWARE`     | Pattern bursting does not start until the digital pattern instrument receives a software Start trigger. Create a software Start trigger by calling the :py:meth:`nidigital.Session.send_software_edge_trigger` method and selecting start trigger in the **trigger** parameter.Related information: SendSoftwareEdgeTrigger method. |
        +------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.TriggerType |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_START_TRIGGER_TYPE**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        Returns a comma delimited string that contains the supported digital pattern instrument models for the specific driver.

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

                - C Attribute: **NIDIGITAL_ATTR_SUPPORTED_INSTRUMENT_MODELS**

tdr_endpoint_termination
------------------------

    .. py:attribute:: tdr_endpoint_termination

        Specifies whether TDR Channels are connected to an open circuit or a short to ground.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------+
            | Characteristic        | Value                        |
            +=======================+==============================+
            | Datatype              | enums.TDREndpointTermination |
            +-----------------------+------------------------------+
            | Permissions           | read-write                   |
            +-----------------------+------------------------------+
            | Repeated Capabilities | None                         |
            +-----------------------+------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TDR_ENDPOINT_TERMINATION**

tdr_offset
----------

    .. py:attribute:: tdr_offset

        Specifies the TDR Offset.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].tdr_offset`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.tdr_offset`

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

                - C Attribute: **NIDIGITAL_ATTR_TDR_OFFSET**

termination_mode
----------------

    .. py:attribute:: termination_mode

        Specifies the behavior of the pin during non-drive cycles.

        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Defined Values:                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
        +===================================================+======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nidigital.TerminationMode.ACTIVE_LOAD` | Specifies that, for non-drive pin states (L, H, X, V, M, E), the active load is connected and the instrument sources or sinks a defined amount of current to load the DUT. The amount of current sourced by the instrument and therefore sunk by the DUT is specified by IOL. The amount of current sunk by the instrument and therefore sourced by the DUT is specified by IOH. The voltage at which the instrument changes between sourcing and sinking is specified by VCOM.                                                                                                                                                                                                                                                                                                                                                                                      |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.TerminationMode.VTERM`       | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver terminates the pin to the configured VTERM voltage through a 50 Ω impedance. VTERM is adjustable to allow for the pin to terminate at a set level. This is useful for instruments that might operate incorrectly if an instrument pin is unterminated and is allowed to float to any voltage level within the instrument voltage range. To address this issue, enable VTERM by configuring the VTERM pin level to the desired voltage and selecting the VTERM termination mode. Setting VTERM to 0 V and selecting the VTERM termination mode has the effect of connecting a 50 Ω termination to ground, which provides an effective 50 Ω impedance for the pin. This can be useful for improving signal integrity of certain DUTs by reducing reflections while the DUT drives the pin. |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.TerminationMode.HIGH_Z`      | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver is put in a high-impedance state and the active load is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].termination_mode`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.termination_mode`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.TerminationMode |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | channels              |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TERMINATION_MODE**

timing_absolute_delay
---------------------

    .. py:attribute:: timing_absolute_delay

        Specifies a timing delay, measured in seconds, and applies the delay to the digital pattern instrument in addition to TDR and calibration adjustments. If the :py:attr:`nidigital.Session.timing_absolute_delay_enabled` property is set to True, this value is the intermodule skew measured by NI-TClk. You can modify this value to override the timing delay and align the I/O timing of this instrument with another instrument that shares the same reference clock. If the :py:attr:`nidigital.Session.timing_absolute_delay_enabled` property is False, this property will return 0.0. Changing the :py:attr:`nidigital.Session.timing_absolute_delay_enabled` property from False to True will set the :py:attr:`nidigital.Session.timing_absolute_delay` value back to your previously set value.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY**

timing_absolute_delay_enabled
-----------------------------

    .. py:attribute:: timing_absolute_delay_enabled

        Specifies whether the :py:attr:`nidigital.Session.timing_absolute_delay` property should be applied to adjust the digital pattern instrument timing reference relative to other instruments in the system. Do not use this feature with digital pattern instruments in a Semiconductor Test System (STS). Timing absolute delay conflicts with the adjustment performed during STS timing calibration. When set to True, the digital pattern instrument automatically adjusts the timing absolute delay to correct the instrument timing reference relative to other instruments in the system for better timing alignment among synchronized instruments.

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

                - C Attribute: **NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED**

vih
---

    .. py:attribute:: vih

        Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic high (1).




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].vih`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.vih`

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

                - C Attribute: **NIDIGITAL_ATTR_VIH**

vil
---

    .. py:attribute:: vil

        Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic low (0).




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].vil`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.vil`

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

                - C Attribute: **NIDIGITAL_ATTR_VIL**

voh
---

    .. py:attribute:: voh

        Specifies the output voltage from the DUT above which the comparator on the digital pattern test instrument interprets a logic high (H).




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voh`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.voh`

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

                - C Attribute: **NIDIGITAL_ATTR_VOH**

vol
---

    .. py:attribute:: vol

        Specifies the output voltage from the DUT below which the comparator on the digital pattern test instrument interprets a logic low (L).




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].vol`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.vol`

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

                - C Attribute: **NIDIGITAL_ATTR_VOL**

vterm
-----

    .. py:attribute:: vterm

        Specifies the termination voltage the digital pattern instrument applies during non-drive cycles when the termination mode is set to V :sub:`term`. The instrument applies the termination voltage through a 50 Ω parallel termination resistance.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].vterm`

            To set/get on all channels, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.vterm`

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

                - C Attribute: **NIDIGITAL_ATTR_VTERM**


NI-TClk Support
===============

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:attr:`nitclk.SessionReference` for a complete list of attributes.


.. contents:: Session


