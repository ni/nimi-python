# -*- coding: utf-8 -*-
# This file was generated
import ctypes

from nifgen import attributes
from nifgen import enums
from nifgen import errors
from nifgen import library_singleton
from nifgen import visatype


class _Generation(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._session._initiate_generation()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._abort_generation()


class _SessionBase(object):
    '''Base class for all NI-FGEN sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    actual_arb_sample_rate = attributes.AttributeViReal64(1150109)
    '''
    Returns the actual sample rate value of the signal generator after any
    coercion or rounding.
    '''
    all_marker_events_latched_status = attributes.AttributeViInt32(1150349)
    '''
    Returns a bit field of the latched status of all Marker Events. Set this
    property to 0 to clear the latched status of all Marker Events.
    '''
    all_marker_events_live_status = attributes.AttributeViInt32(1150344)
    '''
    Returns a bit field of the live status of all Marker Events.
    '''
    analog_data_mask = attributes.AttributeViInt32(1150234)
    '''
    Specifies the mask to apply to the analog output data. The masked data
    is replaced with the data in the `Analog Static
    Value <pniFgen_AnalogStaticValue.html>`__ property.
    '''
    analog_filter_enabled = attributes.AttributeViBoolean(1150103)
    '''
    Specifies whether the signal generator applies an analog filter to the
    output signal. Set this property to TRUE to enable the filter. This
    property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script
    output modes. You also can use this property in Standard Function and
    Frequency List output modes for user-defined waveforms.

    **Default Value**: FALSE
    '''
    analog_path = attributes.AttributeEnum(attributes.AttributeViInt32, enums.AnalogPath, 1150222)
    '''
    Specifies the analog signal path. The main path allows the user to
    configure gain, offset, analog filter status, output impedance, and
    output enable.

    The direct path presents a much smaller gain range, and you cannot
    adjust offset or the filter status. The direct path provides a smaller
    output range but lower distortion. The main path has two amplifier
    options, high and low gain. Setting this value to
    **NIFGEN_VAL_MAIN_ANALOG_PATH** allows NI-FGEN to choose the
    amplifier based on the user-specified gain.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    analog_static_value = attributes.AttributeViInt32(1150235)
    '''
    Specifies the static value that replaces data masked by the `Analog Data
    Mask <pniFgen_AnalogDataMask.html>`__ property.
    '''
    arb_gain = attributes.AttributeViReal64(1250202)
    '''
    Specifies the factor by which the signal generator scales the arbitrary
    waveform data. When you create arbitrary waveforms, you must first
    normalize the data points to the range -1.0 to +1.0. Use this property
    to scale the arbitrary waveform to other ranges.

    For example, when you set this property to 2.0, the output signal ranges
    from -2.0 V to +2.0 V.

    Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
    property is set to **NIFGEN_VAL_OUTPUT_ARB** or
    **NIFGEN_VAL_OUTPUT_SEQ**.
    '''
    arb_marker_position = attributes.AttributeViInt32(1150327)
    '''
    Specifies the position for a marker to be asserted in the arbitrary
    waveform.

    Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
    property is set to **NIFGEN_VAL_OUTPUT_ARB**. Use the `niFgen Export
    Signal <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Export_Signal.html')>`__
    VI to export the marker signal.

    **Default Value**: -1
    '''
    arb_offset = attributes.AttributeViReal64(1250203)
    '''
    Specifies the value the signal generator adds to the arbitrary waveform
    data. When you create arbitrary waveforms, you must first normalize the
    data points to the range -1.0 to +1.0. Use this property to shift the
    arbitrary waveform range.

    For example, when you set this property to 1.0, the output signal ranges
    from 0.0 V to 2.0 V.

    Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
    property is set to **NIFGEN_VAL_OUTPUT_ARB** or
    **NIFGEN_VAL_OUTPUT_SEQ**.
    '''
    arb_repeat_count = attributes.AttributeViInt32(1150328)
    '''
    Specifies the number of times to repeat the arbitrary waveform when the
    **Trigger Mode** parameter in the `niFgen Configure Trigger
    Mode <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Configure_Trigger_Mode.html')>`__
    VI is set to **Single** or **Stepped**.

    This property is ignored if the **Trigger Mode** parameter is set to
    **Continuous** or **Burst**. Use this property when the `Output
    Mode <pniFgen_OutputMode.html>`__ property is set to
    **NIFGEN_VAL_OUTPUT_ARB**.

    When used during
    `streaming <javascript:LaunchHelp('SigGenHelp.chm::/streaming.html')>`__
    operations, this property specifies the number of times to repeat the
    streaming waveform (the onboard memory allocated for streaming).

    **Default Value**: 1
    '''
    arb_sample_rate = attributes.AttributeViReal64(1250204)
    '''
    Specifies the rate, in samples per second, at which the signal generator
    generates the points in arbitrary waveforms.

    Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
    property is set to **NIFGEN_VAL_OUTPUT_ARB** or
    **NIFGEN_VAL_OUTPUT_SEQ**.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    arb_sequence_handle = attributes.AttributeViInt32(1250211)
    '''
    Selects which sequence the signal generator produces. You can create
    multiple sequences using the `niFgen Create Arbitrary
    Sequence <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Arbitrary_Sequence.html')>`__
    VI.

    The niFgen Create Arbitrary Sequence VI returns a **Sequence Handle**
    that you use to identify the particular sequence. To configure the
    signal generator to produce a particular sequence, set this property to
    the **Sequence Handle** value. Use this property when the `Output
    Mode <pniFgen_OutputMode.html>`__ property is set to
    **NIFGEN_VAL_OUTPUT_SEQ**.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    arb_waveform_handle = attributes.AttributeViInt32(1250201)
    '''
    Selects which arbitrary waveform the signal generator produces. You can
    create multiple arbitrary waveforms using the `niFgen Create
    Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
    VI.

    The `niFgen Create
    Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
    VI, `niFgen Allocate
    Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Allocate_Waveform.html')>`__
    VI, and similar VIs return a **Waveform Handle** that you use to
    identify the particular waveform. To configure the signal generator to
    produce a particular waveform, set this property to the **Waveform
    Handle** value.

    Use this property only when the `Output
    Mode <pniFgen_OutputMode.html>`__ property is set to
    **NIFGEN_VAL_OUTPUT_ARB**.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    aux_power_enabled = attributes.AttributeViBoolean(1150411)
    '''
    Controls the specified auxiliary power pin. Setting this property to
    TRUE energizes the auxiliary power when the session is committed. When
    this property is FALSE, the power pin of the connector outputs no power.

    **Default Value**: FALSE
    '''
    bus_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.BusType, 1150215)
    '''
    Returns the bus type of the signal generator.
    '''
    cache = attributes.AttributeViBoolean(1050004)
    '''
    Specifies whether to cache the value of properties.

    When caching is enabled (TRUE), NI-FGEN keeps track of the current
    instrument settings and avoids sending redundant commands to the
    instrument. Thus, you can significantly increase execution speed.
    NI-FGEN can choose always to cache or never to cache particular
    properties regardless of the setting of this property. Use the `niFgen
    Initialize With
    Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
    VI to override this value.

    **Default Value**: TRUE
    '''
    cal_adc_input = attributes.AttributeEnum(attributes.AttributeViInt32, enums.CalADCInput, 1150227)
    '''
    Specifies the input of the calibration ADC. The ADC can take a reading
    from several inputs: the analog output, a 2.5 V reference, and ground.
    The latter two inputs are used to calibrate the ADC itself.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    channel_count = attributes.AttributeViInt32(1050203)
    '''
    Returns the number of channels that NI-FGEN supports. For each property
    for which IVI_VAL_MULTI_CHANNEL is set, the IVI engine maintains a
    separate cache value for each channel.
    '''
    channel_delay = attributes.AttributeViReal64(1150369)
    '''
    Specifies the delay to apply to the analog output of the channel
    specified by the `Active Channel <pniFgen_ActiveChannel.html>`__
    property.

    You can use the output delay to configure the timing relationship
    between channels on a multichannel device. Values for this property can
    be zero or positive. A value of zero indicates that the channels are
    aligned. A positive value delays the analog output by the specified
    number of seconds.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    clock_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ClockMode, 1150110)
    '''
    Specifies the Sample Clock mode for the signal generator.

    For signal generators that support it, this property allows switching
    the Sample Clock to a high-resolution clocking mode. When in divide-down
    sampling mode, the sample rate can be set only to certain frequencies,
    based on dividing down the Sample Clock. However, in high-resolution
    mode, the sample rate may be set to any value.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    common_mode_offset = attributes.AttributeViReal64(1150366)
    '''
    Specifies the value the signal generator adds to or subtracts from the
    arbitrary waveform data. This property applies only when set the
    `Terminal Configuration <pniFgen_TerminalConfiguration.html>`__ property
    to **Differential**. Common-mode offset is applied to the signals
    generated at each differential output terminal.
    '''
    daqmx_task = attributes.AttributeViInt32(1150221)
    '''
    Returns the NI-DAQmx task pointer.
    '''
    data_marker_events_count = attributes.AttributeViInt32(1150273)
    '''
    Returns the number of Data Marker Events supported by the device.
    '''
    data_marker_event_data_bit_number = attributes.AttributeViInt32(1150337)
    '''
    Specifies the bit number to assign to the Data Marker Event.
    '''
    data_marker_event_level_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DataMarkerEventLevelPolarity, 1150338)
    '''
    Specifies the output polarity of the Data Marker Event. Refer to `Data
    Marker
    Events <javascript:LaunchHelp('SigGenHelp.chm::/events_data_markers.html')>`__
    topic for more information about Data Marker Event polarity.
    '''
    data_marker_event_output_terminal = attributes.AttributeViString(1150339)
    '''
    Specifies the destination terminal for the Data Marker Event. For a list
    of the terminals available on your device, refer to the Routes topic for
    your device or the **Device Routes** tab in MAX.

    Note:
    NI recommends using a data sample rate of less than 200 MS/s for data
    markers routed to RTSI. Faster sample rates may lead to unwanted
    behavior.
    '''
    data_transfer_block_size = attributes.AttributeViInt32(1150241)
    '''
    Specifies the number of samples at a time to download to onboard memory.
    This property is useful when the total data to be transferred to onboard
    memory is large.
    '''
    data_transfer_maximum_bandwidth = attributes.AttributeViReal64(1150373)
    '''
    Specifies the maximum amount of bus bandwidth to use for data transfers.

    The signal generator limits data transfer speeds on the PCI Express bus
    to the value you specify for this property. Set this property to
    optimize bus bandwidth usage for multidevice streaming applications by
    preventing the signal generator from consuming all the available
    bandwidth on a PCI Express link when waveforms are being written to the
    onboard memory of the device.
    '''
    data_transfer_maximum_in_flight_reads = attributes.AttributeViInt32(1150375)
    '''
    Specifies the maximum number of concurrent PCI Express read requests the
    signal generator can issue.

    When transferring data from computer memory to device onboard memory
    across the PCI Express bus, the signal generator can issue multiple
    memory reads at the same time. In general, the larger the number of read
    requests, the more efficiently the device uses the bus because the
    multiple read requests keep the data flowing, even in a PCI Express
    topology that has high latency due to PCI Express switches in the data
    path. Most NI devices can issue a large number of read requests
    (typically 8 or 16). By default, this property is set to the highest
    value the signal generator supports.

    If other devices in your system cannot tolerate long data latencies, it
    may be helpful to decrease the number of in-flight read requests the NI
    signal generator issues. This change helps to reduce the amount of data
    the signal generator reads at one time.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    data_transfer_preferred_packet_size = attributes.AttributeViInt32(1150374)
    '''
    Specifies the preferred size of the data field in a PCI Express read
    request packet.

    In general, the larger the packet size, the more efficiently the device
    uses the bus. By default, NI signal generators use the largest packet
    size allowed by the system. However, due to different system
    implementations, some systems may perform better with smaller packet
    sizes.

    Recommended values for this property are powers of two between 64 and
    512.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    digital_data_mask = attributes.AttributeViInt32(1150236)
    '''
    Specifies the mask to apply to the output on the digital connector. The
    masked data is replaced with the data in the `Digital Static
    Value <pniFgen_DigitalStaticValue.html>`__ property.
    '''
    digital_edge_script_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ScriptTriggerDigitalEdgeEdge, 1150292)
    '''
    Specifies the active edge for the Script Trigger. This property is used
    when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
    property is set to **Digital Edge**.
    '''
    digital_edge_script_trigger_source = attributes.AttributeViString(1150291)
    '''
    Specifies the source terminal for the Script Trigger. This property is
    used when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
    property is set to **Digital Edge**.
    '''
    digital_edge_start_trigger_edge = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartTriggerDigitalEdgeEdge, 1150282)
    '''
    Specifies the active edge for the Start Trigger. This property is used
    only when the `Start Trigger Type <pniFgen_StartTriggerType.html>`__
    property is set to **Digital Edge**.
    '''
    digital_edge_start_trigger_source = attributes.AttributeViString(1150281)
    '''
    Specifies the source terminal for the Start Trigger. This property is
    used only when the `Start Trigger
    Type <pniFgen_StartTriggerType.html>`__ property is set to **Digital
    Edge**.

    You can specify any valid source terminal for this property. Valid
    sources can be found in the Routes topic for your device or in
    Measurement & Automation Explorer under the **Device Routes** tab.

    Source terminals can be specified in two ways. If your device is named
    Dev1 and your terminal is PFI0, then the terminal can be specified as a
    fully qualified terminal name, "/Dev1/PFI0". You can also specify the
    terminal using PFI 0.
    '''
    digital_filter_enabled = attributes.AttributeViBoolean(1150102)
    '''
    Specifies whether the signal generator applies a digital filter to the
    output signal. Set this property to TRUE to use a digital filter. This
    property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script
    output modes. You also can use this property in Standard Function and
    Frequency List output modes for user-defined waveforms.

    **Default Value**: FALSE
    '''
    digital_filter_interpolation_factor = attributes.AttributeViReal64(1150218)
    '''
    Specifies the interpolation factor when the `Digital Filter
    Enabled <pniFgen_DigitalFilterEnabled.html>`__ property is set to TRUE.

    **Valid Values**: 2, 4, and 8

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    digital_gain = attributes.AttributeViReal64(1150254)
    '''
    Specifies a factor by which the signal generator digitally multiplies
    generated data before converting it to an analog signal in the DAC. For
    a digital gain greater than 1.0, the product of digital gain times the
    generated data must be inside the range ±1.0, assuming floating point
    data. If the product exceeds these limits, the signal generator clips
    the output signal, and an error results.

    Some signal generators support both digital gain and analog gain,
    specified with the `Amplitude <pniFgen_Amplitude.html>`__ property or
    `Arbitrary Waveform Gain <pniFgen_ArbitraryWaveformGain.html>`__
    property. Digital gain can be changed during generation without the
    glitches that may occur when changing analog gains, because of relay
    switching. However, the DAC output resolution is a function of analog
    gain, so only analog gain makes full use of the resolution of the DAC.

    **Default Value**: 1
    '''
    digital_level_script_trigger_active_level = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ScriptTriggerDigitalLevelActiveLevel, 1150294)
    '''
    Specifies the active level for the Script Trigger. This property is used
    when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
    property is set to **Digital Level**.
    '''
    digital_level_script_trigger_source = attributes.AttributeViString(1150293)
    '''
    Specifies the source terminal for the Script Trigger. This property is
    used when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
    property is set to **Digital Level**.
    '''
    digital_pattern_enabled = attributes.AttributeViBoolean(1150101)
    '''
    Specifies whether the signal generator generates a digital pattern
    corresponding to the output signal. Set this property to TRUE to
    generate a digital pattern.
    '''
    digital_static_value = attributes.AttributeViInt32(1150237)
    '''
    Specifies the static value that replaces data masked by the `Digital
    Data Mask <pniFgen_DigitalDataMask.html>`__ property.
    '''
    direct_dma_enabled = attributes.AttributeViBoolean(1150244)
    '''
    Enables the device for Direct DMA writes.

    When enabled, all `niFgen Create
    Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
    VI and `niFgen Write
    Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_Waveform_poly.html')>`__
    VI calls that are given a data address in the Direct DMA window download
    data residing on the Direct DMA device to the instrument onboard memory.
    '''
    direct_dma_window_address = attributes.AttributeViInt32(1150274)
    '''
    Specifies the window address (beginning of window) of the waveform data
    source. This window address is specified by your Direct DMA-compatible
    data source.
    '''
    direct_dma_window_size = attributes.AttributeViInt32(1150245)
    '''
    Specifies the size of the memory window provided by your Direct
    DMA-compatible data source.
    '''
    done_event_delay = attributes.AttributeViReal64(1150358)
    '''
    Specifies the amount of delay applied to a Done Event with respect to
    the analog output of the signal generator.

    A positive delay value indicates that the Done Event occurs after the
    analog data, while a negative delay value indicates that the Done Event
    occurs before the analog data. A value of zero aligns the Done Event
    with the analog output.

    You can specify the units of the delay value by setting the `Delay
    Units <pniFgen_DoneEventDelayUnits.html>`__ property.

    **Default Value**: 0
    '''
    done_event_delay_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DoneEventDelayUnits, 1150359)
    '''
    Specifies the units used for the `Done Event Delay
    Value <pniFgen_DoneEventDelayValue.html>`__ property.
    '''
    done_event_latched_status = attributes.AttributeViBoolean(1150351)
    '''
    Returns the latched status of the specified Done Event.
    '''
    done_event_level_active_level = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DoneEventActiveLevel, 1150317)
    '''
    Specifies the output polarity of the Done Event.
    '''
    done_event_output_behavior = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DoneEventOutputBehavior, 1150332)
    '''
    Specifies the output behavior for the Done Event.
    '''
    done_event_output_terminal = attributes.AttributeViString(1150315)
    '''
    Specifies the destination terminal for the Done Event. For a list of the
    terminals available on your device, refer to the Routes topic for your
    device or the **Device Routes** tab in MAX.
    '''
    done_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DoneEventPulsePolarity, 1150319)
    '''
    Specifies the output polarity of the Done Event.
    '''
    done_event_pulse_width = attributes.AttributeViReal64(1150336)
    '''
    Specifies the pulse width for the Done Event.
    '''
    done_event_pulse_width_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DoneEventPulseWidthUnits, 1150334)
    '''
    Specifies the pulse width units for the Done Event.
    '''
    error_elaboration = attributes.AttributeViString(1050103)
    '''
    Contains an optional string with additional information concerning the
    primary error condition.
    '''
    exported_onboard_reference_clock_output_terminal = attributes.AttributeViString(1150322)
    '''
    Specifies the terminal at which to export the onboard Reference Clock.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.
    '''
    exported_reference_clock_output_terminal = attributes.AttributeViString(1150321)
    '''
    Specifies the terminal at which to export the Reference Clock.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.
    '''
    exported_sample_clock_divisor = attributes.AttributeViInt32(1150219)
    '''
    Specifies the factor by which to divide the update (Sample) Clock before
    it is exported.

    To export the Sample Clock, use the `niFgen Export
    Signal <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Export_Signal.html')>`__
    VI or the `Exported Sample Clock Output
    Terminal <pniFgen_ExportedSampleClockOutputTerminal.html>`__ property.

    **Valid Values**: 1 to 4,096

    **Default Value**: 1

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    exported_sample_clock_output_terminal = attributes.AttributeViString(1150320)
    '''
    Specifies the terminal at which to export the Sample Clock. If you
    specify a divisor with the `Exported Sample Clock
    Divisor <pniFgen_ExportedSampleClockDivisor.html>`__ property, the
    Sample Clock exported with this property is the value of the Sample
    Clock after it is divided-down.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.

    Note:
    The signal generator must not be in the Generating state when you change
    this property. To change the device configuration, call the `niFgen
    Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    exported_sample_clock_timebase_divisor = attributes.AttributeViInt32(1150230)
    '''
    Specifies the factor by which to divide the device clock (Sample Clock
    timebase) before it is exported.

    To export the Sample Clock timebase, use the `niFgen Export
    Signal <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Export_Signal.html')>`__
    VI or the `Exported Sample Clock Timebase Output
    Terminal <pniFgen_ExportedSampleClockTimebaseOutputTerminal.html>`__
    property.

    **Valid Values**: 1 to 4,194,304

    Note: Not all devices support a divisor value of 1.
    '''
    exported_sample_clock_timebase_output_terminal = attributes.AttributeViString(1150329)
    '''
    Specifies the terminal at which to export the Sample Clock Timebase.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.

    If you specify a divisor with the `Exported Sample Clock Timebase
    Divisor <pniFgen_ExportedSampleClockTimebaseDivisor.html>`__ property,
    the Sample Clock timebase exported with the Exported Sample Clock
    Timebase Output Terminal property is the value of the Sample Clock
    timebase after it is divided down.

    Note:
    The signal generator must not be in the Generating state when you change
    this property. To change the device configuration, call the `niFgen
    Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    exported_script_trigger_output_terminal = attributes.AttributeViString(1150295)
    '''
    Specifies the output terminal for the exported Script Trigger.

    Setting this property to an empty string means that when you commit the
    session, the signal is removed from that terminal and, if possible, the
    terminal is tristated.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.
    '''
    exported_start_trigger_output_terminal = attributes.AttributeViString(1150283)
    '''
    Specifies the destination terminal for exporting the Start Trigger.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.
    '''
    external_clock_delay_binary_value = attributes.AttributeViInt32(1150233)
    '''
    Specifies the external clock delay binary value.
    '''
    external_sample_clock_multiplier = attributes.AttributeViReal64(1150376)
    '''
    Specifies a multiplication factor to use to obtain a desired sample rate
    from an external Sample Clock.

    The resulting sample rate is equal to this factor multiplied by the
    external Sample Clock rate. You can use this property to generate
    samples at a rate higher than your external clock rate. When using this
    property, you do not need to explicitly set the external clock rate.
    '''
    file_transfer_block_size = attributes.AttributeViInt32(1150240)
    '''
    Specifies the maximum number of samples to transfer at one time from the
    device to host memory. This property is used in conjunction with the
    `niFgen Create Waveform From
    File <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
    VI and the `niFgen Write Waveform From
    File <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_Waveform_poly.html')>`__
    VI.

    If the requested value is not evenly divisible by the required
    increment, this property is coerced up to the next 64-sample increment
    (32-sample increment for complex samples).
    '''
    filter_correction_frequency = attributes.AttributeViReal64(1150104)
    '''
    Specifies the filter correction frequency of the analog filter. This
    property can correct for the ripples in the analog filter frequency
    response at the frequency specified.

    When using the Standard Waveform output mode, this property should be
    set to the same frequency as the standard waveform. To disable filter
    correction, set this property to 0.

    **Units**: hertz (Hz)

    **Default Value**: 0
    '''
    flatness_correction_enabled = attributes.AttributeViBoolean(1150323)
    '''
    Specify a value of TRUE to enable flatness correction. When flatness
    correction is enabled, the signal generator applies a flatness
    correction factor to the generated sine wave to ensure the same output
    power level at all frequencies.

    Set this property to FALSE when performing flatness calibration.
    '''
    fpga_bitfile_path = attributes.AttributeViString(1150412)
    '''
    Gets the absolute file path to the bitfile loaded on the FPGA.
    '''
    freq_list_duration_quantum = attributes.AttributeViReal64(1150214)
    '''
    Returns the quantum that all durations must be a multiple of in a
    frequency list.
    '''
    freq_list_handle = attributes.AttributeViInt32(1150208)
    '''
    Sets which frequency list the signal generator produces. You create a
    frequency list using the `niFgen Create Frequency
    List <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Frequency_List.html')>`__
    VI. The niFgen Create Frequency List VI returns a handle that you use to
    identify the list.

    **Default Value**: None

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    func_amplitude = attributes.AttributeViReal64(1250102)
    '''
    Controls the amplitude of the standard waveform that the signal
    generator produces. This value is the amplitude at the output terminal.

    For example, to produce a waveform ranging from -5.00 V to +5.00 V, set
    Amplitude property to 10.00 V.

    **Units**: volts peak-to-peak (Vpk-pk)

    **Default Value**: None

    Note:
    This parameter does not affect signal generator behavior when you set
    the `Waveform <pniFgen_Waveform.html>`__ property to
    **NIFGEN_VAL_WFM_DC**.
    '''
    func_buffer_size = attributes.AttributeViInt32(1150238)
    '''
    Contains the number of samples used in the standard function waveform
    buffer.

    This property is valid only on devices that implement Standard Function
    output mode in software, and it is read-only for all other devices.

    Note:
    Refer to the `Standard Function
    Mode <javascript:LaunchHelp('SigGenHelp.chm::/Function_Generation_Mode.html')>`__
    topic in the *NI Signal Generators Help* for more information about the
    implementation of Standard Function output mode on your device.
    '''
    func_dc_offset = attributes.AttributeViReal64(1250103)
    '''
    Controls the DC offset of the standard waveform that the signal
    generator produces.

    This value is the offset at the output terminal. The value is the offset
    from ground to the center of the waveform you specify with the
    `Waveform <pniFgen_Waveform.html>`__ property.

    For example, to configure a waveform with an amplitude of 10.00 V to
    range from 0.00 V to +10.00 V, set this property to 5.00 V.

    **Units**: volts (V)

    **Default Value**: None
    '''
    func_duty_cycle_high = attributes.AttributeViReal64(1250106)
    '''
    Specifies the duty cycle of the square wave the signal generator is
    producing. Specify this property as a percentage of the time the square
    wave is high in a cycle.

    **Units**: Percentage of time the waveform is high

    **Default Value**: 50%

    Note:
    This parameter only affects signal generator behavior when you set the
    `Waveform <pniFgen_Waveform.html>`__ property to
    **NIFGEN_VAL_WFM_SQUARE**.
    '''
    func_frequency = attributes.AttributeViReal64(1250104)
    '''
    Controls the frequency of the standard waveform that the signal
    generator produces.

    **Units**: hertz (Hz)

    **Default Value**: None

    Note:
    This parameter does not affect signal generator behavior when you set
    the `Waveform <pniFgen_Waveform.html>`__ property to
    **NIFGEN_VAL_WFM_DC**. For **NIFGEN_VAL_WFM_SINE** , the range is
    between 0 MHz and 16 MHz, but the range is between 0 MHz and 1 MHz for
    all other waveforms.
    '''
    func_max_buffer_size = attributes.AttributeViInt32(1150239)
    '''
    Sets the maximum number of samples that can be used in the standard
    function waveform buffer. Increasing this value may increase the quality
    of the waveform but may also increase the amount of time required to
    change the waveform while running.

    This property is valid only on devices that implement Standard Function
    output mode in software, and it is read-only for all other devices.

    Note:
    Refer to the `Standard Function
    Mode <javascript:LaunchHelp('SigGenHelp.chm::/Function_Generation_Mode.html')>`__
    topic in the *NI Signal Generators Help* for more information about the
    implementation of Standard Function output mode on your device.
    '''
    func_start_phase = attributes.AttributeViReal64(1250105)
    '''
    Controls horizontal offset of the standard waveform the signal generator
    produces. Specify this property in degrees of one waveform cycle.

    A start phase of 180 degrees means output generation begins halfway
    through the waveform. A start phase of 360 degrees offsets the output by
    an entire waveform cycle, which is identical to a start phase of 0
    degrees.

    **Units**: Degrees of one cycle

    **Default Value**: None

    Note:
    This property does not affect signal generator behavior when you set the
    `Waveform <pniFgen_Waveform.html>`__ property to
    **NIFGEN_VAL_WFM_DC**.
    '''
    func_waveform = attributes.AttributeEnum(attributes.AttributeViInt32, enums.Waveform, 1250101)
    '''
    Specifies which standard waveform the signal generator produces. Use
    this property only when the `Output Mode <pniFgen_OutputMode.html>`__
    property is set to **NIFGEN_VAL_OUTPUT_FUNC**.

    **Default Value**: **NIFGEN_VAL_WFM_DC**
    '''
    gain_dac_value = attributes.AttributeViInt32(1150223)
    '''
    Specifies the value programmed to the Gain DAC. The value should be
    treated as an unsigned, right-justified number.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    group_capabilities = attributes.AttributeViString(1050401)
    '''
    Returns a comma-separated list of class-extension groups that NI-FGEN
    implements.
    '''
    idle_behavior = attributes.AttributeEnum(attributes.AttributeViInt32, enums.IdleBehavior, 1150377)
    '''
    Specifies the behavior of the output during the Idle state.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    idle_value = attributes.AttributeViInt32(1150378)
    '''
    Specifies the value to generate in the Idle state. You must set the
    `Idle Behavior <pniFgen_IdleBehavior.html>`__ property to **Jump To
    Value** to use this property.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    instrument_firmware_revision = attributes.AttributeViString(1050510)
    '''
    Returns the firmware revision information for the instrument you are
    currently using.
    '''
    instrument_manufacturer = attributes.AttributeViString(1050511)
    '''
    Returns the name of the instrument manufacturer you are currently using.
    '''
    instrument_model = attributes.AttributeViString(1050512)
    '''
    Returns the model number or name of the instrument that you are
    currently using.
    '''
    interchange_check = attributes.AttributeViBoolean(1050021)
    '''
    Specifies whether to perform interchangeability checking and log
    interchangeability warnings when you call VIs. Set this property to TRUE
    to enable interchangeability checking.

    Interchangeability warnings indicate that using your application with a
    different instrument might cause different behavior. Interchangeability
    checking examines the properties in a capability group only if you
    specify a value for at least one property within that group.
    Interchangeability warnings can occur when a property affects the
    behavior of the instrument and you have not set that property or the
    property has been invalidated since you set it.
    '''
    io_resource_descriptor = attributes.AttributeViString(1050304)
    '''
    Returns the resource descriptor NI-FGEN uses to identify the physical
    device.

    If you initialize NI-FGEN with a logical name, this property contains
    the resource descriptor that corresponds to the entry in the IVI
    Configuration utility.

    If you initialize NI-FGEN with the resource descriptor, this property
    contains that value.
    '''
    load_impedance = attributes.AttributeViReal64(1150220)
    '''
    Specifies the load impedance connected to the analog output of the
    channel.

    If the load impedance is set to -1.0, NI-FGEN matches the load impedance
    to the `Output Impedance <pniFgen_OutputImpedance.html>`__ property
    value. NI-FGEN compensates to give the desired peak-to-peak voltage
    amplitude or arbitrary gain (relative to 1 V).

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    logical_name = attributes.AttributeViString(1050305)
    '''
    Returns the logical name you specified when opening the current IVI
    session.

    You may pass a logical name to the `niFgen
    Initialize <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize.html')>`__
    VI or the `niFgen Initialize With
    Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
    VI. The IVI Configuration utility must contain an entry for the logical
    name. The logical name entry refers to a virtual instrument section in
    the IVI Configuration file. The virtual instrument section specifies a
    physical device and initial user options.
    '''
    major_version = attributes.AttributeViInt32(1050503)
    '''
    Returns the major version number of NI-FGEN.
    '''
    marker_events_count = attributes.AttributeViInt32(1150271)
    '''
    Returns the number of markers supported by the device. Use this property
    when the `Output Mode <pniFgen_OutputMode.html>`__ property is set to
    **NIFGEN_VAL_OUTPUT_SCRIPT**.
    '''
    marker_event_delay = attributes.AttributeViReal64(1150354)
    '''
    Specifies the amount of delay applied to a Marker Event with respect to
    the analog output of the signal generator.

    A positive delay value indicates that the Marker Event occurs after the
    analog data, while a negative delay value indicates that the Marker
    Event occurs before the analog data. The default value is zero, which
    aligns the Marker Event with the analog output.

    You can specify the units of the delay value using the `Marker Event
    Delay Units <pniFgen_MarkerEventDelayUnits.html>`__ property.

    **Default Value**: 0
    '''
    marker_event_delay_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MarkerEventDelayUnits, 1150355)
    '''
    Specifies the units used for the `Marker Event Delay
    Value <pniFgen_MarkerEventDelayValue.html>`__ property.
    '''
    marker_event_latched_status = attributes.AttributeViBoolean(1150350)
    '''
    Specifies the latched status of the specified Marker Event. Set this
    property to FALSE to clear the latched status of the Marker Event.
    '''
    marker_event_live_status = attributes.AttributeViBoolean(1150345)
    '''
    Returns TRUE if the status of the specified Marker Event is live, and
    FALSE otherwise.
    '''
    marker_event_output_behavior = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MarkerEventOutputBehavior, 1150342)
    '''
    Specifies the output behavior for the Marker Event.
    '''
    marker_event_output_terminal = attributes.AttributeViString(1150312)
    '''
    Specifies the destination terminal for the Marker Event.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.
    '''
    marker_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MarkerEventPulsePolarity, 1150313)
    '''
    Specifies the output polarity of the Marker Event.
    '''
    marker_event_pulse_width = attributes.AttributeViReal64(1150340)
    '''
    Specifies the pulse width value of the Marker Event. Set the units for
    the values with the `Marker Event Pulse Width
    Units <pniFgen_MarkerEventPulseWidthUnits.html>`__ property.
    '''
    marker_event_pulse_width_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MarkerEventPulseWidthUnits, 1150341)
    '''
    Specifies the pulse width units of the Marker Event.
    '''
    marker_event_toggle_initial_state = attributes.AttributeEnum(attributes.AttributeViInt32, enums.MarkerEventToggleInitialState, 1150343)
    '''
    Specifies the initial state of the Marker Event.
    '''
    max_freq_list_duration = attributes.AttributeViReal64(1150213)
    '''
    Returns the maximum duration, in seconds, of any one step in the
    frequency list.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    max_freq_list_length = attributes.AttributeViInt32(1150211)
    '''
    Returns the maximum number of steps that can be in a frequency list.
    '''
    max_loop_count = attributes.AttributeViInt32(1250215)
    '''
    Returns the maximum number of times the signal generator can repeat a
    waveform in a sequence. Typically, this value is constant for the signal
    generator.
    '''
    max_num_freq_lists = attributes.AttributeViInt32(1150209)
    '''
    Returns the maximum number of frequency lists that the signal generator
    allows.
    '''
    max_num_sequences = attributes.AttributeViInt32(1250212)
    '''
    Returns the maximum number of arbitrary sequences the signal generator
    allows.
    '''
    max_num_waveforms = attributes.AttributeViInt32(1250205)
    '''
    Returns the maximum number of arbitrary waveforms that the signal
    generator allows. On some signal generators, this value may vary with
    remaining onboard memory.
    '''
    max_sequence_length = attributes.AttributeViInt32(1250214)
    '''
    Returns the maximum number of arbitrary waveforms the signal generator
    allows in a sequence.
    '''
    max_waveform_size = attributes.AttributeViInt32(1250208)
    '''
    Returns the maximum number of points the signal generator allows in an
    arbitrary waveform. On some signal generators, this value may vary with
    remaining onboard memory.
    '''
    memory_size = attributes.AttributeViInt32(1150242)
    '''
    Returns the amount of memory in bytes on the signal generator.
    '''
    minor_version = attributes.AttributeViInt32(1050504)
    '''
    Returns the minor version number of NI-FGEN.
    '''
    min_freq_list_duration = attributes.AttributeViReal64(1150212)
    '''
    Returns the minimum duration, in seconds, of any one step in a frequency
    list.
    '''
    min_freq_list_length = attributes.AttributeViInt32(1150210)
    '''
    Returns the minimum number of frequency lists that the signal generator
    allows.
    '''
    min_sequence_length = attributes.AttributeViInt32(1250213)
    '''
    Returns the minimum number of arbitrary waveforms the signal generator
    allows in a sequence. Typically, this value is constant for the signal
    generator.
    '''
    min_waveform_size = attributes.AttributeViInt32(1250207)
    '''
    Returns the minimum number of points the signal generator allows in an
    arbitrary waveform. Typically, this value is constant for the signal
    generator.

    Note:
    In some cases, you may need to supply a larger waveform than the value
    specified by this property. Refer to the "Features Supported" topic for
    your device in the *NI Signal Generators Help* for a table of minimum
    waveform sizes.
    '''
    module_revision = attributes.AttributeViString(1150390)
    '''
    Returns the revision letter of the module you are using.
    '''
    offset_dac_value = attributes.AttributeViInt32(1150224)
    '''
    Specifies the value programmed to the Offset DAC. The value should be
    treated as an unsigned, right-justified number.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    operation_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OperationMode, 1250005)
    '''
    Specifies how the signal generator produces waveforms. NI signal
    generators currently support only one value:
    **NIFGEN_VAL_OPERATE_CONTINUOUS**. To control trigger mode, set the
    `Trigger Mode <pniFgen_TriggerMode.html>`__ property.
    '''
    oscillator_freq_dac_value = attributes.AttributeViInt32(1150225)
    '''
    Specifies the value programmed to the Oscillator DAC. The value should
    be treated as an unsigned, right-justified number.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    oscillator_phase_dac_value = attributes.AttributeViInt32(1150232)
    '''
    Specifies the oscillator phase DAC value.
    '''
    osp_carrier_enabled = attributes.AttributeViBoolean(1150249)
    '''
    Enables (TRUE) or disables (FALSE) generation of the carrier.
    '''
    osp_carrier_frequency = attributes.AttributeViReal64(1150250)
    '''
    Specifies the frequency of the generated carrier.
    '''
    osp_carrier_phase_i = attributes.AttributeViReal64(1150251)
    '''
    Specifies the I carrier phase, in degrees, at the first point of the
    generated signal.

    **Default Value**: 0.0
    '''
    osp_carrier_phase_q = attributes.AttributeViReal64(1150252)
    '''
    Specifies the Q carrier phase, in degrees, at the first point of the
    generated signal. This property is used only when the `Data Processing
    Mode <pniFgen_DataProcessingMode.html>`__ property is set to
    **Complex**.

    **Default Value**: -90.0
    '''
    osp_cic_filter_enabled = attributes.AttributeViBoolean(1150257)
    '''
    Enables (TRUE) or disables (FALSE) the CIC filter.

    Note:
    You must set the CIC Filter Enabled and `FIR Filter
    Enabled <pniFgen_FIRFilterEnabled.html>`__ properties to the same value.
    '''
    osp_cic_filter_gain = attributes.AttributeViReal64(1150263)
    '''
    Specifies the gain applied at the final stage of the CIC filter. This
    property is commonly used to compensate for attenuation in the FIR
    filter. If you set the `FIR Filter Type <pniFgen_FilterType.html>`__ to
    a value other than **Custom**, NI-FGEN calculates the CIC gain to
    achieve unity gain between the FIR and CIC filters. Setting this
    property overrides the value set by NI-FGEN.
    '''
    osp_cic_filter_interpolation = attributes.AttributeViReal64(1150258)
    '''
    Specifies the interpolation factor for the CIC filter. If you do not set
    this value, NI-FGEN calculates the appropriate value based on the value
    of the `IQ Rate <pniFgen_IQRate.html>`__ property.
    '''
    osp_compensate_for_filter_group_delay = attributes.AttributeViBoolean(1150389)
    '''
    Adjusts for OSP filter group delay when aligning analog outputs and
    events in OSP mode. If you set this property to TRUE, event outputs
    align more closely with the analog output. The analog output also aligns
    more closely between two devices synchronized using NI-TClk.

    Note:
    Group delay is the delay that occurs as a result of passing through a
    FIR filter. At a low I/Q rate, the group delay can become so large that
    some devices may not be able to align the events with the output. In
    this case, you must increase the I/Q rate or disable this property.
    '''
    osp_data_processing_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.DataProcessingMode, 1150247)
    '''
    Controls the way that data is processed by the OSP block.

    Note:
    When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FGEN
    restricts this property value to Complex.
    '''
    osp_enabled = attributes.AttributeViBoolean(1150246)
    '''
    Enables (TRUE) or disables (FALSE) the OSP block of the signal
    generator. When the OSP block is disabled, all OSP-related properties
    are disabled and have no effect on the generated signal.
    '''
    osp_fir_filter_enabled = attributes.AttributeViBoolean(1150255)
    '''
    Specify TRUE to enables the FIR filter. Specify FALSE to disable the FIR
    filter.

    Note:
    You must set the `CIC Filter Enabled <pniFgen_CICFilterEnabled.html>`__
    property and the FIR Filter Enabled property to the same value.
    '''
    osp_fir_filter_flat_passband = attributes.AttributeViReal64(1150261)
    '''
    Specifies the passband value to use when calculating the FIR filter
    coefficients. The FIR filter is designed to be flat to passband × I/Q
    rate. This property is used only when the `Filter
    Type <pniFgen_FilterType.html>`__ property is set to **Flat**.
    '''
    osp_fir_filter_gaussian_bt = attributes.AttributeViReal64(1150262)
    '''
    Specifies the BT value to use when calculating the pulse-shaping FIR
    filter coefficients. The BT value is the product of the -3 dB bandwidth
    and the symbol period. This property is used only when the `Filter
    Type <pniFgen_FilterType.html>`__ property is set to **Gaussian**.
    '''
    osp_fir_filter_interpolation = attributes.AttributeViReal64(1150256)
    '''
    Specifies the interpolation factor for the FIR filter. If you do not set
    this value, NI-FGEN calculates the appropriate value based on the value
    of the `IQ Rate <pniFgen_IQRate.html>`__ property.
    '''
    osp_fir_filter_raised_cosine_alpha = attributes.AttributeViReal64(1150260)
    '''
    Specifies the alpha value to use when calculating the pulse-shaping FIR
    filter coefficients. This property is used only when the `Filter
    Type <pniFgen_FilterType.html>`__ property is set to **Raised Cosine**.
    '''
    osp_fir_filter_root_raised_cosine_alpha = attributes.AttributeViReal64(1150259)
    '''
    Specifies the alpha value to use when calculating the pulse-shaping FIR
    filter coefficients. This property is used only when the `Filter
    Type <pniFgen_FilterType.html>`__ property is set to **Root Raised
    Cosine**.
    '''
    osp_fir_filter_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.FilterType, 1150253)
    '''
    Specifies the pulse-shaping filter type for the FIR filter.
    '''
    osp_frequency_shift = attributes.AttributeViReal64(1150371)
    '''
    Specifies the amount of frequency shift applied to the baseband signal.

    Note:
    When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FGEN
    restricts this property value to 0.
    '''
    osp_iq_rate = attributes.AttributeViReal64(1150248)
    '''
    Specifies the rate at which the user-provided waveform data is generated
    when the `OSP Enabled <pniFgen_OSPEnabled.html>`__ property is set to
    TRUE.

    NI-FGEN sets the `Sample Rate <pniFgen_SampleRate.html>`__ property of
    the signal generator to the product of the IQ Rate, `FIR Interpolation
    Factor <pniFgen_FIRInterpolation.html>`__, and `CIC Interpolation
    Factor <pniFgen_CICInterpolation.html>`__ properties. When the `Data
    Processing Mode <pniFgen_DataProcessingMode.html>`__ property is set to
    **Real**, the IQ Rate value is the rate at which the signal generator
    processes real (I) data. When the Data Processing Mode property is set
    to **Complex**, the IQ Rate value is the rate at which the signal
    generator processes complex (I/Q) data.
    '''
    osp_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OSPMode, 1150370)
    '''
    Specifies the generation mode of the OSP, which determines the type of
    data contained in the output signal.

    For more information about the OSP modes your device supports, refer to
    `Devices <javascript:LaunchHelp('SigGenHelp.chm::/device_specific.html')>`__
    section of the *NI Signal Generators Help*.

    Note:
    When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FGEN
    restricts this property value to BaseBand.
    '''
    osp_overflow_error_reporting = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OSPOverflowErrorReporting, 1150268)
    '''
    Configures error reporting when the OSP block detects an overflow in any
    of its stages. Overflows lead to waveform clipping.

    You can use the `OSP Overflow Status <pniFgen_OSPOverflowStatus.html>`__
    property to query for overflow conditions regardless of the setting of
    the OSP Overflow Error Reporting property. The device continues to
    generate after an overflow regardless of the setting of the OSP Overflow
    Error Reporting property.
    '''
    osp_overflow_status = attributes.AttributeViInt32(1150269)
    '''
    Returns a bit field of the overflow status in any stage of the OSP
    block. This property is functional regardless of the value for the `OSP
    Overflow Error Reporting <pniFgen_OSPOverflowErrorReporting.html>`__
    property.

    Set this property to 0 to clear the current OSP overflow status.
    '''
    osp_pre_filter_gain_i = attributes.AttributeViReal64(1150264)
    '''
    Specifies the digital gain to apply to the I data stream before any
    filtering by the OSP block.

    **Valid Values**: -2.0 to 2.0

    **Default Value**: 1.0
    '''
    osp_pre_filter_gain_q = attributes.AttributeViReal64(1150265)
    '''
    Specifies the digital gain to apply to the Q data stream before any
    filtering by the OSP block. This property is used only when the `Data
    Processing Mode <pniFgen_DataProcessingMode.html>`__ property is set to
    **Complex**.

    **Valid Values**: -2.0 to 2.0

    **Default Value**: 1.0
    '''
    osp_pre_filter_offset_i = attributes.AttributeViReal64(1150266)
    '''
    Specifies the digital offset to apply to the I data stream. This offset
    is applied after the prefilter gain and before any filtering.

    **Valid Values**: -1.0 to 1.0

    **Default Value**: 0.9
    '''
    osp_pre_filter_offset_q = attributes.AttributeViReal64(1150267)
    '''
    Specifies the digital offset to apply to the Q data stream. This offset
    is applied after the prefilter gain and before any filtering. This
    property is only used when the `Data Processing
    Mode <pniFgen_DataProcessingMode.html>`__ property is set to
    **Complex**.

    **Valid Values**: -1.0 to 1.0

    **Default Value**: 0.0
    '''
    output_enabled = attributes.AttributeViBoolean(1250003)
    '''
    Specifies whether the signal that the signal generator produces appears
    at the output connector.
    '''
    output_impedance = attributes.AttributeViReal64(1250004)
    '''
    Specifies the output impedance of the signal generator at the output
    connector. NI signal generators have an output impedance of 50 ohms and
    an optional 75 ohms on select modules.

    If the `Load Impedance <pniFgen_LoadImpedance.html>`__ property value
    matches the output impedance, the voltage at the signal output connector
    is at the necessary level. The voltage at the signal output connector
    varies with load output impedance, up to doubling the voltage for a
    high-impedance load.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    output_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.OutputMode, 1250001)
    '''
    Specifies the output mode the signal generator uses. The output mode you
    specify determines which VIs and properties you use to configure the
    waveform the signal generator produces.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    p2p_data_transfer_permission_address = attributes.AttributeViInt64(1150398)
    '''
    Indicates the address in the writer peer to which the signal generator
    sends data transfer permission credits. This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    Note:
    You can use this property only when the `Manual Configuration
    Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
    TRUE.
    '''
    p2p_data_transfer_permission_address_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.P2PAddressType, 1150399)
    '''
    Specifies the type of address for the `Data Transfer Permission
    Address <pniFgen_DataTransferPermissionAddress.html>`__ property. This
    property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    **Default Value**: **Virtual**

    Note:
    You can only use this property when the `Manual Configuration
    Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
    TRUE.
    '''
    p2p_data_transfer_permission_initial_credits = attributes.AttributeViInt32(1150408)
    '''
    Specifies the initial amount of data, in samples per channel, that the
    writer peer is allowed to transfer over the bus into the configured
    endpoint when the peer-to-peer data stream is enabled. If you do not set
    this property and the endpoint is empty, credits equal to the full size
    of the endpoint are issued to the writer peer. If data has been written
    to the endpoint using the `niFgen Write P2P Endpoint
    I16 <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_P2P_Endpoint_I16.html')>`__
    VI prior to enabling the stream, credits equal to the remaining space
    available in the endpoint are issued to the writer peer. This property
    is coerced up by NI-FGEN to 8-byte boundaries.
    '''
    p2p_data_transfer_permission_interval = attributes.AttributeViInt32(1150400)
    '''
    Specifies the interval, in samples per channel, at which the signal
    generator issues credits to allow the writer peer to transfer data over
    the bus into the configured endpoint. Refer to the `Flow
    Control <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Flow_Control.html')>`__
    topic in the *NI Signal Generators Help* for more information. This
    property is coerced up by NI-FGEN to the nearest 128-byte boundary. This
    property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    **Default Value**: 1,024
    '''
    p2p_destination_channels = attributes.AttributeViString(1150392)
    '''
    Specifies which channels are written to by a peer-to-peer endpoint. If
    multiple channels are specified, data is deinterleaved to each channel.
    Channels are configured using the `niFgen Configure
    Channels <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Configure_Channels.html')>`__
    VI. This property is `endpoint
    based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    **Default Value**: "" (empty string), all channels are configured
    '''
    p2p_done_notification_address = attributes.AttributeViInt64(1150405)
    '''
    Returns the signal generator address to which the writer peer sends the
    `Done Notification Value <pniFgen_DoneNotificationValue.html>`__. This
    property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
    Refer to the `Stopping a Peer-to-Peer
    Generation <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Stopping_Generation.html')>`__
    topic in the *NI Signal Generators Help* for more information about
    using Done Notifications.

    Note:
    You can only use this property when the `Manual Configuration
    Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
    TRUE.
    '''
    p2p_done_notification_address_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.P2PAddressType, 1150406)
    '''
    Specifies the address type of the `Done Notification
    Address <pniFgen_DoneNotificationAddress.html>`__ property. This
    property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
    Refer to the `Stopping a Peer-to-Peer
    Generation <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Stopping_Generation.html')>`__
    topic in the *NI Signal Generators Help* for more information about
    using Done Notifications.

    Default Value: **Virtual**

    Note:
    You can only use this property when the `Manual Configuration
    Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
    TRUE.
    '''
    p2p_done_notification_value = attributes.AttributeViInt32(1150407)
    '''
    Returns the value the writer peer writes to the address specified by the
    `Done Notification Address <pniFgen_DoneNotificationAddress.html>`__
    property. This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
    Refer to the `Stopping a Peer-to-Peer
    Generation <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Stopping_Generation.html')>`__
    topic in the *NI Signal Generators Help* for more information about
    using Done Notifications.

    Note:
    You can only use this property when the `Manual Configuration
    Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
    TRUE.
    '''
    p2p_enabled = attributes.AttributeViBoolean(1150391)
    '''
    Specifies whether the signal generator reads data from the peer-to-peer
    endpoint (TRUE) instead of reading it from the onboard memory. This
    property is `endpoint
    based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    **Default Value**: FALSE
    '''
    p2p_endpoint_count = attributes.AttributeViInt32(1150396)
    '''
    Returns the number of peer-to-peer FIFO endpoints supported by the
    device.
    '''
    p2p_endpoint_fullness_start_trigger_level = attributes.AttributeViInt32(1150410)
    '''
    Specifies the number of samples the endpoint needs to receive before the
    signal generator starts generation. This property applies only when the
    `Start Trigger Type <pniFgen_StartTriggerType.html>`__ property is set
    to **P2P Endpoint Fullness**. Refer to the `Flow
    Control <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Flow_Control.html')>`__
    topic in the *NI Signal Generators Help* for more information about
    peer-to-peer operations. This property is coerced down to 8-byte
    boundaries.

    Note:
    Due to an additional internal FIFO in the signal generator, the writer
    peer actually must write 2,304 bytes more than the quantity of data
    specified by this property to satisfy the trigger level.
    '''
    p2p_endpoint_size = attributes.AttributeViInt32(1150393)
    '''
    Returns the size, in samples per channel, of the peer-to-peer endpoint.
    This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
    '''
    p2p_endpoint_window_address = attributes.AttributeViInt64(1150401)
    '''
    Returns the signal generator address where endpoint data is sent by the
    writer peer. The type of this address is specified by the `Endpoint
    Window Address Type <pniFgen_EndpointWindowAddressType.html>`__
    property. This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    Note:
    You can only use this property when the `Manual Configuration
    Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
    TRUE.
    '''
    p2p_endpoint_window_address_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.P2PAddressType, 1150402)
    '''
    Specifies the type of the `Endpoint Window
    Address <pniFgen_EndpointWindowAddress.html>`__ property. This property
    is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    **Default Value**: **Virtual**

    Note:
    You can only use this property when the `Manual Configuration
    Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
    TRUE.
    '''
    p2p_endpoint_window_size = attributes.AttributeViInt32(1150403)
    '''
    Returns the size, in bytes, of the endpoint window. The endpoint window
    is also described by the `Endpoint Window
    Address <pniFgen_EndpointWindowAddress.html>`__ property and the
    `Endpoint Window Address
    Type <pniFgen_EndpointWindowAddressType.html>`__ property. This property
    is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    Note:
    You can only use this property when the `Manual Configuration
    Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
    TRUE.
    '''
    p2p_manual_configuration_enabled = attributes.AttributeViBoolean(1150397)
    '''
    Enables (TRUE) or disables (FALSE) manual configuration for a
    peer-to-peer endpoint. Enabling this property disables automatic NI-P2P
    stream manager flow control and Done Notifications.
    '''
    p2p_most_space_available_in_endpoint = attributes.AttributeViInt32(1150395)
    '''
    Returns the largest number of samples per channel available in the
    endpoint since this property was last read. This property can be used to
    determine how much endpoint space to use as a buffer against PCI Express
    bus traffic latencies by reading the property and keeping track of the
    largest value returned. This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    If you want to minimize the latency for data to move through the
    endpoint and be generated by the signal generator, use the `Data
    Transfer Permission Initial
    Credits <pniFgen_DataTransferPermissionInitialCredits.html>`__ property
    to grant fewer initial credits than the default of the entire endpoint
    size.
    '''
    p2p_space_available_in_endpoint = attributes.AttributeViInt32(1150394)
    '''
    Returns the current space available in the endpoint in samples per
    channel. You can use this property when priming the endpoint with
    initial data through the `niFgen Write P2P Endpoint
    I16 <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_P2P_Endpoint_I16.html')>`__
    VI to determine how many samples you can write. You also can use this
    property to characterize the performance and measure the latency of the
    peer-to-peer stream as data moves across the bus. This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
    '''
    pci_dma_optimizations_enabled = attributes.AttributeViBoolean(1150362)
    '''
    Controls whether NI-FGEN allows performance optimizations for DMA
    transfers. This property is only valid for PCI and PXI SMC-based
    devices. This property is enabled (TRUE) by default, and NI recommends
    leaving it enabled.

    **Default Value**: TRUE

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    post_amplifier_attenuation = attributes.AttributeViReal64(1150229)
    '''
    Specifies the amount of post-amplifier attenuation to apply to the
    signal, in dB.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    pre_amplifier_attenuation = attributes.AttributeViReal64(1150228)
    '''
    Specifies the amount of preamplifier attenuation to apply to the signal,
    in dB.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    primary_error = attributes.AttributeViInt32(1050101)
    '''
    Describes the first error that occurred since the last call to the
    `niFgen Error
    Message <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Error_Message.html')>`__
    VI on the session.

    The value follows the VXIplug&play completion code conventions. A
    negative value (0x80000000 or higher in hex) describes an error
    condition. A positive value describes a warning condition and indicates
    that no error occurred. A zero indicates that no error or warning
    occurred. The error and warning values can be status codes defined by
    IVI, VISA, class drivers, or specific drivers.
    '''
    query_instrument_status = attributes.AttributeViBoolean(1050003)
    '''
    Specifies whether NI-FGEN retains instrument status after each
    operation. Set this property to TRUE to query the instrument status.

    Querying the instrument status is very useful for debugging. After you
    validate your program, you can set this property to FALSE to disable
    status checking and maximize performance. However, the effect on NI-FGEN
    is minor.

    NI-FGEN can choose to ignore status checking for particular properties
    regardless of the setting of this property. Use the `niFgen Initialize
    With
    Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
    VI to override this value.

    **Default Value**: TRUE
    '''
    range_check = attributes.AttributeViBoolean(1050002)
    '''
    Specifies whether to validate property values and VI parameters. Set
    this property to TRUE to enable range-checking.

    If enabled, in some cases, NI-FGEN does extra validation of parameter
    values that you pass to NI-FGEN VIs. Range checking parameters is useful
    for debugging. After you validate your program, you can set this
    property to FALSE to disable range checking and maximize performance.

    Use the `niFgen Initialize With
    Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
    VI to override the value of this property.

    **Default Value**: TRUE
    '''
    ready_for_start_event_level_active_level = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ReadyForStartEventActiveLevel, 1150311)
    '''
    Specifies the output polarity of the Ready for Start Event.
    '''
    ready_for_start_event_live_status = attributes.AttributeViBoolean(1150348)
    '''
    Returns TRUE if the status of the specified Ready for Start Event is
    live, and FALSE otherwise.
    '''
    ready_for_start_event_output_terminal = attributes.AttributeViString(1150310)
    '''
    Specifies the destination terminal for the Ready for Start Event. For a
    list of the terminals available on your device, refer to the Routes
    topic for your device or the **Device Routes** tab in MAX.
    '''
    record_coercions = attributes.AttributeViBoolean(1050006)
    '''
    Specifies whether the IVI engine keeps a list of the value coercions it
    makes for ViInt32 and ViReal64 properties. Set this property to TRUE to
    record the coercions. Use the `niFgen Initialize With
    Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
    VI to override this value.

    **Default Value**: FALSE
    '''
    reference_clock_source = attributes.AttributeEnum(attributes.AttributeViString, enums.ReferenceClockSource, 1150113)
    '''
    Specifies the Reference Clock source used by the signal generator.

    The signal generator derives the frequencies and sample rates that it
    uses to generate waveforms from the source you specify. For example,
    when you set this property to **Clock In**, the signal generator uses
    the signal it receives at its CLK In front panel connector as its
    Reference Clock.

    Note:
    The signal generator must not be in the Generating state when you change
    this property. To change the device configuration, call the `niFgen
    Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    ref_clock_frequency = attributes.AttributeViReal64(1150107)
    '''
    Specifies the Reference Clock frequency. The signal generator uses the
    Reference Clock to derive frequencies and sample rates when generating
    output.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    ref_clock_source = attributes.AttributeViInt32(1250002)
    '''
    Controls the Reference Clock source the signal generator uses.

    The signal generator derives the frequencies and sample rates that it
    uses to generate waveforms from the source you specify. For example,
    when you set this attribute to **Clock In**, the signal generator uses
    the signal it receives at the Clk In front panel connector as its
    Reference Clock.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    sample_clock_absolute_delay = attributes.AttributeViReal64(1150231)
    '''
    Specifies the delay in seconds to apply to an external Sample Clock.
    This property is useful when trying to align the output of two devices.

    Note:
    For the NI 5421, absolute delay can only be applied when an external
    Sample Clock is used.
    '''
    sample_clock_source = attributes.AttributeEnum(attributes.AttributeViString, enums.SampleClockSource, 1150112)
    '''
    Specifies the Sample Clock source.

    Note:
    The signal generator must not be in the Generating state when you change
    this property. To change the device configuration, call the `niFgen
    Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    sample_clock_timebase_rate = attributes.AttributeViReal64(1150368)
    '''
    Specifies the Sample Clock Timebase rate. This property applies only to
    external Sample Clock timebases.

    Note:
    The signal generator must not be in the Generating state when you change
    this property. To change the device configuration, call the `niFgen
    Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    sample_clock_timebase_source = attributes.AttributeEnum(attributes.AttributeViString, enums.SampleClockTimebaseSource, 1150367)
    '''
    Specifies the Sample Clock Timebase source.

    Note:
    The signal generator must not be in the Generating state when you change
    this property. To change the device configuration, call the `niFgen
    Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    script_to_generate = attributes.AttributeViString(1150270)
    '''
    Specifies which script the signal generator uses. To configure the
    signal generator to run a particular script, set this property to the
    name of the script.

    Use the `niFgen Write
    Script <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_Script.html')>`__
    VI to create multiple scripts. Use this property when the `Output
    Mode <pniFgen_OutputMode.html>`__ property is set to
    **NIFGEN_VAL_OUTPUT_SCRIPT**.

    Note:
    The signal generator must not be in the Generating state when you change
    this property. To change the device configuration, call the `niFgen
    Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    script_triggers_count = attributes.AttributeViInt32(1150272)
    '''
    Returns the number of Script Triggers supported by the device. Use this
    property when the `Output Mode <pniFgen_OutputMode.html>`__ property is
    set to **NIFGEN_VAL_OUTPUT_SCRIPT**.
    '''
    script_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ScriptTriggerType, 1150290)
    '''
    Specifies the Script trigger type. Depending upon the value of this
    property, additional properties may be needed to fully configure the
    trigger.
    '''
    secondary_error = attributes.AttributeViInt32(1050102)
    '''
    Provides an optional code with additional information concerning the
    primary error condition. The error and warning values can be status
    codes defined by IVI, VISA, class drivers, or specific drivers. Zero
    indicates no additional information.
    '''
    serial_number = attributes.AttributeViString(1150243)
    '''
    Returns the serial number of the signal generator.
    '''
    simulate = attributes.AttributeViBoolean(1050005)
    '''
    Specifies whether or not to simulate NI-FGEN I/O operations. Set this
    property to TRUE to enable simulation.

    If simulation is enabled, NI-FGEN VIs perform range checking and can get
    and set properties, but they do not perform instrument I/O. For output
    parameters that represent instrument data, NI-FGEN VIs return calculated
    values.

    Use the `niFgen Initialize With
    Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
    VI to override the value of this property.

    **Default Value**: FALSE
    '''
    specific_driver_class_spec_major_version = attributes.AttributeViInt32(1050515)
    '''
    Returns the major version number of the class specification with which
    NI-FGEN is compliant.
    '''
    specific_driver_class_spec_minor_version = attributes.AttributeViInt32(1050516)
    '''
    Returns the minor version number of the class specification with which
    NI-FGEN is compliant.
    '''
    specific_driver_description = attributes.AttributeViString(1050514)
    '''
    Contains a brief description of the specific driver.
    '''
    specific_driver_prefix = attributes.AttributeViString(1050302)
    '''
    Contains the prefix for NI-FGEN. The name of each user-callable VI in
    NI-FGEN starts with this prefix.
    '''
    specific_driver_revision = attributes.AttributeViString(1050551)
    '''
    Contains additional version information about NI-FGEN.
    '''
    specific_driver_vendor = attributes.AttributeViString(1050513)
    '''
    Contains the name of the vendor that supplies NI-FGEN.
    '''
    started_event_delay = attributes.AttributeViReal64(1150356)
    '''
    Specifies the amount of delay applied to a Started Event with respect to
    the analog output of the signal generator.

    A positive delay value indicates that the Started Event occurs after the
    analog data, while a negative delay value indicates that the Started
    Event occurs before the analog data. The default value is zero, which
    aligns the Started Event with the analog output.

    You can specify the units of the delay value by setting the `Started
    Event Delay Units <pniFgen_StartedEventDelayUnits.html>`__ property.

    **Default Value**: 0
    '''
    started_event_delay_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartedEventDelayUnits, 1150357)
    '''
    Specifies the units used for the `Started Event Delay
    Value <pniFgen_StartedEventDelayValue.html>`__ property.
    '''
    started_event_latched_status = attributes.AttributeViBoolean(1150352)
    '''
    Returns the latched status of the specified Started Event.
    '''
    started_event_level_active_level = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartedEventActiveLevel, 1150316)
    '''
    Specifies the output polarity of the Started Event.
    '''
    started_event_output_behavior = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartedEventOutputBehavior, 1150331)
    '''
    Specifies the output behavior for the Started Event.
    '''
    started_event_output_terminal = attributes.AttributeViString(1150314)
    '''
    Specifies the destination terminal for the Started Event. For a list of
    the terminals available on your device, refer to the Routes topic for
    your device or the **Device Routes** tab in MAX.
    '''
    started_event_pulse_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartedEventPulsePolarity, 1150318)
    '''
    Specifies the output polarity of the Started Event.
    '''
    started_event_pulse_width = attributes.AttributeViReal64(1150335)
    '''
    Specifies the pulse width value for the Started Event.
    '''
    started_event_pulse_width_units = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartedEventPulseWidthUnits, 1150333)
    '''
    Specifies the pulse width units for the Started Event.
    '''
    start_trigger_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.StartTriggerType, 1150280)
    '''
    Specifies the type of Start Trigger you want to use.
    '''
    streaming_space_available_in_waveform = attributes.AttributeViInt32(1150325)
    '''
    Returns the space available in the streaming waveform for writing new
    data.

    Use this property in conjunction with the `Streaming Waveform
    Handle <pniFgen_StreamingWaveformHandle.html>`__ property or the
    `Streaming Waveform Name <pniFgen_StreamingWaveformName.html>`__
    property.
    '''
    streaming_waveform_handle = attributes.AttributeViInt32(1150324)
    '''
    Specifies the waveform handle of the waveform used to continuously
    stream data during generation.

    This property is used in conjunction with the `Space Available in
    Streaming Waveform <pniFgen_SpaceAvailInStreamingWfm.html>`__ property.

    **Default Value**: -1

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    streaming_waveform_name = attributes.AttributeViString(1150326)
    '''
    Specifies the name of the waveform used to continuously stream data
    during generation. This property defaults to an empty string when no
    streaming waveform is specified.

    Use this property in conjunction with the `Space Available in Streaming
    Waveform <pniFgen_SpaceAvailInStreamingWfm.html>`__ property.

    **Default Value**: ""

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    streaming_write_timeout = attributes.AttributeViReal64(1150409)
    '''
    Specifies the maximum amount of time allowed to complete a streaming
    write operation.

    **Units**: seconds (s)
    '''
    supported_instrument_models = attributes.AttributeViString(1050327)
    '''
    Returns a model code of the instrument. For drivers that support more
    than one device, this property contains a comma-separated list of
    supported instrument models.
    '''
    synchronization = attributes.AttributeEnum(attributes.AttributeViInt32, enums.SynchronizationSource, 1150111)
    '''
    Specifies the source of the synchronization signal to use.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    sync_duty_cycle_high = attributes.AttributeViReal64(1150105)
    '''
    Specifies the duty cycle of the square wave the signal generator
    produces on the SYNC OUT connector. Specify this property as a
    percentage of the time the square wave is high in each cycle.

    **Units**: Percentage of time the waveform is high

    **Default Value**: 50%
    '''
    sync_out_output_terminal = attributes.AttributeViString(1150330)
    '''
    Specifies the terminal at which to export the SYNC OUT signal. This
    property is not supported for all devices. For a list of the terminals
    available on your device, refer to the Routes topic for your device or
    the **Device Routes** tab in MAX.
    '''
    terminal_configuration = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TerminalConfiguration, 1150365)
    '''
    Specifies whether to analyze gain and offset values based on
    single-ended or
    `differential <javascript:LaunchHelp('SigGenHelp.chm::/fund_differential_output.html')>`__
    operation.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    trigger_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerMode, 1150108)
    '''
    Controls the trigger mode.

    **Default Value**: **NIFGEN_VAL_CONTINUOUS**
    '''
    trigger_source = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerSource, 1250302)
    '''
    Specifies which trigger source the signal generator uses.

    After you call the `niFgen Initiate
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initiate_Generation.html')>`__
    VI, the signal generator waits for the trigger you specify in this
    parameter. After it receives a trigger, the signal generator produces
    the number of cycles you specify in the `Repeat
    Count <pniFgen_ArbWfm.RepeatCount.html>`__ property.

    The value you select for this property is also the source for the
    trigger in the other trigger modes as specified by the `Trigger
    Mode <pniFgen_TriggerMode.html>`__ property.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    update_clock_source = attributes.AttributeEnum(attributes.AttributeViInt32, enums.UpdateClockSource, 1150106)
    '''
    Controls the Update Clock source.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    video_waveform_type = attributes.AttributeEnum(attributes.AttributeViInt32, enums.VideoWaveformType, 1150216)
    '''
    Specifies the waveform type the NI 5431 generates. Setting this property
    ensures the oscillator crystal is set to the proper frequency.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    wait_behavior = attributes.AttributeEnum(attributes.AttributeViInt32, enums.WaitBehavior, 1150379)
    '''
    Specifies the behavior of the output while waiting for a Script Trigger
    or during a wait instruction.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    wait_value = attributes.AttributeViInt32(1150380)
    '''
    Specifies the value to generate while waiting. You must set the `Wait
    Behavior <pniFgen_WaitBehavior.html>`__ property to **Jump To Value** to
    use this property.

    Note:
    You cannot change this property while the device is generating a
    waveform. If you want to change the device configuration, call the
    `niFgen Abort
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
    VI or wait for the generation to complete.
    '''
    waveform_quantum = attributes.AttributeViInt32(1250206)
    '''
    Returns the quantum value the signal generator allows. The size of each
    arbitrary waveform must be a multiple of this quantum value.

    For example, when this property returns a value of 8, all waveform sizes
    must be a multiple of 8. Typically, this value is constant for the
    signal generator.
    '''

    def __init__(self, repeated_capability):
        self._library = library_singleton.get()
        self._repeated_capability = repeated_capability
        self._encoding = 'windows-1251'

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
            waveform_name (string): Specifies the name to associate with the allocated waveform.
            waveform_size (int): Specifies the size of the waveform to allocate in samples.

                **Default Value**: "4096"
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case 3
        waveform_size_ctype = visatype.ViInt32(waveform_size)  # case 8
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_size_ctype = visatype.ViInt32(waveform_size)  # case 8
        waveform_handle_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_AllocateWaveform(vi_ctype, channel_name_ctype, waveform_size_ctype, ctypes.pointer(waveform_handle_ctype))
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        error_code = self._library.niFgen_ClearUserStandardWaveform(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_arb_sequence(self, sequence_handle, gain, offset):
        '''configure_arb_sequence

        Configures the signal generator attributes that affect arbitrary
        sequence generation. Sets the ARB_SEQUENCE_HANDLE,
        ARB_GAIN, and ARB_OFFSET attributes.

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
                ARB_SEQUENCE_HANDLE attribute to this value. You can
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
                ARB_OFFSET attribute to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        sequence_handle_ctype = visatype.ViInt32(sequence_handle)  # case 8
        gain_ctype = visatype.ViReal64(gain)  # case 8
        offset_ctype = visatype.ViReal64(offset)  # case 8
        error_code = self._library.niFgen_ConfigureArbSequence(vi_ctype, channel_name_ctype, sequence_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_arb_waveform(self, waveform_handle, gain, offset):
        '''configure_arb_waveform

        Configures the attributes of the signal generator that affect arbitrary
        waveform generation. Sets the ARB_WAVEFORM_HANDLE,
        ARB_GAIN, and ARB_OFFSET attributes.

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
                ARB_WAVEFORM_HANDLE attribute to this value. You can
                create an arbitrary waveform using one of the following niFgen Create
                Waveform functions:

                -  create_waveform_f64
                -  create_waveform_i16
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64
                -  CreateWaveformFromFileHWS

                These functions return a handle that you use to identify the waveform.

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
                ARB_OFFSET attribute to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_handle_ctype = visatype.ViInt32(waveform_handle)  # case 8
        gain_ctype = visatype.ViReal64(gain)  # case 8
        offset_ctype = visatype.ViReal64(offset)  # case 8
        error_code = self._library.niFgen_ConfigureArbWaveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_custom_fir_filter_coefficients(self, number_of_coefficients, coefficients_array):
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

            session['0,1'].configure_custom_fir_filter_coefficients(number_of_coefficients, coefficients_array)

        Args:
            number_of_coefficients (int): Specifies the number of coefficients. The NI 5441 requires 95.
            coefficients_array (list of float): Specifies the array of data the onboard signal processor uses for the
                FIR filter coefficients. For the NI 5441, provide a symmetric array of
                95 coefficients to this parameter. The array must have at least as many
                elements as the value that you specify in the **numberOfCoefficients**
                parameter in this function.
                The coefficients should range between –1.00 and +1.00.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        number_of_coefficients_ctype = visatype.ViInt32(number_of_coefficients)  # case 8
        coefficients_array_ctype = (visatype.ViReal64 * len(coefficients_array))(*coefficients_array)  # case 4
        error_code = self._library.niFgen_ConfigureCustomFIRFilterCoefficients(vi_ctype, channel_name_ctype, number_of_coefficients_ctype, coefficients_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_standard_waveform(self, waveform, amplitude, dc_offset, frequency, start_phase):
        '''configure_standard_waveform

        Configures the following attributes of the signal generator that affect
        standard waveform generation:

        -  FUNC_WAVEFORM
        -  FUNC_AMPLITUDE
        -  FUNC_DC_OFFSET
        -  FUNC_FREQUENCY
        -  FUNC_START_PHASE

        Note:
        You must call the ConfigureOutputMode function with the
        **outputMode** parameter set to NIFGEN_VAL_OUTPUT_FUNC before calling
        this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].configure_standard_waveform(waveform, amplitude, dc_offset, frequency, start_phase)

        Args:
            waveform (int): Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the FUNC_WAVEFORM attribute to this
                value.

                ****Defined Values****

                **Default Value**: NIFGEN_VAL_WFM_SINE

                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_SINE      | Specifies that the signal generator produces a sinusoid waveform.                                                                    |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_SQUARE    | Specifies that the signal generator produces a square waveform.                                                                      |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_TRIANGLE  | Specifies that the signal generator produces a triangle waveform.                                                                    |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_RAMP_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                               |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_RAMP_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                               |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_DC        | Specifies that the signal generator produces a constant voltage.                                                                     |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_NOISE     | Specifies that the signal generator produces white noise.                                                                            |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_USER      | Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform function. |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
            amplitude (float): Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the FUNC_AMPLITUDE attribute to
                this value.

                For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
                the amplitude to 10.00 V.

                **Units**: peak-to-peak voltage

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                function to NIFGEN_VAL_WFM_DC.
            dc_offset (float): Specifies the DC offset of the standard waveform that you want the
                signal generator to produce. The value is the offset from ground to the
                center of the waveform you specify with the **waveform** parameter,
                observed at the output terminal. For example, to configure a waveform
                with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
                **dcOffset** to 5.00 V. NI-FGEN sets the FUNC_DC_OFFSET
                attribute to this value.

                **Units**: volts

                **Default Value**: None
            frequency (float): | Specifies the frequency of the standard waveform that you want the
                  signal generator to produce. NI-FGEN sets the
                  FUNC_FREQUENCY attribute to this value.

                **Units**: hertz

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                function to NIFGEN_VAL_WFM_DC.
            start_phase (float): Specifies the horizontal offset of the standard waveform that you want
                the signal generator to produce. Specify this parameter in degrees of
                one waveform cycle. NI-FGEN sets the FUNC_START_PHASE
                attribute to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: 0.00

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter to NIFGEN_VAL_WFM_DC.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_ctype = visatype.ViInt32(waveform)  # case 8
        amplitude_ctype = visatype.ViReal64(amplitude)  # case 8
        dc_offset_ctype = visatype.ViReal64(dc_offset)  # case 8
        frequency_ctype = visatype.ViReal64(frequency)  # case 8
        start_phase_ctype = visatype.ViReal64(start_phase)  # case 8
        error_code = self._library.niFgen_ConfigureStandardWaveform(vi_ctype, channel_name_ctype, waveform_ctype, amplitude_ctype, dc_offset_ctype, frequency_ctype, start_phase_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_waveform_f64(self, waveform_size, waveform_data_array):
        '''create_waveform_f64

        Creates an onboard waveform from binary F64 (floating point double) data
        for use in Arbitrary Waveform output mode or Arbitrary Sequence output
        mode. The **waveformHandle** returned can later be used for setting the
        active waveform, changing the data in the waveform, building sequences
        of waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the nifgen_ConfigureOutputMode function to set the
        **outputMode** parameter to NIFGEN_VAL_OUTPUT_ARB or
        NIFGEN_VAL_OUTPUT_SEQ before calling this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].create_waveform_f64(waveform_size, waveform_data_array)

        Args:
            waveform_size (int): | Specifies the size of the arbitrary waveform that you want to create.
                | The size must meet the following restrictions:

                -  The size must be less than or equal to the maximum waveform size that
                   the device allows.
                -  The size must be greater than or equal to the minimum waveform size
                   that the device allows.
                -  The size must be an integer multiple of the device waveform quantum.

                You can obtain these values from the **maximumWaveformSize**,
                **minimumWaveformSize**, and **waveformQuantum** parameters of the
                nifgen_QueryArbWfmCapabilities function.

                | ****Default Value**:** None
            waveform_data_array (list of float): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None

        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_size_ctype = visatype.ViInt32(waveform_size)  # case 8
        waveform_data_array_ctype = (visatype.ViReal64 * len(waveform_data_array))(*waveform_data_array)  # case 4
        waveform_handle_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_CreateWaveformF64(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, ctypes.pointer(waveform_handle_ctype))
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
        DIGITAL_GAIN attribute to generate different voltage
        outputs.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].create_waveform_from_file_f64(file_name, byte_order)

        Args:
            file_name (string): The full path and name of the file where the waveform data resides.
            byte_order (int): Specifies the byte order of the data in the file.

                ****Defined Values****

                |
                | ****Default Value**:** NIFGEN_VAL_LITTLE_ENDIAN

                +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_LITTLE_ENDIAN | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
                +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_BIG_ENDIAN    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
                +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(self._encoding))  # case 3
        byte_order_ctype = visatype.ViInt32(byte_order)  # case 8
        waveform_handle_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_CreateWaveformFromFileF64(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, ctypes.pointer(waveform_handle_ctype))
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
        represent –1 to +1 V. Use the DIGITAL_GAIN attribute to
        generate different voltage outputs.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].create_waveform_from_file_i16(file_name, byte_order)

        Args:
            file_name (string): The full path and name of the file where the waveform data resides.
            byte_order (int): Specifies the byte order of the data in the file.

                ****Defined Values****

                |
                | ****Default Value**:** NIFGEN_VAL_LITTLE_ENDIAN

                +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_LITTLE_ENDIAN | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
                +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_BIG_ENDIAN    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
                +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(self._encoding))  # case 3
        byte_order_ctype = visatype.ViInt32(byte_order)  # case 8
        waveform_handle_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_CreateWaveformFromFileI16(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, ctypes.pointer(waveform_handle_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_waveform_i16(self, waveform_size, waveform_data_array):
        '''create_waveform_i16

        Creates an onboard waveform from binary 16-bit signed integer (I16) data
        for use in Arbitrary Waveform or Arbitrary Sequence output mode. The
        **waveformHandle** returned can later be used for setting the active
        waveform, changing the data in the waveform, building sequences of
        waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the nifgen_ConfigureOutputMode function to set the
        **outputMode** parameter to NIFGEN_VAL_OUTPUT_ARB or
        NIFGEN_VAL_OUTPUT_SEQ before calling this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].create_waveform_i16(waveform_size, waveform_data_array)

        Args:
            waveform_size (int): | Specifies the size of the arbitrary waveform that you want to create.
                | The size must meet the following restrictions:

                -  The size must be less than or equal to the maximum waveform size that
                   the device allows.
                -  The size must be greater than or equal to the minimum waveform size
                   that the device allows.
                -  The size must be an integer multiple of the device waveform quantum.

                You can obtain these values from the **maximumWaveformSize**,
                **minimumWaveformSize**, and **waveformQuantum** parameters of the
                nifgen_QueryArbWfmCapabilities function.

                |
                | ****Default Value**:** None
            waveform_data_array (list of int): Specify the array of data that you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in the Waveform Size parameter.
                You must normalize the data points in the array to be between -32768 and
                +32767.
                ****Default Value**:** None

        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_size_ctype = visatype.ViInt32(waveform_size)  # case 8
        waveform_data_array_ctype = (visatype.ViInt16 * len(waveform_data_array))(*waveform_data_array)  # case 4
        waveform_handle_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_CreateWaveformI16(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, ctypes.pointer(waveform_handle_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def define_user_standard_waveform(self, waveform_size, waveform_data_array):
        '''define_user_standard_waveform

        Defines a user waveform for use in either Standard Function or Frequency
        List output mode.

        To select the waveform, set the **waveform** parameter to
        NIFGEN_VAL_WFM_USER with either the nifgen_ConfigureStandardWaveform
        or the nifgen_CreateFreqList function.

        The waveform data must be scaled between –1.0 and 1.0. Use the
        **amplitude** parameter in the configure_standard_waveform
        function to generate different output voltages.

        Note:
        You must call the nifgen_ConfigureOutputMode function to set the
        **outputMode** parameter to NIFGEN_VAL_OUTPUT_FUNC or
        NIFGEN_VAL_OUTPUT_FREQ_LIST before calling this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].define_user_standard_waveform(waveform_size, waveform_data_array)

        Args:
            waveform_size (int): Specifies the size of the waveform in samples.
                **Default Value**: 16384
            waveform_data_array (list of float): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_size_ctype = visatype.ViInt32(waveform_size)  # case 8
        waveform_data_array_ctype = (visatype.ViReal64 * len(waveform_data_array))(*waveform_data_array)  # case 4
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
            waveform_name (string): Specifies the name to associate with the allocated waveform.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case 3
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
            script_name (string): Specifies the name of the script you want to delete. The script name
                appears in the text of the script following the script keyword.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        script_name_ctype = ctypes.create_string_buffer(script_name.encode(self._encoding))  # case 3
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViBoolean()  # case 13
        error_code = self._library.niFgen_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_int64(self, attribute_id):
        '''_get_attribute_vi_int64

        Queries the value of a ViInt64 attribute. You can use this function to
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

            session['0,1']._get_attribute_vi_int64(attribute_id)

        Args:
            attribute_id (int): Specifies the ID of an attribute.

        Returns:
            attribute_value (int): Returns the current value of the attribute. Pass the address of a
                ViInt64 variable.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViInt64()  # case 13
        error_code = self._library.niFgen_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViReal64()  # case 13
        error_code = self._library.niFgen_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
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
            array_size (int): Specifies the number of bytes in the ViChar array you specify for the
                **attributeValue** parameter.

                If the current value of the attribute, including the terminating NUL
                byte, contains more bytes than you indicate in this parameter, the
                function copies **arraySize** – 1 bytes into the buffer, places an ASCII
                NUL byte at the end of the buffer, and returns the array size you must
                pass to get the entire value. For example, if the value is 123456 and
                **arraySize** is 4, the function places 123 into the buffer and returns
                7.

                If you pass a negative number, the function copies the value to the
                buffer regardless of the number of bytes in the value.

                If you pass 0, you can pass VI_NULL for the **attributeValue** buffer
                parameter.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        array_size_ctype = visatype.ViInt32()  # case 6
        attribute_value_ctype = None  # case 11
        error_code = self._library.niFgen_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        attribute_value_ctype = (visatype.ViChar * array_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
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

        Args:
            error_description_buffer_size (int): Specifies the size of the **errorDescription** array.

                You can determine the array size needed to store the entire error
                description by setting this parameter to 0. The function then ignores
                the **errorDescription** buffer, which may be set to VI_NULL, and gives
                as its return value the required buffer size. You can then call the
                function a second time using the correct buffer size.

        Returns:
            error_code (int): The error code for the session or execution thread.

                A value of VI_SUCCESS (0) indicates that no error occurred. A positive
                value indicates a warning. A negative value indicates an error.

                You can call nifgen_error_message to get a text description of the
                value.

                If you are not interested in this value, you can pass VI_NULL.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code_ctype = visatype.ViStatus()  # case 13
        error_description_buffer_size_ctype = visatype.ViInt32()  # case 6
        error_description_ctype = None  # case 11
        error_code = self._library.niFgen_GetError(vi_ctype, ctypes.pointer(error_code_ctype), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_description_ctype = (visatype.ViChar * error_description_buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niFgen_GetError(vi_ctype, ctypes.pointer(error_code_ctype), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def get_fir_filter_coefficients(self, array_size, coefficients_array, number_of_coefficients_read):
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

            session['0,1'].get_fir_filter_coefficients(array_size, coefficients_array, number_of_coefficients_read)

        Args:
            array_size (int): Specifies the size of the coefficient array
            coefficients_array (list of float): Specifies the array of data the onboard signal processor uses for the
                FIR filter coefficients. For the NI 5441, provide a symmetric array of
                95 coefficients to this parameter. The array must have at least as many
                elements as the value that you specify in the **numberOfCoefficients**
                parameter in this function.
                The coefficients should range between –1.00 and +1.00.
            number_of_coefficients_read (list of int): Specifies the array of data containing the number of coefficients you
                want to read.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        array_size_ctype = visatype.ViInt32(array_size)  # case 8
        coefficients_array_ctype = (visatype.ViReal64 * len(coefficients_array))(*coefficients_array)  # case 4
        number_of_coefficients_read_ctype = (visatype.ViInt32 * len(number_of_coefficients_read))(*number_of_coefficients_read)  # case 4
        error_code = self._library.niFgen_GetFIRFilterCoefficients(vi_ctype, channel_name_ctype, array_size_ctype, coefficients_array_ctype, number_of_coefficients_read_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _initialize_with_channels(self, resource_name, reset_device, option_string):
        '''_initialize_with_channels

        Creates and returns a new NI-FGEN session to the specified channel of a
        waveform generator that is used in all subsequent NI-FGEN function
        calls.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1']._initialize_with_channels(resource_name, reset_device, option_string)

        Args:
            resource_name (string): Caution:
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
            option_string (string): Sets the initial value of certain session attributes.

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
                | RangeCheck       | RANGE_CHECK             | VI_TRUE, VI_FALSE |
                +------------------+-------------------------+-------------------+
                | QueryInstrStatus | QUERY_INSTRUMENT_STATUS | VI_TRUE, VI_FALSE |
                +------------------+-------------------------+-------------------+
                | Cache            | cache                   | VI_TRUE, VI_FALSE |
                +------------------+-------------------------+-------------------+
                | Simulate         | simulate                | VI_TRUE, VI_FALSE |
                +------------------+-------------------------+-------------------+

        Returns:
            vi (int): Returns a session handle that you can use to identify the device in all
                subsequent NI-FGEN function calls.
        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case 3
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        reset_device_ctype = visatype.ViBoolean(reset_device)  # case 8
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case 3
        vi_ctype = visatype.ViSession()  # case 13
        error_code = self._library.niFgen_InitializeWithChannels(resource_name_ctype, channel_name_ctype, reset_device_ctype, option_string_ctype, ctypes.pointer(vi_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def route_signal_out(self, route_signal_from, route_signal_to):
        '''route_signal_out

        Routes various signals in the signal generator to the RTSI lines and
        front panel terminals.

        +---+--------------------------------------------------------------------------------------------------+
        |   | You can clear a previously routed signal by routing NIFGEN_VAL_NONE to the destination terminal. |
        +---+--------------------------------------------------------------------------------------------------+
        |   | You can clear a previously routed signal by routing NIFGEN_VAL_NONE to the destination terminal. |
        +---+--------------------------------------------------------------------------------------------------+

        Note:
        The signal generator must not be in the Generating state when you call
        this function.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].route_signal_out(route_signal_from, route_signal_to)

        Args:
            route_signal_from (int): Various signals can be routed out the RTSI lines.

                ****Defined Values****

                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_NONE                    | Nothing Sending this value clears the line.                                                                                                                                                                                                                                                                     |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_MARKER                  | Marker Event                                                                                                                                                                                                                                                                                                    |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_SYNC_OUT                | SYNC signal This signal normally appears on the SYNC OUT front panel connector.                                                                                                                                                                                                                                 |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_OUT_START_TRIGGER       | Start Trigger The Start Trigger is normally generated at the start of the sequence. Call the nifgen_ConfigureTriggerSource function to receive this trigger.                                                                                                                                                    |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_BOARD_CLOCK             | Signal generator board clock The signal generator board clock is 20 MHz for the NI PCI-5401/5411/5431. The NI PXI-5404 has a 20 MHz board clock, and the NI PXI-5421 has integer divisors of 100 MHz. The NI PXI-5401/5411/5431 does not support routing a Board Clock to RTSI lines or front panel connectors. |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_SYNCHRONIZATION         | Synchronization strobe A synchronization strobe is used to guarantee absolute synchronization between two or more signal generators. Call the nifgen_ConfigureSynchronization function to receive the strobe.                                                                                                   |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_SOFTWARE_TRIG           | Software trigger                                                                                                                                                                                                                                                                                                |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_OUT_UPDATE              | —                                                                                                                                                                                                                                                                                                               |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_REF_OUT                 | Reference Clock out front panel connector                                                                                                                                                                                                                                                                       |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_PXI_CLK10               | PXI 10 MHz backplane Reference Clock                                                                                                                                                                                                                                                                            |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_PXI_STAR                | PXI star trigger line                                                                                                                                                                                                                                                                                           |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_PFI_0                   | PFI 0                                                                                                                                                                                                                                                                                                           |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_RTSI_0                  | RTSI 0 or PXI_Trig 0                                                                                                                                                                                                                                                                                            |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_RTSI_1                  | RTSI 1 or PXI_Trig 1                                                                                                                                                                                                                                                                                            |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_RTSI_2                  | RTSI 2 or PXI_Trig 2                                                                                                                                                                                                                                                                                            |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_RTSI_3                  | RTSI 3 or PXI_Trig 3                                                                                                                                                                                                                                                                                            |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_RTSI_4                  | RTSI 4 or PXI_Trig 4                                                                                                                                                                                                                                                                                            |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_RTSI_5                  | RTSI 5 or PXI_Trig 5                                                                                                                                                                                                                                                                                            |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_RTSI_6                  | RTSI 6 or PXI_Trig 6                                                                                                                                                                                                                                                                                            |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_RTSI_7                  | RTSI 7 or PXI_Trig 7                                                                                                                                                                                                                                                                                            |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_REF_CLOCK_RTSI_CLOCK    | RTSI clock                                                                                                                                                                                                                                                                                                      |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK | Onboard Reference Clock                                                                                                                                                                                                                                                                                         |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_UPDATE_CLOCK            | Sample Clock                                                                                                                                                                                                                                                                                                    |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_PLL_REF_SOURCE          | PLL Reference Clock                                                                                                                                                                                                                                                                                             |
                +------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
            route_signal_to (int): The possible RTSI lines to which you can route a signal.

                ****Defined Values****

                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_RTSI_0               | RTSI 0 or PXI_Trig 0                      |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_RTSI_1               | RTSI 1 or PXI_Trig 1                      |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_RTSI_2               | RTSI 2 or PXI_Trig 2                      |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_RTSI_3               | RTSI 3 or PXI_Trig 3                      |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_RTSI_4               | RTSI 4 or PXI_Trig 4                      |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_RTSI_5               | RTSI 5 or PXI_Trig 5                      |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_RTSI_6               | RTSI 6 or PXI_Trig 6                      |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_RTSI_7               | RTSI 7 or PXI_Trig 7                      |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_REF_CLOCK_RTSI_CLOCK | RTSI clock                                |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_REF_OUT              | Reference Clock out front panel connector |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_PFI_0                | PFI 0                                     |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_PFI_1                | PFI 1                                     |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_PFI_4                | PFI 4                                     |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_PFI_5                | PFI 5                                     |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_PXI_STAR             | PXI star trigger line                     |
                +---------------------------------+-------------------------------------------+
                | NIFGEN_VAL_PXI_CLK10            | PXI 10 MHz backplane Reference Clock      |
                +---------------------------------+-------------------------------------------+
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        route_signal_from_ctype = visatype.ViInt32(route_signal_from)  # case 8
        route_signal_to_ctype = visatype.ViInt32(route_signal_to)  # case 8
        error_code = self._library.niFgen_RouteSignalOut(vi_ctype, channel_name_ctype, route_signal_from_ctype, route_signal_to_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViBoolean(attribute_value)  # case 8
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViInt32(attribute_value)  # case 8
        error_code = self._library.niFgen_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int64(self, attribute_id, attribute_value):
        '''_set_attribute_vi_int64

        Sets the value of a ViInt64 attribute.

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

            session['0,1']._set_attribute_vi_int64(attribute_id, attribute_value)

        Args:
            attribute_id (int): Specifies the ID of an attribute.
            attribute_value (int): Specifies the value to which you want to set the attribute. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViInt64(attribute_value)  # case 8
        error_code = self._library.niFgen_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = visatype.ViReal64(attribute_value)  # case 8
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
            attribute_value (string): Specifies the value to which you want to set the attribute. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 8
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case 3
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
            waveform_name (string): Specifies the name to associate with the allocated waveform.
            relative_to (int): Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +------------------------------------------+-------------------------------------------------------------------------+
                | NIFGEN_VAL_WAVEFORM_POSITION_START (0)   | Use the start of the waveform as the reference position.                |
                +------------------------------------------+-------------------------------------------------------------------------+
                | NIFGEN_VAL_WAVEFORM_POSITION_CURRENT (1) | Use the current position within the waveform as the reference position. |
                +------------------------------------------+-------------------------------------------------------------------------+
            offset (int): Specifies the offset from the **relativeTo** parameter at which to start
                loading the data into the waveform.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case 3
        relative_to_ctype = visatype.ViInt32(relative_to)  # case 8
        offset_ctype = visatype.ViInt32(offset)  # case 8
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
            relative_to (int): Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +------------------------------------------+-------------------------------------------------------------------------+
                | NIFGEN_VAL_WAVEFORM_POSITION_START (0)   | Use the start of the waveform as the reference position.                |
                +------------------------------------------+-------------------------------------------------------------------------+
                | NIFGEN_VAL_WAVEFORM_POSITION_CURRENT (1) | Use the current position within the waveform as the reference position. |
                +------------------------------------------+-------------------------------------------------------------------------+
            offset (int): Specifies the offset from **relativeTo** at which to start loading the
                data into the waveform.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_handle_ctype = visatype.ViInt32(waveform_handle)  # case 8
        relative_to_ctype = visatype.ViInt32(relative_to)  # case 8
        offset_ctype = visatype.ViInt32(offset)  # case 8
        error_code = self._library.niFgen_SetWaveformNextWritePosition(vi_ctype, channel_name_ctype, waveform_handle_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_binary16_analog_static_value(self, value):
        '''write_binary16_analog_static_value

        | Writes the 16-bit value to the DAC, which could be output as a DC
          Voltage.
        | This function writes to the DAC only when in an external calibration
          session.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

            session['0,1'].write_binary16_analog_static_value(value)

        Args:
            value (int): The value to write.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        value_ctype = visatype.ViInt16(value)  # case 8
        error_code = self._library.niFgen_WriteBinary16AnalogStaticValue(vi_ctype, channel_name_ctype, value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_binary16_waveform(self, waveform_handle, size, data):
        '''write_binary16_waveform

        Writes binary data to the waveform in onboard memory. The waveform
        handle passed must have been created by a call to the
        nifgen_AllocateWaveform or the nifgen_CreateWaveformI16 function.

        By default, the subsequent call to the write_binary16_waveform
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

            session['0,1'].write_binary16_waveform(waveform_handle, size, data)

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the nifgen_AllocateWaveform function.
            size (int): Specifies the number of samples to load into the waveform.

                **Default Value**: 0
            data (list of int): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**. The binary data
                is left-justified.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_handle_ctype = visatype.ViInt32(waveform_handle)  # case 8
        size_ctype = visatype.ViInt32(size)  # case 8
        data_ctype = (visatype.ViInt16 * len(data))(*data)  # case 4
        error_code = self._library.niFgen_WriteBinary16Waveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_named_waveform_f64(self, waveform_name, size, data):
        '''write_named_waveform_f64

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        nifgen_AllocateWaveform function or to one of the following niFgen
        Create Waveform functions:

        -  nifgen_CreateWaveformF64
        -  nifgen_CreateWaveformI16
        -  nifgen_CreateWaveformFromFileI16
        -  nifgen_CreateWaveformFromFileF64
        -  nifgen_CreateWaveformFromFileHWS

        By default, the subsequent call to the write_named_waveform_f64
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

            session['0,1'].write_named_waveform_f64(waveform_name, size, data)

        Args:
            waveform_name (string): Specifies the name to associate with the allocated waveform.
            size (int): Specifies the number of samples to load into the waveform.

                **Default Value**: 0
            data (list of float): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case 3
        size_ctype = visatype.ViInt32(size)  # case 8
        data_ctype = (visatype.ViReal64 * len(data))(*data)  # case 4
        error_code = self._library.niFgen_WriteNamedWaveformF64(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_named_waveform_i16(self, waveform_name, size, data):
        '''write_named_waveform_i16

        Writes binary data to the named waveform in onboard memory.

        By default, the subsequent call to the write_named_waveform_i16
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

            session['0,1'].write_named_waveform_i16(waveform_name, size, data)

        Args:
            waveform_name (string): Specifies the name to associate with the allocated waveform.
            size (int): Specifies the number of samples to load into the waveform.

                **Default Value**: 0
            data (list of int): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case 3
        size_ctype = visatype.ViInt32(size)  # case 8
        data_ctype = (visatype.ViInt16 * len(data))(*data)  # case 4
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
            script (string): Contains the text of the script you want to use for your generation
                operation. Refer to `scripting
                Instructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__
                for more information about writing scripts.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        script_ctype = ctypes.create_string_buffer(script.encode(self._encoding))  # case 3
        error_code = self._library.niFgen_WriteScript(vi_ctype, channel_name_ctype, script_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_waveform(self, waveform_handle, size, data):
        '''write_waveform

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        nifgen_AllocateWaveform function or one of the following niFgen
        CreateWaveform functions:

        -  nifgen_CreateWaveformF64
        -  nifgen_CreateWaveformI16
        -  nifgen_CreateWaveformFromFileI16
        -  nifgen_CreateWaveformFromFileF64
        -  nifgen_CreateWaveformFromFileHWS

        By default, the subsequent call to the write_waveform function
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

            session['0,1'].write_waveform(waveform_handle, size, data)

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the nifgen_AllocateWaveform function.
            size (int): Specifies the number of samples to load into the waveform.

                **Default Value**: 0
            data (list of float): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        waveform_handle_ctype = visatype.ViInt32(waveform_handle)  # case 8
        size_ctype = visatype.ViInt32(size)  # case 8
        data_ctype = (visatype.ViReal64 * len(data))(*data)  # case 4
        error_code = self._library.niFgen_WriteWaveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, error_code):
        '''_error_message

        Converts a status code returned by an NI-FGEN function into a
        user-readable string.

        Args:
            error_code (int): Specifies the **status** parameter that is returned from any of the
                NI-FGEN functions.

                **Default Value**: 0 (VI_SUCCESS)

        Returns:
            error_message (string): Returns the error message string read from the instrument error message
                queue.

                You must pass a ViChar array with at least 256 bytes.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code_ctype = visatype.ViStatus(error_code)  # case 8
        error_message_ctype = (visatype.ViChar * 256)()  # case 10
        error_code = self._library.niFgen_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class _RepeatedCapability(_SessionBase):
    '''Allows for setting/getting properties and calling methods for specific repeated capabilities (such as channels) on your session.'''

    def __init__(self, vi, repeated_capability):
        super(_RepeatedCapability, self).__init__(repeated_capability)
        self._vi = vi
        self._is_frozen = True


class Session(_SessionBase):
    '''An NI-FGEN session to a National Instruments Signal Generator.'''

    def __init__(self, resource_name, reset_device, option_string):
        super(Session, self).__init__(repeated_capability='')
        self._vi = 0  # This must be set before calling _initialize_with_channels().
        self._vi = self._initialize_with_channels(resource_name, reset_device, option_string)
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        return _RepeatedCapability(self._vi, repeated_capability)

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

    def _abort_generation(self):
        '''_abort_generation

        Aborts any previously initiated signal generation. Call the
        nifgen_InitiateGeneration function to cause the signal generator to
        produce a signal again.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFgen_AbortGeneration(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def adjust_sample_clock_relative_delay(self, adjustment_time):
        '''adjust_sample_clock_relative_delay

        Delays (or phase shifts) the Sample Clock, which delays the generated
        signal. Delaying the Sample Clock can be useful when synchronizing the
        output of multiple modules or when intentionally phase shifting the
        output relative to a fixed reference, such as the PLL Reference Clock.

        Adjustment time can be positive or negative, but it must be less than or
        equal to the Sample Clock period. The delay takes effect immediately
        after this function is called. To delay an external Sample Clock, use
        the SAMPLE_CLOCK_ABSOLUTE_DELAY attribute.

        Args:
            adjustment_time (float): Specifies the amount of time to adjust the Sample Clock delay.

                **Units**: Seconds

                **Default Value**: 0
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        adjustment_time_ctype = visatype.ViReal64(adjustment_time)  # case 8
        error_code = self._library.niFgen_AdjustSampleClockRelativeDelay(vi_ctype, adjustment_time_ctype)
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
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
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        sequence_handle_ctype = visatype.ViInt32(sequence_handle)  # case 8
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

                -  create_waveform_f64
                -  create_waveform_i16
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64
                -  CreateWaveformFromFileHWS

                **Defined Value**:

                NIFGEN_VAL_ALL_WAVEFORMS—Remove all waveforms from the signal
                generator.

                **Default Value**: None
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        waveform_handle_ctype = visatype.ViInt32(waveform_handle)  # case 8
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
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        frequency_list_handle_ctype = visatype.ViInt32(frequency_list_handle)  # case 8
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFgen_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_script_trigger(self, trigger_id, source, edge):
        '''configure_digital_edge_script_trigger

        Configures the specified Script Trigger for digital edge triggering.

        Args:
            trigger_id (string): Specifies the Script Trigger used for triggering.

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
            source (string): Specifies which trigger source the signal generator uses.

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
            edge (int): Specifies the edge to detect.

                ****Defined Values****

                ****Default Value**:** NIFGEN_VAL_RISING_EDGE

                +-------------------------+------------------------------------------------------------------+
                | NIFGEN_VAL_RISING_EDGE  | Occurs when the signal transitions from low level to high level. |
                +-------------------------+------------------------------------------------------------------+
                | NIFGEN_VAL_FALLING_EDGE | Occurs when the signal transitions from high level to low level. |
                +-------------------------+------------------------------------------------------------------+
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case 3
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case 3
        edge_ctype = visatype.ViInt32(edge)  # case 8
        error_code = self._library.niFgen_ConfigureDigitalEdgeScriptTrigger(vi_ctype, trigger_id_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_edge_start_trigger(self, source, edge):
        '''configure_digital_edge_start_trigger

        Configures the Start Trigger for digital edge triggering.

        Args:
            source (string): Specifies which trigger source the signal generator uses.

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
            edge (int): Specifies the edge to detect.

                ****Defined Values****

                ****Default Value**:** NIFGEN_VAL_RISING_EDGE

                +-------------------------+------------------------------------------------------------------+
                | NIFGEN_VAL_RISING_EDGE  | Occurs when the signal transitions from low level to high level. |
                +-------------------------+------------------------------------------------------------------+
                | NIFGEN_VAL_FALLING_EDGE | Occurs when the signal transitions from high level to low level. |
                +-------------------------+------------------------------------------------------------------+
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case 3
        edge_ctype = visatype.ViInt32(edge)  # case 8
        error_code = self._library.niFgen_ConfigureDigitalEdgeStartTrigger(vi_ctype, source_ctype, edge_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_digital_level_script_trigger(self, trigger_id, source, trigger_when):
        '''configure_digital_level_script_trigger

        Configures the specified Script Trigger for digital level triggering.

        Args:
            trigger_id (string): Specifies the Script Trigger used for triggering.

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
            source (string): Specifies which trigger source the signal generator uses.

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
            trigger_when (int): Specifies whether the Script Trigger asserts on a high or low digital
                level.

                **Defined Values**

                **Default Value**: "HighLevel"

                +-------------+-------------------------------------------------+
                | "HighLevel" | Script Trigger asserts on a high digital level. |
                +-------------+-------------------------------------------------+
                | "LowLevel"  | Script Trigger asserts on a low digital level.  |
                +-------------+-------------------------------------------------+
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case 3
        source_ctype = ctypes.create_string_buffer(source.encode(self._encoding))  # case 3
        trigger_when_ctype = visatype.ViInt32(trigger_when)  # case 8
        error_code = self._library.niFgen_ConfigureDigitalLevelScriptTrigger(vi_ctype, trigger_id_ctype, source_ctype, trigger_when_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_arb_sequence(self, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array):
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
        **outputMode** parameter to NIFGEN_VAL_OUTPUT_SEQ before calling this
        function.

        Args:
            sequence_length (int): Specifies the number of waveforms in the new arbitrary sequence that you
                want to create. The value you pass must be between the minimum and
                maximum sequence lengths that the signal generator allows. You can
                obtain the minimum and maximum sequence lengths from
                **minimumSequenceLength** and **maximumSequenceLength** in the
                nifgen_QueryArbSeqCapabilities function.

                **Default Value**: None
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

        Returns:
            coerced_markers_array (list of int): Returns an array of all given markers that are coerced (rounded) to the
                nearest marker quantum. Not all devices coerce markers.

                **Default Value**: None
            sequence_handle (int): Returns the handle that identifies the new arbitrary sequence. You can
                pass this handle to nifgen_ConfigureArbSequence to generate the
                arbitrary sequence.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        sequence_length_ctype = visatype.ViInt32(sequence_length)  # case 8
        waveform_handles_array_ctype = (visatype.ViInt32 * len(waveform_handles_array))(*waveform_handles_array)  # case 4
        loop_counts_array_ctype = (visatype.ViInt32 * len(loop_counts_array))(*loop_counts_array)  # case 4
        sample_counts_array_ctype = (visatype.ViInt32 * len(sample_counts_array))(*sample_counts_array)  # case 4
        marker_location_array_ctype = (visatype.ViInt32 * len(marker_location_array))(*marker_location_array)  # case 4
        coerced_markers_array_ctype = (visatype.ViInt32 * 1)()  # case 10
        sequence_handle_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_CreateAdvancedArbSequence(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, sample_counts_array_ctype, marker_location_array_ctype, coerced_markers_array_ctype, ctypes.pointer(sequence_handle_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(coerced_markers_array_ctype[i]) for i in range(1)], int(sequence_handle_ctype.value)

    def create_arb_sequence(self, sequence_length, waveform_handles_array, loop_counts_array):
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
        **outputMode** parameter to NIFGEN_VAL_OUTPUT_SEQ before calling this
        function.

        Args:
            sequence_length (int): Specifies the number of waveforms in the new arbitrary sequence that you
                want to create. The value you pass must be between the minimum and
                maximum sequence lengths that the signal generator allows. You can
                obtain the minimum and maximum sequence lengths from
                **minimumSequenceLength** and **maximumSequenceLength** in the
                nifgen_QueryArbSeqCapabilities function.

                **Default Value**: None
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        sequence_length_ctype = visatype.ViInt32(sequence_length)  # case 8
        waveform_handles_array_ctype = (visatype.ViInt32 * len(waveform_handles_array))(*waveform_handles_array)  # case 4
        loop_counts_array_ctype = (visatype.ViInt32 * len(loop_counts_array))(*loop_counts_array)  # case 4
        sequence_handle_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_CreateArbSequence(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, ctypes.pointer(sequence_handle_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(sequence_handle_ctype.value)

    def create_arb_waveform(self, waveform_size, waveform_data_array):
        '''create_arb_waveform

        [OBSOLETE] This function is obsolete. Use the nifgen_CreateWaveformF64,
        nifgen_CreateWaveformI16, or nifgen_CreateWaveformComplexF64 function
        instead of this function.

        Creates an arbitrary waveform and returns a handle that identifies that
        waveform. You can pass this handle to the nifgen_ConfigureArbWaveform
        function to produce that waveform. You can also use the handles this
        function returns to specify a sequence of arbitrary waveforms with the
        nifgen_CreateArbSequence function.

        Note:
        You must scale the data between –1.00 and +1.00. Use the **arbGain**
        parameter to generate different output voltages.

        Args:
            waveform_size (int): | Specifies the size of the arbitrary waveform that you want created.
                | The size must meet the following restrictions:

                -  The size must be less than or equal to the maximum waveform size that
                   the device allows.
                -  The size must be greater than or equal to the minimum waveform size
                   that the device allows.
                -  The size must be an integer multiple of the device waveform quantum.

                |
                | You can obtain these values from the **maximumWaveformSize**,
                  **minimumWaveformSize**, and **waveformQuantum** parameters in the
                  nifgen_QueryArbWfmCapabilities function.
                | ****Default Value**:** None
            waveform_data_array (list of float): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None

        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        waveform_size_ctype = visatype.ViInt32(waveform_size)  # case 8
        waveform_data_array_ctype = (visatype.ViReal64 * len(waveform_data_array))(*waveform_data_array)  # case 4
        waveform_handle_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_CreateArbWaveform(vi_ctype, waveform_size_ctype, waveform_data_array_ctype, ctypes.pointer(waveform_handle_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_binary16_arb_waveform(self, waveform_size, waveform_data_array):
        '''create_binary16_arb_waveform

        [OBSOLETE] This function is obsolete. Use the nifgen_CreateWaveformI16
        function instead of this function.

        Creates an arbitrary waveform from binary data and returns a handle that
        identifies that waveform. You can pass this handle to the
        nifgen_ConfigureArbWaveform function to produce that waveform. You can
        also use the handles this function returns to specify a sequence of
        arbitrary waveforms with the nifgen_CreateArbSequence function.

        Note:
        You must set the output mode to NIFGEN_VAL_OUTPUT_ARB or
        NIFGEN_VAL_OUTPUT_SEQ before calling this function.

        Args:
            waveform_size (int): | Specifies the size of the arbitrary waveform that you want created.
                | The size must meet the following restrictions:

                -  The size must be less than or equal to the maximum waveform size that
                   the device allows.
                -  The size must be greater than or equal to the minimum waveform size
                   that the device allows.
                -  The size must be an integer multiple of the device waveform quantum.

                |
                | You can obtain these values from the **maximumWaveformSize**,
                  **minimumWaveformSize**, and **waveformQuantum** parameters in
                  nifgen_QueryArbWfmCapabilities.
                | ****Default Value**:** None
            waveform_data_array (list of int): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –32768 and
                32767.

                **Default Value**: None

        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        waveform_size_ctype = visatype.ViInt32(waveform_size)  # case 8
        waveform_data_array_ctype = (visatype.ViInt16 * len(waveform_data_array))(*waveform_data_array)  # case 4
        waveform_handle_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_CreateBinary16ArbWaveform(vi_ctype, waveform_size_ctype, waveform_data_array_ctype, ctypes.pointer(waveform_handle_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_freq_list(self, waveform, frequency_list_length, frequency_array, duration_array):
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
            waveform (int): Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the FUNC_WAVEFORM attribute to this
                value.

                ****Defined Values****

                **Default Value**: NIFGEN_VAL_WFM_SINE

                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_SINE      | Specifies that the signal generator produces a sinusoid waveform.                                                                    |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_SQUARE    | Specifies that the signal generator produces a square waveform.                                                                      |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_TRIANGLE  | Specifies that the signal generator produces a triangle waveform.                                                                    |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_RAMP_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                               |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_RAMP_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                               |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_DC        | Specifies that the signal generator produces a constant voltage.                                                                     |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_NOISE     | Specifies that the signal generator produces white noise.                                                                            |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_WFM_USER      | Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform function. |
                +--------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
            frequency_list_length (int): Specifies the number of steps in the frequency list you want to create.
                The value must be between the minimum and maximum frequency list lengths
                that the signal generator allows. You can obtain the minimum and maximum
                frequency list lengths from the **minimumFrequencyListLength** and
                **maximumFrequencyListLength** parameters in the
                nifgen_QueryFreqListCapabilities function.

                **frequency** and **duration** must each be at least as long as this
                frequency list length.

                **Default Value**: None
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        waveform_ctype = visatype.ViInt32(waveform)  # case 8
        frequency_list_length_ctype = visatype.ViInt32(frequency_list_length)  # case 8
        frequency_array_ctype = (visatype.ViReal64 * len(frequency_array))(*frequency_array)  # case 4
        duration_array_ctype = (visatype.ViReal64 * len(duration_array))(*duration_array)  # case 4
        frequency_list_handle_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_CreateFreqList(vi_ctype, waveform_ctype, frequency_list_length_ctype, frequency_array_ctype, duration_array_ctype, ctypes.pointer(frequency_list_handle_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(frequency_list_handle_ctype.value)

    def disable(self):
        '''disable

        Places the instrument in a quiescent state where it has minimal or no
        impact on the system to which it is connected. The analog output and all
        exported signals are disabled.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFgen_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_handler(self, error_code):
        '''error_handler

        Converts a status code returned by an NI-FGEN function into a
        user-readable string and returns any error elaborations.

        Args:
            error_code (int): Specifies the **status** parameter that is returned from any of the
                NI-FGEN functions.

                **Default Value**: 0 (VI_SUCCESS)

        Returns:
            error_message (string): Returns the error message string read from the instrument error message
                queue.

                You must pass a ViChar array with at least 256 bytes.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code_ctype = visatype.ViStatus(error_code)  # case 8
        error_message_ctype = (visatype.ViChar * 1)()  # case 10
        error_code = self._library.niFgen_ErrorHandler(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return error_message_ctype.value.decode(self._encoding)

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

        Args:
            signal (int): Specifies the source of the signal to route.
                ****Defined Values****

                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK | Onboard 10 MHz synchronization clock (PCI only)                                                                                                               |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_SYNC_OUT                | SYNC OUT signal The SYNC OUT signal is normally generated on the SYNC OUT front panel connector.                                                              |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_START_TRIGGER           | Start Trigger                                                                                                                                                 |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_MARKER_EVENT            | Marker Event                                                                                                                                                  |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE   | The clock from which the Sample Clock is derived                                                                                                              |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_SYNCHRONIZATION         | Synchronization strobe (NI 5404/5411/5431 only) A synchronization strobe is used to guarantee absolute synchronization between two or more signal generators. |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_SAMPLE_CLOCK            | Sample Clock                                                                                                                                                  |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_REFERENCE_CLOCK         | PLL Reference Clock                                                                                                                                           |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_SCRIPT_TRIGGER          | Script Trigger                                                                                                                                                |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_READY_FOR_START_EVENT   | Ready For Start Event                                                                                                                                         |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_STARTED_EVENT           | Started Event                                                                                                                                                 |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_DONE_EVENT              | Done Event                                                                                                                                                    |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIFGEN_VAL_DATA_MARKER_EVENT       | Data Marker Event                                                                                                                                             |
                +------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
            signal_identifier (string): Specifies which instance of the selected signal to export.
                ****Defined Values****

                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "" (empty string)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "ScriptTrigger0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "ScriptTrigger1"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "ScriptTrigger2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "ScriptTrigger3"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "Marker0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "Marker1"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "Marker2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "Marker3"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "DataMarker0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "DataMarker1"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "DataMarker2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "DataMarker3"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | \* These Data Marker values apply only to single-channel devices or to multichannel devices that are configured for single-channel operation. When using a device that is configured for multichannel operation, specify the channel number along with the signal identifier. For example, to export Data Marker 0 on channel 1 of a device configured for multichannel operation, use the value "1/ DataMarker0." If you do not specify a channel when using a device configured for multichannel generation, DataMarker0 generates on all channels. |
                +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
            output_terminal (string): Specifies the output terminal to export the signal.
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        signal_ctype = visatype.ViInt32(signal)  # case 8
        signal_identifier_ctype = ctypes.create_string_buffer(signal_identifier.encode(self._encoding))  # case 3
        output_terminal_ctype = ctypes.create_string_buffer(output_terminal.encode(self._encoding))  # case 3
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        year_ctype = visatype.ViInt32()  # case 13
        month_ctype = visatype.ViInt32()  # case 13
        day_ctype = visatype.ViInt32()  # case 13
        hour_ctype = visatype.ViInt32()  # case 13
        minute_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_GetExtCalLastDateAndTime(vi_ctype, ctypes.pointer(year_ctype), ctypes.pointer(month_ctype), ctypes.pointer(day_ctype), ctypes.pointer(hour_ctype), ctypes.pointer(minute_ctype))
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        temperature_ctype = visatype.ViReal64()  # case 13
        error_code = self._library.niFgen_GetExtCalLastTemp(vi_ctype, ctypes.pointer(temperature_ctype))
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        months_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_GetExtCalRecommendedInterval(vi_ctype, ctypes.pointer(months_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_hardware_state(self):
        '''get_hardware_state

        Returns the current hardware state of the device and, if the device is
        in the hardware error state, the current hardware error.

        Note: Hardware states do not necessarily correspond to NI-FGEN states.

        Returns:
            state (int): Returns the hardware state of the signal generator.

                **Defined Values**

                +--------------------------------------+--------------------------------------------+
                | NIFGEN_VAL_IDLE                      | The device is in the Idle state.           |
                +--------------------------------------+--------------------------------------------+
                | NIFGEN_VAL_WAITING_FOR_START_TRIGGER | The device is waiting for Start Trigger.   |
                +--------------------------------------+--------------------------------------------+
                | NIFGEN_VAL_RUNNING                   | The device is in the Running state.        |
                +--------------------------------------+--------------------------------------------+
                | NIFGEN_VAL_DONE                      | The generation has completed successfully. |
                +--------------------------------------+--------------------------------------------+
                | NIFGEN_VAL_HARDWARE_ERROR            | There is a hardware error.                 |
                +--------------------------------------+--------------------------------------------+
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        state_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_GetHardwareState(vi_ctype, ctypes.pointer(state_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(state_ctype.value)

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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        year_ctype = visatype.ViInt32()  # case 13
        month_ctype = visatype.ViInt32()  # case 13
        day_ctype = visatype.ViInt32()  # case 13
        hour_ctype = visatype.ViInt32()  # case 13
        minute_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_GetSelfCalLastDateAndTime(vi_ctype, ctypes.pointer(year_ctype), ctypes.pointer(month_ctype), ctypes.pointer(day_ctype), ctypes.pointer(hour_ctype), ctypes.pointer(minute_ctype))
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        temperature_ctype = visatype.ViReal64()  # case 13
        error_code = self._library.niFgen_GetSelfCalLastTemp(vi_ctype, ctypes.pointer(temperature_ctype))
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        self_cal_supported_ctype = visatype.ViBoolean()  # case 13
        error_code = self._library.niFgen_GetSelfCalSupported(vi_ctype, ctypes.pointer(self_cal_supported_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_supported_ctype.value)

    def initialize_analog_output_calibration(self):
        '''initialize_analog_output_calibration

        Sets up the device to start the analog output calibration.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFgen_InitializeAnalogOutputCalibration(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def initialize_cal_adc_calibration(self):
        '''initialize_cal_adc_calibration

        Initializes an external calibration session for ADC calibration. For the
        NI 5421/5422/5441, ADC calibration involves characterizing the gain and
        offset of the onboard ADC.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFgen_InitializeCalADCCalibration(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def initialize_flatness_calibration(self):
        '''initialize_flatness_calibration

        Initializes an external calibration session to calibrate flatness.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFgen_InitializeFlatnessCalibration(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def initialize_oscillator_frequency_calibration(self):
        '''initialize_oscillator_frequency_calibration

        Sets up the device to start the VCXO calibration.

        The session handle should be the handle returned by the
        nifgen_InitExtCal function.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFgen_InitializeOscillatorFrequencyCalibration(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _initiate_generation(self):
        '''_initiate_generation

        Initiates signal generation. If you want to abort signal generation,
        call the nifgen_AbortGeneration function. After the signal generation
        is aborted, you can call the _initiate_generation function to
        cause the signal generator to produce a signal again.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        done_ctype = visatype.ViBoolean()  # case 13
        error_code = self._library.niFgen_IsDone(vi_ctype, ctypes.pointer(done_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    def query_arb_seq_capabilities(self):
        '''query_arb_seq_capabilities

        Returns the attributes of the signal generator that are related to
        creating arbitrary sequences (the MAX_NUM_SEQUENCES,
        MIN_SEQUENCE_LENGTH,
        MAX_SEQUENCE_LENGTH, and MAX_LOOP_COUNT
        attributes).

        Returns:
            maximum_number_of_sequences (int): Returns the maximum number of arbitrary waveform sequences that the
                signal generator allows. NI-FGEN obtains this value from the
                MAX_NUM_SEQUENCES attribute.
            minimum_sequence_length (int): Returns the minimum number of arbitrary waveforms the signal generator
                allows in a sequence. NI-FGEN obtains this value from the
                MIN_SEQUENCE_LENGTH attribute.
            maximum_sequence_length (int): Returns the maximum number of arbitrary waveforms the signal generator
                allows in a sequence. NI-FGEN obtains this value from the
                MAX_SEQUENCE_LENGTH attribute.
            maximum_loop_count (int): Returns the maximum number of times the signal generator can repeat an
                arbitrary waveform in a sequence. NI-FGEN obtains this value from the
                MAX_LOOP_COUNT attribute.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_number_of_sequences_ctype = visatype.ViInt32()  # case 13
        minimum_sequence_length_ctype = visatype.ViInt32()  # case 13
        maximum_sequence_length_ctype = visatype.ViInt32()  # case 13
        maximum_loop_count_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_QueryArbSeqCapabilities(vi_ctype, ctypes.pointer(maximum_number_of_sequences_ctype), ctypes.pointer(minimum_sequence_length_ctype), ctypes.pointer(maximum_sequence_length_ctype), ctypes.pointer(maximum_loop_count_ctype))
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
                MAX_NUM_WAVEFORMS attribute.
            waveform_quantum (int): The size (number of points) of each waveform must be a multiple of a
                constant quantum value. This parameter obtains the quantum value that
                the signal generator uses. NI-FGEN returns this value from the
                WAVEFORM_QUANTUM attribute.

                For example, when this attribute returns a value of 8, all waveform
                sizes must be a multiple of 8.
            minimum_waveform_size (int): Returns the minimum number of points that the signal generator allows in
                a waveform. NI-FGEN obtains this value from the
                MIN_WAVEFORM_SIZE attribute.
            maximum_waveform_size (int): Returns the maximum number of points that the signal generator allows in
                a waveform. NI-FGEN obtains this value from the
                MAX_WAVEFORM_SIZE attribute.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_number_of_waveforms_ctype = visatype.ViInt32()  # case 13
        waveform_quantum_ctype = visatype.ViInt32()  # case 13
        minimum_waveform_size_ctype = visatype.ViInt32()  # case 13
        maximum_waveform_size_ctype = visatype.ViInt32()  # case 13
        error_code = self._library.niFgen_QueryArbWfmCapabilities(vi_ctype, ctypes.pointer(maximum_number_of_waveforms_ctype), ctypes.pointer(waveform_quantum_ctype), ctypes.pointer(minimum_waveform_size_ctype), ctypes.pointer(maximum_waveform_size_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_waveforms_ctype.value), int(waveform_quantum_ctype.value), int(minimum_waveform_size_ctype.value), int(maximum_waveform_size_ctype.value)

    def query_freq_list_capabilities(self):
        '''query_freq_list_capabilities

        Returns the attributes of the signal generator that are related to
        creating frequency lists. These attributes are
        MAX_NUM_FREQ_LISTS,
        MIN_FREQ_LIST_LENGTH,
        MAX_FREQ_LIST_LENGTH,
        MIN_FREQ_LIST_DURATION,
        MAX_FREQ_LIST_DURATION, and
        FREQ_LIST_DURATION_QUANTUM.

        Returns:
            maximum_number_of_freq_lists (int): Returns the maximum number of frequency lists that the signal generator
                allows. NI-FGEN obtains this value from the
                MAX_NUM_FREQ_LISTS attribute.
            minimum_frequency_list_length (int): Returns the minimum number of steps that the signal generator allows in
                a frequency list. NI-FGEN obtains this value from the
                MIN_FREQ_LIST_LENGTH attribute.
            maximum_frequency_list_length (int): Returns the maximum number of steps that the signal generator allows in
                a frequency list. NI-FGEN obtains this value from the
                MAX_FREQ_LIST_LENGTH attribute.
            minimum_frequency_list_duration (float): Returns the minimum duration that the signal generator allows in a step
                of a frequency list. NI-FGEN obtains this value from the
                MIN_FREQ_LIST_DURATION attribute.
            maximum_frequency_list_duration (float): Returns the maximum duration that the signal generator allows in a step
                of a frequency list. NI-FGEN obtains this value from the
                MAX_FREQ_LIST_DURATION attribute.
            frequency_list_duration_quantum (float): Returns the quantum of which all durations must be a multiple in a
                frequency list. NI-FGEN obtains this value from the
                FREQ_LIST_DURATION_QUANTUM attribute.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_number_of_freq_lists_ctype = visatype.ViInt32()  # case 13
        minimum_frequency_list_length_ctype = visatype.ViInt32()  # case 13
        maximum_frequency_list_length_ctype = visatype.ViInt32()  # case 13
        minimum_frequency_list_duration_ctype = visatype.ViReal64()  # case 13
        maximum_frequency_list_duration_ctype = visatype.ViReal64()  # case 13
        frequency_list_duration_quantum_ctype = visatype.ViReal64()  # case 13
        error_code = self._library.niFgen_QueryFreqListCapabilities(vi_ctype, ctypes.pointer(maximum_number_of_freq_lists_ctype), ctypes.pointer(minimum_frequency_list_length_ctype), ctypes.pointer(maximum_frequency_list_length_ctype), ctypes.pointer(minimum_frequency_list_duration_ctype), ctypes.pointer(maximum_frequency_list_duration_ctype), ctypes.pointer(frequency_list_duration_quantum_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_freq_lists_ctype.value), int(minimum_frequency_list_length_ctype.value), int(maximum_frequency_list_length_ctype.value), float(minimum_frequency_list_duration_ctype.value), float(maximum_frequency_list_duration_ctype.value), float(frequency_list_duration_quantum_ctype.value)

    def read_cal_adc(self, number_of_reads_to_average, return_calibrated_value):
        '''read_cal_adc

        Takes one or more voltage measurements from the onboard calibration ADC
        and returns the value or the average value. The signal that the ADC
        actually measures can be specified using the
        CAL_ADC_INPUT attribute. The ADC has some inherent gain
        and offset. These values can be determined during an external
        calibration session and stored in the calibration EEPROM.

        If the **returnCalibratedValue** parameter is VI_TRUE, NI-FGEN adjusts
        the value that is returned to account for the gain and offset of the
        ADC. Otherwise, the raw voltage value reported by the ADC is returned.

        Args:
            number_of_reads_to_average (int): Specifies the number of measurements to be taken and averaged to
                determine the return value.
            return_calibrated_value (bool): Specifies whether the voltage returned from the ADC should be adjusted
                to account for the gain and offset of the ADC.

        Returns:
            cal_adc_value (float): Specifies the average of the voltage measurements taken from the onboard
                calibration ADC.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        number_of_reads_to_average_ctype = visatype.ViInt32(number_of_reads_to_average)  # case 8
        return_calibrated_value_ctype = visatype.ViBoolean(return_calibrated_value)  # case 8
        cal_adc_value_ctype = visatype.ViReal64()  # case 13
        error_code = self._library.niFgen_ReadCalADC(vi_ctype, number_of_reads_to_average_ctype, return_calibrated_value_ctype, ctypes.pointer(cal_adc_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(cal_adc_value_ctype.value)

    def read_current_temperature(self):
        '''read_current_temperature

        Reads the current onboard temperature of the device. The temperature is
        returned in degrees Celsius.

        Returns:
            temperature (float): Returns the current temperature read from onboard temperature sensors,
                in degrees Celsius.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        temperature_ctype = visatype.ViReal64()  # case 13
        error_code = self._library.niFgen_ReadCurrentTemperature(vi_ctype, ctypes.pointer(temperature_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def reset_device(self):
        '''reset_device

        Performs a hard reset on the device. Generation is stopped, all routes
        are released, external bidirectional terminals are tristated, FPGAs are
        reset, hardware is configured to its default state, and all session
        attributes are reset to their default states.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFgen_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self):
        '''self_cal

        Performs a full internal self-calibration on the device. If the
        calibration is successful, new calibration data and constants are stored
        in the onboard EEPROM.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
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
            trigger (int): Sets the clock mode of the signal generator.

                ****Defined Values****

                +----------------------------+
                | NIFGEN_VAL_DIVIDE_DOWN     |
                +----------------------------+
                | NIFGEN_VAL_HIGH_RESOLUTION |
                +----------------------------+
                | NIFGEN_VAL_AUTOMATIC       |
                +----------------------------+
            trigger_id (string):
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        trigger_ctype = visatype.ViInt32(trigger)  # case 8
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case 3
        error_code = self._library.niFgen_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger(self):
        '''send_software_trigger

        Sends a command to trigger the signal generator.

        Note:
        This function can act as an override for an external edge trigger.
        However, the NI 5401/5411/5431 do not support overriding an external
        digital edge trigger.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niFgen_SendSoftwareTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_until_done(self, max_time):
        '''wait_until_done

        Waits until the device is done generating or until the maximum time has
        expired.

        Args:
            max_time (int): Specifies the timeout value in milliseconds.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        max_time_ctype = visatype.ViInt32(max_time)  # case 8
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
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
        vi_ctype = visatype.ViSession(self._vi)  # case 1
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
            self_test_message (string): Returns the self-test response string from the instrument.

                You must pass a ViChar array with at least 256 bytes.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        self_test_result_ctype = visatype.ViInt16()  # case 13
        self_test_message_ctype = (visatype.ViChar * 256)()  # case 10
        error_code = self._library.niFgen_self_test(vi_ctype, ctypes.pointer(self_test_result_ctype), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



