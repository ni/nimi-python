# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class AcquisitionStatus(Enum):
    COMPLETE = 1
    IN_PROGRESS = 0
    STATUS_UNKNOWN = -1


class AcquisitionType(Enum):
    NORMAL = 0
    r'''
    Sets the digitizer to normal resolution mode. The digitizer can use real-time sampling or equivalent-time sampling.
    '''
    FLEXRES = 1001
    r'''
    Sets the digitizer to flexible resolution mode if supported.  The digitizer uses different hardware configurations to change the resolution depending on the sampling rate used.
    '''
    DDC = 1002
    r'''
    Sets the digitizer to DDC mode on the NI 5620/5621.
    '''


class ArrayMeasurement(Enum):
    NO_MEASUREMENT = 4000
    r'''
    None
    '''
    LAST_ACQ_HISTOGRAM = 4001
    r'''
    Last Acquisition Histogram
    '''
    FFT_PHASE_SPECTRUM = 4002
    r'''
    FFT Phase Spectrum
    '''
    FFT_AMP_SPECTRUM_VOLTS_RMS = 4003
    r'''
    FFT Amp. Spectrum (Volts RMS)
    '''
    MULTI_ACQ_VOLTAGE_HISTOGRAM = 4004
    r'''
    Multi Acquisition Voltage Histogram
    '''
    MULTI_ACQ_TIME_HISTOGRAM = 4005
    r'''
    Multi Acquisition Time Histogram
    '''
    ARRAY_INTEGRAL = 4006
    r'''
    Array Integral
    '''
    DERIVATIVE = 4007
    r'''
    Derivative
    '''
    INVERSE = 4008
    r'''
    Inverse
    '''
    HANNING_WINDOW = 4009
    r'''
    Hanning Window
    '''
    FLAT_TOP_WINDOW = 4010
    r'''
    Flat Top Window
    '''
    POLYNOMIAL_INTERPOLATION = 4011
    r'''
    Polynomial Interpolation
    '''
    MULTIPLY_CHANNELS = 4012
    r'''
    Multiply Channels
    '''
    ADD_CHANNELS = 4013
    r'''
    Add Channels
    '''
    SUBTRACT_CHANNELS = 4014
    r'''
    Subtract Channels
    '''
    DIVIDE_CHANNELS = 4015
    r'''
    Divide Channels
    '''
    MULTI_ACQ_AVERAGE = 4016
    r'''
    Multi Acquisition Average
    '''
    BUTTERWORTH_FILTER = 4017
    r'''
    Butterworth IIR Filter
    '''
    CHEBYSHEV_FILTER = 4018
    r'''
    Chebyshev IIR Filter
    '''
    FFT_AMP_SPECTRUM_DB = 4019
    r'''
    FFT Amp. Spectrum (dB)
    '''
    HAMMING_WINDOW = 4020
    r'''
    Hamming Window
    '''
    WINDOWED_FIR_FILTER = 4021
    r'''
    FIR Windowed Filter
    '''
    BESSEL_FILTER = 4022
    r'''
    Bessel IIR Filter
    '''
    TRIANGLE_WINDOW = 4023
    r'''
    Triangle Window
    '''
    BLACKMAN_WINDOW = 4024
    r'''
    Blackman Window
    '''
    ARRAY_OFFSET = 4025
    r'''
    Array Offset
    '''
    ARRAY_GAIN = 4026
    r'''
    Array Gain
    '''


class CableSenseMode(Enum):
    DISABLED = 0
    r'''
    The oscilloscope is not configured to emit a CableSense signal.
    '''
    ON_DEMAND = 1
    r'''
    The oscilloscope is configured to emit a single CableSense pulse.
    '''


class _CalibrationTypes(Enum):
    SELF = 1
    EXTERNAL = 0
    MANUFACTURE = 2


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


class FIRFilterWindow(Enum):
    NONE = 0
    r'''
    No window.
    '''
    HANNING = 409
    r'''
    Specifies a Hanning window.
    '''
    FLAT_TOP = 410
    r'''
    Specifies a Flat Top window.
    '''
    HAMMING = 420
    r'''
    Specifies a Hamming window.
    '''
    TRIANGLE = 423
    r'''
    Specifies a Triangle window.
    '''
    BLACKMAN = 424
    r'''
    Specifies a Blackman window.
    '''


class FetchRelativeTo(Enum):
    READ_POINTER = 388
    r'''
    The read pointer is set to zero when a new acquisition is initiated. After every fetch the read pointer is incremeted to be the sample after the last sample retrieved.  Therefore, you can repeatedly fetch relative to the read pointer for a continuous acquisition program.
    '''
    PRETRIGGER = 477
    r'''
    Fetches relative to the first pretrigger point requested with configure_horizontal_timing.
    '''
    NOW = 481
    r'''
    Fetch data at the last sample acquired.
    '''
    START = 482
    r'''
    Fetch data starting at the first point sampled by the digitizer.
    '''
    TRIGGER = 483
    r'''
    Fetch at the first posttrigger sample.
    '''


class FilterType(Enum):
    LOWPASS = 0
    r'''
    Specifies lowpass as the filter type.
    '''
    HIGHPASS = 1
    r'''
    Specifies highpass as the filter type.
    '''
    BANDPASS = 2
    r'''
    Specifies bandpass as the filter type.
    '''
    BANDSTOP = 3
    r'''
    Specifies bandstop as the filter type.
    '''


class FlexFIRAntialiasFilterType(Enum):
    FOURTYEIGHT_TAP_STANDARD = 0
    r'''
    This filter is optimized for alias protection and frequency-domain flatness
    '''
    FOURTYEIGHT_TAP_HANNING = 1
    r'''
    This filter is optimized for the lowest possible bandwidth for a 48 tap filter and maximizes the SNR
    '''
    SIXTEEN_TAP_HANNING = 2
    r'''
    This filter is optimized for the lowest possible bandwidth for a 16 tap filter and maximizes the SNR
    '''
    EIGHT_TAP_HANNING = 3
    r'''
    This filter is optimized for the lowest possible bandwidth for a 8 tap filter and maximizes the SNR
    '''


class GlitchCondition(Enum):
    GREATER = 2
    r'''
    Trigger on pulses with a duration greater than the specified glitch width.
    '''
    LESS = 1
    r'''
    Trigger on pulses with a duration shorter than the specified glitch width.
    '''


class GlitchPolarity(Enum):
    POSITIVE = 1
    r'''
    Trigger on pulses of positive polarity relative to the trigger threshold.
    '''
    NEGATIVE = 2
    r'''
    Trigger on pulses of negative polarity relative to the trigger threshold.
    '''
    EITHER = 3
    r'''
    Trigger on pulses of either positive or negative polarity.
    '''


class Option(Enum):
    SELF_CALIBRATE_ALL_CHANNELS = 0
    r'''
    Self Calibrating all Channels
    '''
    RESTORE_EXTERNAL_CALIBRATION = 1
    r'''
    Restore External Calibration.
    '''


class PercentageMethod(Enum):
    LOWHIGH = 0
    r'''
    Specifies that the reference level percentages should be computed using
    the low/high method,
    '''
    MINMAX = 1
    r'''
    Reference level percentages are computed using the min/max method.
    '''
    BASETOP = 2
    r'''
    Reference level percentages are computed using the base/top method.
    '''


class RISMethod(Enum):
    EXACT_NUM_AVERAGES = 1
    r'''
    Acquires exactly the specified number of records for each bin in the RIS acquisition.  An error is returned from the fetch method if the RIS acquisition does not successfully acquire the specified number of waveforms within the timeout period.  You may call the fetch method again to allow more time for the acquisition to finish.
    '''
    MIN_NUM_AVERAGES = 2
    r'''
    Each RIS sample is the average of a least a minimum number of randomly
    distributed points.
    '''
    INCOMPLETE = 3
    r'''
    Returns the RIS waveform after the specified timeout even if it is incomplete.  If no waveforms have been acquired in certain bins, these bins will have a NaN (when fetching scaled data) or a zero (when fetching binary data). A warning (positive error code) is returned from the fetch method if the RIS acquisition did not finish.  The acquisition aborts when data is returned.
    '''
    LIMITED_BIN_WIDTH = 5
    r'''
    Limits the waveforms in the various bins to be within 200 ps of the center of the bin.
    '''


class RefLevelUnits(Enum):
    VOLTS = 0
    r'''
    Specifies that the reference levels are given in units of volts.
    '''
    PERCENTAGE = 1
    r'''
    (Default) Specifies that the reference levels are given in percentage
    units.
    '''


class RefTriggerDetectorLocation(Enum):
    ANALOG_DETECTION_CIRCUIT = 0
    r'''
    use the hardware analog circuitry to implement the reference trigger.  This option will trigger before any onboard signal processing.
    '''
    DDC_OUTPUT = 1
    r'''
    use the onboard signal processing logic to implement the reference trigger.  This option will trigger based on the onboard signal processed data.
    '''


class RuntPolarity(Enum):
    POSITIVE = 1
    r'''
    Trigger on pulses of positive polarity relative to runt_low_threshold that do not cross runt_high_threshold.
    '''
    NEGATIVE = 2
    r'''
    Trigger on pulses of negative polarity relative to runt_high_threshold that do not cross runt_low_threshold.
    '''
    EITHER = 3
    r'''
    Trigger on pulses of either positive or negative polarity.
    '''


class RuntTimeCondition(Enum):
    NONE = 0
    r'''
    Time qualification is disabled. Trigger on runt pulses based solely on the voltage level of the pulses.
    '''
    WITHIN = 1
    r'''
    Trigger on pulses that, in addition to meeting runt voltage criteria, have a duration within the range bounded by runt_time_low_limit and runt_time_high_limit.
    '''
    OUTSIDE = 2
    r'''
    Trigger on pulses that, in addition to meeting runt voltage criteria, have a duration not within the range bounded by runt_time_low_limit and runt_time_high_limit.
    '''


class ScalarMeasurement(Enum):
    NO_MEASUREMENT = 4000
    r'''
    None
    '''
    RISE_TIME = 0
    FALL_TIME = 1
    FREQUENCY = 2
    PERIOD = 3
    VOLTAGE_RMS = 4
    VOLTAGE_PEAK_TO_PEAK = 5
    VOLTAGE_MAX = 6
    VOLTAGE_MIN = 7
    VOLTAGE_HIGH = 8
    VOLTAGE_LOW = 9
    VOLTAGE_AVERAGE = 10
    WIDTH_NEG = 11
    WIDTH_POS = 12
    DUTY_CYCLE_NEG = 13
    DUTY_CYCLE_POS = 14
    AMPLITUDE = 15
    VOLTAGE_CYCLE_RMS = 16
    VOLTAGE_CYCLE_AVERAGE = 17
    OVERSHOOT = 18
    PRESHOOT = 19
    LOW_REF_VOLTS = 1000
    MID_REF_VOLTS = 1001
    HIGH_REF_VOLTS = 1002
    AREA = 1003
    CYCLE_AREA = 1004
    INTEGRAL = 1005
    VOLTAGE_BASE = 1006
    VOLTAGE_TOP = 1007
    FFT_FREQUENCY = 1008
    FFT_AMPLITUDE = 1009
    RISE_SLEW_RATE = 1010
    FALL_SLEW_RATE = 1011
    AC_ESTIMATE = 1012
    DC_ESTIMATE = 1013
    TIME_DELAY = 1014
    AVERAGE_PERIOD = 1015
    AVERAGE_FREQUENCY = 1016
    VOLTAGE_BASE_TO_TOP = 1017
    PHASE_DELAY = 1018


class TerminalConfiguration(Enum):
    SINGLE_ENDED = 0
    r'''
    Channel is single ended
    '''
    UNBALANCED_DIFFERENTIAL = 1
    r'''
    Channel is unbalanced differential
    '''
    DIFFERENTIAL = 2
    r'''
    Channel is differential
    '''


class TriggerCoupling(Enum):
    AC = 0
    r'''
    AC coupling
    '''
    DC = 1
    r'''
    DC coupling
    '''
    HF_REJECT = 3
    r'''
    Highpass filter coupling
    '''
    LF_REJECT = 4
    r'''
    Lowpass filter coupling
    '''
    AC_PLUS_HF_REJECT = 1001
    r'''
    Highpass and lowpass filter coupling
    '''


class TriggerModifier(Enum):
    NO_TRIGGER_MOD = 1
    r'''
    Normal triggering.
    '''
    AUTO = 2
    r'''
    Software will trigger an acquisition automatically if no trigger arrives
    after a certain amount of time.
    '''
    AUTO_LEVEL = 3


class TriggerSlope(Enum):
    NEGATIVE = 0
    r'''
    Falling edge
    '''
    POSITIVE = 1
    r'''
    Rising edge
    '''
    SLOPE_EITHER = 3
    r'''
    Either edge
    '''


class TriggerType(Enum):
    EDGE = 1
    r'''
    Configures the digitizer for edge triggering.  An edge trigger occurs when the trigger signal crosses the trigger level specified with the set trigger slope.  You configure the trigger level and slope with configure_trigger_edge.
    '''
    HYSTERESIS = 1001
    r'''
    Configures the digitizer for hysteresis triggering.  A hysteresis trigger occurs when the trigger signal crosses the trigger level with the specified slope and passes through the hysteresis window you specify. You configure the trigger level, slope, and hysteresis with configure_trigger_hysteresis.
    '''
    DIGITAL = 1002
    r'''
    Configures the digitizer for digital triggering. A digital trigger occurs when the trigger signal has the specified slope. You configure the trigger slope with configure_trigger_digital.
    '''
    WINDOW = 1003
    r'''
    Configures the digitizer for window triggering.  A window trigger occurs when the trigger signal enters or leaves the window defined by the values you specify with the Low Window Level, High Window Level, and Window Mode Parameters.  You configure the low window level high window level, and window mode with configure_trigger_window.
    '''
    SOFTWARE = 1004
    r'''
    Configures the digitizer for software triggering.  A software trigger occurs when SendSoftwareTrigger is called.
    '''
    TV = 5
    r'''
    Configures the digitizer for video/TV triggering.   You configure the video trigger parameters like signal Format, Line to trigger off of, Polarity, and Enable DC Restore with configure_trigger_video.
    '''
    GLITCH = 4
    WIDTH = 2
    RUNT = 3
    IMMEDIATE = 6
    r'''
    Configures the digitizer for immediate triggering.   An immediate trigger occurs as soon as the pretrigger samples are acquired.
    '''


class TriggerWindowMode(Enum):
    ENTERING = 0
    r'''
    Trigger upon entering the window
    '''
    LEAVING = 1
    r'''
    Trigger upon leaving the window
    '''
    ENTERING_OR_LEAVING = 2


class VerticalCoupling(Enum):
    AC = 0
    r'''
    AC coupling
    '''
    DC = 1
    r'''
    DC coupling
    '''
    GND = 2
    r'''
    GND coupling
    '''


class VideoPolarity(Enum):
    POSITIVE = 1
    r'''
    Specifies that the video signal has positive polarity.
    '''
    NEGATIVE = 2
    r'''
    Specifies that the video signal has negative polarity.
    '''


class VideoSignalFormat(Enum):
    NTSC = 1
    r'''
    NTSC signal format supports line numbers from 1 to 525
    '''
    PAL = 2
    r'''
    PAL signal format supports line numbers from 1 to 625
    '''
    SECAM = 3
    r'''
    SECAM signal format supports line numbers from 1 to 625
    '''
    M_PAL = 1001
    r'''
    M-PAL signal format supports line numbers from 1 to 525
    '''
    VIDEO_480I_59_94_FIELDS_PER_SECOND = 1010
    r'''
    480 lines, interlaced, 59.94 fields per second
    '''
    VIDEO_480I_60_FIELDS_PER_SECOND = 1011
    r'''
    480 lines, interlaced, 60 fields per second
    '''
    VIDEO_480P_59_94_FRAMES_PER_SECOND = 1015
    r'''
    480 lines, progressive, 59.94 frames per second
    '''
    VIDEO_480P_60_FRAMES_PER_SECOND = 1016
    r'''
    480 lines, progressive,60 frames per second
    '''
    VIDEO_576I_50_FIELDS_PER_SECOND = 1020
    r'''
    576 lines, interlaced, 50 fields per second
    '''
    VIDEO_576P_50_FRAMES_PER_SECOND = 1025
    r'''
    576 lines, progressive, 50 frames per second
    '''
    VIDEO_720P_50_FRAMES_PER_SECOND = 1031
    r'''
    720 lines, progressive, 50 frames per second
    '''
    VIDEO_720P_59_94_FRAMES_PER_SECOND = 1032
    r'''
    720 lines, progressive, 59.94 frames per second
    '''
    VIDEO_720P_60_FRAMES_PER_SECOND = 1033
    r'''
    720 lines, progressive, 60 frames per second
    '''
    VIDEO_1080I_50_FIELDS_PER_SECOND = 1040
    r'''
    1,080 lines, interlaced, 50 fields per second
    '''
    VIDEO_1080I_59_94_FIELDS_PER_SECOND = 1041
    r'''
    1,080 lines, interlaced, 59.94 fields per second
    '''
    VIDEO_1080I_60_FIELDS_PER_SECOND = 1042
    r'''
    1,080 lines, interlaced, 60 fields per second
    '''
    VIDEO_1080P_24_FRAMES_PER_SECOND = 1045
    r'''
    1,080 lines, progressive, 24 frames per second
    '''


class VideoTriggerEvent(Enum):
    FIELD1 = 1
    r'''
    Trigger on field 1 of the signal
    '''
    FIELD2 = 2
    r'''
    Trigger on field 2 of the signal
    '''
    ANY_FIELD = 3
    r'''
    Trigger on the first field acquired
    '''
    ANY_LINE = 4
    r'''
    Trigger on the first line acquired
    '''
    LINE_NUMBER = 5
    r'''
    Trigger on a specific line of a video signal.  Valid values vary depending on the signal format configured.
    '''


class WhichTrigger(Enum):
    START = 0
    ARM_REFERENCE = 1
    REFERENCE = 2
    ADVANCE = 3


class WidthCondition(Enum):
    WITHIN = 1
    r'''
    Trigger on pulses with a duration within the range bounded by width_low_threshold and width_high_threshold.
    '''
    OUTSIDE = 2
    r'''
    Trigger on pulses with a duration not within the range bounded by width_low_threshold and width_high_threshold.
    '''


class WidthPolarity(Enum):
    POSITIVE = 1
    r'''
    Trigger on pulses of positive polarity relative to the trigger threshold.
    '''
    NEGATIVE = 2
    r'''
    Trigger on pulses of negative polarity relative to the trigger threshold.
    '''
    EITHER = 3
    r'''
    Trigger on pulses of either positive or negative polarity.
    '''
