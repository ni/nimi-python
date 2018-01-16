# This file was generated

from enum import Enum


class AnalogPath(Enum):
    MAIN = 0
    '''
    Specifies use of the main path.  NI-FGEN chooses the amplifier based on the user-specified gain.
    '''
    DIRECT = 1
    '''
    Specifies use of the direct path.
    '''
    FIXED_LOW_GAIN = 2
    '''
    Specifies use of the low-gain amplifier in the main path, no matter  what value the user specifies for gain. This setting limits the output  range.
    '''
    FIXED_HIGH_GAIN = 3
    '''
    Specifies use of the high-gain amplifier in the main path.
    '''


class BusType(Enum):
    INVALID = 0
    '''
    Indicates an invalid bus type.
    '''
    AT = 1
    '''
    Indicates the signal generator is the AT bus type.
    '''
    PCI = 2
    '''
    Indicates the signal generator is the PCI bus type.
    '''
    PXI = 3
    '''
    Indicates the signal generator is the PXI bus type.
    '''
    VXI = 4
    '''
    Indicates the signal generator is the VXI bus type.
    '''
    PCMCIA = 5
    '''
    Indicates the signal generator is the PCI-CMA bus type.
    '''
    PXIE = 6
    '''
    Indicates the signal generator is the PXI Express bus type.
    '''


class ByteOrder(Enum):
    LITTLE = 0
    BIG = 1


class CalADCInput(Enum):
    ANALOG_OUTPUT = 0
    '''
    Specifies that the ADC measures the analog output.
    '''
    INTERNAL_VOLTAGE_REFERENCE = 1
    '''
    Specifies that the ADC measures the internal voltage reference.
    '''
    GROUND = 2
    '''
    Specifies that the ADC measures the ground voltage.
    '''
    ANALOG_OUTPUT_DIFFERENTIAL = 3
    '''
    Specifies that the ADC measures the differential analog output.
    '''
    ANALOG_OUTPUT_PLUS = 4
    '''
    Specifies that the ADC measures the positive differential analog output.
    '''
    ANALOG_OUTPUT_MINUS = 5
    '''
    Specifies that the ADC measures the negative differential analog output.
    '''
    ANALOG_OUTPUT_IDLE = 6
    '''
    Specifies that the ADC measures the idle analog output.
    '''


class ClockMode(Enum):
    HIGH_RESOLUTION = 0
    '''
    High resolution sampling—Sample rate is generated by a high–resolution clock source.
    '''
    DIVIDE_DOWN = 1
    '''
    Divide down sampling—Sample rates are generated by dividing the source frequency.
    '''
    AUTOMATIC = 2
    '''
    Automatic Selection—NI-FGEN selects between the divide–down and high–resolution clocking modes.
    '''


class DataMarkerEventLevelPolarity(Enum):
    HIGH = 101
    '''
    When the operation is ready to start, the Ready for Start  event level is high.
    '''
    LOW = 102
    '''
    When the operation is ready to start, the Ready for Start  event level is low.
    '''


class DataProcessingMode(Enum):
    REAL = 0
    '''
    The waveform data points are real numbers (I data).
    '''
    COMPLEX = 1
    '''
    The waveform data points are complex numbers (I/Q data).
    '''


class DoneEventActiveLevel(Enum):
    HIGH = 101
    '''
    When the operation is ready to start, the Ready for Start  event level is high.
    '''
    LOW = 102
    '''
    When the operation is ready to start, the Ready for Start  event level is low.
    '''


class DoneEventDelayUnits(Enum):
    SAMPLE_CLOCK_PERIODS = 101
    '''
    Specifies the pulse width in Sample clock periods.
    '''
    SECONDS = 102
    '''
    Specifies the pulse width in seconds.
    '''


class DoneEventOutputBehavior(Enum):
    PULSE = 101
    '''
    Triggers a pulse for a specified period of time.
    '''
    LEVEL = 102
    '''
    Shifts high or low while the event is active, depending  on the active state you specify.
    '''


class DoneEventPulsePolarity(Enum):
    HIGH = 101
    '''
    When the operation is ready to start, the Ready for Start  event level is high.
    '''
    LOW = 102
    '''
    When the operation is ready to start, the Ready for Start  event level is low.
    '''


class DoneEventPulseWidthUnits(Enum):
    SAMPLE_CLOCK_PERIODS = 101
    '''
    Specifies the pulse width in Sample clock periods.
    '''
    SECONDS = 102
    '''
    Specifies the pulse width in seconds.
    '''


class FilterType(Enum):
    FLAT = 0
    '''
    Applies a flat filter to the data with the passband value specified  in the NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND attribute.
    '''
    RAISED_COSINE = 1
    '''
    Applies a raised cosine filter to the data with the alpha value  specified in the NIFGEN_ATTR_OSP_FIR_FILTER_RAISED_COSINE_ALPHA attribute.
    '''
    ROOT_RAISED_COSINE = 2
    '''
    Applies a root raised cosine filter to the data with the alpha value  specified in the NIFGEN_ATTR_OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA attribute.
    '''
    GAUSSIAN = 3
    '''
    Applies a Gaussian filter to the data with the BT value specified in the  NIFGEN_ATTR_OSP_FIR_FILTER_GAUSSIAN_BT attribute.
    '''
    CUSTOM = 4
    '''
    Applies a custom filter to the data. If NIFGEN_VAL_OSP_CUSTOM is selected,  you must provide a set of FIR filter coefficients with the  niFgen_ConfigureCustomFIRFilterCoefficients function.
    '''


class HardwareState(Enum):
    IDLE = 0
    WAITING_FOR_START_TRIGGER = 1
    RUNNING = 2
    DONE = 3
    HARDWARE_ERROR = 4


class IdleBehavior(Enum):
    HOLD_LAST = 400
    '''
    While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.
    '''
    JUMP_TO = 401
    '''
    While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value attribute.
    '''


class MarkerEventDelayUnits(Enum):
    SAMPLE_CLOCK_PERIODS = 101
    '''
    Specifies the pulse width in Sample clock periods.
    '''
    SECONDS = 102
    '''
    Specifies the pulse width in seconds.
    '''


class MarkerEventOutputBehavior(Enum):
    PULSE = 101
    '''
    Triggers a pulse for a specified period of time.
    '''
    LEVEL = 102
    '''
    Shifts high or low while the event is active, depending  on the active state you specify.
    '''
    TOGGLE = 103
    '''
    Changes to high or low while the event is active, depending on the
    active state you specify.
    '''


class MarkerEventPulsePolarity(Enum):
    HIGH = 101
    '''
    When the operation is ready to start, the Ready for Start  event level is high.
    '''
    LOW = 102
    '''
    When the operation is ready to start, the Ready for Start  event level is low.
    '''


class MarkerEventPulseWidthUnits(Enum):
    SAMPLE_CLOCK_PERIODS = 101
    '''
    Specifies the pulse width in Sample clock periods.
    '''
    SECONDS = 102
    '''
    Specifies the pulse width in seconds.
    '''


class MarkerEventToggleInitialState(Enum):
    HIGH = 101
    '''
    Sets the initial state of the Marker event to high.
    '''
    LOW = 102
    '''
    Sets the initial state of the Marker event to low.
    '''


class OSPMode(Enum):
    IF = 0
    '''
    The OSP block generates intermediate frequency (IF) data.
    '''
    BASEBAND = 1
    '''
    The OSP block generates baseband data.
    '''


class OSPOverflowErrorReporting(Enum):
    ERROR = 0
    '''
    NI-FGEN returns errors whenever an overflow has occurred in the OSP block.
    '''
    DISABLED = 2
    '''
    NI-FGEN does not return errors when an overflow occurs in the OSP block.
    '''


class OutputMode(Enum):
    FUNC = 0
    '''
    Standard Function mode—  Generates standard function waveforms  such as sine, square, triangle, and so on.
    '''
    ARB = 1
    '''
    Arbitrary waveform mode—Generates  waveforms from user-created/provided  waveform arrays of numeric data.
    '''
    SEQ = 2
    '''
    Arbitrary sequence mode —  Generates downloaded waveforms  in an order your specify.
    '''
    FREQ_LIST = 101
    '''
    Frequency List mode—Generates a  standard function using a list of  frequencies you define.
    '''
    SCRIPT = 102
    '''
    **Script mode—**\ Allows you to use scripting to link and loop multiple
    waveforms in complex combinations.
    '''


class P2PAddressType(Enum):
    PHYSICAL = 0
    '''
    Physical
    '''
    VIRTUAL = 1
    '''
    Physical
    '''


class ReadyForStartEventActiveLevel(Enum):
    HIGH = 101
    '''
    When the operation is ready to start, the Ready for Start  event level is high.
    '''
    LOW = 102
    '''
    When the operation is ready to start, the Ready for Start  event level is low.
    '''


class ReferenceClockSource(Enum):
    CLOCK_IN = 'ClkIn'
    '''
    Specifies that the CLK IN input signal from the front panel connector is
    used as the Reference Clock source.
    '''
    NONE = 'None'
    '''
    Specifies that a Reference Clock is not used.
    '''
    ONBOARD_REFERENCE_CLOCK = 'OnboardRefClk'
    '''
    Specifies that the onboard Reference Clock is used as the Reference
    Clock source.
    '''
    PXI_CLOCK = 'PXI_Clk'
    '''
    Specifies the PXI Clock is used as the Reference Clock source.
    '''
    RTSI_7 = 'RTSI7'
    '''
    Specifies that the RTSI line 7 is used as the Reference Clock source.
    '''


class RelativeTo(Enum):
    START = 0
    CURRENT = 1


class SampleClockSource(Enum):
    CLOCK_IN = '"ClkIn"'
    '''
    Specifies that the signal at the CLK IN front panel connector is used as
    the Sample Clock source.
    '''
    DDC_CLOCK_IN = '"DDC_ClkIn"'
    '''
    Specifies that the Sample Clock from DDC connector is used as the Sample
    Clock source.
    '''
    ONBOARD_CLOCK = '"OnboardClock"'
    '''
    Specifies that the onboard clock is used as the Sample Clock source.
    '''
    PXI_STAR_LINE = '"PXI_Star"'
    '''
    Specifies that the PXI_STAR trigger line is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_0RTSI_0 = '"PXI_Trig0"'
    '''
    Specifies that the PXI or RTSI line 0 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_1RTSI_1 = '"PXI_Trig1"'
    '''
    Specifies that the PXI or RTSI line 1 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_2RTSI_2 = '"PXI_Trig2"'
    '''
    Specifies that the PXI or RTSI line 2 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_3RTSI_3 = '"PXI_Trig3"'
    '''
    Specifies that the PXI or RTSI line 3 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_4RTSI_4 = '"PXI_Trig4"'
    '''
    Specifies that the PXI or RTSI line 4 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_5RTSI_5 = '"PXI_Trig5"'
    '''
    Specifies that the PXI or RTSI line 5 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_6RTSI_6 = '"PXI_Trig6"'
    '''
    Specifies that the PXI or RTSI line 6 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_7RTSI_7 = '"PXI_Trig7"'
    '''
    Specifies that the PXI or RTSI line 7 is used as the Sample Clock
    source.
    '''


class SampleClockTimebaseSource(Enum):
    CLOCK_IN = '"ClkIn"'
    '''
    Specifies that the external signal on the CLK IN front panel connector
    is used as the source.
    '''
    ONBOARD_CLOCK = '"OnboardClock"'
    '''
    Specifies that the onboard Sample Clock timebase is used as the source.
    '''


class ScriptTriggerDigitalEdgeEdge(Enum):
    RISING = 101
    '''
    Rising Edge
    '''
    FALLING = 102
    '''
    Falling Edge
    '''


class ScriptTriggerDigitalLevelActiveLevel(Enum):
    HIGH = 101
    '''
    High Level
    '''
    LOW = 102
    '''
    Low Level
    '''


class ScriptTriggerType(Enum):
    TRIG_NONE = 101
    '''
    No trigger is configured. Signal generation starts immediately.
    '''
    DIGITAL_EDGE = 102
    '''
    Trigger is asserted when a digital edge is detected.
    '''
    DIGITAL_LEVEL = 103
    '''
    Trigger is asserted when a digital level is detected.
    '''
    SOFTWARE_EDGE = 104
    '''
    Trigger is asserted when a software edge is detected.
    '''


class Signal(Enum):
    ONBOARD_REFERENCE_CLOCK = 1019
    SYNC_OUT = 1002
    START_TRIGGER = 1004
    MARKER_EVENT = 1001
    SAMPLE_CLOCK_TIMEBASE = 1006
    SYNCHRONIZATION = 1007
    SAMPLE_CLOCK = 101
    REFERENCE_CLOCK = 102
    SCRIPT_TRIGGER = 103
    READY_FOR_START_EVENT = 105
    STARTED_EVENT = 106
    DONE_EVENT = 107
    DATA_MARKER_EVENT = 108


class StartTriggerDigitalEdgeEdge(Enum):
    RISING = 101
    '''
    Rising Edge
    '''
    FALLING = 102
    '''
    Falling Edge
    '''


class StartTriggerType(Enum):
    TRIG_NONE = 101
    '''
    None
    '''
    DIGITAL_EDGE = 102
    '''
    Digital Edge
    '''
    SOFTWARE_EDGE = 104
    '''
    Software Edge
    '''
    P2P_ENDPOINT_FULLNESS = 106
    '''
    P2P Endpoint Fullness
    '''


class StartedEventActiveLevel(Enum):
    HIGH = 101
    '''
    When the operation is ready to start, the Ready for Start  event level is high.
    '''
    LOW = 102
    '''
    When the operation is ready to start, the Ready for Start  event level is low.
    '''


class StartedEventDelayUnits(Enum):
    SAMPLE_CLOCK_PERIODS = 101
    '''
    Specifies the pulse width in Sample clock periods.
    '''
    SECONDS = 102
    '''
    Specifies the pulse width in seconds.
    '''


class StartedEventOutputBehavior(Enum):
    PULSE = 101
    '''
    Triggers a pulse for a specified period of time.
    '''
    LEVEL = 102
    '''
    Shifts high or low while the event is active, depending  on the active state you specify.
    '''


class StartedEventPulsePolarity(Enum):
    HIGH = 101
    '''
    When the operation is ready to start, the Ready for Start  event level is high.
    '''
    LOW = 102
    '''
    When the operation is ready to start, the Ready for Start  event level is low.
    '''


class StartedEventPulseWidthUnits(Enum):
    SAMPLE_CLOCK_PERIODS = 101
    '''
    Specifies the pulse width in Sample clock periods.
    '''
    SECONDS = 102
    '''
    Specifies the pulse width in seconds.
    '''


class SynchronizationSource(Enum):
    TTL0 = 111
    '''
    PXI TRIG0 or VXI TTL0
    '''
    TTL1 = 112
    '''
    PXI TRIG1 or VXI TTL1
    '''
    TTL2 = 113
    '''
    PXI TRIG2 or VXI TTL2
    '''
    TTL3 = 114
    '''
    PXI TRIG3 or VXI TTL3
    '''
    TTL4 = 115
    '''
    PXI TRIG4 or VXI TTL4
    '''
    TTL5 = 116
    '''
    PXI TRIG5 or VXI TTL5
    '''
    TTL6 = 117
    '''
    PXI TRIG6 or VXI TTL6
    '''
    RTSI_0 = 141
    '''
    RTSI 0
    '''
    RTSI_1 = 142
    '''
    RTSI 1
    '''
    RTSI_2 = 143
    '''
    RTSI 2
    '''
    RTSI_3 = 144
    '''
    RTSI 3
    '''
    RTSI_4 = 145
    '''
    RTSI 4
    '''
    RTSI_5 = 146
    '''
    RTSI 5
    '''
    RTSI_6 = 147
    '''
    RTSI 6
    '''
    NONE = 1000
    '''
    No Synchronization Source
    '''


class TerminalConfiguration(Enum):
    SINGLE_ENDED = 300
    '''
    Single-ended operation
    '''
    DIFFERENTIAL = 301
    '''
    Differential operation
    '''


class Trigger(Enum):
    START = 1004
    SCRIPT = 103


class TriggerMode(Enum):
    SINGLE = 1
    '''
    Single Trigger Mode - The waveform you describe in the sequence list is  generated only once by going through the entire staging list. Only one  trigger is required to start the waveform generation. You can use Single  trigger mode with the output mode in any mode. After a trigger is  received, the waveform generation starts from the first stage and  continues through to the last stage. Then, the last stage generates  repeatedly until you stop the waveform generation.
    '''
    CONTINUOUS = 2
    '''
    Continuous Trigger Mode - The waveform you describe in the staging list generates infinitely by repeatedly cycling through the staging list.  After a trigger is received, the waveform generation starts from the  first stage and continues through to the last stage. After the last stage  completes, the waveform generation loops back to the start of the  first stage and continues until it is stopped. Only one trigger is  required to start the waveform generation.
    '''
    STEPPED = 3
    '''
    Stepped Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates. Then, the device waits for the  next trigger signal. On the next trigger, the waveform described by the  second stage generates, and so on. After the staging list completes,  the waveform generation returns to the first stage and continues in a  cyclic fashion. After any stage has generated completely, the first  eight samples of the next stage are repeated continuously until the next  trigger is received.
    trigger mode.

    Note: In Frequency List mode, Stepped trigger mode is the same as Burst
    '''
    BURST = 4
    '''
    Burst Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates until another trigger is  received. At the next trigger, the buffer of the previous stage completes, and then the waveform described by the second stage generates. After the staging list completes, the waveform generation  returns to the first stage and continues in a cyclic fashion. In  Frequency List mode, the duration instruction is ignored, and the trigger  switches the frequency to the next frequency in the list.
    trigger mode.

    Note: In Frequency List mode, Stepped trigger mode is the same as Burst
    '''


class TriggerSource(Enum):
    IMMEDIATE = 0
    '''
    Immediate-The signal generator does not wait for a trigger of any kind.
    '''
    EXTERNAL = 1
    '''
    External-The signal generator waits for a trigger on the external trigger input
    '''
    SOFTWARE_TRIG = 2
    '''
    Software Trigger-The signal generator waits until you call niFgen_SendSWTrigger.
    '''
    TTL0 = 111
    '''
    PXI TRIG0 or VXI TTL0
    '''
    TTL1 = 112
    '''
    PXI TRIG1 or VXI TTL1
    '''
    TTL2 = 113
    '''
    PXI TRIG2 or VXI TTL2
    '''
    TTL3 = 114
    '''
    PXI TRIG3 or VXI TTL3
    '''
    TTL4 = 115
    '''
    PXI TRIG4 or VXI TTL4
    '''
    TTL5 = 116
    '''
    PXI TRIG5 or VXI TTL5
    '''
    TTL6 = 117
    '''
    PXI TRIG6 or VXI TTL6
    '''
    PXI_STAR = 131
    '''
    PXI star
    '''
    RTSI_0 = 141
    '''
    RTSI line 0
    '''
    RTSI_1 = 142
    '''
    RTSI line 1
    '''
    RTSI_2 = 143
    '''
    RTSI line 2
    '''
    RTSI_3 = 144
    '''
    RTSI line 3
    '''
    RTSI_4 = 145
    '''
    RTSI line 4
    '''
    RTSI_5 = 146
    '''
    RTSI line 5
    '''
    RTSI_6 = 147
    '''
    RTSI line 6
    '''
    RTSI_7 = 1010
    '''
    RTSI line 7
    '''
    PFI_0 = 1011
    '''
    PFI 0
    '''
    PFI_1 = 1012
    '''
    PFI 1
    '''
    PFI_2 = 1013
    '''
    PFI 2
    '''
    PFI_3 = 1014
    '''
    PFI 3
    '''
    OTHER_TERMINAL = 1018
    '''
    Specifies that another terminal is used.
    '''


class TriggerWhen(Enum):
    HIGH = 101
    LOW = 102


class VideoWaveformType(Enum):
    PAL_B = 0
    '''
    PAL B Video Type
    '''
    PAL_D = 1
    '''
    PAL D Video Type
    '''
    PAL_G = 2
    '''
    PAL G Video Type
    '''
    PAL_H = 3
    '''
    PAL H Video Type
    '''
    PAL_I = 4
    '''
    PAL I Video Type
    '''
    PAL_M = 5
    '''
    PAL M Video Type
    '''
    PAL_N = 6
    '''
    PAL N Video Type
    '''
    NTSC_M = 7
    '''
    NTSC M Video Type
    '''


class WaitBehavior(Enum):
    HOLD_LAST = 400
    '''
    While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.
    '''
    JUMP_TO = 401
    '''
    While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value attribute.
    '''


class Waveform(Enum):
    SINE = 1
    '''
    Sinusoid waveform
    '''
    SQUARE = 2
    '''
    Square waveform
    '''
    TRIANGLE = 3
    '''
    Triange waveform
    '''
    RAMP_UP = 4
    '''
    Positive ramp waveform
    '''
    RAMP_DOWN = 5
    '''
    Negative ramp waveform
    '''
    DC = 6
    '''
    Constant voltage
    '''
    NOISE = 101
    '''
    White noise
    '''
    USER = 102
    '''
    User-defined waveform as defined by the niFgen_DefineUserStandardWaveform function.
    '''
