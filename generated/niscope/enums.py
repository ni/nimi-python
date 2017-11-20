# This file was generated

from enum import Enum


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


class ArrayMeasurement(Enum):
    Last_Acq._Histogram = 4001
    '''
    Last Acquisition Histogram
    '''
    Multi_Acq._Voltage_Histogram = 4004
    '''
    Multi Acquisition Voltage Histogram
    '''
    Multi_Acq._Time_Histogram = 4005
    '''
    Multi Acquisition Time Histogram
    '''
    Multi_Acq._Average = 4016
    '''
    Multi Acquisition Average
    '''
    Polynomial_Interpolation = 4011
    '''
    Polynomial Interpolation
    '''
    Array_Integral = 4006
    '''
    Array Integral
    '''
    Derivative = 4007
    '''
    Derivative
    '''
    Inverse = 4008
    '''
    Inverse
    '''
    Multiply_Channels = 4012
    '''
    Multiply Channels
    '''
    Add_Channels = 4013
    '''
    Add Channels
    '''
    Subtract_Channels = 4014
    '''
    Subtract Channels
    '''
    Divide_Channels = 4015
    '''
    Divide Channels
    '''
    Array_Offset = 4025
    '''
    Array Offset
    '''
    Array_Gain = 4026
    '''
    Array Gain
    '''
    Hanning_Window = 4009
    '''
    Hanning Window
    '''
    Flat_Top_Window = 4010
    '''
    Flat Top Window
    '''
    Hamming_Window = 4020
    '''
    Hamming Window
    '''
    Triangle_Window = 4023
    '''
    Triangle Window
    '''
    Blackman_Window = 4024
    '''
    Blackman Window
    '''
    FIR_Windowed_Filter = 4021
    '''
    FIR Windowed Filter
    '''
    Bessel_IIR_Filter = 4022
    '''
    Bessel IIR Filter
    '''
    Butterworth_IIR_Filter = 4017
    '''
    Butterworth IIR Filter
    '''
    Chebyshev_IIR_Filter = 4018
    '''
    Chebyshev IIR Filter
    '''
    FFT_Phase_Spectrum = 4002
    '''
    FFT Phase Spectrum
    '''
    FFT_Amp._Spectrum_(Volts_RMS) = 4003
    '''
    FFT Amp. Spectrum (Volts RMS)
    '''
    FFT_Amp._Spectrum_(dB) = 4019
    '''
    FFT Amp. Spectrum (dB)
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


class ClearableMeasurement(Enum):
    All_Measurements = 10000
    Multi_Acq._Voltage_Histogram = 4004
    Multi_Acq._Time_Histogram = 4005
    Multi_Acq._Average = 4016
    Frequency = 2
    Period = 3
    Average_Period = 1015
    Rise_Time = 0
    Fall_Time = 1
    Rising_Slew_Rate = 1010
    Falling_Slew_Rate = 1011
    Overshoot = 18
    Preshoot = 19
    Voltage_RMS = 4
    Voltage_Cycle_RMS = 16
    AC_Estimate = 1012
    FFT_Amplitude = 1009
    Voltage_Average = 10
    Voltage_Cycle_Average = 17
    DC_Estimate = 1013
    Voltage_Max = 6
    Voltage_Min = 7
    Voltage_Peak-to-Peak = 5
    Voltage_High = 8
    Voltage_Low = 9
    Voltage_Amplitude = 15
    Voltage_Top = 1007
    Voltage_Base = 1006
    Voltage_Base-to-Top = 1017
    Negative_Width = 11
    Positive_Width = 12
    Negative_Duty_Cycle = 13
    Positive_Duty_Cycle = 14
    Integral = 1005
    Area = 1003
    Cycle_Area = 1004
    Time_Delay = 1014
    Phase_Delay = 1018
    Low_Ref_Volts = 1000
    Mid_Ref_Volts = 1001
    High_Ref_Volts = 1002
    Volt._Hist._Mean = 2000
    Volt._Hist._Stdev = 2001
    Volt._Hist._Median = 2003
    Volt._Hist._Mode = 2010
    Volt._Hist._Max = 2005
    Volt._Hist._Min = 2006
    Volt._Hist._Peak-to-Peak = 2002
    Volt._Hist._Mean_+_Stdev = 2007
    Volt._Hist._Mean_+_2_Stdev = 2008
    Volt._Hist._Mean_+_3_Stdev = 2009
    Volt._Hist._Hits = 2004
    Volt._Hist._New_Hits = 2011
    Time_Hist._Mean = 3000
    Time_Hist._Stdev = 3001
    Time_Hist._Median = 3003
    Time_Hist._Mode = 3010
    Time_Hist._Max = 3005
    Time_Hist._Min = 3006
    Time_Hist._Peak-to-Peak = 3002
    Time_Hist._Mean_+_Stdev = 3007
    Time_Hist._Mean_+_2_Stdev = 3008
    Time_Hist._Mean_+_3_Stdev = 3009
    Time_Hist._Hits = 3004
    Time_Hist._New_Hits = 3011


class DataProcessingMode(Enum):
    REAL = 0
    '''
    The waveform data points are real numbers (I data).
    '''
    COMPLEX = 1
    '''
    The waveform data points are complex numbers (IQ data).
    '''


class ExportDestinations(Enum):
    PXI_Trigger_Line_0/RTSI_0 = 'VAL_RTSI_0'
    PXI_Trigger_Line_1/RTSI_1 = 'VAL_RTSI_1'
    PXI_Trigger_Line_2/RTSI_2 = 'VAL_RTSI_2'
    PXI_Trigger_Line_3/RTSI_3 = 'VAL_RTSI_3'
    PXI_Trigger_Line_4/RTSI_4 = 'VAL_RTSI_4'
    PXI_Trigger_Line_5/RTSI_5 = 'VAL_RTSI_5'
    PXI_Trigger_Line_6/RTSI_6 = 'VAL_RTSI_6'
    PXI_Trigger_Line_7/RTSI_7_(RTSI_Clock) = 'VAL_RTSI_7'
    PXI_Star_Trigger = 'VAL_PXI_STAR'
    PFI_0 = 'VAL_PFI_0'
    PFI_1 = 'VAL_PFI_1'
    PFI_2 = 'VAL_PFI_2'
    Clock_Out = 'VAL_CLK_OUT'
    AUX_0/PFI_0 = 'VAL_AUX_0_PFI_0'
    AUX_0/PFI_1 = 'VAL_AUX_0_PFI_1'
    AUX_0/PFI_2 = 'VAL_AUX_0_PFI_2'
    AUX_0/PFI_3 = 'VAL_AUX_0_PFI_3'
    AUX_0/PFI_4 = 'VAL_AUX_0_PFI_4'
    AUX_0/PFI_5 = 'VAL_AUX_0_PFI_5'
    AUX_0/PFI_6 = 'VAL_AUX_0_PFI_6'
    AUX_0/PFI_7 = 'VAL_AUX_0_PFI_7'


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


class InputImpedance(Enum):
    _1_mega_ohm = 0
    _50_ohms = 2


class Option(Enum):
    Self_Calibrate_All_Channels = 0
    '''
    Self Calibrating all Channels
    '''
    Restore_External_Calibration = 1
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
