Enums
=====

Enums used in NI-SCOPE

.. py:currentmodule:: niscope



.. py:data:: AcquisitionStatus

    .. py:attribute:: AcquisitionStatus.COMPLETE



    .. py:attribute:: AcquisitionStatus.IN_PROGRESS



    .. py:attribute:: AcquisitionStatus.STATUS_UNKNOWN




.. py:data:: AcquisitionType

    .. py:attribute:: AcquisitionType.NORMAL



        Sets the digitizer to normal resolution mode. The digitizer can use real-time sampling or equivalent-time sampling.

        



    .. py:attribute:: AcquisitionType.FLEXRES



        Sets the digitizer to flexible resolution mode if supported.  The digitizer uses different hardware configurations to change the resolution depending on the sampling rate used.

        



    .. py:attribute:: AcquisitionType.DDC



        Sets the digitizer to DDC mode on the NI 5620/5621.

        




.. py:data:: ExportableSignals

    .. py:attribute:: ExportableSignals.START_TRIGGER



    .. py:attribute:: ExportableSignals.ADVANCE_TRIGGER



    .. py:attribute:: ExportableSignals.REF_TRIGGER



    .. py:attribute:: ExportableSignals.END_OF_RECORD_EVENT



    .. py:attribute:: ExportableSignals.END_OF_ACQUISITION_EVENT



    .. py:attribute:: ExportableSignals.READY_FOR_START_EVENT



    .. py:attribute:: ExportableSignals.READY_FOR_ADVANCE_EVENT



    .. py:attribute:: ExportableSignals.READY_FOR_REF_EVENT



    .. py:attribute:: ExportableSignals.REF_CLOCK



    .. py:attribute:: ExportableSignals.SAMPLE_CLOCK



    .. py:attribute:: ExportableSignals.FIVE_V_OUT




.. py:data:: FetchRelativeTo

    .. py:attribute:: FetchRelativeTo.READ_POINTER



        The read pointer is set to zero when a new acquisition is initiated. After every fetch the read pointer is incremeted to be the sample after the last sample retrieved.  Therefore, you can repeatedly fetch relative to the read pointer for a continuous acquisition program.

        



    .. py:attribute:: FetchRelativeTo.PRETRIGGER



        Fetches relative to the first pretrigger point requested with :py:meth:`niscope.Session.configure_horizontal_timing`.

        



    .. py:attribute:: FetchRelativeTo.NOW



        Fetch data at the last sample acquired.

        



    .. py:attribute:: FetchRelativeTo.START



        Fetch data starting at the first point sampled by the digitizer.

        



    .. py:attribute:: FetchRelativeTo.TRIGGER



        Fetch at the first posttrigger sample.

        




.. py:data:: FlexFIRAntialiasFilterType

    .. py:attribute:: FlexFIRAntialiasFilterType.FOURTYEIGHT_TAP_STANDARD



        This filter is optimized for alias protection and frequency-domain flatness

        



    .. py:attribute:: FlexFIRAntialiasFilterType.FOURTYEIGHT_TAP_HANNING



        This filter is optimized for the lowest possible bandwidth for a 48 tap filter and maximizes the SNR

        



    .. py:attribute:: FlexFIRAntialiasFilterType.SIXTEEN_TAP_HANNING



        This filter is optimized for the lowest possible bandwidth for a 16 tap filter and maximizes the SNR

        



    .. py:attribute:: FlexFIRAntialiasFilterType.EIGHT_TAP_HANNING



        This filter is optimized for the lowest possible bandwidth for a 8 tap filter and maximizes the SNR

        




.. py:data:: Option

    .. py:attribute:: Option.SELF_CALIBRATE_ALL_CHANNELS



        Self Calibrating all Channels

        



    .. py:attribute:: Option.RESTORE_EXTERNAL_CALIBRATION



        Restore External Calibration.

        




.. py:data:: RISMethod

    .. py:attribute:: RISMethod.EXACT_NUM_AVERAGES



        Acquires exactly the specified number of records for each bin in the RIS acquisition.  An error is returned from the fetch method if the RIS acquisition does not successfully acquire the specified number of waveforms within the timeout period.  You may call the fetch method again to allow more time for the acquisition to finish.

        



    .. py:attribute:: RISMethod.MIN_NUM_AVERAGES



        Each RIS sample is the average of a least a minimum number of randomly
        distributed points.

        



    .. py:attribute:: RISMethod.INCOMPLETE



        Returns the RIS waveform after the specified timeout even if it is incomplete.  If no waveforms have been acquired in certain bins, these bins will have a NaN (when fetching scaled data) or a zero (when fetching binary data). A warning (positive error code) is returned from the fetch method if the RIS acquisition did not finish.  The acquisition aborts when data is returned.

        



    .. py:attribute:: RISMethod.LIMITED_BIN_WIDTH



        Limits the waveforms in the various bins to be within 200 ps of the center of the bin.

        




.. py:data:: RefTriggerDetectorLocation

    .. py:attribute:: RefTriggerDetectorLocation.ANALOG_DETECTION_CIRCUIT



        use the hardware analog circuitry to implement the reference trigger.  This option will trigger before any onboard signal processing.

        



    .. py:attribute:: RefTriggerDetectorLocation.DDC_OUTPUT



        use the onboard signal processing logic to implement the reference trigger.  This option will trigger based on the onboard signal processed data.

        




.. py:data:: TerminalConfiguration

    .. py:attribute:: TerminalConfiguration.SINGLE_ENDED



        Channel is single ended

        



    .. py:attribute:: TerminalConfiguration.UNBALANCED_DIFFERENTIAL



        Channel is unbalanced differential

        



    .. py:attribute:: TerminalConfiguration.DIFFERENTIAL



        Channel is differential

        




.. py:data:: TriggerCoupling

    .. py:attribute:: TriggerCoupling.AC



        AC coupling

        



    .. py:attribute:: TriggerCoupling.DC



        DC coupling

        



    .. py:attribute:: TriggerCoupling.HF_REJECT



        Highpass filter coupling

        



    .. py:attribute:: TriggerCoupling.LF_REJECT



        Lowpass filter coupling

        



    .. py:attribute:: TriggerCoupling.AC_PLUS_HF_REJECT



        Highpass and lowpass filter coupling

        




.. py:data:: TriggerModifier

    .. py:attribute:: TriggerModifier.NO_TRIGGER_MOD



        Normal triggering.

        



    .. py:attribute:: TriggerModifier.AUTO



        Software will trigger an acquisition automatically if no trigger arrives
        after a certain amount of time.

        




.. py:data:: TriggerSlope

    .. py:attribute:: TriggerSlope.NEGATIVE



        Falling edge

        



    .. py:attribute:: TriggerSlope.POSITIVE



        Rising edge

        




.. py:data:: TriggerType

    .. py:attribute:: TriggerType.EDGE



        Configures the digitizer for edge triggering.  An edge trigger occurs when the trigger signal crosses the trigger level specified with the set trigger slope.  You configure the trigger level and slope with :py:meth:`niscope.Session.configure_trigger_edge`.

        



    .. py:attribute:: TriggerType.TV



        Configures the digitizer for video/TV triggering.   You configure the video trigger parameters like signal Format, Line to trigger off of, Polarity, and Enable DC Restore with :py:meth:`niscope.Session.configure_trigger_video`.

        



    .. py:attribute:: TriggerType.IMMEDIATE



        Configures the digitizer for immediate triggering.   An immediate trigger occurs as soon as the pretrigger samples are acquired.

        



    .. py:attribute:: TriggerType.HYSTERESIS



        Configures the digitizer for hysteresis triggering.  A hysteresis trigger occurs when the trigger signal crosses the trigger level with the specified slope and passes through the hysteresis window you specify. You configure the trigger level, slope, and hysteresis with :py:meth:`niscope.Session.configure_trigger_hysteresis`.

        



    .. py:attribute:: TriggerType.DIGITAL



        Configures the digitizer for digital triggering. A digital trigger occurs when the trigger signal has the specified slope. You configure the trigger slope with :py:meth:`niscope.Session.configure_trigger_digital`.

        



    .. py:attribute:: TriggerType.WINDOW



        Configures the digitizer for window triggering.  A window trigger occurs when the trigger signal enters or leaves the window defined by the values you specify with the Low Window Level, High Window Level, and Window Mode Parameters.  You configure the low window level high window level, and window mode with :py:meth:`niscope.Session.configure_trigger_window`.

        



    .. py:attribute:: TriggerType.SOFTWARE



        Configures the digitizer for software triggering.  A software trigger occurs when :py:meth:`niscope.Session.SendSoftwareTrigger` is called.

        




.. py:data:: TriggerWindowMode

    .. py:attribute:: TriggerWindowMode.ENTERING



        Trigger upon entering the window

        



    .. py:attribute:: TriggerWindowMode.LEAVING



        Trigger upon leaving the window

        




.. py:data:: VerticalCoupling

    .. py:attribute:: VerticalCoupling.AC



        AC coupling

        



    .. py:attribute:: VerticalCoupling.DC



        DC coupling

        



    .. py:attribute:: VerticalCoupling.GND



        GND coupling

        




.. py:data:: VideoPolarity

    .. py:attribute:: VideoPolarity.POSITIVE



        Specifies that the video signal has positive polarity.

        



    .. py:attribute:: VideoPolarity.NEGATIVE



        Specifies that the video signal has negative polarity.

        




.. py:data:: VideoSignalFormat

    .. py:attribute:: VideoSignalFormat.NTSC



        NTSC signal format supports line numbers from 1 to 525

        



    .. py:attribute:: VideoSignalFormat.PAL



        PAL signal format supports line numbers from 1 to 625

        



    .. py:attribute:: VideoSignalFormat.SECAM



        SECAM signal format supports line numbers from 1 to 625

        



    .. py:attribute:: VideoSignalFormat.M_PAL



        M-PAL signal format supports line numbers from 1 to 525

        



    .. py:attribute:: VideoSignalFormat.VIDEO_480I_59_94_FIELDS_PER_SECOND



        480 lines, interlaced, 59.94 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_480I_60_FIELDS_PER_SECOND



        480 lines, interlaced, 60 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_480P_59_94_FRAMES_PER_SECOND



        480 lines, progressive, 59.94 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_480P_60_FRAMES_PER_SECOND



        480 lines, progressive,60 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_576I_50_FIELDS_PER_SECOND



        576 lines, interlaced, 50 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_576P_50_FRAMES_PER_SECOND



        576 lines, progressive, 50 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_720P_50_FRAMES_PER_SECOND



        720 lines, progressive, 50 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_720P_59_94_FRAMES_PER_SECOND



        720 lines, progressive, 59.94 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_720P_60_FRAMES_PER_SECOND



        720 lines, progressive, 60 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_1080I_50_FIELDS_PER_SECOND



        1,080 lines, interlaced, 50 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_1080I_59_94_FIELDS_PER_SECOND



        1,080 lines, interlaced, 59.94 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_1080I_60_FIELDS_PER_SECOND



        1,080 lines, interlaced, 60 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_1080P_24_FRAMES_PER_SECOND



        1,080 lines, progressive, 24 frames per second

        




.. py:data:: VideoTriggerEvent

    .. py:attribute:: VideoTriggerEvent.FIELD1



        Trigger on field 1 of the signal

        



    .. py:attribute:: VideoTriggerEvent.FIELD2



        Trigger on field 2 of the signal

        



    .. py:attribute:: VideoTriggerEvent.ANY_FIELD



        Trigger on the first field acquired

        



    .. py:attribute:: VideoTriggerEvent.ANY_LINE



        Trigger on the first line acquired

        



    .. py:attribute:: VideoTriggerEvent.LINE_NUMBER



        Trigger on a specific line of a video signal.  Valid values vary depending on the signal format configured.

        




.. py:data:: WhichTrigger

    .. py:attribute:: WhichTrigger.START



    .. py:attribute:: WhichTrigger.ARM_REFERENCE



    .. py:attribute:: WhichTrigger.REFERENCE



    .. py:attribute:: WhichTrigger.ADVANCE


