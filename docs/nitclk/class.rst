nitclk.Session
==============

.. py:module:: nitclk

.. py:class:: Session(self)

    

    TBD

    




    **Properties**

    +------------------------------------------------+----------+
    | Property                                       | Datatype |
    +================================================+==========+
    | :py:attr:`exported_sync_pulse_output_terminal` | str      |
    +------------------------------------------------+----------+
    | :py:attr:`exported_tclk_output_terminal`       | str      |
    +------------------------------------------------+----------+
    | :py:attr:`pause_trigger_master_session`        | int      |
    +------------------------------------------------+----------+
    | :py:attr:`ref_trigger_master_session`          | int      |
    +------------------------------------------------+----------+
    | :py:attr:`sample_clock_delay`                  | float    |
    +------------------------------------------------+----------+
    | :py:attr:`script_trigger_master_session`       | int      |
    +------------------------------------------------+----------+
    | :py:attr:`sequencer_flag_master_session`       | int      |
    +------------------------------------------------+----------+
    | :py:attr:`start_trigger_master_session`        | int      |
    +------------------------------------------------+----------+
    | :py:attr:`sync_pulse_clock_source`             | str      |
    +------------------------------------------------+----------+
    | :py:attr:`sync_pulse_sender_sync_pulse_source` | str      |
    +------------------------------------------------+----------+
    | :py:attr:`sync_pulse_source`                   | str      |
    +------------------------------------------------+----------+
    | :py:attr:`tclk_actual_period`                  | float    |
    +------------------------------------------------+----------+

    **Public methods**

    +----------------------------------------------------+
    | Method name                                        |
    +====================================================+
    | :py:func:`configure_for_homogeneous_triggers`      |
    +----------------------------------------------------+
    | :py:func:`finish_sync_pulse_sender_synchronize`    |
    +----------------------------------------------------+
    | :py:func:`get_attribute_vi_real64`                 |
    +----------------------------------------------------+
    | :py:func:`get_attribute_vi_session`                |
    +----------------------------------------------------+
    | :py:func:`get_attribute_vi_string`                 |
    +----------------------------------------------------+
    | :py:func:`get_extended_error_info`                 |
    +----------------------------------------------------+
    | :py:func:`init_for_documentation`                  |
    +----------------------------------------------------+
    | :py:func:`initiate`                                |
    +----------------------------------------------------+
    | :py:func:`is_done`                                 |
    +----------------------------------------------------+
    | :py:func:`set_attribute_vi_real64`                 |
    +----------------------------------------------------+
    | :py:func:`set_attribute_vi_session`                |
    +----------------------------------------------------+
    | :py:func:`set_attribute_vi_string`                 |
    +----------------------------------------------------+
    | :py:func:`setup_for_sync_pulse_sender_synchronize` |
    +----------------------------------------------------+
    | :py:func:`synchronize`                             |
    +----------------------------------------------------+
    | :py:func:`syncronize_to_sync_pulse_sender`         |
    +----------------------------------------------------+
    | :py:func:`wait_until_done`                         |
    +----------------------------------------------------+


Properties
----------

exported_sync_pulse_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: exported_sync_pulse_output_terminal

        Specifies the destination of the Sync Pulse. This property is most often  used when synchronizing a multichassis system.
        Values
        Empty string. Empty string is a valid value, indicating that the signal is  not exported.
        PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
        PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
        Examples of Device-Specific Settings
        - NI PXI-5122 supports  'PFI0' and  'PFI1'
        - NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'
        - NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
        Default Value is empty string

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Export Sync Pulse Output Terminal**
                - C Attribute: **NITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL**

exported_tclk_output_terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: exported_tclk_output_terminal

        Specifies the destination of the device's TClk signal.
        Values
        Empty string. Empty string is a valid value, indicating that the signal is  not exported.
        PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
        PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
        Examples of Device-Specific Settings
        - NI PXI-5122 supports  'PFI0' and  'PFI1'
        - NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'
        - NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
        Default Value is empty string

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output Terminal**
                - C Attribute: **NITCLK_ATTR_EXPORTED_TCLK_OUTPUT_TERMINAL**

pause_trigger_master_session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: pause_trigger_master_session

        Specifies the pause trigger master session.
        For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Pause Trigger Master Session**
                - C Attribute: **NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION**

ref_trigger_master_session
~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: ref_trigger_master_session

        Specifies the reference trigger master session.
        For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Reference Trigger Master Session**
                - C Attribute: **NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION**

sample_clock_delay
~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: sample_clock_delay

        Specifies the sample clock delay.
        Specifies the delay, in seconds, to apply to the session sample clock  relative to the other synchronized sessions. During synchronization,  NI-TClk aligns the sample clocks on the synchronized devices. If you want  to delay the sample clocks, set this property before calling  :py:meth:`nitclk.Session.synchronize`.
        not supported for acquisition sessions.
        Values - Between minus one and plus one period of the sample clock.
        One sample clock period is equal to (1/sample clock rate). For example,  for a session with sample rate of 100 MS/s, you can specify sample clock  delays between -10.0 ns and +10.0 ns.
        Default Value is 0



        .. note:: Sample clock delay is supported for generation sessions only; it is

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Sample Clock Delay**
                - C Attribute: **NITCLK_ATTR_SAMPLE_CLOCK_DELAY**

script_trigger_master_session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: script_trigger_master_session

        Specifies the script trigger master session.
        For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Script Trigger Master Session**
                - C Attribute: **NITCLK_ATTR_SCRIPT_TRIGGER_MASTER_SESSION**

sequencer_flag_master_session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: sequencer_flag_master_session

        Specifies the sequencer flag master session.
        For external triggers, the session that originally receives the trigger.
        For None (no trigger configured) or software triggers, the session that
        originally generates the trigger.

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Sequencer Flag Master Session**
                - C Attribute: **NITCLK_ATTR_SEQUENCER_FLAG_MASTER_SESSION**

start_trigger_master_session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: start_trigger_master_session

        Specifies the start trigger master session.
        For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Start Trigger Master Session**
                - C Attribute: **NITCLK_ATTR_START_TRIGGER_MASTER_SESSION**

sync_pulse_clock_source
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: sync_pulse_clock_source

        Specifies the Sync Pulse Clock source. This property is typically used to  synchronize PCI devices when you want to control RTSI 7 yourself. Make  sure that a 10 MHz clock is driven onto RTSI 7.
        Values
        PCI Devices -  'RTSI_7' and  'None'
        PXI Devices -  'PXI_CLK10' and  'None'
        Default Value -  'None' directs :py:meth:`nitclk.Session.synchronize` to create the necessary routes. For  PCI, one of the synchronized devices drives a 10 MHz clock on RTSI 7  unless that line is already being driven.

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Sync Pulse Clock Source**
                - C Attribute: **NITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE**

sync_pulse_sender_sync_pulse_source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: sync_pulse_sender_sync_pulse_source

        Specifies the external sync pulse source for the Sync Pulse Sender.  You can use this source to synchronize  the Sync Pulse Sender with an external non-TClk source.
        Values
        Empty string. Empty string is a valid value, indicating that the signal is  not exported.
        PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
        PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
        Examples of Device-Specific Settings
        - NI PXI-5122 supports  'PFI0' and  'PFI1'
        - NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'
        - NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
        Default Value is empty string

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **External Pulse Source**
                - C Attribute: **NITCLK_ATTR_SYNC_PULSE_SENDER_SYNC_PULSE_SOURCE**

sync_pulse_source
~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: sync_pulse_source

        Specifies the Sync Pulse source. This property is most often used when  synchronizing a multichassis system.
        Values
        Empty string
        PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
        PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
        Examples of Device-Specific Settings
        - NI PXI-5122 supports  'PFI0' and  'PFI1'
        - NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
        - NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
        Default Value - Empty string. This default value directs  :py:meth:`nitclk.Session.synchronize` to set this property when all the synchronized devices  are in one PXI chassis. To synchronize a multichassis system, you must set  this property before calling :py:meth:`nitclk.Session.synchronize`.

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Sync Pulse Source**
                - C Attribute: **NITCLK_ATTR_SYNC_PULSE_SOURCE**

tclk_actual_period
~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:attribute:: tclk_actual_period

        Indicates the computed TClk period that will be used during the acquisition.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Period**
                - C Attribute: **NITCLK_ATTR_TCLK_ACTUAL_PERIOD**


Methods
-------


configure_for_homogeneous_triggers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: configure_for_homogeneous_triggers(sessions)

            Configures the properties commonly required for the TClk synchronization
            of device sessions with homogeneous triggers in a single PXI chassis or
            a single PC. Use :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` to configure
            the properties for the reference clocks, start triggers, reference
            triggers, script triggers, and pause triggers. If
            :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` cannot perform all the steps
            appropriate for the given sessions, it returns an error. If an error is
            returned, use the instrument driver methods and properties for signal
            routing, along with the following NI-TClk properties:
            :py:data:`nitclk.Session.start_trigger_master_session`
            :py:data:`nitclk.Session.ref_trigger_master_session`
            :py:data:`nitclk.Session.script_trigger_master_session`
            :py:data:`nitclk.Session.pause_trigger_master_session`
            :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` affects the following clocks and
            triggers: - Reference clocks - Start triggers - Reference triggers -
            Script triggers - Pause triggers Reference Clocks
            :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` configures the reference clocks
            if they are needed. Specifically, if the internal sample clocks or
            internal sample clock timebases are used, and the reference clock source
            is not configured--or is set to None (no trigger
            configured)--:py:meth:`nitclk.Session.configure_for_homogeneous_triggers` configures the
            following: PXI--The reference clock source on all devices is set to be
            the 10 MHz PXI backplane clock (PXI_CLK10). PCI--One of the devices
            exports its 10 MHz onboard reference clock to RTSI 7. The reference
            clock source on all devices is set to be RTSI 7. Note: If the reference
            clock source is set to a value other than None,
            :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` cannot configure the reference
            clock source. Start Triggers If the start trigger is set to None (no
            trigger configured) for all sessions, the sessions are configured to
            share the start trigger. The start trigger is shared by: - Implicitly
            exporting the start trigger from one session - Configuring the other
            sessions for digital edge start triggers with sources corresponding to
            the exported start trigger - Setting
            :py:data:`nitclk.Session.start_trigger_master_session` to the session that is
            exporting the trigger for all sessions If the start triggers are None
            for all except one session, :py:meth:`nitclk.Session.configure_for_homogeneous_triggers`
            configures the sessions to share the start trigger from the one excepted
            session. The start trigger is shared by: - Implicitly exporting start
            trigger from the session with the start trigger that is not None -
            Configuring the other sessions for digital-edge start triggers with
            sources corresponding to the exported start trigger - Setting
            :py:data:`nitclk.Session.start_trigger_master_session` to the session that is
            exporting the trigger for all sessions If start triggers are configured
            for all sessions, :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` does not
            affect the start triggers. Start triggers are considered to be
            configured for all sessions if either of the following conditions is
            true: - No session has a start trigger that is None - One session has a
            start trigger that is None, and all other sessions have start triggers
            other than None. The one session with the None trigger must have
            :py:data:`nitclk.Session.start_trigger_master_session` set to itself, indicating
            that the session itself is the start trigger master Reference Triggers
            :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` configures sessions that support
            reference triggers to share the reference triggers if the reference
            triggers are None (no trigger configured) for all except one session.
            The reference triggers are shared by: - Implicitly exporting the
            reference trigger from the session whose reference trigger is not None -
            Configuring the other sessions that support the reference trigger for
            digital-edge reference triggers with sources corresponding to the
            exported reference trigger - Setting
            :py:data:`nitclk.Session.ref_trigger_master_session` to the session that is
            exporting the trigger for all sessions that support reference trigger If
            the reference triggers are configured for all sessions that support
            reference triggers, :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` does not
            affect the reference triggers. Reference triggers are considered to be
            configured for all sessions if either one or the other of the following
            conditions is true: - No session has a reference trigger that is None -
            One session has a reference trigger that is None, and all other sessions
            have reference triggers other than None. The one session with the None
            trigger must have :py:data:`nitclk.Session.ref_trigger_master_session` set to
            itself, indicating that the session itself is the reference trigger
            master Reference Trigger Holdoffs Acquisition sessions may be configured
            with the reference trigger. For acquisition sessions, when the reference
            trigger is shared, :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` configures
            the holdoff properties (which are instrument driver specific) on the
            reference trigger master session so that the session does not recognize
            the reference trigger before the other sessions are ready. This
            condition is only relevant when the sample clock rates, sample clock
            timebase rates, sample counts, holdoffs, and/or any delays for the
            acquisitions are different. When the sample clock rates, sample clock
            timebase rates, and/or the sample counts are different in acquisition
            sessions sharing the reference trigger, you should also set the holdoff
            properties for the reference trigger master using the instrument driver.
            Script Triggers :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` configures
            sessions that support script triggers to share them, if the script
            triggers are None (no trigger configured) for all except one session.
            The script triggers are shared in the following ways: - Implicitly
            exporting the script trigger from the session whose script trigger is
            not None - Configuring the other sessions that support the script
            trigger for digital-edge script triggers with sources corresponding to
            the exported script trigger - Setting
            :py:data:`nitclk.Session.script_trigger_master_session` to the session that is
            exporting the trigger for all sessions that support script triggers If
            the script triggers are configured for all sessions that support script
            triggers, :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` does not affect script
            triggers. Script triggers are considered to be configured for all
            sessions if either one or the other of the following conditions are
            true: - No session has a script trigger that is None - One session has a
            script trigger that is None and all other sessions have script triggers
            other than None. The one session with the None trigger must have
            :py:data:`nitclk.Session.script_trigger_master_session` set to itself, indicating
            that the session itself is the script trigger master Pause Triggers
            :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` configures generation sessions
            that support pause triggers to share them, if the pause triggers are
            None (no trigger configured) for all except one session. The pause
            triggers are shared by: - Implicitly exporting the pause trigger from
            the session whose script trigger is not None - Configuring the other
            sessions that support the pause trigger for digital-edge pause triggers
            with sources corresponding to the exported pause trigger - Setting
            :py:data:`nitclk.Session.pause_trigger_master_session` to the session that is
            exporting the trigger for all sessions that support script triggers If
            the pause triggers are configured for all generation sessions that
            support pause triggers, :py:meth:`nitclk.Session.configure_for_homogeneous_triggers` does not
            affect pause triggers. Pause triggers are considered to be configured
            for all sessions if either one or the other of the following conditions
            is true: - No session has a pause trigger that is None - One session has
            a pause trigger that is None and all other sessions have pause triggers
            other than None. The one session with the None trigger must have
            :py:data:`nitclk.Session.pause_trigger_master_session` set to itself, indicating
            that the session itself is the pause trigger master Note: TClk
            synchronization is not supported for pause triggers on acquisition
            sessions.

            



            :param sessions:


                sessions is an array of sessions that are being synchronized.

                


            :type sessions: list of vi_session

finish_sync_pulse_sender_synchronize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: finish_sync_pulse_sender_synchronize(sessions, min_time)

            TBD

            



            :param sessions:


                sessions is an array of sessions that are being synchronized.

                


            :type sessions: list of vi_session
            :param min_time:


                Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

                


            :type min_time: float

get_attribute_vi_real64
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: get_attribute_vi_real64(attribute_id)

            Gets the value of an NI-TClk ViReal64 property.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nitclk.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nitclk.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].get_attribute_vi_real64(attribute_id)


            :param attribute_id:


                The ID of the property that you want to get Supported Property
                :py:data:`nitclk.Session.sample_clock_delay`

                


            :type attribute_id: int

            :rtype: float
            :return:


                    The value that you are getting

                    



get_attribute_vi_session
~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: get_attribute_vi_session(attribute_id)

            Gets the value of an NI-TClk ViSession property.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nitclk.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nitclk.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].get_attribute_vi_session(attribute_id)


            :param attribute_id:


                The ID of the property that you want to set Supported Properties
                :py:data:`nitclk.Session.start_trigger_master_session`
                :py:data:`nitclk.Session.ref_trigger_master_session`
                :py:data:`nitclk.Session.script_trigger_master_session`
                :py:data:`nitclk.Session.pause_trigger_master_session`

                


            :type attribute_id: int

            :rtype: int
            :return:


                    The value that you are getting

                    



get_attribute_vi_string
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: get_attribute_vi_string(attribute_id, buf_size, value)

            This method queries the value of an NI-TClk ViString property. You
            must provide a ViChar array to serve as a buffer for the value. You pass
            the number of bytes in the buffer as bufSize. If the current value of
            the property, including the terminating NULL byte, is larger than the
            size you indicate in bufSize, the method copies bufSize minus 1 bytes
            into the buffer, places an ASCII NULL byte at the end of the buffer, and
            returns the array size that you must pass to get the entire value. For
            example, if the value is "123456" and bufSize is 4, the method places
            "123" into the buffer and returns 7. If you want to call
            :py:meth:`nitclk.Session.get_attribute_vi_string` just to get the required array size, pass 0
            for bufSize and VI_NULL for the value.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nitclk.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nitclk.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].get_attribute_vi_string(attribute_id, buf_size, value)


            :param attribute_id:


                The ID of the property that you want to get Supported Properties
                :py:data:`nitclk.Session.sync_pulse_source`
                :py:data:`nitclk.Session.sync_pulse_clock_source`
                :py:data:`nitclk.Session.exported_sync_pulse_output_terminal`

                


            :type attribute_id: int
            :param buf_size:


                The number of bytes in the ViChar array that you specify for the value
                parameter

                


            :type buf_size: int
            :param value:


                The value that you are getting

                


            :type value: vi_char

get_extended_error_info
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: get_extended_error_info()

            Reports extended error information for the most recent NI-TClk method
            that returned an error. To establish the method that returned an
            error, use the return values of the individual methods because once
            :py:meth:`nitclk.Session.get_extended_error_info` reports an errorString, it does not report
            an empty string again.

            



init_for_documentation
~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: init_for_documentation()

            TBD

            



initiate
~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: initiate(sessions)

            Initiates the acquisition or generation sessions specified, taking into
            consideration any special requirements needed for synchronization. For
            example, the session exporting the TClk-synchronized start trigger is
            not initiated until after :py:meth:`nitclk.Session.initiate` initiates all the sessions
            that import the TClk-synchronized start trigger.

            



            :param sessions:


                sessions is an array of sessions that are being synchronized.

                


            :type sessions: list of vi_session

is_done
~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: is_done(sessions)

            Monitors the progress of the acquisitions and/or generations
            corresponding to sessions.

            



            :param sessions:


                sessions is an array of sessions that are being synchronized.

                


            :type sessions: list of vi_session

            :rtype: bool
            :return:


                    Indicates that the operation is done. The operation is done when each
                    session has completed without any errors or when any one of the sessions
                    reports an error.

                    



set_attribute_vi_real64
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: set_attribute_vi_real64(attribute_id, value)

            Sets the value of an NI-TClk VIReal64 property.
            :py:meth:`nitclk.Session.set_attribute_vi_real64` is a low-level method that you can use to
            set the values NI-TClk properties. NI-TClk contains high-level methods
            that set most of the properties. It is best to use the high-level
            methods as much as possible.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nitclk.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nitclk.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].set_attribute_vi_real64(attribute_id, value)


            :param attribute_id:


                The ID of the property that you want to set Supported Property
                :py:data:`nitclk.Session.sample_clock_delay`

                


            :type attribute_id: int
            :param value:


                The value for the property

                


            :type value: float

set_attribute_vi_session
~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: set_attribute_vi_session(attribute_id)

            Sets the value of an NI-TClk ViSession property.
            :py:meth:`nitclk.Session.set_attribute_vi_session` is a low-level method that you can use
            to set the values NI-TClk properties. NI-TClk contains high-level
            methods that set most of the properties. It is best to use the
            high-level methods as much as possible.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nitclk.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nitclk.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].set_attribute_vi_session(attribute_id)


            :param attribute_id:


                The ID of the property that you want to set Supported Properties
                :py:data:`nitclk.Session.start_trigger_master_session`
                :py:data:`nitclk.Session.ref_trigger_master_session`
                :py:data:`nitclk.Session.script_trigger_master_session`
                :py:data:`nitclk.Session.pause_trigger_master_session`

                


            :type attribute_id: int

set_attribute_vi_string
~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: set_attribute_vi_string(attribute_id, value)

            Sets the value of an NI-TClk VIString property.
            :py:meth:`nitclk.Session.set_attribute_vi_string` is a low-level method that you can use to
            set the values of NI-TClk properties. NI-TClk contain high-level
            methods that set most of the properties. It is best to use the
            high-level methods as much as possible.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nitclk.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nitclk.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].set_attribute_vi_string(attribute_id, value)


            :param attribute_id:


                Pass the ID of the property that you want to set Supported Properties
                :py:data:`nitclk.Session.sync_pulse_source`
                :py:data:`nitclk.Session.sync_pulse_clock_source`
                :py:data:`nitclk.Session.exported_sync_pulse_output_terminal`

                


            :type attribute_id: int
            :param value:


                Pass the value for the property

                


            :type value: str

setup_for_sync_pulse_sender_synchronize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: setup_for_sync_pulse_sender_synchronize(sessions, min_time)

            TBD

            



            :param sessions:


                sessions is an array of sessions that are being synchronized.

                


            :type sessions: list of vi_session
            :param min_time:


                Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

                


            :type min_time: float

synchronize
~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: synchronize(sessions, min_time)

            Synchronizes the TClk signals on the given sessions. After
            :py:meth:`nitclk.Session.synchronize` executes, TClk signals from all sessions are
            synchronized. Note: Before using this NI-TClk method, verify that your
            system is configured as specified in the PXI Trigger Lines and RTSI
            Lines topic of the NI-TClk Synchronization Help. You can locate this
            help file at Start>>Programs>>National Instruments>>NI-TClk.

            



            :param sessions:


                sessions is an array of sessions that are being synchronized.

                


            :type sessions: list of vi_session
            :param min_time:


                Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

                


            :type min_time: float

syncronize_to_sync_pulse_sender
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: syncronize_to_sync_pulse_sender(sessions, min_time)

            TBD

            



            :param sessions:


                sessions is an array of sessions that are being synchronized.

                


            :type sessions: list of vi_session
            :param min_time:


                Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

                


            :type min_time: float

wait_until_done
~~~~~~~~~~~~~~~

    .. py:currentmodule:: nitclk.Session

    .. py:method:: wait_until_done(sessions, timeout)

            Call this method to pause execution of your program until the
            acquisitions and/or generations corresponding to sessions are done or
            until the method returns a timeout error. :py:meth:`nitclk.Session.wait_until_done` is a
            blocking method that periodically checks the operation status. It
            returns control to the calling program if the operation completes
            successfully or an error occurs (including a timeout error). This
            method is most useful for finite data operations that you expect to
            complete within a certain time.

            



            :param sessions:


                sessions is an array of sessions that are being synchronized.

                


            :type sessions: list of vi_session
            :param timeout:


                The amount of time in seconds that :py:meth:`nitclk.Session.wait_until_done` waits for the
                sessions to complete. If timeout is exceeded, :py:meth:`nitclk.Session.wait_until_done`
                returns an error.

                


            :type timeout: float



Properties
----------

+---------------------------------------------------------------+----------+
| Property                                                      | Datatype |
+===============================================================+==========+
| :py:attr:`nitclk.Session.exported_sync_pulse_output_terminal` | str      |
+---------------------------------------------------------------+----------+
| :py:attr:`nitclk.Session.exported_tclk_output_terminal`       | str      |
+---------------------------------------------------------------+----------+
| :py:attr:`nitclk.Session.pause_trigger_master_session`        | int      |
+---------------------------------------------------------------+----------+
| :py:attr:`nitclk.Session.ref_trigger_master_session`          | int      |
+---------------------------------------------------------------+----------+
| :py:attr:`nitclk.Session.sample_clock_delay`                  | float    |
+---------------------------------------------------------------+----------+
| :py:attr:`nitclk.Session.script_trigger_master_session`       | int      |
+---------------------------------------------------------------+----------+
| :py:attr:`nitclk.Session.sequencer_flag_master_session`       | int      |
+---------------------------------------------------------------+----------+
| :py:attr:`nitclk.Session.start_trigger_master_session`        | int      |
+---------------------------------------------------------------+----------+
| :py:attr:`nitclk.Session.sync_pulse_clock_source`             | str      |
+---------------------------------------------------------------+----------+
| :py:attr:`nitclk.Session.sync_pulse_sender_sync_pulse_source` | str      |
+---------------------------------------------------------------+----------+
| :py:attr:`nitclk.Session.sync_pulse_source`                   | str      |
+---------------------------------------------------------------+----------+
| :py:attr:`nitclk.Session.tclk_actual_period`                  | float    |
+---------------------------------------------------------------+----------+

Methods
-------

+-------------------------------------------------------------------+
| Method name                                                       |
+===================================================================+
| :py:func:`nitclk.Session.configure_for_homogeneous_triggers`      |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.finish_sync_pulse_sender_synchronize`    |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.get_attribute_vi_real64`                 |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.get_attribute_vi_session`                |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.get_attribute_vi_string`                 |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.get_extended_error_info`                 |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.init_for_documentation`                  |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.initiate`                                |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.is_done`                                 |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.set_attribute_vi_real64`                 |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.set_attribute_vi_session`                |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.set_attribute_vi_string`                 |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.setup_for_sync_pulse_sender_synchronize` |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.synchronize`                             |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.syncronize_to_sync_pulse_sender`         |
+-------------------------------------------------------------------+
| :py:func:`nitclk.Session.wait_until_done`                         |
+-------------------------------------------------------------------+

