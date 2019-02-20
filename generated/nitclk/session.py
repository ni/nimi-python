# This file was generated

import ctypes

import nitclk._attributes as _attributes
import nitclk._library_singleton as _library_singleton
import nitclk._visatype as _visatype
import nitclk.errors as errors

# Used for __repr__ and __str__
import pprint
pp = pprint.PrettyPrinter(indent=4)


# Helper functions for creating ctypes needed for calling into the driver DLL
def get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


class Properties(object):
    '''Properties container for NI-TClk attributes.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    exported_sync_pulse_output_terminal = _attributes.AttributeViString(2)
    '''Type: str

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
    '''
    exported_tclk_output_terminal = _attributes.AttributeViString(9)
    '''Type: str

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
    '''
    pause_trigger_master_session = _attributes.AttributeViInt32(6)
    '''Type: int

    Specifies the pause trigger master session.
    For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.
    '''
    ref_trigger_master_session = _attributes.AttributeViInt32(4)
    '''Type: int

    Specifies the reference trigger master session.
    For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.
    '''
    sample_clock_delay = _attributes.AttributeViReal64(11)
    '''Type: float

    Specifies the sample clock delay.
    Specifies the delay, in seconds, to apply to the session sample clock  relative to the other synchronized sessions. During synchronization,  NI-TClk aligns the sample clocks on the synchronized devices. If you want  to delay the sample clocks, set this property before calling  synchronize.
    not supported for acquisition sessions.
    Values - Between minus one and plus one period of the sample clock.
    One sample clock period is equal to (1/sample clock rate). For example,  for a session with sample rate of 100 MS/s, you can specify sample clock  delays between -10.0 ns and +10.0 ns.
    Default Value is 0

    Note: Sample clock delay is supported for generation sessions only; it is
    '''
    script_trigger_master_session = _attributes.AttributeViInt32(5)
    '''Type: int

    Specifies the script trigger master session.
    For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.
    '''
    sequencer_flag_master_session = _attributes.AttributeViInt32(16)
    '''Type: int

    Specifies the sequencer flag master session.
    For external triggers, the session that originally receives the trigger.
    For None (no trigger configured) or software triggers, the session that
    originally generates the trigger.
    '''
    start_trigger_master_session = _attributes.AttributeViInt32(3)
    '''Type: int

    Specifies the start trigger master session.
    For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.
    '''
    sync_pulse_clock_source = _attributes.AttributeViString(10)
    '''Type: str

    Specifies the Sync Pulse Clock source. This property is typically used to  synchronize PCI devices when you want to control RTSI 7 yourself. Make  sure that a 10 MHz clock is driven onto RTSI 7.
    Values
    PCI Devices -  'RTSI_7' and  'None'
    PXI Devices -  'PXI_CLK10' and  'None'
    Default Value -  'None' directs synchronize to create the necessary routes. For  PCI, one of the synchronized devices drives a 10 MHz clock on RTSI 7  unless that line is already being driven.
    '''
    sync_pulse_sender_sync_pulse_source = _attributes.AttributeViString(13)
    '''Type: str

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
    '''
    sync_pulse_source = _attributes.AttributeViString(1)
    '''Type: str

    Specifies the Sync Pulse source. This property is most often used when  synchronizing a multichassis system.
    Values
    Empty string
    PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
    PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
    Examples of Device-Specific Settings
    - NI PXI-5122 supports  'PFI0' and  'PFI1'
    - NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
    - NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
    Default Value - Empty string. This default value directs  synchronize to set this property when all the synchronized devices  are in one PXI chassis. To synchronize a multichassis system, you must set  this property before calling synchronize.
    '''
    tclk_actual_period = _attributes.AttributeViReal64(8)
    '''Type: float

    Indicates the computed TClk period that will be used during the acquisition.
    '''

    def __init__(self, repeated_capability_list, sessions, encoding):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._sessions = sessions
        self._library = _library_singleton.get()
        self._encoding = encoding

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("sessions=" + pp.pformat(sessions))
        param_list.append("library=" + pp.pformat(library))
        param_list.append("encoding=" + pp.pformat(encoding))
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    def __repr__(self):
        return '{0}.{1}({2})'.format('nitclk', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    def _get_error_description(self, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self._get_error()
            return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._error_message(error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."


class Session(object):
    '''An NI-TClk session.'''

    def __init__(self):
        r'''An NI-TClk session.

        TBD
        '''
        if sessions is None or len(sessions) == 0:
            raise ValueError('sessions can not be omitted or an empty list')

        self._sessions = []
        for session in sessions:
            if hasattr(session, 'get_session_reference'):
                s = session.get_session_reference()
            else:
                s = session
            self._sessions.append(s)

        self._library = _library_singleton.get()
        self._encoding = 'windows-1251'

        # Instantiate any repeated capability objects

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("sessions=" + pp.pformat(sessions))
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    ''' These are code-generated '''

    def configure_for_homogeneous_triggers(self, session_count):
        r'''configure_for_homogeneous_triggers

        Configures the properties commonly required for the TClk synchronization
        of device sessions with homogeneous triggers in a single PXI chassis or
        a single PC. Use configure_for_homogeneous_triggers to configure
        the properties for the reference clocks, start triggers, reference
        triggers, script triggers, and pause triggers. If
        configure_for_homogeneous_triggers cannot perform all the steps
        appropriate for the given sessions, it returns an error. If an error is
        returned, use the instrument driver methods and properties for signal
        routing, along with the following NI-TClk properties:
        start_trigger_master_session
        ref_trigger_master_session
        script_trigger_master_session
        pause_trigger_master_session
        configure_for_homogeneous_triggers affects the following clocks and
        triggers: - Reference clocks - Start triggers - Reference triggers -
        Script triggers - Pause triggers Reference Clocks
        configure_for_homogeneous_triggers configures the reference clocks
        if they are needed. Specifically, if the internal sample clocks or
        internal sample clock timebases are used, and the reference clock source
        is not configured--or is set to None (no trigger
        configured)--configure_for_homogeneous_triggers configures the
        following: PXI--The reference clock source on all devices is set to be
        the 10 MHz PXI backplane clock (PXI_CLK10). PCI--One of the devices
        exports its 10 MHz onboard reference clock to RTSI 7. The reference
        clock source on all devices is set to be RTSI 7. Note: If the reference
        clock source is set to a value other than None,
        configure_for_homogeneous_triggers cannot configure the reference
        clock source. Start Triggers If the start trigger is set to None (no
        trigger configured) for all sessions, the sessions are configured to
        share the start trigger. The start trigger is shared by: - Implicitly
        exporting the start trigger from one session - Configuring the other
        sessions for digital edge start triggers with sources corresponding to
        the exported start trigger - Setting
        start_trigger_master_session to the session that is
        exporting the trigger for all sessions If the start triggers are None
        for all except one session, configure_for_homogeneous_triggers
        configures the sessions to share the start trigger from the one excepted
        session. The start trigger is shared by: - Implicitly exporting start
        trigger from the session with the start trigger that is not None -
        Configuring the other sessions for digital-edge start triggers with
        sources corresponding to the exported start trigger - Setting
        start_trigger_master_session to the session that is
        exporting the trigger for all sessions If start triggers are configured
        for all sessions, configure_for_homogeneous_triggers does not
        affect the start triggers. Start triggers are considered to be
        configured for all sessions if either of the following conditions is
        true: - No session has a start trigger that is None - One session has a
        start trigger that is None, and all other sessions have start triggers
        other than None. The one session with the None trigger must have
        start_trigger_master_session set to itself, indicating
        that the session itself is the start trigger master Reference Triggers
        configure_for_homogeneous_triggers configures sessions that support
        reference triggers to share the reference triggers if the reference
        triggers are None (no trigger configured) for all except one session.
        The reference triggers are shared by: - Implicitly exporting the
        reference trigger from the session whose reference trigger is not None -
        Configuring the other sessions that support the reference trigger for
        digital-edge reference triggers with sources corresponding to the
        exported reference trigger - Setting
        ref_trigger_master_session to the session that is
        exporting the trigger for all sessions that support reference trigger If
        the reference triggers are configured for all sessions that support
        reference triggers, configure_for_homogeneous_triggers does not
        affect the reference triggers. Reference triggers are considered to be
        configured for all sessions if either one or the other of the following
        conditions is true: - No session has a reference trigger that is None -
        One session has a reference trigger that is None, and all other sessions
        have reference triggers other than None. The one session with the None
        trigger must have ref_trigger_master_session set to
        itself, indicating that the session itself is the reference trigger
        master Reference Trigger Holdoffs Acquisition sessions may be configured
        with the reference trigger. For acquisition sessions, when the reference
        trigger is shared, configure_for_homogeneous_triggers configures
        the holdoff properties (which are instrument driver specific) on the
        reference trigger master session so that the session does not recognize
        the reference trigger before the other sessions are ready. This
        condition is only relevant when the sample clock rates, sample clock
        timebase rates, sample counts, holdoffs, and/or any delays for the
        acquisitions are different. When the sample clock rates, sample clock
        timebase rates, and/or the sample counts are different in acquisition
        sessions sharing the reference trigger, you should also set the holdoff
        properties for the reference trigger master using the instrument driver.
        Script Triggers configure_for_homogeneous_triggers configures
        sessions that support script triggers to share them, if the script
        triggers are None (no trigger configured) for all except one session.
        The script triggers are shared in the following ways: - Implicitly
        exporting the script trigger from the session whose script trigger is
        not None - Configuring the other sessions that support the script
        trigger for digital-edge script triggers with sources corresponding to
        the exported script trigger - Setting
        script_trigger_master_session to the session that is
        exporting the trigger for all sessions that support script triggers If
        the script triggers are configured for all sessions that support script
        triggers, configure_for_homogeneous_triggers does not affect script
        triggers. Script triggers are considered to be configured for all
        sessions if either one or the other of the following conditions are
        true: - No session has a script trigger that is None - One session has a
        script trigger that is None and all other sessions have script triggers
        other than None. The one session with the None trigger must have
        script_trigger_master_session set to itself, indicating
        that the session itself is the script trigger master Pause Triggers
        configure_for_homogeneous_triggers configures generation sessions
        that support pause triggers to share them, if the pause triggers are
        None (no trigger configured) for all except one session. The pause
        triggers are shared by: - Implicitly exporting the pause trigger from
        the session whose script trigger is not None - Configuring the other
        sessions that support the pause trigger for digital-edge pause triggers
        with sources corresponding to the exported pause trigger - Setting
        pause_trigger_master_session to the session that is
        exporting the trigger for all sessions that support script triggers If
        the pause triggers are configured for all generation sessions that
        support pause triggers, configure_for_homogeneous_triggers does not
        affect pause triggers. Pause triggers are considered to be configured
        for all sessions if either one or the other of the following conditions
        is true: - No session has a pause trigger that is None - One session has
        a pause trigger that is None and all other sessions have pause triggers
        other than None. The one session with the None trigger must have
        pause_trigger_master_session set to itself, indicating
        that the session itself is the pause trigger master Note: TClk
        synchronization is not supported for pause triggers on acquisition
        sessions.

        Args:
            session_count (int): Number of elements in the sessions array

        '''
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        error_code = self._library.niTClk_ConfigureForHomogeneousTriggers(session_count_ctype, sessions_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def finish_sync_pulse_sender_synchronize(self, session_count, min_time):
        r'''finish_sync_pulse_sender_synchronize

        

        Args:
            session_count (int): Number of elements in the sessions array

            min_time (float): Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

        '''
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        min_time_ctype = _visatype.ViReal64(min_time)  # case S150
        error_code = self._library.niTClk_FinishSyncPulseSenderSynchronize(session_count_ctype, sessions_ctype, min_time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def init_for_documentation(self):
        r'''init_for_documentation

        TBD
        '''
        session_list_ctype = get_ctypes_pointer_for_buffer(value=session_list, library_type=_visatype.ViSession)  # case B550
        error_code = self._library.niTClk_InitForDocumentation(session_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def initiate(self, session_count):
        r'''initiate

        Initiates the acquisition or generation sessions specified, taking into
        consideration any special requirements needed for synchronization. For
        example, the session exporting the TClk-synchronized start trigger is
        not initiated until after initiate initiates all the sessions
        that import the TClk-synchronized start trigger.

        Args:
            session_count (int): Number of elements in the sessions array

        '''
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        error_code = self._library.niTClk_Initiate(session_count_ctype, sessions_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_done(self, session_count):
        r'''is_done

        Monitors the progress of the acquisitions and/or generations
        corresponding to sessions.

        Args:
            session_count (int): Number of elements in the sessions array


        Returns:
            done (bool): Indicates that the operation is done. The operation is done when each
                session has completed without any errors or when any one of the sessions
                reports an error.

        '''
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        done_ctype = _visatype.ViBoolean()  # case S200
        error_code = self._library.niTClk_IsDone(session_count_ctype, sessions_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    def setup_for_sync_pulse_sender_synchronize(self, session_count, min_time):
        r'''setup_for_sync_pulse_sender_synchronize

        

        Args:
            session_count (int): Number of elements in the sessions array

            min_time (float): Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

        '''
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        min_time_ctype = _visatype.ViReal64(min_time)  # case S150
        error_code = self._library.niTClk_SetupForSyncPulseSenderSynchronize(session_count_ctype, sessions_ctype, min_time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def synchronize(self, session_count, min_time):
        r'''synchronize

        Synchronizes the TClk signals on the given sessions. After
        synchronize executes, TClk signals from all sessions are
        synchronized. Note: Before using this NI-TClk method, verify that your
        system is configured as specified in the PXI Trigger Lines and RTSI
        Lines topic of the NI-TClk Synchronization Help. You can locate this
        help file at Start>>Programs>>National Instruments>>NI-TClk.

        Args:
            session_count (int): Number of elements in the sessions array

            min_time (float): Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

        '''
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        min_time_ctype = _visatype.ViReal64(min_time)  # case S150
        error_code = self._library.niTClk_Synchronize(session_count_ctype, sessions_ctype, min_time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def syncronize_to_sync_pulse_sender(self, session_count, min_time):
        r'''syncronize_to_sync_pulse_sender

        

        Args:
            session_count (int): Number of elements in the sessions array

            min_time (float): Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

        '''
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        min_time_ctype = _visatype.ViReal64(min_time)  # case S150
        error_code = self._library.niTClk_SyncronizeToSyncPulseSender(session_count_ctype, sessions_ctype, min_time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_until_done(self, session_count, timeout):
        r'''wait_until_done

        Call this method to pause execution of your program until the
        acquisitions and/or generations corresponding to sessions are done or
        until the method returns a timeout error. wait_until_done is a
        blocking method that periodically checks the operation status. It
        returns control to the calling program if the operation completes
        successfully or an error occurs (including a timeout error). This
        method is most useful for finite data operations that you expect to
        complete within a certain time.

        Args:
            session_count (int): Number of elements in the sessions array

            timeout (float): The amount of time in seconds that wait_until_done waits for the
                sessions to complete. If timeout is exceeded, wait_until_done
                returns an error.

        '''
        session_count_ctype = _visatype.ViUInt32(0 if sessions is None else len(sessions))  # case S160
        sessions_ctype = get_ctypes_pointer_for_buffer(value=sessions, library_type=_visatype.ViSession)  # case B550
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        error_code = self._library.niTClk_WaitUntilDone(session_count_ctype, sessions_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return



