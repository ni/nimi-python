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
    Sets the digitizer to normal resolution mode. The digitizer can use
    real-time sampling or equivalent-time sampling.
    '''
    FLEX_RES = 1001
    '''
    Sets the digitizer to flexible resolution mode, if supported. The
    digitizer uses different hardware configurations to change the
    resolution depending on the sampling rate used.
    '''
    DDC = 1002
    '''
    Sets the NI 5620/5621digitizer to DDC mode.
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
    The read pointer is set to zero when a new acquisition is initiated.
    After every fetch the read pointer is incremented to be the sample after
    the last sample retrieved. Therefore, you can repeatedly fetch relative
    to the read pointer for a continuous acquisition program.
    '''
    PRETRIGGER = 477
    '''
    Fetches relative to the first pretrigger point requested with the
    niScope Configure Horizontal Timing VI.
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
    48 Tap Standard filter is optimized for alias protection and
    frequency-domain flatness.
    '''
    _48_TAP_HANNING = 1
    '''
    48 Tap Hanning filter is optimized for the lowest possible bandwidth for
    a 48 tap filter and maximizes the SNR.
    '''
    _16_TAP_HANNING = 2
    '''
    16 Tap Hanning is optimized for the lowest possible bandwidth for a 16
    tap filter and maximizes the SNR.
    '''
    _8_TAP_HANNING = 3
    '''
    8 Tap Hanning filter is optimized for the lowest possible bandwidth for
    a 8 tap filter and maximizes the SNR.
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


class Prog.FIRFilterReal/Complex(Enum):
    REAL = 0
    '''
    Sets a dual real filter.
    '''
    COMPLEX = 1
    '''
    Sets a complex filter.
    '''


class Prog.FIRFilterSymmetry(Enum):
    SYMMETRIC = 0
    '''
    Sets a symmetric filter.
    '''
    ASYMMETRIC = 1
    '''
    Sets an asymmetric filter.
    '''


class Prog.FIRFilterSymmetryType(Enum):
    EVEN = 0
    '''
    Sets the discriminator FIR symmetry type to even.
    '''
    ODD = 1
    '''
    Sets the discriminator FIR symmetry type to odd.
    '''


class QInputtoCoord.Converter(Enum):
    I_AND_Q = 0
    '''
    Enables the Q input to coordinate converter.
    '''
    Q_ZEROED = 1
    '''
    Zeroes out the Q input the to coordinate converter.
    '''


class RISMethod(Enum):
    EXACT_NUM_AVG_ = 1
    '''
    Acquires exactly the specified number of records for each bin in the RIS
    acquisition.
    '''
    MIN_NUM_AVG_ = 2
    '''
    Each RIS sample is the average of a least a minimum number of randomly
    distributed points.
    '''
    INCOMPLETE = 3
    '''
    If RIS does not complete in the allotted fetch time, the Fetch VI should
    abort and return the incomplete data. Any missing samples appear as NaN
    when fetching scaled data or zero when fetching binary data. A warning
    with a positive error code is returned from the Fetch VI if the RIS
    acquisition did not finish. The acquisition is aborted when data is
    returned.
    '''
    LIMIT_BIN_WIDTH = 5
    '''
    Each RIS sample is the average of Min Num Avg points distributed close
    to the sample period boundaries (within 200 ps). Points falling between
    sample periods are ignored.
    '''


class Ref.LevelUnits(Enum):
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
    (Default) Uses the hardware analog circuitry to implement the reference
    trigger. This option detects trigger conditions by analyzing the
    unprocessed analog signal.
    '''
    DDC_OUTPUT = 1
    '''
    Uses the onboard signal processing logic to implement the reference
    trigger. This option detects trigger conditions by analyzing the
    processed digital signal.
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
    Single-ended channel terminal configuration.
    '''
    UNBALANCED_DIFFERENTIAL = 1
    '''
    Unbalanced differential channel terminal configuration.
    '''
    DIFFERENTIAL = 2
    '''
    Differential channel terminal configuration.
    '''


class TimingNCOFreq.OffsetBits(Enum):
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
    AC coupled
    '''
    DC = 1
    '''
    DC coupled
    '''
    HF_REJECT = 3
    '''
    HF Reject filter.
    '''
    LF_REJECT = 4
    '''
    LF Reject filter.
    '''
    AC_PLUS_HF_REJECT = 1001
    '''
    AC Plus HF Reject filter.
    '''


class TriggerModifier(Enum):
    NONE = 1
    '''
    Normal triggering.
    '''
    AUTO_TRIGGER = 2
    '''
    Software will trigger an acquisition automatically if no trigger arrives
    after a certain amount of time.
    '''


class TriggerSlope(Enum):
    NEGATIVE = 0
    '''
    Specifies a falling edge (negative slope).
    '''
    POSITIVE = 1
    '''
    Specifies a rising edge (positive slope).
    '''


class TriggerType(Enum):
    EDGE = 1
    '''
    Specifies an edge trigger.
    '''
    VIDEO = 5
    '''
    Specifies a video trigger.
    '''
    IMMEDIATE = 6
    '''
    Specifies an immediate trigger.
    '''
    HYSTERESIS = 1001
    '''
    Specifies a hysteresis trigger.
    '''
    DIGITAL = 1002
    '''
    Specifies a digital trigger.
    '''
    WINDOW = 1003
    '''
    Specifies a window trigger.
    '''
    SOFTWARE = 1004
    '''
    Specifies a software trigger.
    '''


class TriggerWindowMode(Enum):
    ENTERING = 0
    '''
    Trigger occurs when a signal enters a window.
    '''
    LEAVING = 1
    '''
    Trigger occurs when a signal leaves a window.
    '''


class VerticalCoupling(Enum):
    AC = 0
    '''
    AC coupled
    '''
    DC = 1
    '''
    DC coupled
    '''
    GROUND = 2
    '''
    Ground coupled
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
    M_NTSC = 1
    '''
    Specifies M-NTSC signal format.
    '''
    BG_PAL = 2
    '''
    Specifies BG/PAL signal format.
    '''
    SECAM = 3
    '''
    Specifies SECAM signal format.
    '''
    M_PAL = 4
    '''
    Specifies M-PAL signal format.
    '''
    _480I59_94_FPS = 5
    '''
    Specifies 480i/59.94 signal format.
    '''
    _480I60_FPS = 6
    '''
    Specifies 480i/60 signal format.
    '''
    _480P59_94_FPS = 7
    '''
    Specifies 480p/59.94 signal format.
    '''
    _480P60_FPS = 8
    '''
    Specifies 480p/60 Fps signal format.
    '''
    _576I60_FPS = 9
    '''
    Specifies 576i/60 fps signal format.
    '''
    _576P50_FPS = 10
    '''
    Specifies 576p/50 Fps signal format.
    '''
    _720P30_FPS = 11
    '''
    Specifies 720p/30 Fps signal format.
    '''
    _720P50_FPS = 12
    '''
    Specifies 720p/50 Fps signal format.
    '''
    _720P59_94_FPS = 13
    '''
    Specifies 720p/59.94 Fps signal format.
    '''
    _720P60_FPS = 14
    '''
    Specifies 720p/60 Fps signal format.
    '''
    _1080I50_FPS = 15
    '''
    Specifies 1080i/50 fps signal format.
    '''
    _1080I59_94_FPS = 16
    '''
    Specifies 1080i/59.94 fps signal format.
    '''
    _1080I60_FPS = 17
    '''
    Specifies 1080i/60 fps signal format.
    '''
    _1080P24_FPS = 18
    '''
    Specifies 1080p/24 Fps signal format.
    '''


class VideoTriggerEvent(Enum):
    FIELD_1 = 1
    '''
    Trigger on field 1 of the signal.
    '''
    FIELD_2 = 2
    '''
    Trigger on field 2 of the signal.
    '''
    ANY_FIELD = 3
    '''
    Trigger on any field of the signal.
    '''
    ANY_LINE = 4
    '''
    Trigger on the first line acquired.
    '''
    LINE_NUMBER = 5
    '''
    Trigger on a specific line of a video signal. Valid values vary
    depending on the signal format.
    '''
