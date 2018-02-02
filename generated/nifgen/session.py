# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
import ctypes
import struct  # noqa: F401

from nifgen import _converters  # noqa: F401   TODO(texasaggie97) remove noqa once we are using converters everywhere
from nifgen import attributes
from nifgen import enums
from nifgen import errors
from nifgen import library_singleton
from nifgen import visatype

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


class _Generation(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._session._initiate_generation()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


class _Channels(object):
    def __init__(self, vi, library, encoding):
        self._vi = vi
        self._library = library
        self._encoding = encoding

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        # First try it as a list
        try:
            rep_cap_list = [str(r) if str(r).lower().startswith('') else '' + str(r) for r in repeated_capability]
        except TypeError:
            # Then try it as a slice
            try:
                def ifnone(a, b):
                    return b if a is None else a
                # Turn the slice into a list so we can iterate over it
                rep_cap_list = list(range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1)))
                # Add prefix to each entry
                rep_cap_list = ['' + str(r) for r in rep_cap_list]
            # Otherwise it must be a single item
            except TypeError:
                rep_cap_list = [str(repeated_capability) if str(repeated_capability).lower().startswith('') else '' + str(repeated_capability)]

        return _SessionBase(vi=self._vi, repeated_capability=','.join(rep_cap_list), library=self._library, encoding=self._encoding, freeze_it=True)


class _P2PStreams(object):
    def __init__(self, vi, library, encoding):
        self._vi = vi
        self._library = library
        self._encoding = encoding

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        # First try it as a list
        try:
            rep_cap_list = [str(r) if str(r).lower().startswith('fifoendpoint') else 'FIFOEndpoint' + str(r) for r in repeated_capability]
        except TypeError:
            # Then try it as a slice
            try:
                def ifnone(a, b):
                    return b if a is None else a
                # Turn the slice into a list so we can iterate over it
                rep_cap_list = list(range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1)))
                # Add prefix to each entry
                rep_cap_list = ['FIFOEndpoint' + str(r) for r in rep_cap_list]
            # Otherwise it must be a single item
            except TypeError:
                rep_cap_list = [str(repeated_capability) if str(repeated_capability).lower().startswith('fifoendpoint') else 'FIFOEndpoint' + str(repeated_capability)]

        return _SessionBase(vi=self._vi, repeated_capability=','.join(rep_cap_list), library=self._library, encoding=self._encoding, freeze_it=True)


class _ScriptTriggers(object):
    def __init__(self, vi, library, encoding):
        self._vi = vi
        self._library = library
        self._encoding = encoding

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        # First try it as a list
        try:
            rep_cap_list = [str(r) if str(r).lower().startswith('scripttrigger') else 'ScriptTrigger' + str(r) for r in repeated_capability]
        except TypeError:
            # Then try it as a slice
            try:
                def ifnone(a, b):
                    return b if a is None else a
                # Turn the slice into a list so we can iterate over it
                rep_cap_list = list(range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1)))
                # Add prefix to each entry
                rep_cap_list = ['ScriptTrigger' + str(r) for r in rep_cap_list]
            # Otherwise it must be a single item
            except TypeError:
                rep_cap_list = [str(repeated_capability) if str(repeated_capability).lower().startswith('scripttrigger') else 'ScriptTrigger' + str(repeated_capability)]

        return _SessionBase(vi=self._vi, repeated_capability=','.join(rep_cap_list), library=self._library, encoding=self._encoding, freeze_it=True)


class _Markers(object):
    def __init__(self, vi, library, encoding):
        self._vi = vi
        self._library = library
        self._encoding = encoding

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        # First try it as a list
        try:
            rep_cap_list = [str(r) if str(r).lower().startswith('marker') else 'Marker' + str(r) for r in repeated_capability]
        except TypeError:
            # Then try it as a slice
            try:
                def ifnone(a, b):
                    return b if a is None else a
                # Turn the slice into a list so we can iterate over it
                rep_cap_list = list(range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1)))
                # Add prefix to each entry
                rep_cap_list = ['Marker' + str(r) for r in rep_cap_list]
            # Otherwise it must be a single item
            except TypeError:
                rep_cap_list = [str(repeated_capability) if str(repeated_capability).lower().startswith('marker') else 'Marker' + str(repeated_capability)]

        return _SessionBase(vi=self._vi, repeated_capability=','.join(rep_cap_list), library=self._library, encoding=self._encoding, freeze_it=True)


class _SessionBase(object):
    '''Base class for all NI-FGEN sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    all_marker_events_latched_status = attributes.AttributeViInt32(1150349)
    '''Type: int

    Returns a bit field of the latched status of all Marker Events.  Write 0 to this attribute to clear the latched status of all Marker Events.
    '''
    all_marker_events_live_status = attributes.AttributeViInt32(1150344)
    '''Type: int

    Returns a bit field of the live status of all Marker Events.
    '''
    analog_data_mask = attributes.AttributeViInt32(1150234)
    '''Type: int

    Specifies the mask to apply to the analog output. The masked data is replaced with the data in NIFGEN_ATTR_ANALOG_STATIC_VALUE.
    '''
    analog_filter_enabled = attributes.AttributeViBoolean(1150103)
    '''Type: bool

    Controls whether the signal generator applies to an analog filter to the output signal. This attribute is valid in arbitrary waveform, arbitrary sequence, and script modes. This attribute can also be used in standard function and frequency list modes for user-defined waveforms.
    '''
    analog_path = attributes.AttributeEnum(attributes.AttributeViInt32, enums.AnalogPath, 1150222)
    '''Type: enums.AnalogPath

    Specifies the analog signal path that should be used. The main path allows you to configure gain, offset, analog filter status, output impedance, and output enable. The main path has two amplifier options, high- and low-gain.
    The direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The direct path also provides a smaller output range but also lower distortion. NI-FGEN normally chooses the amplifier based on the user-specified gain.
    '''
    analog_static_value = attributes.AttributeViInt32(1150235)
    '''Type: int

    Specifies the static value that replaces data masked by NIFGEN_ATTR_ANALOG_DATA_MASK.
    '''
    arb_gain = attributes.AttributeViReal64(1250202)
    '''Type: float

    Specifies the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this attribute to scale the arbitrary waveform to other ranges.
    For example, when you set this attribute to 2.0, the output signal ranges from -2.0 V to +2.0 V.
    Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.
    '''
    arb_marker_position = attributes.AttributeViInt32(1150327)
    '''Type: int

    Specifies the position for a marker to be asserted in the arbitrary waveform. This attribute defaults to -1 when no marker position is specified. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.
    Use niFgen_ExportSignal to export the marker signal.
    '''
    arb_offset = attributes.AttributeViReal64(1250203)
    '''Type: float

    Specifies the value that the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this attribute to shift the arbitrary waveform range.
    For example, when you set this attribute to 1.0, the output signal ranges from 2.0 V to 0.0 V.
    Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.
    Units: Volts
    '''
    arb_repeat_count = attributes.AttributeViInt32(1150328)
    '''Type: int

    Specifies number of times to repeat the arbitrary waveform when the triggerMode parameter of nifgen_ConfigureTriggerMode is set to NIFGEN_VAL_SINGLE or NIFGEN_VAL_STEPPED. This attribute is ignored if the triggerMode parameter is set to NIFGEN_VAL_CONTINUOUS or NIFGEN_VAL_BURST. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.
    When used during streaming, this attribute specifies the number of times to repeat the streaming waveform (the onboard memory allocated for streaming).  For more information about streaming, refer to the Streaming topic.
    '''
    arb_sample_rate = attributes.AttributeViReal64(1250204)
    '''Type: float

    Specifies the rate at which the signal generator outputs the points in arbitrary waveforms.  Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set  to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.
    Units: Samples/s
    '''
    arb_sequence_handle = attributes.AttributeViInt32(1250211)
    '''Type: int

    This channel-based attribute identifies which sequence the signal generator produces. You can create multiple sequences using niFgen_CreateArbSequence. niFgen_CreateArbSequence returns a handle that you can use to identify the particular sequence. To configure the signal generator to produce a particular sequence, set this attribute to the sequence handle.
    Use this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SEQ.
    '''
    arb_waveform_handle = attributes.AttributeViInt32(1250201)
    '''Type: int

    Selects which arbitrary waveform the signal generator produces. You can create multiple arbitrary waveforms using one of the following niFgen Create Waveform functions:
    niFgen_CreateWaveformF64
    niFgen_CreateWaveformI16
    niFgen_CreateWaveformFromFileI16
    niFgen_CreateWaveformFromFileF64
    niFgen_CreateWaveformFromFileHWS
    These functions return a handle that you can use to identify the particular waveform. To configure the signal generator to produce a particular waveform, set this attribute to the waveform handle.
    Use this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.
    '''
    aux_power_enabled = attributes.AttributeViBoolean(1150411)
    '''Type: bool

    Controls the specified auxiliary power pin. Setting this attribute to TRUE energizes the auxiliary power when the session is committed. When this attribute is FALSE, the power pin of the connector outputs no power.
    '''
    bus_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.BusType, 1150215)
    '''Type: enums.BusType

    The bus type of the signal generator.
    '''
    cache = attributes.AttributeViBoolean(1050004)
    '''Type: bool

    Specifies whether to cache the value of attributes.   When caching is enabled, NI-FGEN keeps track of  the current device settings and avoids sending redundant commands to  the device. Thus, you can significantly increase execution speed.
    NI-FGEN can choose to always cache or to never cache  particular attributes regardless of the setting of this attribute.  Use niFgen_InitWithOptions to override the default value.
    '''
    cal_adc_input = attributes.AttributeEnum(attributes.AttributeViInt32, enums.CalADCInput, 1150227)
    '''Type: enums.CalADCInput

    Specifies the input of the calibration ADC. The ADC can take a reading from several inputs: the analog output, a 2.5 V reference, and ground.
    '''
    channel_delay = attributes.AttributeViReal64(1150369)
    '''Type: float

    Specifies, in seconds, the delay to apply to the analog output of the channel specified by the channel string. You can use the channel delay to configure the timing relationship between channels on a multichannel device. Values for this attribute can be zero or positive. A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds.
    '''
    clock_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ClockMode, 1150110)
    '''Type: enums.ClockMode

    Controls which clock mode is used for the signal generator.
    For signal generators that support it, this attribute allows switching the sample  clock to High-Resolution mode. When in Divide-Down  mode, the sample rate can only be set to certain frequences, based on  dividing down the update clock. However, in High-Resolution mode, the  sample rate may be set to any value.
    '''
    common_mode_offset = attributes.AttributeViReal64(1150366)
    '''Type: float

    Specifies, in volts, the value the signal generator adds to or subtracts from the arbitrary waveform data. This attribute applies only when you set the NIFGEN_ATTR_TERMINAL_CONFIGURATION attribute to NIFGEN_VAL_DIFFERENTIAL. Common mode offset is applied to the signals generated at each differential output terminal.
    '''
    data_marker_events_count = attributes.AttributeViInt32(1150273)
    '''Type: int

    Returns the number of Data Marker Events supported by the device.
    '''
    data_marker_event_data_bit_number = attributes.AttributeViInt32(1150337)
    '''Type: int

    Specifies the bit number to assign to the Data Marker Event.
    '''
    data_marker_event_level_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DataMarkerEventLevelPolarity, 1150338)
    '''Type: enums.DataMarkerEventLevelPolarity

    Specifies the output polarity of the Data marker event.
    '''
    data_marker_event_output_terminal = attributes.AttributeViString(1150339)
    '''Type: str

    Specifies the destination terminal for the Data Marker Event.
    '''
    data_transfer_block_size = attributes.AttributeViInt32(1150241)
    '''Type: int

    The number of samples at a time to download to onboard memory. Useful when the total data to be transferred to onboard memory is large.
    '''
    data_transfer_maximum_bandwidth = attributes.AttributeViReal64(1150373)
    '''Type: float

    Specifies the maximum amount of bus bandwidth (in bytes per second) to use for data transfers. The signal generator limits data transfer speeds on the PCIe bus to the value you specify for this attribute. Set this attribute to optimize bus bandwidth usage for multi-device streaming applications by preventing the signal generator from consuming all of the available bandwidth on a PCI express link when waveforms are being written to the onboard memory of the device.
    '''
    data_transfer_maximum_in_flight_reads = attributes.AttributeViInt32(1150375)
    '''Type: int

    Specifies the maximum number of concurrent PCI Express read requests the signal generator can issue.
    When transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this attribute is set to the highest value the signal generator supports.
    If other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the NI signal generator issues. This helps to reduce the amount of data the signal generator reads at one time.
    '''
    data_transfer_preferred_packet_size = attributes.AttributeViInt32(1150374)
    '''Type: int

    Specifies the preferred size of the data field in a PCI Express read request packet. In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.
    Recommended values for this attribute are powers of two between 64 and 512.
    In some cases, the signal generator generates packets smaller than  the preferred size you set with this attribute.
    You cannot change this attribute while the device is generating a waveform. If you want to change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete.

    Note:
    :
    '''
    digital_data_mask = attributes.AttributeViInt32(1150236)
    '''Type: int

    Specifies the mask to apply to the output on the digital connector. The masked data is replaced with the data in NIFGEN_ATTR_DIGITAL_STATIC_VALUE.
    '''
    digital_edge_script_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ScriptTriggerDigitalEdgeEdge, 1150292)
    '''Type: enums.ScriptTriggerDigitalEdgeEdge

    Specifies the active edge for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Edge.
    '''
    digital_edge_script_trigger_source = attributes.AttributeViString(1150291)
    '''Type: str

    Specifies the source terminal for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Edge.
    '''
    digital_edge_start_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartTriggerDigitalEdgeEdge, 1150282)
    '''Type: enums.StartTriggerDigitalEdgeEdge

    Specifies the active edge for the Start trigger. This attribute is used only when NIFGEN_ATTR_START_TRIGGER_TYPE is set to Digital Edge.
    '''
    digital_edge_start_trigger_source = attributes.AttributeViString(1150281)
    '''Type: str

    Specifies the source terminal for the Start trigger. This attribute is used only when NIFGEN_ATTR_START_TRIGGER_TYPE is set to Digital Edge.
    '''
    digital_filter_enabled = attributes.AttributeViBoolean(1150102)
    '''Type: bool

    Controls whether the signal generator applies a digital filter to the output signal. This attribute is valid in arbitrary waveform, arbitrary sequence, and script modes. This attribute can also be used in standard function and frequency list modes for user-defined waveforms.
    '''
    digital_filter_interpolation_factor = attributes.AttributeViReal64(1150218)
    '''Type: float

    This attribute only affects the device when NIFGEN_ATTR_DIGITAL_FILTER_ENABLED is set to VI_TRUE. If you do not set this attribute directly, NI-FGEN automatically selects the maximum interpolation factor allowed for the current sample rate. Valid values are 2, 4, and 8.
    '''
    digital_gain = attributes.AttributeViReal64(1150254)
    '''Type: float

    Specifies a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the DAC. For a digital gain greater than 1.0, the product of digital gain times the generated data must be inside the range plus or minus 1.0 (assuming floating point data).  If the product exceeds these limits, the signal generator clips the output signal, and an error results.
    Some signal generators support both digital gain and an analog gain (analog gain is specified with the NIFGEN_ATTR_FUNC_AMPLITUDE attribute or the NIFGEN_ATTR_ARB_GAIN attribute). Digital gain can be changed during generation without the glitches that may occur when changing analog gains, due to relay switching. However, the DAC output resolution is a function of analog gain, so only analog gain makes full use of the resolution of the DAC.
    '''
    digital_level_script_trigger_active_level = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ScriptTriggerDigitalLevelActiveLevel, 1150294)
    '''Type: enums.ScriptTriggerDigitalLevelActiveLevel

    Specifies the active level for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Level.
    '''
    digital_level_script_trigger_source = attributes.AttributeViString(1150293)
    '''Type: str

    Specifies the source terminal for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Level.
    '''
    digital_pattern_enabled = attributes.AttributeViBoolean(1150101)
    '''Type: bool

    Controls whether the signal generator generates a digital pattern of the output signal.
    '''
    digital_static_value = attributes.AttributeViInt32(1150237)
    '''Type: int

    Specifies the static value that replaces data masked by NIFGEN_ATTR_DIGITAL_DATA_MASK.
    '''
    direct_dma_enabled = attributes.AttributeViBoolean(1150244)
    '''Type: bool

    Enable the device for Direct DMA writes. When enabled, all Create Waveform and Write Waveform function calls that are given a data address in the Direct DMA Window will download data residing on the Direct DMA device to the instrument's onboard memory.
    '''
    direct_dma_window_address = attributes.AttributeViInt32(1150274)
    '''Type: int

    Specifies the window address (beginning of window) of the waveform data source. This window address is specified by your Direct DMA-compatible data source.
    '''
    direct_dma_window_size = attributes.AttributeViInt32(1150245)
    '''Type: int

    Specifies the size of the memory window in bytes (not samples) provided by your Direct DMA-compatible data source.
    '''
    done_event_delay = attributes.AttributeViReal64(1150358)
    '''Type: float

    Specifies the amount of delay applied to a Done Event with respect to the  analog output of the signal generator. A positive delay value indicates that  the Done Event will come out after the analog data, while a negative delay  value indicates that the Done Event will come out before the analog data.  The default value is zero, which will align the Done Event with the analog output.  You can specify the units of the delay value by setting the  NIFGEN_ATTR_DONE_EVENT_DELAY attribute.
    '''
    done_event_delay_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DoneEventDelayUnits, 1150359)
    '''Type: enums.DoneEventDelayUnits

    Specifies the units applied to the value of the NIFGEN_ATTR_DONE_EVENT_DELAY attribute. Valid units are seconds and sample clock periods.
    '''
    done_event_latched_status = attributes.AttributeViBoolean(1150351)
    '''Type: bool

    Returns the latched status of the specified Done Event.
    '''
    done_event_level_active_level = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DoneEventActiveLevel, 1150317)
    '''Type: enums.DoneEventActiveLevel

    Specifies the output polarity of the Done Event.
    '''
    done_event_output_behavior = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DoneEventOutputBehavior, 1150332)
    '''Type: enums.DoneEventOutputBehavior

    Specifies the output behavior for the Done Event.
    '''
    done_event_output_terminal = attributes.AttributeViString(1150315)
    '''Type: str

    Specifies the destination terminal for the Done Event.
    '''
    done_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DoneEventPulsePolarity, 1150319)
    '''Type: enums.DoneEventPulsePolarity

    Specifies the output polarity of the Done Event.
    '''
    done_event_pulse_width = attributes.AttributeViReal64(1150336)
    '''Type: float

    Specifies the pulse width for the Done Event.
    '''
    done_event_pulse_width_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DoneEventPulseWidthUnits, 1150334)
    '''Type: enums.DoneEventPulseWidthUnits

    Specifies the pulse width units for the Done Event.
    '''
    driver_setup = attributes.AttributeViString(1050007)
    '''Type: str

    Specifies the driver setup portion of the option string that was passed into the niFgen_InitWithOptions function.
    '''
    exported_onboard_reference_clock_output_terminal = attributes.AttributeViString(1150322)
    '''Type: str

    Specifies the terminal to which to export the Onboard Reference Clock.
    '''
    exported_reference_clock_output_terminal = attributes.AttributeViString(1150321)
    '''Type: str

    Specifies the terminal to which to export the Reference Clock.
    '''
    exported_sample_clock_divisor = attributes.AttributeViInt32(1150219)
    '''Type: int

    Specifies the factor by which to divide the Sample clock, also known as the Update clock, before it is exported.  To export the Sample clock, use the niFgen_ExportSignal function or the  NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL attribute.
    '''
    exported_sample_clock_output_terminal = attributes.AttributeViString(1150320)
    '''Type: str

    Specifies the terminal to which to export the Sample Clock.
    '''
    exported_sample_clock_timebase_divisor = attributes.AttributeViInt32(1150230)
    '''Type: int

    Specifies the factor by which to divide the sample clock timebase (board clock) before it is exported.  To export the Sample clock timebase, use the niFgen_ExportSignal function or the  NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL attribute.
    '''
    exported_sample_clock_timebase_output_terminal = attributes.AttributeViString(1150329)
    '''Type: str

    Specifies the terminal to which to export the Sample clock timebase. If you specify a divisor with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR attribute,   the Sample clock exported with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL  attribute is the value of the Sample clock timebase after it is divided-down.  For a list of the terminals available on your device, refer to the Device Routes tab in MAX.
    To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this attribute.
    '''
    exported_script_trigger_output_terminal = attributes.AttributeViString(1150295)
    '''Type: str

    Specifies the output terminal for the exported Script trigger.
    Setting this attribute to an empty string means that when you commit the session, the signal is removed from that terminal and, if possible, the terminal is tristated.
    '''
    exported_start_trigger_output_terminal = attributes.AttributeViString(1150283)
    '''Type: str

    Specifies the destination terminal for exporting the Start trigger.
    '''
    external_clock_delay_binary_value = attributes.AttributeViInt32(1150233)
    '''Type: int

    Binary value of the external clock delay.
    '''
    external_sample_clock_multiplier = attributes.AttributeViReal64(1150376)
    '''Type: float

    Specifies a multiplication factor to use to obtain a desired sample rate from an external Sample clock.  The resulting sample rate is equal to this factor multiplied by the external Sample clock rate.  You can use this attribute to generate samples at a rate higher than your external clock rate.  When using this attribute, you do not need to explicitly set the external clock rate.
    '''
    file_transfer_block_size = attributes.AttributeViInt32(1150240)
    '''Type: int

    The number of samples at a time to read from the file and download to onboard memory. Used in conjunction with the Create From File and Write From File functions.
    '''
    filter_correction_frequency = attributes.AttributeViReal64(1150104)
    '''Type: float

    Controls the filter correction frequency of the analog filter. This attribute corrects for the ripples in the analog filter frequency response at the frequency specified. For standard waveform output, the filter correction frequency should be set to be the same as the frequency of the standard waveform. To have no filter correction, set this attribute to 0 Hz.
    '''
    flatness_correction_enabled = attributes.AttributeViBoolean(1150323)
    '''Type: bool

    When VI_TRUE, the signal generator applies a flatness correction factor to the generated sine wave in order to ensure the same output power level at all frequencies.
    This attribute should be set to VI_FALSE when performing Flatness Calibration.
    '''
    fpga_bitfile_path = attributes.AttributeViString(1150412)
    '''Type: str

    Gets the absolute file path to the bitfile loaded on the FPGA.
    '''
    freq_list_duration_quantum = attributes.AttributeViReal64(1150214)
    '''Type: float

    Returns the quantum of which all durations must be a multiple in a  frequency list.
    '''
    freq_list_handle = attributes.AttributeViInt32(1150208)
    '''Type: int

    Sets which frequency list the signal generator  produces. Create a frequency list using niFgen_CreateFreqList.  niFgen_CreateFreqList returns a handle that you can  use to identify the list.
    '''
    func_amplitude = attributes.AttributeViReal64(1250102)
    '''Type: float

    Controls the amplitude of the standard waveform that the  signal generator produces. This value is the amplitude at the  output terminal.
    For example, to produce a waveform ranging from -5.00 V to +5.00 V, set  the amplitude to 10.00 V.
    set the Waveform parameter to NIFGEN_VAL_WFM_DC.
    Units: Vpk-pk

    Note: This parameter does not affect signal generator behavior when you
    '''
    func_buffer_size = attributes.AttributeViInt32(1150238)
    '''Type: int

    This attribute contains the number of samples used in the standard function waveform  buffer. This attribute is only valid on devices that implement standard function mode  in software, and is read-only for all other devices.
    implementation of Standard Function Mode on your device.

    Note: Refer to the Standard Function Mode topic for more information on the
    '''
    func_dc_offset = attributes.AttributeViReal64(1250103)
    '''Type: float

    Controls the DC offset of the standard waveform that the  signal generator produces.  This value is the offset at the output  terminal. The value is the offset from ground to the center of the  waveform that you specify with the Waveform parameter.
    For example, to configure a waveform with an amplitude of 10.00 V to  range from 0.00 V to +10.00 V, set DC Offset to 5.00 V.
    Units: volts
    '''
    func_duty_cycle_high = attributes.AttributeViReal64(1250106)
    '''Type: float

    Controls the duty cycle of the square wave the signal generator  produces. Specify this attribute as a percentage of  the time the square wave is high in a cycle.
    set the Waveform parameter to NIFGEN_VAL_WFM_SQUARE.
    Units: Percentage of time the waveform is high

    Note: This parameter only affects signal generator behavior when you
    '''
    func_frequency = attributes.AttributeViReal64(1250104)
    '''Type: float

    Controls the frequency of the standard waveform that the  signal generator produces.
    Units: hertz
    (1) This parameter does not affect signal generator behavior when you  set the Waveform parameter of the niFgen_ConfigureStandardWaveform function  to NIFGEN_VAL_WFM_DC.
    (2) For NIFGEN_VAL_WFM_SINE, the range is between 0 MHz and 16 MHz, but the  range is between 0 MHz and 1 MHz for all other waveforms.

    Note:
    :
    '''
    func_max_buffer_size = attributes.AttributeViInt32(1150239)
    '''Type: int

    This attribute sets the maximum number of samples that can be used in the standard  function waveform buffer. Increasing this value may increase the quality of  the waveform. This attribute is only valid on devices that implement standard  function mode in software, and is read-only for all other devices.
    implementation of Standard Function Mode on your device.

    Note: Refer to the Standard Function Mode topic for more information on the
    '''
    func_start_phase = attributes.AttributeViReal64(1250105)
    '''Type: float

    Controls horizontal offset of the standard waveform the  signal generator produces. Specify this attribute in degrees of  one waveform cycle.
    A start phase of 180 degrees means output generation begins halfway  through the waveform. A start phase of 360 degrees offsets the output by  an entire waveform cycle, which is identical to a start phase of 0  degrees.
    set the Waveform parameter to NIFGEN_VAL_WFM_DC.
    Units: Degrees of one cycle

    Note: This parameter does not affect signal generator behavior when you
    '''
    func_waveform = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Waveform, 1250101)
    '''Type: enums.Waveform

    This channel-based attribute specifies which standard waveform the signal generator produces.
    Use this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to  NIFGEN_VAL_OUTPUT_FUNC.
    NIFGEN_VAL_WFM_SINE      - Sinusoid waveform
    NIFGEN_VAL_WFM_SQUARE    - Square waveform
    NIFGEN_VAL_WFM_TRIANGLE  - Triangle waveform
    NIFGEN_VAL_WFM_RAMP_UP   - Positive ramp waveform
    NIFGEN_VAL_WFM_RAMP_DOWN - Negative ramp waveform
    NIFGEN_VAL_WFM_DC        - Constant voltage
    NIFGEN_VAL_WFM_NOISE     - White noise
    NIFGEN_VAL_WFM_USER      - User-defined waveform as defined with
    niFgen_DefineUserStandardWaveform
    '''
    gain_dac_value = attributes.AttributeViInt32(1150223)
    '''Type: int

    Specifies the value programmed to the gain DAC. The value should be treated as an unsigned, right-justified number.
    '''
    group_capabilities = attributes.AttributeViString(1050401)
    '''Type: str

    Returns a string that contains a comma-separated list of class-extention groups that  NI-FGEN implements.
    '''
    idle_behavior = attributes.AttributeEnum(attributes.AttributeViInt32, enums.IdleBehavior, 1150377)
    '''Type: enums.IdleBehavior

    Specifies the behavior of the output during the Idle state.  The output can be configured to hold the last generated voltage before entering the Idle state or jump to the Idle Value.
    '''
    idle_value = attributes.AttributeViInt32(1150378)
    '''Type: int

    Specifies the value to generate in the Idle state.  The Idle Behavior must be configured to jump to this value.
    '''
    id_query_response = attributes.AttributeViString(1150001)
    instrument_firmware_revision = attributes.AttributeViString(1050510)
    '''Type: str

    A string that contains the firmware revision information  for the device that you are currently using.
    '''
    instrument_manufacturer = attributes.AttributeViString(1050511)
    '''Type: str

    A string that contains the name of the device manufacturer you are currently  using.
    '''
    instrument_model = attributes.AttributeViString(1050512)
    '''Type: str

    A string that contains the model number or name of the device that you  are currently using.
    '''
    interchange_check = attributes.AttributeViBoolean(1050021)
    '''Type: bool

    Specifies whether to perform interchangeability checking and retrieve  interchangeability warnings when you call  niFgen_InitiateGeneration.
    Interchangeability warnings indicate that using your application with a  different device might cause different behavior.   Call niFgen_GetNextInterchangeWarning to extract interchange warnings.   Call niFgen_ClearInterchangeWarnings to clear the list  of interchangeability warnings without reading them.
    Interchangeability checking examines the attributes in a  capability group only if you specify a value for at least one  attribute within that group. Interchangeability warnings can  occur when an attribute affects the behavior of the device and you  have not set that attribute, or the attribute has been invalidated since you set it.
    '''
    io_resource_descriptor = attributes.AttributeViString(1050304)
    '''Type: str

    Indicates the resource descriptor that NI-FGEN uses to identify the physical device.
    If you initialize NI-FGEN with a logical name, this  attribute contains the resource descriptor that corresponds  to the entry in the IVI Configuration Utility.
    If you initialize NI-FGEN with the resource  descriptor, this attribute contains that value.
    '''
    load_impedance = attributes.AttributeViReal64(1150220)
    '''Type: float

    This channel-based attribute specifies the load impedance connected to the analog output of the channel. If you set this attribute to NIFGEN_VAL_MATCHED_LOAD_IMPEDANCE (-1.0), NI-FGEN assumes that the load impedance matches the output impedance. NI-FGEN compensates to give the desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V).
    '''
    logical_name = attributes.AttributeViString(1050305)
    '''Type: str

    A string containing the logical name that you specified when opening the  current IVI session.
    You may pass a logical name to niFgen_init or  niFgen_InitWithOptions.  The IVI Configuration Utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.
    '''
    major_version = attributes.AttributeViInt32(1050503)
    '''Type: int

    Returns the major version number of NI-FGEN.
    '''
    marker_events_count = attributes.AttributeViInt32(1150271)
    '''Type: int

    Returns the number of markers supported by the device. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.
    '''
    marker_event_delay = attributes.AttributeViReal64(1150354)
    '''Type: float

    Specifies the amount of delay applied to a Marker Event with respect to the  analog output of the signal generator. A positive delay value indicates that  the Marker Event will come out after the analog data, while a negative delay  value indicates that the Marker Event will come out before the analog data.  The default value is zero, which will align the Marker Event with the  analog output. You can specify the units of the delay value by setting the NIFGEN_ATTR_MARKER_EVENT_DELAY attribute.
    '''
    marker_event_delay_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MarkerEventDelayUnits, 1150355)
    '''Type: enums.MarkerEventDelayUnits

    Specifies the units applied to the value of the NIFGEN_ATTR_MARKER_EVENT_DELAY attribute.  Valid units are seconds and sample clock periods.
    '''
    marker_event_latched_status = attributes.AttributeViBoolean(1150350)
    '''Type: bool

    Specifies the latched status of the specified Marker Event.
    Write VI_TRUE to this attribute to clear the latched status of the Marker Event.
    '''
    marker_event_live_status = attributes.AttributeViBoolean(1150345)
    '''Type: bool

    Returns the live status of the specified Marker Event.
    '''
    marker_event_output_behavior = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MarkerEventOutputBehavior, 1150342)
    '''Type: enums.MarkerEventOutputBehavior

    Specifies the output behavior for the Marker Event.
    '''
    marker_event_output_terminal = attributes.AttributeViString(1150312)
    '''Type: str

    Specifies the destination terminal for the Marker Event.
    '''
    marker_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MarkerEventPulsePolarity, 1150313)
    '''Type: enums.MarkerEventPulsePolarity

    Specifies the output polarity of the Marker Event.
    '''
    marker_event_pulse_width = attributes.AttributeViReal64(1150340)
    '''Type: float

    Specifies the pulse width for the Marker Event.
    '''
    marker_event_pulse_width_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MarkerEventPulseWidthUnits, 1150341)
    '''Type: enums.MarkerEventPulseWidthUnits

    Specifies the pulse width units for the Marker Event.
    '''
    marker_event_toggle_initial_state = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MarkerEventToggleInitialState, 1150343)
    '''Type: enums.MarkerEventToggleInitialState

    Specifies the output polarity of the Marker Event.
    '''
    max_freq_list_duration = attributes.AttributeViReal64(1150213)
    '''Type: float

    Returns the maximum duration of any one step in the frequency  list.
    '''
    max_freq_list_length = attributes.AttributeViInt32(1150211)
    '''Type: int

    Returns the maximum number of steps that can be in a frequency  list.
    '''
    max_loop_count = attributes.AttributeViInt32(1250215)
    '''Type: int

    Returns the maximum number of times that the signal generator can repeat a waveform in a sequence. Typically, this value is constant for the signal generator.
    '''
    max_num_freq_lists = attributes.AttributeViInt32(1150209)
    '''Type: int

    Returns the maximum number of frequency lists the signal generator allows.
    '''
    max_num_sequences = attributes.AttributeViInt32(1250212)
    '''Type: int

    Returns the maximum number of arbitrary sequences that the signal generator allows. Typically, this value is constant for the signal generator.
    '''
    max_num_waveforms = attributes.AttributeViInt32(1250205)
    '''Type: int

    Returns the maximum number of arbitrary waveforms that the signal generator allows. Typically, this value is constant for the signal generator.
    '''
    max_sequence_length = attributes.AttributeViInt32(1250214)
    '''Type: int

    Returns the maximum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.
    '''
    max_waveform_size = attributes.AttributeViInt32(1250208)
    '''Type: int

    Returns the size, in samples, of the largest waveform that can be created. This attribute reflects the space currently available, taking into account previously allocated waveforms and instructions.
    '''
    memory_size = attributes.AttributeViInt32(1150242)
    '''Type: int

    The total amount of memory, in bytes, on the signal generator.
    '''
    minor_version = attributes.AttributeViInt32(1050504)
    '''Type: int

    Returns the minor version number of NI-FGEN.
    '''
    min_freq_list_duration = attributes.AttributeViReal64(1150212)
    '''Type: float

    Returns the minimum number of steps that can be in a frequency  list.
    '''
    min_freq_list_length = attributes.AttributeViInt32(1150210)
    '''Type: int

    Returns the minimum number of frequency lists that the signal generator allows.
    '''
    min_sequence_length = attributes.AttributeViInt32(1250213)
    '''Type: int

    Returns the minimum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.
    '''
    min_waveform_size = attributes.AttributeViInt32(1250207)
    '''Type: int

    Returns the minimum number of points that the signal generator allows in an arbitrary waveform. Typically, this value is constant for the signal generator.
    '''
    module_revision = attributes.AttributeViString(1150390)
    '''Type: str

    A string that contains the module revision  for the device that you are currently using.
    '''
    num_channels = attributes.AttributeViInt32(1050203)
    '''Type: int

    Indicates the number of channels that the specific instrument  driver supports.
    For each attribute for which IVI_VAL_MULTI_CHANNEL is set, the IVI Engine maintains a separate cache value for each channel.
    '''
    offset_dac_value = attributes.AttributeViInt32(1150224)
    '''Type: int

    Specifies the value programmed to the offset DAC. The value should be treated as an unsigned, right-justified number.
    '''
    oscillator_freq_dac_value = attributes.AttributeViInt32(1150225)
    '''Type: int

    Specifies the value programmed to the oscillator frequency DAC. The value should be treated as an unsigned, right-justified number.
    '''
    oscillator_phase_dac_value = attributes.AttributeViInt32(1150232)
    '''Type: int

    The value of the oscillator phase DAC.
    '''
    osp_carrier_enabled = attributes.AttributeViBoolean(1150249)
    '''Type: bool

    Enables or disables generation of the carrier.
    '''
    osp_carrier_frequency = attributes.AttributeViReal64(1150250)
    '''Type: float

    The frequency of the generated carrier.
    '''
    osp_carrier_phase_i = attributes.AttributeViReal64(1150251)
    '''Type: float

    I Carrier Phase in degrees at the first point of the generation.
    '''
    osp_carrier_phase_q = attributes.AttributeViReal64(1150252)
    '''Type: float

    Q Carrier Phase in degrees at the first point of the generation.  This attribute is only used when the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE  attribute is set to NIFGEN_VAL_OSP_COMPLEX.
    '''
    osp_cic_filter_enabled = attributes.AttributeViBoolean(1150257)
    '''Type: bool

    Enables or disables the CIC filter.
    The NIFGEN_ATTR_OSP_CIC_FILTER_ENABLED and NIFGEN_ATTR_OSP_FIR_FILTER_ENABLED  attributes must have the same enable/disable setting.
    '''
    osp_cic_filter_gain = attributes.AttributeViReal64(1150263)
    '''Type: float

    Gain applied at the final stage of the CIC filter. Commonly used to compensate  for attenuation in the FIR filter. For FIR filter types other than Custom,  NI-FGEN calculates the CIC gain in order to achieve unity gain between the FIR  and CIC filters. Setting this attribute overrides the value set by NI-FGEN.
    '''
    osp_cic_filter_interpolation = attributes.AttributeViReal64(1150258)
    '''Type: float

    Interpolation factor for the CIC filter. If you do not set this value, NI-FGEN  calculates the appropriate value based on the value of the NIFGEN_ATTR_OSP_IQ_RATE attribute.
    '''
    osp_compensate_for_filter_group_delay = attributes.AttributeViBoolean(1150389)
    '''Type: bool

    Compensate for OSP Filter Group Delay. If this is enabled, the Event Outputs will be aligned  with the Analog Output. The Analog output will also be aligned between synchronized devices  (using NI-TClk).
    '''
    osp_data_processing_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DataProcessingMode, 1150247)
    '''Type: enums.DataProcessingMode

    The way in which data is processed by the OSP block.
    '''
    osp_enabled = attributes.AttributeViBoolean(1150246)
    '''Type: bool

    Enables or disables the OSP block of the signal generator. When the OSP block is disabled, all OSP-related attributes are disabled and have no effect on the generated signal.
    '''
    osp_fir_filter_enabled = attributes.AttributeViBoolean(1150255)
    '''Type: bool

    Enables or disables the FIR filter.
    The NIFGEN_ATTR_OSP_CIC_FILTER_ENABLED and NIFGEN_ATTR_OSP_FIR_FILTER_ENABLED  attributes must have the same enable/disable setting.
    '''
    osp_fir_filter_flat_passband = attributes.AttributeViReal64(1150261)
    '''Type: float

    Passband value to use when calculating the FIR filter coefficients.  The FIR filter is designed to be flat to passband × IQ rate.  This attribute is used only when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE  attribute is set to NIFGEN_VAL_OSP_FLAT.
    '''
    osp_fir_filter_gaussian_bt = attributes.AttributeViReal64(1150262)
    '''Type: float

    BT value to use when calculating the pulse-shaping FIR filter coefficients.  Only used when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute is set to  NIFGEN_VAL_OSP_GAUSSIAN.
    '''
    osp_fir_filter_interpolation = attributes.AttributeViReal64(1150256)
    '''Type: float

    Interpolation factor for the FIR filter. If you do not set this value,  NI-FGEN calculates the appropriate value based on the value of the NIFGEN_ATTR_OSP_IQ_RATE attribute.
    '''
    osp_fir_filter_raised_cosine_alpha = attributes.AttributeViReal64(1150260)
    '''Type: float

    Alpha value to use when calculating the pulse shaping FIR filter  coefficients. Only used when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE  attribute is set to NIFGEN_VAL_OSP_RAISED_COSINE.
    '''
    osp_fir_filter_root_raised_cosine_alpha = attributes.AttributeViReal64(1150259)
    '''Type: float

    Alpha value to use when calculating the pulse-shaping FIR filter  coefficients. This attribute is used only when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE  attribute is set to NIFGEN_VAL_OSP_ROOT_RAISED_COSINE.
    '''
    osp_fir_filter_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.FilterType, 1150253)
    '''Type: enums.FilterType

    Pulse-shaping filter type for the FIR filter.
    '''
    osp_frequency_shift = attributes.AttributeViReal64(1150371)
    '''Type: float

    Specifies the amount of frequency shift applied to the baseband signal.
    '''
    osp_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OSPMode, 1150370)
    '''Type: enums.OSPMode

    Specifies the generation mode of the OSP, which determines the type of data contained in the output signal.
    '''
    osp_overflow_error_reporting = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OSPOverflowErrorReporting, 1150268)
    '''Type: enums.OSPOverflowErrorReporting

    Configures error reporting when the OSP block detects an overflow in any of its stages.  Overflows lead to clipping of the waveform.
    You can use the NIFGEN_ATTR_OSP_OVERFLOW_STATUS attribute to query for overflow  conditions whether or not the NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING attribute is  enabled. The device will continue to generate after an overflow whether or not the  NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING attribute is enabled.
    '''
    osp_overflow_status = attributes.AttributeViInt32(1150269)
    '''Type: int

    Returns a bit field of the overflow status in any stage of the OSP block.  This attribute is functional regardless of the value for the  NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING attribute.
    Write 0 to this attribute to clear the current NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING value.
    '''
    osp_pre_filter_gain_i = attributes.AttributeViReal64(1150264)
    '''Type: float

    Digital gain to apply to the I data stream before any filtering by the OSP block.
    '''
    osp_pre_filter_gain_q = attributes.AttributeViReal64(1150265)
    '''Type: float

    Digital gain to apply to the Q data stream before any filtering by the OSP block.  This attribute is only used when the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute  is set to NIFGEN_VAL_OSP_COMPLEX.
    '''
    osp_pre_filter_offset_i = attributes.AttributeViReal64(1150266)
    '''Type: float

    Digital offset to apply to the I data stream. This offset is applied after  the Pre-Filter Gain and before any filtering.
    '''
    osp_pre_filter_offset_q = attributes.AttributeViReal64(1150267)
    '''Type: float

    Digital offset to apply to the Q data stream. This offset is applied after  the Pre-Filter Gain and before any filtering. This attribute is used only when  the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute is set to NIFGEN_VAL_OSP_COMPLEX.
    '''
    output_enabled = attributes.AttributeViBoolean(1250003)
    '''Type: bool

    This channel-based attribute specifies whether the signal that the signal generator produces appears at the output connector.
    '''
    output_impedance = attributes.AttributeViReal64(1250004)
    '''Type: float

    This channel-based attribute specifies the signal generator output impedance at the output connector. NI signal sources modules have an output impedance of 50 ohms and an optional 75 ohms on select modules. If the load impedance matches the output impedance, then the voltage at the signal output connector is at the needed level. The voltage at the signal output connector varies with load output impedance, up to doubling the voltage for a high-impedance load.
    '''
    output_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OutputMode, 1250001)
    '''Type: enums.OutputMode

    Sets which output mode the signal generator will use. The value you specify determines which functions and attributes you use to configure the waveform the signal generator produces.

    Note: The signal generator must not be in the Generating state when you change this attribute. To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.
    '''
    p2p_endpoint_fullness_start_trigger_level = attributes.AttributeViInt32(1150410)
    '''Type: int

    Specifies the Endpoint threshold for the Start trigger. This attribute is used only when NIFGEN_ATTR_START_TRIGGER_TYPE is set to P2P Endpoint Fullness.
    '''
    pci_dma_optimizations_enabled = attributes.AttributeViBoolean(1150362)
    '''Type: bool

    Controls whether or not NI-FGEN allows performance optimizations for DMA transfers.
    This attribute is only valid for PCI and PXI SMC-based devices.
    This attribute is enabled (VI_TRUE) by default, and NI recommends leaving it enabled.
    '''
    post_amplifier_attenuation = attributes.AttributeViReal64(1150229)
    '''Type: float

    Specifies the amount of post-amplifier attenuation that should be applied to the signal (in dB).
    '''
    pre_amplifier_attenuation = attributes.AttributeViReal64(1150228)
    '''Type: float

    Specifies the amount of pre-amplifier attenuation that should be applied to the signal (in dB).
    '''
    range_check = attributes.AttributeViBoolean(1050002)
    '''Type: bool

    Specifies whether to validate attribute values and function parameters.  If enabled, NI-FGEN validates the parameter values that  you pass to the functions. Range-checking  parameters is very useful for debugging. After you validate your program,  you can set this attribute to VI_FALSE to disable range checking and  maximize performance.
    Default Value: VI_TRUE
    Use niFgen_InitWithOptions to override the default value.
    '''
    ready_for_start_event_level_active_level = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ReadyForStartEventActiveLevel, 1150311)
    '''Type: enums.ReadyForStartEventActiveLevel

    Specifies the output polarity of the Ready for Start Event.
    '''
    ready_for_start_event_live_status = attributes.AttributeViBoolean(1150348)
    '''Type: bool

    Returns the live status of the specified Ready For Start Event.
    '''
    ready_for_start_event_output_terminal = attributes.AttributeViString(1150310)
    '''Type: str

    Specifies the destination terminal for the Ready for Start Event.
    '''
    record_coercions = attributes.AttributeViBoolean(1050006)
    '''Type: bool

    Specifies whether the IVI Engine keeps a list of  the value coercions it makes for ViInt32 and ViReal64 attributes.   Call niFgen_GetNextCoercionRecord to extract and delete the oldest  coercion record from the list.
    Default Value: VI_FALSE
    Use niFgen_InitWithOptions to override default value.
    '''
    reference_clock_source = attributes.AttributeEnum(attributes.AttributeViString, enums.ReferenceClockSource, 1150113)
    '''Type: enums.ReferenceClockSource

    Specifies the reference clock source used by the signal generator.
    The signal generator derives the frequencies and sample rates that it uses  to generate waveforms from the source you specify.  For example, when you set this attribute to ClkIn, the signal  generator uses the signal it receives at the CLK IN front  panel connector as the Reference clock.
    To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this attribute.
    '''
    ref_clock_frequency = attributes.AttributeViReal64(1150107)
    '''Type: float

    Sets the frequency of the signal generator reference  clock. The signal generator uses the reference clock to derive  frequencies and sample rates when generating output.
    '''
    sample_clock_absolute_delay = attributes.AttributeViReal64(1150231)
    '''Type: float

    Specifies the absolute delay adjustment of the sample clock. The  sample clock delay adjustment is expressed in seconds.
    can only be applied when an external sample clock is used.

    Note: For the NI 5421, absolute delay
    '''
    sample_clock_source = attributes.AttributeEnum(attributes.AttributeViString, enums.SampleClockSource, 1150112)
    '''Type: enums.SampleClockSource

    Specifies the Sample clock source. If you specify a divisor with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR  attribute, the Sample clock exported with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL attribute is the  value of the Sample clock after it is divided-down. For a list of the terminals available on your device, refer  to the Device Routes tab in MAX.
    To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this attribute.
    '''
    sample_clock_timebase_rate = attributes.AttributeViReal64(1150368)
    '''Type: float

    Specifies the Sample clock timebase rate. This attribute applies only to external Sample clock timebases.
    To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this attribute.
    '''
    sample_clock_timebase_source = attributes.AttributeEnum(attributes.AttributeViString, enums.SampleClockTimebaseSource, 1150367)
    '''Type: enums.SampleClockTimebaseSource

    Specifies the Sample Clock Timebase source.
    To change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this attribute.
    '''
    script_to_generate = attributes.AttributeViString(1150270)
    '''Type: str

    Specifies which script the generator produces. To configure the generator to run a particular script, set this attribute to the name of the script. Use niFgen_WriteScript to create multiple scripts. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.

    Note: The signal generator must not be in the Generating state when you change this attribute. To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.
    '''
    script_triggers_count = attributes.AttributeViInt32(1150272)
    '''Type: int

    Specifies the number of Script triggers supported by the device. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.
    '''
    script_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ScriptTriggerType, 1150290)
    '''Type: enums.ScriptTriggerType

    Specifies the Script trigger type. Depending upon the value of this attribute, additional attributes may need to be configured to fully configure the trigger.
    '''
    serial_number = attributes.AttributeViString(1150243)
    '''Type: str

    The signal generator's serial number.
    '''
    simulate = attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Specifies whether to simulate NI-FGEN I/O  operations. If simulation is enabled, NI-FGEN  functions perform range checking and call Ivi_GetAttribute and  Ivi_SetAttribute, but they do not perform device I/O.   For output parameters that represent device data, NI-FGEN  functions return calculated values.
    Default Value: VI_FALSE
    Use niFgen_InitWithOptions to override default value.
    '''
    specific_driver_class_spec_major_version = attributes.AttributeViInt32(1050515)
    '''Type: int

    Returns the major version number of the class specification with which NI-FGEN is compliant.
    '''
    specific_driver_class_spec_minor_version = attributes.AttributeViInt32(1050516)
    '''Type: int

    Returns the minor version number of the class specification with which NI-FGEN is compliant.
    '''
    specific_driver_description = attributes.AttributeViString(1050514)
    '''Type: str

    Returns a brief description of NI-FGEN.
    '''
    specific_driver_revision = attributes.AttributeViString(1050551)
    '''Type: str

    A string that contains additional version information about  NI-FGEN.
    '''
    specific_driver_vendor = attributes.AttributeViString(1050513)
    '''Type: str

    A string that contains the name of the vendor that supplies NI-FGEN.
    '''
    started_event_delay = attributes.AttributeViReal64(1150356)
    '''Type: float

    Specifies the amount of delay applied to a Started Event with respect to the  analog output of the signal generator. A positive delay value specifies that  the Started Event occurs after the analog data, and a negative delay  value specifies that the Started Event occurs before the analog data.  The default value is zero, which will align the Started event with the analog output.
    You can specify the units of the delay value by setting the NIFGEN_ATTR_STARTED_EVENT_DELAY attribute.
    '''
    started_event_delay_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartedEventDelayUnits, 1150357)
    '''Type: enums.StartedEventDelayUnits

    Specifies the units applied to the value of the NIFGEN_ATTR_STARTED_EVENT_DELAY
    attribute.  Valid units are seconds and sample clock periods.
    '''
    started_event_latched_status = attributes.AttributeViBoolean(1150352)
    '''Type: bool

    Specifies the latched status of the Started Event.
    '''
    started_event_level_active_level = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartedEventActiveLevel, 1150316)
    '''Type: enums.StartedEventActiveLevel

    Specifies the output polarity of the Started Event.
    '''
    started_event_output_behavior = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartedEventOutputBehavior, 1150331)
    '''Type: enums.StartedEventOutputBehavior

    Specifies the output behavior for the Started Event.
    '''
    started_event_output_terminal = attributes.AttributeViString(1150314)
    '''Type: str

    Specifies the destination terminal for the Started Event.
    '''
    started_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartedEventPulsePolarity, 1150318)
    '''Type: enums.StartedEventPulsePolarity

    Specifies the output polarity of the Started Event.
    '''
    started_event_pulse_width = attributes.AttributeViReal64(1150335)
    '''Type: float

    Specifies the pulse width for the Started Event.
    '''
    started_event_pulse_width_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartedEventPulseWidthUnits, 1150333)
    '''Type: enums.StartedEventPulseWidthUnits

    Specifies the pulse width units for the Started Event.
    '''
    start_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartTriggerType, 1150280)
    '''Type: enums.StartTriggerType

    Specifies whether you want the Start trigger to be a Digital Edge, or Software trigger. You can also choose None as the value for this attribute.
    '''
    streaming_space_available_in_waveform = attributes.AttributeViInt32(1150325)
    '''Type: int

    Indicates the space available (in samples) in the streaming waveform for writing new data. During generation, this available space may be in multiple locations with, for example, part of the available space at the end of the streaming waveform and the rest at the beginning. In this situation, writing a block of waveform data the size of the  total space available in the streaming waveform causes NI-FGEN to return an error, as  NI-FGEN will not wrap the data from the end of the waveform to the beginning and cannot write data past the end of the waveform buffer.
    To avoid writing data past the end of the waveform, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform.
    Used in conjunction with the NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE or NIFGEN_ATTR_STREAMING_WAVEFORM_NAME attributes.
    '''
    streaming_waveform_handle = attributes.AttributeViInt32(1150324)
    '''Type: int

    Specifies the waveform handle of the waveform used to continuously stream data during generation. This attribute defaults to -1 when no streaming waveform is specified.
    Used in conjunction with NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM.
    '''
    streaming_waveform_name = attributes.AttributeViString(1150326)
    '''Type: str

    Specifies the name of the waveform used to continuously stream data during generation. This attribute defaults to // when no streaming waveform is specified.
    Use in conjunction with NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM.
    '''
    streaming_write_timeout = attributes.AttributeViReal64(1150409)
    '''Type: float

    Specifies the maximum amount of time allowed to complete a streaming write operation.
    '''
    supported_instrument_models = attributes.AttributeViString(1050327)
    '''Type: str

    Returns a model code of the device. For NI-FGEN versions that support more than one device, this  attribute contains a comma-separated list of supported device  models.
    '''
    synchronization = attributes.AttributeEnum(attributes.AttributeViInt32, enums.SynchronizationSource, 1150111)
    '''Type: enums.SynchronizationSource

    Specify the source of the synchronization signal that you want to use.
    '''
    sync_duty_cycle_high = attributes.AttributeViReal64(1150105)
    '''Type: float

    Controls the duty cycle of the square wave the signal generator  produces on the SYNC out line.  Specify this attribute as a  percentage of the time the square wave is high in each cycle.
    Units: Percentage of time the waveform is high
    '''
    sync_out_output_terminal = attributes.AttributeViString(1150330)
    '''Type: str

    Specifies the terminal to which to export the SYNC OUT signal. This attribute is not supported for all devices.
    '''
    terminal_configuration = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TerminalConfiguration, 1150365)
    '''Type: enums.TerminalConfiguration

    Specifies whether gain and offset values will be analyzed based on single-ended or differential operation.
    '''
    trigger_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerMode, 1150108)
    '''Type: enums.TriggerMode

    Controls the trigger mode.
    '''
    trigger_source = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerSource, 1250302)
    '''Type: enums.TriggerSource

    Controls which trigger source the signal generator uses.
    After you call the niFgen_InitiateGeneration function, the signal generator waits for the trigger that you specify in the triggerSource parameter. After the signal generator receives a trigger, it produces the number of cycles that you specify in the NIFGEN_ATTR_CYCLE_COUNT attribute.
    This attribute is also the source for the trigger in the other trigger modes as specified by the NIFGEN_ATTR_TRIGGER_MODE attribute.
    '''
    video_waveform_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.VideoWaveformType, 1150216)
    '''Type: enums.VideoWaveformType

    Selects which waveform type that the NI 5431 generates. Setting this attribute ensures that the crystal is set to the proper frequency.
    '''
    wait_behavior = attributes.AttributeEnum(attributes.AttributeViInt32, enums.WaitBehavior, 1150379)
    '''Type: enums.WaitBehavior

    Specifies the behavior of the output while waiting for a script trigger or during a wait instruction.  The output can be configured to hold the last generated voltage before waiting or jump to the Wait Value.
    '''
    wait_value = attributes.AttributeViInt32(1150380)
    '''Type: int

    Specifies the value to generate while waiting.  The Wait Behavior must be configured to jump to this value.
    '''
    waveform_quantum = attributes.AttributeViInt32(1250206)
    '''Type: int

    The size of each arbitrary waveform must be a multiple of a quantum value. This attribute returns the quantum value that the signal generator allows.
    For example, when this attribute returns a value of 8, all waveform sizes must be a multiple of 8. Typically, this value is constant for the signal generator.
    '''

    def __init__(self, repeated_capability, vi=None, library=None, encoding=None, freeze_it=False):
        self._repeated_capability = repeated_capability
        self._vi = vi
        self._library = library
        self._encoding = encoding
        self._param_list = "repeated_capability=" + pp.pformat(repeated_capability)
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

    def allocate_named_waveform(self, waveform_name, waveform_size):
        '''allocate_named_waveform

        Specifies the size of a named waveform up front so that it can be
        allocated in onboard memory before loading the associated data. Data can
        then be loaded in smaller blocks with the niFgen Write (Binary16)
        Waveform functions.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].allocate_named_waveform(waveform_name, waveform_size)

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            waveform_size (int): Specifies the size of the waveform to allocate in samples.

                **Default Value**: "4096"

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_size_ctype = visatype.ViInt32(waveform_size)  # case S150
        error_code = self._library.niFgen_AllocateNamedWaveform(vi_ctype, channel_name_ctype, waveform_name_ctype, waveform_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def allocate_waveform(self, waveform_size):
        '''allocate_waveform

        Specifies the size of a waveform so that it can be allocated in onboard
        memory before loading the associated data. Data can then be loaded in
        smaller blocks with the Write Binary 16 Waveform functions.

        Note:
        The signal generator must not be in the Generating state when you call
        this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].allocate_waveform(waveform_size)

        Args:
            waveform_size (int): Specifies, in samples, the size of the waveform to allocate.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_size_ctype = visatype.ViInt32(waveform_size)  # case S150
        waveform_handle_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_AllocateWaveform(vi_ctype, channel_name_ctype, waveform_size_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def clear_user_standard_waveform(self):
        '''clear_user_standard_waveform

        Clears the user-defined waveform created by the
        nifgen_DefineUserStandardWaveform function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].clear_user_standard_waveform()
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        error_code = self._library.niFgen_ClearUserStandardWaveform(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_arb_sequence(self, sequence_handle, gain, offset):
        '''configure_arb_sequence

        Configures the signal generator attributes that affect arbitrary
        sequence generation. Sets the arb_sequence_handle,
        arb_gain, and arb_offset attributes.

        Note:
        The signal generator must not be in the Generating state when you call
        this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].configure_arb_sequence(sequence_handle, gain, offset)

        Args:
            sequence_handle (int): Specifies the handle of the arbitrary sequence that you want the signal
                generator to produce. NI-FGEN sets the
                arb_sequence_handle attribute to this value. You can
                create an arbitrary sequence using the create_arb_sequence or
                create_advanced_arb_sequence function. These functions return a
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
                arb_offset attribute to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        sequence_handle_ctype = visatype.ViInt32(sequence_handle)  # case S150
        gain_ctype = visatype.ViReal64(gain)  # case S150
        offset_ctype = visatype.ViReal64(offset)  # case S150
        error_code = self._library.niFgen_ConfigureArbSequence(vi_ctype, channel_name_ctype, sequence_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_arb_waveform(self, waveform_handle, gain, offset):
        '''configure_arb_waveform

        Configures the attributes of the signal generator that affect arbitrary
        waveform generation. Sets the arb_waveform_handle,
        arb_gain, and arb_offset attributes.

        Note:
        The signal generator must not be in the Generating state when you call
        this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].configure_arb_waveform(waveform_handle, gain, offset)

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform you want the signal
                generator to produce. NI-FGEN sets the
                arb_waveform_handle attribute to this value. You can
                create an arbitrary waveform using one of the following niFgen Create
                Waveform functions:

                -  _create_waveform_f64
                -  _create_waveform_i16
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64
                -  CreateWaveformFromFileHWS

                These functions return a handle that you use to identify the waveform.

                **Default Value**: None

                Note:
                One or more of the referenced functions are not in the Python API for this driver.

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
                arb_offset attribute to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_handle_ctype = visatype.ViInt32(waveform_handle)  # case S150
        gain_ctype = visatype.ViReal64(gain)  # case S150
        offset_ctype = visatype.ViReal64(offset)  # case S150
        error_code = self._library.niFgen_ConfigureArbWaveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_custom_fir_filter_coefficients(self, coefficients_array):
        '''configure_custom_fir_filter_coefficients

        Sets the FIR filter coefficients used by the onboard signal processing
        block. The values are coerced to the closest settings achievable by the
        signal generator.

        Refer to the *FIR Filter* topic for your device in the *NI Signal
        Generators Help* for more information about FIR filter coefficients.
        This function is supported only for the NI 5441.

        Note:
        The signal generator must not be in the Generating state when you call
        this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].configure_custom_fir_filter_coefficients(coefficients_array)

        Args:
            coefficients_array (list of float): Specifies the array of data the onboard signal processor uses for the
                FIR filter coefficients. For the NI 5441, provide a symmetric array of
                95 coefficients to this parameter. The array must have at least as many
                elements as the value that you specify in the **numberOfCoefficients**
                parameter in this function.
                The coefficients should range between –1.00 and +1.00.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        number_of_coefficients_ctype = visatype.ViInt32(0 if coefficients_array is None else len(coefficients_array))  # case S160
        coefficients_array_ctype = get_ctypes_pointer_for_buffer(value=coefficients_array, library_type=visatype.ViReal64)  # case B550
        error_code = self._library.niFgen_ConfigureCustomFIRFilterCoefficients(vi_ctype, channel_name_ctype, number_of_coefficients_ctype, coefficients_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_freq_list(self, frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0):
        '''configure_freq_list

        Configures the attributes of the signal generator that affect frequency
        list generation (the freq_list_handle,
        func_amplitude, func_dc_offset, and
        func_start_phase attributes).

        Note:
        The signal generator must not be in the Generating state when you call
        this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].configure_freq_list(frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0)

        Args:
            frequency_list_handle (int): Specifies the handle of the frequency list that you want the signal
                generator to produce. NI-FGEN sets the freq_list_handle
                attribute to this value. You can create a frequency list using the
                create_freq_list function, which returns a handle that you use to
                identify the list.
                **Default Value**: None

            amplitude (float): Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the func_amplitude attribute to
                this value.

                For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
                the amplitude to 10.00 V.

                **Units**: peak-to-peak voltage

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                function to Waveform.DC.

            dc_offset (float): Specifies the DC offset of the standard waveform that you want the
                signal generator to produce. The value is the offset from ground to the
                center of the waveform you specify with the **waveform** parameter,
                observed at the output terminal. For example, to configure a waveform
                with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
                **dcOffset** to 5.00 V. NI-FGEN sets the func_dc_offset
                attribute to this value.

                **Units**: volts

                **Default Value**: None

            start_phase (float): Specifies the horizontal offset of the standard waveform you want the
                signal generator to produce. Specify this attribute in degrees of one
                waveform cycle. NI-FGEN sets the func_start_phase
                attribute to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: None degrees

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter to Waveform.DC.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        frequency_list_handle_ctype = visatype.ViInt32(frequency_list_handle)  # case S150
        amplitude_ctype = visatype.ViReal64(amplitude)  # case S150
        dc_offset_ctype = visatype.ViReal64(dc_offset)  # case S150
        start_phase_ctype = visatype.ViReal64(start_phase)  # case S150
        error_code = self._library.niFgen_ConfigureFreqList(vi_ctype, channel_name_ctype, frequency_list_handle_ctype, amplitude_ctype, dc_offset_ctype, start_phase_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_standard_waveform(self, waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0):
        '''configure_standard_waveform

        Configures the following attributes of the signal generator that affect
        standard waveform generation:

        -  func_waveform
        -  func_amplitude
        -  func_dc_offset
        -  func_frequency
        -  func_start_phase

        Note:
        You must call the ConfigureOutputMode function with the
        **outputMode** parameter set to OutputMode.FUNC before calling
        this function.

        Note:
        One or more of the referenced functions are not in the Python API for this driver.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].configure_standard_waveform(waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0)

        Args:
            waveform (enums.Waveform): Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the func_waveform attribute to this
                value.

                ****Defined Values****

                **Default Value**: Waveform.SINE

                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SINE      | Specifies that the signal generator produces a sinusoid waveform.                                                                    |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SQUARE    | Specifies that the signal generator produces a square waveform.                                                                      |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.TRIANGLE  | Specifies that the signal generator produces a triangle waveform.                                                                    |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                               |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                               |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.DC        | Specifies that the signal generator produces a constant voltage.                                                                     |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.NOISE     | Specifies that the signal generator produces white noise.                                                                            |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.USER      | Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform function. |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+

            amplitude (float): Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the func_amplitude attribute to
                this value.

                For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
                the amplitude to 10.00 V.

                **Units**: peak-to-peak voltage

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                function to Waveform.DC.

            frequency (float): | Specifies the frequency of the standard waveform that you want the
                  signal generator to produce. NI-FGEN sets the
                  func_frequency attribute to this value.

                **Units**: hertz

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                function to Waveform.DC.

            dc_offset (float): Specifies the DC offset of the standard waveform that you want the
                signal generator to produce. The value is the offset from ground to the
                center of the waveform you specify with the **waveform** parameter,
                observed at the output terminal. For example, to configure a waveform
                with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
                **dcOffset** to 5.00 V. NI-FGEN sets the func_dc_offset
                attribute to this value.

                **Units**: volts

                **Default Value**: None

            start_phase (float): Specifies the horizontal offset of the standard waveform that you want
                the signal generator to produce. Specify this parameter in degrees of
                one waveform cycle. NI-FGEN sets the func_start_phase
                attribute to this value. A start phase of 180 degrees means output
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
            raise TypeError('Parameter mode must be of type ' + str(enums.Waveform))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_ctype = visatype.ViInt32(waveform.value)  # case S130
        amplitude_ctype = visatype.ViReal64(amplitude)  # case S150
        dc_offset_ctype = visatype.ViReal64(dc_offset)  # case S150
        frequency_ctype = visatype.ViReal64(frequency)  # case S150
        start_phase_ctype = visatype.ViReal64(start_phase)  # case S150
        error_code = self._library.niFgen_ConfigureStandardWaveform(vi_ctype, channel_name_ctype, waveform_ctype, amplitude_ctype, dc_offset_ctype, frequency_ctype, start_phase_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_waveform(self, waveform_data_array):
        '''create_waveform

        Creates an onboard waveform
        for use in Arbitrary Waveform output mode or Arbitrary Sequence output
        mode.

        Note:
        You must set output_mode to OutputMode.ARB or
        OutputMode.SEQ before calling this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].create_waveform(waveform_data_array)

        Args:
            waveform_data_array (list of float): Array of data for the new arbitrary waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used in other methods when referring to this waveform.

        '''
        # Check the type by using string comparison so that we don't import numpy unecessarilly.
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

    def _create_waveform_f64(self, waveform_data_array):
        '''_create_waveform_f64

        Creates an onboard waveform from binary F64 (floating point double) data
        for use in Arbitrary Waveform output mode or Arbitrary Sequence output
        mode. The **waveformHandle** returned can later be used for setting the
        active waveform, changing the data in the waveform, building sequences
        of waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the nifgen_ConfigureOutputMode function to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._create_waveform_f64(waveform_data_array)

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_size_ctype = visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_array = get_ctypes_and_array(value=waveform_data_array, array_type="d")  # case B550
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array_array, library_type=visatype.ViReal64)  # case B550
        waveform_handle_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_CreateWaveformF64(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def _create_waveform_f64_numpy(self, waveform_data_array):
        '''_create_waveform_f64

        Creates an onboard waveform from binary F64 (floating point double) data
        for use in Arbitrary Waveform output mode or Arbitrary Sequence output
        mode. The **waveformHandle** returned can later be used for setting the
        active waveform, changing the data in the waveform, building sequences
        of waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the nifgen_ConfigureOutputMode function to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._create_waveform_f64(waveform_data_array)

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_size_ctype = visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array)  # case B510
        waveform_handle_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_CreateWaveformF64(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_waveform_from_file_f64(self, file_name, byte_order):
        '''create_waveform_from_file_f64

        This function takes the floating point double (F64) data from the
        specified file and creates an onboard waveform for use in Arbitrary
        Waveform or Arbitrary Sequence output mode. The **waveformHandle**
        returned by this function can later be used for setting the active
        waveform, changing the data in the waveform, building sequences of
        waveforms, or deleting the waveform when it is no longer needed.

        Note:
        The F64 data must be between –1.0 and +1.0 V. Use the
        digital_gain attribute to generate different voltage
        outputs.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].create_waveform_from_file_f64(file_name, byte_order)

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
            raise TypeError('Parameter mode must be of type ' + str(enums.ByteOrder))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(self._encoding))  # case C020
        byte_order_ctype = visatype.ViInt32(byte_order.value)  # case S130
        waveform_handle_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_CreateWaveformFromFileF64(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_waveform_from_file_i16(self, file_name, byte_order):
        '''create_waveform_from_file_i16

        Takes the binary 16-bit signed integer (I16) data from the specified
        file and creates an onboard waveform for use in Arbitrary Waveform or
        Arbitrary Sequence output mode. The **waveformHandle** returned by this
        function can later be used for setting the active waveform, changing the
        data in the waveform, building sequences of waveforms, or deleting the
        waveform when it is no longer needed.

        Note:
        The I16 data (values between –32768 and +32767) is assumed to
        represent –1 to +1 V. Use the digital_gain attribute to
        generate different voltage outputs.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].create_waveform_from_file_i16(file_name, byte_order)

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
            raise TypeError('Parameter mode must be of type ' + str(enums.ByteOrder))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(self._encoding))  # case C020
        byte_order_ctype = visatype.ViInt32(byte_order.value)  # case S130
        waveform_handle_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_CreateWaveformFromFileI16(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def _create_waveform_i16_numpy(self, waveform_data_array):
        '''_create_waveform_i16

        Creates an onboard waveform from binary 16-bit signed integer (I16) data
        for use in Arbitrary Waveform or Arbitrary Sequence output mode. The
        **waveformHandle** returned can later be used for setting the active
        waveform, changing the data in the waveform, building sequences of
        waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the nifgen_ConfigureOutputMode function to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._create_waveform_i16(waveform_data_array)

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_size_ctype = visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array)  # case B510
        waveform_handle_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_CreateWaveformI16(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def define_user_standard_waveform(self, waveform_data_array):
        '''define_user_standard_waveform

        Defines a user waveform for use in either Standard Function or Frequency
        List output mode.

        To select the waveform, set the **waveform** parameter to
        Waveform.USER with either the nifgen_ConfigureStandardWaveform
        or the nifgen_CreateFreqList function.

        The waveform data must be scaled between –1.0 and 1.0. Use the
        **amplitude** parameter in the configure_standard_waveform
        function to generate different output voltages.

        Note:
        You must call the nifgen_ConfigureOutputMode function to set the
        **outputMode** parameter to OutputMode.FUNC or
        OutputMode.FREQ_LIST before calling this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].define_user_standard_waveform(waveform_data_array)

        Args:
            waveform_data_array (list of float): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_size_ctype = visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=visatype.ViReal64)  # case B550
        error_code = self._library.niFgen_DefineUserStandardWaveform(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_named_waveform(self, waveform_name):
        '''delete_named_waveform

        Removes a previously created arbitrary waveform from the signal
        generator memory and invalidates the waveform handle.

        Note:
        The signal generator must not be in the Generating state when you call
        this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].delete_named_waveform(waveform_name)

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_DeleteNamedWaveform(vi_ctype, channel_name_ctype, waveform_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_script(self, script_name):
        '''delete_script

        Deletes the specified script from onboard memory.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].delete_script(script_name)

        Args:
            script_name (str): Specifies the name of the script you want to delete. The script name
                appears in the text of the script following the script keyword.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        script_name_ctype = ctypes.create_string_buffer(script_name.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_DeleteScript(vi_ctype, channel_name_ctype, script_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _get_attribute_vi_boolean(self, attribute_id):
        '''_get_attribute_vi_boolean

        Queries the value of a ViBoolean attribute.

        You can use this function to get the values of instrument-specific
        attributes and inherent IVI attributes. If the attribute represents an
        instrument state, this function performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_boolean(attribute_id)

        Args:
            attribute_id (int): Specifies the ID of an attribute.


        Returns:
            attribute_value (bool): Returns the current value of the attribute. Pass the address of a
                ViBoolean variable.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViBoolean()  # case S200
        error_code = self._library.niFgen_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

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
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_int32(attribute_id)

        Args:
            attribute_id (int): Specifies the ID of an attribute.


        Returns:
            attribute_value (int): Returns the current value of the attribute. Pass the address of a
                ViInt32 variable.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, attribute_id):
        '''_get_attribute_vi_real64

        Queries the value of a ViReal64 attribute.

        You can use this function to get the values of instrument-specific
        attributes and inherent IVI attributes. If the attribute represents an
        instrument state, this function performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_real64(attribute_id)

        Args:
            attribute_id (int): Specifies the ID of an attribute.


        Returns:
            attribute_value (float): Returns the current value of the attribute. Pass the address of a
                ViReal64 variable.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViReal64()  # case S200
        error_code = self._library.niFgen_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, attribute_id):
        '''_get_attribute_vi_string

        Queries the value of a ViString attribute.

        You can use this function to get the values of instrument-specific
        attributes and inherent IVI attributes. If the attribute represents an
        instrument state, this function performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid.

        You must provide a ViChar array to serve as a buffer for the value. You
        pass the number of bytes in the buffer as the **arraySize** parameter.
        If the current value of the attribute, including the terminating NUL
        byte, is larger than the size you indicate in the **arraySize**
        parameter, the function copies **arraySize** – 1 bytes into the buffer,
        places an ASCII NUL byte at the end of the buffer, and returns the array
        size you must pass to get the entire value. For example, if the value is
        123456 and **arraySize** is 4, the function places 123 into the buffer
        and returns 7.

        If you want to call this function just to get the required array size,
        you can pass 0 for **arraySize** and VI_NULL for the **attributeValue**
        buffer.

        If you want the function to fill in the buffer regardless of the number
        of bytes in the value, pass a negative number for the **arraySize**
        parameter.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_string(attribute_id)

        Args:
            attribute_id (int): Specifies the ID of an attribute.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        array_size_ctype = visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niFgen_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (visatype.ViChar * array_size_ctype.value)()  # case C060
        error_code = self._library.niFgen_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def _get_error(self):
        '''_get_error

        Returns the error information associated with an IVI session or with the
        current execution thread. If you specify a valid IVI session for the
        **vi** parameter, this function retrieves and then clears the error
        information for the session. If you pass VI_NULL for the **vi**
        parameter, this function retrieves and then clears the error information
        for the current execution thread.

        The IVI Engine also maintains this error information separately for each
        thread. This feature is useful if you do not have a session handle to
        pass to the _get_error or nifgen_ClearError functions. This
        situation occurs when a call to the nifgen_init or
        nifgen_InitWithOptions function fails.

        Returns:
            error_code (int): The error code for the session or execution thread.

                A value of VI_SUCCESS (0) indicates that no error occurred. A positive
                value indicates a warning. A negative value indicates an error.

                You can call nifgen_error_message to get a text description of the
                value.

                If you are not interested in this value, you can pass VI_NULL.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code_ctype = visatype.ViStatus()  # case S200
        error_description_buffer_size_ctype = visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library.niFgen_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFgen_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def get_fir_filter_coefficients(self):
        '''get_fir_filter_coefficients

        | Returns the FIR filter coefficients used by the onboard signal
          processing block. These coefficients are determined by NI-FGEN and
          based on the FIR filter type and corresponding attribute (Alpha,
          Passband, BT) unless you are using the custom filter. If you are using
          a custom filter, the coefficients returned are those set with the
          nifgen_ConfigureCustomFIRFilterCoefficients function coerced to the
          quantized values used by the device.
        | To use this function, first call an instance of the
          get_fir_filter_coefficients function with the
          **coefficientsArray** parameter set to VI_NULL. Calling the function
          in this state returns the current size of the **coefficientsArray** as
          the value of the **numberOfCoefficientsRead** parameter. Create an
          array of this size, and call the get_fir_filter_coefficients
          function a second time, passing the new array as the
          **coefficientsArray** parameter and the size as the **arraySize**
          parameter. This second function call populates the array with the FIR
          filter coefficients.
        | Refer to the FIR Filter topic for your device in the *NI Signal
          Generators Help* for more information about FIR filter coefficients.
          This function is supported only for the NI 5441.
        | **Default Value**: None

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].get_fir_filter_coefficients()

        Returns:
            number_of_coefficients_read (int): Specifies the array of data containing the number of coefficients you
                want to read.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        array_size_ctype = visatype.ViInt32()  # case S170
        coefficients_array_ctype = None  # case B580
        number_of_coefficients_read_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_GetFIRFilterCoefficients(vi_ctype, channel_name_ctype, array_size_ctype, coefficients_array_ctype, None if number_of_coefficients_read_ctype is None else (ctypes.pointer(number_of_coefficients_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = visatype.ViInt32(error_code)  # case S180
        coefficients_array_size = array_size_ctype.value  # case B590
        coefficients_array_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViReal64, size=coefficients_array_size)  # case B590
        error_code = self._library.niFgen_GetFIRFilterCoefficients(vi_ctype, channel_name_ctype, array_size_ctype, coefficients_array_ctype, None if number_of_coefficients_read_ctype is None else (ctypes.pointer(number_of_coefficients_read_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(coefficients_array_ctype[i]) for i in range(array_size_ctype.value)], int(number_of_coefficients_read_ctype.value)

    def _initialize_with_channels(self, resource_name, reset_device=False, option_string=""):
        '''_initialize_with_channels

        Creates and returns a new NI-FGEN session to the specified channel of a
        waveform generator that is used in all subsequent NI-FGEN function
        calls.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._initialize_with_channels(resource_name, reset_device=False, option_string='""')

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

            reset_device (bool): Specifies whether you want to reset the device during the initialization
                procedure. VI_TRUE specifies that the device is reset and performs the
                same function as the nifgen_Reset function.

                ****Defined Values****

                **Default Value**: VI_FALSE

                +----------+---------------------+
                | VI_TRUE  | Reset device        |
                +----------+---------------------+
                | VI_FALSE | Do not reset device |
                +----------+---------------------+

            option_string (str): Sets the initial value of certain session attributes.

                The syntax for **optionString** is

                <*attributeName*> = <*value*>

                where

                *attributeName* is the name of the attribute and *value* is the value to
                which the attribute is set

                To set multiple attributes, separate them with a comma.

                If you pass NULL or an empty string for this parameter, the session uses
                the default values for these attributes. You can override the default
                values by assigning a value explicitly in a string that you pass for
                this parameter.

                You do not have to specify all of the attributes and may leave any of
                them out. However, if you do not specify one of the attributes, its
                default value is used.

                If simulation is enabled (Simulate=1), you may specify the device that
                you want to simulate. To specify a device, enter the following syntax in
                **optionString**.

                DriverSetup=Model:<*driver model number*>;Channels:<*channel
                names*>;BoardType:<*module type*>;MemorySize:<*size of onboard memory in
                bytes*>

                **Syntax Examples**

                **Attributes and **Defined Values****

                **Default Values**: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"

                +------------------+-------------------------+-------------------+
                | Attribute Name   | Attribute               | Values            |
                +==================+=========================+===================+
                | RangeCheck       | range_check             | VI_TRUE, VI_FALSE |
                +------------------+-------------------------+-------------------+
                | QueryInstrStatus | query_instrument_status | VI_TRUE, VI_FALSE |
                +------------------+-------------------------+-------------------+
                | Cache            | cache                   | VI_TRUE, VI_FALSE |
                +------------------+-------------------------+-------------------+
                | Simulate         | simulate                | VI_TRUE, VI_FALSE |
                +------------------+-------------------------+-------------------+


        Returns:
            vi (int): Returns a session handle that you can use to identify the device in all
                subsequent NI-FGEN function calls.

        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        reset_device_ctype = visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = visatype.ViSession()  # case S200
        error_code = self._library.niFgen_InitializeWithChannels(resource_name_ctype, channel_name_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        '''_set_attribute_vi_boolean

        Sets the value of a ViBoolean attribute.

        This is a low-level function that you can use to set the values of
        instrument-specific attributes and inherent IVI attributes. If the
        attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level functions that set most of the instrument
        attributes. NI recommends that you use the high-level driver functions
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the attributes. In contrast, when you set multiple
        attributes using the Set Attribute functions, the functions check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level functions that
        configure multiple attributes perform instrument I/O only for the
        attributes whose value you change. Thus, you can safely call the
        high-level functions without the penalty of redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_boolean(attribute_id, attribute_value)

        Args:
            attribute_id (int): Specifies the ID of an attribute.

            attribute_value (bool): Specifies the value to which you want to set the attribute. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niFgen_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        '''_set_attribute_vi_int32

        Sets the value of a ViInt32 attribute.

        This is a low-level function that you can use to set the values of
        instrument-specific attributes and inherent IVI attributes. If the
        attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level functions that set most of the instrument
        attributes. NI recommends that you use the high-level driver functions
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the attributes. In contrast, when you set multiple
        attributes using the Set Attribute functions, the functions check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level functions that
        configure multiple attributes perform instrument I/O only for the
        attributes whose value you change. Thus, you can safely call the
        high-level functions without the penalty of redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_int32(attribute_id, attribute_value)

        Args:
            attribute_id (int): Specifies the ID of an attribute.

            attribute_value (int): Specifies the value to which you want to set the attribute. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niFgen_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        '''_set_attribute_vi_real64

        Sets the value of a ViReal64 attribute.

        This is a low-level function that you can use to set the values of
        instrument-specific attributes and inherent IVI attributes. If the
        attribute represents an instrument state, this function performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular attribute.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level functions that set most of the instrument
        attributes. NI recommends that you use the high-level driver functions
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the attributes. In contrast, when you set multiple
        attributes using the Set Attribute functions, the functions check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level functions that
        configure multiple attributes perform instrument I/O only for the
        attributes whose value you change. Thus, you can safely call the
        high-level functions without the penalty of redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_real64(attribute_id, attribute_value)

        Args:
            attribute_id (int): Specifies the ID of an attribute.

            attribute_value (float): Specifies the value to which you want to set the attribute. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niFgen_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, attribute_id, attribute_value):
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

        NI-FGEN contains high-level functions that set most of the instrument
        attributes. NI recommends that you use the high-level driver functions
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the attributes. In contrast, when you set multiple
        attributes using the Set Attribute functions, the functions check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level functions that
        configure multiple attributes perform instrument I/O only for the
        attributes whose value you change. Thus, you can safely call the
        high-level functions without the penalty of redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_string(attribute_id, attribute_value)

        Args:
            attribute_id (int): Specifies the ID of an attribute.

            attribute_value (str): Specifies the value to which you want to set the attribute. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_named_waveform_next_write_position(self, waveform_name, relative_to, offset):
        '''set_named_waveform_next_write_position

        Sets the position in the waveform to which data is written at the next
        write. This function allows you to write to arbitrary locations within
        the waveform. These settings apply only to the next write to the
        waveform specified by the **waveformHandle** parameter. Subsequent
        writes to that waveform begin where the last write left off, unless this
        function is called again. The **waveformHandle** passed in must have
        been created with a call to one of the following functions:

        -  nifgen_AllocateWaveform
        -  nifgen_CreateWaveformF64
        -  nifgen_CreateWaveformI16
        -  nifgen_CreateWaveformFromFileI16
        -  nifgen_CreateWaveformFromFileF64
        -  nifgen_CreateWaveformFromFileHWS

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].set_named_waveform_next_write_position(waveform_name, relative_to, offset)

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
            raise TypeError('Parameter mode must be of type ' + str(enums.RelativeTo))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        relative_to_ctype = visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = visatype.ViInt32(offset)  # case S150
        error_code = self._library.niFgen_SetNamedWaveformNextWritePosition(vi_ctype, channel_name_ctype, waveform_name_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_waveform_next_write_position(self, waveform_handle, relative_to, offset):
        '''set_waveform_next_write_position

        Sets the position in the waveform at which the next waveform data is
        written. This function allows you to write to arbitrary locations within
        the waveform. These settings apply only to the next write to the
        waveform specified by the waveformHandle parameter. Subsequent writes to
        that waveform begin where the last write left off, unless this function
        is called again. The waveformHandle passed in must have been created by
        a call to the nifgen_AllocateWaveform function or one of the following
        niFgen CreateWaveform functions:

        -  nifgen_CreateWaveformF64
        -  nifgen_CreateWaveformI16
        -  nifgen_CreateWaveformFromFileI16
        -  nifgen_CreateWaveformFromFileF64
        -  nifgen_CreateWaveformFromFileHWS

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].set_waveform_next_write_position(waveform_handle, relative_to, offset)

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the nifgen_AllocateWaveform function.

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
            raise TypeError('Parameter mode must be of type ' + str(enums.RelativeTo))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_handle_ctype = visatype.ViInt32(waveform_handle)  # case S150
        relative_to_ctype = visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = visatype.ViInt32(offset)  # case S150
        error_code = self._library.niFgen_SetWaveformNextWritePosition(vi_ctype, channel_name_ctype, waveform_handle_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_binary16_waveform_numpy(self, waveform_handle, data):
        '''_write_binary16_waveform

        Writes binary data to the waveform in onboard memory. The waveform
        handle passed must have been created by a call to the
        nifgen_AllocateWaveform or the nifgen_CreateWaveformI16 function.

        By default, the subsequent call to the _write_binary16_waveform
        function continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        nifgen_SetWaveformNextWritePosition function. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._write_binary16_waveform(waveform_handle, data)

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the nifgen_AllocateWaveform function.

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_handle_ctype = visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteBinary16Waveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_named_waveform_f64(self, waveform_name, data):
        '''_write_named_waveform_f64

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        nifgen_AllocateWaveform function or to one of the following niFgen
        Create Waveform functions:

        -  nifgen_CreateWaveformF64
        -  nifgen_CreateWaveformI16
        -  nifgen_CreateWaveformFromFileI16
        -  nifgen_CreateWaveformFromFileF64
        -  nifgen_CreateWaveformFromFileHWS

        By default, the subsequent call to the _write_named_waveform_f64
        function continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        nifgen_SetNamedWaveformNextWritePosition function. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._write_named_waveform_f64(waveform_name, data)

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            data (array.array("d")): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_array = get_ctypes_and_array(value=data, array_type="d")  # case B550
        data_ctype = get_ctypes_pointer_for_buffer(value=data_array, library_type=visatype.ViReal64)  # case B550
        error_code = self._library.niFgen_WriteNamedWaveformF64(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_named_waveform_f64_numpy(self, waveform_name, data):
        '''_write_named_waveform_f64

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        nifgen_AllocateWaveform function or to one of the following niFgen
        Create Waveform functions:

        -  nifgen_CreateWaveformF64
        -  nifgen_CreateWaveformI16
        -  nifgen_CreateWaveformFromFileI16
        -  nifgen_CreateWaveformFromFileF64
        -  nifgen_CreateWaveformFromFileHWS

        By default, the subsequent call to the _write_named_waveform_f64
        function continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        nifgen_SetNamedWaveformNextWritePosition function. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._write_named_waveform_f64(waveform_name, data)

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteNamedWaveformF64(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_named_waveform_i16_numpy(self, waveform_name, data):
        '''_write_named_waveform_i16

        Writes binary data to the named waveform in onboard memory.

        By default, the subsequent call to the _write_named_waveform_i16
        function continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        nifgen_SetNamedWaveformNextWritePosition function. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._write_named_waveform_i16(waveform_name, data)

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteNamedWaveformI16(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_script(self, script):
        '''write_script

        Writes a string containing one or more scripts that govern the
        generation of waveforms.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].write_script(script)

        Args:
            script (str): Contains the text of the script you want to use for your generation
                operation. Refer to `scripting
                Instructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__
                for more information about writing scripts.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        script_ctype = ctypes.create_string_buffer(script.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_WriteScript(vi_ctype, channel_name_ctype, script_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_waveform(self, waveform_handle, data):
        '''_write_waveform

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        nifgen_AllocateWaveform function or one of the following niFgen
        CreateWaveform functions:

        -  nifgen_CreateWaveformF64
        -  nifgen_CreateWaveformI16
        -  nifgen_CreateWaveformFromFileI16
        -  nifgen_CreateWaveformFromFileF64
        -  nifgen_CreateWaveformFromFileHWS

        By default, the subsequent call to the _write_waveform function
        continues writing data from the position of the last sample written. You
        can set the write position and offset by calling the
        nifgen_SetWaveformNextWritePosition function. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._write_waveform(waveform_handle, data)

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the nifgen_AllocateWaveform function.

            data (array.array("d")): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_handle_ctype = visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_array = get_ctypes_and_array(value=data, array_type="d")  # case B550
        data_ctype = get_ctypes_pointer_for_buffer(value=data_array, library_type=visatype.ViReal64)  # case B550
        error_code = self._library.niFgen_WriteWaveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _write_waveform_numpy(self, waveform_handle, data):
        '''_write_waveform

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        nifgen_AllocateWaveform function or one of the following niFgen
        CreateWaveform functions:

        -  nifgen_CreateWaveformF64
        -  nifgen_CreateWaveformI16
        -  nifgen_CreateWaveformFromFileI16
        -  nifgen_CreateWaveformFromFileF64
        -  nifgen_CreateWaveformFromFileHWS

        By default, the subsequent call to the _write_waveform function
        continues writing data from the position of the last sample written. You
        can set the write position and offset by calling the
        nifgen_SetWaveformNextWritePosition function. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._write_waveform(waveform_handle, data)

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the nifgen_AllocateWaveform function.

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case C010
        waveform_handle_ctype = visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteWaveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_waveform(self, waveform_name_or_handle, data):
        '''write_waveform

        Writes data to the waveform in onboard memory.

        By default, subsequent calls to this function
        continue writing data from the position of the last sample written. You
        can set the write position and offset by calling the nifgen_SetNamedWaveformNextWritePosition
        nifgen_SetWaveformNextWritePosition function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].write_waveform(waveform_name_or_handle, data)

        Args:
            waveform_name_or_handle (int): The name (str) or handle (int) of an arbitrary waveform previously allocated with allocate_named_waveform or allocate_waveform.

            data (list of float): Array of data to load into the waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.

        '''
        use_named = isinstance(waveform_name_or_handle, str)
        # Check the type by using string comparison so that we don't import numpy unecessarilly.
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
        '''_error_message

        Converts a status code returned by an NI-FGEN function into a
        user-readable string.

        Args:
            error_code (int): Specifies the **status** parameter that is returned from any of the
                NI-FGEN functions.

                **Default Value**: 0 (VI_SUCCESS)


        Returns:
            error_message (str): Returns the error message string read from the instrument error message
                queue.

                You must pass a ViChar array with at least 256 bytes.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code_ctype = visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFgen_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class Session(_SessionBase):
    '''An NI-FGEN session to a National Instruments Signal Generator.'''

    def __init__(self, resource_name, reset_device=False, option_string=""):
        super(Session, self).__init__(repeated_capability='')
        self._library = library_singleton.get()
        self._encoding = 'windows-1251'
        self._vi = 0  # This must be set before calling _initialize_with_channels().
        self._vi = self._initialize_with_channels(resource_name, reset_device, option_string)
        self.channels = _Channels(self._vi, self._library, self._encoding)
        self.p2p_streams = _P2PStreams(self._vi, self._library, self._encoding)
        self.script_triggers = _ScriptTriggers(self._vi, self._library, self._encoding)
        self.markers = _Markers(self._vi, self._library, self._encoding)
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        param_list.append("option_string=" + pp.pformat(option_string))
        self._param_list = ', '.join(param_list)
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def initiate(self):
        return _Generation(self)

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

        Aborts any previously initiated signal generation. Call the
        nifgen_InitiateGeneration function to cause the signal generator to
        produce a signal again.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_AbortGeneration(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_arb_memory(self):
        '''clear_arb_memory

        Removes all previously created arbitrary waveforms, sequences, and
        scripts from the signal generator memory and invalidates all waveform
        handles, sequence handles, and waveform names.

        Note:
        The signal generator must not be in the Generating state when you
        call this function.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_ClearArbMemory(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_arb_sequence(self, sequence_handle):
        '''clear_arb_sequence

        Removes a previously created arbitrary sequence from the signal
        generator memory and invalidates the sequence handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this function.

        Args:
            sequence_handle (int): Specifies the handle of the arbitrary sequence that you want the signal
                generator to remove. You can create an arbitrary sequence using the
                nifgen_CreateArbSequence or nifgen_CreateAdvancedArbSequence function.
                These functions return a handle that you use to identify the sequence.

                | **Defined Value**:
                | NIFGEN_VAL_ALL_SEQUENCES—Remove all sequences from the signal
                  generator

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        sequence_handle_ctype = visatype.ViInt32(sequence_handle)  # case S150
        error_code = self._library.niFgen_ClearArbSequence(vi_ctype, sequence_handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_arb_waveform(self, waveform_handle):
        '''clear_arb_waveform

        Removes a previously created arbitrary waveform from the signal
        generator memory and invalidates the waveform handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this function.

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform that you want the signal
                generator to remove.

                You can create multiple arbitrary waveforms using one of the following
                niFgen Create Waveform functions:

                -  _create_waveform_f64
                -  _create_waveform_i16
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64
                -  CreateWaveformFromFileHWS

                **Defined Value**:

                NIFGEN_VAL_ALL_WAVEFORMS—Remove all waveforms from the signal
                generator.

                **Default Value**: None

                Note:
                One or more of the referenced functions are not in the Python API for this driver.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        waveform_handle_ctype = visatype.ViInt32(waveform_handle)  # case S150
        error_code = self._library.niFgen_ClearArbWaveform(vi_ctype, waveform_handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_freq_list(self, frequency_list_handle):
        '''clear_freq_list

        Removes a previously created frequency list from the signal generator
        memory and invalidates the frequency list handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this function.

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        frequency_list_handle_ctype = visatype.ViInt32(frequency_list_handle)  # case S150
        error_code = self._library.niFgen_ClearFreqList(vi_ctype, frequency_list_handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self):
        '''commit

        Causes a transition to the Committed state. This function verifies
        attribute values, reserves the device, and commits the attribute values
        to the device. If the attribute values are all valid, NI-FGEN sets the
        device hardware configuration to match the session configuration. This
        function does not support the NI 5401/5404/5411/5431 signal generators.

        In the Committed state, you can load waveforms, scripts, and sequences
        into memory. If any attributes are changed, NI-FGEN implicitly
        transitions back to the Idle state, where you can program all session
        properties before applying them to the device. This function has no
        effect if the device is already in the Committed or Generating state and
        returns a successful status value.

        Calling this VI before the niFgen Initiate Generation VI is optional but
        has the following benefits:

        -  Routes are committed, so signals are exported or imported.
        -  Any Reference Clock and external clock circuits are phase-locked.
        -  A subsequent _initiate_generation function can run faster
           because the device is already configured.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_script_trigger(self, trigger_id, source, edge=enums.ScriptTriggerDigitalEdgeEdge.RISING):
        '''configure_digital_edge_script_trigger

        Configures the specified Script Trigger for digital edge triggering.

        Args:
            trigger_id (str): Specifies the Script Trigger used for triggering.

                **Defined Values**

                **Default Value**: "ScriptTrigger0"

                +------------------+------------------+
                | "ScriptTrigger0" | Script Trigger 0 |
                +------------------+------------------+
                | "ScriptTrigger1" | Script Trigger 1 |
                +------------------+------------------+
                | "ScriptTrigger2" | Script Trigger 2 |
                +------------------+------------------+
                | "ScriptTrigger3" | Script Trigger 3 |
                +------------------+------------------+

            source (str): Specifies which trigger source the signal generator uses.

                **Defined Values**

                **Default Value**: "PFI0"

                +-------------+-----------------------------------+
                | "PFI0"      | PFI 0                             |
                +-------------+-----------------------------------+
                | "PFI1"      | PFI 1                             |
                +-------------+-----------------------------------+
                | "PFI2"      | PFI 2                             |
                +-------------+-----------------------------------+
                | "PFI3"      | PFI 3                             |
                +-------------+-----------------------------------+
                | "PFI4"      | PFI 4                             |
                +-------------+-----------------------------------+
                | "PFI5"      | PFI 5                             |
                +-------------+-----------------------------------+
                | "PFI6"      | PFI 6                             |
                +-------------+-----------------------------------+
                | "PFI7"      | PFI 7                             |
                +-------------+-----------------------------------+
                | "PXI_Trig0" | PXI trigger line 0 or RTSI line 0 |
                +-------------+-----------------------------------+
                | "PXI_Trig1" | PXI trigger line 1 or RTSI line 1 |
                +-------------+-----------------------------------+
                | "PXI_Trig2" | PXI trigger line 2 or RTSI line 2 |
                +-------------+-----------------------------------+
                | "PXI_Trig3" | PXI trigger line 3 or RTSI line 3 |
                +-------------+-----------------------------------+
                | "PXI_Trig4" | PXI trigger line 4 or RTSI line 4 |
                +-------------+-----------------------------------+
                | "PXI_Trig5" | PXI trigger line 5 or RTSI line 5 |
                +-------------+-----------------------------------+
                | "PXI_Trig6" | PXI trigger line 6 or RTSI line 6 |
                +-------------+-----------------------------------+
                | "PXI_Trig7" | PXI trigger line 7 or RTSI line 7 |
                +-------------+-----------------------------------+
                | "PXI_Star"  | PXI star trigger line             |
                +-------------+-----------------------------------+

            edge (enums.ScriptTriggerDigitalEdgeEdge): Specifies the edge to detect.

                ****Defined Values****

                ****Default Value**:** ScriptTriggerDigitalEdgeEdge.RISING

                +--------------------------------------+------------------------------------------------------------------+
                | ScriptTriggerDigitalEdgeEdge.RISING  | Occurs when the signal transitions from low level to high level. |
                +--------------------------------------+------------------------------------------------------------------+
                | ScriptTriggerDigitalEdgeEdge.FALLING | Occurs when the signal transitions from high level to low level. |
                +--------------------------------------+------------------------------------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(edge) is not enums.ScriptTriggerDigitalEdgeEdge:
            raise TypeError('Parameter mode must be of type ' + str(enums.ScriptTriggerDigitalEdgeEdge))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C020
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = visatype.ViInt32(edge.value)  # case S130
        error_code = self._library.niFgen_ConfigureDigitalEdgeScriptTrigger(vi_ctype, trigger_id_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_start_trigger(self, source, edge=enums.StartTriggerDigitalEdgeEdge.RISING):
        '''configure_digital_edge_start_trigger

        Configures the Start Trigger for digital edge triggering.

        Args:
            source (str): Specifies which trigger source the signal generator uses.

                **Defined Values**

                **Default Value**: "PFI0"

                +-------------+-----------------------------------+
                | "PFI0"      | PFI 0                             |
                +-------------+-----------------------------------+
                | "PFI1"      | PFI 1                             |
                +-------------+-----------------------------------+
                | "PFI2"      | PFI 2                             |
                +-------------+-----------------------------------+
                | "PFI3"      | PFI 3                             |
                +-------------+-----------------------------------+
                | "PFI4"      | PFI 4                             |
                +-------------+-----------------------------------+
                | "PFI5"      | PFI 5                             |
                +-------------+-----------------------------------+
                | "PFI6"      | PFI 6                             |
                +-------------+-----------------------------------+
                | "PFI7"      | PFI 7                             |
                +-------------+-----------------------------------+
                | "PXI_Trig0" | PXI trigger line 0 or RTSI line 0 |
                +-------------+-----------------------------------+
                | "PXI_Trig1" | PXI trigger line 1 or RTSI line 1 |
                +-------------+-----------------------------------+
                | "PXI_Trig2" | PXI trigger line 2 or RTSI line 2 |
                +-------------+-----------------------------------+
                | "PXI_Trig3" | PXI trigger line 3 or RTSI line 3 |
                +-------------+-----------------------------------+
                | "PXI_Trig4" | PXI trigger line 4 or RTSI line 4 |
                +-------------+-----------------------------------+
                | "PXI_Trig5" | PXI trigger line 5 or RTSI line 5 |
                +-------------+-----------------------------------+
                | "PXI_Trig6" | PXI trigger line 6 or RTSI line 6 |
                +-------------+-----------------------------------+
                | "PXI_Trig7" | PXI trigger line 7 or RTSI line 7 |
                +-------------+-----------------------------------+
                | "PXI_Star"  | PXI star trigger line             |
                +-------------+-----------------------------------+

            edge (enums.StartTriggerDigitalEdgeEdge): Specifies the edge to detect.

                ****Defined Values****

                ****Default Value**:** StartTriggerDigitalEdgeEdge.RISING

                +-------------------------------------+------------------------------------------------------------------+
                | StartTriggerDigitalEdgeEdge.RISING  | Occurs when the signal transitions from low level to high level. |
                +-------------------------------------+------------------------------------------------------------------+
                | StartTriggerDigitalEdgeEdge.FALLING | Occurs when the signal transitions from high level to low level. |
                +-------------------------------------+------------------------------------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(edge) is not enums.StartTriggerDigitalEdgeEdge:
            raise TypeError('Parameter mode must be of type ' + str(enums.StartTriggerDigitalEdgeEdge))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        edge_ctype = visatype.ViInt32(edge.value)  # case S130
        error_code = self._library.niFgen_ConfigureDigitalEdgeStartTrigger(vi_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_level_script_trigger(self, trigger_id, source, trigger_when):
        '''configure_digital_level_script_trigger

        Configures the specified Script Trigger for digital level triggering.

        Args:
            trigger_id (str): Specifies the Script Trigger used for triggering.

                **Defined Values**

                **Default Value**: "ScriptTrigger0"

                +------------------+------------------+
                | "ScriptTrigger0" | Script Trigger 0 |
                +------------------+------------------+
                | "ScriptTrigger1" | Script Trigger 1 |
                +------------------+------------------+
                | "ScriptTrigger2" | Script Trigger 2 |
                +------------------+------------------+
                | "ScriptTrigger3" | Script Trigger 3 |
                +------------------+------------------+

            source (str): Specifies which trigger source the signal generator uses.

                **Defined Values**

                **Default Value**: "PFI0"

                +-------------+-----------------------------------+
                | "PFI0"      | PFI 0                             |
                +-------------+-----------------------------------+
                | "PFI1"      | PFI 1                             |
                +-------------+-----------------------------------+
                | "PFI2"      | PFI 2                             |
                +-------------+-----------------------------------+
                | "PFI3"      | PFI 3                             |
                +-------------+-----------------------------------+
                | "PFI4"      | PFI 4                             |
                +-------------+-----------------------------------+
                | "PFI5"      | PFI 5                             |
                +-------------+-----------------------------------+
                | "PFI6"      | PFI 6                             |
                +-------------+-----------------------------------+
                | "PFI7"      | PFI 7                             |
                +-------------+-----------------------------------+
                | "PXI_Trig0" | PXI trigger line 0 or RTSI line 0 |
                +-------------+-----------------------------------+
                | "PXI_Trig1" | PXI trigger line 1 or RTSI line 1 |
                +-------------+-----------------------------------+
                | "PXI_Trig2" | PXI trigger line 2 or RTSI line 2 |
                +-------------+-----------------------------------+
                | "PXI_Trig3" | PXI trigger line 3 or RTSI line 3 |
                +-------------+-----------------------------------+
                | "PXI_Trig4" | PXI trigger line 4 or RTSI line 4 |
                +-------------+-----------------------------------+
                | "PXI_Trig5" | PXI trigger line 5 or RTSI line 5 |
                +-------------+-----------------------------------+
                | "PXI_Trig6" | PXI trigger line 6 or RTSI line 6 |
                +-------------+-----------------------------------+
                | "PXI_Trig7" | PXI trigger line 7 or RTSI line 7 |
                +-------------+-----------------------------------+
                | "PXI_Star"  | PXI star trigger line             |
                +-------------+-----------------------------------+

            trigger_when (enums.TriggerWhen): Specifies whether the Script Trigger asserts on a high or low digital
                level.

                **Defined Values**

                **Default Value**: "HighLevel"

                +-------------+-------------------------------------------------+
                | "HighLevel" | Script Trigger asserts on a high digital level. |
                +-------------+-------------------------------------------------+
                | "LowLevel"  | Script Trigger asserts on a low digital level.  |
                +-------------+-------------------------------------------------+

        '''
        if type(trigger_when) is not enums.TriggerWhen:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerWhen))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C020
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case C020
        trigger_when_ctype = visatype.ViInt32(trigger_when.value)  # case S130
        error_code = self._library.niFgen_ConfigureDigitalLevelScriptTrigger(vi_ctype, trigger_id_ctype, source_ctype, trigger_when_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_arb_sequence(self, waveform_handles_array, loop_counts_array, sample_counts_array=None, marker_location_array=None):
        '''create_advanced_arb_sequence

        Creates an arbitrary sequence from an array of waveform handles and an
        array of corresponding loop counts. This function returns a handle that
        identifies the sequence. You pass this handle to the
        configure_arb_sequence function to specify what arbitrary sequence
        you want the signal generator to produce.

        The create_advanced_arb_sequence function extends on the
        create_arb_sequence function by adding the ability to set the
        number of samples in each sequence step and to set marker locations.

        An arbitrary sequence consists of multiple waveforms. For each waveform,
        you specify the number of times the signal generator produces the
        waveform before proceeding to the next waveform. The number of times to
        repeat a specific waveform is called the loop count.

        Note:
        The signal generator must not be in the Generating state when you call
        this function.
        You must call the nifgen_ConfigureOutputMode function to set the
        **outputMode** parameter to OutputMode.SEQ before calling this
        function.

        Args:
            waveform_handles_array (list of int): Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                nifgen_AllocateWaveform function or one of the following niFgen
                CreateWaveform functions:

                -  nifgen_CreateWaveformF64
                -  nifgen_CreateWaveformI16
                -  nifgen_CreateWaveformFromFileI16
                -  nifgen_CreateWaveformFromFileF64
                -  nifgen_CreateWaveformFromFileHWS

                **Default Value**: None

            loop_counts_array (list of int): Specifies the array of loop counts you want to use to create a new
                arbitrary sequence. The array must have at least as many elements as the
                value that you specify in the **sequenceLength** parameter. Each
                **loopCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates how many times to repeat that waveform. Each
                element of the **loopCountsArray** must be less than or equal to the
                maximum number of loop counts that the signal generator allows. You can
                obtain the maximum loop count from **maximumLoopCount** in the
                nifgen_QueryArbSeqCapabilities function.

                **Default Value**: None

            sample_counts_array (list of int): Specifies the array of sample counts that you want to use to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value you specify in the **sequenceLength** parameter. Each
                **sampleCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates the subset, in samples, of the given waveform to
                generate. Each element of the **sampleCountsArray** must be larger than
                the minimum waveform size, a multiple of the waveform quantum and no
                larger than the number of samples in the corresponding waveform. You can
                obtain these values by calling the nifgen_QueryArbWfmCapabilities
                function.

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
                pass this handle to nifgen_ConfigureArbSequence to generate the
                arbitrary sequence.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        sequence_length_ctype = visatype.ViInt32(0 if waveform_handles_array is None else len(waveform_handles_array))  # case S160
        waveform_handles_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_handles_array, library_type=visatype.ViInt32)  # case B550
        loop_counts_array_ctype = get_ctypes_pointer_for_buffer(value=loop_counts_array, library_type=visatype.ViInt32)  # case B550
        sample_counts_array_ctype = get_ctypes_pointer_for_buffer(value=sample_counts_array, library_type=visatype.ViInt32)  # case B550
        marker_location_array_ctype = get_ctypes_pointer_for_buffer(value=marker_location_array, library_type=visatype.ViInt32)  # case B550
        coerced_markers_array_size = (0 if marker_location_array is None else len(marker_location_array))  # case B560
        coerced_markers_array_ctype = get_ctypes_pointer_for_buffer(library_type=visatype.ViInt32, size=coerced_markers_array_size)  # case B560
        sequence_handle_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_CreateAdvancedArbSequence(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, sample_counts_array_ctype, marker_location_array_ctype, coerced_markers_array_ctype, None if sequence_handle_ctype is None else (ctypes.pointer(sequence_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(coerced_markers_array_ctype[i]) for i in range((0 if marker_location_array is None else len(marker_location_array)))], int(sequence_handle_ctype.value)

    def create_arb_sequence(self, waveform_handles_array, loop_counts_array):
        '''create_arb_sequence

        Creates an arbitrary sequence from an array of waveform handles and an
        array of corresponding loop counts. This function returns a handle that
        identifies the sequence. You pass this handle to the
        nifgen_ConfigureArbSequence function to specify what arbitrary sequence
        you want the signal generator to produce.

        An arbitrary sequence consists of multiple waveforms. For each waveform,
        you can specify the number of times that the signal generator produces
        the waveform before proceeding to the next waveform. The number of times
        to repeat a specific waveform is called the loop count.

        Note:
        You must call the nifgen_ConfigureOutputMode function to set the
        **outputMode** parameter to OutputMode.SEQ before calling this
        function.

        Args:
            waveform_handles_array (list of int): Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                nifgen_AllocateWaveform function or one of the following niFgen
                CreateWaveform functions:

                -  nifgen_CreateWaveformF64
                -  nifgen_CreateWaveformI16
                -  nifgen_CreateWaveformFromFileI16
                -  nifgen_CreateWaveformFromFileF64
                -  nifgen_CreateWaveformFromFileHWS

                **Default Value**: None

            loop_counts_array (list of int): Specifies the array of loop counts you want to use to create a new
                arbitrary sequence. The array must have at least as many elements as the
                value that you specify in the **sequenceLength** parameter. Each
                **loopCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates how many times to repeat that waveform. Each
                element of the **loopCountsArray** must be less than or equal to the
                maximum number of loop counts that the signal generator allows. You can
                obtain the maximum loop count from **maximumLoopCount** in the
                nifgen_QueryArbSeqCapabilities function.

                **Default Value**: None


        Returns:
            sequence_handle (int): Returns the handle that identifies the new arbitrary sequence. You can
                pass this handle to nifgen_ConfigureArbSequence to generate the
                arbitrary sequence.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        sequence_length_ctype = visatype.ViInt32(0 if waveform_handles_array is None else len(waveform_handles_array))  # case S160
        waveform_handles_array_ctype = get_ctypes_pointer_for_buffer(value=waveform_handles_array, library_type=visatype.ViInt32)  # case B550
        loop_counts_array_ctype = get_ctypes_pointer_for_buffer(value=loop_counts_array, library_type=visatype.ViInt32)  # case B550
        sequence_handle_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_CreateArbSequence(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, None if sequence_handle_ctype is None else (ctypes.pointer(sequence_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(sequence_handle_ctype.value)

    def create_freq_list(self, waveform, frequency_array, duration_array):
        '''create_freq_list

        Creates a frequency list from an array of frequencies
        (**frequencyArray**) and an array of durations (**durationArray**). The
        two arrays should have the same number of elements, and this value must
        also be the size of the **frequencyListLength**. The function returns a
        handle that identifies the frequency list (the **frequencyListHandle**).
        You can pass this handle to nifgen_ConfigureFreqList to specify what
        frequency list you want the signal generator to produce.

        A frequency list consists of a list of frequencies and durations. The
        signal generator generates each frequency for the given amount of time
        and then proceeds to the next frequency. When the end of the list is
        reached, the signal generator starts over at the beginning of the list.

        Note:
        The signal generator must not be in the Generating state when you call
        this function.

        Args:
            waveform (enums.Waveform): Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the func_waveform attribute to this
                value.

                ****Defined Values****

                **Default Value**: Waveform.SINE

                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SINE      | Specifies that the signal generator produces a sinusoid waveform.                                                                    |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SQUARE    | Specifies that the signal generator produces a square waveform.                                                                      |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.TRIANGLE  | Specifies that the signal generator produces a triangle waveform.                                                                    |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                               |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                               |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.DC        | Specifies that the signal generator produces a constant voltage.                                                                     |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.NOISE     | Specifies that the signal generator produces white noise.                                                                            |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.USER      | Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform function. |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------------+

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
                this handle to nifgen_ConfigureFreqList to generate the arbitrary
                sequence.

        '''
        if type(waveform) is not enums.Waveform:
            raise TypeError('Parameter mode must be of type ' + str(enums.Waveform))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        waveform_ctype = visatype.ViInt32(waveform.value)  # case S130
        frequency_list_length_ctype = visatype.ViInt32(0 if frequency_array is None else len(frequency_array))  # case S160
        frequency_array_ctype = get_ctypes_pointer_for_buffer(value=frequency_array, library_type=visatype.ViReal64)  # case B550
        duration_array_ctype = get_ctypes_pointer_for_buffer(value=duration_array, library_type=visatype.ViReal64)  # case B550
        frequency_list_handle_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_CreateFreqList(vi_ctype, waveform_ctype, frequency_list_length_ctype, frequency_array_ctype, duration_array_ctype, None if frequency_list_handle_ctype is None else (ctypes.pointer(frequency_list_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(frequency_list_handle_ctype.value)

    def disable(self):
        '''disable

        Places the instrument in a quiescent state where it has minimal or no
        impact on the system to which it is connected. The analog output and all
        exported signals are disabled.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_signal(self, signal, signal_identifier, output_terminal):
        '''export_signal

        Routes signals (clocks, triggers, and events) to the output terminal you
        specify.

        Any routes created within a session persist after the session closes to
        prevent signal glitching. To unconfigure signal routes created in
        previous sessions, set **resetDevice** in the init function to
        VI_TRUE or use the reset_device function.

        If you export a signal with this function and commit the session, the
        signal is routed to the output terminal you specify.

        Note:
        One or more of the referenced functions are not in the Python API for this driver.

        Args:
            signal (enums.Signal): Specifies the source of the signal to route.
                ****Defined Values****

                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.ONBOARD_REFERENCE_CLOCK | Onboard 10 MHz synchronization clock (PCI only)                                                                                                               |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.SYNC_OUT                | SYNC OUT signal The SYNC OUT signal is normally generated on the SYNC OUT front panel connector.                                                              |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.START_TRIGGER           | Start Trigger                                                                                                                                                 |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.MARKER_EVENT            | Marker Event                                                                                                                                                  |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.SAMPLE_CLOCK_TIMEBASE   | The clock from which the Sample Clock is derived                                                                                                              |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.SYNCHRONIZATION         | Synchronization strobe (NI 5404/5411/5431 only) A synchronization strobe is used to guarantee absolute synchronization between two or more signal generators. |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.SAMPLE_CLOCK            | Sample Clock                                                                                                                                                  |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.REFERENCE_CLOCK         | PLL Reference Clock                                                                                                                                           |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.SCRIPT_TRIGGER          | Script Trigger                                                                                                                                                |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.READY_FOR_START_EVENT   | Ready For Start Event                                                                                                                                         |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.STARTED_EVENT           | Started Event                                                                                                                                                 |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.DONE_EVENT              | Done Event                                                                                                                                                    |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Signal.DATA_MARKER_EVENT       | Data Marker Event                                                                                                                                             |
                +--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            signal_identifier (str): Specifies which instance of the selected signal to export.
                ****Defined Values****

                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "" (empty string)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Default (for non instance-based signals) |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "ScriptTrigger0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Script Trigger 0                         |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "ScriptTrigger1"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Script Trigger 1                         |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "ScriptTrigger2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Script Trigger 2                         |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "ScriptTrigger3"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Script Trigger 3                         |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "Marker0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Marker 0                                 |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "Marker1"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Marker 1                                 |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "Marker2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Marker 2                                 |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "Marker3"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Marker 3                                 |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "DataMarker0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Data Marker 0\*                          |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "DataMarker1"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Data Marker 1\*                          |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "DataMarker2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Data Marker 2\*                          |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | "DataMarker3"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Data Marker 3\*                          |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
                | \* These Data Marker values apply only to single-channel devices or to multichannel devices that are configured for single-channel operation. When using a device that is configured for multichannel operation, specify the channel number along with the signal identifier. For example, to export Data Marker 0 on channel 1 of a device configured for multichannel operation, use the value "1/ DataMarker0." If you do not specify a channel when using a device configured for multichannel generation, DataMarker0 generates on all channels. |                                          |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------+

            output_terminal (str): Specifies the output terminal to export the signal.
                ****Defined Values****

                +-------------------+------------------------------+
                | "" (empty string) | Do not export signal         |
                +-------------------+------------------------------+
                | "PFI0"            | PFI line 0                   |
                +-------------------+------------------------------+
                | "PFI1"            | PFI line 1                   |
                +-------------------+------------------------------+
                | "PFI4"            | PFI line 4                   |
                +-------------------+------------------------------+
                | "PFI5"            | PFI line 5                   |
                +-------------------+------------------------------+
                | "PXI_Trig0"       | PXI or RTSI line 0           |
                +-------------------+------------------------------+
                | "PXI_Trig1"       | PXI or RTSI line 1           |
                +-------------------+------------------------------+
                | "PXI_Trig2"       | PXI or RTSI line 2           |
                +-------------------+------------------------------+
                | "PXI_Trig3"       | PXI or RTSI line 3           |
                +-------------------+------------------------------+
                | "PXI_Trig4"       | PXI or RTSI line 4           |
                +-------------------+------------------------------+
                | "PXI_Trig5"       | PXI or RTSI line 5           |
                +-------------------+------------------------------+
                | "PXI_Trig6"       | PXI or RTSI line 6           |
                +-------------------+------------------------------+
                | "PXI_Trig7"       | PXI or RTSI line 7           |
                +-------------------+------------------------------+
                | "DDC_ClkOut"      | Clock out from DDC connector |
                +-------------------+------------------------------+
                | "PXI_Star"        | PXI star trigger line        |
                +-------------------+------------------------------+

                Note:
                The following **Defined Values** are examples of possible output
                terminals. For a complete list of the output terminals available on your
                device, refer to the Routes topic for your device or the **Device
                Routes** tab in MAX.

        '''
        if type(signal) is not enums.Signal:
            raise TypeError('Parameter mode must be of type ' + str(enums.Signal))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        signal_ctype = visatype.ViInt32(signal.value)  # case S130
        signal_identifier_ctype = ctypes.create_string_buffer(signal_identifier.encode(self._encoding))  # case C020
        output_terminal_ctype = ctypes.create_string_buffer(output_terminal.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_ExportSignal(vi_ctype, signal_ctype, signal_identifier_ctype, output_terminal_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_ext_cal_last_date_and_time(self):
        '''get_ext_cal_last_date_and_time

        Returns the date and time of the last successful external calibration.
        The time returned is 24-hour (military) local time; for example, if the
        device was calibrated at 2:30 PM, this function returns 14 for the
        **hour** parameter and 30 for the **minute** parameter.

        Returns:
            year (int): Specifies the year of the last successful calibration.

            month (int): Specifies the month of the last successful calibration.

            day (int): Specifies the day of the last successful calibration.

            hour (int): Specifies the hour of the last successful calibration.

            minute (int): Specifies the minute of the last successful calibration.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        year_ctype = visatype.ViInt32()  # case S200
        month_ctype = visatype.ViInt32()  # case S200
        day_ctype = visatype.ViInt32()  # case S200
        hour_ctype = visatype.ViInt32()  # case S200
        minute_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_GetExtCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_ext_cal_last_temp(self):
        '''get_ext_cal_last_temp

        Returns the temperature at the last successful external calibration. The
        temperature is returned in degrees Celsius.

        Returns:
            temperature (float): Specifies the temperature at the last successful calibration in degrees
                Celsius.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        temperature_ctype = visatype.ViReal64()  # case S200
        error_code = self._library.niFgen_GetExtCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_ext_cal_recommended_interval(self):
        '''get_ext_cal_recommended_interval

        Returns the recommended interval between external calibrations in
        months.

        Returns:
            months (int): Specifies the recommended interval between external calibrations in
                months.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        months_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_GetExtCalRecommendedInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_hardware_state(self):
        '''get_hardware_state

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        state_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_GetHardwareState(vi_ctype, None if state_ctype is None else (ctypes.pointer(state_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.HardwareState(state_ctype.value)

    def get_self_cal_last_date_and_time(self):
        '''get_self_cal_last_date_and_time

        Returns the date and time of the last successful self-calibration.

        All values are returned as separate parameters. Each parameter is
        returned as an integer, including the year, month, day, hour, minute,
        and second. For example, if the device is calibrated in September 2013,
        this function returns 9 for the **month** parameter and 2013 for the
        **year** parameter.

        The time returned is 24-hour (military) local time. For example, if the
        device was calibrated at 2:30 PM, this function returns 14 for the
        **hours** parameter and 30 for the **minutes** parameter.

        Returns:
            year (int): Specifies the year of the last successful calibration.

            month (int): Specifies the month of the last successful calibration.

            day (int): Specifies the day of the last successful calibration.

            hour (int): Specifies the hour of the last successful calibration.

            minute (int): Specifies the minute of the last successful calibration.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        year_ctype = visatype.ViInt32()  # case S200
        month_ctype = visatype.ViInt32()  # case S200
        day_ctype = visatype.ViInt32()  # case S200
        hour_ctype = visatype.ViInt32()  # case S200
        minute_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_GetSelfCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_self_cal_last_temp(self):
        '''get_self_cal_last_temp

        Returns the temperature at the last successful self-calibration. The
        temperature is returned in degrees Celsius.

        Returns:
            temperature (float): Specifies the temperature at the last successful calibration in degrees
                Celsius.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        temperature_ctype = visatype.ViReal64()  # case S200
        error_code = self._library.niFgen_GetSelfCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_self_cal_supported(self):
        '''get_self_cal_supported

        Returns whether the device supports self–calibration.

        Returns:
            self_cal_supported (bool): Returns whether the device supports self-calibration.

                ****Defined Values****

                +----------+------------------------------------+
                | VI_TRUE  | Self–calibration is supported.     |
                +----------+------------------------------------+
                | VI_FALSE | Self–calibration is not supported. |
                +----------+------------------------------------+

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        self_cal_supported_ctype = visatype.ViBoolean()  # case S200
        error_code = self._library.niFgen_GetSelfCalSupported(vi_ctype, None if self_cal_supported_ctype is None else (ctypes.pointer(self_cal_supported_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_supported_ctype.value)

    def _initiate_generation(self):
        '''_initiate_generation

        Initiates signal generation. If you want to abort signal generation,
        call the nifgen_AbortGeneration function. After the signal generation
        is aborted, you can call the _initiate_generation function to
        cause the signal generator to produce a signal again.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_InitiateGeneration(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_done(self):
        '''is_done

        Determines whether the current generation is complete. This function
        sets the **done** parameter to VI_TRUE if the session is in the Idle or
        Committed states.

        Note:
        NI-FGEN only reports the **done** parameter as VI_TRUE after the
        current generation is complete in Single trigger mode.

        Returns:
            done (bool): Returns information about the completion of waveform generation.

                **Defined Values**

                +----------+-----------------------------+
                | VI_TRUE  | Generation is complete.     |
                +----------+-----------------------------+
                | VI_FALSE | Generation is not complete. |
                +----------+-----------------------------+

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        done_ctype = visatype.ViBoolean()  # case S200
        error_code = self._library.niFgen_IsDone(vi_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    def query_arb_seq_capabilities(self):
        '''query_arb_seq_capabilities

        Returns the attributes of the signal generator that are related to
        creating arbitrary sequences (the max_num_sequences,
        min_sequence_length,
        max_sequence_length, and max_loop_count
        attributes).

        Returns:
            maximum_number_of_sequences (int): Returns the maximum number of arbitrary waveform sequences that the
                signal generator allows. NI-FGEN obtains this value from the
                max_num_sequences attribute.

            minimum_sequence_length (int): Returns the minimum number of arbitrary waveforms the signal generator
                allows in a sequence. NI-FGEN obtains this value from the
                min_sequence_length attribute.

            maximum_sequence_length (int): Returns the maximum number of arbitrary waveforms the signal generator
                allows in a sequence. NI-FGEN obtains this value from the
                max_sequence_length attribute.

            maximum_loop_count (int): Returns the maximum number of times the signal generator can repeat an
                arbitrary waveform in a sequence. NI-FGEN obtains this value from the
                max_loop_count attribute.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        maximum_number_of_sequences_ctype = visatype.ViInt32()  # case S200
        minimum_sequence_length_ctype = visatype.ViInt32()  # case S200
        maximum_sequence_length_ctype = visatype.ViInt32()  # case S200
        maximum_loop_count_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_QueryArbSeqCapabilities(vi_ctype, None if maximum_number_of_sequences_ctype is None else (ctypes.pointer(maximum_number_of_sequences_ctype)), None if minimum_sequence_length_ctype is None else (ctypes.pointer(minimum_sequence_length_ctype)), None if maximum_sequence_length_ctype is None else (ctypes.pointer(maximum_sequence_length_ctype)), None if maximum_loop_count_ctype is None else (ctypes.pointer(maximum_loop_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_sequences_ctype.value), int(minimum_sequence_length_ctype.value), int(maximum_sequence_length_ctype.value), int(maximum_loop_count_ctype.value)

    def query_arb_wfm_capabilities(self):
        '''query_arb_wfm_capabilities

        Returns the attributes of the signal generator that are related to
        creating arbitrary waveforms. These attributes are the maximum number of
        waveforms, waveform quantum, minimum waveform size, and maximum waveform
        size.

        Note:
        If you do not want to obtain the waveform quantum, pass a value of
        VI_NULL for this parameter.

        Returns:
            maximum_number_of_waveforms (int): Returns the maximum number of arbitrary waveforms that the signal
                generator allows. NI-FGEN obtains this value from the
                max_num_waveforms attribute.

            waveform_quantum (int): The size (number of points) of each waveform must be a multiple of a
                constant quantum value. This parameter obtains the quantum value that
                the signal generator uses. NI-FGEN returns this value from the
                waveform_quantum attribute.

                For example, when this attribute returns a value of 8, all waveform
                sizes must be a multiple of 8.

            minimum_waveform_size (int): Returns the minimum number of points that the signal generator allows in
                a waveform. NI-FGEN obtains this value from the
                min_waveform_size attribute.

            maximum_waveform_size (int): Returns the maximum number of points that the signal generator allows in
                a waveform. NI-FGEN obtains this value from the
                max_waveform_size attribute.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        maximum_number_of_waveforms_ctype = visatype.ViInt32()  # case S200
        waveform_quantum_ctype = visatype.ViInt32()  # case S200
        minimum_waveform_size_ctype = visatype.ViInt32()  # case S200
        maximum_waveform_size_ctype = visatype.ViInt32()  # case S200
        error_code = self._library.niFgen_QueryArbWfmCapabilities(vi_ctype, None if maximum_number_of_waveforms_ctype is None else (ctypes.pointer(maximum_number_of_waveforms_ctype)), None if waveform_quantum_ctype is None else (ctypes.pointer(waveform_quantum_ctype)), None if minimum_waveform_size_ctype is None else (ctypes.pointer(minimum_waveform_size_ctype)), None if maximum_waveform_size_ctype is None else (ctypes.pointer(maximum_waveform_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_waveforms_ctype.value), int(waveform_quantum_ctype.value), int(minimum_waveform_size_ctype.value), int(maximum_waveform_size_ctype.value)

    def query_freq_list_capabilities(self):
        '''query_freq_list_capabilities

        Returns the attributes of the signal generator that are related to
        creating frequency lists. These attributes are
        max_num_freq_lists,
        min_freq_list_length,
        max_freq_list_length,
        min_freq_list_duration,
        max_freq_list_duration, and
        freq_list_duration_quantum.

        Returns:
            maximum_number_of_freq_lists (int): Returns the maximum number of frequency lists that the signal generator
                allows. NI-FGEN obtains this value from the
                max_num_freq_lists attribute.

            minimum_frequency_list_length (int): Returns the minimum number of steps that the signal generator allows in
                a frequency list. NI-FGEN obtains this value from the
                min_freq_list_length attribute.

            maximum_frequency_list_length (int): Returns the maximum number of steps that the signal generator allows in
                a frequency list. NI-FGEN obtains this value from the
                max_freq_list_length attribute.

            minimum_frequency_list_duration (float): Returns the minimum duration that the signal generator allows in a step
                of a frequency list. NI-FGEN obtains this value from the
                min_freq_list_duration attribute.

            maximum_frequency_list_duration (float): Returns the maximum duration that the signal generator allows in a step
                of a frequency list. NI-FGEN obtains this value from the
                max_freq_list_duration attribute.

            frequency_list_duration_quantum (float): Returns the quantum of which all durations must be a multiple in a
                frequency list. NI-FGEN obtains this value from the
                freq_list_duration_quantum attribute.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        maximum_number_of_freq_lists_ctype = visatype.ViInt32()  # case S200
        minimum_frequency_list_length_ctype = visatype.ViInt32()  # case S200
        maximum_frequency_list_length_ctype = visatype.ViInt32()  # case S200
        minimum_frequency_list_duration_ctype = visatype.ViReal64()  # case S200
        maximum_frequency_list_duration_ctype = visatype.ViReal64()  # case S200
        frequency_list_duration_quantum_ctype = visatype.ViReal64()  # case S200
        error_code = self._library.niFgen_QueryFreqListCapabilities(vi_ctype, None if maximum_number_of_freq_lists_ctype is None else (ctypes.pointer(maximum_number_of_freq_lists_ctype)), None if minimum_frequency_list_length_ctype is None else (ctypes.pointer(minimum_frequency_list_length_ctype)), None if maximum_frequency_list_length_ctype is None else (ctypes.pointer(maximum_frequency_list_length_ctype)), None if minimum_frequency_list_duration_ctype is None else (ctypes.pointer(minimum_frequency_list_duration_ctype)), None if maximum_frequency_list_duration_ctype is None else (ctypes.pointer(maximum_frequency_list_duration_ctype)), None if frequency_list_duration_quantum_ctype is None else (ctypes.pointer(frequency_list_duration_quantum_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_freq_lists_ctype.value), int(minimum_frequency_list_length_ctype.value), int(maximum_frequency_list_length_ctype.value), float(minimum_frequency_list_duration_ctype.value), float(maximum_frequency_list_duration_ctype.value), float(frequency_list_duration_quantum_ctype.value)

    def read_current_temperature(self):
        '''read_current_temperature

        Reads the current onboard temperature of the device. The temperature is
        returned in degrees Celsius.

        Returns:
            temperature (float): Returns the current temperature read from onboard temperature sensors,
                in degrees Celsius.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        temperature_ctype = visatype.ViReal64()  # case S200
        error_code = self._library.niFgen_ReadCurrentTemperature(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def reset_device(self):
        '''reset_device

        Performs a hard reset on the device. Generation is stopped, all routes
        are released, external bidirectional terminals are tristated, FPGAs are
        reset, hardware is configured to its default state, and all session
        attributes are reset to their default states.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):
        '''reset_with_defaults

        Resets the instrument and reapplies initial user–specified settings from
        the logical name that was used to initialize the session. If the session
        was created without a logical name, this function is equivalent to the
        nifgen_reset function.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self):
        '''self_cal

        Performs a full internal self-calibration on the device. If the
        calibration is successful, new calibration data and constants are stored
        in the onboard EEPROM.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_SelfCal(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, trigger, trigger_id):
        '''send_software_edge_trigger

        Sends a command to trigger the signal generator. This VI can act as an
        override for an external edge trigger.

        Note:
        This VI does not override external digital edge triggers of the
        NI 5401/5411/5431.

        Args:
            trigger (enums.Trigger): Sets the clock mode of the signal generator.

                ****Defined Values****

                +---------------------------+
                | ClockMode.DIVIDE_DOWN     |
                +---------------------------+
                | ClockMode.HIGH_RESOLUTION |
                +---------------------------+
                | ClockMode.AUTOMATIC       |
                +---------------------------+

            trigger_id (str):

        '''
        if type(trigger) is not enums.Trigger:
            raise TypeError('Parameter mode must be of type ' + str(enums.Trigger))
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        trigger_ctype = visatype.ViInt32(trigger.value)  # case S130
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_until_done(self, max_time=10000):
        '''wait_until_done

        Waits until the device is done generating or until the maximum time has
        expired.

        Args:
            max_time (int): Specifies the timeout value in milliseconds.

        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        max_time_ctype = visatype.ViInt32(max_time)  # case S150
        error_code = self._library.niFgen_WaitUntilDone(vi_ctype, max_time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        '''_close

        Performs the following operations:

        -  Closes the instrument I/O session.
        -  Destroys the NI-FGEN session and all of its attributes.
        -  Deallocates any memory resources NI-FGEN uses.

        Not all signal routes established by calling the nifgen_ExportSignal
        and nifgen_RouteSignalOut functions are released when the NI-FGEN
        session is closed. The following table shows what happens to a signal
        route on your device when you call the _close function.

        +--------------------+-------------------+------------------+
        | Routes To          | NI 5401/5411/5431 | Other Devices    |
        +====================+===================+==================+
        | Front Panel        | Remain connected  | Remain connected |
        +--------------------+-------------------+------------------+
        | RTSI/PXI Backplane | Remain connected  | Disconnected     |
        +--------------------+-------------------+------------------+

        Note:
        After calling _close, you cannot use NI-FGEN again until you
        call the nifgen_init or nifgen_InitWithOptions functions.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset(self):
        '''reset

        Resets the instrument to a known state. This function aborts the
        generation, clears all routes, and resets session attributes to the
        default values. This function does not, however, commit the session
        properties or configure the device hardware to its default state.

        Note:
        For the NI 5401/5404/5411/5431, this function exhibits the same
        behavior as the nifgen_ResetDevice function.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):
        '''self_test

        Runs the instrument self-test routine and returns the test result(s).

        Note:
        When used on some signal generators, the device is reset after the
        self_test function runs. If you use the self_test
        function, your device may not be in its previously configured state
        after the function runs.

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
        vi_ctype = visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = visatype.ViInt16()  # case S200
        self_test_message_ctype = (visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFgen_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



