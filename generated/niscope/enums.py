# This file was generated

from enum import Enum


class AGCAverageControl(Enum):
    MEAN = 0
    '''
    Mean average.
    '''
    MEDIAN = 1
    '''
    Median average.
    '''


class AOUTParallelOutputSource(Enum):
    I_DATA = 0
    '''
    Specifies I data as the source for the AOUT parallel output from the
    DDC.
    '''
    MAGNITUDE_DATA = 1
    '''
    Specifies magnitude data as the source for the AOUT parallel output from
    the DDC.
    '''
    FREQUENCY_DATA = 2
    '''
    Specifies frequency data as the source for the AOUT parallel output from
    the DDC.
    '''


class AcquisitionType(Enum):
    NORMAL = 0
    '''
    Sets the digitizer to normal resolution mode. The digitizer can use real-time sampling or equivalent-time sampling.
    '''
    FLEXRES = 1001
    '''
    Sets the digitizer to flexible resolution mode if supported.  The digitizer uses different hardware configurations to change the resolution depending on the sampling rate used.
    '''
    DDC = 1002
    '''
    Sets the digitizer to DDC mode on the NI 5620/5621.
    '''


class AddressType(Enum):
    PHYSICAL = 0
    '''
    Physical address.
    '''
    VIRTUAL = 1
    '''
    Virtual address.
    '''


class BOUTParallelOutputSource(Enum):
    MAGNITUDE_DATA = 1
    '''
    Specifies magnitude data as the source.
    '''
    Q_DATA = 3
    '''
    Specifies Q data as the source.
    '''
    PHASE_DATA = 4
    '''
    Specifies phase data as the source.
    '''


class BoolEnableDisable(Enum):
    DISABLED = 0
    '''
    Disabled
    '''
    ENABLED = 1
    '''
    Enabled
    '''


class BoolEnableDisableChan(Enum):
    DISABLED = 0
    '''
    Does not acquire a waveform for the channel.
    '''
    ENABLED = 1
    '''
    Acquires a waveform for the channel.
    '''


class BoolEnableDisableIQ(Enum):
    DISABLED = 0
    '''
    A scalar fetch returns an array of waveforms in the following format:
    III...QQQ...
    '''
    ENABLED = 1
    '''
    (Default) A scalar fetch returns an array of waveforms in the following
    format: IQIQIQ...
    '''


class BoolEnableDisableRealtime(Enum):
    DISABLED = 0
    '''
    Allow both real-time and equivalent-time measurements.
    '''
    ENABLED = 1
    '''
    Allow only real-time measurements.
    '''


class BoolEnableDisableTIS(Enum):
    DISABLED = 0
    '''
    (Default) Use only this channel's ADC to acquire data for this channel.
    '''
    ENABLED = 1
    '''
    Use multiple interleaved ADCs to acquire data for this channel.
    '''


class CoordinateConverterInput(Enum):
    RESAMPLER_HB = 0
    '''
    Selects the HB filter as the source for the input to the coordinate
    converter.
    '''
    PROGRAMMABLE_FIR = 1
    '''
    Selects the programmable FIR filter as the source for the input to the
    coordinate converter.
    '''


class DataJustificationMode(Enum):
    LEFT = 1
    RIGHT = 2


class DataProcessingMode(Enum):
    REAL = 0
    '''
    The waveform data points are real numbers (I data).
    '''
    COMPLEX = 1
    '''
    The waveform data points are complex numbers (IQ data).
    '''


class DiscriminatorFIRInputSource(Enum):
    PHASE = 0
    '''
    Sets the discriminator FIR input source to phase.
    '''
    MAGNITUDE = 1
    '''
    Sets the discriminator FIR input source to magnitude.
    '''
    RESAMPLER = 3
    '''
    Sets the discriminator FIR input source to resampler.
    '''


class DiscriminatorFIRSymmetry(Enum):
    SYMMETRIC = 0
    '''
    Sets the discriminator FIR symmetry to symmetric.
    '''
    ASYMMETRIC = 1
    '''
    Sets the discriminator FIR symmetry to asymmetric.
    '''


class DiscriminatorFIRSymmetryType(Enum):
    EVEN = 0
    '''
    Sets the discriminator FIR symmetry type to even.
    '''
    ODD = 1
    '''
    Sets the discriminator FIR symmetry type to odd.
    '''


class FIRFilterWindow(Enum):
    NONE = 0
    '''
    No window.
    '''
    HANNING = 409
    '''
    Specifies a Hanning window.
    '''
    FLAT_TOP = 410
    '''
    Specifies a Flat Top window.
    '''
    HAMMING = 420
    '''
    Specifies a Hamming window.
    '''
    TRIANGLE = 423
    '''
    Specifies a Triangle window.
    '''
    BLACKMAN = 424
    '''
    Specifies a Blackman window.
    '''


class FetchRelativeTo(Enum):
    READ_POINTER = 388
    '''
    The read pointer is set to zero when a new acquisition is initiated. After every fetch the read pointer is incremeted to be the sample after the last sample retrieved.  Therefore, you can repeatedly fetch relative to the read pointer for a continuous acquisition program.
    '''
    PRETRIGGER = 477
    '''
    Fetches relative to the first pretrigger point requested with niScope_ConfigureHorizontalTiming.
    '''
    NOW = 481
    '''
    Fetch data at the last sample acquired.
    '''
    START = 482
    '''
    Fetch data starting at the first point sampled by the digitizer.
    '''
    TRIGGER = 483
    '''
    Fetch at the first posttrigger sample.
    '''


class FilterType(Enum):
    LOWPASS = 0
    '''
    Specifies lowpass as the filter type.
    '''
    HIGHPASS = 1
    '''
    Specifies highpass as the filter type.
    '''
    BANDPASS = 2
    '''
    Specifies bandpass as the filter type.
    '''
    BANDSTOP = 3
    '''
    Specifies bandstop as the filter type.
    '''


class FlexFIRAntialiasFilterType(Enum):
    _48_TAP_STANDARD = 0
    '''
    This filter is optimized for alias protection and frequency-domain flatness
    '''
    _48_TAP_HANNING = 1
    '''
    This filter is optimized for the lowest possible bandwidth for a 48 tap filter and maximizes the SNR
    '''
    _16_TAP_HANNING = 2
    '''
    This filter is optimized for the lowest possible bandwidth for a 16 tap filter and maximizes the SNR
    '''
    _8_TAP_HANNING = 3
    '''
    This filter is optimized for the lowest possible bandwidth for a 8 tap filter and maximizes the SNR
    '''


class NotificationType(Enum):
    NEVER = 0
    '''
    Never send notification.
    '''
    DONE = 1
    '''
    Notify when digitizer acquisition is done.
    '''


class OverflowErrorReporting(Enum):
    ERROR = 0
    '''
    Execution stops and NI-SCOPE returns an error when an overflow has
    occurred in the OSP block.
    '''
    WARNING = 1
    '''
    Execution continues and NI-SCOPE returns a warning when an overflow has
    occurred in the OSP block.
    '''
    DISABLED = 2
    '''
    NI-SCOPE does not return an error when an overflow has occurred in the
    OSP block.
    '''


class PercentageMethod(Enum):
    LOWHIGH = 0
    '''
    Specifies that the reference level percentages should be computed using
    the low/high method,
    '''
    MINMAX = 1
    '''
    Reference level percentages are computed using the min/max method.
    '''
    BASETOP = 2
    '''
    Reference level percentages are computed using the base/top method.
    '''


class ProgFIRFilterRealComplex(Enum):
    REAL = 0
    '''
    Sets a dual real filter.
    '''
    COMPLEX = 1
    '''
    Sets a complex filter.
    '''


class ProgFIRFilterSymmetry(Enum):
    SYMMETRIC = 0
    '''
    Sets a symmetric filter.
    '''
    ASYMMETRIC = 1
    '''
    Sets an asymmetric filter.
    '''


class ProgFIRFilterSymmetryType(Enum):
    EVEN = 0
    '''
    Sets the discriminator FIR symmetry type to even.
    '''
    ODD = 1
    '''
    Sets the discriminator FIR symmetry type to odd.
    '''


class QInputtoCoordConverter(Enum):
    I_AND_Q = 0
    '''
    Enables the Q input to coordinate converter.
    '''
    Q_ZEROED = 1
    '''
    Zeroes out the Q input the to coordinate converter.
    '''


class RISMethod(Enum):
    EXACT_NUM_AVERAGES = 1
    '''
    Acquires exactly the specified number of records for each bin in the RIS acquisition.  An error is returned from the fetch function if the RIS acquisition does not successfully acquire the specified number of waveforms within the timeout period.  You may call the fetch function again to allow more time for the acquisition to finish.
    '''
    MIN_NUM_AVERAGES = 2
    '''
    Each RIS sample is the average of a least a minimum number of randomly
    distributed points.
    '''
    INCOMPLETE = 3
    '''
    Returns the RIS waveform after the specified timeout even if it is incomplete.  If no waveforms have been acquired in certain bins, these bins will have a NaN (when fetching scaled data) or a zero (when fetching binary data). A warning (positive error code) is returned from the fetch function if the RIS acquisition did not finish.  The acquisition aborts when data is returned.
    '''
    LIMITED_BIN_WIDTH = 5
    '''
    Limits the waveforms in the various bins to be within 200 ps of the center of the bin.
    '''


class RefLevelUnits(Enum):
    VOLTS = 0
    '''
    Specifies that the reference levels are given in units of volts.
    '''
    PERCENTAGE = 1
    '''
    (Default) Specifies that the reference levels are given in percentage
    units.
    '''


class RefTriggerDetectorLocation(Enum):
    ANALOG_DETECTION_CIRCUIT = 0
    '''
    use the hardware analog circuitry to implement the reference trigger.  This option will trigger before any onboard signal processing.
    '''
    DDC_OUTPUT = 1
    '''
    use the onboard signal processing logic to implement the reference trigger.  This option will trigger based on the onboard signal processed data.
    '''


class ResamplerFilterMode(Enum):
    RESAMPLER_ENABLED = 1
    '''
    Resampler enabled.
    '''
    HB_1_ENABLED = 2
    '''
    HB 1 enabled.
    '''
    RESAMPLER_AND_HB_1 = 3
    '''
    Resampler and HB 1.
    '''
    BOTH_HB_FILTERS = 6
    '''
    Both HB Filters.
    '''
    RESAMPLER_AND_BOTH_HB_FILTERS = 7
    '''
    Resampler and Both HB Filters.
    '''


class StreamingPositionType(Enum):
    START_TRIGGER = 0
    '''
    Data is streamed from the start trigger.
    '''
    REFERENCE_TRIGGER = 1
    '''
    Data is streamed relative to the reference trigger and reference
    position.
    '''
    SYNC_TRIGGER = 2
    '''
    Data is streamed relative to the sync trigger and reference position.
    '''


class SyncoutCLKSelect(Enum):
    CLKIN = 0
    '''
    Specifies CLKIN as the source for Syncout CLK.
    '''
    PROCCLK = 1
    '''
    Specifies PROCCLK as the source for Syncout CLK.
    '''


class TerminalConfiguration(Enum):
    SINGLE_ENDED = 0
    '''
    Channel is single ended
    '''
    UNBALANCED_DIFFERENTIAL = 1
    '''
    Channel is unbalanced differential
    '''
    DIFFERENTIAL = 2
    '''
    Channel is differential
    '''


class TimingNCOFreqOffsetBits(Enum):
    _8_BITS = 0
    '''
    Specifies 8 offset bits in the timing NCO.
    '''
    _16_BITS = 1
    '''
    Specifies 16 offset bits in the timing NCO.
    '''
    _24_BITS = 2
    '''
    Specifies 24 offset bits in the timing NCO.
    '''
    _32_BITS = 3
    '''
    Specifies 32 offset bits in the timing NCO.
    '''


class TriggerCoupling(Enum):
    AC = 0
    '''
    AC coupling
    '''
    DC = 1
    '''
    DC coupling
    '''
    HF_REJECT = 2
    '''
    Highpass filter coupling
    '''
    LF_REJECT = 3
    '''
    Lowpass filter coupling
    '''
    AC_PLUS_HF_REJECT = 1001
    '''
    Highpass and lowpass filter coupling
    '''


class TriggerModifier(Enum):
    NO_TRIGGER_MOD = 1
    '''
    Normal triggering.
    '''
    AUTO = 2
    '''
    Software will trigger an acquisition automatically if no trigger arrives
    after a certain amount of time.
    '''


class TriggerSlope(Enum):
    NEGATIVE = 0
    '''
    Falling edge
    '''
    POSITIVE = 1
    '''
    Rising edge
    '''


class TriggerType(Enum):
    EDGE = 1
    '''
    Configures the digitizer for edge triggering.  An edge trigger occurs when the trigger signal crosses the trigger level specified with the set trigger slope.  You configure the trigger level and slope with niScope_ConfigureTriggerEdge.
    '''
    TV = 5
    '''
    Configures the digitizer for video/TV triggering.   You configure the video trigger parameters like signal Format, Line to trigger off of, Polarity, and Enable DC Restore with niScope_ConfigureTriggerVideo.
    '''
    IMMEDIATE = 6
    '''
    Configures the digitizer for immediate triggering.   An immediate trigger occurs as soon as the pretrigger samples are acquired.
    '''
    HYSTERESIS = 1001
    '''
    Configures the digitizer for hysteresis triggering.  A hysteresis trigger occurs when the trigger signal crosses the trigger level with the specified slope and passes through the hysteresis window you specify. You configure the trigger level, slope, and hysteresis with niScope_ConfigureTriggerHysteresis.
    '''
    DIGITAL = 1002
    '''
    Configures the digitizer for digital triggering. A digital trigger occurs when the trigger signal has the specified slope. You configure the trigger slope with niScope_ConfigureTriggerDigital.
    '''
    WINDOW = 1003
    '''
    Configures the digitizer for window triggering.  A window trigger occurs when the trigger signal enters or leaves the window defined by the values you specify with the Low Window Level, High Window Level, and Window Mode Parameters.  You configure the low window level high window level, and window mode with niScope_ConfigureTriggerWindow.
    '''
    SOFTWARE = 1004
    '''
    Configures the digitizer for software triggering.  A software trigger occurs when niScope_SendSoftwareTrigger is called.
    '''


class TriggerWindowMode(Enum):
    ENTERING = 0
    '''
    Trigger upon entering the window
    '''
    LEAVING = 1
    '''
    Trigger upon leaving the window
    '''


class VerticalCoupling(Enum):
    AC = 0
    '''
    AC coupling
    '''
    DC = 1
    '''
    DC coupling
    '''
    GND = 2
    '''
    GND coupling
    '''


class VideoPolarity(Enum):
    POSITIVE = 1
    '''
    Specifies that the video signal has positive polarity.
    '''
    NEGATIVE = 2
    '''
    Specifies that the video signal has negative polarity.
    '''


class VideoSignalFormat(Enum):
    NTSC = 1
    '''
    NTSC signal format supports line numbers from 1 to 525
    '''
    PAL = 2
    '''
    PAL signal format supports line numbers from 1 to 625
    '''
    SECAM = 3
    '''
    SECAM signal format supports line numbers from 1 to 625
    '''
    M_PAL = 1001
    '''
    M-PAL signal format supports line numbers from 1 to 525
    '''
    _480I_59_94_FIELDS_PER_SECOND = 1010
    '''
    480 lines, interlaced, 59.94 fields per second
    '''
    _480I_60_FIELDS_PER_SECOND = 1011
    '''
    480 lines, interlaced, 60 fields per second
    '''
    _480P_59_94_FRAMES_PER_SECOND = 1015
    '''
    480 lines, progressive, 59.94 frames per second
    '''
    _480P_60_FRAMES_PER_SECOND = 1016
    '''
    480 lines, progressive,60 frames per second
    '''
    _576I_50_FIELDS_PER_SECOND = 1020
    '''
    576 lines, interlaced, 50 fields per second
    '''
    _576P_50_FRAMES_PER_SECOND = 1025
    '''
    576 lines, progressive, 50 frames per second
    '''
    _720P_50_FRAMES_PER_SECOND = 1031
    '''
    720 lines, progressive, 50 frames per second
    '''
    _720P_59_94_FRAMES_PER_SECOND = 1032
    '''
    720 lines, progressive, 59.94 frames per second
    '''
    _720P_60_FRAMES_PER_SECOND = 1033
    '''
    720 lines, progressive, 60 frames per second
    '''
    _1080I_50_FIELDS_PER_SECOND = 1040
    '''
    1,080 lines, interlaced, 50 fields per second
    '''
    _1080I_59_94_FIELDS_PER_SECOND = 1041
    '''
    1,080 lines, interlaced, 59.94 fields per second
    '''
    _1080I_60_FIELDS_PER_SECOND = 1042
    '''
    1,080 lines, interlaced, 60 fields per second
    '''
    _1080P_24_FRAMES_PER_SECOND = 1045
    '''
    1,080 lines, progressive, 24 frames per second
    '''


class VideoTriggerEvent(Enum):
    FIELD1 = 1
    '''
    Trigger on field 1 of the signal
    '''
    FIELD2 = 2
    '''
    Trigger on field 2 of the signal
    '''
    ANY_FIELD = 3
    '''
    Trigger on the first field acquired
    '''
    ANY_LINE = 4
    '''
    Trigger on the first line acquired
    '''
    LINE_NUMBER = 5
    '''
    Trigger on a specific line of a video signal.  Valid values vary depending on the signal format configured.
    '''
