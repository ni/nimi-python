Enums
=====

Enums used in NI-SCOPE

.. py:currentmodule:: niscope



.. py:data:: AcquisitionType

    .. py:attribute:: niscope.AcquisitionType.NORMAL



        Sets the digitizer to normal resolution mode. The digitizer can use
        real-time sampling or equivalent-time sampling.

        



    .. py:attribute:: niscope.AcquisitionType.FLEX_RES



        Sets the digitizer to flexible resolution mode, if supported. The
        digitizer uses different hardware configurations to change the
        resolution depending on the sampling rate used.

        



    .. py:attribute:: niscope.AcquisitionType.DDC



        Sets the NI 5620/5621digitizer to DDC mode.

        




.. py:data:: AddressType

    .. py:attribute:: niscope.AddressType.PHYSICAL



        Physical address.

        



    .. py:attribute:: niscope.AddressType.VIRTUAL



        Virtual address.

        




.. py:data:: BoolEnableDisable

    .. py:attribute:: niscope.BoolEnableDisable.DISABLED



        Disabled

        



    .. py:attribute:: niscope.BoolEnableDisable.ENABLED



        Enabled

        




.. py:data:: BoolEnableDisableChan

    .. py:attribute:: niscope.BoolEnableDisableChan.DISABLED



        Does not acquire a waveform for the channel.

        



    .. py:attribute:: niscope.BoolEnableDisableChan.ENABLED



        Acquires a waveform for the channel.

        




.. py:data:: BoolEnableDisableIQ

    .. py:attribute:: niscope.BoolEnableDisableIQ.DISABLED



        A scalar fetch returns an array of waveforms in the following format:
        III...QQQ...

        



    .. py:attribute:: niscope.BoolEnableDisableIQ.ENABLED



        (Default) A scalar fetch returns an array of waveforms in the following
        format: IQIQIQ...

        




.. py:data:: BoolEnableDisableRealtime

    .. py:attribute:: niscope.BoolEnableDisableRealtime.DISABLED



        Allow both real-time and equivalent-time measurements.

        



    .. py:attribute:: niscope.BoolEnableDisableRealtime.ENABLED



        Allow only real-time measurements.

        




.. py:data:: BoolEnableDisableTIS

    .. py:attribute:: niscope.BoolEnableDisableTIS.DISABLED



        (Default) Use only this channel's ADC to acquire data for this channel.

        



    .. py:attribute:: niscope.BoolEnableDisableTIS.ENABLED



        Use multiple interleaved ADCs to acquire data for this channel.

        




.. py:data:: DataProcessingMode

    .. py:attribute:: niscope.DataProcessingMode.REAL



        The waveform data points are real numbers (I data).

        



    .. py:attribute:: niscope.DataProcessingMode.COMPLEX



        The waveform data points are complex numbers (IQ data).

        




.. py:data:: FIRFilterWindow

    .. py:attribute:: niscope.FIRFilterWindow.NONE



        No window.

        



    .. py:attribute:: niscope.FIRFilterWindow.HANNING



        Specifies a Hanning window.

        



    .. py:attribute:: niscope.FIRFilterWindow.FLAT_TOP



        Specifies a Flat Top window.

        



    .. py:attribute:: niscope.FIRFilterWindow.HAMMING



        Specifies a Hamming window.

        



    .. py:attribute:: niscope.FIRFilterWindow.TRIANGLE



        Specifies a Triangle window.

        



    .. py:attribute:: niscope.FIRFilterWindow.BLACKMAN



        Specifies a Blackman window.

        




.. py:data:: FetchRelativeTo

    .. py:attribute:: niscope.FetchRelativeTo.READ_POINTER



        The read pointer is set to zero when a new acquisition is initiated.
        After every fetch the read pointer is incremented to be the sample after
        the last sample retrieved. Therefore, you can repeatedly fetch relative
        to the read pointer for a continuous acquisition program.

        



    .. py:attribute:: niscope.FetchRelativeTo.PRETRIGGER



        Fetches relative to the first pretrigger point requested with the
        niScope Configure Horizontal Timing VI.

        



    .. py:attribute:: niscope.FetchRelativeTo.NOW



        Fetch data at the last sample acquired.

        



    .. py:attribute:: niscope.FetchRelativeTo.START



        Fetch data starting at the first point sampled by the digitizer.

        



    .. py:attribute:: niscope.FetchRelativeTo.TRIGGER



        Fetch at the first posttrigger sample.

        




.. py:data:: FilterType

    .. py:attribute:: niscope.FilterType.LOWPASS



        Specifies lowpass as the filter type.

        



    .. py:attribute:: niscope.FilterType.HIGHPASS



        Specifies highpass as the filter type.

        



    .. py:attribute:: niscope.FilterType.BANDPASS



        Specifies bandpass as the filter type.

        



    .. py:attribute:: niscope.FilterType.BANDSTOP



        Specifies bandstop as the filter type.

        




.. py:data:: FlexFIRAntialiasFilterType

    .. py:attribute:: niscope.FlexFIRAntialiasFilterType._48_TAP_STANDARD



        48 Tap Standard filter is optimized for alias protection and
        frequency-domain flatness.

        



    .. py:attribute:: niscope.FlexFIRAntialiasFilterType._48_TAP_HANNING



        48 Tap Hanning filter is optimized for the lowest possible bandwidth for
        a 48 tap filter and maximizes the SNR.

        



    .. py:attribute:: niscope.FlexFIRAntialiasFilterType._16_TAP_HANNING



        16 Tap Hanning is optimized for the lowest possible bandwidth for a 16
        tap filter and maximizes the SNR.

        



    .. py:attribute:: niscope.FlexFIRAntialiasFilterType._8_TAP_HANNING



        8 Tap Hanning filter is optimized for the lowest possible bandwidth for
        a 8 tap filter and maximizes the SNR.

        




.. py:data:: NotificationType

    .. py:attribute:: niscope.NotificationType.NEVER



        Never send notification.

        



    .. py:attribute:: niscope.NotificationType.DONE



        Notify when digitizer acquisition is done.

        




.. py:data:: OverflowErrorReporting

    .. py:attribute:: niscope.OverflowErrorReporting.ERROR



        Execution stops and NI-SCOPE returns an error when an overflow has
        occurred in the OSP block.

        



    .. py:attribute:: niscope.OverflowErrorReporting.WARNING



        Execution continues and NI-SCOPE returns a warning when an overflow has
        occurred in the OSP block.

        



    .. py:attribute:: niscope.OverflowErrorReporting.DISABLED



        NI-SCOPE does not return an error when an overflow has occurred in the
        OSP block.

        




.. py:data:: PercentageMethod

    .. py:attribute:: niscope.PercentageMethod.LOWHIGH



        Specifies that the reference level percentages should be computed using
        the low/high method,

        



    .. py:attribute:: niscope.PercentageMethod.MINMAX



        Reference level percentages are computed using the min/max method.

        



    .. py:attribute:: niscope.PercentageMethod.BASETOP



        Reference level percentages are computed using the base/top method.

        




.. py:data:: RISMethod

    .. py:attribute:: niscope.RISMethod.EXACT_NUM_AVG_



        Acquires exactly the specified number of records for each bin in the RIS
        acquisition.

        



    .. py:attribute:: niscope.RISMethod.MIN_NUM_AVG_



        Each RIS sample is the average of a least a minimum number of randomly
        distributed points.

        



    .. py:attribute:: niscope.RISMethod.INCOMPLETE



        If RIS does not complete in the allotted fetch time, the Fetch VI should
        abort and return the incomplete data. Any missing samples appear as NaN
        when fetching scaled data or zero when fetching binary data. A warning
        with a positive error code is returned from the Fetch VI if the RIS
        acquisition did not finish. The acquisition is aborted when data is
        returned.

        



    .. py:attribute:: niscope.RISMethod.LIMIT_BIN_WIDTH



        Each RIS sample is the average of Min Num Avg points distributed close
        to the sample period boundaries (within 200 ps). Points falling between
        sample periods are ignored.

        




.. py:data:: RefLevelUnits

    .. py:attribute:: niscope.RefLevelUnits.VOLTS



        Specifies that the reference levels are given in units of volts.

        



    .. py:attribute:: niscope.RefLevelUnits.PERCENTAGE



        (Default) Specifies that the reference levels are given in percentage
        units.

        




.. py:data:: RefTriggerDetectorLocation

    .. py:attribute:: niscope.RefTriggerDetectorLocation.ANALOG_DETECTION_CIRCUIT



        (Default) Uses the hardware analog circuitry to implement the reference
        trigger. This option detects trigger conditions by analyzing the
        unprocessed analog signal.

        



    .. py:attribute:: niscope.RefTriggerDetectorLocation.DDC_OUTPUT



        Uses the onboard signal processing logic to implement the reference
        trigger. This option detects trigger conditions by analyzing the
        processed digital signal.

        




.. py:data:: StreamingPositionType

    .. py:attribute:: niscope.StreamingPositionType.START_TRIGGER



        Data is streamed from the start trigger.

        



    .. py:attribute:: niscope.StreamingPositionType.REFERENCE_TRIGGER



        Data is streamed relative to the reference trigger and reference
        position.

        



    .. py:attribute:: niscope.StreamingPositionType.SYNC_TRIGGER



        Data is streamed relative to the sync trigger and reference position.

        




.. py:data:: TerminalConfiguration

    .. py:attribute:: niscope.TerminalConfiguration.SINGLE_ENDED



        Single-ended channel terminal configuration.

        



    .. py:attribute:: niscope.TerminalConfiguration.UNBALANCED_DIFFERENTIAL



        Unbalanced differential channel terminal configuration.

        



    .. py:attribute:: niscope.TerminalConfiguration.DIFFERENTIAL



        Differential channel terminal configuration.

        




.. py:data:: TriggerCoupling

    .. py:attribute:: niscope.TriggerCoupling.AC



        AC coupled

        



    .. py:attribute:: niscope.TriggerCoupling.DC



        DC coupled

        



    .. py:attribute:: niscope.TriggerCoupling.HF_REJECT



        HF Reject filter.

        



    .. py:attribute:: niscope.TriggerCoupling.LF_REJECT



        LF Reject filter.

        



    .. py:attribute:: niscope.TriggerCoupling.AC_PLUS_HF_REJECT



        AC Plus HF Reject filter.

        




.. py:data:: TriggerModifier

    .. py:attribute:: niscope.TriggerModifier.NONE



        Normal triggering.

        



    .. py:attribute:: niscope.TriggerModifier.AUTO_TRIGGER



        Software will trigger an acquisition automatically if no trigger arrives
        after a certain amount of time.

        




.. py:data:: TriggerSlope

    .. py:attribute:: niscope.TriggerSlope.NEGATIVE



        Specifies a falling edge (negative slope).

        



    .. py:attribute:: niscope.TriggerSlope.POSITIVE



        Specifies a rising edge (positive slope).

        




.. py:data:: TriggerType

    .. py:attribute:: niscope.TriggerType.EDGE



        Specifies an edge trigger.

        



    .. py:attribute:: niscope.TriggerType.VIDEO



        Specifies a video trigger.

        



    .. py:attribute:: niscope.TriggerType.IMMEDIATE



        Specifies an immediate trigger.

        



    .. py:attribute:: niscope.TriggerType.HYSTERESIS



        Specifies a hysteresis trigger.

        



    .. py:attribute:: niscope.TriggerType.DIGITAL



        Specifies a digital trigger.

        



    .. py:attribute:: niscope.TriggerType.WINDOW



        Specifies a window trigger.

        



    .. py:attribute:: niscope.TriggerType.SOFTWARE



        Specifies a software trigger.

        




.. py:data:: TriggerWindowMode

    .. py:attribute:: niscope.TriggerWindowMode.ENTERING



        Trigger occurs when a signal enters a window.

        



    .. py:attribute:: niscope.TriggerWindowMode.LEAVING



        Trigger occurs when a signal leaves a window.

        




.. py:data:: VerticalCoupling

    .. py:attribute:: niscope.VerticalCoupling.AC



        AC coupled

        



    .. py:attribute:: niscope.VerticalCoupling.DC



        DC coupled

        



    .. py:attribute:: niscope.VerticalCoupling.GROUND



        Ground coupled

        




.. py:data:: VideoPolarity

    .. py:attribute:: niscope.VideoPolarity.POSITIVE



        Specifies that the video signal has positive polarity.

        



    .. py:attribute:: niscope.VideoPolarity.NEGATIVE



        Specifies that the video signal has negative polarity.

        




.. py:data:: VideoSignalFormat

    .. py:attribute:: niscope.VideoSignalFormat.M_NTSC



        Specifies M-NTSC signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat.BG_PAL



        Specifies BG/PAL signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat.SECAM



        Specifies SECAM signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat.M_PAL



        Specifies M-PAL signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._480I59_94_FPS



        Specifies 480i/59.94 signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._480I60_FPS



        Specifies 480i/60 signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._480P59_94_FPS



        Specifies 480p/59.94 signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._480P60_FPS



        Specifies 480p/60 Fps signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._576I60_FPS



        Specifies 576i/60 fps signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._576P50_FPS



        Specifies 576p/50 Fps signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._720P30_FPS



        Specifies 720p/30 Fps signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._720P50_FPS



        Specifies 720p/50 Fps signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._720P59_94_FPS



        Specifies 720p/59.94 Fps signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._720P60_FPS



        Specifies 720p/60 Fps signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._1080I50_FPS



        Specifies 1080i/50 fps signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._1080I59_94_FPS



        Specifies 1080i/59.94 fps signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._1080I60_FPS



        Specifies 1080i/60 fps signal format.

        



    .. py:attribute:: niscope.VideoSignalFormat._1080P24_FPS



        Specifies 1080p/24 Fps signal format.

        




.. py:data:: VideoTriggerEvent

    .. py:attribute:: niscope.VideoTriggerEvent.FIELD_1



        Trigger on field 1 of the signal.

        



    .. py:attribute:: niscope.VideoTriggerEvent.FIELD_2



        Trigger on field 2 of the signal.

        



    .. py:attribute:: niscope.VideoTriggerEvent.ANY_FIELD



        Trigger on any field of the signal.

        



    .. py:attribute:: niscope.VideoTriggerEvent.ANY_LINE



        Trigger on the first line acquired.

        



    .. py:attribute:: niscope.VideoTriggerEvent.LINE_NUMBER



        Trigger on a specific line of a video signal. Valid values vary
        depending on the signal format.

        


