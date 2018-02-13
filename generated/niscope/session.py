# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes
import struct  # noqa: F401

from niscope import _converters  # noqa: F401   TODO(texasaggie97) remove noqa once we are using converters everywhere
from niscope import attributes
from niscope import enums
from niscope import errors
from niscope import library_singleton
from niscope import visatype

from niscope import waveform_info  # noqa: F401

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


class _Acquisition(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._session._initiate_acquisition()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


class _RepeatedCapabilities(object):
    def __init__(self, session, prefix):
        self._session = session
        self._prefix = prefix

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)

        return _SessionBase(vi=self._session._vi, repeated_capability=rep_caps, library=self._session._library, encoding=self._session._encoding, freeze_it=True)


class _SessionBase(object):
    '''Base class for all NI-SCOPE sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    _5102_adjust_pretrigger_samples = attributes.AttributeViBoolean(1150085)
    '''Type: bool

    When set to true and the digitizer is set to master, the number of pretrigger samples  and total samples are adjusted to be able to synchronize a master and slave 5102.
    '''
    _5v_out_output_terminal = attributes.AttributeViString(1150129)
    '''Type: str

    Specifies the destination for the 5 Volt signal.
    Consult your device documentation for a specific list of valid destinations.
    '''
    absolute_sample_clock_offset = attributes.AttributeViReal64(1150374)
    '''Type: float

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
    accessory_gain = attributes.AttributeViReal64(1150279)
    '''Type: float

    Returns the calibration gain for the current device configuration.
    **Related topics:**
    `NI 5122/5124/5142
    Calibration <digitizers.chm::/5122_Calibration.html>`__

    Note:
    This property is only supported by the NI PXI-5900 differential
    amplifier.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    accessory_gain.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    accessory_gain.Session instance, and calling set/get value on the result.:

        session['0,1'].accessory_gain = var
        var = session['0,1'].accessory_gain
    '''
    accessory_offset = attributes.AttributeViReal64(1150280)
    '''Type: float

    Returns the calibration offset for the current device configuration.
    **Related topics:**
    `NI 5122/5124/5142
    Calibration <digitizers.chm::/5122_Calibration.html>`__

    Note:
    This property is supported only by the NI PXI-5900 differential
    amplifier.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    accessory_offset.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    accessory_offset.Session instance, and calling set/get value on the result.:

        session['0,1'].accessory_offset = var
        var = session['0,1'].accessory_offset
    '''
    acquisition_start_time = attributes.AttributeViReal64(1250109)
    '''Type: float

    Specifies the length of time from the trigger event to the first point in  the waveform record in seconds.  If the value is positive, the first point  in the waveform record occurs after the trigger event (same as specifying  NISCOPE_ATTR_TRIGGER_DELAY_TIME).  If the value is negative, the first point  in the waveform record occurs before the trigger event (same as specifying  NISCOPE_ATTR_HORZ_RECORD_REF_POSITION).
    '''
    acquisition_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.AcquisitionType, 1250101)
    '''Type: enums.AcquisitionType

    Specifies how the digitizer acquires data and fills the waveform record.
    '''
    acq_arm_source = attributes.AttributeViString(1150053)
    '''Type: str

    Specifies the source the digitizer monitors for a start (acquisition arm) trigger.   When the start trigger is received, the digitizer begins acquiring pretrigger  samples.
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
    '''
    adv_trig_src = attributes.AttributeViString(1150094)
    '''Type: str

    Specifies the source the digitizer monitors for an advance trigger.   When the advance trigger is received, the digitizer begins acquiring pretrigger  samples.
    '''
    allow_more_records_than_memory = attributes.AttributeViBoolean(1150068)
    '''Type: bool

    Indicates whether more records can be configured with niScope_ConfigureHorizontalTiming  than fit in the onboard memory. If this attribute is set to VI_TRUE, it is necessary  to fetch records while the acquisition is in progress.  Eventually, some of  the records will be overwritten.  An error is returned from the fetch function  if you attempt to fetch a record that has been overwritten.
    '''
    arm_ref_trig_src = attributes.AttributeViString(1150095)
    '''Type: str

    Specifies the source the digitizer monitors for an arm reference trigger.   When the arm reference trigger is received, the digitizer begins looking for a  reference (stop) trigger from the user-configured trigger source.
    '''
    backlog = attributes.AttributeViReal64(1150084)
    '''Type: float

    Returns the number of samples (NISCOPE_ATTR_POINTS_DONE) that have been acquired but not fetched  for the record specified by NISCOPE_ATTR_FETCH_RECORD_NUMBER.
    '''
    bandpass_filter_enabled = attributes.AttributeViBoolean(1150318)
    '''Type: bool

    Enables the bandpass filter on the specificed channel.  The default value is FALSE.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    bandpass_filter_enabled.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    bandpass_filter_enabled.Session instance, and calling set/get value on the result.:

        session['0,1'].bandpass_filter_enabled = var
        var = session['0,1'].bandpass_filter_enabled
    '''
    binary_sample_width = attributes.AttributeViInt32(1150005)
    '''Type: int

    Indicates the bit width of the binary data in the acquired waveform.  Useful for determining which Binary Fetch function to use. Compare to NISCOPE_ATTR_RESOLUTION.
    To configure the device to store samples with a lower resolution that the native, set this attribute to the desired binary width.
    This can be useful for streaming at faster speeds at the cost of resolution. The least significant bits will be lost with this configuration.
    Valid Values: 8, 16, 32
    '''
    cache = attributes.AttributeViBoolean(1050004)
    '''Type: bool

    Specifies whether to cache the value of attributes.  When caching is  enabled, the instrument driver keeps track of the current instrument  settings and avoids sending redundant commands to the instrument.  Thus,  you can significantly increase execution speed.
    The instrument driver can choose to always cache or to never cache  particular attributes regardless of the setting of this attribute.
    The default value is VI_TRUE.   Use niScope_InitWithOptions  to override this value.
    '''
    channel_count = attributes.AttributeViInt32(1050203)
    '''Type: int

    Indicates the number of channels that the specific instrument driver  supports.
    For channel-based properties, the IVI engine maintains a separate cache value for each channel.
    '''
    channel_enabled = attributes.AttributeViBoolean(1250005)
    '''Type: bool

    Specifies whether the digitizer acquires a waveform for the channel.
    Valid Values:
    VI_TRUE  (1) - Acquire data on this channel
    VI_FALSE (0) - Don't acquire data on this channel

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    channel_enabled.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    channel_enabled.Session instance, and calling set/get value on the result.:

        session['0,1'].channel_enabled = var
        var = session['0,1'].channel_enabled
    '''
    channel_terminal_configuration = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TerminalConfiguration, 1150107)
    '''Type: enums.TerminalConfiguration

    Specifies the terminal configuration for the channel.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    channel_terminal_configuration.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    channel_terminal_configuration.Session instance, and calling set/get value on the result.:

        session['0,1'].channel_terminal_configuration = var
        var = session['0,1'].channel_terminal_configuration
    '''
    clock_sync_pulse_source = attributes.AttributeViString(1150007)
    '''Type: str

    For the NI 5102, specifies the line on which the sample clock is sent or received. For the NI 5112/5620/5621/5911,  specifies the line on which the one-time sync pulse is sent or received. This line should be the same for all devices to be synchronized.
    '''
    data_transfer_block_size = attributes.AttributeViInt32(1150316)
    '''Type: int

    Specifies the maximum number of samples to transfer at one time from the device to host memory. Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may also increase the amount of page-locked memory required from the system.
    '''
    data_transfer_maximum_bandwidth = attributes.AttributeViReal64(1150321)
    '''Type: float

    This property specifies the maximum bandwidth that the device is allowed to consume.
    '''
    data_transfer_preferred_packet_size = attributes.AttributeViInt32(1150322)
    '''Type: int

    This property specifies the size of (read request|memory write) data payload. Due to alignment of the data buffers, the hardware may not always generate a packet of this size.
    '''
    ddc_center_frequency = attributes.AttributeViReal64(1150303)
    '''Type: float

    The frequency at which the DDC block frequency translates the input data.
    Default Value: 10 MHz

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    ddc_center_frequency.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    ddc_center_frequency.Session instance, and calling set/get value on the result.:

        session['0,1'].ddc_center_frequency = var
        var = session['0,1'].ddc_center_frequency
    '''
    ddc_data_processing_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DataProcessingMode, 1150304)
    '''Type: enums.DataProcessingMode

    The way in which data is processed by the DDC block.
    Valid Values:
    Real (0)
    Complex (1)
    Default Value: Complex
    '''
    ddc_enabled = attributes.AttributeViBoolean(1150300)
    '''Type: bool

    Enables/disables the Digital Down Converter (DDC) block of the digitizer.  When the DDC block is disabled, all DDC-related properties are disabled and  have no effect on the acquired signal.
    Default Value: VI_FALSE

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    ddc_enabled.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    ddc_enabled.Session instance, and calling set/get value on the result.:

        session['0,1'].ddc_enabled = var
        var = session['0,1'].ddc_enabled
    '''
    ddc_frequency_translation_enabled = attributes.AttributeViBoolean(1150302)
    '''Type: bool

    Enables/disables frequency translating the data around the user-selected center  frequency down to baseband.
    Default Value: VI_TRUE

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    ddc_frequency_translation_enabled.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    ddc_frequency_translation_enabled.Session instance, and calling set/get value on the result.:

        session['0,1'].ddc_frequency_translation_enabled = var
        var = session['0,1'].ddc_frequency_translation_enabled
    '''
    ddc_frequency_translation_phase_i = attributes.AttributeViReal64(1150305)
    '''Type: float

    The I center frequency phase in degrees at the first point of the acquisition.
    Default Value: 0

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    ddc_frequency_translation_phase_i.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    ddc_frequency_translation_phase_i.Session instance, and calling set/get value on the result.:

        session['0,1'].ddc_frequency_translation_phase_i = var
        var = session['0,1'].ddc_frequency_translation_phase_i
    '''
    ddc_frequency_translation_phase_q = attributes.AttributeViReal64(1150306)
    '''Type: float

    The Q center frequency phase in degrees at the first point of the acquisition.  Use this attribute only when NISCOPE_ATTR_DDC_DATA_PROCESSING_MODE is set to Complex.
    Default Value: 90

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    ddc_frequency_translation_phase_q.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    ddc_frequency_translation_phase_q.Session instance, and calling set/get value on the result.:

        session['0,1'].ddc_frequency_translation_phase_q = var
        var = session['0,1'].ddc_frequency_translation_phase_q
    '''
    ddc_q_source = attributes.AttributeViString(1150310)
    '''Type: str

    Indicates the channel that is the input of the Q path of the DDC.
    Default Value: The channel that the attribute is configured off of.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    ddc_q_source.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    ddc_q_source.Session instance, and calling set/get value on the result.:

        session['0,1'].ddc_q_source = var
        var = session['0,1'].ddc_q_source
    '''
    device_number = attributes.AttributeViInt32(1150076)
    '''Type: int

    Indicates the device number associated with the current session.
    '''
    device_temperature = attributes.AttributeViReal64(1150086)
    '''Type: float

    Returns the temperature of the device in degrees Celsius from the onboard sensor.
    '''
    digital_gain = attributes.AttributeViReal64(1150307)
    '''Type: float

    Applies gain to the specified channel in hardware before any onboard processing.
    Valid Values:
    -1.5 to 1.5

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    digital_gain.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    digital_gain.Session instance, and calling set/get value on the result.:

        session['0,1'].digital_gain = var
        var = session['0,1'].digital_gain
    '''
    digital_offset = attributes.AttributeViReal64(1150308)
    '''Type: float

    Applies offset to the specified channel in hardware before any onboard processing.
    Valid Values:
    -1.5 to 1.5 V

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    digital_offset.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    digital_offset.Session instance, and calling set/get value on the result.:

        session['0,1'].digital_offset = var
        var = session['0,1'].digital_offset
    '''
    dither_enabled = attributes.AttributeViBoolean(1150319)
    '''Type: bool

    Enables or Disables the analog dither on the device.  The default value is FALSE.
    Using dither can improve the spectral performance of the device by reducing the effects of quantization.  However, adding dither increases the power level to the ADC, so you may need to either decrease the signal level or increase your vertical range.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    dither_enabled.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    dither_enabled.Session instance, and calling set/get value on the result.:

        session['0,1'].dither_enabled = var
        var = session['0,1'].dither_enabled
    '''
    driver_setup = attributes.AttributeViString(1050007)
    '''Type: str

    This attribute indicates the Driver Setup string that the user  specified when initializing the driver.
    Some cases exist where the end-user must specify instrument driver  options at initialization.  An example of this is specifying  a particular instrument model from among a family of instruments  that the driver supports.  This is useful when using simulation.   The end-user can specify driver-specific options through  the DriverSetup keyword in the optionsString parameter in  niScope_InitWithOptions, or through the IVI Configuration Utility.
    If the user does not specify a Driver Setup string, this attribute returns an empty string.
    '''
    enable_dc_restore = attributes.AttributeViBoolean(1150093)
    '''Type: bool

    Restores the video-triggered data retrieved by the digitizer to the video signal's zero reference point.
    Valid Values:
    VI_TRUE - Enable DC restore
    VI_FALSE - Disable DC restore
    '''
    enable_time_interleaved_sampling = attributes.AttributeViBoolean(1150128)
    '''Type: bool

    Specifies whether the digitizer acquires the waveform using multiple ADCs for the channel  enabling a higher maximum real-time sampling rate.
    Valid Values:
    VI_TRUE  (1) - Use multiple interleaved ADCs on this channel
    VI_FALSE (0) - Use only this channel's ADC to acquire data for this channel

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    enable_time_interleaved_sampling.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    enable_time_interleaved_sampling.Session instance, and calling set/get value on the result.:

        session['0,1'].enable_time_interleaved_sampling = var
        var = session['0,1'].enable_time_interleaved_sampling
    '''
    end_of_acquisition_event_output_terminal = attributes.AttributeViString(1150101)
    '''Type: str

    Specifies the destination for the End of Acquisition Event.    When this event is asserted, the digitizer has completed sampling for all records.
    Consult your device documentation for a specific list of valid destinations.
    '''
    end_of_record_event_output_terminal = attributes.AttributeViString(1150099)
    '''Type: str

    Specifies the destination for the End of Record Event.    When this event is asserted, the digitizer has completed sampling for the current record.
    Consult your device documentation for a specific list of valid destinations.
    '''
    end_of_record_to_advance_trigger_holdoff = attributes.AttributeViReal64(1150366)
    '''Type: float

    End of Record to Advance Trigger Holdoff is the length of time (in
    seconds) that a device waits between the completion of one record and
    the acquisition of pre-trigger samples for the next record. During this
    time, the acquisition engine state delays the transition to the Wait for
    Advance Trigger state, and will not store samples in onboard memory,
    accept an Advance Trigger, or trigger on the input signal..
    **Supported Devices**: NI 5185/5186
    '''
    equalization_filter_enabled = attributes.AttributeViBoolean(1150313)
    '''Type: bool

    Enables the onboard signal processing FIR block. This block is connected directly to the input signal.  This filter is designed to compensate the input signal for artifacts introduced to the signal outside  of the digitizer. However, since this is a generic FIR filter any coefficients are valid.  Coefficients  should be between +1 and -1 in value.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    equalization_filter_enabled.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    equalization_filter_enabled.Session instance, and calling set/get value on the result.:

        session['0,1'].equalization_filter_enabled = var
        var = session['0,1'].equalization_filter_enabled
    '''
    equalization_num_coefficients = attributes.AttributeViInt32(1150312)
    '''Type: int

    Returns the number of coefficients that the FIR filter can accept.  This filter is designed  to compensate the input signal for artifacts introduced to the signal outside of the digitizer.   However, since this is a generic FIR filter any coefficients are valid.  Coefficients should be  between +1 and -1 in value.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    equalization_num_coefficients.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    equalization_num_coefficients.Session instance, and calling set/get value on the result.:

        session['0,1'].equalization_num_coefficients = var
        var = session['0,1'].equalization_num_coefficients
    '''
    exported_advance_trigger_output_terminal = attributes.AttributeViString(1150109)
    '''Type: str

    Specifies the destination to export the advance trigger.   When the advance trigger is received, the digitizer begins acquiring  samples for the Nth record.
    Consult your device documentation for a specific list of valid destinations.
    '''
    exported_ref_trigger_output_terminal = attributes.AttributeViString(1150098)
    '''Type: str

    Specifies the destination export for the reference (stop) trigger.
    Consult your device documentation for a specific list of valid destinations.
    '''
    exported_start_trigger_output_terminal = attributes.AttributeViString(1150097)
    '''Type: str

    Specifies the destination to export the Start trigger.   When the start trigger is received, the digitizer begins acquiring  samples.
    Consult your device documentation for a specific list of valid destinations.
    '''
    fetch_interleaved_data = attributes.AttributeViBoolean(1150072)
    '''Type: bool

    Set to VI_TRUE to retrieve one array with alternating values on the NI 5620/5621.  For example, this attribute can be used to retrieve a single array with I and Q interleaved  instead of two separate arrays. If set to VI_TRUE, the resulting array will be twice the size of the actual record length.
    '''
    fetch_interleaved_iq_data = attributes.AttributeViBoolean(1150311)
    '''Type: bool

    Enables/disables interleaving of the I and Q data.  When disabled, the traditional  niScope_Fetch() functions will return the I waveform for each acquisition followed by  the Q waveform.  When enabled, the I and Q  data are interleaved into a single waveform.  In the interleaving case, you must  allocate twice as many elements in the array as number of samples being fetched (since each  sample contains an I and a Q component).
    Default Value: VI_TRUE
    '''
    fetch_meas_num_samples = attributes.AttributeViInt32(1150081)
    '''Type: int

    Number of samples to fetch when performing a measurement. Use -1 to fetch the actual record length.
    Default Value: -1
    '''
    fetch_num_records = attributes.AttributeViInt32(1150080)
    '''Type: int

    Number of records to fetch. Use -1 to fetch all configured records.
    Default Value: -1
    '''
    fetch_offset = attributes.AttributeViInt32(1150078)
    '''Type: int

    Offset in samples to start fetching data within each record. The offset is applied relative to  NISCOPE_ATTR_FETCH_RELATIVE_TO.The offset can be positive or negative.
    Default Value: 0
    '''
    fetch_record_number = attributes.AttributeViInt32(1150079)
    '''Type: int

    Zero-based index of the first record to fetch.  Use NISCOPE_FETCH_NUM_RECORDS to set the number of records to fetch.
    Default Value: 0.
    '''
    fetch_relative_to = attributes.AttributeEnum(attributes.AttributeViInt32, enums.FetchRelativeTo, 1150077)
    '''Type: enums.FetchRelativeTo

    Position to start fetching within one record.
    Default Value: NISCOPE_VAL_PRETRIGGER
    '''
    flex_fir_antialias_filter_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.FlexFIRAntialiasFilterType, 1150271)
    '''Type: enums.FlexFIRAntialiasFilterType

    The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter.
    Use this attribute to select from several types of filters to achieve desired filtering characteristics.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    flex_fir_antialias_filter_type.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    flex_fir_antialias_filter_type.Session instance, and calling set/get value on the result.:

        session['0,1'].flex_fir_antialias_filter_type = var
        var = session['0,1'].flex_fir_antialias_filter_type
    '''
    fpga_bitfile_path = attributes.AttributeViString(1150375)
    '''Type: str

    Gets the absolute file path to the bitfile loaded on the FPGA.

    Note: Gets the absolute file path to the bitfile loaded on the FPGA.
    '''
    fractional_resample_enabled = attributes.AttributeViBoolean(1150320)
    '''Type: bool

    Enables the onboard signal processing block that resamples the input waveform to the user desired sample rate.  The default value is FALSE.
    '''
    group_capabilities = attributes.AttributeViString(1050401)
    '''Type: str

    A string that contains a comma-separated list of class extension groups that this driver implements.
    '''
    high_pass_filter_frequency = attributes.AttributeViReal64(1150377)
    '''Type: float

    Specifies the frequency for the highpass filter in Hz. The device uses
    one of the valid values listed below. If an invalid value is specified,
    no coercion occurs. The default value is 0.
    **(PXIe-5164) Valid Values:**
    0 90 450
    **Related topics:**
    `Digital Filtering <digitizers.chm::/Digital_Filtering_Overview.html>`__
    '''
    horz_enforce_realtime = attributes.AttributeViBoolean(1150004)
    '''Type: bool

    Indicates whether the digitizer enforces real-time measurements  or allows equivalent-time measurements.
    '''
    horz_min_num_pts = attributes.AttributeViInt32(1250009)
    '''Type: int

    Specifies the minimum number of points you require in the waveform record for each channel.  NI-SCOPE uses the value you specify to configure the record length that the digitizer uses  for waveform acquisition. NISCOPE_ATTR_HORZ_RECORD_LENGTH returns the actual record length.
    Valid Values: 1 - available onboard memory
    '''
    horz_num_records = attributes.AttributeViInt32(1150001)
    '''Type: int

    Specifies the number of records to acquire. Can be used for multi-record acquisition  and single-record acquisitions. Setting this to 1 indicates a single-record acquisition.
    '''
    horz_record_length = attributes.AttributeViInt32(1250008)
    '''Type: int

    Returns the actual number of points the digitizer acquires for each channel.  The value is equal to or greater than the minimum number of points you specify with  NISCOPE_ATTR_HORZ_MIN_NUM_PTS.
    Allocate a ViReal64 array of this size or greater to pass as the WaveformArray parameter of  the Read and Fetch functions. This attribute is only valid after a call to the one of the  Configure Horizontal functions.
    '''
    horz_record_ref_position = attributes.AttributeViReal64(1250011)
    '''Type: float

    Specifies the position of the Reference Event in the waveform record.  When the digitizer detects a trigger, it waits the length of time the  NISCOPE_ATTR_TRIGGER_DELAY_TIME attribute specifies. The event that occurs when  the delay time elapses is the Reference Event. The Reference Event is relative to the  start of the record and is a percentage of the record length. For example, the value 50.0  corresponds to the center of the waveform record and 0.0 corresponds to the first element in the waveform record.
    Valid Values: 0.0 - 100.0
    '''
    horz_sample_rate = attributes.AttributeViReal64(1250010)
    '''Type: float

    Returns the effective sample rate using the current configuration. The units are samples per second.  This attribute is only valid after a call to the one of the Configure Horizontal functions.
    Units: Hertz (Samples / Second)
    '''
    horz_time_per_record = attributes.AttributeViReal64(1250007)
    '''Type: float

    Specifies the length of time that corresponds to the record length.
    Units: Seconds
    '''
    input_clock_source = attributes.AttributeViString(1150002)
    '''Type: str

    Specifies the input source for the PLL reference clock (the 1 MHz to 20 MHz clock on the NI 5122, the 10 MHz clock  for the NI 5112/5620/5621/5911) to which the digitizer will be phase-locked; for the NI 5102, this is the source  of the board clock.
    '''
    input_impedance = attributes.AttributeViReal64(1250103)
    '''Type: float

    Specifies the input impedance for the channel in Ohms.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    input_impedance.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    input_impedance.Session instance, and calling set/get value on the result.:

        session['0,1'].input_impedance = var
        var = session['0,1'].input_impedance
    '''
    instrument_firmware_revision = attributes.AttributeViString(1050510)
    '''Type: str

    A string that contains the firmware revision information  for the instrument you are currently using.
    '''
    instrument_manufacturer = attributes.AttributeViString(1050511)
    '''Type: str

    A string that contains the name of the instrument manufacturer.
    '''
    instrument_model = attributes.AttributeViString(1050512)
    '''Type: str

    A string that contains the model number of the current instrument.
    '''
    interchange_check = attributes.AttributeViBoolean(1050021)
    '''Type: bool

    NI-SCOPE does not generate interchange warnings and therefore ignores this attribute.
    '''
    interleaving_offset_correction_enabled = attributes.AttributeViBoolean(1150376)
    '''Type: bool

    Enables the interleaving offset correction on the specified channel. The
    default value is TRUE.
    **Related topics:**
    `Timed Interleaved
    Sampling <digitizers.chm::/TimeInterleavedSampling.html>`__

    Note: If disabled, warranted specifications are not guaranteed.
    '''
    io_resource_descriptor = attributes.AttributeViString(1050304)
    '''Type: str

    Indicates the resource descriptor the driver uses to identify the physical device.  If you initialize the driver with a logical name, this attribute contains the resource descriptor  that corresponds to the entry in the IVI Configuration utility.
    If you initialize the instrument driver with the resource descriptor, this attribute contains that  value.You can pass a logical name to niScope_Init or niScope_InitWithOptions. The IVI Configuration  utility must contain an entry for the logical name. The logical name entry refers to a virtual  instrument section in the IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.
    '''
    logical_name = attributes.AttributeViString(1050305)
    '''Type: str

    A string containing the logical name you specified when opening the current IVI session.  You can pass a logical name to niScope_Init or niScope_InitWithOptions. The IVI Configuration  utility must contain an entry for the logical name. The logical name entry refers to a virtual  instrument section in the IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.
    '''
    master_enable = attributes.AttributeViBoolean(1150008)
    '''Type: bool

    Specifies whether you want the device to be a master or a slave. The master typically originates  the trigger signal and clock sync pulse. For a standalone device, set this attribute to VI_FALSE.
    '''
    max_input_frequency = attributes.AttributeViReal64(1250006)
    '''Type: float

    Specifies the bandwidth of the channel. Express this value as the frequency at which the input  circuitry attenuates the input signal by 3 dB. The units are hertz.
    Defined Values:
    NISCOPE_VAL_BANDWIDTH_FULL (-1.0)
    NISCOPE_VAL_BANDWIDTH_DEVICE_DEFAULT (0.0)
    NISCOPE_VAL_20MHZ_BANDWIDTH (20000000.0)
    NISCOPE_VAL_100MHZ_BANDWIDTH (100000000.0)
    NISCOPE_VAL_20MHZ_MAX_INPUT_FREQUENCY (20000000.0)
    NISCOPE_VAL_100MHZ_MAX_INPUT_FREQUENCY (100000000.0)

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    max_input_frequency.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    max_input_frequency.Session instance, and calling set/get value on the result.:

        session['0,1'].max_input_frequency = var
        var = session['0,1'].max_input_frequency
    '''
    max_real_time_sampling_rate = attributes.AttributeViReal64(1150073)
    '''Type: float

    Returns the maximum real time sample rate in Hz.
    '''
    max_ris_rate = attributes.AttributeViReal64(1150074)
    '''Type: float

    Returns the maximum sample rate in RIS mode in Hz.
    '''
    meas_array_gain = attributes.AttributeViReal64(1150043)
    '''Type: float

    Every element of an array is multiplied by this scalar value during the Array Gain measurement.  Refer to NISCOPE_VAL_ARRAY_GAIN for more information.
    Default: 1.0

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_array_gain.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_array_gain.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_array_gain = var
        var = session['0,1'].meas_array_gain
    '''
    meas_array_offset = attributes.AttributeViReal64(1150044)
    '''Type: float

    Every element of an array is added to this scalar value during the Array Offset measurement. Refer to NISCOPE_VAL_ARRAY_OFFSET for more information.
    Default: 0.0

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_array_offset.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_array_offset.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_array_offset = var
        var = session['0,1'].meas_array_offset
    '''
    meas_chan_high_ref_level = attributes.AttributeViReal64(1150040)
    '''Type: float

    Stores the high reference level used in many scalar measurements. Different channels may have different reference  levels. Do not use the IVI-defined, nonchannel-based attributes such as NISCOPE_ATTR_MEAS_HIGH_REF if you use  this attribute to set various channels to different values.
    Default: 90%

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_chan_high_ref_level.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_chan_high_ref_level.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_chan_high_ref_level = var
        var = session['0,1'].meas_chan_high_ref_level
    '''
    meas_chan_low_ref_level = attributes.AttributeViReal64(1150038)
    '''Type: float

    Stores the low reference level used in many scalar measurements. Different channels  may have different reference levels. Do not use the IVI-defined, nonchannel-based attributes such as  NISCOPE_ATTR_MEAS_LOW_REF if you use this attribute to set various channels to different values.
    Default: 10%

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_chan_low_ref_level.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_chan_low_ref_level.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_chan_low_ref_level = var
        var = session['0,1'].meas_chan_low_ref_level
    '''
    meas_chan_mid_ref_level = attributes.AttributeViReal64(1150039)
    '''Type: float

    Stores the mid reference level used in many scalar measurements. Different channels  may have different reference levels. Do not use the IVI-defined, nonchannel-based attributes such as  NISCOPE_ATTR_MEAS_MID_REF if you use this attribute to set various channels to different values.
    Default: 50%

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_chan_mid_ref_level.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_chan_mid_ref_level.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_chan_mid_ref_level = var
        var = session['0,1'].meas_chan_mid_ref_level
    '''
    meas_filter_center_freq = attributes.AttributeViReal64(1150032)
    '''Type: float

    The center frequency in hertz for filters of type bandpass and bandstop. The width of the filter is specified by NISCOPE_ATTR_MEAS_FILTER_WIDTH, where the cutoff frequencies are the center ± width.
    Default: 1.0e6 Hz

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_filter_center_freq.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_filter_center_freq.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_filter_center_freq = var
        var = session['0,1'].meas_filter_center_freq
    '''
    meas_filter_cutoff_freq = attributes.AttributeViReal64(1150031)
    '''Type: float

    Specifies the cutoff frequency in hertz for filters of type lowpass and highpass. The cutoff frequency definition varies depending on the filter.
    Default: 1.0e6 Hz

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_filter_cutoff_freq.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_filter_cutoff_freq.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_filter_cutoff_freq = var
        var = session['0,1'].meas_filter_cutoff_freq
    '''
    meas_filter_order = attributes.AttributeViInt32(1150036)
    '''Type: int

    Specifies the order of an IIR filter. All positive integers are valid.
    Default: 2
    '''
    meas_filter_ripple = attributes.AttributeViReal64(1150033)
    '''Type: float

    Specifies the amount of ripple in the passband in units of decibels (positive values). Used only for Chebyshev filters. The more ripple allowed gives a sharper cutoff for a given filter order.
    Default: 0.1 dB
    '''
    meas_filter_taps = attributes.AttributeViInt32(1150037)
    '''Type: int

    Defines the number of taps (coefficients) for an FIR filter.
    Default: 25
    '''
    meas_filter_transient_waveform_percent = attributes.AttributeViReal64(1150034)
    '''Type: float

    The percentage (0 - 100%) of the IIR filtered waveform to eliminate from the beginning of the waveform. This allows eliminating the transient portion of the waveform that is undefined due to the assumptions necessary at the boundary condition.
    Default: 20.0%

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_filter_transient_waveform_percent.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_filter_transient_waveform_percent.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_filter_transient_waveform_percent = var
        var = session['0,1'].meas_filter_transient_waveform_percent
    '''
    meas_filter_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.FilterType, 1150035)
    '''Type: enums.FilterType

    Specifies the type of filter, for both IIR and FIR filters. The allowed values are the following:
    ·  NISCOPE_VAL_MEAS_LOWPASS
    ·  NISCOPE_VAL_MEAS_HIGHPASS
    ·  NISCOPE_VAL_MEAS_BANDPASS
    ·  NISCOPE_VAL_MEAS_BANDSTOP
    Default: NISCOPE_VAL_MEAS_LOWPASS
    '''
    meas_filter_width = attributes.AttributeViReal64(1150041)
    '''Type: float

    Specifies the width of bandpass and bandstop type filters in hertz. The cutoff frequencies occur at NISCOPE_ATTR_MEAS_FILTER_CENTER_FREQ ± one-half width.
    Default: 1.0e3 Hz
    '''
    meas_fir_filter_window = attributes.AttributeEnum(attributes.AttributeViInt32, enums.FIRFilterWindow, 1150042)
    '''Type: enums.FIRFilterWindow

    Specifies the FIR window type. The possible choices are:
    NISCOPE_VAL_NONE
    NISCOPE_VAL_HANNING_WINDOW
    NISCOPE_VAL_HAMMING_WINDOW
    NISCOPE_VAL_TRIANGLE_WINDOW
    NISCOPE_VAL_FLAT_TOP_WINDOW
    NISCOPE_VAL_BLACKMAN_WINDOW
    The symmetric windows are applied to the FIR filter coefficients to limit passband ripple in FIR filters.
    Default: NISCOPE_VAL_NONE

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_fir_filter_window.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_fir_filter_window.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_fir_filter_window = var
        var = session['0,1'].meas_fir_filter_window
    '''
    meas_hysteresis_percent = attributes.AttributeViReal64(1150019)
    '''Type: float

    Digital hysteresis that is used in several of the scalar waveform measurements. This attribute specifies the percentage of the full-scale vertical range for the hysteresis window size.
    Default: 2%

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_hysteresis_percent.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_hysteresis_percent.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_hysteresis_percent = var
        var = session['0,1'].meas_hysteresis_percent
    '''
    meas_interpolation_sampling_factor = attributes.AttributeViReal64(1150030)
    '''Type: float

    The new number of points for polynomial interpolation is the sampling factor times the input number of points. For example, if you acquire 1,000 points with the digitizer and set this attribute to 2.5, calling niScope_FetchWaveformMeasurementArray with the NISCOPE_VAL_POLYNOMIAL_INTERPOLATION measurement resamples the waveform to 2,500 points.
    Default: 2.0

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_interpolation_sampling_factor.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_interpolation_sampling_factor.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_interpolation_sampling_factor = var
        var = session['0,1'].meas_interpolation_sampling_factor
    '''
    meas_last_acq_histogram_size = attributes.AttributeViInt32(1150020)
    '''Type: int

    Specifies the size (that is, the number of bins) in the last acquisition histogram. This histogram is used to determine several scalar measurements, most importantly voltage low and voltage high.
    Default: 256

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_last_acq_histogram_size.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_last_acq_histogram_size.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_last_acq_histogram_size = var
        var = session['0,1'].meas_last_acq_histogram_size
    '''
    meas_other_channel = attributes.AttributeViString(1150018)
    '''Type: str

    Specifies the second channel for two-channel measurements, such as NISCOPE_VAL_ADD_CHANNELS. If processing steps are registered with this channel, the processing is done before the waveform is used in a two-channel measurement.
    Default: '0'

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_other_channel.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_other_channel.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_other_channel = var
        var = session['0,1'].meas_other_channel
    '''
    meas_percentage_method = attributes.AttributeEnum(attributes.AttributeViInt32, enums.PercentageMethod, 1150045)
    '''Type: enums.PercentageMethod

    Specifies the method used to map percentage reference units to voltages for the reference. Possible values are:
    NISCOPE_VAL_MEAS_LOW_HIGH
    NISCOPE_VAL_MEAS_MIN_MAX
    NISCOPE_VAL_MEAS_BASE_TOP
    Default: NISCOPE_VAL_MEAS_BASE_TOP

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_percentage_method.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_percentage_method.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_percentage_method = var
        var = session['0,1'].meas_percentage_method
    '''
    meas_polynomial_interpolation_order = attributes.AttributeViInt32(1150029)
    '''Type: int

    Specifies the polynomial order used for the polynomial interpolation measurement. For example, an order of 1 is linear interpolation whereas an order of 2 specifies parabolic interpolation. Any positive integer is valid.
    Default: 1
    '''
    meas_ref_level_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.RefLevelUnits, 1150016)
    '''Type: enums.RefLevelUnits

    Specifies the units of the reference levels.
    NISCOPE_VAL_MEAS_VOLTAGE--Specifies that the reference levels are given in units of volts
    NISCOPE_VAL_MEAS_PERCENTAGE--Percentage units, where the measurements voltage low and voltage high represent 0% and 100%, respectively.
    Default: NISCOPE_VAL_MEAS_PERCENTAGE

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_ref_level_units.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_ref_level_units.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_ref_level_units = var
        var = session['0,1'].meas_ref_level_units
    '''
    meas_time_histogram_high_time = attributes.AttributeViReal64(1150028)
    '''Type: float

    Specifies the highest time value included in the multiple acquisition time histogram. The units are always seconds.
    Default: 5.0e-4 seconds
    '''
    meas_time_histogram_high_volts = attributes.AttributeViReal64(1150026)
    '''Type: float

    Specifies the highest voltage value included in the multiple-acquisition time histogram. The units are always volts.
    Default: 10.0 V

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_time_histogram_high_volts.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_time_histogram_high_volts.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_time_histogram_high_volts = var
        var = session['0,1'].meas_time_histogram_high_volts
    '''
    meas_time_histogram_low_time = attributes.AttributeViReal64(1150027)
    '''Type: float

    Specifies the lowest time value included in the multiple-acquisition time histogram. The units are always seconds.
    Default: -5.0e-4 seconds
    '''
    meas_time_histogram_low_volts = attributes.AttributeViReal64(1150025)
    '''Type: float

    Specifies the lowest voltage value included in the multiple acquisition time histogram. The units are always volts.
    Default: -10.0 V

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_time_histogram_low_volts.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_time_histogram_low_volts.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_time_histogram_low_volts = var
        var = session['0,1'].meas_time_histogram_low_volts
    '''
    meas_time_histogram_size = attributes.AttributeViInt32(1150024)
    '''Type: int

    Determines the multiple acquisition voltage histogram size. The size is set during the first call to a time histogram measurement after clearing the measurement history with niScope_ClearWaveformMeasurementStats.
    Default: 256

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    meas_time_histogram_size.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    meas_time_histogram_size.Session instance, and calling set/get value on the result.:

        session['0,1'].meas_time_histogram_size = var
        var = session['0,1'].meas_time_histogram_size
    '''
    meas_voltage_histogram_high_volts = attributes.AttributeViReal64(1150023)
    '''Type: float

    Specifies the highest voltage value included in the multiple acquisition voltage histogram. The units are always volts.
    Default: 10.0 V
    '''
    meas_voltage_histogram_low_volts = attributes.AttributeViReal64(1150022)
    '''Type: float

    Specifies the lowest voltage value included in the multiple-acquisition voltage histogram. The units are always volts.
    Default: -10.0 V
    '''
    meas_voltage_histogram_size = attributes.AttributeViInt32(1150021)
    '''Type: int

    Determines the multiple acquisition voltage histogram size. The size is set the first time a voltage histogram measurement is called after clearing the measurement history with the function niScope_ClearWaveformMeasurementStats.
    Default: 256
    '''
    min_sample_rate = attributes.AttributeViReal64(1150009)
    '''Type: float

    Specify the sampling rate for the acquisition in Samples per second.
    Valid Values:
    The combination of sampling rate and min record length must allow the  digitizer to sample at a valid sampling rate for the acquisition type specified  in niScope_ConfigureAcquisition and not require more memory than the  onboard memory module allows.
    '''
    mux_mode_register = attributes.AttributeViInt32(1151002)
    onboard_memory_size = attributes.AttributeViInt32(1150069)
    '''Type: int

    Returns the total combined amount of onboard memory for all channels in bytes.
    '''
    oscillator_phase_dac_value = attributes.AttributeViInt32(1150105)
    '''Type: int

    Gets or sets the binary phase DAC value that controls the delay added to the Phase Locked Loop (PLL) of the sample clock.

    Note: if this value is set, sample clock adjust and TClk will not be able to do any sub-sample adjustment of the timebase sample clock.
    '''
    output_clock_source = attributes.AttributeViString(1150003)
    '''Type: str

    Specifies the output source for the 10 MHz clock to which another digitizer's sample clock can be phased-locked.
    '''
    overflow_error_reporting = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OverflowErrorReporting, 1150309)
    '''Type: enums.OverflowErrorReporting

    Configures error reporting when the DDC block detects an overflow in any of its  stages. Overflows lead to clipping of the waveform.
    Valid Values:
    Warning (0)
    Error (1)
    Disabled (2)
    Default Value: Warning
    '''
    p2p_advanced_attributes_enabled = attributes.AttributeViBoolean(1150343)
    '''Type: bool

    Enables/disables the advanced attributes for a peer-to-peer endpoint. These attributes cannot be used if  an endpoint is being configured by NI-P2P, or a resource reservation error will occur.
    Default Value: VI_FALSE

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_channels_to_stream = attributes.AttributeViString(1150339)
    '''Type: str

    Specifies which channels are written to a peer-to-peer endpoint. If multiple channels are specified,  the channels are interleaved by sample.
    Default Value: 0

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_data_trans_permission_addr = attributes.AttributeViInt64(1150329)
    '''Type: int

    Returns the address of a hardware register used to grant permisison for the peer-to-peer endpoint to write  data to another peer.. The type of this address is determined by the  NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR_TYPE attribute. Permission is granted in bytes and the register  is additive.

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_data_trans_permission_addr_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.AddressType, 1150330)
    '''Type: enums.AddressType

    Specifies the type of address returned from the NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR attribute.
    Valid Values:
    Physical (0)
    Virtual (1)
    Default Value: Virtual

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_destination_window_addr = attributes.AttributeViInt64(1150331)
    '''Type: int

    Specifies the destination for data written by the peer-to-peer endpoint. The type of this address is specified  by the NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR_TYPE attribute.
    Valid Values: A valid, non-NULL physical or virtual address.

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_destination_window_addr_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.AddressType, 1150332)
    '''Type: enums.AddressType

    Specifies the type of the NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR attribute.
    Valid Values:
    Physical (0)
    Virtual (1)
    Default Value: Virtual

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_destination_window_size = attributes.AttributeViInt64(1150333)
    '''Type: int

    Specifies the size, in bytes, of the destination window determined by the  NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDRESS and the NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDRESS_TYPE  attributes.
    Valid Values: Any non-NULL value.

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_enabled = attributes.AttributeViBoolean(1150338)
    '''Type: bool

    Specifies whether the digitizer writes data to the peer-to-peer endpoint.
    Default Value: VI_FALSE

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_endpoint_overflow = attributes.AttributeViBoolean(1150344)
    '''Type: bool

    Returns TRUE if the endpoint FIFO has overflowed. Reset the endpoint to clear the overflow condition.

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_endpoint_size = attributes.AttributeViInt32(1150342)
    '''Type: int

    Returns the size in samples of the peer-to-peer endpoint.

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_fifo_endpoint_count = attributes.AttributeViInt32(1150345)
    '''Type: int

    Returns the number of FIFO-based peer-to-peer endpoints this device supports.

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_most_samples_avail_in_endpoint = attributes.AttributeViInt32(1150341)
    '''Type: int

    Returns the most number of samples available to stream from a peer-to-peer endpoint since the last  time this attribute was read.

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_notify_message_push_addr = attributes.AttributeViInt64(1150335)
    '''Type: int

    Specifies the address to Push Message push Value to on the event specified by the  NISCOPE_ATTR_P2P_NOTIFY_PUSH_MESSAGE_ON attribute.

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_notify_message_push_addr_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.AddressType, 1150336)
    '''Type: enums.AddressType

    Specifies the type of the NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR attribute.
    Valid Values:
    Physical (0)
    Virtual (1)
    Default Value: Virtual

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_notify_message_push_value = attributes.AttributeViInt64(1150337)
    '''Type: int

    Specifies the value to be pushed to the NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR attribute on the event specified  by the NISCOPE_ATTR_MESSAGE_PUSH_ON attribute.

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_notify_push_message_on = attributes.AttributeEnum(attributes.AttributeViInt32, enums.NotificationType, 1150334)
    '''Type: enums.NotificationType

    Specifies the event to push the NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_VALUE attribute to the  NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR attribute. Setting this attribute to NISCOPE_VAL_NOTIFY_DONE pushes  the message when the acquisition has completed.
    Valid Values:
    Never (0)
    Done (1)
    Default Value: Done

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_onboard_memory_enabled = attributes.AttributeViBoolean(1150354)
    '''Type: bool

    Specifies whether the digitizer writes data to onboard memory when a peer-to-peer endpoint is enabled.
    Default Value: VI_FALSE

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_samples_avail_in_endpoint = attributes.AttributeViInt32(1150328)
    '''Type: int

    Returns the current number of samples available to stream from a peer-to-peer endpoint.

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    p2p_samples_transferred = attributes.AttributeViInt64(1150340)
    '''Type: int

    Returns the number of samples transferred through the peer-to-peer endpoint since it was last reset.

    Note: This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.
    '''
    pll_lock_status = attributes.AttributeViBoolean(1151303)
    '''Type: bool

    If TRUE, the PLL has remained locked to the external reference clock since it was last checked. If FALSE,  the PLL has become unlocked from the external reference clock since it was last checked.
    '''
    points_done = attributes.AttributeViReal64(1150082)
    '''Type: float

    Actual number of samples acquired in the record specified by NISCOPE_ATTR_FETCH_RECORD_NUMBER from the NISCOPE_ATTR_FETCH_RELATIVE_TO and NISCOPE_ATTR_FETCH_OFFSET attributes.
    '''
    poll_interval = attributes.AttributeViInt32(1150100)
    '''Type: int

    Specifies the poll interval in milliseconds to use during RIS acquisitions to check  whether the acquisition is complete.
    '''
    probe_attenuation = attributes.AttributeViReal64(1250004)
    '''Type: float

    Specifies the probe attenuation for the input channel. For example, for a 10:1 probe,  set this attribute to 10.0.
    Valid Values:
    Any positive real number. Typical values are 1, 10, and 100.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    probe_attenuation.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    probe_attenuation.Session instance, and calling set/get value on the result.:

        session['0,1'].probe_attenuation = var
        var = session['0,1'].probe_attenuation
    '''
    range_check = attributes.AttributeViBoolean(1050002)
    '''Type: bool

    Specifies whether to validate attribute values and function parameters.   If enabled, the instrument driver validates the parameters values that you  pass to driver functions.  Range checking parameters is very useful for  debugging.  After you validate your program, you can set this attribute to  VI_FALSE to disable range checking and maximize performance.
    The default value is VI_TRUE.   Use the niScope_InitWithOptions  function to override this value.
    '''
    ready_for_advance_event_output_terminal = attributes.AttributeViString(1150112)
    '''Type: str

    Specifies the destination for the Ready for Advance Event.    When this event is asserted, the digitizer is ready to receive an advance trigger.
    Consult your device documentation for a specific list of valid destinations.
    '''
    ready_for_ref_event_output_terminal = attributes.AttributeViString(1150111)
    '''Type: str

    Specifies the destination for the Ready for Reference Event.   When this event is asserted, the digitizer is ready to receive a reference trigger.
    Consult your device documentation for a specific list of valid destinations.
    '''
    ready_for_start_event_output_terminal = attributes.AttributeViString(1150110)
    '''Type: str

    Specifies the destination for the Ready for Start Event.   When this event is asserted, the digitizer is ready to receive a start trigger.
    Consult your device documentation for a specific list of valid destinations.
    '''
    records_done = attributes.AttributeViInt32(1150083)
    '''Type: int

    Specifies the number of records that have been completely acquired.
    '''
    record_arm_source = attributes.AttributeViString(1150065)
    '''Type: str

    Specifies the record arm source.
    '''
    record_coercions = attributes.AttributeViBoolean(1050006)
    '''Type: bool

    Specifies whether the IVI engine keeps a list of the value coercions it  makes for ViInt32 and ViReal64 attributes.  You call  Ivi_GetNextCoercionInfo to extract and delete the oldest coercion record  from the list.
    The default value is VI_FALSE.   Use the niScope_InitWithOptions  function to override this value.
    '''
    ref_clk_rate = attributes.AttributeViReal64(1150090)
    '''Type: float

    If NISCOPE_ATTR_INPUT_CLOCK_SOURCE is an external source, this attribute specifies the frequency of the input,  or reference clock, to which the internal sample clock timebase is synchronized. The frequency is in hertz.
    '''
    ref_trigger_detector_location = attributes.AttributeEnum(attributes.AttributeViInt32, enums.RefTriggerDetectorLocation, 1150314)
    '''Type: enums.RefTriggerDetectorLocation

    Indicates which analog compare circuitry to use on the device.
    '''
    ref_trigger_minimum_quiet_time = attributes.AttributeViReal64(1150315)
    '''Type: float

    The amount of time the trigger circuit must not detect a signal above the trigger level before  the trigger is armed.  This attribute is useful for triggering at the beginning and not in the  middle of signal bursts.
    '''
    ref_trig_tdc_enable = attributes.AttributeViBoolean(1150096)
    '''Type: bool

    This attribute controls whether the TDC is used to compute an accurate trigger.
    '''
    resolution = attributes.AttributeViInt32(1150102)
    '''Type: int

    Indicates the bit width of valid data (as opposed to padding bits) in the acquired waveform. Compare to NISCOPE_ATTR_BINARY_SAMPLE_WIDTH.
    '''
    ris_in_auto_setup_enable = attributes.AttributeViBoolean(1150106)
    '''Type: bool

    Indicates whether the digitizer should use RIS sample rates when searching for a frequency in autosetup.
    Valid Values:
    VI_TRUE  (1) - Use RIS sample rates in autosetup
    VI_FALSE (0) - Do not use RIS sample rates in autosetup
    '''
    ris_method = attributes.AttributeEnum(attributes.AttributeViInt32, enums.RISMethod, 1150071)
    '''Type: enums.RISMethod

    Specifies the algorithm for random-interleaved sampling, which is used if the sample rate exceeds the  value of NISCOPE_ATTR_MAX_REAL_TIME_SAMPLING_RATE.
    '''
    ris_num_averages = attributes.AttributeViInt32(1150070)
    '''Type: int

    The number of averages for each bin in an RIS acquisition.  The number of averages  times the oversampling factor is the minimum number of real-time acquisitions  necessary to reconstruct the RIS waveform.  Averaging is useful in RIS because  the trigger times are not evenly spaced, so adjacent points in the reconstructed  waveform not be accurately spaced.  By averaging, the errors in both time and  voltage are smoothed.
    '''
    samples_transferred_per_record = attributes.AttributeViInt32(1150380)
    '''Type: int

    Returns the number of samples transferred per record when you set the
    `Stream Relative To <pniScope_P2PStreamRelativeTo.html>`__ property to
    **Reference Trigger** or **Sync Trigger**.

    Note: This property is only supported on NI 5160/5162 digitizers.
    '''
    sample_clock_timebase_multiplier = attributes.AttributeViInt32(1150367)
    '''Type: int

    If `Sample Clock Timebase
    Source <pniScope_SampleClockTimebaseSource.html>`__ is an external
    source, this property specifies the ratio between the `Sample Clock
    Timebase Rate <pniScope_SampleClockTimebaseRate.html>`__ and the actual
    sample rate, which can be higher. This property can be used in
    conjunction with the `Sample Clock Timebase Divisor
    Property <pniscope_SampleClockTimebaseDivisor.html>`__.
    Some devices use multiple ADCs to sample the same channel at an
    effective sample rate that is greater than the specified clock rate.
    When providing an external sample clock use this property to indicate
    when you want a higher sample rate. Valid values for this property vary
    by device and current configuration.
    **Related topics:**
    `Sample Clock <digitizers.chm::/Sample_Clock.html>`__
    '''
    sample_mode = attributes.AttributeViInt32(1250106)
    '''Type: int

    Indicates the sample mode the digitizer is currently using.
    '''
    samp_clk_timebase_div = attributes.AttributeViInt32(1150089)
    '''Type: int

    If NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC is an external source, specifies the ratio between the sample clock timebase rate and the actual sample rate, which can be slower.
    '''
    samp_clk_timebase_rate = attributes.AttributeViReal64(1150088)
    '''Type: float

    If NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC is an external source, specifies the frequency in hertz of the external clock used as the timebase source.
    '''
    samp_clk_timebase_src = attributes.AttributeViString(1150087)
    '''Type: str

    Specifies the source of the sample clock timebase, which is the timebase used to control waveform sampling.  The actual sample rate may be the timebase itself or a divided version of the timebase, depending on the  NISCOPE_ATTR_MIN_SAMPLE_RATE (for internal sources) or the NISCOPE_ATTR_SAMP_CLK_TIMEBASE_DIV (for external sources).
    '''
    serial_number = attributes.AttributeViString(1150104)
    '''Type: str

    Returns the serial number of the device.
    '''
    simulate = attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Specifies whether or not to simulate instrument driver I/O operations.  If  simulation is enabled, instrument driver functions perform range checking  and call Ivi_GetAttribute and Ivi_SetAttribute functions, but they do not  perform instrument I/O.  For output parameters that represent instrument  data, the instrument driver functions return calculated values.
    The default value is VI_FALSE.   Use the niScope_InitWithOptions  function to override this value.
    '''
    slave_trigger_delay = attributes.AttributeViReal64(1150046)
    '''Type: float

    Specifies the delay for the trigger from the master to the slave in seconds.  This value adjusts the initial X value of the slave devices to correct for the  propagation delay between the master trigger output and slave trigger input.
    '''
    specific_driver_class_spec_major_version = attributes.AttributeViInt32(1050515)
    '''Type: int

    The major version number of the class specification with which this driver is compliant.
    '''
    specific_driver_class_spec_minor_version = attributes.AttributeViInt32(1050516)
    '''Type: int

    The minor version number of the class specification with which this driver is compliant.
    '''
    specific_driver_description = attributes.AttributeViString(1050514)
    '''Type: str

    A string that contains a brief description of the specific  driver
    '''
    specific_driver_revision = attributes.AttributeViString(1050551)
    '''Type: str

    A string that contains additional version information about this  instrument driver.
    '''
    specific_driver_vendor = attributes.AttributeViString(1050513)
    '''Type: str

    A string that contains the name of the vendor that supplies this driver.
    '''
    start_to_ref_trigger_holdoff = attributes.AttributeViReal64(1150103)
    '''Type: float

    Pass the length of time you want the digitizer to wait after it starts acquiring  data until the digitizer enables the trigger system to detect a reference (stop) trigger.
    Units: Seconds
    Valid Values: 0.0 - 171.8

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    start_to_ref_trigger_holdoff.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    start_to_ref_trigger_holdoff.Session instance, and calling set/get value on the result.:

        session['0,1'].start_to_ref_trigger_holdoff = var
        var = session['0,1'].start_to_ref_trigger_holdoff
    '''
    stream_relative_to = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StreamingPositionType, 1150373)
    '''Type: enums.StreamingPositionType

    Determines which trigger peer-to-peer data is streamed relative to. The
    default value is **Start Trigger**.

    Note: On the NI 5122/5622, only **Start Trigger** is valid for this property.
    '''
    supported_instrument_models = attributes.AttributeViString(1050327)
    '''Type: str

    A string that contains a comma-separated list of the instrument model numbers supported by this driver.
    '''
    trigger_auto_triggered = attributes.AttributeViBoolean(1150278)
    '''Type: bool

    Specifies if the last acquisition was auto triggered.   You can use the Auto Triggered attribute to find out if the last acquisition was triggered.
    '''
    trigger_coupling = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerCoupling, 1250014)
    '''Type: enums.TriggerCoupling

    Specifies how the digitizer couples the trigger source. This attribute affects instrument operation only when  NISCOPE_ATTR_TRIGGER_TYPE is set to NISCOPE_VAL_EDGE_TRIGGER, NISCOPE_VAL_HYSTERESIS_TRIGGER, or NISCOPE_VAL_WINDOW_TRIGGER.
    '''
    trigger_delay_time = attributes.AttributeViReal64(1250015)
    '''Type: float

    Specifies the trigger delay time in seconds. The trigger delay time is the length of time the digitizer waits  after it receives the trigger. The event that occurs when the trigger delay elapses is the Reference Event.
    Valid Values: 0.0 - 171.8
    '''
    trigger_from_pfi_delay = attributes.AttributeViReal64(1150052)
    '''Type: float

    This is a factory-programmed value that specifies the delay for the PFI lines  to the trigger input in seconds.  By itself, this attribute has no effect on  the acquired data.  However, depending on how the trigger lines are routed  between the master and slave devices, you can use this value as a starting  point to set NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.
    '''
    trigger_from_rtsi_delay = attributes.AttributeViReal64(1150051)
    '''Type: float

    This is a factory-programmed value that specifies the delay for the RTSI bus  to the trigger input in seconds.  By itself, this attribute has no effect on  the acquired data.  However, depending on how the trigger lines are routed  between the master and slave devices, you can use this value as a starting point  to set NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.
    '''
    trigger_from_star_delay = attributes.AttributeViReal64(1150050)
    '''Type: float

    This is a factory-programmed value that specifies the delay for PXI Star  Trigger line to the trigger input in seconds.  By itself, this attribute  has no effect on the acquired data.  However, depending on how the trigger  lines are routed between the master and slave devices, you can use this value  as a starting point to set NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.
    '''
    trigger_holdoff = attributes.AttributeViReal64(1250016)
    '''Type: float

    Specifies the length of time (in seconds) the digitizer waits after detecting a trigger before  enabling the trigger subsystem to detect another trigger. This attribute affects instrument operation  only when the digitizer requires multiple acquisitions to build a complete waveform. The digitizer requires  multiple waveform acquisitions when it uses equivalent-time sampling or when the digitizer is configured for a  multi-record acquisition through a call to niScope_ConfigureHorizontalTiming.
    Valid Values: 0.0 - 171.8
    '''
    trigger_hysteresis = attributes.AttributeViReal64(1150006)
    '''Type: float

    Specifies the size of the hysteresis window on either side of the trigger level.  The digitizer triggers when the trigger signal passes through the threshold you specify  with the Trigger Level parameter, has the slope you specify with the Trigger Slope parameter,  and passes through the hysteresis window that you specify with this parameter.
    '''
    trigger_impedance = attributes.AttributeViReal64(1150075)
    '''Type: float

    Specifies the input impedance for the external analog trigger channel in Ohms.
    Valid Values:
    50      - 50 ohms
    1000000 - 1 mega ohm
    '''
    trigger_level = attributes.AttributeViReal64(1250017)
    '''Type: float

    Specifies the voltage threshold for the trigger subsystem. The units are volts.  This attribute affects instrument behavior only when the NISCOPE_ATTR_TRIGGER_TYPE is set to  NISCOPE_VAL_EDGE_TRIGGER, NISCOPE_VAL_HYSTERESIS_TRIGGER, or NISCOPE_VAL_WINDOW_TRIGGER.
    Valid Values:
    The values of the range and offset parameters in niScope_ConfigureVertical determine the valid range for the trigger level  on the channel you use as the Trigger Source. The value you pass for this parameter must meet the following conditions:
    '''
    trigger_modifier = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerModifier, 1250102)
    '''Type: enums.TriggerModifier

    Configures the device to automatically complete an acquisition if a trigger has not been received.
    Valid Values:
    None (1)         - Normal triggering
    Auto Trigger (2) - Auto trigger acquisition if no trigger arrives
    '''
    trigger_slope = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerSlope, 1250018)
    '''Type: enums.TriggerSlope

    Specifies if a rising or a falling edge triggers the digitizer.  This attribute affects instrument operation only when NISCOPE_ATTR_TRIGGER_TYPE is set to  NISCOPE_VAL_EDGE_TRIGGER, NISCOPE_VAL_HYSTERESIS_TRIGGER, or NISCOPE_VAL_WINDOW_TRIGGER.
    '''
    trigger_source = attributes.AttributeViString(1250013)
    '''Type: str

    Specifies the source the digitizer monitors for the trigger event.
    '''
    trigger_to_pfi_delay = attributes.AttributeViReal64(1150049)
    '''Type: float

    This is a factory-programmed value that specifies the delay for the trigger  to the PFI lines in seconds.  By itself, this attribute has no effect on the  acquired data.  However, depending on how the trigger lines are routed between  the master and slave devices, you can use this value as a starting point to set  NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.
    '''
    trigger_to_rtsi_delay = attributes.AttributeViReal64(1150048)
    '''Type: float

    This is a factory-programmed value that specifies the delay for the trigger  to the RTSI bus in seconds.  By itself, this attribute has no effect on the  acquired data.  However, depending on how the trigger lines are routed between  the master and slave devices, you can use this value as a starting point to set   NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.
    '''
    trigger_to_star_delay = attributes.AttributeViReal64(1150047)
    '''Type: float

    This is a factory-programmed value that specifies the delay for the trigger  to the PXI Star Trigger line in seconds.  By itself, this attribute has no  effect on the acquired data.  However, depending on how the trigger lines  are routed between the master and slave devices, you can use this value as  a starting point to set NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.
    '''
    trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerType, 1250012)
    '''Type: enums.TriggerType

    Specifies the type of trigger to use.
    '''
    trigger_window_high_level = attributes.AttributeViReal64(1150014)
    '''Type: float

    Pass the upper voltage threshold you want the digitizer to use for  window triggering.
    The digitizer triggers when the trigger signal enters or leaves  the window you specify with NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL and NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL
    Valid Values:
    The values of the Vertical Range and Vertical Offset parameters in  niScope_ConfigureVertical determine the valid range for the  High Window Level on the channel you use as the Trigger Source parameter  in niScope_ConfigureTriggerSource.  The value you pass for this parameter  must meet the following conditions.
    High Trigger Level <= Vertical Range/2 + Vertical Offset
    High Trigger Level >= (-Vertical Range/2) + Vertical Offset
    High Trigger Level > Low Trigger Level
    '''
    trigger_window_low_level = attributes.AttributeViReal64(1150013)
    '''Type: float

    Pass the lower voltage threshold you want the digitizer to use for  window triggering.
    The digitizer triggers when the trigger signal enters or leaves  the window you specify with NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL and NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL.
    Units: Volts
    Valid Values:
    The values of the Vertical Range and Vertical Offset parameters in  niScope_ConfigureVertical determine the valid range for the  Low Window Level on the channel you use as the Trigger Source parameter  in niScope_ConfigureTriggerSource.  The value you pass for this parameter  must meet the following conditions.
    Low Trigger Level <= Vertical Range/2 + Vertical Offset
    Low Trigger Level >= (-Vertical Range/2) + Vertical Offset
    Low Trigger Level < High Trigger Level
    '''
    trigger_window_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerWindowMode, 1150012)
    '''Type: enums.TriggerWindowMode

    Specifies whether you want a trigger to occur when the signal enters or leaves the window specified by  NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL, or NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL.
    '''
    tv_trigger_event = attributes.AttributeEnum(attributes.AttributeViInt32, enums.VideoTriggerEvent, 1250205)
    '''Type: enums.VideoTriggerEvent

    Specifies the condition in the video signal that causes the digitizer to trigger.
    '''
    tv_trigger_line_number = attributes.AttributeViInt32(1250206)
    '''Type: int

    Specifies the line on which to trigger, if NISCOPE_ATTR_TV_TRIGGER_EVENT is set to line number. The  valid ranges of the attribute depend on the signal format selected.  M-NTSC has a valid range of 1 to 525.  B/G-PAL, SECAM, 576i, and 576p have a valid range of  1 to 625. 720p has a valid range of 1 to 750. 1080i and 1080p have a valid range of 1125.
    '''
    tv_trigger_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.VideoPolarity, 1250204)
    '''Type: enums.VideoPolarity

    Specifies whether the video signal sync is positive or negative.
    '''
    tv_trigger_signal_format = attributes.AttributeEnum(attributes.AttributeViInt32, enums.VideoSignalFormat, 1250201)
    '''Type: enums.VideoSignalFormat

    Specifies the type of video signal, such as NTSC, PAL, or SECAM.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    tv_trigger_signal_format.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    tv_trigger_signal_format.Session instance, and calling set/get value on the result.:

        session['0,1'].tv_trigger_signal_format = var
        var = session['0,1'].tv_trigger_signal_format
    '''
    vertical_coupling = attributes.AttributeEnum(attributes.AttributeViInt32, enums.VerticalCoupling, 1250003)
    '''Type: enums.VerticalCoupling

    Specifies how the digitizer couples the input signal for the channel.  When input coupling changes, the input stage takes a finite amount of time to settle.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    vertical_coupling.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    vertical_coupling.Session instance, and calling set/get value on the result.:

        session['0,1'].vertical_coupling = var
        var = session['0,1'].vertical_coupling
    '''
    vertical_offset = attributes.AttributeViReal64(1250002)
    '''Type: float

    Specifies the location of the center of the range. The value is with respect to ground and is in volts.  For example, to acquire a sine wave that spans between 0.0 and 10.0 V, set this attribute to 5.0 V.

    Note: This attribute is not supported by all digitizers.Refer to the NI High-Speed Digitizers Help for a list of vertical offsets supported for each device.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    vertical_offset.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    vertical_offset.Session instance, and calling set/get value on the result.:

        session['0,1'].vertical_offset = var
        var = session['0,1'].vertical_offset
    '''
    vertical_range = attributes.AttributeViReal64(1250001)
    '''Type: float

    Specifies the absolute value of the input range for a channel in volts.  For example, to acquire a sine wave that spans between -5 and +5 V, set this attribute to 10.0 V.
    Refer to the NI High-Speed Digitizers Help for a list of supported vertical ranges for each device.  If the specified range is not supported by a device, the value is coerced  up to the next valid range.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    vertical_range.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    vertical_range.Session instance, and calling set/get value on the result.:

        session['0,1'].vertical_range = var
        var = session['0,1'].vertical_range
    '''

    def __init__(self, repeated_capability, vi, library, encoding, freeze_it=False):
        self._repeated_capability = repeated_capability
        self._vi = vi
        self._library = library
        self._encoding = encoding

        # Store the parameter list for later printing in __repr__
        self._param_list = "repeated_capability=" + pp.pformat(repeated_capability)

        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('niscope', self.__class__.__name__, self._param_list)

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

    def _actual_num_wfms(self):
        '''_actual_num_wfms

        Helps you to declare appropriately sized waveforms. NI-SCOPE handles the
        channel list parsing for you.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._actual_num_wfms()

        Returns:
            num_wfms (int): Returns the number of records times the number of channels; if you are
                operating in DDC mode (NI 5620/5621 only), this value is multiplied by
                two.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        num_wfms_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niScope_ActualNumWfms(vi_ctype, channel_list_ctype, None if num_wfms_ctype is None else (ctypes.pointer(num_wfms_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(num_wfms_ctype.value)

    def cal_self_calibrate(self, option=enums.Option.SELF_CALIBRATE_ALL_CHANNELS):
        '''cal_self_calibrate

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
        One or more of the referenced functions are not in the Python API for this driver.

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].cal_self_calibrate(option=niscope.Option.SELF_CALIBRATE_ALL_CHANNELS)

        Args:
            option (enums.Option): The calibration option. Use VI_NULL for a normal self-calibration
                operation or NISCOPE_VAL_CAL_RESTORE_EXTERNAL_CALIBRATION to
                restore the previous calibration.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(option) is not enums.Option:
            raise TypeError('Parameter mode must be of type ' + str(enums.Option))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        option_ctype = visatype.ViInt32(option.value)  # case S130
        error_code = self._library.niScope_CalSelfCalibrate(vi_ctype, channel_list_ctype, option_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_waveform_measurement_stats(self, clearable_measurement_function=enums.ClearableMeasurement.ALL_MEASUREMENTS):
        '''clear_waveform_measurement_stats

        Clears the waveform stats on the channel and measurement you specify. If
        you want to clear all of the measurements, use
        NISCOPE_VAL_ALL_MEASUREMENTS in the **clearableMeasurementFunction**
        parameter.

        Every time a measurement is called, the statistics information is
        updated, including the min, max, mean, standard deviation, and number of
        updates. This information is fetched with
        fetch_measurement_stats. The multi-acquisition array measurements
        are also cleared with this function.

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].clear_waveform_measurement_stats(clearable_measurement_function=niscope.ClearableMeasurement.ALL_MEASUREMENTS)

        Args:
            clearable_measurement_function (enums.ClearableMeasurement): The `scalar
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
                or `array
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
                to clear the stats for.

        '''
        if type(clearable_measurement_function) is not enums.ClearableMeasurement:
            raise TypeError('Parameter mode must be of type ' + str(enums.ClearableMeasurement))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        clearable_measurement_function_ctype = visatype.ViInt32(clearable_measurement_function.value)  # case S130
        error_code = self._library.niScope_ClearWaveformMeasurementStats(vi_ctype, channel_list_ctype, clearable_measurement_function_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_chan_characteristics(self, input_impedance, max_input_frequency):
        '''configure_chan_characteristics

        Configures the attributes that control the electrical characteristics of
        the channel—the input impedance and the bandwidth.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].configure_chan_characteristics(input_impedance, max_input_frequency)

        Args:
            input_impedance (float): The input impedance for the channel; NI-SCOPE sets
                input_impedance to this value.

            max_input_frequency (float): The bandwidth for the channel; NI-SCOPE sets
                max_input_frequency to this value. Pass 0 for this
                value to use the hardware default bandwidth. Pass –1 for this value to
                achieve full bandwidth.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        input_impedance_ctype = visatype.ViReal64(input_impedance)  # case S150
        max_input_frequency_ctype = visatype.ViReal64(max_input_frequency)  # case S150
        error_code = self._library.niScope_ConfigureChanCharacteristics(vi_ctype, channel_list_ctype, input_impedance_ctype, max_input_frequency_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_equalization_filter_coefficients(self, coefficients):
        '''configure_equalization_filter_coefficients

        Configures the custom coefficients for the equalization FIR filter on
        the device. This filter is designed to compensate the input signal for
        artifacts introduced to the signal outside of the digitizer. Because
        this filter is a generic FIR filter, any coefficients are valid.
        Coefficient values should be between +1 and –1.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].configure_equalization_filter_coefficients(coefficients)

        Args:
            coefficients (list of float): The custom coefficients for the equalization FIR filter on the device.
                These coefficients should be between +1 and –1. You can obtain the
                number of coefficients from the
                `equalization_num_coefficients <cviNISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS.html>`__
                attribute. The
                `equalization_filter_enabled <cviNISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED.html>`__
                attribute must be set to TRUE to enable the filter.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        number_of_coefficients_ctype = visatype.ViInt32(0 if coefficients is None else len(coefficients))  # case S160
        coefficients_ctype = get_ctypes_pointer_for_buffer(value=coefficients, library_type=visatype.ViReal64)  # case B550
        error_code = self._library.niScope_ConfigureEqualizationFilterCoefficients(vi_ctype, channel_list_ctype, number_of_coefficients_ctype, coefficients_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_vertical(self, range, coupling, offset=0.0, probe_attenuation=1.0, enabled=True):
        '''configure_vertical

        Configures the most commonly configured attributes of the digitizer
        vertical subsystem, such as the range, offset, coupling, probe
        attenuation, and the channel.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].configure_vertical(range, coupling, offset=0.0, probe_attenuation=1.0, enabled=True)

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
            raise TypeError('Parameter mode must be of type ' + str(enums.VerticalCoupling))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        range_ctype = visatype.ViReal64(range)  # case S150
        offset_ctype = visatype.ViReal64(offset)  # case S150
        coupling_ctype = visatype.ViInt32(coupling.value)  # case S130
        probe_attenuation_ctype = visatype.ViReal64(probe_attenuation)  # case S150
        enabled_ctype = visatype.ViBoolean(enabled)  # case S150
        error_code = self._library.niScope_ConfigureVertical(vi_ctype, channel_list_ctype, range_ctype, offset_ctype, coupling_ctype, probe_attenuation_ctype, enabled_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _fetch(self, num_samples, timeout=5.0):
        '''_fetch

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This function returns
        scaled voltage waveforms.

        This function may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note:
        You can use read instead of this function. read
        starts an acquisition on all enabled channels, waits for the acquisition
        to complete, and returns the waveform for the specified channel.

        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._fetch(num_samples, timeout=5.0)

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the function returns an error.

            timeout (float): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm (array.array("d")): Returns an array whose length is the **numSamples** times number of
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
                One or more of the referenced functions are not in the Python API for this driver.

            wfm_info (list of WaveformInfo): Returns an array of structures with the following timing and scaling
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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = visatype.ViInt32(num_samples)  # case S150
        wfm_size = (num_samples * self._actual_num_wfms())  # case B560
        wfm_array = array.array("d", [0] * wfm_size)  # case B560
        wfm_ctype = get_ctypes_pointer_for_buffer(value=wfm_array, library_type=visatype.ViReal64)  # case B560
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_Fetch(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, wfm_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return wfm_array, [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def _fetch_into(self, num_samples, wfm, timeout=5.0):
        '''_fetch

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This function returns
        scaled voltage waveforms.

        This function may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note:
        You can use read instead of this function. read
        starts an acquisition on all enabled channels, waits for the acquisition
        to complete, and returns the waveform for the specified channel.

        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._fetch(num_samples, timeout=5.0)

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the function returns an error.

            wfm (numpy.array(dtype=numpy.float64)): Returns an array whose length is the **numSamples** times number of
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
                One or more of the referenced functions are not in the Python API for this driver.

            timeout (float): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm (numpy.array(dtype=numpy.float64)): Returns an array whose length is the **numSamples** times number of
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
                One or more of the referenced functions are not in the Python API for this driver.

            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns an array of structures with the following timing and scaling
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

        if type(wfm) is not numpy.ndarray:
            raise TypeError('wfm must be {0}, is {1}'.format(numpy.ndarray, type(wfm)))
        if numpy.isfortran(wfm) is True:
            raise TypeError('wfm must be in C-order')
        if wfm.dtype is not numpy.dtype('float64'):
            raise TypeError('wfm must be numpy.ndarray of dtype=float64, is ' + str(wfm.dtype))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = visatype.ViInt32(num_samples)  # case S150
        wfm_ctype = get_ctypes_pointer_for_buffer(value=wfm)  # case B510
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_Fetch(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, wfm_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def _fetch_binary16_into(self, num_samples, wfm, timeout=5.0):
        '''_fetch_binary16

        Retrieves data from a previously initiated acquisition and returns
        binary 16-bit waveforms. This function may return multiple waveforms
        depending on the number of channels, the acquisition type, and the
        number of records you specify.

        Refer to `Using Fetch
        Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on using this function.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._fetch_binary16(num_samples, timeout=5.0)

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the function returns an error.

            wfm (numpy.array(dtype=numpy.int16)): Returns an array whose length is the **numSamples** times number of
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
                One or more of the referenced functions are not in the Python API for this driver.

            timeout (float): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm (numpy.array(dtype=numpy.int16)): Returns an array whose length is the **numSamples** times number of
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
                One or more of the referenced functions are not in the Python API for this driver.

            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns an array of structures with the following timing and scaling
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

        if type(wfm) is not numpy.ndarray:
            raise TypeError('wfm must be {0}, is {1}'.format(numpy.ndarray, type(wfm)))
        if numpy.isfortran(wfm) is True:
            raise TypeError('wfm must be in C-order')
        if wfm.dtype is not numpy.dtype('int16'):
            raise TypeError('wfm must be numpy.ndarray of dtype=int16, is ' + str(wfm.dtype))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = visatype.ViInt32(num_samples)  # case S150
        wfm_ctype = get_ctypes_pointer_for_buffer(value=wfm)  # case B510
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_FetchBinary16(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, wfm_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def _fetch_binary32_into(self, num_samples, wfm, timeout=5.0):
        '''_fetch_binary32

        Retrieves data from a previously initiated acquisition and returns
        binary 32-bit waveforms. This function may return multiple waveforms
        depending on the number of channels, the acquisition type, and the
        number of records you specify.

        Refer to `Using Fetch
        Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on using this function.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._fetch_binary32(num_samples, timeout=5.0)

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the function returns an error.

            wfm (numpy.array(dtype=numpy.int32)): Returns an array whose length is the **numSamples** times number of
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
                One or more of the referenced functions are not in the Python API for this driver.

            timeout (float): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm (numpy.array(dtype=numpy.int32)): Returns an array whose length is the **numSamples** times number of
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
                One or more of the referenced functions are not in the Python API for this driver.

            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns an array of structures with the following timing and scaling
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

        if type(wfm) is not numpy.ndarray:
            raise TypeError('wfm must be {0}, is {1}'.format(numpy.ndarray, type(wfm)))
        if numpy.isfortran(wfm) is True:
            raise TypeError('wfm must be in C-order')
        if wfm.dtype is not numpy.dtype('int32'):
            raise TypeError('wfm must be numpy.ndarray of dtype=int32, is ' + str(wfm.dtype))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = visatype.ViInt32(num_samples)  # case S150
        wfm_ctype = get_ctypes_pointer_for_buffer(value=wfm)  # case B510
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_FetchBinary32(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, wfm_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def _fetch_binary8_into(self, num_samples, wfm, timeout=5.0):
        '''_fetch_binary8

        Retrieves data from a previously initiated acquisition and returns
        binary 8-bit waveforms. This function may return multiple waveforms
        depending on the number of channels, the acquisition type, and the
        number of records you specify.

        Refer to `Using Fetch
        Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on using this function.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._fetch_binary8(num_samples, timeout=5.0)

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the function returns an error.

            wfm (numpy.array(dtype=numpy.int8)): Returns an array whose length is the **numSamples** times number of
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
                One or more of the referenced functions are not in the Python API for this driver.

            timeout (float): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm (numpy.array(dtype=numpy.int8)): Returns an array whose length is the **numSamples** times number of
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
                One or more of the referenced functions are not in the Python API for this driver.

            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns an array of structures with the following timing and scaling
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

        if type(wfm) is not numpy.ndarray:
            raise TypeError('wfm must be {0}, is {1}'.format(numpy.ndarray, type(wfm)))
        if numpy.isfortran(wfm) is True:
            raise TypeError('wfm must be in C-order')
        if wfm.dtype is not numpy.dtype('int8'):
            raise TypeError('wfm must be numpy.ndarray of dtype=int8, is ' + str(wfm.dtype))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = visatype.ViInt32(num_samples)  # case S150
        wfm_ctype = get_ctypes_pointer_for_buffer(value=wfm)  # case B510
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_FetchBinary8(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, wfm_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def fetch_into(self, wfm, timeout=5.0):
        '''fetch

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This function returns
        scaled voltage waveforms.

        This function may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].fetch(num_samples, wfm, timeout=5.0)

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the function throws an exception.

            wfm (array.array("d")): numpy array of the appropriate type and size the should be acquired as a 1D array. Size should
                be **num_samples** times number of waveforms. Call _actual_num_wfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Types supported are

                - `numpy.float64`
                - `numpy.int8`
                - `numpy.in16`
                - `numpy.int32`

                Example:

                .. code-block:: python

                    wfm = numpy.ndarray(num_samples * session.actual_num_wfms(), dtype=numpy.float64)
                    wfm_info = session['0,1'].fetch_into(num_samples, wfms, timeout=5.0)

            timeout (float): The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (list of WaveformInfo): Returns an array of classed with the following timing and scaling information about each waveform:

                                    -  **relative_initial_x** the time (in seconds) from the trigger to the first sample in the fetched waveform
                                    -  **absolute_initial_x** timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
                                    -  **x_increment** the time between points in the acquired waveform in seconds -  **actual_samples** the actual number of samples fetched and placed in the waveform array
                                    -  **gain** the gain factor of the given channel; useful for scaling binary data with the following formula:

                                        .. math::

                                            voltage = binary data * gain factor + offset

                                    -  **offset** the offset factor of the given channel; useful for scaling binary data with the following formula:

                                        .. math::

                                            voltage = binary data * gain factor + offset

                                    Call _actual_num_wfms to determine the size of this array.

        '''
        import numpy

        num_samples = int(len(wfm) / self._actual_num_wfms())

        if wfm.dtype == numpy.float64:
            return self._fetch_into(num_samples=num_samples, wfm=wfm, timeout=timeout)
        elif wfm.dtype == numpy.int8:
            return self._fetch_binary8_into(num_samples=num_samples, wfm=wfm, timeout=timeout)
        elif wfm.dtype == numpy.int16:
            return self._fetch_binary16_into(num_samples=num_samples, wfm=wfm, timeout=timeout)
        elif wfm.dtype == numpy.int32:
            return self._fetch_binary32_into(num_samples=num_samples, wfm=wfm, timeout=timeout)
        else:
            raise TypeError("Unsupported dtype. Is {0}, expected {1}, {2}, {3}, or {5}".format(wfm.dtype, numpy.float64, numpy.int8, numpy.int16, numpy.int32))

    def fetch(self, num_samples, timeout=5.0):
        '''fetch

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This function returns
        scaled voltage waveforms.

        This function may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].fetch(num_samples, timeout=5.0)

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the function throws an exception.

            timeout (float): The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout.


        Returns:
            wfm (list of float): Returns an array whose length is the **numSamples** times number of
                waveforms. Call _actual_num_wfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

            wfm_info (list of WaveformInfo): Returns an array of classed with the following timing and scaling information about each waveform:

                                    -  **relative_initial_x** the time (in seconds) from the trigger to the first sample in the fetched waveform
                                    -  **absolute_initial_x** timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
                                    -  **x_increment** the time between points in the acquired waveform in seconds -  **actual_samples** the actual number of samples fetched and placed in the waveform array
                                    -  **gain** the gain factor of the given channel; useful for scaling binary data with the following formula:

                                        .. math::

                                            voltage = binary data * gain factor + offset

                                    -  **offset** the offset factor of the given channel; useful for scaling binary data with the following formula:

                                        .. math::

                                            voltage = binary data * gain factor + offset

                                    Call _actual_num_wfms to determine the size of this array.

        '''
        return self._fetch(num_samples, timeout)

    def fetch_measurement(self, scalar_meas_function, timeout=5.0):
        '''fetch_measurement

        Fetches a waveform from the digitizer and performs the specified
        waveform measurement. Refer to `Using Fetch
        Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information.

        Many of the measurements use the low, mid, and high reference levels.
        You configure the low, mid, and high references by using
        meas_chan_low_ref_level,
        meas_chan_mid_ref_level, and
        meas_chan_high_ref_level to set each channel
        differently.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].fetch_measurement(scalar_meas_function, timeout=5.0)

        Args:
            scalar_meas_function (enums.ScalarMeasurement): The `scalar
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
                to be performed.

            timeout (float): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            result (list of float): Contains an array of all measurements acquired; call
                _actual_num_wfms to determine the array length.

        '''
        if type(scalar_meas_function) is not enums.ScalarMeasurement:
            raise TypeError('Parameter mode must be of type ' + str(enums.ScalarMeasurement))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = visatype.ViReal64(timeout)  # case S150
        scalar_meas_function_ctype = visatype.ViInt32(scalar_meas_function.value)  # case S130
        result_size = self._actual_num_wfms()  # case B560
        result_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=result_size)  # case B560
        error_code = self._library.niScope_FetchMeasurement(vi_ctype, channel_list_ctype, timeout_ctype, scalar_meas_function_ctype, result_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(result_ctype[i]) for i in range(self._actual_num_wfms())]

    def fetch_measurement_stats(self, scalar_meas_function, timeout=5.0):
        '''fetch_measurement_stats

        Obtains a waveform measurement and returns the measurement value. This
        function may return multiple statistical results depending on the number
        of channels, the acquisition type, and the number of records you
        specify.

        You specify a particular measurement type, such as rise time, frequency,
        or voltage peak-to-peak. The waveform on which the digitizer calculates
        the waveform measurement is from an acquisition that you previously
        initiated. The statistics for the specified measurement function are
        returned, where the statistics are updated once every acquisition when
        the specified measurement is fetched by any of the Fetch Measurement
        functions. If a Fetch Measurement function has not been called, this
        function fetches the data on which to perform the measurement. The
        statistics are cleared by calling
        clear_waveform_measurement_stats. Refer to `Using Fetch
        Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on incorporating fetch functions in your application.

        Many of the measurements use the low, mid, and high reference levels.
        You configure the low, mid, and high references with
        meas_chan_low_ref_level,
        meas_chan_mid_ref_level, and
        meas_chan_high_ref_level to set each channel
        differently.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].fetch_measurement_stats(scalar_meas_function, timeout=5.0)

        Args:
            scalar_meas_function (enums.ScalarMeasurement): The `scalar
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
                to be performed on each fetched waveform.

            timeout (float): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            result (list of float): Returns the resulting measurement

            mean (list of float): Returns the mean scalar value, which is obtained by averaging each
                fetch_measurement_stats call.

            stdev (list of float): Returns the standard deviation of the most recent **numInStats**
                measurements.

            min (list of float): Returns the smallest scalar value acquired (the minimum of the
                **numInStats** measurements).

            max (list of float): Returns the largest scalar value acquired (the maximum of the
                **numInStats** measurements).

            num_in_stats (list of int): Returns the number of times fetch_measurement_stats has been
                called.

        '''
        if type(scalar_meas_function) is not enums.ScalarMeasurement:
            raise TypeError('Parameter mode must be of type ' + str(enums.ScalarMeasurement))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = visatype.ViReal64(timeout)  # case S150
        scalar_meas_function_ctype = visatype.ViInt32(scalar_meas_function.value)  # case S130
        result_size = self._actual_num_wfms()  # case B560
        result_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=result_size)  # case B560
        mean_size = self._actual_num_wfms()  # case B560
        mean_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=mean_size)  # case B560
        stdev_size = self._actual_num_wfms()  # case B560
        stdev_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=stdev_size)  # case B560
        min_size = self._actual_num_wfms()  # case B560
        min_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=min_size)  # case B560
        max_size = self._actual_num_wfms()  # case B560
        max_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=max_size)  # case B560
        num_in_stats_size = self._actual_num_wfms()  # case B560
        num_in_stats_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViInt32, size=num_in_stats_size)  # case B560
        error_code = self._library.niScope_FetchMeasurementStats(vi_ctype, channel_list_ctype, timeout_ctype, scalar_meas_function_ctype, result_ctype, mean_ctype, stdev_ctype, min_ctype, max_ctype, num_in_stats_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(result_ctype[i]) for i in range(self._actual_num_wfms())], [float(mean_ctype[i]) for i in range(self._actual_num_wfms())], [float(stdev_ctype[i]) for i in range(self._actual_num_wfms())], [float(min_ctype[i]) for i in range(self._actual_num_wfms())], [float(max_ctype[i]) for i in range(self._actual_num_wfms())], [int(num_in_stats_ctype[i]) for i in range(self._actual_num_wfms())]

    def _get_attribute_vi_boolean(self, attribute_id):
        '''_get_attribute_vi_boolean

        Queries the value of a ViBoolean attribute. You can use this function to
        get the values of instrument-specific attributes and inherent IVI
        attributes. If the attribute represents an instrument state, this
        function performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_boolean(attribute_id)

        Args:
            attribute_id (int): The ID of an attribute.


        Returns:
            value (bool): Returns the current value of the attribute; pass the address of a
                ViBoolean variable.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        value_ctype = visatype.ViBoolean()  # case S200
        error_code = self._library.niScope_GetAttributeViBoolean(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def _get_attribute_vi_int32(self, attribute_id):
        '''_get_attribute_vi_int32

        Queries the value of a ViInt32 attribute. You can use this function to
        get the values of instrument-specific attributes and inherent IVI
        attributes. If the attribute represents an instrument state, this
        function performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_int32(attribute_id)

        Args:
            attribute_id (int): The ID of an attribute.


        Returns:
            value (int): Returns the current value of the attribute.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        value_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niScope_GetAttributeViInt32(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def _get_attribute_vi_real64(self, attribute_id):
        '''_get_attribute_vi_real64

        Queries the value of a ViReal64 attribute. You can use this function to
        get the values of instrument-specific attributes and inherent IVI
        attributes. If the attribute represents an instrument state, this
        function performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_real64(attribute_id)

        Args:
            attribute_id (int): The ID of an attribute.


        Returns:
            value (float): Returns the current value of the attribute; pass the address of a
                ViReal64 variable.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        value_ctype = visatype.ViReal64()  # case S200
        error_code = self._library.niScope_GetAttributeViReal64(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def _get_attribute_vi_string(self, attribute_id):
        '''_get_attribute_vi_string

        Queries the value of a ViString attribute. You can use this function to
        get the values of instrument-specific attributes and inherent IVI
        attributes. If the attribute represents an instrument state, this
        function performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid.

        You must provide a ViChar array to serve as a buffer for the value. You
        pass the number of bytes in the buffer as the **bufSize**. If the
        current value of the attribute, including the terminating NUL byte, is
        larger than the size you indicate in the **bufSize**, the function
        copies (**bufSize** – 1) bytes into the buffer, places an ASCII NUL byte
        at the end of the buffer, and returns the **bufSize** you must pass to
        get the entire value. For example, if the value is 123456 and the
        **bufSize** is 4, the function places 123 into the buffer and returns 7.
        If you want to call this function just to get the required buffer size,
        you can pass 0 for the **bufSize** and VI_NULL for the **value**.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_string(attribute_id)

        Args:
            attribute_id (int): The ID of an attribute.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        buf_size_ctype = visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        error_code = self._library.niScope_GetAttributeViString(vi_ctype, channel_list_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buf_size_ctype = visatype.ViInt32(error_code)  # case S180
        value_ctype = (visatype.ViChar * buf_size_ctype.value)()  # case C060
        error_code = self._library.niScope_GetAttributeViString(vi_ctype, channel_list_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(self._encoding)

    def get_equalization_filter_coefficients(self, number_of_coefficients):
        '''get_equalization_filter_coefficients

        Retrieves the custom coefficients for the equalization FIR filter on the
        device. This filter is designed to compensate the input signal for
        artifacts introduced to the signal outside of the digitizer. Because
        this filter is a generic FIR filter, any coefficients are valid.
        Coefficient values should be between +1 and –1.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].get_equalization_filter_coefficients(number_of_coefficients)

        Args:
            number_of_coefficients (int): The number of coefficients being passed in the **coefficients** array.


        Returns:
            coefficients (list of float): The custom coefficients for the equalization FIR filter on the device.
                These coefficients should be between +1 and –1. You can obtain the
                number of coefficients from the
                `equalization_num_coefficients <cviNISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS.html>`__
                attribute.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        number_of_coefficients_ctype = visatype.ViInt32(number_of_coefficients)  # case S190
        coefficients_size = number_of_coefficients  # case B600
        coefficients_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=coefficients_size)  # case B600
        error_code = self._library.niScope_GetEqualizationFilterCoefficients(vi_ctype, channel_ctype, number_of_coefficients_ctype, coefficients_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(coefficients_ctype[i]) for i in range(number_of_coefficients_ctype.value)]

    def _get_error(self):
        '''_get_error

        Reads an error code and message from the error queue. National
        Instruments digitizers do not contain an error queue. Errors are
        reported as they occur. Therefore, this function does not detect errors.

        Note:
        This function is included for compliance with the IviScope Class
        Specification.

        Returns:
            error_code (int): Passes the number of bytes in the ViChar array you specify for the
                Description parameter.

                If the error description, including the terminating NULL byte, contains
                more bytes than you indicate in this parameter, the function copies
                **bufferSize** – 1 bytes into the buffer, places an ASCII NULL byte at
                the end of the buffer, and returns the buffer size you must pass to get
                the entire value. For example, if the value is "123456" and the Buffer
                Size is 4, the function places "123" into the buffer and returns 7.

                If you pass a negative number, the function copies the value to the
                buffer regardless of the number of bytes in the value.

                If you pass 0, you can pass VI_NULL for the **description** parameter.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code_ctype = visatype.ViStatus()  # case S200
        buffer_size_ctype = visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niScope_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = visatype.ViInt32(error_code)  # case S180
        description_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niScope_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

    def read(self, num_samples, timeout=5.0):
        '''read

        Initiates an acquisition, waits for it to complete, and retrieves the
        data. The process is similar to calling _initiate_acquisition,
        acquisition_status, and _fetch. The only difference is
        that with read, you enable all channels specified with
        **channelList** before the acquisition; in the other method, you enable
        the channels with configure_vertical.

        This function may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note:
        Some functionality is not supported in all digitizers. Refer to
        `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].read(num_samples, timeout=5.0)

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the function returns an error.

            timeout (float): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm (array.array("d")): Returns an array whose length is the **numSamples** times number of
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
                One or more of the referenced functions are not in the Python API for this driver.

            wfm_info (list of WaveformInfo): Returns an array of structures with the following timing and scaling
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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = visatype.ViReal64(timeout)  # case S150
        num_samples_ctype = visatype.ViInt32(num_samples)  # case S150
        wfm_size = (num_samples * self._actual_num_wfms())  # case B560
        wfm_array = array.array("d", [0] * wfm_size)  # case B560
        wfm_ctype = get_ctypes_pointer_for_buffer(value=wfm_array, library_type=visatype.ViReal64)  # case B560
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library.niScope_Read(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, wfm_ctype, wfm_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return wfm_array, [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def read_measurement(self, scalar_meas_function, timeout=5.0):
        '''read_measurement

        Initiates an acquisition, waits for it to complete, and performs the
        specified waveform measurement for a single channel and record or for
        multiple channels and records.

        Refer to `Using Fetch
        Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information.

        Many of the measurements use the low, mid, and high reference levels.
        You configure the low, mid, and high references by using
        meas_chan_low_ref_level,
        meas_chan_mid_ref_level, and
        meas_chan_high_ref_level to set each channel
        differently.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1'].read_measurement(scalar_meas_function, timeout=5.0)

        Args:
            scalar_meas_function (enums.ScalarMeasurement): The `scalar
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
                to be performed

            timeout (float): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            result (array.array("d")): Contains an array of all measurements acquired. Call
                _actual_num_wfms to determine the array length.

        '''
        if type(scalar_meas_function) is not enums.ScalarMeasurement:
            raise TypeError('Parameter mode must be of type ' + str(enums.ScalarMeasurement))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        timeout_ctype = visatype.ViReal64(timeout)  # case S150
        scalar_meas_function_ctype = visatype.ViInt32(scalar_meas_function.value)  # case S130
        result_size = self._actual_num_wfms()  # case B560
        result_array = array.array("d", [0] * result_size)  # case B560
        result_ctype = get_ctypes_pointer_for_buffer(value=result_array, library_type=visatype.ViReal64)  # case B560
        error_code = self._library.niScope_ReadMeasurement(vi_ctype, channel_list_ctype, timeout_ctype, scalar_meas_function_ctype, result_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return result_array

    def _set_attribute_vi_boolean(self, attribute_id, value):
        '''_set_attribute_vi_boolean

        Sets the value of a ViBoolean attribute. This is a low-level function
        that you can use to set the values of instrument-specific attributes and
        inherent IVI attributes. If the attribute represents an instrument
        state, this function performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level functions that set most of the instrument
        attributes. Use the high-level driver functions as much as possible
        because they handle order dependencies and multithread locking for you.
        In addition, the high-level functions perform status checking only after
        setting all of the attributes. In contrast, when you set multiple
        attributes using the SetAttribute functions, the functions check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level functions that configure multiple attributes perform
        instrument I/O only for the attributes whose value you change. Thus, you
        can safely call the high-level functions without the penalty of
        redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_boolean(attribute_id, value)

        Args:
            attribute_id (int): The ID of an attribute.

            value (bool): The value that you want to set the attribute to. Some values might not
                be valid depending on the current settings of the instrument session.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        value_ctype = visatype.ViBoolean(value)  # case S150
        error_code = self._library.niScope_SetAttributeViBoolean(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, attribute_id, value):
        '''_set_attribute_vi_int32

        Sets the value of a ViInt32 attribute. This is a low-level function that
        you can use to set the values of instrument-specific attributes and
        inherent IVI attributes. If the attribute represents an instrument
        state, this function performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level functions that set most of the instrument
        attributes. Use the high-level functions as much as possible because
        they handle order dependencies and multithread locking for you. In
        addition, high-level functions perform status checking only after
        setting all of the attributes. In contrast, when you set multiple
        attributes using the Set Attribute functions, the functions check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level functions that configure multiple attributes perform
        instrument I/O only for the attributes whose value you change. Thus, you
        can safely call the high-level functions without the penalty of
        redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_int32(attribute_id, value)

        Args:
            attribute_id (int): The ID of an attribute.

            value (int): The value that you want to set the attribute. Some values might not be
                valid depending on the current settings of the instrument session.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        value_ctype = visatype.ViInt32(value)  # case S150
        error_code = self._library.niScope_SetAttributeViInt32(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, attribute_id, value):
        '''_set_attribute_vi_real64

        Sets the value of a ViReal64 attribute. This is a low-level function
        that you can use to set the values of instrument-specific attributes and
        inherent IVI attributes. If the attribute represents an instrument
        state, this function performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level functions that set most of the instrument
        attributes. Use the high-level driver functions as much as possible
        because they handle order dependencies and multithread locking for you.
        In addition, the high-level functions perform status checking only after
        setting all of the attributes. In contrast, when you set multiple
        attributes using the Set Attribute functions, the functions check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level functions that configure multiple attributes perform
        instrument I/O only for the attributes whose value you change. Thus, you
        can safely call the high-level functions without the penalty of
        redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_real64(attribute_id, value)

        Args:
            attribute_id (int): The ID of an attribute.

            value (float): The value that you want to set the attribute to. Some values might not
                be valid depending on the current settings of the instrument session.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        value_ctype = visatype.ViReal64(value)  # case S150
        error_code = self._library.niScope_SetAttributeViReal64(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, attribute_id, value):
        '''_set_attribute_vi_string

        Sets the value of a ViString attribute.

        This is a low-level function that you can use to set the values of
        instrument-specific attributes and inherent IVI attributes. If the
        attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level functions that set most of the instrument
        attributes. Use the high-level driver functions as much as possible
        because they handle order dependencies and multithread locking for you.
        In addition, the high-level functions perform status checking only after
        setting all of the attributes. In contrast, when you set multiple
        attributes using the SetAttribute functions, the functions check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level functions that configure multiple attributes perform
        instrument I/O only for the attributes whose value you change. Thus, you
        can safely call the high-level functions without the penalty of
        redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_string(attribute_id, value)

        Args:
            attribute_id (int): The ID of an attribute.

            value (str): The value that you want to set the attribute to. Some values might not
                be valid depending on the current settings of the instrument session.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library.niScope_SetAttributeViString(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return


class Session(_SessionBase):
    '''An NI-SCOPE session to a National Instruments Digitizer.'''

    def __init__(self, resource_name, id_query=False, reset_device=False, options={}):
        '''An NI-SCOPE session to a National Instruments Digitizer.

        Performs the following initialization actions:

        -  Creates a new IVI instrument driver and optionally sets the initial
           state of the following session properties: Range Check, Cache,
           Simulate, Record Value Coercions
        -  Opens a session to the specified device using the interface and
           address you specify for the **resourceName**
        -  Resets the digitizer to a known state if **resetDevice** is set to
           VI_TRUE
        -  Queries the instrument ID and verifies that it is valid for this
           instrument driver if the **IDQuery** is set to VI_TRUE
        -  Returns an instrument handle that you use to identify the instrument
           in all subsequent instrument driver function calls

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

                When you set this parameter to VI_TRUE, NI-SCOPE verifies that the
                device you initialize is a type that it supports.

                When you set this parameter to VI_FALSE, the function initializes the
                device without performing an ID query.

                **Defined Values**

                | VI_TRUE—Perform ID query
                | VI_FALSE—Skip ID query

                **Default Value**: VI_TRUE

            reset_device (bool): Specify whether to reset the device during the initialization process.

                Default Value: VI_TRUE

                **Defined Values**

                VI_TRUE (1)—Reset device

                VI_FALSE (0)—Do not reset device

                Note:
                For the NI 5112, repeatedly resetting the device may cause excessive
                wear on the electromechanical relays. Refer to `NI 5112
                Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
                for recommended programming practices.

            options (str): Specifies the initial value of certain attributes for the session. The
                syntax for **options** is a dictionary of attributes with an assigned
                value. For example:

                { 'simulate': False }

                You do not have to specify a value for all the attributes. If you do not
                specify a value for an attribute, the default value is used.

                Advanced Example:
                { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

                +-------------------------+---------+
                | Attribute               | Default |
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


        Returns:
            session (niscope.Session): A session object representing the device.

        '''
        super(Session, self).__init__(repeated_capability='', vi=None, library=None, encoding=None, freeze_it=False)
        options = _converters.convert_init_with_options_dictionary(options, self._encoding)
        self._library = library_singleton.get()
        self._encoding = 'windows-1251'

        # Call specified init function
        self._vi = 0  # This must be set before calling _init_with_options().
        self._vi = self._init_with_options(resource_name, id_query, reset_device, options)

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '')

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("id_query=" + pp.pformat(id_query))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def initiate(self):
        return _Acquisition(self)

    def close(self):
        try:
            self._close()
        except errors.Error as e:
            self._vi = 0
            raise
        self._vi = 0

    ''' These are code-generated '''

    def abort(self):
        '''abort

        Aborts an acquisition and returns the digitizer to the Idle state. Call
        this function if the digitizer times out waiting for a trigger.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_Abort(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def acquisition_status(self):
        '''acquisition_status

        Returns status information about the acquisition to the **status**
        output parameter.

        Returns:
            acquisition_status (enums.AcquisitionStatus): Returns whether the acquisition is complete, in progress, or unknown.

                **Defined Values**

                AcquisitionStatus.COMPLETE

                AcquisitionStatus.IN_PROGRESS

                AcquisitionStatus.STATUS_UNKNOWN

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        acquisition_status_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niScope_AcquisitionStatus(vi_ctype, None if acquisition_status_ctype is None else (ctypes.pointer(acquisition_status_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.AcquisitionStatus(acquisition_status_ctype.value)

    def auto_setup(self):
        '''auto_setup

        Automatically configures the instrument. When you call this function,
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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_AutoSetup(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self):
        '''commit

        Commits to hardware all the parameter settings associated with the task.
        Use this function if you want a parameter change to be immediately
        reflected in the hardware. This function is not supported for
        Traditional NI-DAQ (Legacy) devices.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_horizontal_timing(self, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime):
        '''configure_horizontal_timing

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
                One or more of the referenced functions are not in the Python API for this driver.

            ref_position (float): The position of the Reference Event in the waveform record specified as
                a percentage.

            num_records (int): The number of records to acquire

            enforce_realtime (bool): Indicates whether the digitizer enforces real-time measurements or
                allows equivalent-time (RIS) measurements; not all digitizers support
                RIS—refer to `Features Supported by
                Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
                more information.

                Default value: VI_TRUE

                **Defined Values**

                VI_TRUE—Allow real-time acquisitions only

                VI_FALSE—Allow real-time and equivalent-time acquisitions

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        min_sample_rate_ctype = visatype.ViReal64(min_sample_rate)  # case S150
        min_num_pts_ctype = visatype.ViInt32(min_num_pts)  # case S150
        ref_position_ctype = visatype.ViReal64(ref_position)  # case S150
        num_records_ctype = visatype.ViInt32(num_records)  # case S150
        enforce_realtime_ctype = visatype.ViBoolean(enforce_realtime)  # case S150
        error_code = self._library.niScope_ConfigureHorizontalTiming(vi_ctype, min_sample_rate_ctype, min_num_pts_ctype, ref_position_ctype, num_records_ctype, enforce_realtime_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_ref_levels(self, low=10.0, mid=50.0, high=90.0):
        '''configure_ref_levels

        This function is included for compliance with the IviScope Class
        Specification.

        Configures the reference levels for all channels of the digitizer. The
        levels may be set on a per channel basis by setting
        meas_chan_high_ref_level,
        meas_chan_low_ref_level, and
        meas_chan_mid_ref_level

        This function configures the reference levels for waveform measurements.
        Call this function before calling fetch_measurement to take a
        rise time, fall time, width negative, width positive, duty cycle
        negative, or duty cycle positive measurement.

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        low_ctype = visatype.ViReal64(low)  # case S150
        mid_ctype = visatype.ViReal64(mid)  # case S150
        high_ctype = visatype.ViReal64(high)  # case S150
        error_code = self._library.niScope_ConfigureRefLevels(vi_ctype, low_ctype, mid_ctype, high_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_digital(self, trigger_source, slope=enums.TriggerSlope.POSITIVE, holdoff=0.0, delay=0.0):
        '''configure_trigger_digital

        Configures the common properties of a digital trigger.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) attribute. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        function such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger function, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        Note:
        For multirecord acquisitions, all records after the first record are
        started by using the Advance Trigger Source. The default is immediate.

        You can adjust the amount of pre-trigger and post-trigger samples using
        the reference position parameter on the
        configure_horizontal_timing function. The default is half of the
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

            holdoff (float): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (float): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        if type(slope) is not enums.TriggerSlope:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerSlope))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        slope_ctype = visatype.ViInt32(slope.value)  # case S130
        holdoff_ctype = visatype.ViReal64(holdoff)  # case S150
        delay_ctype = visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerDigital(vi_ctype, trigger_source_ctype, slope_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_edge(self, trigger_source, trigger_coupling, level=0.0, slope=enums.TriggerSlope.POSITIVE, holdoff=0.0, delay=0.0):
        '''configure_trigger_edge

        Configures common properties for analog edge triggering.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) attribute. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        function such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger function, you specify
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

            trigger_coupling (enums.TriggerCoupling): Applies coupling and filtering options to the trigger signal. Refer to
                trigger_coupling for more information.

            level (float): The voltage threshold for the trigger. Refer to
                trigger_level for more information.

            slope (enums.TriggerSlope): Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to trigger_slope for more
                information.

            holdoff (float): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (float): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        if type(slope) is not enums.TriggerSlope:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerSlope))
        if type(trigger_coupling) is not enums.TriggerCoupling:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerCoupling))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        level_ctype = visatype.ViReal64(level)  # case S150
        slope_ctype = visatype.ViInt32(slope.value)  # case S130
        trigger_coupling_ctype = visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = visatype.ViReal64(holdoff)  # case S150
        delay_ctype = visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerEdge(vi_ctype, trigger_source_ctype, level_ctype, slope_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_hysteresis(self, trigger_source, trigger_coupling, level=0.0, hysteresis=0.05, slope=enums.TriggerSlope.POSITIVE, holdoff=0.0, delay=0.0):
        '''configure_trigger_hysteresis

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
        function such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger function, you specify
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

            trigger_coupling (enums.TriggerCoupling): Applies coupling and filtering options to the trigger signal. Refer to
                trigger_coupling for more information.

            level (float): The voltage threshold for the trigger. Refer to
                trigger_level for more information.

            hysteresis (float): The size of the hysteresis window on either side of the **level** in
                volts; the digitizer triggers when the trigger signal passes through the
                hysteresis value you specify with this parameter, has the slope you
                specify with **slope**, and passes through the **level**. Refer to
                trigger_hysteresis for defined values.

            slope (enums.TriggerSlope): Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to trigger_slope for more
                information.

            holdoff (float): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (float): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        if type(slope) is not enums.TriggerSlope:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerSlope))
        if type(trigger_coupling) is not enums.TriggerCoupling:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerCoupling))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        level_ctype = visatype.ViReal64(level)  # case S150
        hysteresis_ctype = visatype.ViReal64(hysteresis)  # case S150
        slope_ctype = visatype.ViInt32(slope.value)  # case S130
        trigger_coupling_ctype = visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = visatype.ViReal64(holdoff)  # case S150
        delay_ctype = visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerHysteresis(vi_ctype, trigger_source_ctype, level_ctype, hysteresis_ctype, slope_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_immediate(self):
        '''configure_trigger_immediate

        Configures common properties for immediate triggering. Immediate
        triggering means the digitizer triggers itself.

        When you initiate an acquisition, the digitizer waits for a trigger. You
        specify the type of trigger that the digitizer waits for with a
        Configure Trigger function, such as configure_trigger_immediate.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_ConfigureTriggerImmediate(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_software(self, holdoff=0.0, delay=0.0):
        '''configure_trigger_software

        Configures common properties for software triggering.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) attribute. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        function such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger function, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        To trigger the acquisition, use send_software_trigger_edge.

        Note:
        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Args:
            holdoff (float): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (float): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        holdoff_ctype = visatype.ViReal64(holdoff)  # case S150
        delay_ctype = visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerSoftware(vi_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_video(self, trigger_source, signal_format, event, polarity, trigger_coupling, enable_dc_restore=False, line_number=1, holdoff=0.0, delay=0.0):
        '''configure_trigger_video

        Configures the common properties for video triggering, including the
        signal format, TV event, line number, polarity, and enable DC restore. A
        video trigger occurs when the digitizer finds a valid video signal sync.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) attribute. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        function such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger function, you specify
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

            holdoff (float): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (float): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        if type(signal_format) is not enums.VideoSignalFormat:
            raise TypeError('Parameter mode must be of type ' + str(enums.VideoSignalFormat))
        if type(event) is not enums.VideoTriggerEvent:
            raise TypeError('Parameter mode must be of type ' + str(enums.VideoTriggerEvent))
        if type(polarity) is not enums.VideoPolarity:
            raise TypeError('Parameter mode must be of type ' + str(enums.VideoPolarity))
        if type(trigger_coupling) is not enums.TriggerCoupling:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerCoupling))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        enable_dc_restore_ctype = visatype.ViBoolean(enable_dc_restore)  # case S150
        signal_format_ctype = visatype.ViInt32(signal_format.value)  # case S130
        event_ctype = visatype.ViInt32(event.value)  # case S130
        line_number_ctype = visatype.ViInt32(line_number)  # case S150
        polarity_ctype = visatype.ViInt32(polarity.value)  # case S130
        trigger_coupling_ctype = visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = visatype.ViReal64(holdoff)  # case S150
        delay_ctype = visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerVideo(vi_ctype, trigger_source_ctype, enable_dc_restore_ctype, signal_format_ctype, event_ctype, line_number_ctype, polarity_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_window(self, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff=0.0, delay=0.0):
        '''configure_trigger_window

        Configures common properties for analog window triggering. A window
        trigger occurs when a signal enters or leaves a window you specify with
        the **high level** or **low level** parameters.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) attribute. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        function such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger function, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        To trigger the acquisition, use send_software_trigger_edge.

        Note:
        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

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

            holdoff (float): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (float): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        '''
        if type(window_mode) is not enums.TriggerWindowMode:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerWindowMode))
        if type(trigger_coupling) is not enums.TriggerCoupling:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerCoupling))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        low_level_ctype = visatype.ViReal64(low_level)  # case S150
        high_level_ctype = visatype.ViReal64(high_level)  # case S150
        window_mode_ctype = visatype.ViInt32(window_mode.value)  # case S130
        trigger_coupling_ctype = visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = visatype.ViReal64(holdoff)  # case S150
        delay_ctype = visatype.ViReal64(delay)  # case S150
        error_code = self._library.niScope_ConfigureTriggerWindow(vi_ctype, trigger_source_ctype, low_level_ctype, high_level_ctype, window_mode_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):
        '''disable

        Aborts any current operation, opens data channel relays, and releases
        RTSI and PFI lines.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_signal(self, signal, output_terminal, signal_identifier="None"):
        '''export_signal

        Configures the digitizer to generate a signal that other devices can
        detect when configured for digital triggering or sharing clocks. The
        **signal** parameter specifies what condition causes the digitizer to
        generate the signal. The **outputTerminal** parameter specifies where to
        send the signal on the hardware (such as a PFI connector or RTSI line).

        In cases where multiple instances of a particular signal exist, use the
        **signalIdentifier** input to specify which instance to control. For
        normal signals, only one instance exists and you should leave this
        parameter set to the empty string. You can call this function multiple
        times and set each available line to a different signal.

        To unprogram a specific line on device, call this function with the
        signal you no longer want to export and set **outputTerminal** to
        NISCOPE_VAL_NONE.

        Note: This function replaces ConfigureTriggerOutput.

        Note:
        One or more of the referenced functions are not in the Python API for this driver.

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        Args:
            signal (enums.ExportableSignals): signal (clock, trigger, or event) to export.

                **Defined Values**

                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
                | ExportableSignals.REF_TRIGGER              | (1)   | Generate a pulse when detecting the Stop/Reference trigger.                                     |
                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
                | ExportableSignals.START_TRIGGER            | (2)   | Generate a pulse when detecting a Start trigger.                                                |
                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
                | ExportableSignals.END_OF_ACQUISITION_EVENT | (3)   | Generate a pulse when the acquisition finishes.                                                 |
                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
                | ExportableSignals.END_OF_RECORD_EVENT      | (4)   | Generate a pulse at the end of the record.                                                      |
                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
                | ExportableSignals.ADVANCE_TRIGGER          | (5)   | Generate a pulse when detecting an Advance trigger.                                             |
                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
                | ExportableSignals.READY_FOR_ADVANCE_EVENT  | (6)   | Asserts when the digitizer is ready to advance to the next record.                              |
                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
                | ExportableSignals.READY_FOR_START_EVENT    | (7)   | Asserts when the digitizer is initiated and ready to accept a Start trigger and begin sampling. |
                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
                | ExportableSignals.READY_FOR_REF_EVENT      | (10)  | Asserts when the digitizer is ready to accept a Reference trigger.                              |
                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
                | ExportableSignals.REF_CLOCK                | (100) | Export the Reference clock for the digitizer to the specified terminal.                         |
                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
                | ExportableSignals.SAMPLE_CLOCK             | (101) | Export the Sample clock for the digitizer to the specified terminal.                            |
                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
                | ExportableSignals._5V_OUT                  | (13)  | Exports a 5 V power supply.                                                                     |
                +--------------------------------------------+-------+-------------------------------------------------------------------------------------------------+

            output_terminal (str): Identifies the hardware signal line on which the digital pulse is
                generated.

                **Defined Values**

                +----------------------+------------------+
                | NISCOPE_VAL_RTSI_0   | ("VAL_RTSI_0")   |
                +----------------------+------------------+
                | NISCOPE_VAL_RTSI_1   | ("VAL_RTSI_1")   |
                +----------------------+------------------+
                | NISCOPE_VAL_RTSI_2   | ("VAL_RTSI_2")   |
                +----------------------+------------------+
                | NISCOPE_VAL_RTSI_3   | ("VAL_RTSI_3")   |
                +----------------------+------------------+
                | NISCOPE_VAL_RTSI_4   | ("VAL_RTSI_4")   |
                +----------------------+------------------+
                | NISCOPE_VAL_RTSI_5   | ("VAL_RTSI_5")   |
                +----------------------+------------------+
                | NISCOPE_VAL_RTSI_6   | ("VAL_RTSI_6")   |
                +----------------------+------------------+
                | NISCOPE_VAL_RTSI_7   | ("VAL_RTSI_7")   |
                +----------------------+------------------+
                | NISCOPE_VAL_PXI_STAR | ("VAL_PXI_STAR") |
                +----------------------+------------------+
                | NISCOPE_VAL_PFI_0    | ("VAL_PFI_0")    |
                +----------------------+------------------+
                | NISCOPE_VAL_PFI_1    | ("VAL_PFI_1")    |
                +----------------------+------------------+
                | NISCOPE_VAL_PFI_2    | ("VAL_PFI_2")    |
                +----------------------+------------------+
                | NISCOPE_VAL_CLK_OUT  | ("VAL_CLK_OUT")  |
                +----------------------+------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            signal_identifier (str): Describes the signal being exported.

        '''
        if type(signal) is not enums.ExportableSignals:
            raise TypeError('Parameter mode must be of type ' + str(enums.ExportableSignals))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        signal_ctype = visatype.ViInt32(signal.value)  # case S130
        signal_identifier_ctype = ctypes.create_string_buffer(signal_identifier.encode(self._encoding))  # case C020
        output_terminal_ctype = ctypes.create_string_buffer(output_terminal.encode(self._encoding))  # case C020
        error_code = self._library.niScope_ExportSignal(vi_ctype, signal_ctype, signal_identifier_ctype, output_terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=""):
        '''_init_with_options

        Performs the following initialization actions:

        -  Creates a new IVI instrument driver and optionally sets the initial
           state of the following session properties: Range Check, Cache,
           Simulate, Record Value Coercions
        -  Opens a session to the specified device using the interface and
           address you specify for the **resourceName**
        -  Resets the digitizer to a known state if **resetDevice** is set to
           VI_TRUE
        -  Queries the instrument ID and verifies that it is valid for this
           instrument driver if the **IDQuery** is set to VI_TRUE
        -  Returns an instrument handle that you use to identify the instrument
           in all subsequent instrument driver function calls

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

                When you set this parameter to VI_TRUE, NI-SCOPE verifies that the
                device you initialize is a type that it supports.

                When you set this parameter to VI_FALSE, the function initializes the
                device without performing an ID query.

                **Defined Values**

                | VI_TRUE—Perform ID query
                | VI_FALSE—Skip ID query

                **Default Value**: VI_TRUE

            reset_device (bool): Specify whether to reset the device during the initialization process.

                Default Value: VI_TRUE

                **Defined Values**

                VI_TRUE (1)—Reset device

                VI_FALSE (0)—Do not reset device

                Note:
                For the NI 5112, repeatedly resetting the device may cause excessive
                wear on the electromechanical relays. Refer to `NI 5112
                Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
                for recommended programming practices.

            option_string (str): | Specifies initialization commands. The following table lists the
                  attributes and the name you use in the **optionString** to identify
                  the attribute.

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
                subsequent NI-SCOPE function calls.

        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = visatype.ViSession()  # case S200
        error_code = self._library.niScope_InitWithOptions(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate_acquisition(self):
        '''_initiate_acquisition

        Initiates a waveform acquisition.

        After calling this function, the digitizer leaves the Idle state and
        waits for a trigger. The digitizer acquires a waveform for each channel
        you enable with configure_vertical.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_InitiateAcquisition(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def probe_compensation_signal_start(self):
        '''probe_compensation_signal_start

        Starts the 1 kHz square wave output on PFI 1 for probe compensation.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_ProbeCompensationSignalStart(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def probe_compensation_signal_stop(self):
        '''probe_compensation_signal_stop

        Stops the 1 kHz square wave output on PFI 1 for probe compensation.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_ProbeCompensationSignalStop(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_device(self):
        '''reset_device

        Performs a hard reset of the device. Acquisition stops, all routes are
        released, RTSI and PFI lines are tristated, hardware is configured to
        its default state, and all session attributes are reset to their default
        state.

        -  `Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):
        '''reset_with_defaults

        Performs a software reset of the device, returning it to the default
        state and applying any initial default settings from the IVI
        Configuration Store.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger_edge(self, which_trigger):
        '''send_software_trigger_edge

        Sends the selected trigger to the digitizer. Call this function if you
        called configure_trigger_software when you want the Reference
        trigger to occur. You can also call this function to override a misused
        edge, digital, or hysteresis trigger. If you have configured
        acq_arm_source, arm_ref_trig_src, or
        adv_trig_src, call this function when you want to send
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
            raise TypeError('Parameter mode must be of type ' + str(enums.WhichTrigger))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        which_trigger_ctype = visatype.ViInt32(which_trigger.value)  # case S130
        error_code = self._library.niScope_SendSoftwareTriggerEdge(vi_ctype, which_trigger_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        '''_close

        When you are finished using an instrument driver session, you must call
        this function to perform the following actions:

        -  Closes the instrument I/O session.
        -  Destroys the IVI session and all of its attributes.
        -  Deallocates any memory resources used by the IVI session.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset(self):
        '''reset

        Stops the acquisition, releases routes, and all session attributes are
        reset to their `default
        states <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cviattribute_defaults)>`__.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niScope_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):
        '''self_test

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = visatype.ViInt16()  # case S200
        self_test_message_ctype = (visatype.ViChar * 256)()  # case C070
        error_code = self._library.niScope_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



