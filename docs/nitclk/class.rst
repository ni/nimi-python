
.. py:module:: nitclk

Public API
==========

The `nitclk` module provides synchronization facilites to allow multiple instruments to simultaneously
respond to triggers, to align Sample Clocks on multiple instruments, and/or to simultaneously start multiple
instruments.

It consists of a set of functions that act on a list of :py:class:`SessionReference` objects or nimi-python `Session`
objects for drivers that support NI-TClk. :py:class:`SessionReference` also has a set of properties for configuration.

.. code:: python

    with niscope.Session('dev1') as scope1, niscope.Session('dev2') as scope2:
        nitclk.configure_for_homogeneous_triggers([scope1, scope2])
        nitclk.initiate([scope1, scope2])
        wfm1 = scope1.fetch()
        wfm2 = scope2.fetch()

configure_for_homogeneous_triggers
----------------------------------

    .. py:currentmodule:: nitclk

    .. py:function:: configure_for_homogeneous_triggers(sessions)

        Configures the properties commonly required for the TClk synchronization
        of device sessions with homogeneous triggers in a single PXI chassis or
        a single PC. Use :py:func:`nitclk.configure_for_homogeneous_triggers` to configure
        the properties for the reference clocks, start triggers, reference
        triggers, script triggers, and pause triggers. If
        :py:func:`nitclk.configure_for_homogeneous_triggers` cannot perform all the steps
        appropriate for the given sessions, it returns an error. If an error is
        returned, use the instrument driver methods and properties for signal
        routing, along with the following NI-TClk properties:
        :py:attr:`nitclk.SessionReference.start_trigger_master_session`
        :py:attr:`nitclk.SessionReference.ref_trigger_master_session`
        :py:attr:`nitclk.SessionReference.script_trigger_master_session`
        :py:attr:`nitclk.SessionReference.pause_trigger_master_session`
        :py:func:`nitclk.configure_for_homogeneous_triggers` affects the following clocks and
        triggers: - Reference clocks - Start triggers - Reference triggers -
        Script triggers - Pause triggers Reference Clocks
        :py:func:`nitclk.configure_for_homogeneous_triggers` configures the reference clocks
        if they are needed. Specifically, if the internal sample clocks or
        internal sample clock timebases are used, and the reference clock source
        is not configured--or is set to None (no trigger
        configured)--:py:func:`nitclk.configure_for_homogeneous_triggers` configures the
        following: PXI--The reference clock source on all devices is set to be
        the 10 MHz PXI backplane clock (PXI_CLK10). PCI--One of the devices
        exports its 10 MHz onboard reference clock to RTSI 7. The reference
        clock source on all devices is set to be RTSI 7. Note: If the reference
        clock source is set to a value other than None,
        :py:func:`nitclk.configure_for_homogeneous_triggers` cannot configure the reference
        clock source. Start Triggers If the start trigger is set to None (no
        trigger configured) for all sessions, the sessions are configured to
        share the start trigger. The start trigger is shared by: - Implicitly
        exporting the start trigger from one session - Configuring the other
        sessions for digital edge start triggers with sources corresponding to
        the exported start trigger - Setting
        :py:attr:`nitclk.SessionReference.start_trigger_master_session` to the session that is
        exporting the trigger for all sessions If the start triggers are None
        for all except one session, :py:func:`nitclk.configure_for_homogeneous_triggers`
        configures the sessions to share the start trigger from the one excepted
        session. The start trigger is shared by: - Implicitly exporting start
        trigger from the session with the start trigger that is not None -
        Configuring the other sessions for digital-edge start triggers with
        sources corresponding to the exported start trigger - Setting
        :py:attr:`nitclk.SessionReference.start_trigger_master_session` to the session that is
        exporting the trigger for all sessions If start triggers are configured
        for all sessions, :py:func:`nitclk.configure_for_homogeneous_triggers` does not
        affect the start triggers. Start triggers are considered to be
        configured for all sessions if either of the following conditions is
        true: - No session has a start trigger that is None - One session has a
        start trigger that is None, and all other sessions have start triggers
        other than None. The one session with the None trigger must have
        :py:attr:`nitclk.SessionReference.start_trigger_master_session` set to itself, indicating
        that the session itself is the start trigger master Reference Triggers
        :py:func:`nitclk.configure_for_homogeneous_triggers` configures sessions that support
        reference triggers to share the reference triggers if the reference
        triggers are None (no trigger configured) for all except one session.
        The reference triggers are shared by: - Implicitly exporting the
        reference trigger from the session whose reference trigger is not None -
        Configuring the other sessions that support the reference trigger for
        digital-edge reference triggers with sources corresponding to the
        exported reference trigger - Setting
        :py:attr:`nitclk.SessionReference.ref_trigger_master_session` to the session that is
        exporting the trigger for all sessions that support reference trigger If
        the reference triggers are configured for all sessions that support
        reference triggers, :py:func:`nitclk.configure_for_homogeneous_triggers` does not
        affect the reference triggers. Reference triggers are considered to be
        configured for all sessions if either one or the other of the following
        conditions is true: - No session has a reference trigger that is None -
        One session has a reference trigger that is None, and all other sessions
        have reference triggers other than None. The one session with the None
        trigger must have :py:attr:`nitclk.SessionReference.ref_trigger_master_session` set to
        itself, indicating that the session itself is the reference trigger
        master Reference Trigger Holdoffs Acquisition sessions may be configured
        with the reference trigger. For acquisition sessions, when the reference
        trigger is shared, :py:func:`nitclk.configure_for_homogeneous_triggers` configures
        the holdoff properties (which are instrument driver specific) on the
        reference trigger master session so that the session does not recognize
        the reference trigger before the other sessions are ready. This
        condition is only relevant when the sample clock rates, sample clock
        timebase rates, sample counts, holdoffs, and/or any delays for the
        acquisitions are different. When the sample clock rates, sample clock
        timebase rates, and/or the sample counts are different in acquisition
        sessions sharing the reference trigger, you should also set the holdoff
        properties for the reference trigger master using the instrument driver.
        Script Triggers :py:func:`nitclk.configure_for_homogeneous_triggers` configures
        sessions that support script triggers to share them, if the script
        triggers are None (no trigger configured) for all except one session.
        The script triggers are shared in the following ways: - Implicitly
        exporting the script trigger from the session whose script trigger is
        not None - Configuring the other sessions that support the script
        trigger for digital-edge script triggers with sources corresponding to
        the exported script trigger - Setting
        :py:attr:`nitclk.SessionReference.script_trigger_master_session` to the session that is
        exporting the trigger for all sessions that support script triggers If
        the script triggers are configured for all sessions that support script
        triggers, :py:func:`nitclk.configure_for_homogeneous_triggers` does not affect script
        triggers. Script triggers are considered to be configured for all
        sessions if either one or the other of the following conditions are
        true: - No session has a script trigger that is None - One session has a
        script trigger that is None and all other sessions have script triggers
        other than None. The one session with the None trigger must have
        :py:attr:`nitclk.SessionReference.script_trigger_master_session` set to itself, indicating
        that the session itself is the script trigger master Pause Triggers
        :py:func:`nitclk.configure_for_homogeneous_triggers` configures generation sessions
        that support pause triggers to share them, if the pause triggers are
        None (no trigger configured) for all except one session. The pause
        triggers are shared by: - Implicitly exporting the pause trigger from
        the session whose script trigger is not None - Configuring the other
        sessions that support the pause trigger for digital-edge pause triggers
        with sources corresponding to the exported pause trigger - Setting
        :py:attr:`nitclk.SessionReference.pause_trigger_master_session` to the session that is
        exporting the trigger for all sessions that support script triggers If
        the pause triggers are configured for all generation sessions that
        support pause triggers, :py:func:`nitclk.configure_for_homogeneous_triggers` does not
        affect pause triggers. Pause triggers are considered to be configured
        for all sessions if either one or the other of the following conditions
        is true: - No session has a pause trigger that is None - One session has
        a pause trigger that is None and all other sessions have pause triggers
        other than None. The one session with the None trigger must have
        :py:attr:`nitclk.SessionReference.pause_trigger_master_session` set to itself, indicating
        that the session itself is the pause trigger master Note: TClk
        synchronization is not supported for pause triggers on acquisition
        sessions.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of (Driver Session or nitclk.SessionReference)

finish_sync_pulse_sender_synchronize
------------------------------------

    .. py:currentmodule:: nitclk

    .. py:function:: finish_sync_pulse_sender_synchronize(sessions, min_time=hightime.timedelta(seconds=0.0))

        Finishes synchronizing the Sync Pulse Sender.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of (nimi-python Session class or nitclk.SessionReference)
        :param min_time:


            Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

            


        :type min_time: float in seconds or hightime.timedelta

initiate
--------

    .. py:currentmodule:: nitclk

    .. py:function:: initiate(sessions)

        Initiates the acquisition or generation sessions specified, taking into
        consideration any special requirements needed for synchronization. For
        example, the session exporting the TClk-synchronized start trigger is
        not initiated until after :py:func:`nitclk.initiate` initiates all the sessions
        that import the TClk-synchronized start trigger.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of (Driver Session or nitclk.SessionReference)

is_done
-------

    .. py:currentmodule:: nitclk

    .. py:function:: is_done(sessions)

        Monitors the progress of the acquisitions and/or generations
        corresponding to sessions.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of (Driver Session or nitclk.SessionReference)

        :rtype: bool
        :return:


                Indicates that the operation is done. The operation is done when each
                session has completed without any errors or when any one of the sessions
                reports an error.

                



setup_for_sync_pulse_sender_synchronize
---------------------------------------

    .. py:currentmodule:: nitclk

    .. py:function:: setup_for_sync_pulse_sender_synchronize(sessions, min_time=hightime.timedelta(seconds=0.0))

        Configures the TClks on all the devices and prepares the Sync Pulse Sender for synchronization

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of (Driver Session or nitclk.SessionReference)
        :param min_time:


            Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

            


        :type min_time: float in seconds or hightime.timedelta

synchronize
-----------

    .. py:currentmodule:: nitclk

    .. py:function:: synchronize(sessions, min_tclk_period=hightime.timedelta(seconds=0.0))

        Synchronizes the TClk signals on the given sessions. After
        :py:func:`nitclk.synchronize` executes, TClk signals from all sessions are
        synchronized. Note: Before using this NI-TClk method, verify that your
        system is configured as specified in the PXI Trigger Lines and RTSI
        Lines topic of the NI-TClk Synchronization Help. You can locate this
        help file at Start>>Programs>>National Instruments>>NI-TClk.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of (Driver Session or nitclk.SessionReference)
        :param min_tclk_period:


            Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

            


        :type min_tclk_period: float in seconds or hightime.timedelta

synchronize_to_sync_pulse_sender
--------------------------------

    .. py:currentmodule:: nitclk

    .. py:function:: synchronize_to_sync_pulse_sender(sessions, min_time=hightime.timedelta(seconds=0.0))

        Synchronizes the other devices to the Sync Pulse Sender.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of (Driver Session or nitclk.SessionReference)
        :param min_time:


            Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

            


        :type min_time: float in seconds or hightime.timedelta

wait_until_done
---------------

    .. py:currentmodule:: nitclk

    .. py:function:: wait_until_done(sessions, timeout=hightime.timedelta(seconds=0.0))

        Call this method to pause execution of your program until the
        acquisitions and/or generations corresponding to sessions are done or
        until the method returns a timeout error. :py:func:`nitclk.wait_until_done` is a
        blocking method that periodically checks the operation status. It
        returns control to the calling program if the operation completes
        successfully or an error occurs (including a timeout error). This
        method is most useful for finite data operations that you expect to
        complete within a certain time.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of (Driver Session or nitclk.SessionReference)
        :param timeout:


            The amount of time in seconds that :py:func:`nitclk.wait_until_done` waits for the
            sessions to complete. If timeout is exceeded, :py:func:`nitclk.wait_until_done`
            returns an error.

            


        :type timeout: float in seconds or hightime.timedelta


SessionReference
================
.. py:currentmodule:: nitclk

.. py:class:: SessionReference(session_number)

    Helper class that contains all NI-TClk properties. This class is what is returned by
    any nimi-python Session class tclk attribute when the driver supports NI-TClk

    .. code:: python

        with niscope.Session('dev1') as session:
            session.tclk.sample_clock_delay = .42

    ..note:: Constructing this class is an advanced use case and should not be needed in most circumstances.

    :param session_number:
        nitclk session
    :type session_number: int, nimi-python Session class, SessionReference


exported_sync_pulse_output_terminal
-----------------------------------

    .. py:currentmodule:: nitclk.SessionReference

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
-----------------------------

    .. py:currentmodule:: nitclk.SessionReference

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
----------------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: pause_trigger_master_session

        Specifies the pause trigger master session.
        For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.

        The following table lists the characteristics of this property.

            +----------------+-------------------------------------------+
            | Characteristic | Value                                     |
            +================+===========================================+
            | Datatype       | Driver Session or nitclk.SessionReference |
            +----------------+-------------------------------------------+
            | Permissions    | read-write                                |
            +----------------+-------------------------------------------+
            | Channel Based  | No                                        |
            +----------------+-------------------------------------------+
            | Resettable     | No                                        |
            +----------------+-------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Pause Trigger Master Session**
                - C Attribute: **NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION**

ref_trigger_master_session
--------------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: ref_trigger_master_session

        Specifies the reference trigger master session.
        For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.

        The following table lists the characteristics of this property.

            +----------------+-------------------------------------------+
            | Characteristic | Value                                     |
            +================+===========================================+
            | Datatype       | Driver Session or nitclk.SessionReference |
            +----------------+-------------------------------------------+
            | Permissions    | read-write                                |
            +----------------+-------------------------------------------+
            | Channel Based  | No                                        |
            +----------------+-------------------------------------------+
            | Resettable     | No                                        |
            +----------------+-------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Reference Trigger Master Session**
                - C Attribute: **NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION**

sample_clock_delay
------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: sample_clock_delay

        Specifies the sample clock delay.
        Specifies the delay, in seconds, to apply to the session sample clock  relative to the other synchronized sessions. During synchronization,  NI-TClk aligns the sample clocks on the synchronized devices. If you want  to delay the sample clocks, set this property before calling  :py:func:`nitclk.synchronize`.
        not supported for acquisition sessions.
        Values - Between minus one and plus one period of the sample clock.
        One sample clock period is equal to (1/sample clock rate). For example,  for a session with sample rate of 100 MS/s, you can specify sample clock  delays between -10.0 ns and +10.0 ns.
        Default Value is 0



        .. note:: Sample clock delay is supported for generation sessions only; it is

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or hightime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | No                                     |
            +----------------+----------------------------------------+
            | Resettable     | No                                     |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Sample Clock Delay**
                - C Attribute: **NITCLK_ATTR_SAMPLE_CLOCK_DELAY**

sequencer_flag_master_session
-----------------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: sequencer_flag_master_session

        Specifies the sequencer flag master session.
        For external triggers, the session that originally receives the trigger.
        For None (no trigger configured) or software triggers, the session that
        originally generates the trigger.

        The following table lists the characteristics of this property.

            +----------------+-------------------------------------------+
            | Characteristic | Value                                     |
            +================+===========================================+
            | Datatype       | Driver Session or nitclk.SessionReference |
            +----------------+-------------------------------------------+
            | Permissions    | read-write                                |
            +----------------+-------------------------------------------+
            | Channel Based  | No                                        |
            +----------------+-------------------------------------------+
            | Resettable     | No                                        |
            +----------------+-------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Sequencer Flag Master Session**
                - C Attribute: **NITCLK_ATTR_SEQUENCER_FLAG_MASTER_SESSION**

start_trigger_master_session
----------------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: start_trigger_master_session

        Specifies the start trigger master session.
        For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.

        The following table lists the characteristics of this property.

            +----------------+-------------------------------------------+
            | Characteristic | Value                                     |
            +================+===========================================+
            | Datatype       | Driver Session or nitclk.SessionReference |
            +----------------+-------------------------------------------+
            | Permissions    | read-write                                |
            +----------------+-------------------------------------------+
            | Channel Based  | No                                        |
            +----------------+-------------------------------------------+
            | Resettable     | No                                        |
            +----------------+-------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Start Trigger Master Session**
                - C Attribute: **NITCLK_ATTR_START_TRIGGER_MASTER_SESSION**

sync_pulse_clock_source
-----------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: sync_pulse_clock_source

        Specifies the Sync Pulse Clock source. This property is typically used to  synchronize PCI devices when you want to control RTSI 7 yourself. Make  sure that a 10 MHz clock is driven onto RTSI 7.
        Values
        PCI Devices -  'RTSI_7' and  'None'
        PXI Devices -  'PXI_CLK10' and  'None'
        Default Value -  'None' directs :py:func:`nitclk.synchronize` to create the necessary routes. For  PCI, one of the synchronized devices drives a 10 MHz clock on RTSI 7  unless that line is already being driven.

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
-----------------------------------

    .. py:currentmodule:: nitclk.SessionReference

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
-----------------

    .. py:currentmodule:: nitclk.SessionReference

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
        Default Value - Empty string. This default value directs  :py:func:`nitclk.synchronize` to set this property when all the synchronized devices  are in one PXI chassis. To synchronize a multichassis system, you must set  this property before calling :py:func:`nitclk.synchronize`.

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
------------------

    .. py:currentmodule:: nitclk.SessionReference

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


.. contents:: nitclk


