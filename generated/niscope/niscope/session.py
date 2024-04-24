# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import niscope._attributes as _attributes
import niscope._converters as _converters
import niscope._library_interpreter as _library_interpreter
import niscope.enums as enums
import niscope.errors as errors

import niscope.waveform_info as waveform_info  # noqa: F401

import niscope.measurement_stats as measurement_stats  # noqa: F401

import hightime
import nitclk

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class _Acquisition(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate_acquisition()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    @wraps(f)
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.unlock()


class _RepeatedCapabilities(object):
    def __init__(self, session, prefix, current_repeated_capability_list):
        self._session = session
        self._prefix = prefix
        # We need at least one element. If we get an empty list, make the one element an empty string
        self._current_repeated_capability_list = current_repeated_capability_list if len(current_repeated_capability_list) > 0 else ['']
        # Now we know there is at lease one entry, so we look if it is an empty string or not
        self._separator = '/' if len(self._current_repeated_capability_list[0]) > 0 else ''

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)
        complete_rep_cap_list = [current_rep_cap + self._separator + rep_cap for current_rep_cap in self._current_repeated_capability_list for rep_cap in rep_caps_list]

        return _SessionBase(
            repeated_capability_list=complete_rep_cap_list,
            all_channels_in_session=self._session._all_channels_in_session,
            interpreter=self._session._interpreter,
            freeze_it=True
        )


# This is a very simple context manager we can use when we need to set/get attributes
# or call functions from _SessionBase that require no channels. It is tied to the specific
# implementation of _SessionBase and how repeated capabilities are handled.
class _NoChannel(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._repeated_capability_cache = self._session._repeated_capability
        self._session._repeated_capability = ''

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._repeated_capability = self._repeated_capability_cache


class _SessionBase(object):
    '''Base class for all NI-SCOPE sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    absolute_sample_clock_offset = _attributes.AttributeViReal64TimeDeltaSeconds(1150374)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Gets or sets the absolute time offset of the sample clock relative to
    the reference clock in terms of seconds.

    Note:
    Configures the sample clock relationship with respect to the reference
    clock. This parameter is factored into NI-TClk adjustments and is
    typically used to improve the repeatability of NI-TClk Synchronization.
    When this parameter is read, the currently programmed value is returned.
    The range of the absolute sample clock offset is [-.5 sample clock
    periods, .5 sample clock periods]. The default absolute sample clock
    offset is 0s.
    '''
    acquisition_start_time = _attributes.AttributeViReal64TimeDeltaSeconds(1250109)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the length of time from the trigger event to the first point in the waveform record in seconds.  If the value is positive, the first point in the waveform record occurs after the trigger event (same as specifying trigger_delay_time).  If the value is negative, the first point in the waveform record occurs before the trigger event (same as specifying horz_record_ref_position).
    '''
    acquisition_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AcquisitionType, 1250101)
    '''Type: enums.AcquisitionType

    Specifies how the digitizer acquires data and fills the waveform record.
    '''
    acq_arm_source = _attributes.AttributeViString(1150053)
    '''Type: str

    Specifies the source the digitizer monitors for a start (acquisition arm) trigger.  When the start trigger is received, the digitizer begins acquiring pretrigger samples.
    Valid Values:
    NISCOPE_VAL_IMMEDIATE     ('VAL_IMMEDIATE')    - Triggers immediately
    NISCOPE_VAL_RTSI_0        ('VAL_RTSI_0')       - RTSI 0
    NISCOPE_VAL_RTSI_1        ('VAL_RTSI_1')       - RTSI 1
    NISCOPE_VAL_RTSI_2        ('VAL_RTSI_2')       - RTSI 2
    NISCOPE_VAL_RTSI_3        ('VAL_RTSI_3')       - RTSI 3
    NISCOPE_VAL_RTSI_4        ('VAL_RTSI_4')       - RTSI 4
    NISCOPE_VAL_RTSI_5        ('VAL_RTSI_5')       - RTSI 5
    NISCOPE_VAL_RTSI_6        ('VAL_RTSI_6')       - RTSI 6
    NISCOPE_VAL_PFI_0         ('VAL_PFI_0')        - PFI 0
    NISCOPE_VAL_PFI_1         ('VAL_PFI_1')        - PFI 1
    NISCOPE_VAL_PFI_2         ('VAL_PFI_2')        - PFI 2
    NISCOPE_VAL_PXI_STAR      ('VAL_PXI_STAR')     - PXI Star Trigger

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    advance_trigger_terminal_name = _attributes.AttributeViString(1150143)
    '''Type: str

    Returns the fully qualified name for the Advance Trigger terminal.  You can use this terminal as the source for another trigger.
    '''
    adv_trig_src = _attributes.AttributeViString(1150094)
    '''Type: str

    Specifies the source the digitizer monitors for an advance trigger.  When the advance trigger is received, the digitizer begins acquiring pretrigger samples.
    '''
    allow_more_records_than_memory = _attributes.AttributeViBoolean(1150068)
    '''Type: bool

    Indicates whether more records can be configured with configure_horizontal_timing than fit in the onboard memory. If this property is set to True, it is necessary to fetch records while the acquisition is in progress.  Eventually, some of the records will be overwritten.  An error is returned from the fetch method if you attempt to fetch a record that has been overwritten.
    '''
    arm_ref_trig_src = _attributes.AttributeViString(1150095)
    '''Type: str

    Specifies the source the digitizer monitors for an arm reference trigger.  When the arm reference trigger is received, the digitizer begins looking for a reference (stop) trigger from the user-configured trigger source.
    '''
    backlog = _attributes.AttributeViReal64(1150084)
    '''Type: float

    Returns the number of samples (points_done) that have been acquired but not fetched for the record specified by fetch_record_number.
    '''
    bandpass_filter_enabled = _attributes.AttributeViBoolean(1150318)
    '''Type: bool

    Enables the bandpass filter on the specificed channel.  The default value is FALSE.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].bandpass_filter_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.bandpass_filter_enabled`
    '''
    binary_sample_width = _attributes.AttributeViInt32(1150005)
    '''Type: int

    Indicates the bit width of the binary data in the acquired waveform.  Useful for determining which Binary Fetch method to use. Compare to resolution.
    To configure the device to store samples with a lower resolution that the native, set this property to the desired binary width.
    This can be useful for streaming at faster speeds at the cost of resolution. The least significant bits will be lost with this configuration.
    Valid Values: 8, 16, 32
    '''
    cable_sense_mode = _attributes.AttributeEnum(_attributes.AttributeViReal64, enums.CableSenseMode, 1150138)
    '''Type: enums.CableSenseMode

    Specifies whether and how the oscilloscope is configured to generate a CableSense signal on the specified channels when the CableSenseSignalStart method is called.

    Device-Specific Behavior:
        PXIe-5160/5162
            - The value of this property must be identical across all channels whose input impedance is set to 50 ohms.
            - If this property is set to a value other than CableSenseMode.DISABLED for any channel(s), the input impedance of all channels for which this property is set to CableSenseMode.DISABLED must be set to 1 M Ohm.

    +-----------------------+
    | **Supported Devices** |
    +-----------------------+
    | PXIe-5110             |
    +-----------------------+
    | PXIe-5111             |
    +-----------------------+
    | PXIe-5113             |
    +-----------------------+
    | PXIe-5160             |
    +-----------------------+
    | PXIe-5162             |
    +-----------------------+

    Note: the input impedance of the channel(s) to convey the CableSense signal must be set to 50 ohms.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    cable_sense_signal_enable = _attributes.AttributeViBoolean(1150139)
    '''Type: bool

    TBD
    '''
    cable_sense_voltage = _attributes.AttributeViReal64(1150137)
    '''Type: float

    Returns the voltage of the CableSense signal that is written to the EEPROM of the oscilloscope during factory calibration.

    +-----------------------+
    | **Supported Devices** |
    +-----------------------+
    | PXIe-5110             |
    +-----------------------+
    | PXIe-5111             |
    +-----------------------+
    | PXIe-5113             |
    +-----------------------+
    | PXIe-5160             |
    +-----------------------+
    | PXIe-5162             |
    +-----------------------+
    '''
    channel_count = _attributes.AttributeViInt32(1050203)
    '''Type: int

    Indicates the number of channels that the specific instrument driver supports.
    For channel-based properties, the IVI engine maintains a separate cache value for each channel.
    '''
    channel_enabled = _attributes.AttributeViBoolean(1250005)
    '''Type: bool

    Specifies whether the digitizer acquires a waveform for the channel.
    Valid Values:
    True  (1) - Acquire data on this channel
    False (0) - Don't acquire data on this channel

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].channel_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.channel_enabled`
    '''
    channel_terminal_configuration = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TerminalConfiguration, 1150107)
    '''Type: enums.TerminalConfiguration

    Specifies the terminal configuration for the channel.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].channel_terminal_configuration`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.channel_terminal_configuration`
    '''
    data_transfer_block_size = _attributes.AttributeViInt32(1150316)
    '''Type: int

    Specifies the maximum number of samples to transfer at one time from the device to host memory. Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may also increase the amount of page-locked memory required from the system.
    '''
    data_transfer_maximum_bandwidth = _attributes.AttributeViReal64(1150321)
    '''Type: float

    This property specifies the maximum bandwidth that the device is allowed to consume.
    '''
    data_transfer_preferred_packet_size = _attributes.AttributeViInt32(1150322)
    '''Type: int

    This property specifies the size of (read request|memory write) data payload. Due to alignment of the data buffers, the hardware may not always generate a packet of this size.
    '''
    device_temperature = _attributes.AttributeViReal64(1150086)
    '''Type: float

    Returns the temperature of the device in degrees Celsius from the onboard sensor.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].device_temperature`

    To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.device_temperature`
    '''
    enabled_channels = _attributes.AttributeViString(1150140)
    '''Type: str

    Returns a comma-separated list of the channels enabled for the session in ascending order.

    If no channels are enabled, this property returns an empty string, "".
    If all channels are enabled, this property enumerates all of the channels.

    Because this property returns channels in ascending order, but the order in which you specify channels for the input is important, the value of this property may not necessarily reflect the order in which NI-SCOPE performs certain actions.

    Refer to Channel String Syntax in the NI High-Speed Digitizers Help for more information on the effects of channel order in NI-SCOPE.
    '''
    enable_dc_restore = _attributes.AttributeViBoolean(1150093)
    '''Type: bool

    Restores the video-triggered data retrieved by the digitizer to the video signal's zero reference point.
    Valid Values:
    True - Enable DC restore
    False - Disable DC restore
    '''
    enable_time_interleaved_sampling = _attributes.AttributeViBoolean(1150128)
    '''Type: bool

    Specifies whether the digitizer acquires the waveform using multiple ADCs for the channel enabling a higher maximum real-time sampling rate.
    Valid Values:
    True  (1) - Use multiple interleaved ADCs on this channel
    False (0) - Use only this channel's ADC to acquire data for this channel

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].enable_time_interleaved_sampling`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.enable_time_interleaved_sampling`
    '''
    end_of_acquisition_event_output_terminal = _attributes.AttributeViString(1150101)
    '''Type: str

    Specifies the destination for the End of Acquisition Event.    When this event is asserted, the digitizer has completed sampling for all records.
    Consult your device documentation for a specific list of valid destinations.
    '''
    end_of_acquisition_event_terminal_name = _attributes.AttributeViString(1150141)
    '''Type: str

    Returns the fully qualified name for the End of Acquisition Event terminal.    You can use this terminal as the source for a trigger.
    '''
    end_of_record_event_output_terminal = _attributes.AttributeViString(1150099)
    '''Type: str

    Specifies the destination for the End of Record Event.    When this event is asserted, the digitizer has completed sampling for the current record.
    Consult your device documentation for a specific list of valid destinations.
    '''
    end_of_record_event_terminal_name = _attributes.AttributeViString(1150142)
    '''Type: str

    Returns the fully qualified name for the End of Record Event terminal.    You can use this terminal as the source for a trigger.
    '''
    end_of_record_to_advance_trigger_holdoff = _attributes.AttributeViReal64TimeDeltaSeconds(1150366)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    End of Record to Advance Trigger Holdoff is the length of time (in
    seconds) that a device waits between the completion of one record and
    the acquisition of pre-trigger samples for the next record. During this
    time, the acquisition engine state delays the transition to the Wait for
    Advance Trigger state, and will not store samples in onboard memory,
    accept an Advance Trigger, or trigger on the input signal..
    **Supported Devices**: NI 5185/5186
    '''
    equalization_filter_enabled = _attributes.AttributeViBoolean(1150313)
    '''Type: bool

    Enables the onboard signal processing FIR block. This block is connected directly to the input signal.  This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. However, since this is a generic FIR filter any coefficients are valid.  Coefficients should be between +1 and -1 in value.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].equalization_filter_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.equalization_filter_enabled`
    '''
    equalization_num_coefficients = _attributes.AttributeViInt32(1150312)
    '''Type: int

    Returns the number of coefficients that the FIR filter can accept.  This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer.  However, since this is a generic FIR filter any coefficients are valid.  Coefficients should be between +1 and -1 in value.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].equalization_num_coefficients`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.equalization_num_coefficients`
    '''
    exported_advance_trigger_output_terminal = _attributes.AttributeViString(1150109)
    '''Type: str

    Specifies the destination to export the advance trigger.  When the advance trigger is received, the digitizer begins acquiring samples for the Nth record.
    Consult your device documentation for a specific list of valid destinations.
    '''
    exported_ref_trigger_output_terminal = _attributes.AttributeViString(1150098)
    '''Type: str

    Specifies the destination export for the reference (stop) trigger.
    Consult your device documentation for a specific list of valid destinations.
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeViString(1150097)
    '''Type: str

    Specifies the destination to export the Start trigger.  When the start trigger is received, the digitizer begins acquiring samples.
    Consult your device documentation for a specific list of valid destinations.
    '''
    _fetch_meas_num_samples = _attributes.AttributeViInt32(1150081)
    '''Type: int

    Number of samples to fetch when performing a measurement. Use -1 to fetch the actual record length.
    Default Value: -1
    '''
    _fetch_num_records = _attributes.AttributeViInt32(1150080)
    '''Type: int

    Number of records to fetch. Use -1 to fetch all configured records.
    Default Value: -1
    '''
    _fetch_offset = _attributes.AttributeViInt32(1150078)
    '''Type: int

    Offset in samples to start fetching data within each record. The offset is applied relative to fetch_relative_to.The offset can be positive or negative.
    Default Value: 0
    '''
    _fetch_record_number = _attributes.AttributeViInt32(1150079)
    '''Type: int

    Zero-based index of the first record to fetch.  Use NISCOPE_FETCH_NUM_RECORDS to set the number of records to fetch.
    Default Value: 0.
    '''
    _fetch_relative_to = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.FetchRelativeTo, 1150077)
    '''Type: enums.FetchRelativeTo

    Position to start fetching within one record.
    Default Value: FetchRelativeTo.PRETRIGGER
    '''
    flex_fir_antialias_filter_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.FlexFIRAntialiasFilterType, 1150271)
    '''Type: enums.FlexFIRAntialiasFilterType

    The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter.
    Use this property to select from several types of filters to achieve desired filtering characteristics.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].flex_fir_antialias_filter_type`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.flex_fir_antialias_filter_type`
    '''
    fpga_bitfile_path = _attributes.AttributeViString(1150375)
    '''Type: str

    Gets the absolute file path to the bitfile loaded on the FPGA.

    Note: Gets the absolute file path to the bitfile loaded on the FPGA.
    '''
    glitch_condition = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.GlitchCondition, 1250403)
    '''Type: enums.GlitchCondition

    Specifies whether the oscilloscope triggers on pulses of duration less than or greater than the value specified by the glitch_width property.
    '''
    glitch_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.GlitchPolarity, 1250402)
    '''Type: enums.GlitchPolarity

    Specifies the polarity of pulses that trigger the oscilloscope for glitch triggering.
    '''
    glitch_width = _attributes.AttributeViReal64(1250401)
    '''Type: float

    Specifies the glitch duration, in seconds.

    The oscilloscope triggers when it detects of pulse of duration either less than or greater than this value depending on the value of the glitch_condition property.
    '''
    high_pass_filter_frequency = _attributes.AttributeViReal64(1150377)
    '''Type: float

    Specifies the frequency for the highpass filter in Hz. The device uses
    one of the valid values listed below. If an invalid value is specified,
    no coercion occurs. The default value is 0.
    **(PXIe-5164) Valid Values:**
    0 90 450
    **Related topics:**
    `Digital Filtering <digitizers.chm::/Digital_Filtering_Overview.html>`__

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].high_pass_filter_frequency`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.high_pass_filter_frequency`
    '''
    horz_enforce_realtime = _attributes.AttributeViBoolean(1150004)
    '''Type: bool

    Indicates whether the digitizer enforces real-time measurements or allows equivalent-time measurements.
    '''
    horz_min_num_pts = _attributes.AttributeViInt32(1250009)
    '''Type: int

    Specifies the minimum number of points you require in the waveform record for each channel.  NI-SCOPE uses the value you specify to configure the record length that the digitizer uses for waveform acquisition. horz_record_length returns the actual record length.
    Valid Values: 1 - available onboard memory
    '''
    horz_num_records = _attributes.AttributeViInt32(1150001)
    '''Type: int

    Specifies the number of records to acquire. Can be used for multi-record acquisition and single-record acquisitions. Setting this to 1 indicates a single-record acquisition.
    '''
    horz_record_length = _attributes.AttributeViInt32(1250008)
    '''Type: int

    Returns the actual number of points the digitizer acquires for each channel.  The value is equal to or greater than the minimum number of points you specify with horz_min_num_pts.
    Allocate a ViReal64 array of this size or greater to pass as the WaveformArray parameter of the Read and Fetch methods. This property is only valid after a call to the one of the Configure Horizontal methods.
    '''
    horz_record_ref_position = _attributes.AttributeViReal64(1250011)
    '''Type: float

    Specifies the position of the Reference Event in the waveform record.  When the digitizer detects a trigger, it waits the length of time the trigger_delay_time property specifies. The event that occurs when the delay time elapses is the Reference Event. The Reference Event is relative to the start of the record and is a percentage of the record length. For example, the value 50.0 corresponds to the center of the waveform record and 0.0 corresponds to the first element in the waveform record.
    Valid Values: 0.0 - 100.0
    '''
    horz_sample_rate = _attributes.AttributeViReal64(1250010)
    '''Type: float

    Returns the effective sample rate using the current configuration. The units are samples per second.  This property is only valid after a call to the one of the Configure Horizontal methods.
    Units: Hertz (Samples / Second)
    '''
    horz_time_per_record = _attributes.AttributeViReal64TimeDeltaSeconds(1250007)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the length of time that corresponds to the record length.
    Units: Seconds
    '''
    input_clock_source = _attributes.AttributeViString(1150002)
    '''Type: str

    Specifies the input source for the PLL reference clock (the 1 MHz to 20 MHz clock on the NI 5122, the 10 MHz clock for the NI 5112/5620/5621/5911) to which the digitizer will be phase-locked; for the NI 5102, this is the source of the board clock.
    '''
    input_impedance = _attributes.AttributeViReal64(1250103)
    '''Type: float

    Specifies the input impedance for the channel in Ohms.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].input_impedance`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.input_impedance`
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    A string that contains the firmware revision information for the instrument you are currently using.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].instrument_firmware_revision`

    To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.instrument_firmware_revision`
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    A string that contains the name of the instrument manufacturer.
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    A string that contains the model number of the current instrument.
    '''
    interleaving_offset_correction_enabled = _attributes.AttributeViBoolean(1150376)
    '''Type: bool

    Enables the interleaving offset correction on the specified channel. The
    default value is TRUE.
    **Related topics:**
    `Timed Interleaved
    Sampling <digitizers.chm::/TimeInterleavedSampling.html>`__

    Note: If disabled, warranted specifications are not guaranteed.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].interleaving_offset_correction_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.interleaving_offset_correction_enabled`
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    Indicates the resource descriptor the driver uses to identify the physical device.  If you initialize the driver with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration utility.
    If you initialize the instrument driver with the resource descriptor, this property contains that value.You can pass a logical name to Init or __init__. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    is_probe_comp_on = _attributes.AttributeViBoolean(1150066)
    '''Type: bool

    Tip:
    This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].is_probe_comp_on`

    To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.is_probe_comp_on`
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    A string containing the logical name you specified when opening the current IVI session.  You can pass a logical name to Init or __init__. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    master_enable = _attributes.AttributeViBoolean(1150008)
    '''Type: bool

    Specifies whether you want the device to be a master or a slave. The master typically originates the trigger signal and clock sync pulse. For a standalone device, set this property to False.
    '''
    max_input_frequency = _attributes.AttributeViReal64(1250006)
    '''Type: float

    Specifies the bandwidth of the channel. Express this value as the frequency at which the input circuitry attenuates the input signal by 3 dB. The units are hertz.
    Defined Values:
    NISCOPE_VAL_BANDWIDTH_FULL (-1.0)
    NISCOPE_VAL_BANDWIDTH_DEVICE_DEFAULT (0.0)
    NISCOPE_VAL_20MHZ_BANDWIDTH (20000000.0)
    NISCOPE_VAL_100MHZ_BANDWIDTH (100000000.0)
    NISCOPE_VAL_20MHZ_MAX_INPUT_FREQUENCY (20000000.0)
    NISCOPE_VAL_100MHZ_MAX_INPUT_FREQUENCY (100000000.0)

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].max_input_frequency`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.max_input_frequency`
    '''
    max_real_time_sampling_rate = _attributes.AttributeViReal64(1150073)
    '''Type: float

    Returns the maximum real time sample rate in Hz.
    '''
    max_ris_rate = _attributes.AttributeViReal64(1150074)
    '''Type: float

    Returns the maximum sample rate in RIS mode in Hz.
    '''
    meas_array_gain = _attributes.AttributeViReal64(1150043)
    '''Type: float

    Every element of an array is multiplied by this scalar value during the Array Gain measurement.  Refer to ArrayMeasurement.ARRAY_GAIN for more information.
    Default: 1.0

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_array_gain`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_array_gain`
    '''
    meas_array_offset = _attributes.AttributeViReal64(1150044)
    '''Type: float

    Every element of an array is added to this scalar value during the Array Offset measurement. Refer to ArrayMeasurement.ARRAY_OFFSET for more information.
    Default: 0.0

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_array_offset`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_array_offset`
    '''
    meas_chan_high_ref_level = _attributes.AttributeViReal64(1150040)
    '''Type: float

    Stores the high reference level used in many scalar measurements. Different channels may have different reference levels. Do not use the IVI-defined, nonchannel-based properties such as meas_high_ref if you use this property to set various channels to different values.
    Default: 90%

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_chan_high_ref_level`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_chan_high_ref_level`
    '''
    meas_chan_low_ref_level = _attributes.AttributeViReal64(1150038)
    '''Type: float

    Stores the low reference level used in many scalar measurements. Different channels may have different reference levels. Do not use the IVI-defined, nonchannel-based properties such as meas_low_ref if you use this property to set various channels to different values.
    Default: 10%

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_chan_low_ref_level`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_chan_low_ref_level`
    '''
    meas_chan_mid_ref_level = _attributes.AttributeViReal64(1150039)
    '''Type: float

    Stores the mid reference level used in many scalar measurements. Different channels may have different reference levels. Do not use the IVI-defined, nonchannel-based properties such as meas_mid_ref if you use this property to set various channels to different values.
    Default: 50%

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_chan_mid_ref_level`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_chan_mid_ref_level`
    '''
    meas_filter_center_freq = _attributes.AttributeViReal64(1150032)
    '''Type: float

    The center frequency in hertz for filters of type bandpass and bandstop. The width of the filter is specified by meas_filter_width, where the cutoff frequencies are the center ± width.
    Default: 1.0e6 Hz

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_filter_center_freq`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_filter_center_freq`
    '''
    meas_filter_cutoff_freq = _attributes.AttributeViReal64(1150031)
    '''Type: float

    Specifies the cutoff frequency in hertz for filters of type lowpass and highpass. The cutoff frequency definition varies depending on the filter.
    Default: 1.0e6 Hz

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_filter_cutoff_freq`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_filter_cutoff_freq`
    '''
    meas_filter_order = _attributes.AttributeViInt32(1150036)
    '''Type: int

    Specifies the order of an IIR filter. All positive integers are valid.
    Default: 2

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_filter_order`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_filter_order`
    '''
    meas_filter_ripple = _attributes.AttributeViReal64(1150033)
    '''Type: float

    Specifies the amount of ripple in the passband in units of decibels (positive values). Used only for Chebyshev filters. The more ripple allowed gives a sharper cutoff for a given filter order.
    Default: 0.1 dB

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_filter_ripple`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_filter_ripple`
    '''
    meas_filter_taps = _attributes.AttributeViInt32(1150037)
    '''Type: int

    Defines the number of taps (coefficients) for an FIR filter.
    Default: 25

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_filter_taps`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_filter_taps`
    '''
    meas_filter_transient_waveform_percent = _attributes.AttributeViReal64(1150034)
    '''Type: float

    The percentage (0 - 100%) of the IIR filtered waveform to eliminate from the beginning of the waveform. This allows eliminating the transient portion of the waveform that is undefined due to the assumptions necessary at the boundary condition.
    Default: 20.0%

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_filter_transient_waveform_percent`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_filter_transient_waveform_percent`
    '''
    meas_filter_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.FilterType, 1150035)
    '''Type: enums.FilterType

    Specifies the type of filter, for both IIR and FIR filters. The allowed values are the following:
    ·  NISCOPE_VAL_MEAS_LOWPASS
    ·  NISCOPE_VAL_MEAS_HIGHPASS
    ·  NISCOPE_VAL_MEAS_BANDPASS
    ·  NISCOPE_VAL_MEAS_BANDSTOP
    Default: NISCOPE_VAL_MEAS_LOWPASS

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_filter_type`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_filter_type`
    '''
    meas_filter_width = _attributes.AttributeViReal64(1150041)
    '''Type: float

    Specifies the width of bandpass and bandstop type filters in hertz. The cutoff frequencies occur at meas_filter_center_freq ± one-half width.
    Default: 1.0e3 Hz

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_filter_width`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_filter_width`
    '''
    meas_fir_filter_window = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.FIRFilterWindow, 1150042)
    '''Type: enums.FIRFilterWindow

    Specifies the FIR window type. The possible choices are:
    FIRFilterWindow.NONE
    ArrayMeasurement.HANNING_WINDOW
    ArrayMeasurement.HAMMING_WINDOW
    ArrayMeasurement.TRIANGLE_WINDOW
    ArrayMeasurement.FLAT_TOP_WINDOW
    ArrayMeasurement.BLACKMAN_WINDOW
    The symmetric windows are applied to the FIR filter coefficients to limit passband ripple in FIR filters.
    Default: FIRFilterWindow.NONE

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_fir_filter_window`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_fir_filter_window`
    '''
    meas_high_ref = _attributes.AttributeViReal64(1250607)
    meas_hysteresis_percent = _attributes.AttributeViReal64(1150019)
    '''Type: float

    Digital hysteresis that is used in several of the scalar waveform measurements. This property specifies the percentage of the full-scale vertical range for the hysteresis window size.
    Default: 2%

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_hysteresis_percent`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_hysteresis_percent`
    '''
    meas_interpolation_sampling_factor = _attributes.AttributeViReal64(1150030)
    '''Type: float

    The new number of points for polynomial interpolation is the sampling factor times the input number of points. For example, if you acquire 1,000 points with the digitizer and set this property to 2.5, calling FetchWaveformMeasurementArray with the ArrayMeasurement.POLYNOMIAL_INTERPOLATION measurement resamples the waveform to 2,500 points.
    Default: 2.0

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_interpolation_sampling_factor`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_interpolation_sampling_factor`
    '''
    meas_last_acq_histogram_size = _attributes.AttributeViInt32(1150020)
    '''Type: int

    Specifies the size (that is, the number of bins) in the last acquisition histogram. This histogram is used to determine several scalar measurements, most importantly voltage low and voltage high.
    Default: 256

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_last_acq_histogram_size`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_last_acq_histogram_size`
    '''
    meas_low_ref = _attributes.AttributeViReal64(1250608)
    meas_mid_ref = _attributes.AttributeViReal64(1250609)
    meas_other_channel = _attributes.AttributeViStringRepeatedCapability(1150018)
    '''Type: str or int

    Specifies the second channel for two-channel measurements, such as ArrayMeasurement.ADD_CHANNELS. If processing steps are registered with this channel, the processing is done before the waveform is used in a two-channel measurement.
    Default: '0'

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_other_channel`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_other_channel`
    '''
    meas_percentage_method = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PercentageMethod, 1150045)
    '''Type: enums.PercentageMethod

    Specifies the method used to map percentage reference units to voltages for the reference. Possible values are:
    NISCOPE_VAL_MEAS_LOW_HIGH
    NISCOPE_VAL_MEAS_MIN_MAX
    NISCOPE_VAL_MEAS_BASE_TOP
    Default: NISCOPE_VAL_MEAS_BASE_TOP

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_percentage_method`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_percentage_method`
    '''
    meas_polynomial_interpolation_order = _attributes.AttributeViInt32(1150029)
    '''Type: int

    Specifies the polynomial order used for the polynomial interpolation measurement. For example, an order of 1 is linear interpolation whereas an order of 2 specifies parabolic interpolation. Any positive integer is valid.
    Default: 1

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_polynomial_interpolation_order`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_polynomial_interpolation_order`
    '''
    meas_ref_level_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RefLevelUnits, 1150016)
    '''Type: enums.RefLevelUnits

    Specifies the units of the reference levels.
    NISCOPE_VAL_MEAS_VOLTAGE--Specifies that the reference levels are given in units of volts
    NISCOPE_VAL_MEAS_PERCENTAGE--Percentage units, where the measurements voltage low and voltage high represent 0% and 100%, respectively.
    Default: NISCOPE_VAL_MEAS_PERCENTAGE

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_ref_level_units`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_ref_level_units`
    '''
    meas_time_histogram_high_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150028)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the highest time value included in the multiple acquisition time histogram. The units are always seconds.
    Default: 5.0e-4 seconds

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_time_histogram_high_time`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_time_histogram_high_time`
    '''
    meas_time_histogram_high_volts = _attributes.AttributeViReal64(1150026)
    '''Type: float

    Specifies the highest voltage value included in the multiple-acquisition time histogram. The units are always volts.
    Default: 10.0 V

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_time_histogram_high_volts`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_time_histogram_high_volts`
    '''
    meas_time_histogram_low_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150027)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the lowest time value included in the multiple-acquisition time histogram. The units are always seconds.
    Default: -5.0e-4 seconds

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_time_histogram_low_time`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_time_histogram_low_time`
    '''
    meas_time_histogram_low_volts = _attributes.AttributeViReal64(1150025)
    '''Type: float

    Specifies the lowest voltage value included in the multiple acquisition time histogram. The units are always volts.
    Default: -10.0 V

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_time_histogram_low_volts`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_time_histogram_low_volts`
    '''
    meas_time_histogram_size = _attributes.AttributeViInt32(1150024)
    '''Type: int

    Determines the multiple acquisition voltage histogram size. The size is set during the first call to a time histogram measurement after clearing the measurement history with clear_waveform_measurement_stats.
    Default: 256

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_time_histogram_size`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_time_histogram_size`
    '''
    meas_voltage_histogram_high_volts = _attributes.AttributeViReal64(1150023)
    '''Type: float

    Specifies the highest voltage value included in the multiple acquisition voltage histogram. The units are always volts.
    Default: 10.0 V

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_voltage_histogram_high_volts`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_voltage_histogram_high_volts`
    '''
    meas_voltage_histogram_low_volts = _attributes.AttributeViReal64(1150022)
    '''Type: float

    Specifies the lowest voltage value included in the multiple-acquisition voltage histogram. The units are always volts.
    Default: -10.0 V

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_voltage_histogram_low_volts`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_voltage_histogram_low_volts`
    '''
    meas_voltage_histogram_size = _attributes.AttributeViInt32(1150021)
    '''Type: int

    Determines the multiple acquisition voltage histogram size. The size is set the first time a voltage histogram measurement is called after clearing the measurement history with the method clear_waveform_measurement_stats.
    Default: 256

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].meas_voltage_histogram_size`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.meas_voltage_histogram_size`
    '''
    min_sample_rate = _attributes.AttributeViReal64(1150009)
    '''Type: float

    Specify the sampling rate for the acquisition in Samples per second.
    Valid Values:
    The combination of sampling rate and min record length must allow the digitizer to sample at a valid sampling rate for the acquisition type specified in ConfigureAcquisition and not require more memory than the onboard memory module allows.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    onboard_memory_size = _attributes.AttributeViInt32(1150069)
    '''Type: int

    Returns the total combined amount of onboard memory for all channels in bytes.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].onboard_memory_size`

    To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.onboard_memory_size`
    '''
    output_clock_source = _attributes.AttributeViString(1150003)
    '''Type: str

    Specifies the output source for the 10 MHz clock to which another digitizer's sample clock can be phased-locked.
    '''
    pll_lock_status = _attributes.AttributeViBoolean(1151303)
    '''Type: bool

    If TRUE, the PLL has remained locked to the external reference clock since it was last checked. If FALSE,  the PLL has become unlocked from the external reference clock since it was last checked.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].pll_lock_status`

    To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.pll_lock_status`
    '''
    points_done = _attributes.AttributeViReal64(1150082)
    '''Type: float

    Actual number of samples acquired in the record specified by fetch_record_number from the fetch_relative_to and fetch_offset properties.
    '''
    poll_interval = _attributes.AttributeViInt32(1150100)
    '''Type: int

    Specifies the poll interval in milliseconds to use during RIS acquisitions to check whether the acquisition is complete.
    '''
    probe_attenuation = _attributes.AttributeViReal64(1250004)
    '''Type: float

    Specifies the probe attenuation for the input channel. For example, for a 10:1 probe,  set this property to 10.0.
    Valid Values:
    Any positive real number. Typical values are 1, 10, and 100.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].probe_attenuation`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.probe_attenuation`
    '''
    ready_for_advance_event_output_terminal = _attributes.AttributeViString(1150112)
    '''Type: str

    Specifies the destination for the Ready for Advance Event.    When this event is asserted, the digitizer is ready to receive an advance trigger.
    Consult your device documentation for a specific list of valid destinations.
    '''
    ready_for_advance_event_terminal_name = _attributes.AttributeViString(1150146)
    '''Type: str

    Returns the fully qualified name for the Ready for Advance Event terminal.    You can use this terminal as the source for a trigger.
    '''
    ready_for_ref_event_output_terminal = _attributes.AttributeViString(1150111)
    '''Type: str

    Specifies the destination for the Ready for Reference Event.  When this event is asserted, the digitizer is ready to receive a reference trigger.
    Consult your device documentation for a specific list of valid destinations.
    '''
    ready_for_ref_event_terminal_name = _attributes.AttributeViString(1150147)
    '''Type: str

    Returns the fully qualified name for the Ready for Reference Event terminal.    You can use this terminal as the source for a trigger.
    '''
    ready_for_start_event_output_terminal = _attributes.AttributeViString(1150110)
    '''Type: str

    Specifies the destination for the Ready for Start Event.  When this event is asserted, the digitizer is ready to receive a start trigger.
    Consult your device documentation for a specific list of valid destinations.
    '''
    ready_for_start_event_terminal_name = _attributes.AttributeViString(1150148)
    '''Type: str

    Returns the fully qualified name for the Ready for Start Event terminal.    You can use this terminal as the source for a trigger.
    '''
    records_done = _attributes.AttributeViInt32(1150083)
    '''Type: int

    Specifies the number of records that have been completely acquired.
    '''
    record_arm_source = _attributes.AttributeViString(1150065)
    '''Type: str

    Specifies the record arm source.
    '''
    ref_clk_rate = _attributes.AttributeViReal64(1150090)
    '''Type: float

    If input_clock_source is an external source, this property specifies the frequency of the input,  or reference clock, to which the internal sample clock timebase is synchronized. The frequency is in hertz.
    '''
    ref_trigger_detector_location = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RefTriggerDetectorLocation, 1150314)
    '''Type: enums.RefTriggerDetectorLocation

    Indicates which analog compare circuitry to use on the device.
    '''
    ref_trigger_minimum_quiet_time = _attributes.AttributeViReal64TimeDeltaSeconds(1150315)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    The amount of time the trigger circuit must not detect a signal above the trigger level before the trigger is armed.  This property is useful for triggering at the beginning and not in the middle of signal bursts.
    '''
    ref_trigger_terminal_name = _attributes.AttributeViString(1150144)
    '''Type: str

    Returns the fully qualified name for the Reference Trigger terminal.  You can use this terminal as the source for another trigger.
    '''
    ref_trig_tdc_enable = _attributes.AttributeViBoolean(1150096)
    '''Type: bool

    This property controls whether the TDC is used to compute an accurate trigger.
    '''
    resolution = _attributes.AttributeViInt32(1150102)
    '''Type: int

    Indicates the bit width of valid data (as opposed to padding bits) in the acquired waveform. Compare to binary_sample_width.
    '''
    ris_in_auto_setup_enable = _attributes.AttributeViBoolean(1150106)
    '''Type: bool

    Indicates whether the digitizer should use RIS sample rates when searching for a frequency in autosetup.
    Valid Values:
    True  (1) - Use RIS sample rates in autosetup
    False (0) - Do not use RIS sample rates in autosetup
    '''
    ris_method = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RISMethod, 1150071)
    '''Type: enums.RISMethod

    Specifies the algorithm for random-interleaved sampling, which is used if the sample rate exceeds the value of max_real_time_sampling_rate.
    '''
    ris_num_averages = _attributes.AttributeViInt32(1150070)
    '''Type: int

    The number of averages for each bin in an RIS acquisition.  The number of averages times the oversampling factor is the minimum number of real-time acquisitions necessary to reconstruct the RIS waveform.  Averaging is useful in RIS because the trigger times are not evenly spaced, so adjacent points in the reconstructed waveform not be accurately spaced.  By averaging, the errors in both time and voltage are smoothed.
    '''
    runt_high_threshold = _attributes.AttributeViReal64(1250301)
    '''Type: float

    Specifies the higher of two thresholds, in volts, that bound the vertical range to examine for runt pulses.

    The runt threshold that causes the oscilloscope to trigger depends on the runt polarity you select. Refer to the runt_polarity property for more information.
    '''
    runt_low_threshold = _attributes.AttributeViReal64(1250302)
    '''Type: float

    Specifies the lower of two thresholds, in volts, that bound the vertical range to examine for runt pulses.

    The runt threshold that causes the oscilloscope to trigger depends on the runt polarity you select. Refer to the runt_polarity property for more information.
    '''
    runt_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RuntPolarity, 1250303)
    '''Type: enums.RuntPolarity

    Specifies the polarity of pulses that trigger the oscilloscope for runt triggering.

    When set to RuntPolarity.POSITIVE, the oscilloscope triggers when the following conditions are met:
        * The leading edge of a pulse crosses the runt_low_threshold in a positive direction;
        * The trailing edge of the pulse crosses the runt_low_threshold in a negative direction; and
        * No portion of the pulse crosses the runt_high_threshold.

    When set to RuntPolarity.NEGATIVE, the oscilloscope triggers when the following conditions are met:
        * The leading edge of a pulse crosses the runt_high_threshold in a negative direction;
        * The trailing edge of the pulse crosses the runt_high_threshold in a positive direction; and
        * No portion of the pulse crosses the runt_low_threshold.

    When set to RuntPolarity.EITHER, the oscilloscope triggers in either case.
    '''
    runt_time_condition = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RuntTimeCondition, 1150132)
    '''Type: enums.RuntTimeCondition

    Specifies whether runt triggers are time qualified, and if so, how the oscilloscope triggers in relation to the duration range bounded by the runt_time_low_limit and runt_time_high_limit properties.
    '''
    runt_time_high_limit = _attributes.AttributeViReal64(1150134)
    '''Type: float

    Specifies, in seconds, the high runt threshold time.

    This property sets the upper bound on the duration of runt pulses that may trigger the oscilloscope. The runt_time_condition property determines how the oscilloscope triggers in relation to the runt time limits.
    '''
    runt_time_low_limit = _attributes.AttributeViReal64(1150133)
    '''Type: float

    Specifies, in seconds, the low runt threshold time.

    This property sets the lower bound on the duration of runt pulses that may trigger the oscilloscope. The runt_time_condition property determines how the oscilloscope triggers in relation to the runt time limits.
    '''
    sample_mode = _attributes.AttributeViInt32(1250106)
    '''Type: int

    Indicates the sample mode the digitizer is currently using.
    '''
    samp_clk_timebase_div = _attributes.AttributeViInt32(1150089)
    '''Type: int

    If samp_clk_timebase_src is an external source, specifies the ratio between the sample clock timebase rate and the actual sample rate, which can be slower.
    '''
    sample_clock_timebase_multiplier = _attributes.AttributeViInt32(1150367)
    '''Type: int

    If samp_clk_timebase_src is an external source, this property specifies the ratio between the samp_clk_timebase_rate and the actual sample rate, which can be higher. This property can be used in conjunction with samp_clk_timebase_div.
    Some devices use multiple ADCs to sample the same channel at an effective sample rate that is greater than the specified clock rate. When providing an external sample clock use this property to indicate when you want a higher sample rate. Valid values for this property vary by device and current configuration.

    **Related topics:**
    `Sample Clock <digitizers.chm::/Sample_Clock.html>`__
    '''
    samp_clk_timebase_rate = _attributes.AttributeViReal64(1150088)
    '''Type: float

    If samp_clk_timebase_src is an external source, specifies the frequency in hertz of the external clock used as the timebase source.
    '''
    samp_clk_timebase_src = _attributes.AttributeViString(1150087)
    '''Type: str

    Specifies the source of the sample clock timebase, which is the timebase used to control waveform sampling.  The actual sample rate may be the timebase itself or a divided version of the timebase, depending on the min_sample_rate (for internal sources) or the samp_clk_timebase_div (for external sources).
    '''
    serial_number = _attributes.AttributeViString(1150104)
    '''Type: str

    Returns the serial number of the device.

    Tip:
    This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container instruments to specify a subset.

    Example: :py:attr:`my_session.instruments[ ... ].serial_number`

    To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.serial_number`
    '''
    accessory_gain = _attributes.AttributeViReal64(1150279)
    '''Type: float

    Returns the calibration gain for the current device configuration.

    **Related topics:**
    `NI 5122/5124/5142 Calibration <digitizers.chm::/5122_Calibration.html>`__

    Note:
    This property is supported only by the NI PXI-5900 differential amplifier.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].accessory_gain`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.accessory_gain`
    '''
    accessory_offset = _attributes.AttributeViReal64(1150280)
    '''Type: float

    Returns the calibration offset for the current device configuration.

    **Related topics:**
    `NI 5122/5124/5142 Calibration <digitizers.chm::/5122_Calibration.html>`__

    Note:
    This property is supported only by the NI PXI-5900 differential amplifier.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].accessory_offset`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.accessory_offset`
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Specifies whether or not to simulate instrument driver I/O operations.  If simulation is enabled, instrument driver methods perform range checking and call Ivi_GetAttribute and Ivi_SetAttribute methods, but they do not perform instrument I/O.  For output parameters that represent instrument data, the instrument driver methods return calculated values.
    The default value is False.  Use the __init__ method to override this value.
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    A string that contains a brief description of the specific driver
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    A string that contains additional version information about this instrument driver.
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    A string that contains the name of the vendor that supplies this driver.
    '''
    start_to_ref_trigger_holdoff = _attributes.AttributeViReal64TimeDeltaSeconds(1150103)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Pass the length of time you want the digitizer to wait after it starts acquiring data until the digitizer enables the trigger system to detect a reference (stop) trigger.
    Units: Seconds
    Valid Values: 0.0 - 171.8
    '''
    start_trigger_terminal_name = _attributes.AttributeViString(1150145)
    '''Type: str

    Returns the fully qualified name for the Start Trigger terminal.  You can use this terminal as the source for another trigger.
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    A string that contains a comma-separated list of the instrument model numbers supported by this driver.
    '''
    trigger_auto_triggered = _attributes.AttributeViBoolean(1150278)
    '''Type: bool

    Specifies if the last acquisition was auto triggered.  You can use the Auto Triggered property to find out if the last acquisition was triggered.
    '''
    trigger_coupling = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerCoupling, 1250014)
    '''Type: enums.TriggerCoupling

    Specifies how the digitizer couples the trigger source. This property affects instrument operation only when trigger_type is set to TriggerType.EDGE, TriggerType.HYSTERESIS, or TriggerType.WINDOW.
    '''
    trigger_delay_time = _attributes.AttributeViReal64TimeDeltaSeconds(1250015)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the trigger delay time in seconds. The trigger delay time is the length of time the digitizer waits after it receives the trigger. The event that occurs when the trigger delay elapses is the Reference Event.
    Valid Values: 0.0 - 171.8
    '''
    trigger_holdoff = _attributes.AttributeViReal64TimeDeltaSeconds(1250016)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the length of time (in seconds) the digitizer waits after detecting a trigger before enabling the trigger subsystem to detect another trigger. This property affects instrument operation only when the digitizer requires multiple acquisitions to build a complete waveform. The digitizer requires multiple waveform acquisitions when it uses equivalent-time sampling or when the digitizer is configured for a multi-record acquisition through a call to configure_horizontal_timing.
    Valid Values: 0.0 - 171.8
    '''
    trigger_hysteresis = _attributes.AttributeViReal64(1150006)
    '''Type: float

    Specifies the size of the hysteresis window on either side of the trigger level.  The digitizer triggers when the trigger signal passes through the threshold you specify with the Trigger Level parameter, has the slope you specify with the Trigger Slope parameter,  and passes through the hysteresis window that you specify with this parameter.
    '''
    trigger_impedance = _attributes.AttributeViReal64(1150075)
    '''Type: float

    Specifies the input impedance for the external analog trigger channel in Ohms.
    Valid Values:
    50      - 50 ohms
    1000000 - 1 mega ohm
    '''
    trigger_level = _attributes.AttributeViReal64(1250017)
    '''Type: float

    Specifies the voltage threshold for the trigger subsystem. The units are volts.  This property affects instrument behavior only when the trigger_type is set to TriggerType.EDGE, TriggerType.HYSTERESIS, or TriggerType.WINDOW.
    Valid Values:
    The values of the range and offset parameters in configure_vertical determine the valid range for the trigger level on the channel you use as the Trigger Source. The value you pass for this parameter must meet the following conditions:
    '''
    trigger_modifier = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerModifier, 1250102)
    '''Type: enums.TriggerModifier

    Configures the device to automatically complete an acquisition if a trigger has not been received.
    Valid Values:
    None (1)         - Normal triggering
    Auto Trigger (2) - Auto trigger acquisition if no trigger arrives
    '''
    trigger_slope = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerSlope, 1250018)
    '''Type: enums.TriggerSlope

    Specifies if a rising or a falling edge triggers the digitizer.  This property affects instrument operation only when trigger_type is set to TriggerType.EDGE, TriggerType.HYSTERESIS, or TriggerType.WINDOW.
    '''
    trigger_source = _attributes.AttributeViString(1250013)
    '''Type: str

    Specifies the source the digitizer monitors for the trigger event.
    '''
    trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerType, 1250012)
    '''Type: enums.TriggerType

    Specifies the type of trigger to use.
    '''
    trigger_window_high_level = _attributes.AttributeViReal64(1150014)
    '''Type: float

    Pass the upper voltage threshold you want the digitizer to use for window triggering.
    The digitizer triggers when the trigger signal enters or leaves the window you specify with trigger_window_low_level and trigger_window_high_level
    Valid Values:
    The values of the Vertical Range and Vertical Offset parameters in configure_vertical determine the valid range for the High Window Level on the channel you use as the Trigger Source parameter in ConfigureTriggerSource.  The value you pass for this parameter must meet the following conditions.
    High Trigger Level <= Vertical Range/2 + Vertical Offset
    High Trigger Level >= (-Vertical Range/2) + Vertical Offset
    High Trigger Level > Low Trigger Level

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    trigger_window_low_level = _attributes.AttributeViReal64(1150013)
    '''Type: float

    Pass the lower voltage threshold you want the digitizer to use for window triggering.
    The digitizer triggers when the trigger signal enters or leaves the window you specify with trigger_window_low_level and trigger_window_high_level.
    Units: Volts
    Valid Values:
    The values of the Vertical Range and Vertical Offset parameters in configure_vertical determine the valid range for the Low Window Level on the channel you use as the Trigger Source parameter in ConfigureTriggerSource.  The value you pass for this parameter must meet the following conditions.
    Low Trigger Level <= Vertical Range/2 + Vertical Offset
    Low Trigger Level >= (-Vertical Range/2) + Vertical Offset
    Low Trigger Level < High Trigger Level

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    trigger_window_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerWindowMode, 1150012)
    '''Type: enums.TriggerWindowMode

    Specifies whether you want a trigger to occur when the signal enters or leaves the window specified by trigger_window_low_level, or trigger_window_high_level.
    '''
    tv_trigger_event = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.VideoTriggerEvent, 1250205)
    '''Type: enums.VideoTriggerEvent

    Specifies the condition in the video signal that causes the digitizer to trigger.
    '''
    tv_trigger_line_number = _attributes.AttributeViInt32(1250206)
    '''Type: int

    Specifies the line on which to trigger, if tv_trigger_event is set to line number. The valid ranges of the property depend on the signal format selected.  M-NTSC has a valid range of 1 to 525.  B/G-PAL, SECAM, 576i, and 576p have a valid range of 1 to 625. 720p has a valid range of 1 to 750. 1080i and 1080p have a valid range of 1125.
    '''
    tv_trigger_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.VideoPolarity, 1250204)
    '''Type: enums.VideoPolarity

    Specifies whether the video signal sync is positive or negative.
    '''
    tv_trigger_signal_format = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.VideoSignalFormat, 1250201)
    '''Type: enums.VideoSignalFormat

    Specifies the type of video signal, such as NTSC, PAL, or SECAM.
    '''
    use_spec_initial_x = _attributes.AttributeViBoolean(1150067)
    vertical_coupling = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.VerticalCoupling, 1250003)
    '''Type: enums.VerticalCoupling

    Specifies how the digitizer couples the input signal for the channel.  When input coupling changes, the input stage takes a finite amount of time to settle.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].vertical_coupling`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.vertical_coupling`
    '''
    vertical_offset = _attributes.AttributeViReal64(1250002)
    '''Type: float

    Specifies the location of the center of the range. The value is with respect to ground and is in volts.  For example, to acquire a sine wave that spans between 0.0 and 10.0 V, set this property to 5.0 V.

    Note: This property is not supported by all digitizers.Refer to the NI High-Speed Digitizers Help for a list of vertical offsets supported for each device.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].vertical_offset`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.vertical_offset`
    '''
    vertical_range = _attributes.AttributeViReal64(1250001)
    '''Type: float

    Specifies the absolute value of the input range for a channel in volts.  For example, to acquire a sine wave that spans between -5 and +5 V, set this property to 10.0 V.
    Refer to the NI High-Speed Digitizers Help for a list of supported vertical ranges for each device.  If the specified range is not supported by a device, the value is coerced up to the next valid range.

    Tip:
    This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].vertical_range`

    To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

    Example: :py:attr:`my_session.vertical_range`
    '''
    width_condition = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WidthCondition, 1250504)
    '''Type: enums.WidthCondition

    Specifies whether the oscilloscope triggers on pulses within or outside the duration range bounded by the width_low_threshold and width_high_threshold properties.
    '''
    width_high_threshold = _attributes.AttributeViReal64(1250502)
    '''Type: float

    Specifies the high width threshold, in seconds.

    This properties sets the upper bound on the duration range that triggers the oscilloscope. The width_condition property determines how the oscilloscope triggers in relation to the width thresholds.
    '''
    width_low_threshold = _attributes.AttributeViReal64(1250501)
    '''Type: float

    Specifies the low width threshold, in seconds.

    This property sets the lower bound on the duration range that triggers the oscilloscope. The width_condition property determines how the oscilloscope triggers in relation to the width thresholds.
    '''
    width_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WidthPolarity, 1250503)
    '''Type: enums.WidthPolarity

    Specifies the polarity of pulses that trigger the oscilloscope for width triggering.
    '''

    def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._interpreter = interpreter

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("interpreter=" + pp.pformat(interpreter))
        self._param_list = ', '.join(param_list)

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.instruments = _RepeatedCapabilities(self, '', repeated_capability_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('niscope', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    ''' These are code-generated '''

    @ivi_synchronized
    def _actual_meas_wfm_size(self, array_meas_function):
        r'''_actual_meas_wfm_size

        Returns the total available size of an array measurement acquisition.

        Args:
            array_meas_function (enums.ArrayMeasurement): The `array
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
                to perform.


        Returns:
            meas_waveform_size (int): Returns the size (in number of samples) of the resulting analysis
                waveform.

        '''
        if type(array_meas_function) is not enums.ArrayMeasurement:
            raise TypeError('Parameter array_meas_function must be of type ' + str(enums.ArrayMeasurement))
        meas_waveform_size = self._interpreter.actual_meas_wfm_size(array_meas_function)
        return meas_waveform_size

    @ivi_synchronized
    def _actual_num_wfms(self):
        r'''_actual_num_wfms

        Helps you to declare appropriately sized waveforms. NI-SCOPE handles the
        channel list parsing for you.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._actual_num_wfms`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._actual_num_wfms`

        Returns:
            num_wfms (int): Returns the number of records times the number of channels; if you are
                operating in DDC mode (NI 5620/5621 only), this value is multiplied by
                two.

        '''
        num_wfms = self._interpreter.actual_num_wfms(self._repeated_capability)
        return num_wfms

    @ivi_synchronized
    def add_waveform_processing(self, meas_function):
        r'''add_waveform_processing

        Adds one measurement to the list of processing steps that are completed
        before the measurement. The processing is added on a per channel basis,
        and the processing measurements are completed in the same order they are
        registered. All measurement library parameters—the properties starting
        with "meas_"—are cached at the time of registering the
        processing, and this set of parameters is used during the processing
        step. The processing measurements are streamed, so the result of the
        first processing step is used as the input for the next step. The
        processing is done before any other measurements.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].add_waveform_processing`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.add_waveform_processing`

        Args:
            meas_function (enums.ArrayMeasurement): The `array
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
                to add.

        '''
        if type(meas_function) is not enums.ArrayMeasurement:
            raise TypeError('Parameter meas_function must be of type ' + str(enums.ArrayMeasurement))
        self._interpreter.add_waveform_processing(self._repeated_capability, meas_function)

    @ivi_synchronized
    def self_cal(self, option=enums.Option.SELF_CALIBRATE_ALL_CHANNELS):
        r'''self_cal

        Self-calibrates most NI digitizers, including all SMC-based devices and
        most Traditional NI-DAQ (Legacy) devices. To verify that your digitizer
        supports self-calibration, refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__.

        For SMC-based digitizers, if the self-calibration is performed
        successfully in a regular session, the calibration constants are
        immediately stored in the self-calibration area of the EEPROM. If the
        self-calibration is performed in an external calibration session, the
        calibration constants take effect immediately for the duration of the
        session. However, they are not stored in the EEPROM until
        CalEnd is called with **action** set to
        NISCOPE_VAL_ACTION_STORE and no errors occur.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].self_cal`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.self_cal`

        Args:
            option (enums.Option): The calibration option. Use VI_NULL for a normal self-calibration
                operation or NISCOPE_VAL_CAL_RESTORE_EXTERNAL_CALIBRATION to
                restore the previous calibration.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(option) is not enums.Option:
            raise TypeError('Parameter option must be of type ' + str(enums.Option))
        self._interpreter.self_cal(self._repeated_capability, option)

    @ivi_synchronized
    def clear_waveform_measurement_stats(self, clearable_measurement_function=enums.ClearableMeasurement.ALL_MEASUREMENTS):
        r'''clear_waveform_measurement_stats

        Clears the waveform stats on the channel and measurement you specify. If
        you want to clear all of the measurements, use
        ClearableMeasurement.ALL_MEASUREMENTS in the **clearableMeasurementFunction**
        parameter.

        Every time a measurement is called, the statistics information is
        updated, including the min, max, mean, standard deviation, and number of
        updates. This information is fetched with
        _fetch_measurement_stats. The multi-acquisition array measurements
        are also cleared with this method.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clear_waveform_measurement_stats`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.clear_waveform_measurement_stats`

        Args:
            clearable_measurement_function (enums.ClearableMeasurement): The `scalar
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
                or `array
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
                to clear the stats for.

        '''
        if type(clearable_measurement_function) is not enums.ClearableMeasurement:
            raise TypeError('Parameter clearable_measurement_function must be of type ' + str(enums.ClearableMeasurement))
        self._interpreter.clear_waveform_measurement_stats(self._repeated_capability, clearable_measurement_function)

    @ivi_synchronized
    def clear_waveform_processing(self):
        r'''clear_waveform_processing

        Clears the list of processing steps assigned to the given channel. The
        processing is added using the add_waveform_processing method,
        where the processing steps are completed in the same order in which they
        are registered. The processing measurements are streamed, so the result
        of the first processing step is used as the input for the next step. The
        processing is also done before any other measurements.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clear_waveform_processing`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.clear_waveform_processing`
        '''
        self._interpreter.clear_waveform_processing(self._repeated_capability)

    @ivi_synchronized
    def configure_chan_characteristics(self, input_impedance, max_input_frequency):
        r'''configure_chan_characteristics

        Configures the properties that control the electrical characteristics of
        the channel—the input impedance and the bandwidth.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_chan_characteristics`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.configure_chan_characteristics`

        Args:
            input_impedance (float): The input impedance for the channel; NI-SCOPE sets
                input_impedance to this value.

            max_input_frequency (float): The bandwidth for the channel; NI-SCOPE sets
                max_input_frequency to this value. Pass 0 for this
                value to use the hardware default bandwidth. Pass –1 for this value to
                achieve full bandwidth.

        '''
        self._interpreter.configure_chan_characteristics(self._repeated_capability, input_impedance, max_input_frequency)

    @ivi_synchronized
    def configure_equalization_filter_coefficients(self, coefficients):
        r'''configure_equalization_filter_coefficients

        Configures the custom coefficients for the equalization FIR filter on
        the device. This filter is designed to compensate the input signal for
        artifacts introduced to the signal outside of the digitizer. Because
        this filter is a generic FIR filter, any coefficients are valid.
        Coefficient values should be between +1 and –1.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_equalization_filter_coefficients`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.configure_equalization_filter_coefficients`

        Args:
            coefficients (list of float): The custom coefficients for the equalization FIR filter on the device.
                These coefficients should be between +1 and –1. You can obtain the
                number of coefficients from the
                `equalization_num_coefficients <cviequalization_num_coefficients.html>`__
                property. The
                `equalization_filter_enabled <cviequalization_filter_enabled.html>`__
                property must be set to TRUE to enable the filter.

        '''
        self._interpreter.configure_equalization_filter_coefficients(self._repeated_capability, coefficients)

    @ivi_synchronized
    def configure_vertical(self, range, coupling, offset=0.0, probe_attenuation=1.0, enabled=True):
        r'''configure_vertical

        Configures the most commonly configured properties of the digitizer
        vertical subsystem, such as the range, offset, coupling, probe
        attenuation, and the channel.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_vertical`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.configure_vertical`

        Args:
            range (float): Specifies the vertical range Refer to vertical_range for
                more information.

            coupling (enums.VerticalCoupling): Specifies how to couple the input signal. Refer to
                vertical_coupling for more information.

            offset (float): Specifies the vertical offset. Refer to vertical_offset
                for more information.

            probe_attenuation (float): Specifies the probe attenuation. Refer to
                probe_attenuation for valid values.

            enabled (bool): Specifies whether the channel is enabled for acquisition. Refer to
                channel_enabled for more information.

        '''
        if type(coupling) is not enums.VerticalCoupling:
            raise TypeError('Parameter coupling must be of type ' + str(enums.VerticalCoupling))
        self._interpreter.configure_vertical(self._repeated_capability, range, offset, coupling, probe_attenuation, enabled)

    @ivi_synchronized
    def fetch(self, num_samples=None, relative_to=enums.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0)):
        '''fetch

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This method returns
        scaled voltage waveforms.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note: Some functionality, such as time stamping, is not supported in all digitizers.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.fetch`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the method raises.

            relative_to (enums.FetchRelativeTo): Position to start fetching within one record.

            offset (int): Offset in samples to start fetching data within each record. The offset can be positive or negative.

            record_number (int): Zero-based index of the first record to fetch.

            num_records (int): Number of records to fetch. Use -1 to fetch all configured records.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.


        Returns:
            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling information about each waveform:

                -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
                -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
                -  **x_increment** (float) the time between points in the acquired waveform in seconds
                -  **channel** (str) channel name this waveform was acquired from
                -  **record** (int) record number of this waveform
                -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                    .. math::

                        voltage = binary data * gain factor + offset

                -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                    .. math::

                        voltage = binary data * gain factor + offset

                - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

        '''
        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records
            if num_samples is None:
                num_samples = self.horz_record_length

        wfm, wfm_info = self._fetch(num_samples, timeout)

        if isinstance(wfm, array.ArrayType):
            mv = memoryview(wfm)
        else:
            mv = wfm

        waveform_info._populate_samples_info(wfm_info, mv, num_samples)

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )

        wfm_info_count = len(wfm_info)
        channel_count = len(channel_names)
        # Should this raise instead? If this asserts, is it the users fault?
        assert wfm_info_count % channel_count == 0, 'Number of waveforms should be evenly divisible by the number of channels: len(wfm_info) == {0}, len(channel_names) == {1}'.format(wfm_info_count, channel_count)
        actual_num_records = int(wfm_info_count / channel_count)
        waveform_info._populate_channel_and_record_info(wfm_info, channel_names, range(record_number, record_number + actual_num_records))

        return wfm_info

    @ivi_synchronized
    def fetch_array_measurement(self, array_meas_function, meas_wfm_size=None, relative_to=enums.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, meas_num_samples=None, timeout=hightime.timedelta(seconds=5.0)):
        r'''fetch_array_measurement

        Obtains a waveform from the digitizer and returns the specified
        measurement array. This method may return multiple waveforms depending
        on the number of channels, the acquisition type, and the number of
        records you specify.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch_array_measurement`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.fetch_array_measurement`

        Args:
            array_meas_function (enums.ArrayMeasurement): The array measurement to perform.

            meas_wfm_size (int): The maximum number of samples returned in the measurement waveform array
                for each waveform measurement. Default Value: None (returns all available samples).

            relative_to (enums.FetchRelativeTo): Position to start fetching within one record.

            offset (int): Offset in samples to start fetching data within each record. The offset can be positive or negative.

            record_number (int): Zero-based index of the first record to fetch.

            num_records (int): Number of records to fetch. Use `None` to fetch all configured records.

            meas_num_samples (int): Number of samples to fetch when performing a measurement. Use `None` to fetch the actual record length.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **channel**-channel name this waveform was acquired from
                -  **record**-record number of this waveform
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **samples**-floating point array of samples. Length will be of actual samples acquired.

        '''
        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records
            self._fetch_meas_num_samples = -1 if meas_num_samples is None else meas_num_samples

        # For GrpcStubInterpreter, the server will automatically get _actual_meas_wfm_size, if needed.
        if isinstance(self._interpreter, _library_interpreter.LibraryInterpreter):
            if meas_wfm_size is None:
                meas_wfm_size = self._actual_meas_wfm_size(array_meas_function)

        meas_wfm, wfm_info = self._fetch_array_measurement(array_meas_function, meas_wfm_size, timeout)

        record_length = int(len(meas_wfm) / len(wfm_info))
        waveform_info._populate_samples_info(wfm_info, meas_wfm, record_length)

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )

        wfm_info_count = len(wfm_info)
        channel_count = len(channel_names)
        # Should this raise instead? If this asserts, is it the users fault?
        assert wfm_info_count % channel_count == 0, 'Number of waveforms should be evenly divisible by the number of channels: len(wfm_info) == {0}, len(channel_names) == {1}'.format(wfm_info_count, channel_count)
        actual_num_records = int(wfm_info_count / channel_count)
        waveform_info._populate_channel_and_record_info(wfm_info, channel_names, range(record_number, record_number + actual_num_records))

        return wfm_info

    @ivi_synchronized
    def fetch_measurement_stats(self, scalar_meas_function, relative_to=enums.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0)):
        r'''fetch_measurement_stats

        Obtains a waveform measurement and returns the measurement value. This
        method may return multiple statistical results depending on the number
        of channels, the acquisition type, and the number of records you
        specify.

        You specify a particular measurement type, such as rise time, frequency,
        or voltage peak-to-peak. The waveform on which the digitizer calculates
        the waveform measurement is from an acquisition that you previously
        initiated. The statistics for the specified measurement method are
        returned, where the statistics are updated once every acquisition when
        the specified measurement is fetched by any of the Fetch Measurement
        methods. If a Fetch Measurement method has not been called, this
        method fetches the data on which to perform the measurement. The
        statistics are cleared by calling
        clear_waveform_measurement_stats.

        Many of the measurements use the low, mid, and high reference levels.
        You configure the low, mid, and high references with
        meas_chan_low_ref_level,
        meas_chan_mid_ref_level, and
        meas_chan_high_ref_level to set each channel
        differently.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch_measurement_stats`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.fetch_measurement_stats`

        Args:
            scalar_meas_function (enums.ScalarMeasurement): The scalar measurement to be performed on each fetched waveform.

            relative_to (enums.FetchRelativeTo): Position to start fetching within one record.

            offset (int): Offset in samples to start fetching data within each record. The offset can be positive or negative.

            record_number (int): Zero-based index of the first record to fetch.

            num_records (int): Number of records to fetch. Use `None` to fetch all configured records.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            measurement_stats (list of MeasurementStats): Returns a list of class instances with the following measurement statistics
                about the specified measurement:

                -	**result** (float): the resulting measurement
                -	**mean** (float): the mean scalar value, which is obtained by
                averaging each fetch_measurement_stats call
                -	**stdev** (float): the standard deviations of the most recent
                **numInStats** measurements
                -	**min_val** (float): the smallest scalar value acquired (the minimum
                of the **numInStats** measurements)
                -	**max_val** (float): the largest scalar value acquired (the maximum
                of the **numInStats** measurements)
                -	**num_in_stats** (int): the number of times fetch_measurement_stats has been called
                -	**channel** (str): channel name this result was acquired from
                -	**record** (int): record number of this result

        '''
        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records

        results, means, stdevs, min_vals, max_vals, nums_in_stats = self._fetch_measurement_stats(scalar_meas_function, timeout)

        output = []
        for result, mean, stdev, min_val, max_val, num_in_stats in zip(results, means, stdevs, min_vals, max_vals, nums_in_stats):
            measurement_stat = measurement_stats.MeasurementStats(result, mean, stdev, min_val, max_val, num_in_stats)
            output.append(measurement_stat)

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )

        results_count = len(results)
        channel_count = len(channel_names)
        # Should this raise instead? If this asserts, is it the users fault?
        assert results_count % channel_count == 0, 'Number of results should be evenly divisible by the number of channels: len(results) == {0}, len(channel_names) == {1}'.format(results_count, channel_count)
        actual_num_records = int(results_count / channel_count)
        waveform_info._populate_channel_and_record_info(output, channel_names, range(record_number, record_number + actual_num_records))

        return output

    @ivi_synchronized
    def get_equalization_filter_coefficients(self):
        '''get_equalization_filter_coefficients

        Retrieves the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and –1.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_equalization_filter_coefficients`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.get_equalization_filter_coefficients`
        '''
        return self._get_equalization_filter_coefficients(self.equalization_num_coefficients)

    @ivi_synchronized
    def read(self, num_samples=None, relative_to=enums.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0)):
        '''read

        Initiates an acquisition, waits for it to complete, and retrieves the
        data. The process is similar to calling _initiate_acquisition,
        acquisition_status, and fetch. The only difference is
        that with read, you enable all channels specified with
        **channelList** before the acquisition; in the other method, you enable
        the channels with configure_vertical.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note: Some functionality, such as time stamping, is not supported in all digitizers.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.read`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the method raises.

            relative_to (enums.FetchRelativeTo): Position to start fetching within one record.

            offset (int): Offset in samples to start fetching data within each record. The offset can be positive or negative.

            record_number (int): Zero-based index of the first record to fetch.

            num_records (int): Number of records to fetch. Use -1 to fetch all configured records.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.


        Returns:
            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling information about each waveform:

                -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
                -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
                -  **x_increment** (float) the time between points in the acquired waveform in seconds
                -  **channel** (str) channel name this waveform was acquired from
                -  **record** (int) record number of this waveform
                -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                    .. math::

                        voltage = binary data * gain factor + offset

                -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                    .. math::

                        voltage = binary data * gain factor + offset

                - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

        '''
        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records
            if num_samples is None:
                num_samples = self.horz_record_length

        wfm, wfm_info = self._read(num_samples, timeout)

        if isinstance(wfm, array.ArrayType):
            mv = memoryview(wfm)
        else:
            mv = wfm

        waveform_info._populate_samples_info(wfm_info, mv, num_samples)

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )

        wfm_info_count = len(wfm_info)
        channel_count = len(channel_names)
        # Should this raise instead? If this asserts, is it the users fault?
        assert wfm_info_count % channel_count == 0, 'Number of waveforms should be evenly divisible by the number of channels: len(wfm_info) == {0}, len(channel_names) == {1}'.format(wfm_info_count, channel_count)
        actual_num_records = int(wfm_info_count / channel_count)
        waveform_info._populate_channel_and_record_info(wfm_info, channel_names, range(record_number, record_number + actual_num_records))

        return wfm_info

    @ivi_synchronized
    def _fetch(self, num_samples, timeout=hightime.timedelta(seconds=5.0)):
        r'''_fetch

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This method returns
        scaled voltage waveforms.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note:
        You can use read instead of this method. read
        starts an acquisition on all enabled channels, waits for the acquisition
        to complete, and returns the waveform for the specified channel.

        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            waveform (array.array("d")): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        '''
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        waveform, wfm_info = self._interpreter.fetch(self._repeated_capability, timeout, num_samples)
        return waveform, wfm_info

    @ivi_synchronized
    def _fetch_into_numpy(self, num_samples, waveform, timeout=hightime.timedelta(seconds=5.0)):
        r'''_fetch_into_numpy

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This method returns
        scaled voltage waveforms.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note:
        You can use read instead of this method. read
        starts an acquisition on all enabled channels, waits for the acquisition
        to complete, and returns the waveform for the specified channel.

        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            waveform (numpy.array(dtype=numpy.float64)): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        '''
        import numpy

        if type(waveform) is not numpy.ndarray:
            raise TypeError('waveform must be {0}, is {1}'.format(numpy.ndarray, type(waveform)))
        if numpy.isfortran(waveform) is True:
            raise TypeError('waveform must be in C-order')
        if waveform.dtype is not numpy.dtype('float64'):
            raise TypeError('waveform must be numpy.ndarray of dtype=float64, is ' + str(waveform.dtype))
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        wfm_info = self._interpreter.fetch_into_numpy(self._repeated_capability, num_samples, waveform, timeout)
        return wfm_info

    @ivi_synchronized
    def _fetch_array_measurement(self, array_meas_function, measurement_waveform_size, timeout=hightime.timedelta(seconds=5.0)):
        r'''_fetch_array_measurement

        Obtains a waveform from the digitizer and returns the specified
        measurement array. This method may return multiple waveforms depending
        on the number of channels, the acquisition type, and the number of
        records you specify.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_array_measurement`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch_array_measurement`

        Args:
            array_meas_function (enums.ArrayMeasurement): The `array
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
                to perform.

            measurement_waveform_size (int): The maximum number of samples returned in the measurement waveform array
                for each waveform measurement. Default Value: None (returns all available samples).

                Note:
                Use the property fetch_meas_num_samples to set the
                number of samples to fetch when performing a measurement. For more
                information about when to use this property, refer to the `NI
                KnowledgeBase <javascript:WWW(WWW_KB_MEAS)>`__.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            meas_wfm (list of float): Returns an array whose length is the number of waveforms times
                **measurementWaveformSize**; call _actual_num_wfms to determine the number of
                waveforms; call _actual_meas_wfm_size to determine the size of each
                waveform.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with channel list of 0, 1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        '''
        if type(array_meas_function) is not enums.ArrayMeasurement:
            raise TypeError('Parameter array_meas_function must be of type ' + str(enums.ArrayMeasurement))
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        meas_wfm, wfm_info = self._interpreter.fetch_array_measurement(self._repeated_capability, timeout, array_meas_function, measurement_waveform_size)
        return meas_wfm, wfm_info

    @ivi_synchronized
    def _fetch_binary16_into_numpy(self, num_samples, waveform, timeout=hightime.timedelta(seconds=5.0)):
        r'''_fetch_binary16_into_numpy

        Retrieves data from a previously initiated acquisition and returns
        binary 16-bit waveforms. This method may return multiple waveforms
        depending on the number of channels, the acquisition type, and the
        number of records you specify.

        Refer to `Using Fetch
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on using this method.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_binary16`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch_binary16`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            waveform (numpy.array(dtype=numpy.int16)): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        '''
        import numpy

        if type(waveform) is not numpy.ndarray:
            raise TypeError('waveform must be {0}, is {1}'.format(numpy.ndarray, type(waveform)))
        if numpy.isfortran(waveform) is True:
            raise TypeError('waveform must be in C-order')
        if waveform.dtype is not numpy.dtype('int16'):
            raise TypeError('waveform must be numpy.ndarray of dtype=int16, is ' + str(waveform.dtype))
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        wfm_info = self._interpreter.fetch_binary16_into_numpy(self._repeated_capability, num_samples, waveform, timeout)
        return wfm_info

    @ivi_synchronized
    def _fetch_binary32_into_numpy(self, num_samples, waveform, timeout=hightime.timedelta(seconds=5.0)):
        r'''_fetch_binary32_into_numpy

        Retrieves data from a previously initiated acquisition and returns
        binary 32-bit waveforms. This method may return multiple waveforms
        depending on the number of channels, the acquisition type, and the
        number of records you specify.

        Refer to `Using Fetch
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on using this method.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_binary32`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch_binary32`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            waveform (numpy.array(dtype=numpy.int32)): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        '''
        import numpy

        if type(waveform) is not numpy.ndarray:
            raise TypeError('waveform must be {0}, is {1}'.format(numpy.ndarray, type(waveform)))
        if numpy.isfortran(waveform) is True:
            raise TypeError('waveform must be in C-order')
        if waveform.dtype is not numpy.dtype('int32'):
            raise TypeError('waveform must be numpy.ndarray of dtype=int32, is ' + str(waveform.dtype))
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        wfm_info = self._interpreter.fetch_binary32_into_numpy(self._repeated_capability, num_samples, waveform, timeout)
        return wfm_info

    @ivi_synchronized
    def _fetch_binary8_into_numpy(self, num_samples, waveform, timeout=hightime.timedelta(seconds=5.0)):
        r'''_fetch_binary8_into_numpy

        Retrieves data from a previously initiated acquisition and returns
        binary 8-bit waveforms. This method may return multiple waveforms
        depending on the number of channels, the acquisition type, and the
        number of records you specify.

        Refer to `Using Fetch
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on using this method.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_binary8`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch_binary8`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            waveform (numpy.array(dtype=numpy.int8)): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        '''
        import numpy

        if type(waveform) is not numpy.ndarray:
            raise TypeError('waveform must be {0}, is {1}'.format(numpy.ndarray, type(waveform)))
        if numpy.isfortran(waveform) is True:
            raise TypeError('waveform must be in C-order')
        if waveform.dtype is not numpy.dtype('int8'):
            raise TypeError('waveform must be numpy.ndarray of dtype=int8, is ' + str(waveform.dtype))
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        wfm_info = self._interpreter.fetch_binary8_into_numpy(self._repeated_capability, num_samples, waveform, timeout)
        return wfm_info

    @ivi_synchronized
    def fetch_into(self, waveform, relative_to=enums.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0)):
        '''fetch

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This method returns
        scaled voltage waveforms.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note: Some functionality, such as time stamping, is not supported in all digitizers.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.fetch`

        Args:
            waveform (array.array("d")): numpy array of the appropriate type and size that should be acquired as a 1D array. Size should be **num_samples** times number of waveforms. Call _actual_num_wfms to determine the number of waveforms.

                Types supported are

                - `numpy.float64`
                - `numpy.int8`
                - `numpy.in16`
                - `numpy.int32`

                Example:

                .. code-block:: python

                    waveform = numpy.ndarray(num_samples * session.actual_num_wfms(), dtype=numpy.float64)
                    wfm_info = session['0,1'].fetch_into(waveform, timeout=5.0)

            relative_to (enums.FetchRelativeTo): Position to start fetching within one record.

            offset (int): Offset in samples to start fetching data within each record.The offset can be positive or negative.

            record_number (int): Zero-based index of the first record to fetch.

            num_records (int): Number of records to fetch. Use -1 to fetch all configured records.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling information about each waveform:

                -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
                -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
                -  **x_increment** (float) the time between points in the acquired waveform in seconds
                -  **channel** (str) channel name this waveform was acquired from
                -  **record** (int) record number of this waveform
                -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                    .. math::

                        voltage = binary data * gain factor + offset

                -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                    .. math::

                        voltage = binary data * gain factor + offset

                - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

        '''
        import numpy

        # Set the fetch attributes
        with _NoChannel(session=self):
            self._fetch_relative_to = relative_to
            self._fetch_offset = offset
            self._fetch_record_number = record_number
            self._fetch_num_records = -1 if num_records is None else num_records

        num_samples = int(len(waveform) / self._actual_num_wfms())

        if waveform.dtype == numpy.float64:
            wfm_info = self._fetch_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        elif waveform.dtype == numpy.int8:
            wfm_info = self._fetch_binary8_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        elif waveform.dtype == numpy.int16:
            wfm_info = self._fetch_binary16_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        elif waveform.dtype == numpy.int32:
            wfm_info = self._fetch_binary32_into_numpy(num_samples=num_samples, waveform=waveform, timeout=timeout)
        else:
            raise TypeError("Unsupported dtype. Is {}, expected {}, {}, {}, or {}".format(waveform.dtype, numpy.float64, numpy.int8, numpy.int16, numpy.int32))

        mv = memoryview(waveform)

        waveform_info._populate_samples_info(wfm_info, mv, num_samples)

        channel_names = _converters.expand_channel_string(
            self._repeated_capability,
            self._all_channels_in_session
        )

        wfm_info_count = len(wfm_info)
        channel_count = len(channel_names)
        # Should this raise instead? If this asserts, is it the users fault?
        assert wfm_info_count % channel_count == 0, 'Number of waveforms should be evenly divisible by the number of channels: len(wfm_info) == {0}, len(channel_names) == {1}'.format(wfm_info_count, channel_count)
        actual_num_records = int(wfm_info_count / channel_count)
        waveform_info._populate_channel_and_record_info(wfm_info, channel_names, range(record_number, record_number + actual_num_records))

        return wfm_info

    @ivi_synchronized
    def _fetch_measurement_stats(self, scalar_meas_function, timeout=hightime.timedelta(seconds=5.0)):
        r'''_fetch_measurement_stats

        Obtains a waveform measurement and returns the measurement value. This
        method may return multiple statistical results depending on the number
        of channels, the acquisition type, and the number of records you
        specify.

        You specify a particular measurement type, such as rise time, frequency,
        or voltage peak-to-peak. The waveform on which the digitizer calculates
        the waveform measurement is from an acquisition that you previously
        initiated. The statistics for the specified measurement method are
        returned, where the statistics are updated once every acquisition when
        the specified measurement is fetched by any of the Fetch Measurement
        methods. If a Fetch Measurement method has not been called, this
        method fetches the data on which to perform the measurement. The
        statistics are cleared by calling
        clear_waveform_measurement_stats. Refer to `Using Fetch
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on incorporating fetch methods in your application.

        Many of the measurements use the low, mid, and high reference levels.
        You configure the low, mid, and high references with
        meas_chan_low_ref_level,
        meas_chan_mid_ref_level, and
        meas_chan_high_ref_level to set each channel
        differently.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_measurement_stats`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch_measurement_stats`

        Args:
            scalar_meas_function (enums.ScalarMeasurement): The `scalar
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
                to be performed on each fetched waveform.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            result (list of float): Returns the resulting measurement

            mean (list of float): Returns the mean scalar value, which is obtained by averaging each
                _fetch_measurement_stats call.

            stdev (list of float): Returns the standard deviation of the most recent **numInStats**
                measurements.

            min (list of float): Returns the smallest scalar value acquired (the minimum of the
                **numInStats** measurements).

            max (list of float): Returns the largest scalar value acquired (the maximum of the
                **numInStats** measurements).

            num_in_stats (list of int): Returns the number of times _fetch_measurement_stats has been
                called.

        '''
        if type(scalar_meas_function) is not enums.ScalarMeasurement:
            raise TypeError('Parameter scalar_meas_function must be of type ' + str(enums.ScalarMeasurement))
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        result, mean, stdev, min, max, num_in_stats = self._interpreter.fetch_measurement_stats(self._repeated_capability, timeout, scalar_meas_function)
        return result, mean, stdev, min, max, num_in_stats

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute_id):
        r'''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties. If the property represents an instrument state, this
        method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): The ID of a property.


        Returns:
            value (bool): Returns the current value of the property; pass the address of a
                ViBoolean variable.

        '''
        value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute_id)
        return value

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute_id):
        r'''_get_attribute_vi_int32

        Queries the value of a ViInt32 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties. If the property represents an instrument state, this
        method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): The ID of a property.


        Returns:
            value (int): Returns the current value of the property.

        '''
        value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute_id)
        return value

    @ivi_synchronized
    def _get_attribute_vi_int64(self, attribute_id):
        r'''_get_attribute_vi_int64

        Queries the value of a ViInt64 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties. If the property represents an instrument state, this
        method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute_id (int): The ID of a property.


        Returns:
            value (int): Returns the current value of the property.

        '''
        value = self._interpreter.get_attribute_vi_int64(self._repeated_capability, attribute_id)
        return value

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute_id):
        r'''_get_attribute_vi_real64

        Queries the value of a ViReal64 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties. If the property represents an instrument state, this
        method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): The ID of a property.


        Returns:
            value (float): Returns the current value of the property; pass the address of a
                ViReal64 variable.

        '''
        value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute_id)
        return value

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute_id):
        r'''_get_attribute_vi_string

        Queries the value of a ViString property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties. If the property represents an instrument state, this
        method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        You must provide a ViChar array to serve as a buffer for the value. You
        pass the number of bytes in the buffer as the **bufSize**. If the
        current value of the property, including the terminating NUL byte, is
        larger than the size you indicate in the **bufSize**, the method
        copies (**bufSize** – 1) bytes into the buffer, places an ASCII NUL byte
        at the end of the buffer, and returns the **bufSize** you must pass to
        get the entire value. For example, if the value is 123456 and the
        **bufSize** is 4, the method places 123 into the buffer and returns 7.
        If you want to call this method just to get the required buffer size,
        you can pass 0 for the **bufSize** and VI_NULL for the **value**.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): The ID of a property.


        Returns:
            value (str): The buffer in which the method returns the current value of the
                property; the buffer must be of type ViChar and have at least as many
                bytes as indicated in the **bufSize**.

        '''
        value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute_id)
        return value

    @ivi_synchronized
    def _get_equalization_filter_coefficients(self, number_of_coefficients):
        r'''_get_equalization_filter_coefficients

        Retrieves the custom coefficients for the equalization FIR filter on the
        device. This filter is designed to compensate the input signal for
        artifacts introduced to the signal outside of the digitizer. Because
        this filter is a generic FIR filter, any coefficients are valid.
        Coefficient values should be between +1 and –1.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_equalization_filter_coefficients`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_equalization_filter_coefficients`

        Args:
            number_of_coefficients (int): The number of coefficients being passed in the **coefficients** array.


        Returns:
            coefficients (list of float): The custom coefficients for the equalization FIR filter on the device.
                These coefficients should be between +1 and –1. You can obtain the
                number of coefficients from the
                `equalization_num_coefficients <cviequalization_num_coefficients.html>`__
                property.

        '''
        coefficients = self._interpreter.get_equalization_filter_coefficients(self._repeated_capability, number_of_coefficients)
        return coefficients

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-SCOPE locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, niscope.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    @ivi_synchronized
    def _read(self, num_samples, timeout=hightime.timedelta(seconds=5.0)):
        r'''_read

        Initiates an acquisition, waits for it to complete, and retrieves the
        data. The process is similar to calling _initiate_acquisition,
        acquisition_status, and fetch. The only difference is
        that with read, you enable all channels specified with
        **channelList** before the acquisition; in the other method, you enable
        the channels with configure_vertical.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note:
        Some functionality is not supported in all digitizers. Refer to
        `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._read`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._read`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            waveform (array.array("d")): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        '''
        timeout = _converters.convert_timedelta_to_seconds_real64(timeout)
        waveform, wfm_info = self._interpreter.read(self._repeated_capability, timeout, num_samples)
        return waveform, wfm_info

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute_id, value):
        r'''_set_attribute_vi_boolean

        Sets the value of a ViBoolean property. This is a low-level method
        that you can use to set the values of instrument-specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level methods that set most of the instrument
        properties. Use the high-level driver methods as much as possible
        because they handle order dependencies and multithread locking for you.
        In addition, the high-level methods perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the SetAttribute methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): The ID of a property.

            value (bool): The value that you want to set the property to. Some values might not
                be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_boolean(self._repeated_capability, attribute_id, value)

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute_id, value):
        r'''_set_attribute_vi_int32

        Sets the value of a ViInt32 property. This is a low-level method that
        you can use to set the values of instrument-specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level methods that set most of the instrument
        properties. Use the high-level methods as much as possible because
        they handle order dependencies and multithread locking for you. In
        addition, high-level methods perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): The ID of a property.

            value (int): The value that you want to set the property. Some values might not be
                valid depending on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute_id, value)

    @ivi_synchronized
    def _set_attribute_vi_int64(self, attribute_id, value):
        r'''_set_attribute_vi_int64

        Sets the value of a ViInt64 property. This is a low-level method that
        you can use to set the values of instrument-specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level methods that set most of the instrument
        properties. Use the high-level methods as much as possible because
        they handle order dependencies and multithread locking for you. In
        addition, high-level methods perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute_id (int): The ID of a property.

            value (int): The value that you want to set the property. Some values might not be
                valid depending on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_int64(self._repeated_capability, attribute_id, value)

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute_id, value):
        r'''_set_attribute_vi_real64

        Sets the value of a ViReal64 property. This is a low-level method
        that you can use to set the values of instrument-specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level methods that set most of the instrument
        properties. Use the high-level driver methods as much as possible
        because they handle order dependencies and multithread locking for you.
        In addition, the high-level methods perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): The ID of a property.

            value (float): The value that you want to set the property to. Some values might not
                be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_real64(self._repeated_capability, attribute_id, value)

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute_id, value):
        r'''_set_attribute_vi_string

        Sets the value of a ViString property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level methods that set most of the instrument
        properties. Use the high-level driver methods as much as possible
        because they handle order dependencies and multithread locking for you.
        In addition, the high-level methods perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the SetAttribute methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): The ID of a property.

            value (str): The value that you want to set the property to. Some values might not
                be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_string(self._repeated_capability, attribute_id, value)

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()

    def _error_message(self, error_code):
        r'''_error_message

        Takes the **Error_Code** returned by the instrument driver methods, interprets it, and returns it as a user-readable string.

        Note:
        When using grpc-device, this method will call GetErrorMessage server-side while providing the same interface.

        Args:
            error_code (int): The **error_code** returned from the instrument. The default is 0, indicating VI_SUCCESS.


        Returns:
            error_message (str): The error information formatted into a string.

        '''
        error_message = self._interpreter.error_message(error_code)
        return error_message


class Session(_SessionBase):
    '''An NI-SCOPE session to an NI digitizer.'''

    def __init__(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None):
        r'''An NI-SCOPE session to an NI digitizer.

        Performs the following initialization actions:

        -  Creates a new IVI instrument driver and optionally sets the initial
           state of the following session properties: Range Check, Cache,
           Simulate, Record Value Coercions
        -  Opens a session to the specified device using the interface and
           address you specify for the **resourceName**
        -  Resets the digitizer to a known state if **resetDevice** is set to
           True
        -  Queries the instrument ID and verifies that it is valid for this
           instrument driver if the **IDQuery** is set to True
        -  Returns an instrument handle that you use to identify the instrument
           in all subsequent instrument driver method calls

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
                However, all IVI names, such as logical names, are case-sensitive. If
                you use logical names, driver session names, or virtual names in your
                program, you must make sure that the name you use matches the name in
                the IVI Configuration Store file exactly, without any variations in the
                case of the characters.

                | Specifies the resource name of the device to initialize

                For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
                the device number assigned by MAX, as shown in Example 1.

                For NI-DAQmx devices, the syntax is just the device name specified in
                MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
                in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
                right-clicking on the name in MAX and entering a new name.

                An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx
                device name, as shown in Example 3. This naming convention allows for
                the use of an NI-DAQmx device in an application that was originally
                designed for a Traditional NI-DAQ device. For example, if the
                application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
                MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

                If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
                exists with that same name, the NI-DAQmx device is matched first.

                You can also pass in the name of an IVI logical name or an IVI virtual
                name configured with the IVI Configuration utility, as shown in Example
                5. A logical name identifies a particular virtual instrument. A virtual
                name identifies a specific device and specifies the initial settings for
                the session.

                +---------+--------------------------------------+--------------------------------------------------+
                | Example | Device Type                          | Syntax                                           |
                +=========+======================================+==================================================+
                | 1       | Traditional NI-DAQ device            | DAQ::1 (1 = device number)                       |
                +---------+--------------------------------------+--------------------------------------------------+
                | 2       | NI-DAQmx device                      | myDAQmxDevice (myDAQmxDevice = device name)      |
                +---------+--------------------------------------+--------------------------------------------------+
                | 3       | NI-DAQmx device                      | DAQ::myDAQmxDevice (myDAQmxDevice = device name) |
                +---------+--------------------------------------+--------------------------------------------------+
                | 4       | NI-DAQmx device                      | DAQ::2 (2 = device name)                         |
                +---------+--------------------------------------+--------------------------------------------------+
                | 5       | IVI logical name or IVI virtual name | myLogicalName (myLogicalName = name)             |
                +---------+--------------------------------------+--------------------------------------------------+

            id_query (bool): Specify whether to perform an ID query.

                When you set this parameter to True, NI-SCOPE verifies that the
                device you initialize is a type that it supports.

                When you set this parameter to False, the method initializes the
                device without performing an ID query.

                **Defined Values**

                | True—Perform ID query
                | False—Skip ID query

                **Default Value**: True

            reset_device (bool): Specify whether to reset the device during the initialization process.

                Default Value: True

                **Defined Values**

                True (1)—Reset device

                False (0)—Do not reset device

                Note:
                For the NI 5112, repeatedly resetting the device may cause excessive
                wear on the electromechanical relays. Refer to `NI 5112
                Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
                for recommended programming practices.

            options (dict): Specifies the initial value of certain properties for the session. The
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

            grpc_options (niscope.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (niscope.Session): A session object representing the device.

        '''
        if grpc_options:
            import niscope._grpc_stub_interpreter as _grpc_stub_interpreter
            interpreter = _grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        else:
            interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')

        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            interpreter=interpreter,
            freeze_it=False,
            all_channels_in_session=None
        )
        options = _converters.convert_init_with_options_dictionary(options)

        # Call specified init function
        # Note that _interpreter default-initializes the session handle in its constructor, so that
        # if _init_with_options fails, the error handler can reference it.
        # And then here, once _init_with_options succeeds, we call set_session_handle
        # with the actual session handle.
        self._interpreter.set_session_handle(self._init_with_options(resource_name, id_query, reset_device, options))

        # NI-TClk does not work over NI gRPC Device Server
        if not grpc_options:
            self.tclk = nitclk.SessionReference(self._interpreter.get_session_handle())

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("id_query=" + pp.pformat(id_query))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._interpreter._close_on_exit:
            self.close()

    def initiate(self):
        '''initiate

        Initiates a waveform acquisition.

        After calling this method, the digitizer leaves the Idle state and
        waits for a trigger. The digitizer acquires a waveform for each channel
        you enable with configure_vertical.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Acquisition(self)

    def close(self):
        '''close

        When you are finished using an instrument driver session, you must call
        this method to perform the following actions:

        -  Closes the instrument I/O session.
        -  Destroys the IVI session and all of its properties.
        -  Deallocates any memory resources used by the IVI session.

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Aborts an acquisition and returns the digitizer to the Idle state. Call
        this method if the digitizer times out waiting for a trigger.
        '''
        self._interpreter.abort()

    @ivi_synchronized
    def acquisition_status(self):
        r'''acquisition_status

        Returns status information about the acquisition to the **status**
        output parameter.

        Returns:
            acquisition_status (enums.AcquisitionStatus): Returns whether the acquisition is complete, in progress, or unknown.

                **Defined Values**

                AcquisitionStatus.COMPLETE

                AcquisitionStatus.IN_PROGRESS

                AcquisitionStatus.STATUS_UNKNOWN

        '''
        acquisition_status = self._interpreter.acquisition_status()
        return acquisition_status

    @ivi_synchronized
    def auto_setup(self):
        r'''auto_setup

        Automatically configures the instrument. When you call this method,
        the digitizer senses the input signal and automatically configures many
        of the instrument settings. If a signal is detected on a channel, the
        driver chooses the smallest available vertical range that is larger than
        the signal range. For example, if the signal is a 1.2 V\ :sub:`pk-pk`
        sine wave, and the device supports 1 V and 2 V vertical ranges, the
        driver will choose the 2 V vertical range for that channel.

        If no signal is found on any analog input channel, a warning is
        returned, and all channels are enabled. A channel is considered to have
        a signal present if the signal is at least 10% of the smallest vertical
        range available for that channel.

        The following settings are changed:

        +--------------------+-----------------------------------------------+
        | **General**        |                                               |
        +--------------------+-----------------------------------------------+
        | Acquisition mode   | Normal                                        |
        +--------------------+-----------------------------------------------+
        | Reference clock    | Internal                                      |
        +--------------------+-----------------------------------------------+
        | **Vertical**       |                                               |
        +--------------------+-----------------------------------------------+
        | Vertical coupling  | AC (DC for NI 5621)                           |
        +--------------------+-----------------------------------------------+
        | Vertical bandwidth | Full                                          |
        +--------------------+-----------------------------------------------+
        | Vertical range     | Changed by auto setup                         |
        +--------------------+-----------------------------------------------+
        | Vertical offset    | 0 V                                           |
        +--------------------+-----------------------------------------------+
        | Probe attenuation  | Unchanged by auto setup                       |
        +--------------------+-----------------------------------------------+
        | Input impedance    | Unchanged by auto setup                       |
        +--------------------+-----------------------------------------------+
        | **Horizontal**     |                                               |
        +--------------------+-----------------------------------------------+
        | Sample rate        | Changed by auto setup                         |
        +--------------------+-----------------------------------------------+
        | Min record length  | Changed by auto setup                         |
        +--------------------+-----------------------------------------------+
        | Enforce realtime   | True                                          |
        +--------------------+-----------------------------------------------+
        | Number of Records  | Changed to 1                                  |
        +--------------------+-----------------------------------------------+
        | **Triggering**     |                                               |
        +--------------------+-----------------------------------------------+
        | Trigger type       | Edge if signal present, otherwise immediate   |
        +--------------------+-----------------------------------------------+
        | Trigger channel    | Lowest numbered channel with a signal present |
        +--------------------+-----------------------------------------------+
        | Trigger slope      | Positive                                      |
        +--------------------+-----------------------------------------------+
        | Trigger coupling   | DC                                            |
        +--------------------+-----------------------------------------------+
        | Reference position | 50%                                           |
        +--------------------+-----------------------------------------------+
        | Trigger level      | 50% of signal on trigger channel              |
        +--------------------+-----------------------------------------------+
        | Trigger delay      | 0                                             |
        +--------------------+-----------------------------------------------+
        | Trigger holdoff    | 0                                             |
        +--------------------+-----------------------------------------------+
        | Trigger output     | None                                          |
        +--------------------+-----------------------------------------------+
        '''
        self._interpreter.auto_setup()

    @ivi_synchronized
    def _cal_fetch_date(self, which_one):
        r'''_cal_fetch_date

        TBD

        Args:
            which_one (enums.CalibrationTypes):


        Returns:
            year (int):

            month (int):

            day (int):

        '''
        if type(which_one) is not enums._CalibrationTypes:
            raise TypeError('Parameter which_one must be of type ' + str(enums._CalibrationTypes))
        year, month, day = self._interpreter.cal_fetch_date(which_one)
        return year, month, day

    @ivi_synchronized
    def _cal_fetch_temperature(self, which_one):
        r'''_cal_fetch_temperature

        TBD

        Args:
            which_one (int):


        Returns:
            temperature (float):

        '''
        temperature = self._interpreter.cal_fetch_temperature(which_one)
        return temperature

    @ivi_synchronized
    def commit(self):
        r'''commit

        Commits to hardware all the parameter settings associated with the task.
        Use this method if you want a parameter change to be immediately
        reflected in the hardware. This method is not supported for
        Traditional NI-DAQ (Legacy) devices.
        '''
        self._interpreter.commit()

    @ivi_synchronized
    def configure_horizontal_timing(self, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime):
        r'''configure_horizontal_timing

        Configures the common properties of the horizontal subsystem for a
        multirecord acquisition in terms of minimum sample rate.

        Args:
            min_sample_rate (float): The sampling rate for the acquisition. Refer to
                min_sample_rate for more information.

            min_num_pts (int): The minimum number of points you need in the record for each channel;
                call ActualRecordLength to obtain the actual record length
                used.

                Valid Values: Greater than 1; limited by available memory

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            ref_position (float): The position of the Reference Event in the waveform record specified as
                a percentage.

            num_records (int): The number of records to acquire

            enforce_realtime (bool): Indicates whether the digitizer enforces real-time measurements or
                allows equivalent-time (RIS) measurements; not all digitizers support
                RIS—refer to `Features Supported by
                Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
                more information.

                Default value: True

                **Defined Values**

                True—Allow real-time acquisitions only

                False—Allow real-time and equivalent-time acquisitions

        '''
        self._interpreter.configure_horizontal_timing(min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)

    @ivi_synchronized
    def _configure_ref_levels(self, low=10.0, mid=50.0, high=90.0):
        r'''_configure_ref_levels

        This method is included for compliance with the IviScope Class
        Specification.

        Configures the reference levels for all channels of the digitizer. The
        levels may be set on a per channel basis by setting
        meas_chan_high_ref_level,
        meas_chan_low_ref_level, and
        meas_chan_mid_ref_level

        This method configures the reference levels for waveform measurements.
        Call this method before calling FetchMeasurement to take a
        rise time, fall time, width negative, width positive, duty cycle
        negative, or duty cycle positive measurement.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Args:
            low (float): Pass the low reference you want the digitizer to use for waveform
                measurements.

                Units: Either a percentage or voltage based on
                meas_ref_level_units. A percentage is calculated with
                the voltage low and voltage high measurements representing 0% and 100%,
                respectively.

                Default Value: 10.0

            mid (float): Pass the mid reference you want the digitizer to use for waveform
                measurements.

                Units: Either a percentage or voltage based on
                meas_ref_level_units. A percentage is calculated with
                the voltage low and voltage high measurements representing 0% and 100%,
                respectively.

                Default Value: 50.0

            high (float): Pass the high reference you want the digitizer to use for waveform
                measurements.

                Units: Either a percentage or voltage based on
                meas_ref_level_units. A percentage is calculated with
                the voltage low and voltage high measurements representing 0% and 100%,
                respectively.

                Default Value: 90.0

        '''
        self._interpreter.configure_ref_levels(low, mid, high)

    @ivi_synchronized
    def configure_trigger_digital(self, trigger_source, slope=enums.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):
        r'''configure_trigger_digital

        Configures the common properties of a digital trigger.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) property. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        Note:
        For multirecord acquisitions, all records after the first record are
        started by using the Advance Trigger Source. The default is immediate.

        You can adjust the amount of pre-trigger and post-trigger samples using
        the reference position parameter on the
        configure_horizontal_timing method. The default is half of the
        record length.

        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Digital triggering is not supported in RIS mode.

        Args:
            trigger_source (str): Specifies the trigger source. Refer to trigger_source
                for defined values.

            slope (enums.TriggerSlope): Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to trigger_slope for more
                information.

            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        if type(slope) is not enums.TriggerSlope:
            raise TypeError('Parameter slope must be of type ' + str(enums.TriggerSlope))
        holdoff = _converters.convert_timedelta_to_seconds_real64(holdoff)
        delay = _converters.convert_timedelta_to_seconds_real64(delay)
        self._interpreter.configure_trigger_digital(trigger_source, slope, holdoff, delay)

    @ivi_synchronized
    def configure_trigger_edge(self, trigger_source, level, trigger_coupling, slope=enums.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):
        r'''configure_trigger_edge

        Configures common properties for analog edge triggering.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) property. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        Note:
        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Args:
            trigger_source (str): Specifies the trigger source. Refer to trigger_source
                for defined values.

            level (float): The voltage threshold for the trigger. Refer to
                trigger_level for more information.

            trigger_coupling (enums.TriggerCoupling): Applies coupling and filtering options to the trigger signal. Refer to
                trigger_coupling for more information.

            slope (enums.TriggerSlope): Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to trigger_slope for more
                information.

            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        if type(slope) is not enums.TriggerSlope:
            raise TypeError('Parameter slope must be of type ' + str(enums.TriggerSlope))
        if type(trigger_coupling) is not enums.TriggerCoupling:
            raise TypeError('Parameter trigger_coupling must be of type ' + str(enums.TriggerCoupling))
        holdoff = _converters.convert_timedelta_to_seconds_real64(holdoff)
        delay = _converters.convert_timedelta_to_seconds_real64(delay)
        self._interpreter.configure_trigger_edge(trigger_source, level, slope, trigger_coupling, holdoff, delay)

    @ivi_synchronized
    def configure_trigger_hysteresis(self, trigger_source, level, hysteresis, trigger_coupling, slope=enums.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):
        r'''configure_trigger_hysteresis

        Configures common properties for analog hysteresis triggering. This kind
        of trigger specifies an additional value, specified in the
        **hysteresis** parameter, that a signal must pass through before a
        trigger can occur. This additional value acts as a kind of buffer zone
        that keeps noise from triggering an acquisition.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the
        acq_arm_source. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        Note:
        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Args:
            trigger_source (str): Specifies the trigger source. Refer to trigger_source
                for defined values.

            level (float): The voltage threshold for the trigger. Refer to
                trigger_level for more information.

            hysteresis (float): The size of the hysteresis window on either side of the **level** in
                volts; the digitizer triggers when the trigger signal passes through the
                hysteresis value you specify with this parameter, has the slope you
                specify with **slope**, and passes through the **level**. Refer to
                trigger_hysteresis for defined values.

            trigger_coupling (enums.TriggerCoupling): Applies coupling and filtering options to the trigger signal. Refer to
                trigger_coupling for more information.

            slope (enums.TriggerSlope): Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to trigger_slope for more
                information.

            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        if type(slope) is not enums.TriggerSlope:
            raise TypeError('Parameter slope must be of type ' + str(enums.TriggerSlope))
        if type(trigger_coupling) is not enums.TriggerCoupling:
            raise TypeError('Parameter trigger_coupling must be of type ' + str(enums.TriggerCoupling))
        holdoff = _converters.convert_timedelta_to_seconds_real64(holdoff)
        delay = _converters.convert_timedelta_to_seconds_real64(delay)
        self._interpreter.configure_trigger_hysteresis(trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay)

    @ivi_synchronized
    def configure_trigger_immediate(self):
        r'''configure_trigger_immediate

        Configures common properties for immediate triggering. Immediate
        triggering means the digitizer triggers itself.

        When you initiate an acquisition, the digitizer waits for a trigger. You
        specify the type of trigger that the digitizer waits for with a
        Configure Trigger method, such as configure_trigger_immediate.
        '''
        self._interpreter.configure_trigger_immediate()

    @ivi_synchronized
    def configure_trigger_software(self, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):
        r'''configure_trigger_software

        Configures common properties for software triggering.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) property. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        To trigger the acquisition, use send_software_trigger_edge.

        Note:
        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Args:
            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        holdoff = _converters.convert_timedelta_to_seconds_real64(holdoff)
        delay = _converters.convert_timedelta_to_seconds_real64(delay)
        self._interpreter.configure_trigger_software(holdoff, delay)

    @ivi_synchronized
    def configure_trigger_video(self, trigger_source, signal_format, event, polarity, trigger_coupling, enable_dc_restore=False, line_number=1, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):
        r'''configure_trigger_video

        Configures the common properties for video triggering, including the
        signal format, TV event, line number, polarity, and enable DC restore. A
        video trigger occurs when the digitizer finds a valid video signal sync.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) property. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        Note:
        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Args:
            trigger_source (str): Specifies the trigger source. Refer to trigger_source
                for defined values.

            signal_format (enums.VideoSignalFormat): Specifies the type of video signal sync the digitizer should look for.
                Refer to tv_trigger_signal_format for more
                information.

            event (enums.VideoTriggerEvent): Specifies the TV event you want to trigger on. You can trigger on a
                specific or on the next coming line or field of the signal.

            polarity (enums.VideoPolarity): Specifies the polarity of the video signal sync.

            trigger_coupling (enums.TriggerCoupling): Applies coupling and filtering options to the trigger signal. Refer to
                trigger_coupling for more information.

            enable_dc_restore (bool): Offsets each video line so the clamping level (the portion of the video
                line between the end of the color burst and the beginning of the active
                image) is moved to zero volt. Refer to
                enable_dc_restore for defined values.

            line_number (int): Selects the line number to trigger on. The line number range covers an
                entire frame and is referenced as shown on `Vertical Blanking and
                Synchronization
                Signal <REPLACE_DRIVER_SPECIFIC_URL_1(gray_scale_image)>`__. Refer to
                tv_trigger_line_number for more information.

                Default value: 1

            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        if type(signal_format) is not enums.VideoSignalFormat:
            raise TypeError('Parameter signal_format must be of type ' + str(enums.VideoSignalFormat))
        if type(event) is not enums.VideoTriggerEvent:
            raise TypeError('Parameter event must be of type ' + str(enums.VideoTriggerEvent))
        if type(polarity) is not enums.VideoPolarity:
            raise TypeError('Parameter polarity must be of type ' + str(enums.VideoPolarity))
        if type(trigger_coupling) is not enums.TriggerCoupling:
            raise TypeError('Parameter trigger_coupling must be of type ' + str(enums.TriggerCoupling))
        holdoff = _converters.convert_timedelta_to_seconds_real64(holdoff)
        delay = _converters.convert_timedelta_to_seconds_real64(delay)
        self._interpreter.configure_trigger_video(trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay)

    @ivi_synchronized
    def configure_trigger_window(self, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):
        r'''configure_trigger_window

        Configures common properties for analog window triggering. A window
        trigger occurs when a signal enters or leaves a window you specify with
        the **high level** or **low level** parameters.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) property. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        To trigger the acquisition, use send_software_trigger_edge.

        Note: Some features are not supported by all digitizers.

        Args:
            trigger_source (str): Specifies the trigger source. Refer to trigger_source
                for defined values.

            low_level (float): Passes the voltage threshold you want the digitizer to use for low
                triggering.

            high_level (float): Passes the voltage threshold you want the digitizer to use for high
                triggering.

            window_mode (enums.TriggerWindowMode): Specifies whether you want the trigger to occur when the signal enters
                or leaves a window.

            trigger_coupling (enums.TriggerCoupling): Applies coupling and filtering options to the trigger signal. Refer to
                trigger_coupling for more information.

            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        if type(window_mode) is not enums.TriggerWindowMode:
            raise TypeError('Parameter window_mode must be of type ' + str(enums.TriggerWindowMode))
        if type(trigger_coupling) is not enums.TriggerCoupling:
            raise TypeError('Parameter trigger_coupling must be of type ' + str(enums.TriggerCoupling))
        holdoff = _converters.convert_timedelta_to_seconds_real64(holdoff)
        delay = _converters.convert_timedelta_to_seconds_real64(delay)
        self._interpreter.configure_trigger_window(trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay)

    @ivi_synchronized
    def disable(self):
        r'''disable

        Aborts any current operation, opens data channel relays, and releases
        RTSI and PFI lines.
        '''
        self._interpreter.disable()

    @ivi_synchronized
    def export_attribute_configuration_buffer(self):
        r'''export_attribute_configuration_buffer

        Exports the property configuration of the session to a configuration
        buffer.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑SCOPE returns an
        error.

        **Related Topics:**

        `Properties and Property
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Returns:
            configuration (bytes): Specifies the byte array buffer to be populated with the exported
                property configuration.

        '''
        configuration = self._interpreter.export_attribute_configuration_buffer()
        return _converters.convert_to_bytes(configuration)

    @ivi_synchronized
    def export_attribute_configuration_file(self, file_path):
        r'''export_attribute_configuration_file

        Exports the property configuration of the session to the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑SCOPE returns an
        error.

        **Related Topics:**

        `Properties and Property
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Args:
            file_path (str): Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .niscopeconfig

        '''
        self._interpreter.export_attribute_configuration_file(file_path)

    @ivi_synchronized
    def get_ext_cal_last_date_and_time(self):
        '''get_ext_cal_last_date_and_time

        Returns the date and time of the last external calibration performed.

        Returns:
            last_cal_datetime (hightime.timedelta, datetime.timedelta, or float in seconds): Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.

        '''

        year, month, day = self._cal_fetch_date(enums._CalibrationTypes.EXTERNAL)
        return hightime.datetime(year, month, day)

    @ivi_synchronized
    def get_ext_cal_last_temp(self):
        '''get_ext_cal_last_temp

        Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful external calibration.
        The temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.
        Temperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.

        Returns:
            temperature (float): Returns the **temperature** in degrees Celsius during the last calibration.

        '''

        return self._cal_fetch_temperature(enums._CalibrationTypes.EXTERNAL.value)

    @ivi_synchronized
    def get_self_cal_last_date_and_time(self):
        '''get_self_cal_last_date_and_time

        Returns the date and time of the last self calibration performed.

        Returns:
            last_cal_datetime (hightime.timedelta, datetime.timedelta, or float in seconds): Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.

        '''

        year, month, day = self._cal_fetch_date(enums._CalibrationTypes.SELF)
        return hightime.datetime(year, month, day)

    @ivi_synchronized
    def get_self_cal_last_temp(self):
        '''get_self_cal_last_temp

        Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful self calibration.
        The temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.
        Temperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.

        Returns:
            temperature (float): Returns the **temperature** in degrees Celsius during the last calibration.

        '''

        return self._cal_fetch_temperature(enums._CalibrationTypes.SELF.value)

    @ivi_synchronized
    def get_channel_names(self, indices):
        r'''get_channel_names

        Returns a list of channel names for given channel indices.

        Args:
            indices (basic sequence types, str, or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0", "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        '''
        indices = _converters.convert_repeated_capabilities_without_prefix(indices)
        names = self._interpreter.get_channel_names(indices)
        return _converters.convert_comma_separated_string_to_list(names)

    @ivi_synchronized
    def import_attribute_configuration_buffer(self, configuration):
        r'''import_attribute_configuration_buffer

        Imports a property configuration to the session from the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        **Related Topics:**

        `Properties and Property
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note:
        You cannot call this method while the session is in a running state,
        such as while acquiring a signal.

        Args:
            configuration (bytes): Specifies the byte array buffer that contains the property
                configuration to import.

        '''
        configuration = _converters.convert_to_bytes(configuration)
        self._interpreter.import_attribute_configuration_buffer(configuration)

    @ivi_synchronized
    def import_attribute_configuration_file(self, file_path):
        r'''import_attribute_configuration_file

        Imports a property configuration to the session from the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        **Related Topics:**

        `Properties and Property
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note:
        You cannot call this method while the session is in a running state,
        such as while acquiring a signal.

        Args:
            file_path (str): Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .niscopeconfig

        '''
        self._interpreter.import_attribute_configuration_file(file_path)

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=""):
        r'''_init_with_options

        Performs the following initialization actions:

        -  Creates a new IVI instrument driver and optionally sets the initial
           state of the following session properties: Range Check, Cache,
           Simulate, Record Value Coercions
        -  Opens a session to the specified device using the interface and
           address you specify for the **resourceName**
        -  Resets the digitizer to a known state if **resetDevice** is set to
           True
        -  Queries the instrument ID and verifies that it is valid for this
           instrument driver if the **IDQuery** is set to True
        -  Returns an instrument handle that you use to identify the instrument
           in all subsequent instrument driver method calls

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
                However, all IVI names, such as logical names, are case-sensitive. If
                you use logical names, driver session names, or virtual names in your
                program, you must make sure that the name you use matches the name in
                the IVI Configuration Store file exactly, without any variations in the
                case of the characters.

                | Specifies the resource name of the device to initialize

                For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
                the device number assigned by MAX, as shown in Example 1.

                For NI-DAQmx devices, the syntax is just the device name specified in
                MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
                in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
                right-clicking on the name in MAX and entering a new name.

                An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx
                device name, as shown in Example 3. This naming convention allows for
                the use of an NI-DAQmx device in an application that was originally
                designed for a Traditional NI-DAQ device. For example, if the
                application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
                MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

                If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
                exists with that same name, the NI-DAQmx device is matched first.

                You can also pass in the name of an IVI logical name or an IVI virtual
                name configured with the IVI Configuration utility, as shown in Example
                5. A logical name identifies a particular virtual instrument. A virtual
                name identifies a specific device and specifies the initial settings for
                the session.

                +---------+--------------------------------------+--------------------------------------------------+
                | Example | Device Type                          | Syntax                                           |
                +=========+======================================+==================================================+
                | 1       | Traditional NI-DAQ device            | DAQ::1 (1 = device number)                       |
                +---------+--------------------------------------+--------------------------------------------------+
                | 2       | NI-DAQmx device                      | myDAQmxDevice (myDAQmxDevice = device name)      |
                +---------+--------------------------------------+--------------------------------------------------+
                | 3       | NI-DAQmx device                      | DAQ::myDAQmxDevice (myDAQmxDevice = device name) |
                +---------+--------------------------------------+--------------------------------------------------+
                | 4       | NI-DAQmx device                      | DAQ::2 (2 = device name)                         |
                +---------+--------------------------------------+--------------------------------------------------+
                | 5       | IVI logical name or IVI virtual name | myLogicalName (myLogicalName = name)             |
                +---------+--------------------------------------+--------------------------------------------------+

            id_query (bool): Specify whether to perform an ID query.

                When you set this parameter to True, NI-SCOPE verifies that the
                device you initialize is a type that it supports.

                When you set this parameter to False, the method initializes the
                device without performing an ID query.

                **Defined Values**

                | True—Perform ID query
                | False—Skip ID query

                **Default Value**: True

            reset_device (bool): Specify whether to reset the device during the initialization process.

                Default Value: True

                **Defined Values**

                True (1)—Reset device

                False (0)—Do not reset device

                Note:
                For the NI 5112, repeatedly resetting the device may cause excessive
                wear on the electromechanical relays. Refer to `NI 5112
                Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
                for recommended programming practices.

            option_string (dict): | Specifies initialization commands. The following table lists the
                  properties and the name you use in the **optionString** to identify
                  the property.

                Default Values: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"

                You can use the option string to simulate a device. The DriverSetup flag
                specifies the model that is to be simulated and the type of the model.
                One example to simulate an NI PXI-5102 would be as follows:

                Option String: Simulate = 1, DriverSetup = Model:5102; BoardType:PXI

                Refer to the example niScope EX Simulated Acquisition for more
                information on simulation.

                You can also use the option string to attach an accessory such as the
                NI 5900 to your digitizer session to allow the seamless use of the
                accessory:

                Option String: DriverSetup = Accessory:Dev1

                Refer to the example niScope EX External Amplifier for more information.


        Returns:
            vi (int): Returns a session handle that you can use to identify the device in all
                subsequent NI-SCOPE method calls.

        '''
        option_string = _converters.convert_init_with_options_dictionary(option_string)
        vi = self._interpreter.init_with_options(resource_name, id_query, reset_device, option_string)
        return vi

    @ivi_synchronized
    def _initiate_acquisition(self):
        r'''_initiate_acquisition

        Initiates a waveform acquisition.

        After calling this method, the digitizer leaves the Idle state and
        waits for a trigger. The digitizer acquires a waveform for each channel
        you enable with configure_vertical.
        '''
        self._interpreter.initiate_acquisition()

    @ivi_synchronized
    def probe_compensation_signal_start(self):
        r'''probe_compensation_signal_start

        Starts the 1 kHz square wave output on PFI 1 for probe compensation.
        '''
        self._interpreter.probe_compensation_signal_start()

    @ivi_synchronized
    def probe_compensation_signal_stop(self):
        r'''probe_compensation_signal_stop

        Stops the 1 kHz square wave output on PFI 1 for probe compensation.
        '''
        self._interpreter.probe_compensation_signal_stop()

    @ivi_synchronized
    def reset_device(self):
        r'''reset_device

        Performs a hard reset of the device. Acquisition stops, all routes are
        released, RTSI and PFI lines are tristated, hardware is configured to
        its default state, and all session properties are reset to their default
        state.

        -  `Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__
        '''
        self._interpreter.reset_device()

    @ivi_synchronized
    def reset_with_defaults(self):
        r'''reset_with_defaults

        Performs a software reset of the device, returning it to the default
        state and applying any initial default settings from the IVI
        Configuration Store.
        '''
        self._interpreter.reset_with_defaults()

    @ivi_synchronized
    def send_software_trigger_edge(self, which_trigger):
        r'''send_software_trigger_edge

        Sends the selected trigger to the digitizer. Call this method if you
        called configure_trigger_software when you want the Reference
        trigger to occur. You can also call this method to override a misused
        edge, digital, or hysteresis trigger. If you have configured
        acq_arm_source, arm_ref_trig_src, or
        adv_trig_src, call this method when you want to send
        the corresponding trigger to the digitizer.

        Args:
            which_trigger (enums.WhichTrigger): Specifies the type of trigger to send to the digitizer.

                **Defined Values**

                | WhichTrigger.START (0L)
                |  WhichTrigger.ARM_REFERENCE (1L)
                | WhichTrigger.REFERENCE (2L)
                | WhichTrigger.ADVANCE (3L)

        '''
        if type(which_trigger) is not enums.WhichTrigger:
            raise TypeError('Parameter which_trigger must be of type ' + str(enums.WhichTrigger))
        self._interpreter.send_software_trigger_edge(which_trigger)

    def _close(self):
        r'''_close

        When you are finished using an instrument driver session, you must call
        this method to perform the following actions:

        -  Closes the instrument I/O session.
        -  Destroys the IVI session and all of its properties.
        -  Deallocates any memory resources used by the IVI session.
        '''
        self._interpreter.close()

    @ivi_synchronized
    def self_test(self):
        '''self_test

        Runs the instrument self-test routine and returns the test result(s). Refer to the
        device-specific help topics for an explanation of the message contents.

        Raises `SelfTestError` on self test failure. Properties on exception object:

        - code - failure code from driver
        - message - status message from driver

        +----------------+------------------+
        | Self-Test Code | Description      |
        +================+==================+
        | 0              | Passed self-test |
        +----------------+------------------+
        | 1              | Self-test failed |
        +----------------+------------------+
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def reset(self):
        r'''reset

        Stops the acquisition, releases routes, and all session properties are
        reset to their `default
        states <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cviattribute_defaults)>`__.
        '''
        self._interpreter.reset()

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Runs the instrument self-test routine and returns the test result(s).

        Returns:
            self_test_result (int): This control contains the value returned from the instrument self-test.

                **Self-Test Code Description**

                0—Self-test passed

                1—Self-test failed

            self_test_message (str): Returns the self-test response string from the instrument. Refer to the
                device-specific help topics for an explanation of the string contents;
                you must pass a ViChar array at least IVI_MAX_MESSAGE_BUF_SIZE bytes
                in length.

        '''
        self_test_result, self_test_message = self._interpreter.self_test()
        return self_test_result, self_test_message
