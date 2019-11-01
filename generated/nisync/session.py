# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes
import datetime  # noqa: F401

import nisync._attributes as _attributes
import nisync._converters as _converters
import nisync._library_singleton as _library_singleton
import nisync._visatype as _visatype
import nisync.enums as enums
import nisync.errors as errors


# Used for __repr__
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


def get_ctypes_and_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class _SessionBase(object):
    '''Base class for all NI-Sync sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    clk10_phase_adjust = _attributes.AttributeViReal64(1150107)
    '''Type: float

    Specifies the PXI_Clk10 Phase Adjust Voltage.  When using the PLL to lock PXI_CLK10 to an external reference clock, the phase between the clocks can be adjusted.  The time between rising edges of PXI_CLK10 and the input clock is minimized using this constant.
    '''
    clkin_attenuation_disable = _attributes.AttributeViBoolean(1150505)
    '''Type: bool

    Setting this property to True disables the ClkIn attenuation.
    '''
    clkin_pll_freq = _attributes.AttributeViReal64(1150500)
    '''Type: float

    Specifies the frequency that the PLL should lock to.  The PLL can be used to lock to frequencies between 1 MHz and 100 MHz, in multiples of 1 MHz.
    '''
    clkin_pll_locked = _attributes.AttributeViBoolean(1150502)
    '''Type: bool

    Returns whether or not the PXI_Clk10 PLL is currently locked to a signal at the ClkIn terminal.
    '''
    clkin_use_pll = _attributes.AttributeViBoolean(1150501)
    '''Type: bool

    Specifies whether or not the connection between ClkIn and PXI_Clk10 should use the PLL circuit.  If this Boolean value is set to True, the PLL will be used to lock to the frequency at ClkIn when connecting to PXI_Clk10.  You must set this property before connecting the clock to PXI_Clk10_In.
    '''
    clkout_gain_enable = _attributes.AttributeViBoolean(1150503)
    '''Type: bool

    Setting this property to True increases the ClkOut amplitude.
    '''
    dds_freq = _attributes.AttributeViReal64(1150400)
    '''Type: float

    Specifies the frequency (in Hertz) that the DDS should generate.
    '''
    dds_initial_delay = _attributes.AttributeViReal64(1150402)
    '''Type: float

    Specifies the initial delay (in seconds) that the DDS should wait before it begins generating a specified frequency.  This property must be set prior to setting the DDS frequency, and it must be set using the same NI-Sync instrument driver session that sets the DDS frequency.
    '''
    dds_phase_adjust = _attributes.AttributeViReal64(1150109)
    '''Type: float

    Specifies the DDS Phase Adjust Voltage.
    '''
    dds_update_source = _attributes.AttributeViString(1150401)
    '''Type: str

    Specifies the signal source to be used when updating the DDS frequency.  The default is to update the frequency immediately, i.e. as soon as the frequency is set.  Alternatively, the DDS frequency can be committed to the DDS with an update pulse that arrives on a PXI_Trig terminal.
    '''
    dds_vcxo_voltage = _attributes.AttributeViReal64(1150108)
    '''Type: float

    Specifies the DDS VCXO Voltage.
    '''
    front_sync_clk_src = _attributes.AttributeViString(1150200)
    '''Type: str

    Specifies the synchronization clock source for the front zone (PFI and PFI_LVDS) terminals.
    '''
    gps_antenna_connected = _attributes.AttributeViBoolean(1150900)
    '''Type: bool

    A Boolean that specifies whether the GPS antenna is properly connected.
    '''
    gps_mobile_mode = _attributes.AttributeViBoolean(1150904)
    '''Type: bool

    A Boolean that specifies whether GPS is using mobile mode.  Enabling mobile mode allows the user to move the GPS  antenna and continuously calculate the current position and velocity.  If mobile mode is disabled, the antenna  must remain in a fixed position while the computer is on.  Timing accuracy is significantly improved with mobile  mode disabled.
    '''
    gps_recalculate_position = _attributes.AttributeViBoolean(1150901)
    '''Type: bool

    A Boolean that specifies whether GPS attempts to recalculate the current position at every system reboot. If not  configured to recalculate position, GPS permanently stores the current location. GPS never performs a self survey  until this flag is set.
    '''
    gps_satellites_available = _attributes.AttributeViInt32(1150902)
    '''Type: int

    An integer that specifies the number of GPS satellites currently being tracked. A minimum of four satellites must be  visible for the onboard GPS receiver to perform a self survey. If using GPS as a Time Reference, four or more  satellites must be visible throughout timing measurements for the most accurate results.
    '''
    gps_self_survey = _attributes.AttributeViInt32(1150903)
    '''Type: int

    An integer that specifies the percentage of the GPS self survey that has been completed. The onboard GPS receiver  performs position fixes during the self survey. The individual position fixes are accumulated and averaged over  the course of the self survey. The GPS Time Reference and location information are most accurate after the self  survey has completed and least accurate at the beginning of a self survey. If using GPS as a Time Reference, wait  until the self survey is complete prior to beginning timing measurements for the most accurate results. The onboard  GPS receiver requires at least four visible satellites to perform a self survey.
    '''
    gps_status = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.GpsStatus, 1150905)
    '''Type: enums.GpsStatus

    An integer enumeration that specifies the status of GPS.  This property can be queried to determine if GPS is in a  valid state before the application continues with other operations dependent on GPS. This property can also be used  to troubleshoot various GPS errors.
    '''
    intf_num = _attributes.AttributeViInt32(1150000)
    '''Type: int

    Returns the interface (board) number of this NI PXI-665x.  If there are multiple instances of the NI PXI-665x, each will have a unique interface number.
    '''
    oscillator_voltage = _attributes.AttributeViReal64(1150106)
    '''Type: float

    Specifies the tuning voltage for the OCXO/TCXO.  The OCXO/TCXO frequency can be varied over a small range.  The output frequency is adjusted using this tuning voltage.
    '''
    pfi0_10kohm_enable = _attributes.AttributeViBoolean(1150116)
    '''Type: bool

    Specifies whether or not the PFI0 terminal should be terminated with 10kOhm impedance.
    '''
    pfi0_1kohm_enable = _attributes.AttributeViBoolean(1150110)
    '''Type: bool

    Specifies whether or not the PFI0 terminal should be terminated with 1kOhm impedance.
    '''
    pfi0_threshold = _attributes.AttributeViReal64(1150100)
    '''Type: float

    Specifies the voltage threshold for PFI0 terminal.
    '''
    pfi1_10kohm_enable = _attributes.AttributeViBoolean(1150117)
    '''Type: bool

    Specifies whether or not the PFI1 terminal should be terminated with 10kOhm impedance.
    '''
    pfi1_1kohm_enable = _attributes.AttributeViBoolean(1150111)
    '''Type: bool

    Specifies whether or not the PFI1 terminal should be terminated with 1kOhm impedance.
    '''
    pfi1_threshold = _attributes.AttributeViReal64(1150101)
    '''Type: float

    Specifies the voltage threshold for PFI1 terminal.
    '''
    pfi2_10kohm_enable = _attributes.AttributeViBoolean(1150118)
    '''Type: bool

    Specifies whether or not the PFI2 terminal should be terminated with 10kOhm impedance.
    '''
    pfi2_1kohm_enable = _attributes.AttributeViBoolean(1150112)
    '''Type: bool

    Specifies whether or not the PFI2 terminal should be terminated with 1kOhm impedance.
    '''
    pfi2_threshold = _attributes.AttributeViReal64(1150102)
    '''Type: float

    Specifies the voltage threshold for PFI2 terminal.
    '''
    pfi3_10kohm_enable = _attributes.AttributeViBoolean(1150119)
    '''Type: bool

    Specifies whether or not the PFI3 terminal should be terminated with 10kOhm impedance.
    '''
    pfi3_1kohm_enable = _attributes.AttributeViBoolean(1150113)
    '''Type: bool

    Specifies whether or not the PFI3 terminal should be terminated with 1kOhm impedance.
    '''
    pfi3_threshold = _attributes.AttributeViReal64(1150103)
    '''Type: float

    Specifies the voltage threshold for PFI3 terminal.
    '''
    pfi4_10kohm_enable = _attributes.AttributeViBoolean(1150120)
    '''Type: bool

    Specifies whether or not the PFI4 terminal should be terminated with 10kOhm impedance.
    '''
    pfi4_1kohm_enable = _attributes.AttributeViBoolean(1150114)
    '''Type: bool

    Specifies whether or not the PFI4 terminal should be terminated with 1kOhm impedance.
    '''
    pfi4_threshold = _attributes.AttributeViReal64(1150104)
    '''Type: float

    Specifies the voltage threshold for PFI4 terminal.
    '''
    pfi5_10kohm_enable = _attributes.AttributeViBoolean(1150121)
    '''Type: bool

    Specifies whether or not the PFI5 terminal should be terminated with 10kOhm impedance.
    '''
    pfi5_1kohm_enable = _attributes.AttributeViBoolean(1150115)
    '''Type: bool

    Specifies whether or not the PFI5 terminal should be terminated with 1kOhm impedance.
    '''
    pfi5_threshold = _attributes.AttributeViReal64(1150105)
    '''Type: float

    Specifies the voltage threshold for PFI5 terminal.
    '''
    pxiclk10_present = _attributes.AttributeViBoolean(1150504)
    '''Type: bool

    Returns whether or not the PXI_Clk10 signal is present on the PXI backplane.
    '''
    rear_sync_clk_src = _attributes.AttributeViString(1150201)
    '''Type: str

    Specifies the synchronization clock source for the rear zone (PXI_Trig, PXI_Star, and PXIe_DStarB) terminals.
    '''
    serial_num = _attributes.AttributeViInt32(1150001)
    '''Type: int

    Returns the serial number of this NI PXI-665x interface.
    '''
    sync_clk_div1 = _attributes.AttributeViInt32(1150202)
    '''Type: int

    Specifies the value for the first clock divisor
    '''
    sync_clk_div2 = _attributes.AttributeViInt32(1150203)
    '''Type: int

    Specifies the value for the second clock divisor
    '''
    sync_clk_pfi0_freq = _attributes.AttributeViReal64(1150205)
    '''Type: float

    Specifies the frequency reference (in MHz) for PFI0
    '''
    sync_clk_rst_clk10_cntr_on_pxitrig = _attributes.AttributeViBoolean(1150208)
    '''Type: bool

    Specifies whether or not the PXI_Clk10 clock divider counters should reset on a PXI_Trig line pulse.  The PXI_Trig line used to reset the divided clock counters is specified with the 'Reset Synchronization Clock PXI_Trig Line' property.
    '''
    sync_clk_rst_dds_cntr_on_pxitrig = _attributes.AttributeViBoolean(1150206)
    '''Type: bool

    Specifies whether or not the DDS clock dividers should reset on a PXI_Trig line pulse.  The PXI_Trig line used to reset the divided clock counters is specified with the 'Reset Synchronization Clock PXI_Trig Line' property.
    '''
    sync_clk_rst_pfi0_cntr_on_pxitrig = _attributes.AttributeViBoolean(1150207)
    '''Type: bool

    Specifies whether or not the PFI0 clock divider counters should reset on a PXI_Trig line pulse.  The PXI_Trig line used to reset the divided clock counters is specified with the 'Reset Synchronization Clock PXI_Trig Line' property.
    '''
    sync_clk_rst_pxitrig_num = _attributes.AttributeViString(1150204)
    '''Type: str

    Specifies the PXI_Trig terminal to use to reset the synchronization clock dividers.
    '''
    terminal_state_pfi = _attributes.AttributeViInt32(1150302)
    '''Type: int

    Returns a bitmap containing the current PFI terminal states.  Each bit represents the state of a PFI terminal.  Bit 0 corresponds to PFI0, but 1 corresponds to PFI1, etc.  Bits 6 and above are not defined.
    '''
    terminal_state_pfilvds = _attributes.AttributeViInt32(1150304)
    '''Type: int

    A bitmap containing the current PFI_LVDS terminal states. Each bit represents the state of a PFI_LVDS terminal. Bit 0 corresponds to PFI_LVDS0, bit 1 corresponds to PFI_LVDS1, and bit 2 corresponds to PFI_LVDS2.
    '''
    terminal_state_pxiedstarbperipheral = _attributes.AttributeViBoolean(1150306)
    '''Type: bool

    Returns the logical state of the PXIe_DStarB peripheral terminal.
    '''
    terminal_state_pxiedstarc = _attributes.AttributeViInt32(1150303)
    '''Type: int

    A bitmap containing the current PXIe_DStarC terminal states. Each bit represents the state of a PXIe_DStarC terminal. Bit 0 corresponds to PXIe_DStarC0, bit 1 corresponds to PXIe_DStarC1, etc.
    '''
    terminal_state_pxistar = _attributes.AttributeViInt32(1150300)
    '''Type: int

    Returns a bitmap containing the PXI_Star terminal states.  Each bit represents the state of a PXI_STAR terminal.  Bit 0 corresponds to PXI_STAR0, bit 1 corresponds to PXI_STAR1, etc.  Bits 13 and above are not defined.
    '''
    terminal_state_pxistarperipheral = _attributes.AttributeViBoolean(1150307)
    '''Type: bool

    Returns the logical state of the PXI_Star peripheral terminal.  This value is only valid when the board is in a peripheral slot.
    '''
    terminal_state_pxitrig = _attributes.AttributeViInt32(1150301)
    '''Type: int

    Returns a bitmap containing the PXI_Trig terminal states.  Each bit represents the state of a PXI_TRIG terminal.  Bit 0 corresponds to PXI_TRIG0, bit 1 corresponds to PXI_TRIG1, etc.  Bits 8 and above are not defined.
    '''
    timeref_correction = _attributes.AttributeViReal64(1150804)
    '''Type: float

    A double that specifies a manual correction, in seconds, to apply to the time reference. Use this property to  calibrate the time reference manually to achieve better synchronization with the configured time reference.
    '''
    timeref_enabled = _attributes.AttributeViBoolean(1150812)
    '''Type: bool

    A boolean that specifies whether the time reference associated with this session is enabled.
    '''
    timeref_is_selected = _attributes.AttributeViBoolean(1150813)
    '''Type: bool

    A boolean that represents whether the time reference associated with this session is the selected time reference.
    '''
    timeref_last_sync_id = _attributes.AttributeViInt32(1150807)
    '''Type: int

    An integer that is incremented when a synchronization message is received from the current time reference.   and the 1588 clock is a master.

    Note: that synchronization messages are not received if the time reference is set to free running or if set to 1588
    '''
    timeref_offset = _attributes.AttributeViReal64(1150802)
    '''Type: float

    A double that specifies the calculated offset, in seconds, from the configured time reference. This property can be  used to determine when the local clock is sufficiently synchronized with the selected time reference to continue  operations.
    '''
    timeref_offset_ns = _attributes.AttributeViReal64(1150808)
    '''Type: float

    A double that specifies the calculated offset, in nanoseconds, from the configured time reference. This property can be  used to determine when the local clock is sufficiently synchronized with the selected time reference to continue  operations.
    '''
    timeref_present = _attributes.AttributeViBoolean(1150800)
    '''Type: bool

    A Boolean that specifies whether the configured time reference is currently providing a valid time signal.
    '''
    timeref_selected_name = _attributes.AttributeViString(1150811)
    '''Type: str

    A string that represents the name of the selected time reference.
    '''
    timeref_selected_type = _attributes.AttributeViString(1150809)
    '''Type: str

    A string that represents the synchronization protocol being used by the selected time reference.
    '''
    timeref_type = _attributes.AttributeViString(1150810)
    '''Type: str

    A string that represents the synchronization protocol being used by the time reference associated with this session.
    '''
    timeref_utc_offset = _attributes.AttributeViInt32(1150805)
    '''Type: int

    An integer that specifies the offset, in seconds, of the UTC timescale from the current time reference.
    '''
    timeref_utc_offset_valid = _attributes.AttributeViBoolean(1150806)
    '''Type: bool

    A boolean that specifies whether the UTC offset of the current time reference is valid.
    '''
    user_led_state = _attributes.AttributeViBoolean(1150600)
    '''Type: bool

    Specifies the state of the User LED.  Setting this Boolean value to True will turn on the User LED, and setting it to False will turn off the User LED.
    '''

    def __init__(self, repeated_capability_list, vi, library, encoding, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._vi = vi
        self._library = library
        self._encoding = encoding

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("vi=" + pp.pformat(vi))
        param_list.append("library=" + pp.pformat(library))
        param_list.append("encoding=" + pp.pformat(encoding))
        self._param_list = ', '.join(param_list)

        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nisync', self.__class__.__name__, self._param_list)

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

    ''' These are code-generated '''


class Session(_SessionBase):
    '''An NI-Sync session'''

    def __init__(self, resource_name, id_query, reset_device):
        r'''An NI-Sync session

        This method performs the following initialization actions: - Creates a
        new NI-Sync instrument driver session. - Opens a session to the
        specified device using the interface and address you specify for the
        Resource Name parameter. - If the ID Query parameter is set to True,
        this method queries the instrument ID and checks that it is valid for
        this instrument driver. - If the Reset parameter is set to True,
        this method resets the module to a known state. Returns a ViSession
        handle that you use to identify the instrument in all subsequent
        instrument driver method calls. - Returns an instrument handle that
        you use to identify the instrument in all subsequent instrument driver
        method calls.

        Args:
            resource_name (str): Resource name of the switch module to initialize. The resource name is
                assigned in Measurement & Automation Explorer (MAX). Syntax PXI[bus
                number]::device number NI-DAQmx name Optional fields are shown in square
                brackets ([]).

                Note:
                VISA aliases are also valid for the resource name.
                Example resource names: Resource Name Description Dev1 DAQmx name
                PXI1Slot5 DAQmx name PXI0::15::INSTR PXI bus 0, device number 15
                PXI::15::INSTR PXI bus 0, device number 15 PXI4::9::INSTR PXI bus 4,
                device number 9

            id_query (bool): This parameter is ignored. Because NI-Sync supports multiple timing and
                synchronization modules, it always queries the device to determine which
                device is installed. Valid Values: True - Query the device (Default
                Value) False - Do not query the device

            reset_device (bool): Specify whether you want the to reset the timing and synchronization
                module during the initialization procedure. Valid Range: True (1) -
                Reset Device False (0) - Don't Reset (Default Value)


        Returns:
            session (nisync.Session): A session object representing the device.

                Note:
                Although you can
                create more than one NI-Sync session for the same resource, it is best
                not to do so. A better approach is to use the same NI-Sync session in
                multiple execution threads. You can use VISA methods viLock and
                viUnlock to protect sections of code that require exclusive access to
                the resource.

        '''
        super(Session, self).__init__(repeated_capability_list=[], vi=None, library=None, encoding=None, freeze_it=False)
        self._library = _library_singleton.get()
        self._encoding = 'windows-1251'

        # Call specified init function
        self._vi = 0  # This must be set before calling init().
        self._vi = self.init(resource_name, id_query, reset_device)

        # Instantiate any repeated capability objects

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("id_query=" + pp.pformat(id_query))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        '''close

        This method performs the following operations: - Closes the NI-Sync
        I/O session. - Destroys the NI-Sync session and all of its properties. -
        Deallocates any memory resources the NI-Sync driver uses. Note: If the
        session is locked, you must unlock the session before calling
        _close. Note: After calling _close, you cannot use the
        instrument driver again until you call init. Note: If any clocks
        have been created with the create_clock method in the context
        of this session and have not been cleared, this method clears them. If
        any future time events have been created with the
        create_future_time_event method in the context of this session
        and have not occurred or been cleared, this method clears them. If any
        time stamp triggers have been enabled with the
        enable_time_stamp_trigger method in the context of this session
        and have not been disabled, this method clears them.

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._vi = 0
            raise
        self._vi = 0

    ''' These are code-generated '''

    def clear_clock(self, terminal):
        r'''clear_clock

        This method clears a clock created by the create_clock
        method. Once the clock is cleared, the associated terminal may be used
        for other operations. When this method is called, the specified line
        is tri-stated.

        Args:
            terminal (str): An input string enumeration that specifies the terminal containing the
                digital signal that is the specified clock. Valid Values:
                NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2
                NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2
                NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5
                NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0
                NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3
                NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6
                NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9
                NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12
                NISYNC_VAL_ALL_CONNECTED If NISYNC_VAL_ALL_CONNECTED is specified,
                all clocks created within the context of this session are cleared.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        terminal_ctype = ctypes.create_string_buffer(terminal.encode(self._encoding))  # case C020
        error_code = self._library.niSync_ClearClock(vi_ctype, terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_future_time_events(self, terminal):
        r'''clear_future_time_events

        This method clears future time events created by the
        create_future_time_event method that have not yet occurred. Once
        the future time events are cleared, the associated terminal can be used
        for other operations. When this method is called, the specified line
        is tri-stated.

        Args:
            terminal (str): An input string enumeration that specifies the terminal that will no
                longer generate future time events. Valid Values: NISYNC_VAL_PFI0
                NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PXITRIG0
                NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3
                NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6
                NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1
                NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4
                NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7
                NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10
                NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12
                NISYNC_VAL_ALL_CONNECTED If NISYNC_VAL_ALL_CONNECTED is specified,
                all future time events created within the context of this session are
                cleared.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        terminal_ctype = ctypes.create_string_buffer(terminal.encode(self._encoding))  # case C020
        error_code = self._library.niSync_ClearFutureTimeEvents(vi_ctype, terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_fpga(self, fpga_program_path):
        r'''configure_fpga

        This method programs the FPGA on the module with an alternate
        bitstream file. The bitstream is specified using an absolute path to a
        location on disk. NOTE: This method is an advanced operation and
        should be used with caution.

        Args:
            fpga_program_path (str): This input specifies the full path to an FPGA bitstream file on disk.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        fpga_program_path_ctype = ctypes.create_string_buffer(fpga_program_path.encode(self._encoding))  # case C020
        error_code = self._library.niSync_ConfigureFpga(vi_ctype, fpga_program_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect_clk_terminals(self, source_terminal, destination_terminal):
        r'''connect_clk_terminals

        This method connects a source clock terminal to a destination clock
        terminal. A clock terminal connection is characterized by its source
        terminal and destination terminal.

        Args:
            source_terminal (str): This input specifies the source clock terminal to connect to the
                destination terminal. Valid Values: NISYNC_VAL_CLKIN (Default Value)
                NISYNC_VAL_CLK10 NISYNC_VAL_OSCILLATOR NISYNC_VAL_DDS
                NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2
                NISYNC_VAL_PXIEDSTARC0 NISYNC_VAL_PXIEDSTARC1
                NISYNC_VAL_PXIEDSTARC2 NISYNC_VAL_PXIEDSTARC3
                NISYNC_VAL_PXIEDSTARC4 NISYNC_VAL_PXIEDSTARC5
                NISYNC_VAL_PXIEDSTARC6 NISYNC_VAL_PXIEDSTARC7
                NISYNC_VAL_PXIEDSTARC8 NISYNC_VAL_PXIEDSTARC9
                NISYNC_VAL_PXIEDSTARC10 NISYNC_VAL_PXIEDSTARC11
                NISYNC_VAL_PXIEDSTARC12 NISYNC_VAL_PXIEDSTARC13
                NISYNC_VAL_PXIEDSTARC14 NISYNC_VAL_PXIEDSTARC15
                NISYNC_VAL_PXIEDSTARC16 NISYNC_VAL_PXIEDSTARA

                Note:
                Each
                PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor
                specific. Your chassis documentation may describe this mapping in
                addition to the chassis.ini and pxisys.ini system description files the
                PXI Specification requires.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            destination_terminal (str): This input specifies the destination clock terminal that the source
                terminal will connect to. Valid Values: NISYNC_VAL_CLK10_IN (Default
                Value) NISYNC_VAL_CLKOUT NISYNC_VAL_BOARD_CLK NISYNC_VAL_PFILVDS0
                NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARA0
                NISYNC_VAL_PXIEDSTARA1 NISYNC_VAL_PXIEDSTARA2
                NISYNC_VAL_PXIEDSTARA3 NISYNC_VAL_PXIEDSTARA4
                NISYNC_VAL_PXIEDSTARA5 NISYNC_VAL_PXIEDSTARA6
                NISYNC_VAL_PXIEDSTARA7 NISYNC_VAL_PXIEDSTARA8
                NISYNC_VAL_PXIEDSTARA9 NISYNC_VAL_PXIEDSTARA10
                NISYNC_VAL_PXIEDSTARA11 NISYNC_VAL_PXIEDSTARA12
                NISYNC_VAL_PXIEDSTARA13 NISYNC_VAL_PXIEDSTARA14
                NISYNC_VAL_PXIEDSTARA15 NISYNC_VAL_PXIEDSTARA16

                Note:
                Each
                PXIe_DStarA trigger is mapped to a single slot. This mapping is vendor
                specific. Your chassis documentation may describe this mapping in
                addition to the chassis.ini and pxisys.ini system description files the
                PXI Specification requires.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_terminal_ctype = ctypes.create_string_buffer(source_terminal.encode(self._encoding))  # case C020
        destination_terminal_ctype = ctypes.create_string_buffer(destination_terminal.encode(self._encoding))  # case C020
        error_code = self._library.niSync_ConnectClkTerminals(vi_ctype, source_terminal_ctype, destination_terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect_sw_trig_to_terminal(self, source_terminal, destination_terminal, synchronization_clock, invert, update_edge, delay):
        r'''connect_sw_trig_to_terminal

        This method connects the global software trigger terminal to a
        destination trigger terminal. A software trigger terminal connection is
        characterized by its source terminal, destination terminal, and a
        synchronization clock. The signal at the destination terminal can be
        inverted, synchronized to the rising or falling edge of the
        synchronization clock, and delayed by up to 15 synchronization clock
        cycles.

        Args:
            source_terminal (str): This input specifies the source software trigger terminal to connect to
                the destination terminal. Valid Values: NISYNC_VAL_SWTRIG_GLOBAL
                (Default Value)

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            destination_terminal (str): This input specifies the destination trigger terminal that the global
                software trigger terminal will connect to. Valid Values:
                NISYNC_VAL_PXITRIG0 (Default Value) NISYNC_VAL_PXITRIG1
                NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4
                NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7
                NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2
                NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5
                NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8
                NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11
                NISYNC_VAL_PXISTAR12 NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14
                NISYNC_VAL_PXISTAR15 NISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR
                NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3
                NISYNC_VAL_PFI4 NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0
                NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0
                NISYNC_VAL_PXIEDSTARB1 NISYNC_VAL_PXIEDSTARB2
                NISYNC_VAL_PXIEDSTARB3 NISYNC_VAL_PXIEDSTARB4
                NISYNC_VAL_PXIEDSTARB5 NISYNC_VAL_PXIEDSTARB6
                NISYNC_VAL_PXIEDSTARB7 NISYNC_VAL_PXIEDSTARB8
                NISYNC_VAL_PXIEDSTARB9 NISYNC_VAL_PXIEDSTARB10
                NISYNC_VAL_PXIEDSTARB11 NISYNC_VAL_PXIEDSTARB12
                NISYNC_VAL_PXIEDSTARB13 NISYNC_VAL_PXIEDSTARB14
                NISYNC_VAL_PXIEDSTARB15 NISYNC_VAL_PXIEDSTARB16
                NISYNC_VAL_PXIEDSTARC

                Note:
                Each PXI_Star and PXIe_DStarB trigger is
                mapped to a single slot. This mapping is vendor specific. Your chassis
                documentation may describe this mapping in addition to the chassis.ini
                and pxisys.ini system description files the PXI Specification requires.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            synchronization_clock (str): This input specifies the synchronization clock to use to synchronize the
                destination terminal with the global software trigger terminal.

                Note:
                Asynchronous connections are not valid for software trigger terminal
                connections.

                Note:
                The source of the synchronization clock for software trigger connections
                is determined by the destination terminal trigger "zone" ("front" for
                the PFI lines, and "rear" for the PXI\_Trig and PXI\_Star terminals).
                The source of the synchronization clock for a given trigger zone can be
                selected using the NISYNC\_ATTR\_FRONT\_SYNC\_CLK\_SRC (PFI zone) and
                NISYNC\_ATTR\_REAR\_SYNC\_CLK\_SRC (PXI backplane zone) properties.
                Valid Values: NISYNC\_VAL\_SYNC\_CLK\_FULLSPEED (Default Value)
                NISYNC\_VAL\_SYNC\_CLK\_DIV1 NISYNC\_VAL\_SYNC\_CLK\_DIV2

            invert (int): This input specifies whether or not the global software trigger terminal
                should be inverted at the destination terminal. Valid Values:
                NISYNC_VAL_DONT_INVERT (Default Value) NISYNC_VAL_INVERT

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            update_edge (int): This input specifies the synchronization clock update edge that the
                global software trigger should be propagated on. Valid Values:
                NISYNC_VAL_UPDATE_EDGE_RISING (Default Value)
                NISYNC_VAL_UPDATE_EDGE_FALLING

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            delay (float): This input specifies the number of seconds to delay the global software
                trigger pulse. The delay must be a multiple of the synchronization clock
                period. The global software trigger can be delayed up to 15 clock cycles
                for each route. Default Value: 0.00 seconds

                Note:
                This input is not
                supported on the PXIe-6674.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_terminal_ctype = ctypes.create_string_buffer(source_terminal.encode(self._encoding))  # case C020
        destination_terminal_ctype = ctypes.create_string_buffer(destination_terminal.encode(self._encoding))  # case C020
        synchronization_clock_ctype = ctypes.create_string_buffer(synchronization_clock.encode(self._encoding))  # case C020
        invert_ctype = _visatype.ViInt32(invert)  # case S150
        update_edge_ctype = _visatype.ViInt32(update_edge)  # case S150
        delay_ctype = _visatype.ViReal64(delay)  # case S150
        error_code = self._library.niSync_ConnectSwTrigToTerminal(vi_ctype, source_terminal_ctype, destination_terminal_ctype, synchronization_clock_ctype, invert_ctype, update_edge_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect_trig_terminals(self, source_terminal, destination_terminal, synchronization_clock, invert, update_edge):
        r'''connect_trig_terminals

        This method connects a source trigger terminal to a destination
        trigger terminal. A trigger terminal connection is characterized by its
        source terminal, destination terminal, and a synchronization clock. The
        signal at the destination terminal can be inverted and synchronized to
        the rising or falling edge of the synchronization clock.

        Args:
            source_terminal (str): This input specifies the source trigger terminal to connect to the
                destination terminal.

                Note:  Each PXI\_Star and PXIe\_DStarC trigger is
                mapped to a single slot. This mapping is vendor specific. Your chassis
                documentation may describe this mapping in addition to the chassis.ini
                and pxisys.ini system description files the PXI Specification requires.

                Note:  The source of the synchronization clock for
                trigger connections is determined by the destination terminal (either
                the PFI sync clock zone or the backplane sync clock zone). Also, the two
                divided versions of the synchronization clock are shared between the PFI
                sync clock zone and the backplane sync clock zone. Valid Values:
                NISYNC\_VAL\_PXITRIG0 (Default Value) NISYNC\_VAL\_PXITRIG1
                NISYNC\_VAL\_PXITRIG2 NISYNC\_VAL\_PXITRIG3 NISYNC\_VAL\_PXITRIG4
                NISYNC\_VAL\_PXITRIG5 NISYNC\_VAL\_PXITRIG6 NISYNC\_VAL\_PXITRIG7
                NISYNC\_VAL\_PXISTAR0 NISYNC\_VAL\_PXISTAR1 NISYNC\_VAL\_PXISTAR2
                NISYNC\_VAL\_PXISTAR3 NISYNC\_VAL\_PXISTAR4 NISYNC\_VAL\_PXISTAR5
                NISYNC\_VAL\_PXISTAR6 NISYNC\_VAL\_PXISTAR7 NISYNC\_VAL\_PXISTAR8
                NISYNC\_VAL\_PXISTAR9 NISYNC\_VAL\_PXISTAR10 NISYNC\_VAL\_PXISTAR11
                NISYNC\_VAL\_PXISTAR12 NISYNC\_VAL\_PXISTAR13 NISYNC\_VAL\_PXISTAR14
                NISYNC\_VAL\_PXISTAR15 NISYNC\_VAL\_PXISTAR16 NISYNC\_VAL\_PXISTAR
                NISYNC\_VAL\_PFI0 NISYNC\_VAL\_PFI1 NISYNC\_VAL\_PFI2 NISYNC\_VAL\_PFI3
                NISYNC\_VAL\_PFI4 NISYNC\_VAL\_PFI5 NISYNC\_VAL\_PFILVDS0
                NISYNC\_VAL\_PFILVDS1 NISYNC\_VAL\_PFILVDS2 NISYNC\_VAL\_GND
                NISYNC\_VAL\_SYNC\_CLK\_FULLSPEED NISYNC\_VAL\_SYNC\_CLK\_DIV1
                NISYNC\_VAL\_SYNC\_CLK\_DIV2 NISYNC\_VAL\_CLKIN NISYNC\_VAL\_PXIEDSTARC0
                NISYNC\_VAL\_PXIEDSTARC1 NISYNC\_VAL\_PXIEDSTARC2
                NISYNC\_VAL\_PXIEDSTARC3 NISYNC\_VAL\_PXIEDSTARC4
                NISYNC\_VAL\_PXIEDSTARC5 NISYNC\_VAL\_PXIEDSTARC6
                NISYNC\_VAL\_PXIEDSTARC7 NISYNC\_VAL\_PXIEDSTARC8
                NISYNC\_VAL\_PXIEDSTARC9 NISYNC\_VAL\_PXIEDSTARC10
                NISYNC\_VAL\_PXIEDSTARC11 NISYNC\_VAL\_PXIEDSTARC12
                NISYNC\_VAL\_PXIEDSTARC13 NISYNC\_VAL\_PXIEDSTARC14
                NISYNC\_VAL\_PXIEDSTARC15 NISYNC\_VAL\_PXIEDSTARC16
                NISYNC\_VAL\_PXIEDSTARB

            destination_terminal (str): This input specifies the destination trigger terminal that the source
                terminal will connect to. Valid Values: NISYNC_VAL_PXITRIG0
                NISYNC_VAL_PXITRIG1 (Default Value) NISYNC_VAL_PXITRIG2
                NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5
                NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0
                NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3
                NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6
                NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9
                NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12
                NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15
                NISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR NISYNC_VAL_PFI0
                NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4
                NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1
                NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0 NISYNC_VAL_PXIEDSTARB1
                NISYNC_VAL_PXIEDSTARB2 NISYNC_VAL_PXIEDSTARB3
                NISYNC_VAL_PXIEDSTARB4 NISYNC_VAL_PXIEDSTARB5
                NISYNC_VAL_PXIEDSTARB6 NISYNC_VAL_PXIEDSTARB7
                NISYNC_VAL_PXIEDSTARB8 NISYNC_VAL_PXIEDSTARB9
                NISYNC_VAL_PXIEDSTARB10 NISYNC_VAL_PXIEDSTARB11
                NISYNC_VAL_PXIEDSTARB12 NISYNC_VAL_PXIEDSTARB13
                NISYNC_VAL_PXIEDSTARB14 NISYNC_VAL_PXIEDSTARB15
                NISYNC_VAL_PXIEDSTARB16 NISYNC_VAL_PXIEDSTARC

                Note:
                Each PXI_Star
                and PXIe_DStarB trigger is mapped to a single slot. This mapping is
                vendor specific. Your chassis documentation may describe this mapping in
                addition to the chassis.ini and pxisys.ini system description files the
                PXI Specification requires.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            synchronization_clock (str): This input specifies the synchronization clock to use to synchronize the
                destination terminal with the source terminal for this connection.

                Note:
                The source of the synchronization clock for trigger connections is
                determined by the destination terminal trigger "zone" ("front" for the
                PFI lines, and "rear" for the PXI_Trig and PXI_Star terminals). The
                source of the synchronization clock for a given trigger zone can be
                selected using the front_sync_clk_src (PFI zone) and
                rear_sync_clk_src (PXI backplane zone) properties.
                Valid Values: NISYNC_VAL_SYNC_CLK_ASYNC
                NISYNC_VAL_SYNC_CLK_FULLSPEED NISYNC_VAL_SYNC_CLK_DIV1
                NISYNC_VAL_SYNC_CLK_DIV2

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            invert (int): This input specifies whether or not the signal at the source terminal
                should be inverted at the destination terminal.

                Note:
                The source and
                destination must be connected synchronously for the signal to be
                inverted. Valid Values: NISYNC_VAL_DONT_INVERT (Default Value)
                NISYNC_VAL_INVERT

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            update_edge (int): This input specifies the synhronization clock update edge that a
                connected signal should be propagated on. Note that the source and
                destination terminals must be connected synchronously for this parameter
                to apply. Valid Values: NISYNC_VAL_UPDATE_EDGE_RISING (Default
                Value) NISYNC_VAL_UPDATE_EDGE_FALLING

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_terminal_ctype = ctypes.create_string_buffer(source_terminal.encode(self._encoding))  # case C020
        destination_terminal_ctype = ctypes.create_string_buffer(destination_terminal.encode(self._encoding))  # case C020
        synchronization_clock_ctype = ctypes.create_string_buffer(synchronization_clock.encode(self._encoding))  # case C020
        invert_ctype = _visatype.ViInt32(invert)  # case S150
        update_edge_ctype = _visatype.ViInt32(update_edge)  # case S150
        error_code = self._library.niSync_ConnectTrigTerminals(vi_ctype, source_terminal_ctype, destination_terminal_ctype, synchronization_clock_ctype, invert_ctype, update_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_clock(self, terminal, high_ticks, low_ticks, start_time_seconds, start_time_nanoseconds, start_time_fractional_nsecs, stop_time_seconds, stop_time_nanoseconds, stop_time_fractional_nsecs):
        r'''create_clock

        This method creates a clock synchronized to the board time associated
        with the specified instrument handle. The terminal associated with this
        clock cannot be used for other operations until the clock is cleared
        with the clear_clock method or the session is closed with the
        Close method. When this method is called, the digital signal
        on the specified terminal is driven low until the clock starts.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Args:
            terminal (str): An input string enumeration that specifies the terminal containing the
                digital signal that is the specified clock. Valid Values:
                NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2
                NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5
                NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0
                NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3
                NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6
                NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9
                NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            high_ticks (int): An input integer that specifies the high ticks of the clock generated on
                the specified terminal. The clock resolution, which can be queried using
                the 1588_CLK_RESOLUTION property, determines the length
                of a tick.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            low_ticks (int): An input integer that specifies the low ticks of the clock generated on
                the specified terminal. The clock resolution, which can be queried using
                the 1588_CLK_RESOLUTION property, determines the length
                of a tick.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            start_time_seconds (int): An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will start. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of seconds is assumed to be within the
                supported time range. Specify 0 to start the clock immediately.

            start_time_nanoseconds (int): An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will start. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of nanoseconds is assumed to be within
                the supported time range. Specify 0 to start the clock immediately.

            start_time_fractional_nsecs (int): An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will start. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of fractional nanoseconds is assumed to
                be within the supported time range. Specify 0 to start the clock
                immediately.

            stop_time_seconds (int): An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will stop. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of seconds is assumed to be within the
                supported time range. Specify 0 to never stop the clock.

            stop_time_nanoseconds (int): An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will stop. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of nanoseconds is assumed to be within
                the supported time range. Specify 0 to never stop the clock.

            stop_time_fractional_nsecs (int): An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will stop. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of fractional nanoseconds is assumed to
                be within the supported time range. Specify 0 to never stop the clock.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        terminal_ctype = ctypes.create_string_buffer(terminal.encode(self._encoding))  # case C020
        high_ticks_ctype = _visatype.ViUInt32(high_ticks)  # case S150
        low_ticks_ctype = _visatype.ViUInt32(low_ticks)  # case S150
        start_time_seconds_ctype = _converters.convert_timedelta_to_seconds(start_time_seconds, _visatype.ViUInt32)  # case S140
        start_time_nanoseconds_ctype = _visatype.ViUInt32(start_time_nanoseconds)  # case S150
        start_time_fractional_nsecs_ctype = _visatype.ViUInt16(start_time_fractional_nsecs)  # case S150
        stop_time_seconds_ctype = _visatype.ViUInt32(stop_time_seconds)  # case S150
        stop_time_nanoseconds_ctype = _visatype.ViUInt32(stop_time_nanoseconds)  # case S150
        stop_time_fractional_nsecs_ctype = _visatype.ViUInt16(stop_time_fractional_nsecs)  # case S150
        error_code = self._library.niSync_CreateClock(vi_ctype, terminal_ctype, high_ticks_ctype, low_ticks_ctype, start_time_seconds_ctype, start_time_nanoseconds_ctype, start_time_fractional_nsecs_ctype, stop_time_seconds_ctype, stop_time_nanoseconds_ctype, stop_time_fractional_nsecs_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_future_time_event(self, terminal, output_level, time_seconds, time_nanoseconds, time_fractional_nanoseconds):
        r'''create_future_time_event

        This method creates a future time event that is synchronized to the
        board time associated with the specified session handle. To create
        multiple future time events, invoke this method multiple times. The
        terminal associated with this future time event cannot be used for
        operations other than generating future time events until the future
        time events are cleared with the clear_future_time_events method
        or the session is closed with the _close method. When this
        method is invoked, the digital signal on the specified terminal is
        driven low until the first future time event occurs. Note: The NI-Sync
        family of devices uses the TAI timescale.

        Args:
            terminal (str): An input string that specifies the terminal generating the digital
                signal whose state is set to the specified value. Valid Values:
                NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2
                NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2
                NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5
                NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0
                NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3
                NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6
                NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9
                NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            output_level (int): An input integer enumeration that specifies the level to set the digital
                signal to at the specified time. Valid Values: NISYNC_VAL_LEVEL_LOW
                NISYNC_VAL_LEVEL_HIGH

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            time_seconds (int): An input integer that specifies a portion of the board time that
                specifies when to change to the specified state of the digital signal on
                the specified terminal. Note that NI-Sync supports only the time range
                between 1 January 1970 and 1 January 2100. Therefore, the specified
                number of seconds is assumed to be within the supported time range.
                Specify 0 to generate the future time event immediately.

            time_nanoseconds (int): An input integer that specifies a portion of the board time that
                specifies when to change to the specified state of the digital signal on
                the specified terminal. Note that NI-Sync supports only the time range
                between 1 January 1970 and 1 January 2100. Therefore, the specified
                number of nanoseconds is assumed to be within the supported time range.
                Specify 0 to generate the future time event immediately.

            time_fractional_nanoseconds (int): An input integer that specifies a portion of the board time that
                specifies when to change to the specified state of the digital signal on
                the specified terminal. Note that NI-Sync supports only the time range
                between 1 January 1970 and 1 January 2100. Therefore, the specified
                number of fractional nanoseconds is assumed to be within the supported
                time range. Specify 0 to generate the future time event immediately.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        terminal_ctype = ctypes.create_string_buffer(terminal.encode(self._encoding))  # case C020
        output_level_ctype = _visatype.ViInt32(output_level)  # case S150
        time_seconds_ctype = _visatype.ViUInt32(time_seconds)  # case S150
        time_nanoseconds_ctype = _visatype.ViUInt32(time_nanoseconds)  # case S150
        time_fractional_nanoseconds_ctype = _visatype.ViUInt16(time_fractional_nanoseconds)  # case S150
        error_code = self._library.niSync_CreateFutureTimeEvent(vi_ctype, terminal_ctype, output_level_ctype, time_seconds_ctype, time_nanoseconds_ctype, time_fractional_nanoseconds_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_gps_timestamping(self):
        r'''disable_gps_timestamping

        This method disables timestamping enabled by
        EnableGPSTimestamping.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSync_DisableGpsTimestamping(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_irig_timestamping(self, terminal_name):
        r'''disable_irig_timestamping

        This method disables timestamping enabled by
        EnableIRIGTimestamping. The associated terminal may be used for
        other operations once timestamping has been disabled.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Args:
            terminal_name (str): An input string that specifies the terminal to which the IRIG input is
                connected.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        terminal_name_ctype = ctypes.create_string_buffer(terminal_name.encode(self._encoding))  # case C020
        error_code = self._library.niSync_DisableIrigTimestamping(vi_ctype, terminal_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable_time_stamp_trigger(self, terminal):
        r'''disable_time_stamp_trigger

        This method disables a time stamp trigger enabled by the
        enable_time_stamp_trigger method. Once the time stamp trigger is
        disabled, the associated terminal may be used for other operations.

        Args:
            terminal (str): An input string enumeration that specifies the terminal containing the
                digital signal that is the trigger to stop time stamping. Valid Values:
                NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2
                NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2
                NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5
                NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0
                NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3
                NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6
                NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9
                NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12
                NISYNC_VAL_ALL_CONNECTED If NISYNC_VAL_ALL_CONNECTED is specified,
                all time stamp triggers enabled within the context of this session are
                disabled.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        terminal_ctype = ctypes.create_string_buffer(terminal.encode(self._encoding))  # case C020
        error_code = self._library.niSync_DisableTimeStampTrigger(vi_ctype, terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_clk_terminals(self, source_terminal, destination_terminal):
        r'''disconnect_clk_terminals

        This method disconnects a source clock terminal from a destination
        clock terminal.

        Args:
            source_terminal (str): This input specifies the source clock terminal to disconnect from the
                destination terminal. The source and destination terminals must be
                connected for this operation to succeed. Valid Values:
                NISYNC_VAL_CLKIN NISYNC_VAL_CLK10 NISYNC_VAL_OSCILLATOR
                NISYNC_VAL_DDS NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1
                NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARC0 NISYNC_VAL_PXIEDSTARC1
                NISYNC_VAL_PXIEDSTARC2 NISYNC_VAL_PXIEDSTARC3
                NISYNC_VAL_PXIEDSTARC4 NISYNC_VAL_PXIEDSTARC5
                NISYNC_VAL_PXIEDSTARC6 NISYNC_VAL_PXIEDSTARC7
                NISYNC_VAL_PXIEDSTARC8 NISYNC_VAL_PXIEDSTARC9
                NISYNC_VAL_PXIEDSTARC10 NISYNC_VAL_PXIEDSTARC11
                NISYNC_VAL_PXIEDSTARC12 NISYNC_VAL_PXIEDSTARC13
                NISYNC_VAL_PXIEDSTARC14 NISYNC_VAL_PXIEDSTARC15
                NISYNC_VAL_PXIEDSTARC16 NISYNC_VAL_PXIEDSTARA
                NISYNC_VAL_ALL_CONNECTED (Default Value)

                Note:
                Each PXIe_DStarC
                trigger is mapped to a single slot. This mapping is vendor specific.
                Your chassis documentation may describe this mapping in addition to the
                chassis.ini and pxisys.ini system description files the PXI
                Specification requires.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            destination_terminal (str): This input specifies the destination clock terminal that the source
                terminal will disconnect from. The source and destination must be
                connected for this operation to succeed. Valid Values:
                NISYNC_VAL_CLKIN NISYNC_VAL_CLK10_IN NISYNC_VAL_CLKOUT
                NISYNC_VAL_BOARD_CLK NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1
                NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARA0 NISYNC_VAL_PXIEDSTARA1
                NISYNC_VAL_PXIEDSTARA2 NISYNC_VAL_PXIEDSTARA3
                NISYNC_VAL_PXIEDSTARA4 NISYNC_VAL_PXIEDSTARA5
                NISYNC_VAL_PXIEDSTARA6 NISYNC_VAL_PXIEDSTARA7
                NISYNC_VAL_PXIEDSTARA8 NISYNC_VAL_PXIEDSTARA9
                NISYNC_VAL_PXIEDSTARA10 NISYNC_VAL_PXIEDSTARA11
                NISYNC_VAL_PXIEDSTARA12 NISYNC_VAL_PXIEDSTARA13
                NISYNC_VAL_PXIEDSTARA14 NISYNC_VAL_PXIEDSTARA15
                NISYNC_VAL_PXIEDSTARA16 NISYNC_VAL_ALL_CONNECTED (Default Value)

                Note:
                Each PXIe_DStarA trigger is mapped to a single slot. This mapping
                is vendor specific. Your chassis documentation may describe this mapping
                in addition to the chassis.ini and pxisys.ini system description files
                the PXI Specification requires.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_terminal_ctype = ctypes.create_string_buffer(source_terminal.encode(self._encoding))  # case C020
        destination_terminal_ctype = ctypes.create_string_buffer(destination_terminal.encode(self._encoding))  # case C020
        error_code = self._library.niSync_DisconnectClkTerminals(vi_ctype, source_terminal_ctype, destination_terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_sw_trig_from_terminal(self, source_terminal, destination_terminal):
        r'''disconnect_sw_trig_from_terminal

        This method disconnects the global software trigger terminal from a
        destination trigger terminal.

        Args:
            source_terminal (str): This input specifies the source software trigger terminal to disconnect
                from the destination terminal. The global software trigger must be
                connected to the destination terminal for this operation to succeed.
                Valid Values: NISYNC_VAL_SWTRIG_GLOBAL (Default Value)

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            destination_terminal (str): This input specifies the destination trigger terminal that the global
                software trigger terminal will disconnect from. The global software
                trigger must be connected to the destination terminal for this operation
                to succeed. Valid Values: NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1
                NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4
                NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7
                NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2
                NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5
                NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8
                NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11
                NISYNC_VAL_PXISTAR12 NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14
                NISYNC_VAL_PXISTAR15 NISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR
                NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3
                NISYNC_VAL_PFI4 NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0
                NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0
                NISYNC_VAL_PXIEDSTARB1 NISYNC_VAL_PXIEDSTARB2
                NISYNC_VAL_PXIEDSTARB3 NISYNC_VAL_PXIEDSTARB4
                NISYNC_VAL_PXIEDSTARB5 NISYNC_VAL_PXIEDSTARB6
                NISYNC_VAL_PXIEDSTARB7 NISYNC_VAL_PXIEDSTARB8
                NISYNC_VAL_PXIEDSTARB9 NISYNC_VAL_PXIEDSTARB10
                NISYNC_VAL_PXIEDSTARB11 NISYNC_VAL_PXIEDSTARB12
                NISYNC_VAL_PXIEDSTARB13 NISYNC_VAL_PXIEDSTARB14
                NISYNC_VAL_PXIEDSTARB15 NISYNC_VAL_PXIEDSTARB16
                NISYNC_VAL_PXIEDSTARC NISYNC_VAL_ALL_CONNECTED (Default Value)

                Note:
                Each PXI_Star and PXIe_DStarB trigger is mapped to a single
                slot. This mapping is vendor specific. Your chassis documentation may
                describe this mapping in addition to the chassis.ini and pxisys.ini
                system description files the PXI Specification requires.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_terminal_ctype = ctypes.create_string_buffer(source_terminal.encode(self._encoding))  # case C020
        destination_terminal_ctype = ctypes.create_string_buffer(destination_terminal.encode(self._encoding))  # case C020
        error_code = self._library.niSync_DisconnectSwTrigFromTerminal(vi_ctype, source_terminal_ctype, destination_terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_trig_terminals(self, source_terminal, destination_terminal):
        r'''disconnect_trig_terminals

        This method disconnects a source trigger terminal from a destination
        trigger terminal.

        Args:
            source_terminal (str): This input specifies the source trigger terminal to disconnect from the
                destination terminal. The source and destination terminals must be
                connected for this operation to succeed. Valid Values:
                NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2
                NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5
                NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0
                NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3
                NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6
                NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9
                NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12
                NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15
                NISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR NISYNC_VAL_PFI0
                NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4
                NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1
                NISYNC_VAL_PFILVDS2 NISYNC_VAL_GND NISYNC_VAL_SYNC_CLK_FULLSPEED
                NISYNC_VAL_SYNC_CLK_DIV1 NISYNC_VAL_SYNC_CLK_DIV2
                NISYNC_VAL_CLKIN NISYNC_VAL_PXIEDSTARC0 NISYNC_VAL_PXIEDSTARC1
                NISYNC_VAL_PXIEDSTARC2 NISYNC_VAL_PXIEDSTARC3
                NISYNC_VAL_PXIEDSTARC4 NISYNC_VAL_PXIEDSTARC5
                NISYNC_VAL_PXIEDSTARC6 NISYNC_VAL_PXIEDSTARC7
                NISYNC_VAL_PXIEDSTARC8 NISYNC_VAL_PXIEDSTARC9
                NISYNC_VAL_PXIEDSTARC10 NISYNC_VAL_PXIEDSTARC11
                NISYNC_VAL_PXIEDSTARC12 NISYNC_VAL_PXIEDSTARC13
                NISYNC_VAL_PXIEDSTARC14 NISYNC_VAL_PXIEDSTARC15
                NISYNC_VAL_PXIEDSTARC16 NISYNC_VAL_PXIEDSTARB
                NISYNC_VAL_ALL_CONNECTED (Default Value)

                Note:
                Each PXI_Star and
                PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor
                specific. Your chassis documentation may describe this mapping in
                addition to the chassis.ini and pxisys.ini system description files the
                PXI Specification requires.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            destination_terminal (str): This input specifies the destination trigger terminal that the source
                terminal disconnect from. The source and destination terminals must be
                connected for this operation to succeed. Valid Values:
                NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2
                NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5
                NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0
                NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3
                NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6
                NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9
                NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12
                NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15
                NISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR NISYNC_VAL_PFI0
                NISYNC_VAL_PFI1 NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4
                NISYNC_VAL_PFI5 NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1
                NISYNC_VAL_PFILVDS2 NISYNC_VAL_PXIEDSTARB0 NISYNC_VAL_PXIEDSTARB1
                NISYNC_VAL_PXIEDSTARB2 NISYNC_VAL_PXIEDSTARB3
                NISYNC_VAL_PXIEDSTARB4 NISYNC_VAL_PXIEDSTARB5
                NISYNC_VAL_PXIEDSTARB6 NISYNC_VAL_PXIEDSTARB7
                NISYNC_VAL_PXIEDSTARB8 NISYNC_VAL_PXIEDSTARB9
                NISYNC_VAL_PXIEDSTARB10 NISYNC_VAL_PXIEDSTARB11
                NISYNC_VAL_PXIEDSTARB12 NISYNC_VAL_PXIEDSTARB13
                NISYNC_VAL_PXIEDSTARB14 NISYNC_VAL_PXIEDSTARB15
                NISYNC_VAL_PXIEDSTARB16 NISYNC_VAL_PXIEDSTARC
                NISYNC_VAL_ALL_CONNECTED (Default Value)

                Note:
                Each PXI_Star and
                PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor
                specific. Your chassis documentation may describe this mapping in
                addition to the chassis.ini and pxisys.ini system description files the
                PXI Specification requires.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_terminal_ctype = ctypes.create_string_buffer(source_terminal.encode(self._encoding))  # case C020
        destination_terminal_ctype = ctypes.create_string_buffer(destination_terminal.encode(self._encoding))  # case C020
        error_code = self._library.niSync_DisconnectTrigTerminals(vi_ctype, source_terminal_ctype, destination_terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enable_gps_timestamping(self):
        r'''enable_gps_timestamping

        This method enables timestamping of the GPS pulse per second
        synchronized to the board time associated with the specified instrument
        handle.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSync_EnableGpsTimestamping(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enable_irig_timestamping(self, irig_type, terminal_name):
        r'''enable_irig_timestamping

        This method enables timestamping IRIG decodes synchronized to the
        board time associated with the specified instrument handle. The terminal
        associated with this timestamp cannot be used for other operations until
        timestamping is disabled with DisableIRIGTimestamping or the
        session is closed with _close.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Args:
            irig_type (int): An input integer enumeration of the IRIG input being supplied. Valid
                Values: NISYNC_VAL_IRIG_TYPE_IRIGB_DC
                NISYNC_VAL_IRIG_TYPE_IRIGB_AM (Default)

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            terminal_name (str): An input string that specifies the terminal to which the IRIG input is
                connected.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        irig_type_ctype = _visatype.ViInt32(irig_type)  # case S150
        terminal_name_ctype = ctypes.create_string_buffer(terminal_name.encode(self._encoding))  # case C020
        error_code = self._library.niSync_EnableIrigTimestamping(vi_ctype, irig_type_ctype, terminal_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enable_time_stamp_trigger(self, terminal, active_edge):
        r'''enable_time_stamp_trigger

        This method enables time stamping of a specified trigger synchronized
        to the board time associated with the specified session handle. The
        terminal associated with this time stamp trigger cannot be used for
        other operations until the time stamp trigger is disabled with the
        disable_time_stamp_trigger method or the session is closed with
        the Close method.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Args:
            terminal (str): An input string enumeration that specifies the terminal containing the
                digital signal that is the trigger to start time stamping. Valid Values:
                NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2
                NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2
                NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5
                NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0
                NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3
                NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6
                NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9
                NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            active_edge (int): An input integer enumeration that specifies the trigger conditions.
                Valid Values: NISYNC_VAL_EDGE_RISING NISYNC_VAL_EDGE_FALLING
                NISYNC_VAL_EDGE_ANY

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        terminal_ctype = ctypes.create_string_buffer(terminal.encode(self._encoding))  # case C020
        active_edge_ctype = _visatype.ViInt32(active_edge)  # case S150
        error_code = self._library.niSync_EnableTimeStampTrigger(vi_ctype, terminal_ctype, active_edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def enable_time_stamp_trigger_with_decimation(self, terminal, active_edge, decimation_count):
        r'''enable_time_stamp_trigger_with_decimation

        This method enables time stamping of a specified trigger synchronized
        to the board time associated with the specified session handle. The
        terminal associated with this time stamp trigger cannot be used for
        other operations until the time stamp trigger is disabled with the
        disable_time_stamp_trigger method or the session is closed with
        the Close method.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Args:
            terminal (str): An input string enumeration that specifies the terminal containing the
                digital signal that is the trigger to start time stamping. Valid Values:
                NISYNC_VAL_PFI0 NISYNC_VAL_PFI1 NISYNC_VAL_PFI2
                NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2
                NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5
                NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0
                NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3
                NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6
                NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9
                NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            active_edge (int): An input integer enumeration that specifies the trigger conditions.
                Valid Values: NISYNC_VAL_EDGE_RISING NISYNC_VAL_EDGE_FALLING
                NISYNC_VAL_EDGE_ANY

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            decimation_count (int): An input specifying how frequently to timestamp incoming trigger events.
                For example, if you pass in a value of 4, every fourth event is
                timestamped. The default is 1. This value must be greater than or equal
                to 1.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        terminal_ctype = ctypes.create_string_buffer(terminal.encode(self._encoding))  # case C020
        active_edge_ctype = _visatype.ViInt32(active_edge)  # case S150
        decimation_count_ctype = _visatype.ViUInt32(decimation_count)  # case S150
        error_code = self._library.niSync_EnableTimeStampTriggerWithDecimation(vi_ctype, terminal_ctype, active_edge_ctype, decimation_count_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_attribute_vi_boolean(self, active_item, attribute_id):
        r'''get_attribute_vi_boolean

        This method sets the value of a ViBoolean property.

        Args:
            active_item (str): Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

            attribute_id (int): This parameter specifies the ID of the property you wish to get.


        Returns:
            attribute_value (bool): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing .

                Note:
                Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        active_item_ctype = ctypes.create_string_buffer(active_item.encode(self._encoding))  # case C020
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niSync_GetAttributeViBoolean(vi_ctype, active_item_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def get_attribute_vi_int32(self, active_item, attribute_id):
        r'''get_attribute_vi_int32

        This method queries the value of a ViInt32 property.

        Args:
            active_item (str): Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

            attribute_id (int): This parameter specifies the ID of the property you wish to get.


        Returns:
            attribute_value (int): Returns the current value of the property. Pass the address of a
                ViInt32 variable. From the method panel window, you can use this
                control as follows. - If the property currently showing in the
                Property ID ring control has named constants as valid values, you can
                view a list of the constants by pressing on this control. Select a value
                by double-clicking on it or by selecting it and then pressing .

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        active_item_ctype = ctypes.create_string_buffer(active_item.encode(self._encoding))  # case C020
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSync_GetAttributeViInt32(vi_ctype, active_item_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_real64(self, active_item, attribute_id):
        r'''get_attribute_vi_real64

        This method queries the value of a ViReal64 property.

        Args:
            active_item (str): Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

            attribute_id (int): This parameter specifies the ID of the property you wish to get.


        Returns:
            attribute_value (float): Returns the current value of the property. Pass the address of a
                ViReal64 variable. From the method panel window, you can use this
                control as follows. - If the property currently showing in the
                Property ID ring control has named constants as valid values, you can
                view a list of the constants by pressing on this control. Select a value
                by double-clicking on it or by selecting it and then pressing .

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        active_item_ctype = ctypes.create_string_buffer(active_item.encode(self._encoding))  # case C020
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niSync_GetAttributeViReal64(vi_ctype, active_item_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def get_attribute_vi_string(self, active_item, attribute_id):
        r'''get_attribute_vi_string

        This method queries the value of a ViString property. You can use
        this method to get the values of instrument- specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        property. - State caching is enabled and the currently cached value is
        invalid. You must provide a ViChar array to serve as a buffer for the
        value. You pass the number of bytes in the buffer as the Buffer Size
        parameter. If the current value of the property, including the
        terminating NUL byte, is larger than the size you indicate in the Buffer
        Size parameter, the method copies Buffer Size - 1 bytes into the
        buffer, places an ASCII NUL byte at the end of the buffer, and returns
        the buffer size you must pass to get the entire value. For example, if
        the value is "123456" and the Buffer Size is 4, the method places
        "123" into the buffer and returns 7. If you want to call this method
        just to get the required buffer size, you can pass 0 for the Buffer Size
        and VI_NULL for the Property Value buffer. If you want the method to
        fill in the buffer regardless of the number of bytes in the value, pass
        a negative number for the Buffer Size parameter.

        Args:
            active_item (str): Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

            attribute_id (int): This parameter specifies the ID of the property you wish to get.


        Returns:
            attribute_value (str): The buffer in which the method returns the current value of the
                property. The buffer must be of type ViChar and have at least as many
                bytes as indicated in the Buffer Size parameter. If the current value of
                the property, including the terminating NUL byte, contains more bytes
                that you indicate in this parameter, the method copies Buffer Size - 1
                bytes into the buffer, places an ASCII NUL byte at the end of the
                buffer, and returns the buffer size you must pass to get the entire
                value. For example, if the value is "123456" and the Buffer Size is 4,
                the method places "123" into the buffer and returns 7. If you specify
                0 for the Buffer Size parameter, you can pass VI_NULL for this
                parameter. From the method panel window, you can use this control as
                follows. - If the property currently showing in the Property ID ring
                control has named constants as valid values, you can view a list of the
                constants by pressing on this control. Select a value by double-clicking
                on it or by selecting it and then pressing .

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        active_item_ctype = ctypes.create_string_buffer(active_item.encode(self._encoding))  # case C020
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niSync_GetAttributeViString(vi_ctype, active_item_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niSync_GetAttributeViString(vi_ctype, active_item_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def get_location(self):
        r'''get_location

        This method returns the last calculated location of the onboard GPS
        receiver. The method returns latitude and longitude in degrees and
        altitude in meters. An external GPS antenna must be connected to receive
        valid data from this method. For best results, allow the GPS receiver
        to complete a self survey before reading location.

        Returns:
            latitude (float): An input double pointer. The caller of this method must allocate a
                ViReal64 and pass the pointer in this argument. The method sets the
                ViReal64 value to the latitude reported by the onboard GPS receiver.
                Negative values represent southern latitude. Positive values represent
                northern latitude.

            longitude (float): An input double pointer. The caller of this method must allocate a
                ViReal64 and pass the pointer in this argument. The method sets the
                ViReal64 value to the longitude reported by the onboard GPS receiver.
                Negative values represent western longitude. Positive values represent
                eastern longitude.

            altitude (float): An input double pointer. The caller of this method must allocate a
                ViReal64 and pass the pointer in this argument. The method sets the
                ViReal64 value to the altitude reported by the onboard GPS receiver.
                Returns current altitude in meters (WGS-84 earth ellipsoid).

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        latitude_ctype = _visatype.ViReal64()  # case S220
        longitude_ctype = _visatype.ViReal64()  # case S220
        altitude_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niSync_GetLocation(vi_ctype, None if latitude_ctype is None else (ctypes.pointer(latitude_ctype)), None if longitude_ctype is None else (ctypes.pointer(longitude_ctype)), None if altitude_ctype is None else (ctypes.pointer(altitude_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(latitude_ctype.value), float(longitude_ctype.value), float(altitude_ctype.value)

    def get_time(self):
        r'''get_time

        This method gets the board time associated with the specified session
        handle. Note: NI-Sync supports only the time range between 1 January
        1970 and 1 January 2100. Therefore, if the supported time range has
        ended, an error is returned. Note: The NI-Sync family of devices uses
        the TAI timescale

        Returns:
            time_seconds (int): An output integer that specifies a portion of the board time.

            time_nanoseconds (int): An output integer that specifies a portion of the board time.

            time_fractional_nanoseconds (int): An output integer that specifies a portion of the board time.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_seconds_ctype = _visatype.ViUInt32()  # case S220
        time_nanoseconds_ctype = _visatype.ViUInt32()  # case S220
        time_fractional_nanoseconds_ctype = _visatype.ViUInt16()  # case S220
        error_code = self._library.niSync_GetTime(vi_ctype, None if time_seconds_ctype is None else (ctypes.pointer(time_seconds_ctype)), None if time_nanoseconds_ctype is None else (ctypes.pointer(time_nanoseconds_ctype)), None if time_fractional_nanoseconds_ctype is None else (ctypes.pointer(time_fractional_nanoseconds_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(time_seconds_ctype.value), int(time_nanoseconds_ctype.value), int(time_fractional_nanoseconds_ctype.value)

    def get_time_reference_names(self):
        r'''get_time_reference_names

        TBD

        Returns:
            time_reference_names (str): The buffer in which the method returns the current value of the
                property. The buffer must be of type ViChar and have at least as many
                bytes as indicated in the Buffer Size parameter. If the current value of
                the property, including the terminating NUL byte, contains more bytes
                that you indicate in this parameter, the method copies Buffer Size - 1
                bytes into the buffer, places an ASCII NUL byte at the end of the
                buffer, and returns the buffer size you must pass to get the entire
                value. For example, if the value is "123456" and the Buffer Size is 4,
                the method places "123" into the buffer and returns 7. If you specify
                0 for the Buffer Size parameter, you can pass VI_NULL for this
                parameter. From the method panel window, you can use this control as
                follows. - If the property currently showing in the Property ID ring
                control has named constants as valid values, you can view a list of the
                constants by pressing on this control. Select a value by double-clicking
                on it or by selecting it and then pressing .

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        buffer_size_ctype = _visatype.ViUInt32()  # case S170
        time_reference_names_ctype = None  # case C050
        error_code = self._library.niSync_GetTimeReferenceNames(vi_ctype, buffer_size_ctype, time_reference_names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViUInt32(error_code)  # case S180
        time_reference_names_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niSync_GetTimeReferenceNames(vi_ctype, buffer_size_ctype, time_reference_names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return time_reference_names_ctype.value.decode(self._encoding)

    def get_velocity(self):
        r'''get_velocity

        This method returns the last calculated velocity of the onboard GPS
        receiver. The method returns east velocity, north velocity, and up
        velocity in meters per second. An external GPS antenna must be connected
        to receive valid data from this method, and the GPS receiver must be
        configured for Mobile Mode to receive nonzero velocity values.

        Returns:
            east_velocity (float): An input double pointer. The caller of this method must allocate a
                ViReal64 and pass the pointer in this argument. The method sets the
                ViReal64 value to the eastVelocity reported by the onboard GPS receiver.
                Negative values represent west velocity. Positive values represent east
                velocity.

            north_velocity (float): An input double pointer. The caller of this method must allocate a
                ViReal64 and pass the pointer in this argument. The method sets the
                ViReal64 value to the northVelocity reported by the onboard GPS
                receiver. Negative values represent south velocity. Positive values
                represent north velocity.

            up_velocity (float): An input double pointer. The caller of this method must allocate a
                ViReal64 and pass the pointer in this argument. The method sets the
                ViReal64 value to the upVelocity reported by the onboard GPS receiver.
                Negative values represent down velocity. Positive values represent up
                velocity.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        east_velocity_ctype = _visatype.ViReal64()  # case S220
        north_velocity_ctype = _visatype.ViReal64()  # case S220
        up_velocity_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niSync_GetVelocity(vi_ctype, None if east_velocity_ctype is None else (ctypes.pointer(east_velocity_ctype)), None if north_velocity_ctype is None else (ctypes.pointer(north_velocity_ctype)), None if up_velocity_ctype is None else (ctypes.pointer(up_velocity_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(east_velocity_ctype.value), float(north_velocity_ctype.value), float(up_velocity_ctype.value)

    def measure_frequency(self, source_terminal, duration):
        r'''measure_frequency

        This method measures the frequency of the signal at the specified
        terminal for a specified duration. The method returns the frequency,
        the calculated error, and the actual duration of the frequency
        measurement.

        Args:
            source_terminal (str): This input specifies the source terminal of the signal to measure. Valid
                Values: NISYNC_VAL_PFI0 (Default Value) NISYNC_VAL_PFI1
                NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4 NISYNC_VAL_PFI5
                NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2
                NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2
                NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5
                NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0
                NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3
                NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6
                NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9
                NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12
                NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15
                NISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR NISYNC_VAL_PXIEDSTARC0
                NISYNC_VAL_PXIEDSTARC1 NISYNC_VAL_PXIEDSTARC2
                NISYNC_VAL_PXIEDSTARC3 NISYNC_VAL_PXIEDSTARC4
                NISYNC_VAL_PXIEDSTARC5 NISYNC_VAL_PXIEDSTARC6
                NISYNC_VAL_PXIEDSTARC7 NISYNC_VAL_PXIEDSTARC8
                NISYNC_VAL_PXIEDSTARC9 NISYNC_VAL_PXIEDSTARC10
                NISYNC_VAL_PXIEDSTARC11 NISYNC_VAL_PXIEDSTARC12
                NISYNC_VAL_PXIEDSTARC13 NISYNC_VAL_PXIEDSTARC14
                NISYNC_VAL_PXIEDSTARC15 NISYNC_VAL_PXIEDSTARC16
                NISYNC_VAL_PXIEDSTARB NISYNC_VAL_OSCILLATOR NISYNC_VAL_CLKIN

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            duration (float): This input specifies the duration of the frequency measurement, in units
                of seconds. The duration should be a multiple of the PXI_Clk10 signal
                period, i.e. it should be specified in multiples of 100 ns. If the
                duration is not a multiple of the PXI_Clk10 period, it will be coerced
                to the closest multiple. Default Value: 0.00000100 seconds


        Returns:
            actual_duration (float): This parameter returns the actual duration, in units of seconds, used in
                the frequency measurement. The measurement duration will be a multiple
                of the PXI_Clk10 period, i.e. it is a multiple of 100ns.

            measured_frequency (float): This parameter returns the frequency measured at the PFI0 terminal, in
                units of Hz. The measurable frequency range is approximately 0.1 Hz to
                105 MHz.

            frequency_error (float): This parameter returns the error calculated for the frequency
                measurement. The formula used to calculate the error is: Measurement
                Error = 1 / (Actual Duration) where "Actual Duration" is the value
                returned in the Actual Duration parameter, i.e. the actual duration of
                the measurement.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_terminal_ctype = ctypes.create_string_buffer(source_terminal.encode(self._encoding))  # case C020
        duration_ctype = _visatype.ViReal64(duration)  # case S150
        actual_duration_ctype = _visatype.ViReal64()  # case S220
        measured_frequency_ctype = _visatype.ViReal64()  # case S220
        frequency_error_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niSync_MeasureFrequency(vi_ctype, source_terminal_ctype, duration_ctype, None if actual_duration_ctype is None else (ctypes.pointer(actual_duration_ctype)), None if measured_frequency_ctype is None else (ctypes.pointer(measured_frequency_ctype)), None if frequency_error_ctype is None else (ctypes.pointer(frequency_error_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(actual_duration_ctype.value), float(measured_frequency_ctype.value), float(frequency_error_ctype.value)

    def measure_frequency_ex(self, source_terminal, duration, decimation_count):
        r'''measure_frequency_ex

        This method measures the frequency of the signal at the specified
        terminal for a specified duration. The method returns the frequency,
        the calculated error, and the actual duration of the frequency
        measurement.

        Args:
            source_terminal (str): This input specifies the source terminal of the signal to measure. Valid
                Values: NISYNC_VAL_PFI0 (Default Value) NISYNC_VAL_PFI1
                NISYNC_VAL_PFI2 NISYNC_VAL_PFI3 NISYNC_VAL_PFI4 NISYNC_VAL_PFI5
                NISYNC_VAL_PFILVDS0 NISYNC_VAL_PFILVDS1 NISYNC_VAL_PFILVDS2
                NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1 NISYNC_VAL_PXITRIG2
                NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4 NISYNC_VAL_PXITRIG5
                NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7 NISYNC_VAL_PXISTAR0
                NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2 NISYNC_VAL_PXISTAR3
                NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5 NISYNC_VAL_PXISTAR6
                NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8 NISYNC_VAL_PXISTAR9
                NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11 NISYNC_VAL_PXISTAR12
                NISYNC_VAL_PXISTAR13 NISYNC_VAL_PXISTAR14 NISYNC_VAL_PXISTAR15
                NISYNC_VAL_PXISTAR16 NISYNC_VAL_PXISTAR NISYNC_VAL_PXIEDSTARC0
                NISYNC_VAL_PXIEDSTARC1 NISYNC_VAL_PXIEDSTARC2
                NISYNC_VAL_PXIEDSTARC3 NISYNC_VAL_PXIEDSTARC4
                NISYNC_VAL_PXIEDSTARC5 NISYNC_VAL_PXIEDSTARC6
                NISYNC_VAL_PXIEDSTARC7 NISYNC_VAL_PXIEDSTARC8
                NISYNC_VAL_PXIEDSTARC9 NISYNC_VAL_PXIEDSTARC10
                NISYNC_VAL_PXIEDSTARC11 NISYNC_VAL_PXIEDSTARC12
                NISYNC_VAL_PXIEDSTARC13 NISYNC_VAL_PXIEDSTARC14
                NISYNC_VAL_PXIEDSTARC15 NISYNC_VAL_PXIEDSTARC16
                NISYNC_VAL_PXIEDSTARB NISYNC_VAL_OSCILLATOR NISYNC_VAL_CLKIN

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            duration (float): This input specifies the duration of the frequency measurement, in units
                of seconds. The duration should be a multiple of the PXI_Clk10 signal
                period, i.e. it should be specified in multiples of 100 ns. If the
                duration is not a multiple of the PXI_Clk10 period, it will be coerced
                to the closest multiple. Default Value: 0.00000100 seconds

            decimation_count (int):


        Returns:
            actual_duration (float): This parameter returns the actual duration, in units of seconds, used in
                the frequency measurement. The measurement duration will be a multiple
                of the PXI_Clk10 period, i.e. it is a multiple of 100ns.

            measured_frequency (float): This parameter returns the frequency measured at the PFI0 terminal, in
                units of Hz. The measurable frequency range is approximately 0.1 Hz to
                105 MHz.

            frequency_error (float): This parameter returns the error calculated for the frequency
                measurement. The formula used to calculate the error is: Measurement
                Error = 1 / (Actual Duration) where "Actual Duration" is the value
                returned in the Actual Duration parameter, i.e. the actual duration of
                the measurement.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_terminal_ctype = ctypes.create_string_buffer(source_terminal.encode(self._encoding))  # case C020
        duration_ctype = _visatype.ViReal64(duration)  # case S150
        decimation_count_ctype = _visatype.ViUInt32(decimation_count)  # case S150
        actual_duration_ctype = _visatype.ViReal64()  # case S220
        measured_frequency_ctype = _visatype.ViReal64()  # case S220
        frequency_error_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niSync_MeasureFrequencyEx(vi_ctype, source_terminal_ctype, duration_ctype, decimation_count_ctype, None if actual_duration_ctype is None else (ctypes.pointer(actual_duration_ctype)), None if measured_frequency_ctype is None else (ctypes.pointer(measured_frequency_ctype)), None if frequency_error_ctype is None else (ctypes.pointer(frequency_error_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(actual_duration_ctype.value), float(measured_frequency_ctype.value), float(frequency_error_ctype.value)

    def persist_config(self):
        r'''persist_config

        This method will copy the sync configuration from volatile storage to
        permanent storage.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSync_PersistConfig(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def read_current_temperature(self):
        r'''read_current_temperature

        This method reads the current module temperature, in degrees celcius.
        Note: A calibration password is not required to use this method. It
        can be invoked with an instrument handle created with either
        init or InitExtCal.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Returns:
            temperature (float): This parameter returns the temperature, in degrees celcius, of the
                timing and synchronization module.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niSync_ReadCurrentTemperature(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def read_last_gps_timestamp(self):
        r'''read_last_gps_timestamp

        This method returns the last timestamp received of the GPS pulse per
        second. The read operation is a single-timestamp, nonblocking read. That
        is, the newest timestamp is returned. If no valid timestamp has ever
        been received, a value of zero is returned for the timestamp and the
        decoded time. A single timestamp can be read multiple times; only the
        reception of a subsequent timestamp updates the values returned. The
        method does not block waiting for a new timestamp to become available.
        Prior to calling ReadLastGPSTimestamp, it is expected that
        timestamping has been enabled by calling EnableGPSTimestamping.
        Note: The NI-Sync family of devices uses the TAI timescale. Note: You
        can combine the values returned in timestampSeconds,
        timestampNanoseconds, and timestampFractionalNanoseconds to get the
        board time the GPS pulse per second was received. You can combine the
        values returned in gpsSeconds, gpsNanoseconds, and
        gpsFractionalNanoseconds to get the time reported by the onboard GPS
        receiver.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Returns:
            time_seconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt32 and pass the pointer in this argument. The method sets the
                ViUInt32 value to the seconds field of when the timestamp occurred.

            time_nanoseconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt32 and pass the pointer in this argument. The method sets the
                ViUInt32 value to the nanoseconds field of when the timestamp occurred.

            time_fractional_nanoseconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt16 and pass the pointer in this argument. The method sets the
                ViUInt16 value to the fractional nanoseconds field of when the timestamp
                occurred.

            gps_seconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt32 and pass the pointer in this argument. The method sets the
                ViUInt32 value to the seconds field of time reported by the onboard GPS
                receiver.

            gps_nanoseconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt32 and pass the pointer in this argument. The method sets the
                ViUInt32 value to the nanoseconds field of the time reported by the
                onboard GPS receiver.

            gps_fractional_nanoseconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt16 and pass the pointer in this argument. The method sets the
                ViUInt16 value to the fractional nanoseconds field of the time reported
                by the onboard GPS receiver.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_seconds_ctype = _visatype.ViUInt32()  # case S220
        time_nanoseconds_ctype = _visatype.ViUInt32()  # case S220
        time_fractional_nanoseconds_ctype = _visatype.ViUInt16()  # case S220
        gps_seconds_ctype = _visatype.ViUInt32()  # case S220
        gps_nanoseconds_ctype = _visatype.ViUInt32()  # case S220
        gps_fractional_nanoseconds_ctype = _visatype.ViUInt16()  # case S220
        error_code = self._library.niSync_ReadLastGpsTimestamp(vi_ctype, None if time_seconds_ctype is None else (ctypes.pointer(time_seconds_ctype)), None if time_nanoseconds_ctype is None else (ctypes.pointer(time_nanoseconds_ctype)), None if time_fractional_nanoseconds_ctype is None else (ctypes.pointer(time_fractional_nanoseconds_ctype)), None if gps_seconds_ctype is None else (ctypes.pointer(gps_seconds_ctype)), None if gps_nanoseconds_ctype is None else (ctypes.pointer(gps_nanoseconds_ctype)), None if gps_fractional_nanoseconds_ctype is None else (ctypes.pointer(gps_fractional_nanoseconds_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(time_seconds_ctype.value), int(time_nanoseconds_ctype.value), int(time_fractional_nanoseconds_ctype.value), int(gps_seconds_ctype.value), int(gps_nanoseconds_ctype.value), int(gps_fractional_nanoseconds_ctype.value)

    def read_last_irig_timestamp(self):
        r'''read_last_irig_timestamp

        This method returns the last IRIG timestamp received. The read
        operation is a single-timestamp, nonblocking read. That is, the newest
        timestamp is returned. If no valid timestamp has ever been received, a
        value of zero is returned for the timestamp and the decoded time. A
        single timestamp can be read multiple times; only the reception of a
        subsequent timestamp will update the values returned. The method does
        not block waiting for a new timestamp to become available. Prior to
        calling ReadLastIRIGTimestamp, it is expected that timestamping
        has been enabled by calling EnableIRIGTimestamping. Note: The
        NI-Sync family of devices uses the TAI timescale. Note: You can combine
        the values returned in timestampSeconds, timestampNanoseconds, and
        timestampFractionalNanoseconds to get the board time the IRIG message
        was received. You can combine the values returned in irigbSeconds,
        irigbNanoseconds, and irigbFractionalNanoseconds to get the time
        reported in the IRIG message.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Returns:
            time_seconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt32 and pass the pointer in this argument. The method sets the
                ViUInt32 value to the seconds field of when the timestamp occurred.

            time_nanoseconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt32 and pass the pointer in this argument. The method sets the
                ViUInt32 value to the nanoseconds field of when the timestamp occurred.

            time_fractional_nanoseconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt16 and pass the pointer in this argument. The method sets the
                ViUInt16 value to the fractional nanoseconds field of when the timestamp
                occurred.

            irig_seconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt32 and pass the pointer in this argument. The method sets the
                ViUInt32 value to the seconds field of time reported in the IRIG
                message.

            irig_nanoseconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt32 and pass the pointer in this argument. The method sets the
                ViUInt32 value to the nanoseconds field of the time reported in the IRIG
                message.

            irig_fractional_nanoseconds (int): An input integer pointer. The caller of this method must allocate a
                ViUInt16 and pass the pointer in this argument. The method sets the
                ViUInt16 value to the fractional nanoseconds field of the time reported
                in the IRIG message.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_seconds_ctype = _visatype.ViUInt32()  # case S220
        time_nanoseconds_ctype = _visatype.ViUInt32()  # case S220
        time_fractional_nanoseconds_ctype = _visatype.ViUInt16()  # case S220
        irig_seconds_ctype = _visatype.ViUInt32()  # case S220
        irig_nanoseconds_ctype = _visatype.ViUInt32()  # case S220
        irig_fractional_nanoseconds_ctype = _visatype.ViUInt16()  # case S220
        error_code = self._library.niSync_ReadLastIrigTimestamp(vi_ctype, None if time_seconds_ctype is None else (ctypes.pointer(time_seconds_ctype)), None if time_nanoseconds_ctype is None else (ctypes.pointer(time_nanoseconds_ctype)), None if time_fractional_nanoseconds_ctype is None else (ctypes.pointer(time_fractional_nanoseconds_ctype)), None if irig_seconds_ctype is None else (ctypes.pointer(irig_seconds_ctype)), None if irig_nanoseconds_ctype is None else (ctypes.pointer(irig_nanoseconds_ctype)), None if irig_fractional_nanoseconds_ctype is None else (ctypes.pointer(irig_fractional_nanoseconds_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(time_seconds_ctype.value), int(time_nanoseconds_ctype.value), int(time_fractional_nanoseconds_ctype.value), int(irig_seconds_ctype.value), int(irig_nanoseconds_ctype.value), int(irig_fractional_nanoseconds_ctype.value)

    def read_multiple_trigger_time_stamp(self, terminal, time_stamps_to_read, timeout):
        r'''read_multiple_trigger_time_stamp

        This method reads trigger time stamps from the internal software
        buffer for the specified terminal. The read operation is a destructive,
        blocking read. That is, the oldest unread time stamp associated with the
        specified terminal is returned. When a time stamp is read, it is removed
        from the buffer. The method does not return until the time stamps
        requested are available to be read, or the specified timeout elapses. If
        the internal software buffer associated with the specified terminal is
        full, time stamp operations for that terminal are suspended. Also, an
        error specifying that the internal software buffer overflowed is
        returned when the ReadMultipleTriggertimestamp method is
        invoked. If the hardware time stamp buffer is full, all trigger time
        stamp operations are suspended. Also, an error specifying that the
        hardware time stamp buffer overflowed is returned when the
        ReadMultipleTriggertimestamp method is invoked. That is, the
        ReadMultipleTriggertimestamp method continues to return
        previously generated time stamps, despite the overflow condition, until
        no time stamps are available. To clear this error condition, the
        DisabletimestampTrigger method must be invoked. Note that
        NI-Sync supports only the time range between 1 January 1970 and 1
        January 2100. Therefore, if the supported time range ends before a time
        stamp is captured, an error is returned. Note: If timestampsToRead is
        not equal to timestampsRead, the data held in the output arrays from
        index timestampsRead to the end of the arrays is uninitialized, and
        should be considered invalid.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Args:
            terminal (str): An input string that specifies the terminal containing the digital
                signal that is the trigger whose oldest unread time stamp will be read.

            time_stamps_to_read (int): An input integer specifying the number of time stamps to read. If the
                number of time stamps is not available before the timeout elapses, the
                number read before the timeout occurred is returned.

            timeout (float): An input floating-point number that specifies the number of seconds to
                wait for a time stamp to be generated before returning a timeout error.


        Returns:
            time_seconds (int): An input pointer to an array of ViUInt32 values. The caller of this
                method must allocate an array of ViUInt32s of size timestampsToRead
                and pass the pointer to the array in this argument. The method sets
                the values of the ViUInt32s to the seconds field of when the time stamp
                occurred. After the method returns, index 0 holds the earliest
                occurring seconds value, and the value returned in timestampsRead, minus
                one, is the index in which the latest occurring seconds value is stored.

            time_nanoseconds (int): An input pointer to an array of ViUInt32 values. The caller of this
                method must allocate an array of ViUInt32s of size timestampsToRead
                and pass the pointer to the array in this argument. The method sets
                the values of the ViUInt32s to the nanoseconds field of when the time
                stamp occurred. After the method returns, index 0 holds the earliest
                occurring nanoseconds value, and the value returned in timestampsRead,
                minus one, is the index in which the latest occurring nanoseconds value
                is stored.

            time_fractional_nanoseconds (int): An input pointer to an array of ViUInt16 values. The caller of this
                method must allocate an array of ViUInt16s of size timestampsToRead
                and pass the pointer to the array in this argument. The method sets
                the values of the ViUInt16s to the fractional nanoseconds field of when
                the time stamp occurred. After the method returns, index 0 holds the
                earliest occurring fractional nanoseconds value, and the value returned
                in timestampsRead, minus one, is the index in which the latest occurring
                fractional nanoseconds value is stored.

            detected_edge_buffer (int): An input pointer to an array of ViInt32s. The caller of this method
                must allocate an array of ViUInt32s of size timestampsToRead and pass
                the pointer to the array in this argument. After the method returns,
                index 0 holds the earliest occurring detectedEdge value, and the value
                returned in timestampsRead, minus one, is the index in which the latest
                occurring detectedEdge value is stored. Each detectedEdge is an integer
                enumeration that specifies the detected trigger condition. Valid Values:
                NISYNC_VAL_EDGE_RISING NISYNC_VAL_EDGE_FALLING

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            time_stamps_read (int): An input pointer to a ViUInt32. The caller of this method must
                allocate a ViUInt32 and pass the pointer to the array in this argument.
                When the method returns, the value at this pointer is set to the
                number of actual time stamps read. This value may be different than
                timestampsToRead if a timeout or other error occurs while reading time
                stamps.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        terminal_ctype = ctypes.create_string_buffer(terminal.encode(self._encoding))  # case C020
        time_stamps_to_read_ctype = _visatype.ViUInt32(time_stamps_to_read)  # case S150
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        time_seconds_ctype = _visatype.ViUInt32()  # case S220
        time_nanoseconds_ctype = _visatype.ViUInt32()  # case S220
        time_fractional_nanoseconds_ctype = _visatype.ViUInt16()  # case S220
        detected_edge_buffer_ctype = _visatype.ViInt32()  # case S220
        time_stamps_read_ctype = _visatype.ViUInt32()  # case S220
        error_code = self._library.niSync_ReadMultipleTriggerTimeStamp(vi_ctype, terminal_ctype, time_stamps_to_read_ctype, timeout_ctype, None if time_seconds_ctype is None else (ctypes.pointer(time_seconds_ctype)), None if time_nanoseconds_ctype is None else (ctypes.pointer(time_nanoseconds_ctype)), None if time_fractional_nanoseconds_ctype is None else (ctypes.pointer(time_fractional_nanoseconds_ctype)), None if detected_edge_buffer_ctype is None else (ctypes.pointer(detected_edge_buffer_ctype)), None if time_stamps_read_ctype is None else (ctypes.pointer(time_stamps_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(time_seconds_ctype.value), int(time_nanoseconds_ctype.value), int(time_fractional_nanoseconds_ctype.value), int(detected_edge_buffer_ctype.value), int(time_stamps_read_ctype.value)

    def read_trigger_time_stamp(self, terminal, timeout):
        r'''read_trigger_time_stamp

        This method reads a trigger time stamp from the internal software
        buffer for the specified terminal. The read operation is a
        single-time-stamp, destructive, blocking read. That is, the oldest
        unread time stamp associated with the specified terminal is returned.
        When a time stamp is read, it is removed from the buffer. The method
        does not return until a time stamp is available to be read or the
        specified timeout elapses. If the internal software buffer associated
        with the specified terminal is full, time stamp operations for that
        terminal are suspended and an error, specifying that the internal
        software buffer overflowed, is returned when the
        read_trigger_time_stamp method is invoked. If the hardware
        time-stamp buffer is full, all trigger time stamp operations are
        suspended and an error, specifying that the hardware time-stamp buffer
        overflowed, is returned when the read_trigger_time_stamp method
        is invoked. That is, the read_trigger_time_stamp method continues
        to return previously generated time stamps, despite the overflow
        condition, until no time stamps are available. To clear this error
        condition, the disable_time_stamp_trigger method must be invoked.
        Note: NI-Sync supports only the time range between 1 January 1970 and 1
        January 2100. Therefore, if the supported time range ends before a time
        stamp is captured, an error is returned. Note: The NI-Sync family of
        devices uses the TAI timescale.

        Args:
            terminal (str): An input string enumeration that specifies the terminal containing the
                digital signal that is the trigger whose oldest unread time stamp will
                be read. Valid Values: NISYNC_VAL_PFI0 NISYNC_VAL_PFI1
                NISYNC_VAL_PFI2 NISYNC_VAL_PXITRIG0 NISYNC_VAL_PXITRIG1
                NISYNC_VAL_PXITRIG2 NISYNC_VAL_PXITRIG3 NISYNC_VAL_PXITRIG4
                NISYNC_VAL_PXITRIG5 NISYNC_VAL_PXITRIG6 NISYNC_VAL_PXITRIG7
                NISYNC_VAL_PXISTAR0 NISYNC_VAL_PXISTAR1 NISYNC_VAL_PXISTAR2
                NISYNC_VAL_PXISTAR3 NISYNC_VAL_PXISTAR4 NISYNC_VAL_PXISTAR5
                NISYNC_VAL_PXISTAR6 NISYNC_VAL_PXISTAR7 NISYNC_VAL_PXISTAR8
                NISYNC_VAL_PXISTAR9 NISYNC_VAL_PXISTAR10 NISYNC_VAL_PXISTAR11
                NISYNC_VAL_PXISTAR12

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            timeout (float): An input floating-point number that specifies the number of seconds to
                wait for a time stamp to be generated before returning a timeout error.
                Default Value: 10 seconds


        Returns:
            time_seconds (int): An output integer that specifies a portion of the board time when the
                trigger associated with the specified terminal was detected.

            time_nanoseconds (int): An output integer that specifies a portion of the board time when the
                trigger associated with the specified terminal was detected.

            time_fractional_nanoseconds (int): An output integer that specifies a portion of the board time when the
                trigger associated with the specified terminal was detected.

            detected_edge (int): An output integer enumeration that specifies the detected trigger
                condition. Valid Values: NISYNC_VAL_EDGE_RISING
                NISYNC_VAL_EDGE_FALLING

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        terminal_ctype = ctypes.create_string_buffer(terminal.encode(self._encoding))  # case C020
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        time_seconds_ctype = _visatype.ViUInt32()  # case S220
        time_nanoseconds_ctype = _visatype.ViUInt32()  # case S220
        time_fractional_nanoseconds_ctype = _visatype.ViUInt16()  # case S220
        detected_edge_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niSync_ReadTriggerTimeStamp(vi_ctype, terminal_ctype, timeout_ctype, None if time_seconds_ctype is None else (ctypes.pointer(time_seconds_ctype)), None if time_nanoseconds_ctype is None else (ctypes.pointer(time_nanoseconds_ctype)), None if time_fractional_nanoseconds_ctype is None else (ctypes.pointer(time_fractional_nanoseconds_ctype)), None if detected_edge_ctype is None else (ctypes.pointer(detected_edge_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(time_seconds_ctype.value), int(time_nanoseconds_ctype.value), int(time_fractional_nanoseconds_ctype.value), int(detected_edge_ctype.value)

    def reset_frequency(self):
        r'''reset_frequency

        This method resets the internal frequency at which the board time
        increments to the default value.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSync_ResetFrequency(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger(self, source_terminal):
        r'''send_software_trigger

        This method sends a pulse on the global software trigger terminal. The
        global software trigger terminal must be connected to a destination
        terminal for this operation to have any effect.

        Args:
            source_terminal (str): This input specifies the source software trigger terminal to send. When
                this method is invoked, the global software trigger will be sent
                simultaneously to all destination terminals that it is connected to.
                Valid Values: NISYNC_VAL_SWTRIG_GLOBAL (Default Value)

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        source_terminal_ctype = ctypes.create_string_buffer(source_terminal.encode(self._encoding))  # case C020
        error_code = self._library.niSync_SendSoftwareTrigger(vi_ctype, source_terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, active_item, attribute_id, attribute_value):
        r'''set_attribute_vi_boolean

        This method sets the value of a ViBoolean property.

        Args:
            active_item (str): Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

            attribute_id (int): This parameter specifies the ID of the property you wish to set.

            attribute_value (bool): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing .

                Note:
                Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        active_item_ctype = ctypes.create_string_buffer(active_item.encode(self._encoding))  # case C020
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niSync_SetAttributeViBoolean(vi_ctype, active_item_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, active_item, attribute_id, attribute_value):
        r'''set_attribute_vi_int32

        This method sets the value of a ViInt32 property.

        Args:
            active_item (str): Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

            attribute_id (int): This parameter specifies the ID of the property you wish to set.

            attribute_value (int): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing .

                Note:
                Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        active_item_ctype = ctypes.create_string_buffer(active_item.encode(self._encoding))  # case C020
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niSync_SetAttributeViInt32(vi_ctype, active_item_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, active_item, attribute_id, attribute_value):
        r'''set_attribute_vi_real64

        This method sets the value of a ViReal64 property.

        Args:
            active_item (str): Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

            attribute_id (int): This parameter specifies the ID of the property you wish to set.

            attribute_value (float): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing .

                Note:
                Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        active_item_ctype = ctypes.create_string_buffer(active_item.encode(self._encoding))  # case C020
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niSync_SetAttributeViReal64(vi_ctype, active_item_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, active_item, attribute_id, attribute_value):
        r'''set_attribute_vi_string

        This method sets the value of a ViString property. This is a
        low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases: - State caching is disabled for
        the entire session or for the particular property. - State caching is
        enabled and the currently cached value is invalid or is different than
        the value you specify. This instrument driver contains high-level
        methods that set most of the instrument properties. It is best to use
        the high-level driver methods as much as possible. They handle order
        dependencies and multithread locking for you. In addition, they perform
        status checking only after setting all of the properties. In contrast,
        when you set multiple properties using the SetAttribute methods, the
        methods check the instrument status after each call. Also, when state
        caching is enabled, the high-level methods that configure multiple
        properties perform instrument I/O only for the properties whose value
        you change. Thus, you can safely call the high-level methods without
        the penalty of redundant instrument I/O.

        Args:
            active_item (str): Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

            attribute_id (int): This parameter specifies the ID of the property you wish to set.

            attribute_value (str): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing .

                Note:
                Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        active_item_ctype = ctypes.create_string_buffer(active_item.encode(self._encoding))  # case C020
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niSync_SetAttributeViString(vi_ctype, active_item_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_time(self, time_source, time_seconds, time_nanoseconds, time_fractional_nanoseconds):
        r'''set_time

        This method sets the absolute board time to the time specified. This
        method leaves the internal frequency at which the board time
        increments unchanged. Note: The NI-Sync family of devices uses the TAI
        timescale.

        Args:
            time_source (int): An input integer enumeration that specifies the time source for the
                board time. Valid Values: NISYNC_VAL_INIT_TIME_SRC_SYSTEM_CLK
                (Default) NISYNC_VAL_INIT_TIME_SRC_MANUAL

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            time_seconds (int): An integer that specifies the seconds portion of the time to which the
                board time will be set. Note that NI-Sync supports setting the initial
                time between 0 hours on 1 January 1970 and 0 hours on 1 January 2100.
                This parameter is ignored unless the timeSource parameter is set to
                NISYNC_VAL_INIT_TIME_SRC_MANUAL.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            time_nanoseconds (int): An integer that specifies the nanoseconds portion of the time to which
                the board time will be set. Note that NI-Sync supports setting the
                initial time between 0 hours on 1 January 1970 and 0 hours on 1 January
                2100. This parameter is ignored unless the timeSource parameter is set
                to NISYNC_VAL_INIT_TIME_SRC_MANUAL.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            time_fractional_nanoseconds (int): An integer that specifies the fractional nanoseconds portion of the time
                to which the board time will be set. Note that NI-Sync supports setting
                the initial time between 0 hours on 1 January 1970 and 0 hours on 1
                January 2100. This parameter is ignored unless the timeSource parameter
                is set to NISYNC_VAL_INIT_TIME_SRC_MANUAL.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        time_source_ctype = _visatype.ViInt32(time_source)  # case S150
        time_seconds_ctype = _visatype.ViUInt32(time_seconds)  # case S150
        time_nanoseconds_ctype = _visatype.ViUInt32(time_nanoseconds)  # case S150
        time_fractional_nanoseconds_ctype = _visatype.ViUInt16(time_fractional_nanoseconds)  # case S150
        error_code = self._library.niSync_SetTime(vi_ctype, time_source_ctype, time_seconds_ctype, time_nanoseconds_ctype, time_fractional_nanoseconds_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_time_reference1588_ordinary_clock(self):
        r'''set_time_reference1588_ordinary_clock

        This method sets the time reference of the device associated with the
        specified instrument handle. The time reference set is used to update
        the value and frequency of the board time such that the board time
        reflects the time reference's time as closely as possible. The board
        time is then used for tasks such as creating future time events, clocks,
        and timestamping triggers. This method is a nonblocking call that
        returns immediately regardless of the state of the time reference set.
        Setting the time reference is a systemwide (per device) configuration
        that persists after the session exits. The time reference is not
        reservable; the last call to set the time reference takes precedence. If
        the time reference set is not providing valid time information, the
        board time free runs from the last known time at the last frequency that
        was applied. Note: When a device's board time and the configured time
        reference's time vary by more than 1 ms, a macro phase adjustment may be
        necessary. A macro phase adjustment is when the board time is adjusted
        by a significant amount and, therefore, the board time no longer
        atomically increments. This should not occur on a well designed and
        stable time reference. If this occurs, future time events, clocks, and
        time stamps may be affected. If the board time is set forward, future
        time events and clock transitions that were missed occur immediately. If
        the board time is set backward, future time events and clock transitions
        are delayed. Note: An alternative to calling this method is to
        configure the default configured Time Reference through Measurement &
        Automation Explorer. The state configured is then reapplied at every
        restart. Note: Closing the session that calls this VI does not alter the
        value of the configured Time Reference. Note: The NI-Sync family of
        devices uses the TAI timescale. This method sets the Time Reference of
        the device to 1588.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSync_SetTimeReference1588OrdinaryClock(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_time_reference_free_running(self):
        r'''set_time_reference_free_running

        This method sets the time reference of the device associated with the
        specified instrument handle. The time reference set is used to update
        the value and frequency of the board time such that the board time
        reflects the time reference's time as closely as possible. The board
        time is then used for tasks such as creating future time events, clocks,
        and timestamping triggers. This method is a nonblocking call that
        returns immediately regardless of the state of the time reference set.
        Setting the time reference is a systemwide (per device) configuration
        that persists after the session exits. The time reference is not
        reservable; the last call to set the time reference takes precedence. If
        the time reference set is not providing valid time information, the
        board time free runs from the last known time at the last frequency that
        was applied. Note: When a device's board time and the configured time
        reference's time vary by more than 1 ms, a macro phase adjustment may be
        necessary. A macro phase adjustment is when the board time is adjusted
        by a significant amount and, therefore, the board time no longer
        atomically increments. This should not occur on a well designed and
        stable time reference. If this occurs, future time events, clocks, and
        time stamps may be affected. If the board time is set forward, future
        time events and clock transitions that were missed occur immediately. If
        the board time is set backward, future time events and clock transitions
        are delayed. Note: An alternative to calling this method is to
        configure the default configured Time Reference through Measurement &
        Automation Explorer. The state configured is then reapplied at every
        restart. Note: Closing the session that calls this VI does not alter the
        value of the configured Time Reference. Note: The NI-Sync family of
        devices uses the TAI timescale. This method sets the Time Reference of
        the device to free running. The board time is guaranteed to atomically
        increment at the last calculated frequency. No external stimuli will
        alter the board time or frequency.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSync_SetTimeReferenceFreeRunning(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_time_reference_gps(self):
        r'''set_time_reference_gps

        This method sets the time reference of the device associated with the
        specified instrument handle. The time reference set is used to update
        the value and frequency of the board time such that the board time
        reflects the time reference's time as closely as possible. The board
        time is then used for tasks such as creating future time events, clocks,
        and timestamping triggers. This method is a nonblocking call that
        returns immediately regardless of the state of the time reference set.
        Setting the time reference is a systemwide (per device) configuration
        that persists after the session exits. The time reference is not
        reservable; the last call to set the time reference takes precedence. If
        the time reference set is not providing valid time information, the
        board time free runs from the last known time at the last frequency that
        was applied. Note: When a device's board time and the configured time
        reference's time vary by more than 1 ms, a macro phase adjustment may be
        necessary. A macro phase adjustment is when the board time is adjusted
        by a significant amount and, therefore, the board time no longer
        atomically increments. This should not occur on a well designed and
        stable time reference. If this occurs, future time events, clocks, and
        time stamps may be affected. If the board time is set forward, future
        time events and clock transitions that were missed occur immediately. If
        the board time is set backward, future time events and clock transitions
        are delayed. Note: An alternative to calling this method is to
        configure the default configured Time Reference through Measurement &
        Automation Explorer. The state configured is then reapplied at every
        restart. Note: Closing the session that calls this VI does not alter the
        value of the configured Time Reference. Note: The NI-Sync family of
        devices uses the TAI timescale. This method sets the Time Reference of
        the device to GPS.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSync_SetTimeReferenceGps(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_time_reference_irig(self, irig_type, terminal_name):
        r'''set_time_reference_irig

        This method sets the time reference of the device associated with the
        specified instrument handle. The time reference set is used to update
        the value and frequency of the board time such that the board time
        reflects the time reference's time as closely as possible. The board
        time is then used for tasks such as creating future time events, clocks,
        and timestamping triggers. This method is a nonblocking call that
        returns immediately regardless of the state of the time reference set.
        Setting the time reference is a systemwide (per device) configuration
        that persists after the session exits. The time reference is not
        reservable; the last call to set the time reference takes precedence. If
        the time reference set is not providing valid time information, the
        board time free runs from the last known time at the last frequency that
        was applied. Note: When a device's board time and the configured time
        reference's time vary by more than 1 ms, a macro phase adjustment may be
        necessary. A macro phase adjustment is when the board time is adjusted
        by a significant amount and, therefore, the board time no longer
        atomically increments. This should not occur on a well designed and
        stable time reference. If this occurs, future time events, clocks, and
        time stamps may be affected. If the board time is set forward, future
        time events and clock transitions that were missed occur immediately. If
        the board time is set backward, future time events and clock transitions
        are delayed. Note: An alternative to calling this method is to
        configure the default configured Time Reference through Measurement &
        Automation Explorer. The state configured is then reapplied every
        restart. Note: Closing the session that calls this VI does not alter the
        value of the configured Time Reference. Note: The NI-Sync family of
        devices uses the TAI timescale. This method sets the Time Reference of
        the device to IRIG.

        Args:
            irig_type (int): An input integer enumeration of the IRIG input being supplied. Valid
                Values: NISYNC_VAL_IRIG_TYPE_IRIGB_DC
                NISYNC_VAL_IRIG_TYPE_IRIGB_AM (Default)

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            terminal_name (str): An input string that specifies the terminal to which the IRIG input is
                connected.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        irig_type_ctype = _visatype.ViInt32(irig_type)  # case S150
        terminal_name_ctype = ctypes.create_string_buffer(terminal_name.encode(self._encoding))  # case C020
        error_code = self._library.niSync_SetTimeReferenceIrig(vi_ctype, irig_type_ctype, terminal_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_time_reference_pps(self, terminal_name, use_manual_time, initial_time_seconds, initial_nanoseconds, initial_fractional_nanoseconds):
        r'''set_time_reference_pps

        This method sets the time reference of the device associated with the
        specified instrument handle. The time reference set is used to update
        the value and frequency of the board time such that the board time
        reflects the time reference's time as closely as possible. The board
        time is then used for tasks such as creating future time events, clocks,
        and timestamping triggers. This method is a nonblocking call that
        returns immediately regardless of the state of the time reference set.
        Setting the time reference is a systemwide (per device) configuration
        that persists after the session exits. The time reference is not
        reservable; the last call to set the time reference takes precedence. If
        the time reference set is not providing valid time information, the
        board time free runs from the last known time at the last frequency that
        was applied. Note: When a device's board time and the configured time
        reference's time vary by more than 1 ms, a macro phase adjustment may be
        necessary. A macro phase adjustment is when the board time is adjusted
        by a significant amount and, therefore, the board time no longer
        atomically increments. This should not occur on a well designed and
        stable time reference. If this occurs, future time events, clocks, and
        time stamps may be affected. If the board time is set forward, future
        time events and clock transitions that were missed occur immediately. If
        the board time is set backward, future time events and clock transitions
        are delayed. Note: An alternative to calling this method is to
        configure the default configured Time Reference through Measurement &
        Automation Explorer. The state configured is then reapplied at every
        restart. Note: Closing the session that calls this VI does not alter the
        value of the configured Time Reference. Note: The NI-Sync family of
        devices uses the TAI timescale. This method sets the Time Reference of
        the device to PPS (pulse per second).

        Args:
            terminal_name (str): An input string that specifies the terminal to which the PPS is
                supplied.

            use_manual_time (bool): An input Boolean that specifies whether to use the user-supplied time or
                the OS system time to represent the time at which the first pulse is
                received. If false, the OS system time is read at the time the first
                pulse is received, and it is used to set the board time. If true, the
                user-specified initial time is used to set the board time when the first
                pulse is recevied. Every subsequent pulse is interpreted to be received
                one second later, and the board time adjusted accordingly.

            initial_time_seconds (int): An input integer that specifies the seconds field of the time to apply
                as the board time when the first pulse is received if useManualTime was
                set to True.

            initial_nanoseconds (int): An input integer that specifies the nanoseconds field of the time to
                apply as the board time when the first pulse is received if
                useManualTime was set to True.

            initial_fractional_nanoseconds (int): An input integer that specifies the fractional nanoseconds field of the
                time to apply as the board time when the first pulse is received if
                useManualTime was set to True.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        terminal_name_ctype = ctypes.create_string_buffer(terminal_name.encode(self._encoding))  # case C020
        use_manual_time_ctype = _visatype.ViBoolean(use_manual_time)  # case S150
        initial_time_seconds_ctype = _visatype.ViUInt32(initial_time_seconds)  # case S150
        initial_nanoseconds_ctype = _visatype.ViUInt32(initial_nanoseconds)  # case S150
        initial_fractional_nanoseconds_ctype = _visatype.ViUInt16(initial_fractional_nanoseconds)  # case S150
        error_code = self._library.niSync_SetTimeReferencePps(vi_ctype, terminal_name_ctype, use_manual_time_ctype, initial_time_seconds_ctype, initial_nanoseconds_ctype, initial_fractional_nanoseconds_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def start1588(self):
        r'''start1588

        This method starts participation in 1588. Note that this method
        returns as soon as participation begins and does not wait until the 1588
        clock has reached a steady state. For clocks, future time events, and
        triggered time stamps to be synchronized with respect to other devices
        participating in 1588, this method should be invoked, 1588 should be
        set as the Time Reference, and the 1588 clock should reach a steady
        state before any of these operations are invoked. Note that you do not
        need to invoke this method in the same session as these other
        operations, but rather you can invoke it in a separate session
        associated with the same device. Note: An alternative to calling this
        method is to configure the 1588 default state through Measurement &
        Automation Explorer. The state configured is then reapplied at every
        restart. Note: Closing the session that calls this method does not
        stop 1588. Stop 1588 must be called explicitly from any session to stop
        1588 participation. Note: If the clock participating in 1588 enters the
        faulty state, and 1588 is configured as the Time Reference, future time
        events, clocks, and time stamps are no longer synchronized with other
        1588 devices participating in PTP. This should not occur on a well
        designed and stable network. You can check for this condition by
        monitoring the 1588 clock state property.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSync_Start1588(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def stop1588(self):
        r'''stop1588

        This method stops participation in 1588.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSync_Stop1588(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        r'''_close

        This method performs the following operations: - Closes the NI-Sync
        I/O session. - Destroys the NI-Sync session and all of its properties. -
        Deallocates any memory resources the NI-Sync driver uses. Note: If the
        session is locked, you must unlock the session before calling
        _close. Note: After calling _close, you cannot use the
        instrument driver again until you call init. Note: If any clocks
        have been created with the create_clock method in the context
        of this session and have not been cleared, this method clears them. If
        any future time events have been created with the
        create_future_time_event method in the context of this session
        and have not occurred or been cleared, this method clears them. If any
        time stamp triggers have been enabled with the
        enable_time_stamp_trigger method in the context of this session
        and have not been disabled, this method clears them.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSync_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):
        r'''error_message

        This method converts a status code returned by an NI-Sync driver
        method into a user-readable string.

        Args:
            error_code (int): Pass the Status parameter that is returned from any of the instrument
                driver methods. Default Value: 0 (VI_SUCCESS)


        Returns:
            error_message (str): Returns the user-readable message string that corresponds to the status
                code you specify. You must pass a ViChar array at least 256 bytes in
                size.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niSync_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return error_message_ctype.value.decode(self._encoding)

    def init(self, resource_name, id_query, reset_device):
        r'''init

        This method performs the following initialization actions: - Creates a
        new NI-Sync instrument driver session. - Opens a session to the
        specified device using the interface and address you specify for the
        Resource Name parameter. - If the ID Query parameter is set to True,
        this method queries the instrument ID and checks that it is valid for
        this instrument driver. - If the Reset parameter is set to True,
        this method resets the module to a known state. Returns a ViSession
        handle that you use to identify the instrument in all subsequent
        instrument driver method calls. - Returns an instrument handle that
        you use to identify the instrument in all subsequent instrument driver
        method calls.

        Args:
            resource_name (str): Resource name of the switch module to initialize. The resource name is
                assigned in Measurement & Automation Explorer (MAX). Syntax PXI[bus
                number]::device number NI-DAQmx name Optional fields are shown in square
                brackets ([]).

                Note:
                VISA aliases are also valid for the resource name.
                Example resource names: Resource Name Description Dev1 DAQmx name
                PXI1Slot5 DAQmx name PXI0::15::INSTR PXI bus 0, device number 15
                PXI::15::INSTR PXI bus 0, device number 15 PXI4::9::INSTR PXI bus 4,
                device number 9

            id_query (bool): This parameter is ignored. Because NI-Sync supports multiple timing and
                synchronization modules, it always queries the device to determine which
                device is installed. Valid Values: True - Query the device (Default
                Value) False - Do not query the device

            reset_device (bool): Specify whether you want the to reset the timing and synchronization
                module during the initialization procedure. Valid Range: True (1) -
                Reset Device False (0) - Don't Reset (Default Value)


        Returns:
            vi (int): Returns a ViSession handle that you use to identify the instrument in
                all subsequent instrument driver method calls.

                Note:
                Although you can
                create more than one NI-Sync session for the same resource, it is best
                not to do so. A better approach is to use the same NI-Sync session in
                multiple execution threads. You can use VISA methods viLock and
                viUnlock to protect sections of code that require exclusive access to
                the resource.

        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niSync_init(resource_name_ctype, id_query_ctype, reset_device_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def reset(self):
        r'''reset

        This method resets the module to a known state. Resetting the module
        performs the following operations: - All terminal connections are
        disconnected. - The DDS frequency is set to 0 Hz if DDS is supported. -
        All PFI front panel terminals are set to 50 input impedance. - The front
        (PFI) and rear (PXI backplane) zone synchronization clock sources are
        set to PXI_Clk10. Resetting the module performs the following
        operations on a timing and synchronization module capable of 1588. - Any
        participation in PTP is stopped. - The 1588 clock is reset to the
        current system time. - All clocks and future time events are cleared. -
        All time stamp triggers are disabled.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niSync_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def revision_query(self):
        r'''revision_query

        This method returns the revision numbers of the NI-Sync driver and the
        firmware of the module.

        Returns:
            instrument_driver_revision (str): Returns the NI-Sync software revision numbers in the form of a string.

                Note: You must pass a ViChar array at least 256 bytes in size.

            firmware_revision (str): Returns the module firmware revision numbers in the form of a string.

                Note: You must pass a ViChar array at least 256 bytes in size.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        instrument_driver_revision_ctype = (_visatype.ViChar * 256)()  # case C070
        firmware_revision_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niSync_revision_query(vi_ctype, instrument_driver_revision_ctype, firmware_revision_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return instrument_driver_revision_ctype.value.decode(self._encoding), firmware_revision_ctype.value.decode(self._encoding)

    def self_test(self):
        r'''self_test

        This method runs the module's self test routine and returns the test
        result(s). Note: Currently, this operation does nothing.

        Returns:
            self_test_result (int): This control contains the value returned from the instrument self test.
                Zero means success. For any other code, see the device's operator's
                manual. Self-Test Code Description
                --------------------------------------- 0 Passed self test 1 Self test
                failed

            self_test_message (str): Returns the self-test response string from the instrument. See the
                device's operation manual for an explanation of the string's contents.

                Note: You must pass a ViChar array at least 256 bytes in size.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niSync_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



