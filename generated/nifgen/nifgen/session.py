# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes
# Used by @ivi_synchronized
from functools import wraps

import nifgen._attributes as _attributes
import nifgen._converters as _converters
import nifgen._library_singleton as _library_singleton
import nifgen._visatype as _visatype
import nifgen.enums as enums
import nifgen.errors as errors

import hightime
import nitclk

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
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
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


class _Generation(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate_generation()

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

        return _SessionBase(vi=self._session._vi, repeated_capability_list=complete_rep_cap_list, library=self._session._library, encoding=self._session._encoding, freeze_it=True)


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
    '''Base class for all NI-FGEN sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    absolute_delay = _attributes.AttributeViReal64(1150413)
    '''Type: float

    Specifies the sub-Sample Clock delay, in seconds, to apply to the
    waveform. Use this property to reduce the trigger jitter when
    synchronizing multiple devices with NI-TClk. This property can also help
    maintain synchronization repeatability by writing the absolute delay
    value of a previous measurement to the current session.
    To set this property, the waveform generator must be in the Idle
    (Configuration) state.
    **Units**: seconds (s)
    **Valid Values**: Plus or minus half of one Sample Clock period
    **Default Value**: 0.0
    **Supported Waveform Generators**: PXIe-5413/5423/5433

    Note:
    If this property is set, NI-TClk cannot perform any sub-Sample Clock
    adjustment.
    '''
    all_marker_events_latched_status = _attributes.AttributeViInt32(1150349)
    '''Type: int

    Returns a bit field of the latched status of all Marker Events.  Write 0 to this property to clear the latched status of all Marker Events.
    '''
    all_marker_events_live_status = _attributes.AttributeViInt32(1150344)
    '''Type: int

    Returns a bit field of the live status of all Marker Events.
    '''
    analog_data_mask = _attributes.AttributeViInt32(1150234)
    '''Type: int

    Specifies the mask to apply to the analog output. The masked data is replaced with the data in analog_static_value.
    '''
    analog_filter_enabled = _attributes.AttributeViBoolean(1150103)
    '''Type: bool

    Controls whether the signal generator applies to an analog filter to the output signal. This property is valid in arbitrary waveform, arbitrary sequence, and script modes. This property can also be used in standard method and frequency list modes for user-defined waveforms.
    '''
    analog_path = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AnalogPath, 1150222)
    '''Type: enums.AnalogPath

    Specifies the analog signal path that should be used. The main path allows you to configure gain, offset, analog filter status, output impedance, and output enable. The main path has two amplifier options, high- and low-gain.
    The direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The direct path also provides a smaller output range but also lower distortion. NI-FGEN normally chooses the amplifier based on the user-specified gain.
    '''
    analog_static_value = _attributes.AttributeViInt32(1150235)
    '''Type: int

    Specifies the static value that replaces data masked by analog_data_mask.
    '''
    arb_gain = _attributes.AttributeViReal64(1250202)
    '''Type: float

    Specifies the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to scale the arbitrary waveform to other ranges.
    For example, when you set this property to 2.0, the output signal ranges from -2.0 V to +2.0 V.
    Use this property when output_mode is set to OutputMode.ARB or OutputMode.SEQ.
    '''
    arb_marker_position = _attributes.AttributeViInt32(1150327)
    '''Type: int

    Specifies the position for a marker to be asserted in the arbitrary waveform. This property defaults to -1 when no marker position is specified. Use this property when output_mode is set to OutputMode.ARB.
    Use ExportSignal to export the marker signal.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nifgen.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nifgen.Session repeated capabilities container, and calling set/get value on the result.
    '''
    arb_offset = _attributes.AttributeViReal64(1250203)
    '''Type: float

    Specifies the value that the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to shift the arbitrary waveform range.
    For example, when you set this property to 1.0, the output signal ranges from 2.0 V to 0.0 V.
    Use this property when output_mode is set to OutputMode.ARB or OutputMode.SEQ.
    Units: Volts
    '''
    arb_repeat_count = _attributes.AttributeViInt32(1150328)
    '''Type: int

    Specifies number of times to repeat the arbitrary waveform when the triggerMode parameter of ConfigureTriggerMode is set to TriggerMode.SINGLE or TriggerMode.STEPPED. This property is ignored if the triggerMode parameter is set to TriggerMode.CONTINUOUS or TriggerMode.BURST. Use this property when output_mode is set to OutputMode.ARB.
    When used during streaming, this property specifies the number of times to repeat the streaming waveform (the onboard memory allocated for streaming).  For more information about streaming, refer to the Streaming topic.
    '''
    arb_sample_rate = _attributes.AttributeViReal64(1250204)
    '''Type: float

    Specifies the rate at which the signal generator outputs the points in arbitrary waveforms.  Use this property when output_mode is set  to OutputMode.ARB or OutputMode.SEQ.
    Units: Samples/s
    '''
    arb_sequence_handle = _attributes.AttributeViInt32(1250211)
    '''Type: int

    This channel-based property identifies which sequence the signal generator produces. You can create multiple sequences using create_arb_sequence. create_arb_sequence returns a handle that you can use to identify the particular sequence. To configure the signal generator to produce a particular sequence, set this property to the sequence handle.
    Use this property only when output_mode is set to OutputMode.SEQ.
    '''
    arb_waveform_handle = _attributes.AttributeViInt32(1250201)
    '''Type: int

    Selects which arbitrary waveform the signal generator produces. You can create multiple arbitrary waveforms using one of the following niFgen Create Waveform methods:
    create_waveform
    create_waveform
    create_waveform_from_file_i16
    create_waveform_from_file_f64
    CreateWaveformFromFileHWS
    These methods return a handle that you can use to identify the particular waveform. To configure the signal generator to produce a particular waveform, set this property to the waveform handle.
    Use this property only when output_mode is set to OutputMode.ARB.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    aux_power_enabled = _attributes.AttributeViBoolean(1150411)
    '''Type: bool

    Controls the specified auxiliary power pin. Setting this property to TRUE energizes the auxiliary power when the session is committed. When this property is FALSE, the power pin of the connector outputs no power.
    '''
    bus_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.BusType, 1150215)
    '''Type: enums.BusType

    The bus type of the signal generator.
    '''
    channel_delay = _attributes.AttributeViReal64(1150369)
    '''Type: float

    Specifies, in seconds, the delay to apply to the analog output of the channel specified by the channel string. You can use the channel delay to configure the timing relationship between channels on a multichannel device. Values for this property can be zero or positive. A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds.
    '''
    clock_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ClockMode, 1150110)
    '''Type: enums.ClockMode

    Controls which clock mode is used for the signal generator.
    For signal generators that support it, this property allows switching the sample  clock to High-Resolution mode. When in Divide-Down  mode, the sample rate can only be set to certain frequences, based on  dividing down the update clock. However, in High-Resolution mode, the  sample rate may be set to any value.
    '''
    common_mode_offset = _attributes.AttributeViReal64(1150366)
    '''Type: float

    Specifies, in volts, the value the signal generator adds to or subtracts from the arbitrary waveform data. This property applies only when you set the terminal_configuration property to TerminalConfiguration.DIFFERENTIAL. Common mode offset is applied to the signals generated at each differential output terminal.
    '''
    data_marker_events_count = _attributes.AttributeViInt32(1150273)
    '''Type: int

    Returns the number of Data Marker Events supported by the device.
    '''
    data_marker_event_data_bit_number = _attributes.AttributeViInt32(1150337)
    '''Type: int

    Specifies the bit number to assign to the Data Marker Event.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nifgen.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nifgen.Session repeated capabilities container, and calling set/get value on the result.
    '''
    data_marker_event_level_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DataMarkerEventLevelPolarity, 1150338)
    '''Type: enums.DataMarkerEventLevelPolarity

    Specifies the output polarity of the Data marker event.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nifgen.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nifgen.Session repeated capabilities container, and calling set/get value on the result.
    '''
    data_marker_event_output_terminal = _attributes.AttributeViString(1150339)
    '''Type: str

    Specifies the destination terminal for the Data Marker Event.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nifgen.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nifgen.Session repeated capabilities container, and calling set/get value on the result.
    '''
    data_transfer_block_size = _attributes.AttributeViInt32(1150241)
    '''Type: int

    The number of samples at a time to download to onboard memory. Useful when the total data to be transferred to onboard memory is large.
    '''
    data_transfer_maximum_bandwidth = _attributes.AttributeViReal64(1150373)
    '''Type: float

    Specifies the maximum amount of bus bandwidth (in bytes per second) to use for data transfers. The signal generator limits data transfer speeds on the PCIe bus to the value you specify for this property. Set this property to optimize bus bandwidth usage for multi-device streaming applications by preventing the signal generator from consuming all of the available bandwidth on a PCI express link when waveforms are being written to the onboard memory of the device.
    '''
    data_transfer_maximum_in_flight_reads = _attributes.AttributeViInt32(1150375)
    '''Type: int

    Specifies the maximum number of concurrent PCI Express read requests the signal generator can issue.
    When transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this property is set to the highest value the signal generator supports.
    If other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the NI signal generator issues. This helps to reduce the amount of data the signal generator reads at one time.
    '''
    data_transfer_preferred_packet_size = _attributes.AttributeViInt32(1150374)
    '''Type: int

    Specifies the preferred size of the data field in a PCI Express read request packet. In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.
    Recommended values for this property are powers of two between 64 and 512.
    In some cases, the signal generator generates packets smaller than  the preferred size you set with this property.
    You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the abort method or wait for the generation to complete.

    Note:
    :
    '''
    digital_data_mask = _attributes.AttributeViInt32(1150236)
    '''Type: int

    Specifies the mask to apply to the output on the digital connector. The masked data is replaced with the data in digital_static_value.
    '''
    digital_edge_script_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerDigitalEdgeEdge, 1150292)
    '''Type: enums.ScriptTriggerDigitalEdgeEdge

    Specifies the active edge for the Script trigger. This property is used when script_trigger_type is set to Digital Edge.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nifgen.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nifgen.Session repeated capabilities container, and calling set/get value on the result.
    '''
    digital_edge_script_trigger_source = _attributes.AttributeViString(1150291)
    '''Type: str

    Specifies the source terminal for the Script trigger. This property is used when script_trigger_type is set to Digital Edge.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nifgen.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nifgen.Session repeated capabilities container, and calling set/get value on the result.
    '''
    digital_edge_start_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.StartTriggerDigitalEdgeEdge, 1150282)
    '''Type: enums.StartTriggerDigitalEdgeEdge

    Specifies the active edge for the Start trigger. This property is used only when start_trigger_type is set to Digital Edge.
    '''
    digital_edge_start_trigger_source = _attributes.AttributeViString(1150281)
    '''Type: str

    Specifies the source terminal for the Start trigger. This property is used only when start_trigger_type is set to Digital Edge.
    '''
    digital_filter_enabled = _attributes.AttributeViBoolean(1150102)
    '''Type: bool

    Controls whether the signal generator applies a digital filter to the output signal. This property is valid in arbitrary waveform, arbitrary sequence, and script modes. This property can also be used in standard method and frequency list modes for user-defined waveforms.
    '''
    digital_filter_interpolation_factor = _attributes.AttributeViReal64(1150218)
    '''Type: float

    This property only affects the device when digital_filter_enabled is set to True. If you do not set this property directly, NI-FGEN automatically selects the maximum interpolation factor allowed for the current sample rate. Valid values are 2, 4, and 8.
    '''
    digital_gain = _attributes.AttributeViReal64(1150254)
    '''Type: float

    Specifies a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the DAC. For a digital gain greater than 1.0, the product of digital gain times the generated data must be inside the range plus or minus 1.0 (assuming floating point data).  If the product exceeds these limits, the signal generator clips the output signal, and an error results.
    Some signal generators support both digital gain and an analog gain (analog gain is specified with the func_amplitude property or the arb_gain property). Digital gain can be changed during generation without the glitches that may occur when changing analog gains, due to relay switching. However, the DAC output resolution is a method of analog gain, so only analog gain makes full use of the resolution of the DAC.
    '''
    digital_pattern_enabled = _attributes.AttributeViBoolean(1150101)
    '''Type: bool

    Controls whether the signal generator generates a digital pattern of the output signal.
    '''
    digital_static_value = _attributes.AttributeViInt32(1150237)
    '''Type: int

    Specifies the static value that replaces data masked by digital_data_mask.
    '''
    done_event_output_terminal = _attributes.AttributeViString(1150315)
    '''Type: str

    Specifies the destination terminal for the Done Event.
    '''
    driver_setup = _attributes.AttributeViString(1050007)
    '''Type: str

    Specifies the driver setup portion of the option string that was passed into the InitWithOptions method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    exported_onboard_reference_clock_output_terminal = _attributes.AttributeViString(1150322)
    '''Type: str

    Specifies the terminal to which to export the Onboard Reference Clock.
    '''
    exported_reference_clock_output_terminal = _attributes.AttributeViString(1150321)
    '''Type: str

    Specifies the terminal to which to export the Reference Clock.
    '''
    exported_sample_clock_divisor = _attributes.AttributeViInt32(1150219)
    '''Type: int

    Specifies the factor by which to divide the Sample clock, also known as the Update clock, before it is exported.  To export the Sample clock, use the ExportSignal method or the  exported_sample_clock_output_terminal property.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    exported_sample_clock_output_terminal = _attributes.AttributeViString(1150320)
    '''Type: str

    Specifies the terminal to which to export the Sample Clock.
    '''
    exported_sample_clock_timebase_divisor = _attributes.AttributeViInt32(1150230)
    '''Type: int

    Specifies the factor by which to divide the sample clock timebase (board clock) before it is exported.  To export the Sample clock timebase, use the ExportSignal method or the  exported_sample_clock_timebase_output_terminal property.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    exported_sample_clock_timebase_output_terminal = _attributes.AttributeViString(1150329)
    '''Type: str

    Specifies the terminal to which to export the Sample clock timebase. If you specify a divisor with the exported_sample_clock_timebase_divisor property,   the Sample clock exported with the exported_sample_clock_timebase_output_terminal  property is the value of the Sample clock timebase after it is divided-down.  For a list of the terminals available on your device, refer to the Device Routes tab in MAX.
    To change the device configuration, call abort or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this property.
    '''
    exported_script_trigger_output_terminal = _attributes.AttributeViString(1150295)
    '''Type: str

    Specifies the output terminal for the exported Script trigger.
    Setting this property to an empty string means that when you commit the session, the signal is removed from that terminal and, if possible, the terminal is tristated.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nifgen.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nifgen.Session repeated capabilities container, and calling set/get value on the result.
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeViString(1150283)
    '''Type: str

    Specifies the destination terminal for exporting the Start trigger.
    '''
    external_clock_delay_binary_value = _attributes.AttributeViInt32(1150233)
    '''Type: int

    Binary value of the external clock delay.
    '''
    external_sample_clock_multiplier = _attributes.AttributeViReal64(1150376)
    '''Type: float

    Specifies a multiplication factor to use to obtain a desired sample rate from an external Sample clock.  The resulting sample rate is equal to this factor multiplied by the external Sample clock rate.  You can use this property to generate samples at a rate higher than your external clock rate.  When using this property, you do not need to explicitly set the external clock rate.
    '''
    file_transfer_block_size = _attributes.AttributeViInt32(1150240)
    '''Type: int

    The number of samples at a time to read from the file and download to onboard memory. Used in conjunction with the Create From File and Write From File methods.
    '''
    filter_correction_frequency = _attributes.AttributeViReal64(1150104)
    '''Type: float

    Controls the filter correction frequency of the analog filter. This property corrects for the ripples in the analog filter frequency response at the frequency specified. For standard waveform output, the filter correction frequency should be set to be the same as the frequency of the standard waveform. To have no filter correction, set this property to 0 Hz.
    '''
    flatness_correction_enabled = _attributes.AttributeViBoolean(1150323)
    '''Type: bool

    When True, the signal generator applies a flatness correction factor to the generated sine wave in order to ensure the same output power level at all frequencies.
    This property should be set to False when performing Flatness Calibration.
    '''
    fpga_bitfile_path = _attributes.AttributeViString(1150412)
    '''Type: str

    Gets the absolute file path to the bitfile loaded on the FPGA.
    '''
    freq_list_duration_quantum = _attributes.AttributeViReal64(1150214)
    '''Type: float

    Returns the quantum of which all durations must be a multiple in a  frequency list.
    '''
    freq_list_handle = _attributes.AttributeViInt32(1150208)
    '''Type: int

    Sets which frequency list the signal generator  produces. Create a frequency list using create_freq_list.  create_freq_list returns a handle that you can  use to identify the list.
    '''
    func_amplitude = _attributes.AttributeViReal64(1250102)
    '''Type: float

    Controls the amplitude of the standard waveform that the  signal generator produces. This value is the amplitude at the  output terminal.
    For example, to produce a waveform ranging from -5.00 V to +5.00 V, set  the amplitude to 10.00 V.
    set the Waveform parameter to Waveform.DC.
    Units: Vpk-pk

    Note: This parameter does not affect signal generator behavior when you
    '''
    func_buffer_size = _attributes.AttributeViInt32(1150238)
    '''Type: int

    This property contains the number of samples used in the standard method waveform  buffer. This property is only valid on devices that implement standard method mode  in software, and is read-only for all other devices.
    implementation of Standard Method Mode on your device.

    Note: Refer to the Standard Method Mode topic for more information on the
    '''
    func_dc_offset = _attributes.AttributeViReal64(1250103)
    '''Type: float

    Controls the DC offset of the standard waveform that the  signal generator produces.  This value is the offset at the output  terminal. The value is the offset from ground to the center of the  waveform that you specify with the Waveform parameter.
    For example, to configure a waveform with an amplitude of 10.00 V to  range from 0.00 V to +10.00 V, set DC Offset to 5.00 V.
    Units: volts
    '''
    func_duty_cycle_high = _attributes.AttributeViReal64(1250106)
    '''Type: float

    Controls the duty cycle of the square wave the signal generator  produces. Specify this property as a percentage of  the time the square wave is high in a cycle.
    set the Waveform parameter to Waveform.SQUARE.
    Units: Percentage of time the waveform is high

    Note: This parameter only affects signal generator behavior when you
    '''
    func_frequency = _attributes.AttributeViReal64(1250104)
    '''Type: float

    Controls the frequency of the standard waveform that the  signal generator produces.
    Units: hertz
    (1) This parameter does not affect signal generator behavior when you  set the Waveform parameter of the configure_standard_waveform method  to Waveform.DC.
    (2) For Waveform.SINE, the range is between 0 MHz and 16 MHz, but the  range is between 0 MHz and 1 MHz for all other waveforms.

    Note:
    :
    '''
    func_max_buffer_size = _attributes.AttributeViInt32(1150239)
    '''Type: int

    This property sets the maximum number of samples that can be used in the standard  method waveform buffer. Increasing this value may increase the quality of  the waveform. This property is only valid on devices that implement standard  method mode in software, and is read-only for all other devices.
    implementation of Standard Method Mode on your device.

    Note: Refer to the Standard Method Mode topic for more information on the
    '''
    func_start_phase = _attributes.AttributeViReal64(1250105)
    '''Type: float

    Controls horizontal offset of the standard waveform the  signal generator produces. Specify this property in degrees of  one waveform cycle.
    A start phase of 180 degrees means output generation begins halfway  through the waveform. A start phase of 360 degrees offsets the output by  an entire waveform cycle, which is identical to a start phase of 0  degrees.
    set the Waveform parameter to Waveform.DC.
    Units: Degrees of one cycle

    Note: This parameter does not affect signal generator behavior when you
    '''
    func_waveform = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Waveform, 1250101)
    '''Type: enums.Waveform

    This channel-based property specifies which standard waveform the signal generator produces.
    Use this property only when output_mode is set to  OutputMode.FUNC.
    Waveform.SINE      - Sinusoid waveform
    Waveform.SQUARE    - Square waveform
    Waveform.TRIANGLE  - Triangle waveform
    Waveform.RAMP_UP   - Positive ramp waveform
    Waveform.RAMP_DOWN - Negative ramp waveform
    Waveform.DC        - Constant voltage
    Waveform.NOISE     - White noise
    Waveform.USER      - User-defined waveform as defined with
    define_user_standard_waveform
    '''
    idle_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.IdleBehavior, 1150377)
    '''Type: enums.IdleBehavior

    Specifies the behavior of the output during the Idle state.  The output can be configured to hold the last generated voltage before entering the Idle state or jump to the Idle Value.
    '''
    idle_value = _attributes.AttributeViInt32(1150378)
    '''Type: int

    Specifies the value to generate in the Idle state.  The Idle Behavior must be configured to jump to this value.
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    A string that contains the firmware revision information  for the device that you are currently using.
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    A string that contains the name of the device manufacturer you are currently  using.
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    A string that contains the model number or name of the device that you  are currently using.
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    Indicates the resource descriptor that NI-FGEN uses to identify the physical device.
    If you initialize NI-FGEN with a logical name, this  property contains the resource descriptor that corresponds  to the entry in the IVI Configuration Utility.
    If you initialize NI-FGEN with the resource  descriptor, this property contains that value.
    '''
    load_impedance = _attributes.AttributeViReal64(1150220)
    '''Type: float

    This channel-based property specifies the load impedance connected to the analog output of the channel. If you set this property to NIFGEN_VAL_MATCHED_LOAD_IMPEDANCE (-1.0), NI-FGEN assumes that the load impedance matches the output impedance. NI-FGEN compensates to give the desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V).

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    A string containing the logical name that you specified when opening the  current IVI session.
    You may pass a logical name to init or  InitWithOptions.  The IVI Configuration Utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    marker_events_count = _attributes.AttributeViInt32(1150271)
    '''Type: int

    Returns the number of markers supported by the device. Use this property when output_mode is set to OutputMode.SCRIPT.
    '''
    marker_event_output_terminal = _attributes.AttributeViString(1150312)
    '''Type: str

    Specifies the destination terminal for the Marker Event.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nifgen.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nifgen.Session repeated capabilities container, and calling set/get value on the result.
    '''
    max_freq_list_duration = _attributes.AttributeViReal64(1150213)
    '''Type: float

    Returns the maximum duration of any one step in the frequency  list.
    '''
    max_freq_list_length = _attributes.AttributeViInt32(1150211)
    '''Type: int

    Returns the maximum number of steps that can be in a frequency  list.
    '''
    max_loop_count = _attributes.AttributeViInt32(1250215)
    '''Type: int

    Returns the maximum number of times that the signal generator can repeat a waveform in a sequence. Typically, this value is constant for the signal generator.
    '''
    max_num_freq_lists = _attributes.AttributeViInt32(1150209)
    '''Type: int

    Returns the maximum number of frequency lists the signal generator allows.
    '''
    max_num_sequences = _attributes.AttributeViInt32(1250212)
    '''Type: int

    Returns the maximum number of arbitrary sequences that the signal generator allows. Typically, this value is constant for the signal generator.
    '''
    max_num_waveforms = _attributes.AttributeViInt32(1250205)
    '''Type: int

    Returns the maximum number of arbitrary waveforms that the signal generator allows. Typically, this value is constant for the signal generator.
    '''
    max_sequence_length = _attributes.AttributeViInt32(1250214)
    '''Type: int

    Returns the maximum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.
    '''
    max_waveform_size = _attributes.AttributeViInt32(1250208)
    '''Type: int

    Returns the size, in samples, of the largest waveform that can be created. This property reflects the space currently available, taking into account previously allocated waveforms and instructions.
    '''
    memory_size = _attributes.AttributeViInt32(1150242)
    '''Type: int

    The total amount of memory, in bytes, on the signal generator.
    '''
    min_freq_list_duration = _attributes.AttributeViReal64(1150212)
    '''Type: float

    Returns the minimum number of steps that can be in a frequency  list.
    '''
    min_freq_list_length = _attributes.AttributeViInt32(1150210)
    '''Type: int

    Returns the minimum number of frequency lists that the signal generator allows.
    '''
    min_sequence_length = _attributes.AttributeViInt32(1250213)
    '''Type: int

    Returns the minimum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.
    '''
    min_waveform_size = _attributes.AttributeViInt32(1250207)
    '''Type: int

    Returns the minimum number of points that the signal generator allows in an arbitrary waveform. Typically, this value is constant for the signal generator.
    '''
    module_revision = _attributes.AttributeViString(1150390)
    '''Type: str

    A string that contains the module revision  for the device that you are currently using.
    '''
    channel_count = _attributes.AttributeViInt32(1050203)
    '''Type: int

    Indicates the number of channels that the specific instrument  driver supports.
    For each property for which IVI_VAL_MULTI_CHANNEL is set, the IVI Engine maintains a separate cache value for each channel.
    '''
    output_enabled = _attributes.AttributeViBoolean(1250003)
    '''Type: bool

    This channel-based property specifies whether the signal that the signal generator produces appears at the output connector.
    '''
    output_impedance = _attributes.AttributeViReal64(1250004)
    '''Type: float

    This channel-based property specifies the signal generator output impedance at the output connector. NI signal sources modules have an output impedance of 50 ohms and an optional 75 ohms on select modules. If the load impedance matches the output impedance, then the voltage at the signal output connector is at the needed level. The voltage at the signal output connector varies with load output impedance, up to doubling the voltage for a high-impedance load.
    '''
    output_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OutputMode, 1250001)
    '''Type: enums.OutputMode

    Sets which output mode the signal generator will use. The value you specify determines which methods and properties you use to configure the waveform the signal generator produces.

    Note: The signal generator must not be in the Generating state when you change this property. To change the device configuration, call abort or wait for the generation to complete.
    '''
    ready_for_start_event_output_terminal = _attributes.AttributeViString(1150310)
    '''Type: str

    Specifies the destination terminal for the Ready for Start Event.
    '''
    reference_clock_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ReferenceClockSource, 1150113)
    '''Type: enums.ReferenceClockSource

    Specifies the reference clock source used by the signal generator.
    The signal generator derives the frequencies and sample rates that it uses  to generate waveforms from the source you specify.  For example, when you set this property to ClkIn, the signal  generator uses the signal it receives at the CLK IN front  panel connector as the Reference clock.
    To change the device configuration, call abort or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this property.
    '''
    ref_clock_frequency = _attributes.AttributeViReal64(1150107)
    '''Type: float

    Sets the frequency of the signal generator reference  clock. The signal generator uses the reference clock to derive  frequencies and sample rates when generating output.
    '''
    sample_clock_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.SampleClockSource, 1150112)
    '''Type: enums.SampleClockSource

    Specifies the Sample clock source. If you specify a divisor with the exported_sample_clock_divisor  property, the Sample clock exported with the exported_sample_clock_output_terminal property is the  value of the Sample clock after it is divided-down. For a list of the terminals available on your device, refer  to the Device Routes tab in MAX.
    To change the device configuration, call abort or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this property.
    '''
    sample_clock_timebase_rate = _attributes.AttributeViReal64(1150368)
    '''Type: float

    Specifies the Sample clock timebase rate. This property applies only to external Sample clock timebases.
    To change the device configuration, call abort or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this property.
    '''
    sample_clock_timebase_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.SampleClockTimebaseSource, 1150367)
    '''Type: enums.SampleClockTimebaseSource

    Specifies the Sample Clock Timebase source.
    To change the device configuration, call the abort method or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this property.
    '''
    script_to_generate = _attributes.AttributeViString(1150270)
    '''Type: str

    Specifies which script the generator produces. To configure the generator to run a particular script, set this property to the name of the script. Use write_script to create multiple scripts. Use this property when output_mode is set to OutputMode.SCRIPT.

    Note: The signal generator must not be in the Generating state when you change this property. To change the device configuration, call abort or wait for the generation to complete.
    '''
    script_triggers_count = _attributes.AttributeViInt32(1150272)
    '''Type: int

    Specifies the number of Script triggers supported by the device. Use this property when output_mode is set to OutputMode.SCRIPT.
    '''
    script_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerType, 1150290)
    '''Type: enums.ScriptTriggerType

    Specifies the Script trigger type. Depending upon the value of this property, additional properties may need to be configured to fully configure the trigger.

    Tip:
    This property can use repeated capabilities. If set or get directly on the
    nifgen.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    nifgen.Session repeated capabilities container, and calling set/get value on the result.
    '''
    serial_number = _attributes.AttributeViString(1150243)
    '''Type: str

    The signal generator's serial number.
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Specifies whether to simulate NI-FGEN I/O  operations. If simulation is enabled, NI-FGEN  methods perform range checking and call Ivi_GetAttribute and  Ivi_SetAttribute, but they do not perform device I/O.   For output parameters that represent device data, NI-FGEN  methods return calculated values.
    Default Value: False
    Use InitWithOptions to override default value.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    Returns a brief description of NI-FGEN.
    '''
    major_version = _attributes.AttributeViInt32(1050503)
    '''Type: int

    Returns the major version number of NI-FGEN.
    '''
    minor_version = _attributes.AttributeViInt32(1050504)
    '''Type: int

    Returns the minor version number of NI-FGEN.
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    A string that contains additional version information about  NI-FGEN.
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    A string that contains the name of the vendor that supplies NI-FGEN.
    '''
    started_event_output_terminal = _attributes.AttributeViString(1150314)
    '''Type: str

    Specifies the destination terminal for the Started Event.
    '''
    start_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.StartTriggerType, 1150280)
    '''Type: enums.StartTriggerType

    Specifies whether you want the Start trigger to be a Digital Edge, or Software trigger. You can also choose None as the value for this property.
    '''
    streaming_space_available_in_waveform = _attributes.AttributeViInt32(1150325)
    '''Type: int

    Indicates the space available (in samples) in the streaming waveform for writing new data. During generation, this available space may be in multiple locations with, for example, part of the available space at the end of the streaming waveform and the rest at the beginning. In this situation, writing a block of waveform data the size of the  total space available in the streaming waveform causes NI-FGEN to return an error, as  NI-FGEN will not wrap the data from the end of the waveform to the beginning and cannot write data past the end of the waveform buffer.
    To avoid writing data past the end of the waveform, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform.
    Used in conjunction with the streaming_waveform_handle or streaming_waveform_name properties.
    '''
    streaming_waveform_handle = _attributes.AttributeViInt32(1150324)
    '''Type: int

    Specifies the waveform handle of the waveform used to continuously stream data during generation. This property defaults to -1 when no streaming waveform is specified.
    Used in conjunction with streaming_space_available_in_waveform.
    '''
    streaming_waveform_name = _attributes.AttributeViString(1150326)
    '''Type: str

    Specifies the name of the waveform used to continuously stream data during generation. This property defaults to // when no streaming waveform is specified.
    Use in conjunction with streaming_space_available_in_waveform.
    '''
    streaming_write_timeout = _attributes.AttributeViReal64TimeDeltaSeconds(1150409)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the maximum amount of time allowed to complete a streaming write operation.
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    Returns a model code of the device. For NI-FGEN versions that support more than one device, this  property contains a comma-separated list of supported device  models.
    '''
    terminal_configuration = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TerminalConfiguration, 1150365)
    '''Type: enums.TerminalConfiguration

    Specifies whether gain and offset values will be analyzed based on single-ended or differential operation.
    '''
    trigger_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerMode, 1150108)
    '''Type: enums.TriggerMode

    Controls the trigger mode.
    '''
    wait_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WaitBehavior, 1150379)
    '''Type: enums.WaitBehavior

    Specifies the behavior of the output while waiting for a script trigger or during a wait instruction.  The output can be configured to hold the last generated voltage before waiting or jump to the Wait Value.
    '''
    wait_value = _attributes.AttributeViInt32(1150380)
    '''Type: int

    Specifies the value to generate while waiting.  The Wait Behavior must be configured to jump to this value.
    '''
    waveform_quantum = _attributes.AttributeViInt32(1250206)
    '''Type: int

    The size of each arbitrary waveform must be a multiple of a quantum value. This property returns the quantum value that the signal generator allows.
    For example, when this property returns a value of 8, all waveform sizes must be a multiple of 8. Typically, this value is constant for the signal generator.
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

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.script_triggers = _RepeatedCapabilities(self, 'ScriptTrigger', repeated_capability_list)
        self.markers = _RepeatedCapabilities(self, 'Marker', repeated_capability_list)

        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nifgen', self.__class__.__name__, self._param_list)

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

    @ivi_synchronized
    def allocate_named_waveform(self, waveform_name, waveform_size):
        r'''allocate_named_waveform

        Specifies the size of a named waveform up front so that it can be
        allocated in onboard memory before loading the associated data. Data can
        then be loaded in smaller blocks with the niFgen Write (Binary16)
        Waveform methods.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            waveform_size (int): Specifies the size of the waveform to allocate in samples.

                **Default Value**: "4096"

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_size_ctype = _visatype.ViInt32(waveform_size)  # case S150
        error_code = self._library.niFgen_AllocateNamedWaveform(vi_ctype, channel_name_ctype, waveform_name_ctype, waveform_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def allocate_waveform(self, waveform_size):
        r'''allocate_waveform

        Specifies the size of a waveform so that it can be allocated in onboard
        memory before loading the associated data. Data can then be loaded in
        smaller blocks with the Write Binary 16 Waveform methods.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_size (int): Specifies, in samples, the size of the waveform to allocate.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(waveform_size)  # case S150
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_AllocateWaveform(vi_ctype, channel_name_ctype, waveform_size_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    @ivi_synchronized
    def clear_user_standard_waveform(self):
        r'''clear_user_standard_waveform

        Clears the user-defined waveform created by the
        define_user_standard_waveform method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niFgen_ClearUserStandardWaveform(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_arb_sequence(self, sequence_handle, gain, offset):
        r'''configure_arb_sequence

        Configures the signal generator properties that affect arbitrary
        sequence generation. Sets the arb_sequence_handle,
        arb_gain, and arb_offset properties.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            sequence_handle (int): Specifies the handle of the arbitrary sequence that you want the signal
                generator to produce. NI-FGEN sets the
                arb_sequence_handle property to this value. You can
                create an arbitrary sequence using the create_arb_sequence or
                create_advanced_arb_sequence method. These methods return a
                handle that you use to identify the sequence.

                **Default Value**: None

            gain (float): Specifies the factor by which the signal generator scales the arbitrary
                waveforms in the sequence. When you create an arbitrary waveform, you
                must first normalize the data points to a range of –1.00 to +1.00. You
                can use this parameter to scale the waveform to other ranges. The gain
                is applied before the offset is added.

                For example, to configure the output signal to range from –2.00 to
                +2.00 V, set **gain** to 2.00.

                **Units**: unitless

                **Default Value**: None

            offset (float): Specifies the value the signal generator adds to the arbitrary waveform
                data. When you create arbitrary waveforms, you must first normalize the
                data points to a range of –1.00 to +1.00 V. You can use this parameter
                to shift the range of the arbitrary waveform. NI-FGEN sets the
                arb_offset property to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        sequence_handle_ctype = _visatype.ViInt32(sequence_handle)  # case S150
        gain_ctype = _visatype.ViReal64(gain)  # case S150
        offset_ctype = _visatype.ViReal64(offset)  # case S150
        error_code = self._library.niFgen_ConfigureArbSequence(vi_ctype, channel_name_ctype, sequence_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_arb_waveform(self, waveform_handle, gain, offset):
        r'''configure_arb_waveform

        Configures the properties of the signal generator that affect arbitrary
        waveform generation. Sets the arb_waveform_handle,
        arb_gain, and arb_offset properties.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform you want the signal
                generator to produce. NI-FGEN sets the
                arb_waveform_handle property to this value. You can
                create an arbitrary waveform using one of the following niFgen Create
                Waveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64
                -  CreateWaveformFromFileHWS

                These methods return a handle that you use to identify the waveform.

                **Default Value**: None

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            gain (float): Specifies the factor by which the signal generator scales the arbitrary
                waveforms in the sequence. When you create an arbitrary waveform, you
                must first normalize the data points to a range of –1.00 to +1.00. You
                can use this parameter to scale the waveform to other ranges. The gain
                is applied before the offset is added.

                For example, to configure the output signal to range from –2.00 to
                +2.00 V, set **gain** to 2.00.

                **Units**: unitless

                **Default Value**: None

            offset (float): Specifies the value the signal generator adds to the arbitrary waveform
                data. When you create arbitrary waveforms, you must first normalize the
                data points to a range of –1.00 to +1.00 V. You can use this parameter
                to shift the range of the arbitrary waveform. NI-FGEN sets the
                arb_offset property to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        gain_ctype = _visatype.ViReal64(gain)  # case S150
        offset_ctype = _visatype.ViReal64(offset)  # case S150
        error_code = self._library.niFgen_ConfigureArbWaveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_freq_list(self, frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0):
        r'''configure_freq_list

        Configures the properties of the signal generator that affect frequency
        list generation (the freq_list_handle,
        func_amplitude, func_dc_offset, and
        func_start_phase properties).

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            frequency_list_handle (int): Specifies the handle of the frequency list that you want the signal
                generator to produce. NI-FGEN sets the freq_list_handle
                property to this value. You can create a frequency list using the
                create_freq_list method, which returns a handle that you use to
                identify the list.
                **Default Value**: None

            amplitude (float): Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the func_amplitude property to
                this value.

                For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
                the amplitude to 10.00 V.

                **Units**: peak-to-peak voltage

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                method to Waveform.DC.

            dc_offset (float): Specifies the DC offset of the standard waveform that you want the
                signal generator to produce. The value is the offset from ground to the
                center of the waveform you specify with the **waveform** parameter,
                observed at the output terminal. For example, to configure a waveform
                with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
                **dcOffset** to 5.00 V. NI-FGEN sets the func_dc_offset
                property to this value.

                **Units**: volts

                **Default Value**: None

            start_phase (float): Specifies the horizontal offset of the standard waveform you want the
                signal generator to produce. Specify this property in degrees of one
                waveform cycle. NI-FGEN sets the func_start_phase
                property to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: None degrees

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter to Waveform.DC.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        frequency_list_handle_ctype = _visatype.ViInt32(frequency_list_handle)  # case S150
        amplitude_ctype = _visatype.ViReal64(amplitude)  # case S150
        dc_offset_ctype = _visatype.ViReal64(dc_offset)  # case S150
        start_phase_ctype = _visatype.ViReal64(start_phase)  # case S150
        error_code = self._library.niFgen_ConfigureFreqList(vi_ctype, channel_name_ctype, frequency_list_handle_ctype, amplitude_ctype, dc_offset_ctype, start_phase_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def configure_standard_waveform(self, waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0):
        r'''configure_standard_waveform

        Configures the following properties of the signal generator that affect
        standard waveform generation:

        -  func_waveform
        -  func_amplitude
        -  func_dc_offset
        -  func_frequency
        -  func_start_phase

        Note:
        You must call the ConfigureOutputMode method with the
        **outputMode** parameter set to OutputMode.FUNC before calling
        this method.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform (enums.Waveform): Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the func_waveform property to this
                value.

                ****Defined Values****

                **Default Value**: Waveform.SINE

                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SINE      | Specifies that the signal generator produces a sinusoid waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SQUARE    | Specifies that the signal generator produces a square waveform.                                                                |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.TRIANGLE  | Specifies that the signal generator produces a triangle waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.DC        | Specifies that the signal generator produces a constant voltage.                                                               |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.NOISE     | Specifies that the signal generator produces white noise.                                                                      |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.USER      | Specifies that the signal generator produces a user-defined waveform as defined with the define_user_standard_waveform method. |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+

            amplitude (float): Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the func_amplitude property to
                this value.

                For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
                the amplitude to 10.00 V.

                **Units**: peak-to-peak voltage

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                method to Waveform.DC.

            frequency (float): | Specifies the frequency of the standard waveform that you want the
                  signal generator to produce. NI-FGEN sets the
                  func_frequency property to this value.

                **Units**: hertz

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                method to Waveform.DC.

            dc_offset (float): Specifies the DC offset of the standard waveform that you want the
                signal generator to produce. The value is the offset from ground to the
                center of the waveform you specify with the **waveform** parameter,
                observed at the output terminal. For example, to configure a waveform
                with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
                **dcOffset** to 5.00 V. NI-FGEN sets the func_dc_offset
                property to this value.

                **Units**: volts

                **Default Value**: None

            start_phase (float): Specifies the horizontal offset of the standard waveform that you want
                the signal generator to produce. Specify this parameter in degrees of
                one waveform cycle. NI-FGEN sets the func_start_phase
                property to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: 0.00

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter to Waveform.DC.

        '''
        if type(waveform) is not enums.Waveform:
            raise TypeError('Parameter waveform must be of type ' + str(enums.Waveform))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_ctype = _visatype.ViInt32(waveform.value)  # case S130
        amplitude_ctype = _visatype.ViReal64(amplitude)  # case S150
        dc_offset_ctype = _visatype.ViReal64(dc_offset)  # case S150
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        start_phase_ctype = _visatype.ViReal64(start_phase)  # case S150
        error_code = self._library.niFgen_ConfigureStandardWaveform(vi_ctype, channel_name_ctype, waveform_ctype, amplitude_ctype, dc_offset_ctype, frequency_ctype, start_phase_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_waveform(self, waveform_data_array):
        '''create_waveform

        Creates an onboard waveform for use in Arbitrary Waveform output mode or Arbitrary Sequence output mode.

        Note: You must set output_mode to OutputMode.ARB or OutputMode.SEQ before calling this method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_data_array (iterable of float or int16): Array of data for the new arbitrary waveform. This may be an iterable of float or int16, or for best performance a numpy.ndarray of dtype int16 or float64.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used in other methods when referring to this waveform.

        '''
        # Check the type by using string comparison so that we don't import numpy unnecessarily.
        if str(type(waveform_data_array)).find("'numpy.ndarray'") != -1:
            import numpy
            if waveform_data_array.dtype == numpy.float64:
                return self._create_waveform_f64_numpy(waveform_data_array)
            elif waveform_data_array.dtype == numpy.int16:
                return self._create_waveform_i16_numpy(waveform_data_array)
            else:
                raise TypeError("Unsupported dtype. Is {0}, expected {1} or {2}".format(waveform_data_array.dtype, numpy.float64, numpy.int16))
        elif isinstance(waveform_data_array, array.array):
            if waveform_data_array.typecode == 'd':
                return self._create_waveform_f64(waveform_data_array)
            elif waveform_data_array.typecode == 'h':
                return self._create_waveform_i16(waveform_data_array)
            else:
                raise TypeError("Unsupported dtype. Is {0}, expected {1} or {2}".format(waveform_data_array.typecode, 'd (double)', 'h (16 bit int)'))

        return self._create_waveform_f64(waveform_data_array)

    @ivi_synchronized
    def _create_waveform_f64(self, waveform_data_array):
        r'''_create_waveform_f64

        Creates an onboard waveform from binary F64 (floating point double) data
        for use in Arbitrary Waveform output mode or Arbitrary Sequence output
        mode. The **waveformHandle** returned can later be used for setting the
        active waveform, changing the data in the waveform, building sequences
        of waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_data_array (array.array("d")): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_array = get_ctypes_and_array(value=waveform_data_array, array_type="d")  # case B550
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array_array, library_type=_visatype.ViReal64)  # case B550
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateWaveformF64(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    @ivi_synchronized
    def _create_waveform_f64_numpy(self, waveform_data_array):
        r'''_create_waveform_f64

        Creates an onboard waveform from binary F64 (floating point double) data
        for use in Arbitrary Waveform output mode or Arbitrary Sequence output
        mode. The **waveformHandle** returned can later be used for setting the
        active waveform, changing the data in the waveform, building sequences
        of waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_data_array (numpy.array(dtype=numpy.float64)): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        import numpy

        if type(waveform_data_array) is not numpy.ndarray:
            raise TypeError('waveform_data_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data_array)))
        if numpy.isfortran(waveform_data_array) is True:
            raise TypeError('waveform_data_array must be in C-order')
        if waveform_data_array.dtype is not numpy.dtype('float64'):
            raise TypeError('waveform_data_array must be numpy.ndarray of dtype=float64, is ' + str(waveform_data_array.dtype))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array)  # case B510
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateWaveformF64(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    @ivi_synchronized
    def create_waveform_from_file_f64(self, file_name, byte_order):
        r'''create_waveform_from_file_f64

        This method takes the floating point double (F64) data from the
        specified file and creates an onboard waveform for use in Arbitrary
        Waveform or Arbitrary Sequence output mode. The **waveformHandle**
        returned by this method can later be used for setting the active
        waveform, changing the data in the waveform, building sequences of
        waveforms, or deleting the waveform when it is no longer needed.

        Note:
        The F64 data must be between –1.0 and +1.0 V. Use the
        digital_gain property to generate different voltage
        outputs.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            file_name (str): The full path and name of the file where the waveform data resides.

            byte_order (enums.ByteOrder): Specifies the byte order of the data in the file.

                ****Defined Values****

                |
                | ****Default Value**:** ByteOrder.LITTLE

                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.LITTLE | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.BIG    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                Data written by most applications in Windows (including
                LabWindows™/CVI™) is in Little Endian format. Data written to a file
                from LabVIEW is in Big Endian format by default on all platforms. Big
                Endian and Little Endian refer to the way data is stored in memory,
                which can differ on different processors.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        if type(byte_order) is not enums.ByteOrder:
            raise TypeError('Parameter byte_order must be of type ' + str(enums.ByteOrder))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(self._encoding))  # case C020
        byte_order_ctype = _visatype.ViInt32(byte_order.value)  # case S130
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateWaveformFromFileF64(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    @ivi_synchronized
    def create_waveform_from_file_i16(self, file_name, byte_order):
        r'''create_waveform_from_file_i16

        Takes the binary 16-bit signed integer (I16) data from the specified
        file and creates an onboard waveform for use in Arbitrary Waveform or
        Arbitrary Sequence output mode. The **waveformHandle** returned by this
        method can later be used for setting the active waveform, changing the
        data in the waveform, building sequences of waveforms, or deleting the
        waveform when it is no longer needed.

        Note:
        The I16 data (values between –32768 and +32767) is assumed to
        represent –1 to +1 V. Use the digital_gain property to
        generate different voltage outputs.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            file_name (str): The full path and name of the file where the waveform data resides.

            byte_order (enums.ByteOrder): Specifies the byte order of the data in the file.

                ****Defined Values****

                |
                | ****Default Value**:** ByteOrder.LITTLE

                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.LITTLE | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.BIG    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                Data written by most applications in Windows (including
                LabWindows™/CVI™) is in Little Endian format. Data written to a file
                from LabVIEW is in Big Endian format by default on all platforms. Big
                Endian and Little Endian refer to the way data is stored in memory,
                which can differ on different processors.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        if type(byte_order) is not enums.ByteOrder:
            raise TypeError('Parameter byte_order must be of type ' + str(enums.ByteOrder))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(self._encoding))  # case C020
        byte_order_ctype = _visatype.ViInt32(byte_order.value)  # case S130
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateWaveformFromFileI16(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    @ivi_synchronized
    def _create_waveform_i16_numpy(self, waveform_data_array):
        r'''_create_waveform_i16

        Creates an onboard waveform from binary 16-bit signed integer (I16) data
        for use in Arbitrary Waveform or Arbitrary Sequence output mode. The
        **waveformHandle** returned can later be used for setting the active
        waveform, changing the data in the waveform, building sequences of
        waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_data_array (numpy.array(dtype=numpy.int16)): Specify the array of data that you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in the Waveform Size parameter.
                You must normalize the data points in the array to be between -32768 and
                +32767.
                ****Default Value**:** None


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        import numpy

        if type(waveform_data_array) is not numpy.ndarray:
            raise TypeError('waveform_data_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data_array)))
        if numpy.isfortran(waveform_data_array) is True:
            raise TypeError('waveform_data_array must be in C-order')
        if waveform_data_array.dtype is not numpy.dtype('int16'):
            raise TypeError('waveform_data_array must be numpy.ndarray of dtype=int16, is ' + str(waveform_data_array.dtype))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array)  # case B510
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateWaveformI16(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    @ivi_synchronized
    def define_user_standard_waveform(self, waveform_data_array):
        r'''define_user_standard_waveform

        Defines a user waveform for use in either Standard Method or Frequency
        List output mode.

        To select the waveform, set the **waveform** parameter to
        Waveform.USER with either the configure_standard_waveform
        or the create_freq_list method.

        The waveform data must be scaled between –1.0 and 1.0. Use the
        **amplitude** parameter in the configure_standard_waveform
        method to generate different output voltages.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.FUNC or
        OutputMode.FREQ_LIST before calling this method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_data_array (list of float): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFgen_DefineUserStandardWaveform(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _delete_named_waveform(self, waveform_name):
        r'''_delete_named_waveform

        Removes a previously created arbitrary waveform from the signal
        generator memory and invalidates the waveform handle.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_DeleteNamedWaveform(vi_ctype, channel_name_ctype, waveform_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def delete_script(self, script_name):
        r'''delete_script

        Deletes the specified script from onboard memory.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            script_name (str): Specifies the name of the script you want to delete. The script name
                appears in the text of the script following the script keyword.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        script_name_ctype = ctypes.create_string_buffer(script_name.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_DeleteScript(vi_ctype, channel_name_ctype, script_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def delete_waveform(self, waveform_name_or_handle):
        '''delete_waveform

        Removes a previously created arbitrary waveform from the signal generator memory.

        Note: The signal generator must not be in the Generating state when you call this method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name_or_handle (str or int): The name (str) or handle (int) of an arbitrary waveform previously allocated with allocate_named_waveform, allocate_waveform or create_waveform.

        '''
        if isinstance(waveform_name_or_handle, str):
            return self._delete_named_waveform(waveform_name_or_handle)
        else:
            return self._clear_arb_waveform(waveform_name_or_handle)

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute_id):
        r'''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

        You can use this method to get the values of instrument-specific
        properties and inherent IVI properties. If the property represents an
        instrument state, this method performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (bool): Returns the current value of the property. Pass the address of a
                ViBoolean variable.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFgen_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

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
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (int): Returns the current value of the property. Pass the address of a
                ViInt32 variable.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute_id):
        r'''_get_attribute_vi_real64

        Queries the value of a ViReal64 property.

        You can use this method to get the values of instrument-specific
        properties and inherent IVI properties. If the property represents an
        instrument state, this method performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (float): Returns the current value of the property. Pass the address of a
                ViReal64 variable.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFgen_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute_id):
        r'''_get_attribute_vi_string

        Queries the value of a ViString property.

        You can use this method to get the values of instrument-specific
        properties and inherent IVI properties. If the property represents an
        instrument state, this method performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        You must provide a ViChar array to serve as a buffer for the value. You
        pass the number of bytes in the buffer as the **arraySize** parameter.
        If the current value of the property, including the terminating NUL
        byte, is larger than the size you indicate in the **arraySize**
        parameter, the method copies **arraySize** – 1 bytes into the buffer,
        places an ASCII NUL byte at the end of the buffer, and returns the array
        size you must pass to get the entire value. For example, if the value is
        123456 and **arraySize** is 4, the method places 123 into the buffer
        and returns 7.

        If you want to call this method just to get the required array size,
        you can pass 0 for **arraySize** and VI_NULL for the **attributeValue**
        buffer.

        If you want the method to fill in the buffer regardless of the number
        of bytes in the value, pass a negative number for the **arraySize**
        parameter.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (str): The buffer in which the method returns the current value of the
                property. The buffer must be a ViChar data type and have at least as
                many bytes as indicated in the **arraySize** parameter.

                If the current value of the property, including the terminating NUL
                byte, contains more bytes than you indicate in this parameter, the
                method copies **arraySize** – 1 bytes into the buffer, places an ASCII
                NUL byte at the end of the buffer, and returns the array size you must
                pass to get the entire value. For example, if the value is 123456 and
                **arraySize** is 4, the method places 123 into the buffer and returns
                7.

                If you specify 0 for the **arraySize** parameter, you can pass VI_NULL
                for this parameter.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        array_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niFgen_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * array_size_ctype.value)()  # case C060
        error_code = self._library.niFgen_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def _get_error(self):
        r'''_get_error

        Returns the error information associated with an IVI session or with the
        current execution thread. If you specify a valid IVI session for the
        **vi** parameter, this method retrieves and then clears the error
        information for the session. If you pass VI_NULL for the **vi**
        parameter, this method retrieves and then clears the error information
        for the current execution thread.

        The IVI Engine also maintains this error information separately for each
        thread. This feature is useful if you do not have a session handle to
        pass to the _get_error or ClearError methods. This
        situation occurs when a call to the init or
        InitWithOptions method fails.

        Returns:
            error_code (int): The error code for the session or execution thread.

                A value of VI_SUCCESS (0) indicates that no error occurred. A positive
                value indicates a warning. A negative value indicates an error.

                You can call _error_message to get a text description of the
                value.

                If you are not interested in this value, you can pass VI_NULL.

            error_description (str): The error description string for the session or execution thread. If the
                error code is nonzero, the description string can further describe the
                error or warning condition.

                If you are not interested in this value, you can pass VI_NULL.
                Otherwise, you must pass a ViChar array of a size specified with the
                **errorDescriptionBufferSize** parameter.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library.niFgen_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFgen_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-FGEN locked the session.
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
            lock (context manager): When used in a with statement, nifgen.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._lock_session()  # We do not call _lock_session() in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    def _lock_session(self):
        '''_lock_session

        Actual call to driver
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

    @ivi_synchronized
    def send_software_edge_trigger(self, trigger=None, trigger_id=None):
        '''send_software_edge_trigger

        Sends a command to trigger the signal generator. This VI can act as an
        override for an external edge trigger.

        Note:
        This VI does not override external digital edge triggers of the
        NI 5401/5411/5431.

        Args:
            trigger (enums.Trigger): Trigger specifies the type of software trigger to send

                +----------------+
                | Defined Values |
                +================+
                | Trigger.START  |
                +----------------+
                | Trigger.SCRIPT |
                +----------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            trigger_id (str): Trigger ID specifies the Script Trigger to use for triggering.

        '''
        if trigger is None or trigger_id is None:
            import warnings
            warnings.warn('trigger and trigger_id should now always be passed in to the method', category=DeprecationWarning)

            # We look at whether we are called directly on the session or a repeated capability container to determine how to behave
            if len(self._repeated_capability) > 0:
                trigger_id = self._repeated_capability
                trigger = enums.Trigger.SCRIPT
            else:
                trigger_id = "None"
                trigger = enums.Trigger.START

        elif trigger is not None and trigger_id is not None:
            pass  # This is how the function should be called

        else:
            raise ValueError('Both trigger ({0}) and trigger_id ({1}) should be passed in to the method'.format(str(trigger), str(trigger_id)))

        if type(trigger) is not enums.Trigger:
            raise TypeError('Parameter trigger must be of type ' + str(enums.Trigger))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_boolean

        Sets the value of a ViBoolean property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (bool): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niFgen_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int32

        Sets the value of a ViInt32 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (int): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niFgen_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_real64

        Sets the value of a ViReal64 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (float): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niFgen_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute_id, attribute_value):
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

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (str): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _set_named_waveform_next_write_position(self, waveform_name, relative_to, offset):
        r'''_set_named_waveform_next_write_position

        Sets the position in the waveform to which data is written at the next
        write. This method allows you to write to arbitrary locations within
        the waveform. These settings apply only to the next write to the
        waveform specified by the **waveformHandle** parameter. Subsequent
        writes to that waveform begin where the last write left off, unless this
        method is called again. The **waveformHandle** passed in must have
        been created with a call to one of the following methods:

        -  allocate_waveform
        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64
        -  CreateWaveformFromFileHWS

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.START (0)   | Use the start of the waveform as the reference position.                |
                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.CURRENT (1) | Use the current position within the waveform as the reference position. |
                +------------------------+-------------------------------------------------------------------------+

            offset (int): Specifies the offset from the **relativeTo** parameter at which to start
                loading the data into the waveform.

        '''
        if type(relative_to) is not enums.RelativeTo:
            raise TypeError('Parameter relative_to must be of type ' + str(enums.RelativeTo))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        relative_to_ctype = _visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = _visatype.ViInt32(offset)  # case S150
        error_code = self._library.niFgen_SetNamedWaveformNextWritePosition(vi_ctype, channel_name_ctype, waveform_name_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def set_next_write_position(self, waveform_name_or_handle, relative_to, offset):
        '''set_next_write_position

        Sets the position in the waveform at which the next waveform data is
        written. This method allows you to write to arbitrary locations within
        the waveform. These settings apply only to the next write to the
        waveform specified by the waveformHandle parameter. Subsequent writes to
        that waveform begin where the last write left off, unless this method
        is called again. The waveformHandle passed in must have been created by
        a call to the allocate_waveform method or one of the following
        create_waveform method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name_or_handle (str or int): The name (str) or handle (int) of an arbitrary waveform previously allocated with allocate_named_waveform, allocate_waveform or create_waveform.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.START (0)   | Use the start of the waveform as the reference position.                |
                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.CURRENT (1) | Use the current position within the waveform as the reference position. |
                +------------------------+-------------------------------------------------------------------------+

            offset (int): Specifies the offset from **relativeTo** at which to start loading the
                data into the waveform.

        '''
        if isinstance(waveform_name_or_handle, str):
            return self._set_named_waveform_next_write_position(waveform_name_or_handle, relative_to, offset)
        else:
            return self._set_waveform_next_write_position(waveform_name_or_handle, relative_to, offset)

    @ivi_synchronized
    def _set_waveform_next_write_position(self, waveform_handle, relative_to, offset):
        r'''_set_waveform_next_write_position

        Sets the position in the waveform at which the next waveform data is
        written. This method allows you to write to arbitrary locations within
        the waveform. These settings apply only to the next write to the
        waveform specified by the waveformHandle parameter. Subsequent writes to
        that waveform begin where the last write left off, unless this method
        is called again. The waveformHandle passed in must have been created by
        a call to the allocate_waveform method or one of the following
        niFgen CreateWaveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64
        -  CreateWaveformFromFileHWS

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.START (0)   | Use the start of the waveform as the reference position.                |
                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.CURRENT (1) | Use the current position within the waveform as the reference position. |
                +------------------------+-------------------------------------------------------------------------+

            offset (int): Specifies the offset from **relativeTo** at which to start loading the
                data into the waveform.

        '''
        if type(relative_to) is not enums.RelativeTo:
            raise TypeError('Parameter relative_to must be of type ' + str(enums.RelativeTo))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        relative_to_ctype = _visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = _visatype.ViInt32(offset)  # case S150
        error_code = self._library.niFgen_SetWaveformNextWritePosition(vi_ctype, channel_name_ctype, waveform_handle_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

    @ivi_synchronized
    def _write_binary16_waveform_numpy(self, waveform_handle, data):
        r'''_write_binary16_waveform

        Writes binary data to the waveform in onboard memory. The waveform
        handle passed must have been created by a call to the
        allocate_waveform or the create_waveform method.

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            data (numpy.array(dtype=numpy.int16)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**. The binary data
                is left-justified.

        '''
        import numpy

        if type(data) is not numpy.ndarray:
            raise TypeError('data must be {0}, is {1}'.format(numpy.ndarray, type(data)))
        if numpy.isfortran(data) is True:
            raise TypeError('data must be in C-order')
        if data.dtype is not numpy.dtype('int16'):
            raise TypeError('data must be numpy.ndarray of dtype=int16, is ' + str(data.dtype))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteBinary16Waveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _write_named_waveform_f64(self, waveform_name, data):
        r'''_write_named_waveform_f64

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or to one of the following niFgen
        Create Waveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64
        -  CreateWaveformFromFileHWS

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            data (array.array("d")): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_array = get_ctypes_and_array(value=data, array_type="d")  # case B550
        data_ctype = get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFgen_WriteNamedWaveformF64(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _write_named_waveform_f64_numpy(self, waveform_name, data):
        r'''_write_named_waveform_f64

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or to one of the following niFgen
        Create Waveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64
        -  CreateWaveformFromFileHWS

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            data (numpy.array(dtype=numpy.float64)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        import numpy

        if type(data) is not numpy.ndarray:
            raise TypeError('data must be {0}, is {1}'.format(numpy.ndarray, type(data)))
        if numpy.isfortran(data) is True:
            raise TypeError('data must be in C-order')
        if data.dtype is not numpy.dtype('float64'):
            raise TypeError('data must be numpy.ndarray of dtype=float64, is ' + str(data.dtype))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteNamedWaveformF64(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _write_named_waveform_i16_numpy(self, waveform_name, data):
        r'''_write_named_waveform_i16

        Writes binary data to the named waveform in onboard memory.

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            data (numpy.array(dtype=numpy.int16)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        import numpy

        if type(data) is not numpy.ndarray:
            raise TypeError('data must be {0}, is {1}'.format(numpy.ndarray, type(data)))
        if numpy.isfortran(data) is True:
            raise TypeError('data must be in C-order')
        if data.dtype is not numpy.dtype('int16'):
            raise TypeError('data must be numpy.ndarray of dtype=int16, is ' + str(data.dtype))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteNamedWaveformI16(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def write_script(self, script):
        r'''write_script

        Writes a string containing one or more scripts that govern the
        generation of waveforms.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            script (str): Contains the text of the script you want to use for your generation
                operation. Refer to `scripting
                Instructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__
                for more information about writing scripts.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        script_ctype = ctypes.create_string_buffer(script.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_WriteScript(vi_ctype, channel_name_ctype, script_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _write_waveform(self, waveform_handle, data):
        r'''_write_waveform

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or one of the following niFgen
        CreateWaveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64
        -  CreateWaveformFromFileHWS

        By default, the subsequent call to the write_waveform method
        continues writing data from the position of the last sample written. You
        can set the write position and offset by calling the
        set_next_write_position method. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            data (array.array("d")): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_array = get_ctypes_and_array(value=data, array_type="d")  # case B550
        data_ctype = get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFgen_WriteWaveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _write_waveform_numpy(self, waveform_handle, data):
        r'''_write_waveform

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or one of the following niFgen
        CreateWaveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64
        -  CreateWaveformFromFileHWS

        By default, the subsequent call to the write_waveform method
        continues writing data from the position of the last sample written. You
        can set the write position and offset by calling the
        set_next_write_position method. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            data (numpy.array(dtype=numpy.float64)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        import numpy

        if type(data) is not numpy.ndarray:
            raise TypeError('data must be {0}, is {1}'.format(numpy.ndarray, type(data)))
        if numpy.isfortran(data) is True:
            raise TypeError('data must be in C-order')
        if data.dtype is not numpy.dtype('float64'):
            raise TypeError('data must be numpy.ndarray of dtype=float64, is ' + str(data.dtype))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteWaveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def write_waveform(self, waveform_name_or_handle, data):
        '''write_waveform

        Writes data to the waveform in onboard memory.

        By default, subsequent calls to this method
        continue writing data from the position of the last sample written. You
        can set the write position and offset by calling the set_next_write_position
        set_next_write_position method.

        Tip:
        This method requires repeated capabilities. If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session repeated capabilities container, and calling this method on the result.

        Args:
            waveform_name_or_handle (str or int): The name (str) or handle (int) of an arbitrary waveform previously allocated with allocate_named_waveform, allocate_waveform or create_waveform.

            data (list of float): Array of data to load into the waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.

        '''
        use_named = isinstance(waveform_name_or_handle, str)
        # Check the type by using string comparison so that we don't import numpy unnecessarily.
        if str(type(data)).find("'numpy.ndarray'") != -1:
            import numpy
            if data.dtype == numpy.float64:
                return self._write_named_waveform_f64_numpy(waveform_name_or_handle, data) if use_named else self._write_waveform_numpy(waveform_name_or_handle, data)
            elif data.dtype == numpy.int16:
                return self._write_named_waveform_i16_numpy(waveform_name_or_handle, data) if use_named else self._write_binary16_waveform_numpy(waveform_name_or_handle, data)
            else:
                raise TypeError("Unsupported dtype. Is {0}, expected {1} or {2}".format(data.dtype, numpy.float64, numpy.int16))
        elif isinstance(data, array.array):
            if data.typecode == 'd':
                return self._write_named_waveform_f64(waveform_name_or_handle, data) if use_named else self._write_waveform(waveform_name_or_handle, data)
            elif data.typecode == 'h':
                return self._write_named_waveform_i16(waveform_name_or_handle, data) if use_named else self._write_binary16_waveform(waveform_name_or_handle, data)
            else:
                raise TypeError("Unsupported dtype. Is {0}, expected {1} or {2}".format(data.typecode, 'd (double)', 'h (16 bit int)'))

        return self._write_named_waveform_f64(waveform_name_or_handle, data) if use_named else self._write_waveform(waveform_name_or_handle, data)

    def _error_message(self, error_code):
        r'''_error_message

        Converts a status code returned by an NI-FGEN method into a
        user-readable string.

        Args:
            error_code (int): Specifies the **status** parameter that is returned from any of the
                NI-FGEN methods.

                **Default Value**: 0 (VI_SUCCESS)


        Returns:
            error_message (str): Returns the error message string read from the instrument error message
                queue.

                You must pass a ViChar array with at least 256 bytes.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFgen_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class Session(_SessionBase):
    '''An NI-FGEN session to a National Instruments Signal Generator.'''

    def __init__(self, resource_name, channel_name=None, reset_device=False, options={}):
        r'''An NI-FGEN session to a National Instruments Signal Generator.

        Creates and returns a new NI-FGEN session to the specified channel of a
        waveform generator that is used in all subsequent NI-FGEN method
        calls.

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
                However, all IVI names, such as logical names, are case-sensitive. If
                you use logical names, driver session names, or virtual names in your
                program, you must ensure that the name you use matches the name in the
                IVI Configuration Store file exactly, without any variations in the case
                of the characters.

                | Specifies the resource name of the device to initialize.

                For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
                the device number assigned by MAX, as shown in Example 1.

                For NI-DAQmx devices, the syntax is just the device name specified in
                MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
                in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
                right-clicking on the name in MAX and entering a new name.

                An alternate syntax for NI-DAQmx devices consists of DAQ::\ *NI-DAQmx
                device name*, as shown in Example 3. This naming convention allows for
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

                +-----------+--------------------------------------+------------------------+---------------------------------+
                | Example # | Device Type                          | Syntax                 | Variable                        |
                +===========+======================================+========================+=================================+
                | 1         | Traditional NI-DAQ device            | DAQ::\ *1*             | (*1* = device number)           |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 2         | NI-DAQmx device                      | *myDAQmxDevice*        | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 3         | NI-DAQmx device                      | DAQ::\ *myDAQmxDevice* | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 4         | NI-DAQmx device                      | DAQ::\ *2*             | (*2* = device name)             |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 5         | IVI logical name or IVI virtual name | *myLogicalName*        | (*myLogicalName* = name)        |
                +-----------+--------------------------------------+------------------------+---------------------------------+

            channel_name (str, list, range, tuple): Specifies the channel that this VI uses.

                **Default Value**: "0"

            reset_device (bool): Specifies whether you want to reset the device during the initialization
                procedure. True specifies that the device is reset and performs the
                same method as the Reset method.

                ****Defined Values****

                **Default Value**: False

                +-------+---------------------+
                | True  | Reset device        |
                +-------+---------------------+
                | False | Do not reset device |
                +-------+---------------------+

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


        Returns:
            session (nifgen.Session): A session object representing the device.

        '''
        super(Session, self).__init__(repeated_capability_list=[], vi=None, library=None, encoding=None, freeze_it=False)
        channel_name = _converters.convert_repeated_capabilities_without_prefix(channel_name)
        options = _converters.convert_init_with_options_dictionary(options)
        self._library = _library_singleton.get()
        self._encoding = 'windows-1251'

        # Call specified init function
        self._vi = 0  # This must be set before calling _initialize_with_channels().
        self._vi = self._initialize_with_channels(resource_name, channel_name, reset_device, options)

        self.tclk = nitclk.SessionReference(self._vi)

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("channel_name=" + pp.pformat(channel_name))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def initiate(self):
        '''initiate

        Initiates signal generation. If you want to abort signal generation,
        call the abort method. After the signal generation
        is aborted, you can call the initiate method to
        cause the signal generator to produce a signal again.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Generation(self)

    def close(self):
        '''close

        Performs the following operations:

        -  Closes the instrument I/O session.
        -  Destroys the NI-FGEN session and all of its properties.
        -  Deallocates any memory resources NI-FGEN uses.

        Not all signal routes established by calling the ExportSignal
        and RouteSignalOut methods are released when the NI-FGEN
        session is closed. The following table shows what happens to a signal
        route on your device when you call the _close method.

        +--------------------+-------------------+------------------+
        | Routes To          | NI 5401/5411/5431 | Other Devices    |
        +====================+===================+==================+
        | Front Panel        | Remain connected  | Remain connected |
        +--------------------+-------------------+------------------+
        | RTSI/PXI Backplane | Remain connected  | Disconnected     |
        +--------------------+-------------------+------------------+

        Note:
        After calling _close, you cannot use NI-FGEN again until you
        call the init or InitWithOptions methods.

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

    @ivi_synchronized
    def abort(self):
        r'''abort

        Aborts any previously initiated signal generation. Call the
        initiate method to cause the signal generator to
        produce a signal again.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_AbortGeneration(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def clear_arb_memory(self):
        r'''clear_arb_memory

        Removes all previously created arbitrary waveforms, sequences, and
        scripts from the signal generator memory and invalidates all waveform
        handles, sequence handles, and waveform names.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_ClearArbMemory(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def clear_arb_sequence(self, sequence_handle):
        r'''clear_arb_sequence

        Removes a previously created arbitrary sequence from the signal
        generator memory and invalidates the sequence handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.

        Args:
            sequence_handle (int): Specifies the handle of the arbitrary sequence that you want the signal
                generator to remove. You can create an arbitrary sequence using the
                create_arb_sequence or create_advanced_arb_sequence method.
                These methods return a handle that you use to identify the sequence.

                | **Defined Value**:
                | NIFGEN_VAL_ALL_SEQUENCES—Remove all sequences from the signal
                  generator

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sequence_handle_ctype = _visatype.ViInt32(sequence_handle)  # case S150
        error_code = self._library.niFgen_ClearArbSequence(vi_ctype, sequence_handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _clear_arb_waveform(self, waveform_handle):
        r'''_clear_arb_waveform

        Removes a previously created arbitrary waveform from the signal
        generator memory and invalidates the waveform handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform that you want the signal
                generator to remove.

                You can create multiple arbitrary waveforms using one of the following
                niFgen Create Waveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64
                -  CreateWaveformFromFileHWS

                **Defined Value**:

                NIFGEN_VAL_ALL_WAVEFORMS—Remove all waveforms from the signal
                generator.

                **Default Value**: None

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        error_code = self._library.niFgen_ClearArbWaveform(vi_ctype, waveform_handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def clear_freq_list(self, frequency_list_handle):
        r'''clear_freq_list

        Removes a previously created frequency list from the signal generator
        memory and invalidates the frequency list handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.

        Args:
            frequency_list_handle (int): Specifies the handle of the frequency list you want the signal generator
                to remove. You create multiple frequency lists using
                create_freq_list. create_freq_list returns a handle that you
                use to identify each list. Specify a value of -1 to clear all frequency
                lists.

                **Defined Value**

                NIFGEN_VAL_ALL_FLISTS—Remove all frequency lists from the signal
                generator.

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        frequency_list_handle_ctype = _visatype.ViInt32(frequency_list_handle)  # case S150
        error_code = self._library.niFgen_ClearFreqList(vi_ctype, frequency_list_handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def commit(self):
        r'''commit

        Causes a transition to the Committed state. This method verifies
        property values, reserves the device, and commits the property values
        to the device. If the property values are all valid, NI-FGEN sets the
        device hardware configuration to match the session configuration. This
        method does not support the NI 5401/5404/5411/5431 signal generators.

        In the Committed state, you can load waveforms, scripts, and sequences
        into memory. If any properties are changed, NI-FGEN implicitly
        transitions back to the Idle state, where you can program all session
        properties before applying them to the device. This method has no
        effect if the device is already in the Committed or Generating state and
        returns a successful status value.

        Calling this VI before the niFgen Initiate Generation VI is optional but
        has the following benefits:

        -  Routes are committed, so signals are exported or imported.
        -  Any Reference Clock and external clock circuits are phase-locked.
        -  A subsequent initiate method can run faster
           because the device is already configured.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def create_advanced_arb_sequence(self, waveform_handles_array, loop_counts_array, sample_counts_array=None, marker_location_array=None):
        r'''create_advanced_arb_sequence

        Creates an arbitrary sequence from an array of waveform handles and an
        array of corresponding loop counts. This method returns a handle that
        identifies the sequence. You pass this handle to the
        configure_arb_sequence method to specify what arbitrary sequence
        you want the signal generator to produce.

        The create_advanced_arb_sequence method extends on the
        create_arb_sequence method by adding the ability to set the
        number of samples in each sequence step and to set marker locations.

        An arbitrary sequence consists of multiple waveforms. For each waveform,
        you specify the number of times the signal generator produces the
        waveform before proceeding to the next waveform. The number of times to
        repeat a specific waveform is called the loop count.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.SEQ before calling this
        method.

        Args:
            waveform_handles_array (list of int): Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                allocate_waveform method or one of the following niFgen
                CreateWaveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64
                -  CreateWaveformFromFileHWS

                **Default Value**: None

            loop_counts_array (list of int): Specifies the array of loop counts you want to use to create a new
                arbitrary sequence. The array must have at least as many elements as the
                value that you specify in the **sequenceLength** parameter. Each
                **loopCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates how many times to repeat that waveform. Each
                element of the **loopCountsArray** must be less than or equal to the
                maximum number of loop counts that the signal generator allows. You can
                obtain the maximum loop count from **maximumLoopCount** in the
                query_arb_seq_capabilities method.

                **Default Value**: None

            sample_counts_array (list of int): Specifies the array of sample counts that you want to use to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value you specify in the **sequenceLength** parameter. Each
                **sampleCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates the subset, in samples, of the given waveform to
                generate. Each element of the **sampleCountsArray** must be larger than
                the minimum waveform size, a multiple of the waveform quantum and no
                larger than the number of samples in the corresponding waveform. You can
                obtain these values by calling the query_arb_wfm_capabilities
                method.

                **Default Value**: None

            marker_location_array (list of int): Specifies the array of marker locations to where you want a marker to be
                generated in the sequence. The array must have at least as many elements
                as the value you specify in the **sequenceLength** parameter. Each
                **markerLocationArray** element corresponds to a
                **waveformHandlesArray** element and indicates where in the waveform a
                marker is to generate. The marker location must be less than the size of
                the waveform the marker is in. The markers are coerced to the nearest
                marker quantum and the coerced values are returned in the
                **coercedMarkersArray** parameter.

                If you do not want a marker generated for a particular sequence stage,
                set this parameter to NIFGEN_VAL_NO_MARKER.

                **Defined Value**: NIFGEN_VAL_NO_MARKER

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            coerced_markers_array (list of int): Returns an array of all given markers that are coerced (rounded) to the
                nearest marker quantum. Not all devices coerce markers.

                **Default Value**: None

            sequence_handle (int): Returns the handle that identifies the new arbitrary sequence. You can
                pass this handle to configure_arb_sequence to generate the
                arbitrary sequence.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sequence_length_ctype = _visatype.ViInt32(0 if waveform_handles_array is None else len(waveform_handles_array))  # case S160
        if loop_counts_array is not None and len(loop_counts_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of loop_counts_array and waveform_handles_array parameters do not match.")  # case S160
        if sample_counts_array is not None and len(sample_counts_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of sample_counts_array and waveform_handles_array parameters do not match.")  # case S160
        if marker_location_array is not None and len(marker_location_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of marker_location_array and waveform_handles_array parameters do not match.")  # case S160
        waveform_handles_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_handles_array, library_type=_visatype.ViInt32)  # case B550
        loop_counts_array_ctype = get_ctypes_pointer_for_buffer(value=loop_counts_array, library_type=_visatype.ViInt32)  # case B550
        sample_counts_array_ctype = get_ctypes_pointer_for_buffer(value=sample_counts_array, library_type=_visatype.ViInt32)  # case B550
        marker_location_array_ctype = get_ctypes_pointer_for_buffer(value=marker_location_array, library_type=_visatype.ViInt32)  # case B550
        coerced_markers_array_size = (0 if marker_location_array is None else len(marker_location_array))  # case B560
        coerced_markers_array_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=coerced_markers_array_size)  # case B560
        sequence_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateAdvancedArbSequence(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, sample_counts_array_ctype, marker_location_array_ctype, coerced_markers_array_ctype, None if sequence_handle_ctype is None else (ctypes.pointer(sequence_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(coerced_markers_array_ctype[i]) for i in range((0 if marker_location_array is None else len(marker_location_array)))], int(sequence_handle_ctype.value)

    @ivi_synchronized
    def create_arb_sequence(self, waveform_handles_array, loop_counts_array):
        r'''create_arb_sequence

        Creates an arbitrary sequence from an array of waveform handles and an
        array of corresponding loop counts. This method returns a handle that
        identifies the sequence. You pass this handle to the
        configure_arb_sequence method to specify what arbitrary sequence
        you want the signal generator to produce.

        An arbitrary sequence consists of multiple waveforms. For each waveform,
        you can specify the number of times that the signal generator produces
        the waveform before proceeding to the next waveform. The number of times
        to repeat a specific waveform is called the loop count.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.SEQ before calling this
        method.

        Args:
            waveform_handles_array (list of int): Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                allocate_waveform method or one of the following niFgen
                CreateWaveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64
                -  CreateWaveformFromFileHWS

                **Default Value**: None

            loop_counts_array (list of int): Specifies the array of loop counts you want to use to create a new
                arbitrary sequence. The array must have at least as many elements as the
                value that you specify in the **sequenceLength** parameter. Each
                **loopCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates how many times to repeat that waveform. Each
                element of the **loopCountsArray** must be less than or equal to the
                maximum number of loop counts that the signal generator allows. You can
                obtain the maximum loop count from **maximumLoopCount** in the
                query_arb_seq_capabilities method.

                **Default Value**: None


        Returns:
            sequence_handle (int): Returns the handle that identifies the new arbitrary sequence. You can
                pass this handle to configure_arb_sequence to generate the
                arbitrary sequence.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sequence_length_ctype = _visatype.ViInt32(0 if waveform_handles_array is None else len(waveform_handles_array))  # case S160
        if loop_counts_array is not None and len(loop_counts_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of loop_counts_array and waveform_handles_array parameters do not match.")  # case S160
        waveform_handles_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_handles_array, library_type=_visatype.ViInt32)  # case B550
        loop_counts_array_ctype = get_ctypes_pointer_for_buffer(value=loop_counts_array, library_type=_visatype.ViInt32)  # case B550
        sequence_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateArbSequence(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, None if sequence_handle_ctype is None else (ctypes.pointer(sequence_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(sequence_handle_ctype.value)

    @ivi_synchronized
    def create_freq_list(self, waveform, frequency_array, duration_array):
        r'''create_freq_list

        Creates a frequency list from an array of frequencies
        (**frequencyArray**) and an array of durations (**durationArray**). The
        two arrays should have the same number of elements, and this value must
        also be the size of the **frequencyListLength**. The method returns a
        handle that identifies the frequency list (the **frequencyListHandle**).
        You can pass this handle to configure_freq_list to specify what
        frequency list you want the signal generator to produce.

        A frequency list consists of a list of frequencies and durations. The
        signal generator generates each frequency for the given amount of time
        and then proceeds to the next frequency. When the end of the list is
        reached, the signal generator starts over at the beginning of the list.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Args:
            waveform (enums.Waveform): Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the func_waveform property to this
                value.

                ****Defined Values****

                **Default Value**: Waveform.SINE

                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SINE      | Specifies that the signal generator produces a sinusoid waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SQUARE    | Specifies that the signal generator produces a square waveform.                                                                |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.TRIANGLE  | Specifies that the signal generator produces a triangle waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.DC        | Specifies that the signal generator produces a constant voltage.                                                               |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.NOISE     | Specifies that the signal generator produces white noise.                                                                      |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.USER      | Specifies that the signal generator produces a user-defined waveform as defined with the define_user_standard_waveform method. |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+

            frequency_array (list of float): Specifies the array of frequencies to form the frequency list. The array
                must have at least as many elements as the value you specify in
                **frequencyListLength**. Each **frequencyArray** element has a
                corresponding **durationArray** element that indicates how long that
                frequency is repeated.

                **Units**: hertz

                **Default Value**: None

            duration_array (list of float): Specifies the array of durations to form the frequency list. The array
                must have at least as many elements as the value that you specify in
                **frequencyListLength**. Each **durationArray** element has a
                corresponding **frequencyArray** element and indicates how long in
                seconds to generate the corresponding frequency.

                **Units**: seconds

                **Default Value**: None


        Returns:
            frequency_list_handle (int): Returns the handle that identifies the new frequency list. You can pass
                this handle to configure_freq_list to generate the arbitrary
                sequence.

        '''
        if type(waveform) is not enums.Waveform:
            raise TypeError('Parameter waveform must be of type ' + str(enums.Waveform))
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_ctype = _visatype.ViInt32(waveform.value)  # case S130
        frequency_list_length_ctype = _visatype.ViInt32(0 if frequency_array is None else len(frequency_array))  # case S160
        if duration_array is not None and len(duration_array) != len(frequency_array):  # case S160
            raise ValueError("Length of duration_array and frequency_array parameters do not match.")  # case S160
        frequency_array_ctype = get_ctypes_pointer_for_buffer(value=frequency_array, library_type=_visatype.ViReal64)  # case B550
        duration_array_ctype = get_ctypes_pointer_for_buffer(value=duration_array, library_type=_visatype.ViReal64)  # case B550
        frequency_list_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateFreqList(vi_ctype, waveform_ctype, frequency_list_length_ctype, frequency_array_ctype, duration_array_ctype, None if frequency_list_handle_ctype is None else (ctypes.pointer(frequency_list_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(frequency_list_handle_ctype.value)

    @ivi_synchronized
    def disable(self):
        r'''disable

        Places the instrument in a quiescent state where it has minimal or no
        impact on the system to which it is connected. The analog output and all
        exported signals are disabled.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def export_attribute_configuration_buffer(self):
        r'''export_attribute_configuration_buffer

        Exports the property configuration of the session to a configuration
        buffer.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑FGEN returns an
        error.

        Returns:
            configuration (bytes): Specifies the byte array buffer to be populated with the exported
                property configuration.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.niFgen_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        size_in_bytes_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_in_bytes_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niFgen_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(configuration_array)

    @ivi_synchronized
    def export_attribute_configuration_file(self, file_path):
        r'''export_attribute_configuration_file

        Exports the property configuration of the session to the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑FGEN returns an
        error.

        Args:
            file_path (str): Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .nifgenconfig

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_ExportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def get_channel_name(self, index):
        r'''get_channel_name

        Returns the channel string that is in the channel table at an index you
        specify.

        Note:
        This method is included for compliance with the IviFgen Class
        Specification.

        Args:
            index (int): A 1-based index into the channel table.


        Returns:
            channel_string (str): Returns the channel string that is in the channel table at the index you
                specify. Do not modify the contents of the channel string.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        channel_string_ctype = None  # case C050
        error_code = self._library.niFgen_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        channel_string_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFgen_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_string_ctype.value.decode(self._encoding)

    @ivi_synchronized
    def _get_ext_cal_last_date_and_time(self):
        r'''_get_ext_cal_last_date_and_time

        Returns the date and time of the last successful external calibration.
        The time returned is 24-hour (military) local time; for example, if the
        device was calibrated at 2:30 PM, this method returns 14 for the
        **hour** parameter and 30 for the **minute** parameter.

        Returns:
            year (int): Specifies the year of the last successful calibration.

            month (int): Specifies the month of the last successful calibration.

            day (int): Specifies the day of the last successful calibration.

            hour (int): Specifies the hour of the last successful calibration.

            minute (int): Specifies the minute of the last successful calibration.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_GetExtCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    @ivi_synchronized
    def get_ext_cal_last_temp(self):
        r'''get_ext_cal_last_temp

        Returns the temperature at the last successful external calibration. The
        temperature is returned in degrees Celsius.

        Returns:
            temperature (float): Specifies the temperature at the last successful calibration in degrees
                Celsius.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFgen_GetExtCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    @ivi_synchronized
    def get_ext_cal_recommended_interval(self):
        r'''get_ext_cal_recommended_interval

        Returns the recommended interval between external calibrations in
        months.

        Returns:
            months (hightime.timedelta): Specifies the recommended interval between external calibrations in
                months.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_GetExtCalRecommendedInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_month_to_timedelta(int(months_ctype.value))

    @ivi_synchronized
    def get_hardware_state(self):
        r'''get_hardware_state

        Returns the current hardware state of the device and, if the device is
        in the hardware error state, the current hardware error.

        Note: Hardware states do not necessarily correspond to NI-FGEN states.

        Returns:
            state (enums.HardwareState): Returns the hardware state of the signal generator.

                **Defined Values**

                +-----------------------------------------+--------------------------------------------+
                | HardwareState.IDLE                      | The device is in the Idle state.           |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.WAITING_FOR_START_TRIGGER | The device is waiting for Start Trigger.   |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.RUNNING                   | The device is in the Running state.        |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.DONE                      | The generation has completed successfully. |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.HARDWARE_ERROR            | There is a hardware error.                 |
                +-----------------------------------------+--------------------------------------------+

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        state_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_GetHardwareState(vi_ctype, None if state_ctype is None else (ctypes.pointer(state_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.HardwareState(state_ctype.value)

    @ivi_synchronized
    def get_ext_cal_last_date_and_time(self):
        '''get_ext_cal_last_date_and_time

        Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this method returns 14 for the **hour** parameter and 30 for the **minute** parameter.

        Returns:
            month (hightime.datetime): Indicates date and time of the last calibration.

        '''
        year, month, day, hour, minute = self._get_ext_cal_last_date_and_time()
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def get_self_cal_last_date_and_time(self):
        '''get_self_cal_last_date_and_time

        Returns the date and time of the last successful self-calibration.

        Returns:
            month (hightime.datetime): Returns the date and time the device was last calibrated.

        '''
        year, month, day, hour, minute = self._get_self_cal_last_date_and_time()
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def _get_self_cal_last_date_and_time(self):
        r'''_get_self_cal_last_date_and_time

        Returns the date and time of the last successful self-calibration.

        All values are returned as separate parameters. Each parameter is
        returned as an integer, including the year, month, day, hour, minute,
        and second. For example, if the device is calibrated in September 2013,
        this method returns 9 for the **month** parameter and 2013 for the
        **year** parameter.

        The time returned is 24-hour (military) local time. For example, if the
        device was calibrated at 2:30 PM, this method returns 14 for the
        **hours** parameter and 30 for the **minutes** parameter.

        Returns:
            year (int): Specifies the year of the last successful calibration.

            month (int): Specifies the month of the last successful calibration.

            day (int): Specifies the day of the last successful calibration.

            hour (int): Specifies the hour of the last successful calibration.

            minute (int): Specifies the minute of the last successful calibration.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_GetSelfCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    @ivi_synchronized
    def get_self_cal_last_temp(self):
        r'''get_self_cal_last_temp

        Returns the temperature at the last successful self-calibration. The
        temperature is returned in degrees Celsius.

        Returns:
            temperature (float): Specifies the temperature at the last successful calibration in degrees
                Celsius.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFgen_GetSelfCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    @ivi_synchronized
    def get_self_cal_supported(self):
        r'''get_self_cal_supported

        Returns whether the device supports self–calibration.

        Returns:
            self_cal_supported (bool): Returns whether the device supports self-calibration.

                ****Defined Values****

                +-------+------------------------------------+
                | True  | Self–calibration is supported.     |
                +-------+------------------------------------+
                | False | Self–calibration is not supported. |
                +-------+------------------------------------+

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_cal_supported_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFgen_GetSelfCalSupported(vi_ctype, None if self_cal_supported_ctype is None else (ctypes.pointer(self_cal_supported_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_supported_ctype.value)

    @ivi_synchronized
    def import_attribute_configuration_buffer(self, configuration):
        r'''import_attribute_configuration_buffer

        Imports a property configuration to the session from the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        Note:
        You cannot call this method while the session is in a running state,
        such as while generating a signal.

        Args:
            configuration (bytes): Specifies the byte array buffer that contains the property
                configuration to import.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_converted = _converters.convert_to_bytes(configuration)  # case B520
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_converted, library_type=_visatype.ViInt8)  # case B520
        error_code = self._library.niFgen_ImportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def import_attribute_configuration_file(self, file_path):
        r'''import_attribute_configuration_file

        Imports a property configuration to the session from the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        Note:
        You cannot call this method while the session is in a running state,
        such as while generating a signal.

        Args:
            file_path (str): Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .nifgenconfig

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_ImportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _initialize_with_channels(self, resource_name, channel_name=None, reset_device=False, option_string=""):
        r'''_initialize_with_channels

        Creates and returns a new NI-FGEN session to the specified channel of a
        waveform generator that is used in all subsequent NI-FGEN method
        calls.

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
                However, all IVI names, such as logical names, are case-sensitive. If
                you use logical names, driver session names, or virtual names in your
                program, you must ensure that the name you use matches the name in the
                IVI Configuration Store file exactly, without any variations in the case
                of the characters.

                | Specifies the resource name of the device to initialize.

                For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
                the device number assigned by MAX, as shown in Example 1.

                For NI-DAQmx devices, the syntax is just the device name specified in
                MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
                in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
                right-clicking on the name in MAX and entering a new name.

                An alternate syntax for NI-DAQmx devices consists of DAQ::\ *NI-DAQmx
                device name*, as shown in Example 3. This naming convention allows for
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

                +-----------+--------------------------------------+------------------------+---------------------------------+
                | Example # | Device Type                          | Syntax                 | Variable                        |
                +===========+======================================+========================+=================================+
                | 1         | Traditional NI-DAQ device            | DAQ::\ *1*             | (*1* = device number)           |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 2         | NI-DAQmx device                      | *myDAQmxDevice*        | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 3         | NI-DAQmx device                      | DAQ::\ *myDAQmxDevice* | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 4         | NI-DAQmx device                      | DAQ::\ *2*             | (*2* = device name)             |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 5         | IVI logical name or IVI virtual name | *myLogicalName*        | (*myLogicalName* = name)        |
                +-----------+--------------------------------------+------------------------+---------------------------------+

            channel_name (str, list, range, tuple): Specifies the channel that this VI uses.

                **Default Value**: "0"

            reset_device (bool): Specifies whether you want to reset the device during the initialization
                procedure. True specifies that the device is reset and performs the
                same method as the Reset method.

                ****Defined Values****

                **Default Value**: False

                +-------+---------------------+
                | True  | Reset device        |
                +-------+---------------------+
                | False | Do not reset device |
                +-------+---------------------+

            option_string (dict): Sets the initial value of certain session properties.

                The syntax for **optionString** is

                <*attributeName*> = <*value*>

                where

                *attributeName* is the name of the property and *value* is the value to
                which the property is set

                To set multiple properties, separate them with a comma.

                If you pass NULL or an empty string for this parameter, the session uses
                the default values for these properties. You can override the default
                values by assigning a value explicitly in a string that you pass for
                this parameter.

                You do not have to specify all of the properties and may leave any of
                them out. However, if you do not specify one of the properties, its
                default value is used.

                If simulation is enabled (Simulate=1), you may specify the device that
                you want to simulate. To specify a device, enter the following syntax in
                **optionString**.

                DriverSetup=Model:<*driver model number*>;Channels:<*channel
                names*>;BoardType:<*module type*>;MemorySize:<*size of onboard memory in
                bytes*>

                **Syntax Examples**

                **Properties and **Defined Values****

                **Default Values**: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"

                +------------------+-------------------------+-------------+
                | Property Name    | Property                | Values      |
                +==================+=========================+=============+
                | RangeCheck       | RANGE_CHECK             | True, False |
                +------------------+-------------------------+-------------+
                | QueryInstrStatus | QUERY_INSTRUMENT_STATUS | True, False |
                +------------------+-------------------------+-------------+
                | Cache            | CACHE                   | True, False |
                +------------------+-------------------------+-------------+
                | Simulate         | simulate                | True, False |
                +------------------+-------------------------+-------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            vi (int): Returns a session handle that you can use to identify the device in all
                subsequent NI-FGEN method calls.

        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        channel_name_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(channel_name).encode(self._encoding))  # case C040
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(self._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niFgen_InitializeWithChannels(resource_name_ctype, channel_name_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    @ivi_synchronized
    def _initiate_generation(self):
        r'''_initiate_generation

        Initiates signal generation. If you want to abort signal generation,
        call the abort method. After the signal generation
        is aborted, you can call the initiate method to
        cause the signal generator to produce a signal again.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_InitiateGeneration(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def is_done(self):
        r'''is_done

        Determines whether the current generation is complete. This method
        sets the **done** parameter to True if the session is in the Idle or
        Committed states.

        Note:
        NI-FGEN only reports the **done** parameter as True after the
        current generation is complete in Single trigger mode.

        Returns:
            done (bool): Returns information about the completion of waveform generation.

                **Defined Values**

                +-------+-----------------------------+
                | True  | Generation is complete.     |
                +-------+-----------------------------+
                | False | Generation is not complete. |
                +-------+-----------------------------+

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFgen_IsDone(vi_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    @ivi_synchronized
    def query_arb_seq_capabilities(self):
        r'''query_arb_seq_capabilities

        Returns the properties of the signal generator that are related to
        creating arbitrary sequences (the max_num_sequences,
        min_sequence_length,
        max_sequence_length, and max_loop_count
        properties).

        Returns:
            maximum_number_of_sequences (int): Returns the maximum number of arbitrary waveform sequences that the
                signal generator allows. NI-FGEN obtains this value from the
                max_num_sequences property.

            minimum_sequence_length (int): Returns the minimum number of arbitrary waveforms the signal generator
                allows in a sequence. NI-FGEN obtains this value from the
                min_sequence_length property.

            maximum_sequence_length (int): Returns the maximum number of arbitrary waveforms the signal generator
                allows in a sequence. NI-FGEN obtains this value from the
                max_sequence_length property.

            maximum_loop_count (int): Returns the maximum number of times the signal generator can repeat an
                arbitrary waveform in a sequence. NI-FGEN obtains this value from the
                max_loop_count property.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_number_of_sequences_ctype = _visatype.ViInt32()  # case S220
        minimum_sequence_length_ctype = _visatype.ViInt32()  # case S220
        maximum_sequence_length_ctype = _visatype.ViInt32()  # case S220
        maximum_loop_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_QueryArbSeqCapabilities(vi_ctype, None if maximum_number_of_sequences_ctype is None else (ctypes.pointer(maximum_number_of_sequences_ctype)), None if minimum_sequence_length_ctype is None else (ctypes.pointer(minimum_sequence_length_ctype)), None if maximum_sequence_length_ctype is None else (ctypes.pointer(maximum_sequence_length_ctype)), None if maximum_loop_count_ctype is None else (ctypes.pointer(maximum_loop_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_sequences_ctype.value), int(minimum_sequence_length_ctype.value), int(maximum_sequence_length_ctype.value), int(maximum_loop_count_ctype.value)

    @ivi_synchronized
    def query_arb_wfm_capabilities(self):
        r'''query_arb_wfm_capabilities

        Returns the properties of the signal generator that are related to
        creating arbitrary waveforms. These properties are the maximum number of
        waveforms, waveform quantum, minimum waveform size, and maximum waveform
        size.

        Note:
        If you do not want to obtain the waveform quantum, pass a value of
        VI_NULL for this parameter.

        Returns:
            maximum_number_of_waveforms (int): Returns the maximum number of arbitrary waveforms that the signal
                generator allows. NI-FGEN obtains this value from the
                max_num_waveforms property.

            waveform_quantum (int): The size (number of points) of each waveform must be a multiple of a
                constant quantum value. This parameter obtains the quantum value that
                the signal generator uses. NI-FGEN returns this value from the
                waveform_quantum property.

                For example, when this property returns a value of 8, all waveform
                sizes must be a multiple of 8.

            minimum_waveform_size (int): Returns the minimum number of points that the signal generator allows in
                a waveform. NI-FGEN obtains this value from the
                min_waveform_size property.

            maximum_waveform_size (int): Returns the maximum number of points that the signal generator allows in
                a waveform. NI-FGEN obtains this value from the
                max_waveform_size property.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_number_of_waveforms_ctype = _visatype.ViInt32()  # case S220
        waveform_quantum_ctype = _visatype.ViInt32()  # case S220
        minimum_waveform_size_ctype = _visatype.ViInt32()  # case S220
        maximum_waveform_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_QueryArbWfmCapabilities(vi_ctype, None if maximum_number_of_waveforms_ctype is None else (ctypes.pointer(maximum_number_of_waveforms_ctype)), None if waveform_quantum_ctype is None else (ctypes.pointer(waveform_quantum_ctype)), None if minimum_waveform_size_ctype is None else (ctypes.pointer(minimum_waveform_size_ctype)), None if maximum_waveform_size_ctype is None else (ctypes.pointer(maximum_waveform_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_waveforms_ctype.value), int(waveform_quantum_ctype.value), int(minimum_waveform_size_ctype.value), int(maximum_waveform_size_ctype.value)

    @ivi_synchronized
    def query_freq_list_capabilities(self):
        r'''query_freq_list_capabilities

        Returns the properties of the signal generator that are related to
        creating frequency lists. These properties are
        max_num_freq_lists,
        min_freq_list_length,
        max_freq_list_length,
        min_freq_list_duration,
        max_freq_list_duration, and
        freq_list_duration_quantum.

        Returns:
            maximum_number_of_freq_lists (int): Returns the maximum number of frequency lists that the signal generator
                allows. NI-FGEN obtains this value from the
                max_num_freq_lists property.

            minimum_frequency_list_length (int): Returns the minimum number of steps that the signal generator allows in
                a frequency list. NI-FGEN obtains this value from the
                min_freq_list_length property.

            maximum_frequency_list_length (int): Returns the maximum number of steps that the signal generator allows in
                a frequency list. NI-FGEN obtains this value from the
                max_freq_list_length property.

            minimum_frequency_list_duration (float): Returns the minimum duration that the signal generator allows in a step
                of a frequency list. NI-FGEN obtains this value from the
                min_freq_list_duration property.

            maximum_frequency_list_duration (float): Returns the maximum duration that the signal generator allows in a step
                of a frequency list. NI-FGEN obtains this value from the
                max_freq_list_duration property.

            frequency_list_duration_quantum (float): Returns the quantum of which all durations must be a multiple in a
                frequency list. NI-FGEN obtains this value from the
                freq_list_duration_quantum property.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_number_of_freq_lists_ctype = _visatype.ViInt32()  # case S220
        minimum_frequency_list_length_ctype = _visatype.ViInt32()  # case S220
        maximum_frequency_list_length_ctype = _visatype.ViInt32()  # case S220
        minimum_frequency_list_duration_ctype = _visatype.ViReal64()  # case S220
        maximum_frequency_list_duration_ctype = _visatype.ViReal64()  # case S220
        frequency_list_duration_quantum_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFgen_QueryFreqListCapabilities(vi_ctype, None if maximum_number_of_freq_lists_ctype is None else (ctypes.pointer(maximum_number_of_freq_lists_ctype)), None if minimum_frequency_list_length_ctype is None else (ctypes.pointer(minimum_frequency_list_length_ctype)), None if maximum_frequency_list_length_ctype is None else (ctypes.pointer(maximum_frequency_list_length_ctype)), None if minimum_frequency_list_duration_ctype is None else (ctypes.pointer(minimum_frequency_list_duration_ctype)), None if maximum_frequency_list_duration_ctype is None else (ctypes.pointer(maximum_frequency_list_duration_ctype)), None if frequency_list_duration_quantum_ctype is None else (ctypes.pointer(frequency_list_duration_quantum_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_freq_lists_ctype.value), int(minimum_frequency_list_length_ctype.value), int(maximum_frequency_list_length_ctype.value), float(minimum_frequency_list_duration_ctype.value), float(maximum_frequency_list_duration_ctype.value), float(frequency_list_duration_quantum_ctype.value)

    @ivi_synchronized
    def read_current_temperature(self):
        r'''read_current_temperature

        Reads the current onboard temperature of the device. The temperature is
        returned in degrees Celsius.

        Returns:
            temperature (float): Returns the current temperature read from onboard temperature sensors,
                in degrees Celsius.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFgen_ReadCurrentTemperature(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    @ivi_synchronized
    def reset_device(self):
        r'''reset_device

        Performs a hard reset on the device. Generation is stopped, all routes
        are released, external bidirectional terminals are tristated, FPGAs are
        reset, hardware is configured to its default state, and all session
        properties are reset to their default states.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def reset_with_defaults(self):
        r'''reset_with_defaults

        Resets the instrument and reapplies initial user–specified settings from
        the logical name that was used to initialize the session. If the session
        was created without a logical name, this method is equivalent to the
        reset method.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def self_cal(self):
        r'''self_cal

        Performs a full internal self-calibration on the device. If the
        calibration is successful, new calibration data and constants are stored
        in the onboard EEPROM.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_SelfCal(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def wait_until_done(self, max_time=hightime.timedelta(seconds=10.0)):
        r'''wait_until_done

        Waits until the device is done generating or until the maximum time has
        expired.

        Args:
            max_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the timeout value in milliseconds.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        max_time_ctype = _converters.convert_timedelta_to_milliseconds_int32(max_time)  # case S140
        error_code = self._library.niFgen_WaitUntilDone(vi_ctype, max_time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        r'''_close

        Performs the following operations:

        -  Closes the instrument I/O session.
        -  Destroys the NI-FGEN session and all of its properties.
        -  Deallocates any memory resources NI-FGEN uses.

        Not all signal routes established by calling the ExportSignal
        and RouteSignalOut methods are released when the NI-FGEN
        session is closed. The following table shows what happens to a signal
        route on your device when you call the _close method.

        +--------------------+-------------------+------------------+
        | Routes To          | NI 5401/5411/5431 | Other Devices    |
        +====================+===================+==================+
        | Front Panel        | Remain connected  | Remain connected |
        +--------------------+-------------------+------------------+
        | RTSI/PXI Backplane | Remain connected  | Disconnected     |
        +--------------------+-------------------+------------------+

        Note:
        After calling _close, you cannot use NI-FGEN again until you
        call the init or InitWithOptions methods.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def self_test(self):
        '''self_test

        Runs the instrument self-test routine and returns the test result(s).

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

        Note:
        When used on some signal generators, the device is reset after the
        self_test method runs. If you use the self_test
        method, your device may not be in its previously configured state
        after the method runs.
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def reset(self):
        r'''reset

        Resets the instrument to a known state. This method aborts the
        generation, clears all routes, and resets session properties to the
        default values. This method does not, however, commit the session
        properties or configure the device hardware to its default state.

        Note:
        For the NI 5401/5404/5411/5431, this method exhibits the same
        behavior as the reset_device method.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Runs the instrument self-test routine and returns the test result(s).

        Note:
        When used on some signal generators, the device is reset after the
        self_test method runs. If you use the self_test
        method, your device may not be in its previously configured state
        after the method runs.

        Returns:
            self_test_result (int): Contains the value returned from the instrument self-test. A value of 0
                indicates success.

                +----------------+------------------+
                | Self-Test Code | Description      |
                +================+==================+
                | 0              | Passed self-test |
                +----------------+------------------+
                | 1              | Self-test failed |
                +----------------+------------------+

            self_test_message (str): Returns the self-test response string from the instrument.

                You must pass a ViChar array with at least 256 bytes.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFgen_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



