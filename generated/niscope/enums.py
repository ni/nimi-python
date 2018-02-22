# This file was generated

from enum import Enum


class AcquisitionStatus(Enum):
    COMPLETE = 1
    IN_PROGRESS = 0
    STATUS_UNKNOWN = -1


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


class ClearableMeasurement(Enum):
    ALL_MEASUREMENTS = 10000
    MULTI_ACQ_VOLTAGE_HISTOGRAM = 4004
    MULTI_ACQ_TIME_HISTOGRAM = 4005
    MULTI_ACQ_AVERAGE = 4016
    FREQUENCY = 2
    AVERAGE_FREQUENCY = 1016
    FFT_FREQUENCY = 1008
    PERIOD = 3
    AVERAGE_PERIOD = 1015
    RISE_TIME = 0
    FALL_TIME = 1
    RISE_SLEW_RATE = 1010
    FALL_SLEW_RATE = 1011
    OVERSHOOT = 18
    PRESHOOT = 19
    VOLTAGE_RMS = 4
    VOLTAGE_CYCLE_RMS = 16
    AC_ESTIMATE = 1012
    FFT_AMPLITUDE = 1009
    VOLTAGE_AVERAGE = 10
    VOLTAGE_CYCLE_AVERAGE = 17
    DC_ESTIMATE = 1013
    VOLTAGE_MAX = 6
    VOLTAGE_MIN = 7
    VOLTAGE_PEAK_TO_PEAK = 5
    VOLTAGE_HIGH = 8
    VOLTAGE_LOW = 9
    AMPLITUDE = 15
    VOLTAGE_TOP = 1007
    VOLTAGE_BASE = 1006
    VOLTAGE_BASE_TO_TOP = 1017
    WIDTH_NEG = 11
    WIDTH_POS = 12
    DUTY_CYCLE_NEG = 13
    DUTY_CYCLE_POS = 14
    INTEGRAL = 1005
    AREA = 1003
    CYCLE_AREA = 1004
    TIME_DELAY = 1014
    PHASE_DELAY = 1018
    LOW_REF_VOLTS = 1000
    MID_REF_VOLTS = 1001
    HIGH_REF_VOLTS = 1002
    VOLTAGE_HISTOGRAM_MEAN = 2000
    VOLTAGE_HISTOGRAM_STDEV = 2001
    VOLTAGE_HISTOGRAM_MEDIAN = 2003
    VOLTAGE_HISTOGRAM_MODE = 2010
    VOLTAGE_HISTOGRAM_MAX = 2005
    VOLTAGE_HISTOGRAM_MIN = 2006
    VOLTAGE_HISTOGRAM_PEAK_TO_PEAK = 2002
    VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV = 2007
    VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV = 2008
    VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV = 2009
    VOLTAGE_HISTOGRAM_HITS = 2004
    VOLTAGE_HISTOGRAM_NEW_HITS = 2011
    TIME_HISTOGRAM_MEAN = 3000
    TIME_HISTOGRAM_STDEV = 3001
    TIME_HISTOGRAM_MEDIAN = 3003
    TIME_HISTOGRAM_MODE = 3010
    TIME_HISTOGRAM_MAX = 3005
    TIME_HISTOGRAM_MIN = 3006
    TIME_HISTOGRAM_PEAK_TO_PEAK = 3002
    TIME_HISTOGRAM_MEAN_PLUS_STDEV = 3007
    TIME_HISTOGRAM_MEAN_PLUS_2_STDEV = 3008
    TIME_HISTOGRAM_MEAN_PLUS_3_STDEV = 3009
    TIME_HISTOGRAM_HITS = 3004
    TIME_HISTOGRAM_NEW_HITS = 3011


class DataProcessingMode(Enum):
    REAL = 0
    '''
    The waveform data points are real numbers (I data).
    '''
    COMPLEX = 1
    '''
    The waveform data points are complex numbers (IQ data).
    '''


class ExportableSignals(Enum):
    START_TRIGGER = 2
    ADVANCE_TRIGGER = 5
    REF_TRIGGER = 1
    END_OF_RECORD_EVENT = 4
    END_OF_ACQUISITION_EVENT = 3
    READY_FOR_START_EVENT = 7
    READY_FOR_ADVANCE_EVENT = 6
    READY_FOR_REF_EVENT = 10
    REF_CLOCK = 100
    SAMPLE_CLOCK = 101
    _5V_OUT = 13


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
    Fetches relative to the first pretrigger point requested with configure_horizontal_timing.
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


class Option(Enum):
    SELF_CALIBRATE_ALL_CHANNELS = 0
    '''
    Self Calibrating all Channels
    '''
    RESTORE_EXTERNAL_CALIBRATION = 1
    '''
    Restore External Calibration.
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


class RISMethod(Enum):
    EXACT_NUM_AVERAGES = 1
    '''
    Acquires exactly the specified number of records for each bin in the RIS acquisition.  An error is returned from the fetch method if the RIS acquisition does not successfully acquire the specified number of waveforms within the timeout period.  You may call the fetch method again to allow more time for the acquisition to finish.
    '''
    MIN_NUM_AVERAGES = 2
    '''
    Each RIS sample is the average of a least a minimum number of randomly
    distributed points.
    '''
    INCOMPLETE = 3
    '''
    Returns the RIS waveform after the specified timeout even if it is incomplete.  If no waveforms have been acquired in certain bins, these bins will have a NaN (when fetching scaled data) or a zero (when fetching binary data). A warning (positive error code) is returned from the fetch method if the RIS acquisition did not finish.  The acquisition aborts when data is returned.
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


class ScalarMeasurement(Enum):
    NO_MEASUREMENT = 4000
    '''
    None
    '''
    FREQUENCY = 2
    AVERAGE_FREQUENCY = 1016
    FFT_FREQUENCY = 1008
    PERIOD = 3
    AVERAGE_PERIOD = 1015
    RISE_TIME = 0
    FALL_TIME = 1
    RISE_SLEW_RATE = 1010
    FALL_SLEW_RATE = 1011
    OVERSHOOT = 18
    PRESHOOT = 19
    VOLTAGE_RMS = 4
    VOLTAGE_CYCLE_RMS = 16
    AC_ESTIMATE = 1012
    FFT_AMPLITUDE = 1009
    VOLTAGE_AVERAGE = 10
    VOLTAGE_CYCLE_AVERAGE = 17
    DC_ESTIMATE = 1013
    VOLTAGE_MAX = 6
    VOLTAGE_MIN = 7
    VOLTAGE_PEAK_TO_PEAK = 5
    VOLTAGE_HIGH = 8
    VOLTAGE_LOW = 9
    AMPLITUDE = 15
    VOLTAGE_TOP = 1007
    VOLTAGE_BASE = 1006
    VOLTAGE_BASE_TO_TOP = 1017
    WIDTH_NEG = 11
    WIDTH_POS = 12
    DUTY_CYCLE_NEG = 13
    DUTY_CYCLE_POS = 14
    INTEGRAL = 1005
    AREA = 1003
    CYCLE_AREA = 1004
    TIME_DELAY = 1014
    PHASE_DELAY = 1018
    LOW_REF_VOLTS = 1000
    MID_REF_VOLTS = 1001
    HIGH_REF_VOLTS = 1002
    VOLTAGE_HISTOGRAM_MEAN = 2000
    VOLTAGE_HISTOGRAM_STDEV = 2001
    VOLTAGE_HISTOGRAM_MEDIAN = 2003
    VOLTAGE_HISTOGRAM_MODE = 2010
    VOLTAGE_HISTOGRAM_MAX = 2005
    VOLTAGE_HISTOGRAM_MIN = 2006
    VOLTAGE_HISTOGRAM_PEAK_TO_PEAK = 2002
    VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV = 2007
    VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV = 2008
    VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV = 2009
    VOLTAGE_HISTOGRAM_HITS = 2004
    VOLTAGE_HISTOGRAM_NEW_HITS = 2011
    TIME_HISTOGRAM_MEAN = 3000
    TIME_HISTOGRAM_STDEV = 3001
    TIME_HISTOGRAM_MEDIAN = 3003
    TIME_HISTOGRAM_MODE = 3010
    TIME_HISTOGRAM_MAX = 3005
    TIME_HISTOGRAM_MIN = 3006
    TIME_HISTOGRAM_PEAK_TO_PEAK = 3002
    TIME_HISTOGRAM_MEAN_PLUS_STDEV = 3008
    TIME_HISTOGRAM_MEAN_PLUS_2_STDEV = 3009
    TIME_HISTOGRAM_HITS = 3004
    TIME_HISTOGRAM_NEW_HITS = 3011


class StreamingPositionType(Enum):
    START = 0
    '''
    Data is streamed from the start trigger.
    '''
    REFERENCE = 1
    '''
    Data is streamed relative to the reference trigger and reference
    position.
    '''
    SYNC = 2
    '''
    Data is streamed relative to the sync trigger and reference position.
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
    Configures the digitizer for edge triggering.  An edge trigger occurs when the trigger signal crosses the trigger level specified with the set trigger slope.  You configure the trigger level and slope with configure_trigger_edge.
    '''
    TV = 5
    '''
    Configures the digitizer for video/TV triggering.   You configure the video trigger parameters like signal Format, Line to trigger off of, Polarity, and Enable DC Restore with configure_trigger_video.
    '''
    IMMEDIATE = 6
    '''
    Configures the digitizer for immediate triggering.   An immediate trigger occurs as soon as the pretrigger samples are acquired.
    '''
    HYSTERESIS = 1001
    '''
    Configures the digitizer for hysteresis triggering.  A hysteresis trigger occurs when the trigger signal crosses the trigger level with the specified slope and passes through the hysteresis window you specify. You configure the trigger level, slope, and hysteresis with configure_trigger_hysteresis.
    '''
    DIGITAL = 1002
    '''
    Configures the digitizer for digital triggering. A digital trigger occurs when the trigger signal has the specified slope. You configure the trigger slope with configure_trigger_digital.
    '''
    WINDOW = 1003
    '''
    Configures the digitizer for window triggering.  A window trigger occurs when the trigger signal enters or leaves the window defined by the values you specify with the Low Window Level, High Window Level, and Window Mode Parameters.  You configure the low window level high window level, and window mode with configure_trigger_window.
    '''
    SOFTWARE = 1004
    '''
    Configures the digitizer for software triggering.  A software trigger occurs when SendSoftwareTrigger is called.
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


class WhichTrigger(Enum):
    START = 0
    ARM_REFERENCE = 1
    REFERENCE = 2
    ADVANCE = 3
