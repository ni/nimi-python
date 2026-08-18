# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum
from enum import IntFlag


class AcquisitionType(Enum):
    IQ = 100
    r'''
    Configures NI-RFSA for I/Q acquisitions.
    '''
    SPECTRUM = 101
    r'''
    Configures NI-RFSA for spectrum acquisitions.
    '''


class Action(Enum):
    COMMIT = 1501
    r'''
    The new calibration constants are stored in the EEPROM.
    '''
    ABORT = 1500
    r'''
    The old calibration constants are kept, and the new ones are discarded.
    '''


class AdvanceTriggerDigitalEdgeEdge(Enum):
    RISING = 900
    r'''
    The trigger asserts on the rising edge of the signal.
    '''
    FALLING = 901
    r'''
    The trigger asserts on the falling edge of the signal.
    '''


class AdvanceTriggerType(Enum):
    NONE = 600
    r'''
    No Advance Trigger is configured.
    '''
    DIGITAL_EDGE = 601
    r'''
    The Advance Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the digital_edge_advance_trigger_source property.
    '''
    SOFTWARE_EDGE = 604
    r'''
    The Advance Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the send_software_edge_trigger method and selecting NIRFSA_VAL_ADVANCE_TRIGGER as the **trigger** parameter.
    '''


class AllowOutOfSpecificationUserSettings(Enum):
    DISABLED = 1900
    r'''
    Disables out-of-specification user settings.
    '''
    ENABLED = 1901
    r'''
    Enables out-of-specification user settings.
    '''


class ArmReferenceTriggerType(Enum):
    NONE = 600
    r'''
    No Arm Reference Trigger is configured.
    '''
    DIGITAL_EDGE = 601
    r'''
    The Arm Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the digital_edge_arm_ref_trigger_source property.
    '''
    SOFTWARE_EDGE = 604
    r'''
    The Arm Reference Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the send_software_edge_trigger method and selecting SoftwareTriggerType.ARM_REF as the **trigger** parameter.
    '''


class CalToneMode(Enum):
    DISABLED = 1900
    r'''
    Disables the calibration tone for the associated signal path.
    '''
    CAL_TONE_LOWBAND_RF = 2701
    r'''
    Injects the calibration tone into the low band RF signal path.
    '''
    CAL_TONE_HIGHBAND_RF = 2702
    r'''
    Injects the calibration tone into the high band RF signal path.
    '''
    CAL_TONE_HIGHBAND_IF = 2703
    r'''
    Injects the calibration tone into the high band IF signal path.
    '''
    CAL_TONE_LOWBAND_RF_WITHOUT_ALC = 2704
    r'''
    Injects the calibration tone into the low band RF signal path, bypassing the ALC.
    '''
    CAL_TONE_COMB_GENERATOR = 2705
    r'''
    Injects the calibration tone into the high band RF signal path through the Comb Generator.
    '''


class CalibrateStep(Enum):
    IF_ATTENUATION = 1600
    r'''
    Initializes the IF Attenuation Calibration step. This step is not supported for the PXIe-5693.
    '''
    IF_RESPONSE = 1601
    r'''
    Initializes the IF Response Calibration step. This step is not supported for the PXIe-5603/5605 or PXIe-5693/5698.
    '''
    IF_REF_LEVEL = 1602
    r'''
    Initializes the Ref Level Calibration step. This step is not supported on the PXIe-5694.
    '''
    LO_EXPORT = 1603
    r'''
    Initializes the LO Export Calibration step. This step calibrates the output power of each LO to be within specification. This step is not supported on the PXIe-5601 or the PXIe-5693/5694/5698.
    '''
    GAIN_REFERENCE = 1604
    r'''
    Initializes the Gain Reference Calibration step. This step calibrates the calibration tone amplitude across supported calibration tone frequencies. This step is not supported on the PXIe-5601/5603/5605 or PXIe-5694.
    '''


class ChannelCoupling(Enum):
    AC = 3001
    r'''
    Specifies that the RF input channel is AC-coupled. For low frequencies (<10 MHz), accuracy decreases because NI-RFSA does not calibrate the configuration.
    '''
    DC = 3002
    r'''
    Specifies that the RF input channel is DC-coupled. NI-RFSA enforces a minimum RF attenuation for device protection.
    '''


class ConditioningCalToneMode(Enum):
    DISABLED = 1900
    r'''
    Disables the calibration tone for the associated signal path.
    '''
    CAL_TONE_LOWBAND_RF = 2701
    r'''
    Injects the calibration tone into the low band RF signal path.
    '''
    CAL_TONE_HIGHBAND_RF = 2702
    r'''
    Injects the calibration tone into the high band RF signal path.
    '''


class DeembeddingType(Enum):
    NONE = 3900
    r'''
    De-embedding is not applied to the measurement.
    '''
    SCALAR = 3901
    r'''
    De-embeds the measurement using only the gain term.
    '''
    VECTOR = 3902
    r'''
    De-embeds the measurement using the gain term and the reflection term.
    '''


class DeviceResponseType(Enum):
    DOWNCONVERTER_IF = 2800
    r'''
    Returns the IF response of the downconverter.
    '''
    DOWNCONVERTER_RF = 2801
    r'''
    Returns the RF response of the downconverter. This value is supported only for the PXIe-5603/5605/5665/5667/5693..
    '''
    DOWNCONVERTER_COMBINED = 2802
    r'''
    Returns the combined RF and IF response of the downconverter. The combined response is in terms of IF frequency. This value is supported only for the PXIe-5603/5605/5665/5667.
    '''
    VSA_IF = 2803
    r'''
    Returns the IF response of the entire NI-RFSA device. This value is supported only for the PXIe-5665/5667.
    '''
    VSA_COMBINED = 2804
    r'''
    Returns the combined IF and RF response of the entire NI-RFSA device. The combined response is in terms of IF frequency. This value is supported only for the PXIe-5665/5667.
    '''


class DigitizerDitherEnabled(Enum):
    DISABLED = 1900
    r'''
    Disables dither on the digitizer.
    '''
    ENABLED = 1901
    r'''
    Enables dither on the digitizer.
    '''


class DigitizerSampleClockExportedTerminal(Enum):
    NONE = 'None'
    r'''
    The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646.
    '''
    CLK_OUT = 'ClkOut'
    r'''
    Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.
    '''


class DigitizerSampleClockTimebaseSource(Enum):
    ONBOARD_CLOCK = 'OnboardClock'
    r'''
    The digitizer uses its onboard clock as the Sample Clock timebase.
    '''
    CLK_IN = 'ClkIn'
    r'''
    The digitizer uses the signal present on the CLK IN connector as the Sample Clock timebase.
    '''
    LO_REF_CLK = 'LORefClk'
    r'''
    The digitizer uses the signal generated on the 100 MHz REF OUT terminal on the PXIe-5653 as the Sample Clock timebase. This value is supported only for the PXIe-5665.
    '''
    PXI_STAR = 'PXI_STAR'
    r'''
    The digitizer uses the signal present at the PXI star trigger line as the Sample Clock timebase. This value is not supported for the PXIe-5668.
    '''
    DOWNCONVERTER_LO2_OUT = 'DownconverterLO2Out'
    r'''
    The digitizer uses the signal present on the LO2 OUT connector on the downconverter as the Sample Clock timebase. This value is supported only for the PXIe-5668.
    '''


class DownconverterFrequencyOffsetMode(Enum):
    AUTOMATIC = 1903
    r'''
    NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the signal_bandwidth property has been set and can be avoided.
    '''
    ENABLED = 1901
    r'''
    NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the signal_bandwidth property has been set and can be avoided. NI-RFSA returns an error if the signal_bandwidth property has not been set, or if the signal bandwidth is too large.
    '''
    USER_DEFINED = 1904
    r'''
    NI-RFSA uses the offset that you specified with the downconverter_frequency_offset or downconverter_center_frequency properties.
    '''


class DownconverterLoopBandwidth(Enum):
    NARROW = 800
    r'''
    Specifies that the downconverter module uses a narrow loop bandwidth.
    '''
    MEDIUM = 801
    r'''
    Specifies that the downconverter module uses a medium loop bandwidth.
    '''
    WIDE = 802
    r'''
    Specifies that the downconverter module uses a wide loop bandwidth.
    '''


class DownconverterPreselectorEnabled(Enum):
    DISABLED = 2600
    r'''
    Disables the preselector.
    '''
    ENABLED_WHEN_IN_SIGNAL_PATH = 2601
    r'''
    The preselector is automatically enabled when it is in the signal path and is automatically disabled when it is not in the signal path. Use the preselector_present property to determine if the downconverter has an preselector.
    '''
    ENABLED = 2602
    r'''
    Enables the preselector. If the preselector is not in the signal path or if the preselector is not supported on the device, NI-RFSA returns an error. Select the DownconverterPreselectorEnabled.ENABLED_WHEN_IN_SIGNAL_PATH whenever possible avoid an error.
    '''


class EnableAttrVals(Enum):
    DISABLED = 1900
    r'''
    The property is disabled.
    '''
    ENABLED = 1901
    r'''
    The property is enabled.
    '''


class EnableRfPreamp(Enum):
    DISABLED = 2500
    r'''
    Disables the RF preamplifier.
    '''
    ENABLED_WHEN_IN_SIGNAL_PATH = 2501
    r'''
    Enables the RF preamplifier when the RF preamplifier is present in the signal path and disables the preamplifier when it is not in the signal path. Only devices with an RF preamplifier on the downconverter and an RF preselector support this option. Use the rf_preamp_present property to determine whether the downconverter has a preamplifier.
    '''
    ENABLED = 2502
    r'''
    Enables the RF preamplifier. If the RF preamplifier is not in a signal path, NI-RFSA returns an error. Select the EnableRfPreamp.ENABLED_WHEN_IN_SIGNAL_PATH value whenever possible to avoid an error.
    '''
    AUTOMATIC = 2503
    r'''
    Automatically enables the RF preamplifier based on the value of the reference_level property. This value is valid only for the PXIe-5644/5645/5646, PXIe-5667, and PXIe-5830/5831/5832/5840/5841.
    '''


class ExportOutputTerminal(Enum):
    DO_NOT_EXPORT = ''
    r'''
    The signal is not exported.
    '''
    CLK_OUT = 'ClkOut'
    r'''
    Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.
    '''
    REF_OUT = 'RefOut'
    r'''
    Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841.
    '''
    REF_OUT2 = 'RefOut2'
    r'''
    Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.
    '''
    PFI0 = 'PFI0'
    r'''
    The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.
    '''
    PFI1 = 'PFI1'
    r'''
    The trigger is received on PFI 1.
    '''
    PXI_TRIG0 = 'PXI_Trig0'
    r'''
    The trigger is received on PXI trigger line 0.
    '''
    PXI_TRIG1 = 'PXI_Trig1'
    r'''
    The trigger is received on PXI trigger line 1.
    '''
    PXI_TRIG2 = 'PXI_Trig2'
    r'''
    The trigger is received on PXI trigger line 2.
    '''
    PXI_TRIG3 = 'PXI_Trig3'
    r'''
    The trigger is received on PXI trigger line 3.
    '''
    PXI_TRIG4 = 'PXI_Trig4'
    r'''
    The trigger is received on PXI trigger line 4.
    '''
    PXI_TRIG5 = 'PXI_Trig5'
    r'''
    The trigger is received on PXI trigger line 5.
    '''
    PXI_TRIG6 = 'PXI_Trig6'
    r'''
    The trigger is received on PXI trigger line 6.
    '''
    PXI_TRIG7 = 'PXI_Trig7'
    r'''
    The trigger is received on PXI trigger line 7.
    '''
    PXI_STAR = 'PXI_STAR'
    r'''
    The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.
    '''
    PXIE_DSTARC = 'PXIe_DStarC'
    r'''
    The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.
    '''
    DIO_PFI0 = 'DIO/PFI0'
    r'''
    The trigger is received on PFI0 from the front panel DIO terminal.
    '''
    DIO_PFI1 = 'DIO/PFI1'
    r'''
    The trigger is received on PFI1 from the front panel DIO terminal.
    '''
    DIO_PFI2 = 'DIO/PFI2'
    r'''
    The trigger is received on PFI2 from the front panel DIO terminal.
    '''
    DIO_PFI3 = 'DIO/PFI3'
    r'''
    The trigger is received on PFI3 from the front panel DIO terminal.
    '''
    DIO_PFI4 = 'DIO/PFI4'
    r'''
    The trigger is received on PFI4 from the front panel DIO terminal.
    '''
    DIO_PFI5 = 'DIO/PFI5'
    r'''
    The trigger is received on PFI5 from the front panel DIO terminal.
    '''
    DIO_PFI6 = 'DIO/PFI6'
    r'''
    The trigger is received on PFI6 from the front panel DIO terminal.
    '''
    DIO_PFI7 = 'DIO/PFI7'
    r'''
    The trigger is received on PFI7 from the front panel DIO terminal.
    '''


class FetchRelativeTo(Enum):
    MOST_RECENT_SAMPLE = 700
    r'''
    Fetching occurs relative to the most recently acquired data. The value of the fetch_offset property must be negative.
    '''
    FIRST_SAMPLE = 701
    r'''
    Fetching occurs at the first sample acquired by the device. If the device wraps its buffer, the first sample is no longer available. In this case, NI-RFSA returns an error if the fetch offset is in the overwritten data.
    '''
    REFERENCE_TRIGGER = 702
    r'''
    Fetching occurs relative to the Reference Trigger. This value behaves like FetchRelativeTo.FIRST_SAMPLE if no Reference Trigger is configured.
    '''
    FIRST_PRETRIGGER_SAMPLE = 703
    r'''
    Fetching occurs relative to the first pretrigger sample acquired.
    '''
    CURRENT_READ_POSITION = 704
    r'''
    Fetching occurs after the last fetched sample.
    '''


class FrequencySettlingUnits(Enum):
    PPM = 2000
    r'''
    Specifies the frequency settling time in parts per million (PPM).
    '''
    SECONDS_AFTER_LOCK = 2001
    r'''
    Specifies the frequency settling in time after lock (seconds).
    '''
    SECONDS_AFTER_IO = 2002
    r'''
    Specifies the frequency settling time after I/O (seconds).
    '''


class IFattenTableSel(Enum):
    STANDARD = 2900
    r'''
    Specifies that the standard IF attenuation table is used for the external calibration.
    '''
    ACPR = 2901
    r'''
    Specifies that the adjacent channel power ratio (ACPR) IF attenuation table is used for the external calibration. You can only select this value if you set the CAL_IF_FILTER_SELECTION property to IFfilterSelection.EXT_CAL_IF_FILTER_PATH_1 or IFfilterSelection.EXT_CAL_IF_FILTER_PATH_2.
    '''


class IFfilter(Enum):
    _187_5_MHZ_WIDE = 1400
    r'''
    The device uses the 187.5 MHz wide bandwidth filter.
    '''
    _187_5_MHZ_NARROW = 1401
    r'''
    The device uses the 187.5 MHz narrow bandwidth filter.
    '''
    _53_MHZ = 1402
    r'''
    The device uses the 53 MHz filter.
    '''
    BYPASS = 1403
    r'''
    The device bypasses the IF filter.
    '''


class IFfilterSelection(Enum):
    EXT_CAL_IF_FILTER_PATH_1 = 2100
    r'''
    Specifies that the 5 MHz filter path is used during calibration.
    '''
    EXT_CAL_IF_FILTER_PATH_2 = 2101
    r'''
    Specifies that the 300 kHz filter path is used during calibration. Not supported for the PXIe-5694.
    '''
    EXT_CAL_IF_FILTER_PATH_3 = 2102
    r'''
    None of the IF filter paths are used during calibration.
    '''
    EXT_CAL_IF_FILTER_PATH_4 = 2103
    r'''
    Specifies that the 20 MHz filter path is used during calibration.
    '''
    EXT_CAL_IF_FILTER_PATH_5 = 2104
    r'''
    Specifies that the 1.4 MHz filter path is used during calibration.
    '''
    EXT_CAL_IF_FILTER_PATH_6 = 2105
    r'''
    Specifies that the 400 kHz filter path is used during calibration.
    '''
    EXT_CAL_IF_FILTER_PATH_7 = 2106
    r'''
    Specifies that the 110 kHz filter path is used during calibration.
    '''
    EXT_CAL_IF_FILTER_PATH_8 = 2107
    r'''
    Specifies that the 30 kHz filter path is used during calibration.
    '''


class IfConditioningDownConversionEnabled(Enum):
    DISABLED = 1900
    r'''
    Disables IF conditioning downconversion.
    '''
    ENABLED = 1901
    r'''
    Enables IF conditioning downconversion.
    '''


class InputIsolationEnabled(Enum):
    DISABLED = 1900
    r'''
    Disables input isolation.
    '''
    ENABLED = 1901
    r'''
    Enables input isolation.
    '''


class InputPort(Enum):
    RF_IN = 2000
    r'''
    Enables the RF IN port.
    '''
    IQ_IN = 2001
    r'''
    Enables the I/Q IN port.
    '''
    CAL_IN = 2002
    r'''
    Enables the CAL IN port.
    '''
    I_ONLY = 2003
    r'''
    Enables the I terminals of the I/Q IN port. It is supported only for PXIe-5645.
    '''


class IqInPortTerminalConfiguration(Enum):
    DIFFERENTIAL = 2100
    r'''
    Sets the terminal configuration to differential.
    '''
    SINGLE_ENDED = 2101
    r'''
    Sets the terminal configuration to single-ended.
    '''


class LinearInterpolationFormat(Enum):
    MAGNITUDE_AND_PHASE = 4001
    r'''
    Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion.
    '''
    MAGNITUDE_DB_AND_PHASE = 4002
    r'''
    Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.
    '''
    REAL_AND_IMAGINARY = 4000
    r'''
    Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.
    '''


class Lo2ExportEnabled(Enum):
    DISABLED = 1900
    r'''
    Disables LO2 export.
    '''
    ENABLED = 1901
    r'''
    Enables LO2 export.
    '''


class LoInjection(Enum):
    HIGH = 1300
    r'''
    Configures the LO signal that the NI-RFSA device generates at a frequency higher than the RF frequency. This LO frequency is given by the formula f<sub>LO</sub> = f<sub>RF</sub> + f<sub>IF</sub>.
    '''
    LOW = 1301
    r'''
    Configures the LO signal that the NI-RFSA device generates at a frequency lower than the RF frequency. This LO frequency is given by the formula f<sub>LO</sub> = f<sub>RF</sub> - f<sub>IF</sub>.
    '''


class LoNumber(Enum):
    LO2 = 2201
    r'''
    Selects LO2, which is the 4 GHz signal path.
    '''
    LO3 = 2202
    r'''
    Selects LO3, which is the 800 MHz signal path.
    '''
    LO1 = 2200
    r'''
    Selects LO1, which is the 3.2 GHz to 8.3 GHz variable signal path.
    '''


class LoOutExportConfigureFromRfsg(Enum):
    DISABLED = 1900
    r'''
    Do not allow NI-RFSG to control the NI-RFSA local oscillator export.
    '''
    ENABLED = 1901
    r'''
    Allow NI-RFSG to control the NI-RFSA local oscillator export.
    '''


class LoPathSel(Enum):
    EXT_CAL_LO_PATH_1 = 2300
    r'''
    Specifies that the LO path 1 is used.
    '''
    EXT_CAL_LO_PATH_2 = 2301
    r'''
    Specifies that the LO path 2 is used.
    '''
    EXT_CAL_LO_PATH_3 = 2302
    r'''
    Specifies that the LO path 3 is used.
    '''
    EXT_CAL_LO_PATH_4 = 2303
    r'''
    Specifies that the LO path 4 is used.
    '''
    EXT_CAL_LO_PATH_5 = 2304
    r'''
    Specifies that the LO path 5 is used.
    '''


class LoPllFractionalModeEnabled(Enum):
    DISABLED = 1900
    r'''
    Disables fractional mode for the LO PLL.
    '''
    ENABLED = 1901
    r'''
    Enables fractional mode for the LO PLL.
    '''


class LoSource(Enum):
    NONE = 'None'
    r'''
    Specifies that no LO source is required to downconvert the RF input signal.
    '''
    ONBOARD = 'Onboard'
    r'''
    Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal.**PXIe-5831/5832** This configuration uses the onboard LO of the PXIe-3622, using the LO2 stage.**PXIe-5831/5832 with PXIe-5653** This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3622.**PXIe-5841 with PXIe-5655** This configuration uses the onboard LO of the PXIe-5655.
    '''
    LO_IN = 'LO_In'
    r'''
    Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel.
    '''
    LO_SOURCE_SECONDARY = 'Secondary'
    r'''
    Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid on only the PXIe-5831 with PXIe-5653 (LO1 stage only) or PXIe-5832 with PCIe-5653 (LO1 stage only).
    '''
    LO_SOURCE_SG_SA_SHARED = 'SG_SA_Shared'
    r'''
    Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSA selects an internal synthesizer and the synthesizer signal is switched to both the RF Out and RF In mixers. This value is valid on only the PXIe-5830/5831/5832/5841 with PXIe-5655.
    '''


class LoYigMainCoilDrive(Enum):
    NORMAL = 2400
    r'''
    Adjusts the YIG main coil on the LO for an underdamped response.
    '''
    FAST = 2401
    r'''
    Adjusts the YIG main coil on the LO for an overdamped response.
    '''


class LoadConfigurationResetOptions(Enum):
    NONE = 0
    r'''
    NI-RFSA resets all configurations.
    '''
    DEEMBEDDING_TABLES = 2
    r'''
    NI-RFSA skips resetting the de-embedding tables.
    '''


class NoiseSourcePowerEnabled(Enum):
    DISABLED = 1900
    r'''
    Disables the noise source power.
    '''
    ENABLED = 1901
    r'''
    Enables the noise source power.
    '''


class NotchFilterEnabled(Enum):
    DISABLED = 3400
    r'''
    Disables the notch filter.
    '''
    ENABLED_WHEN_IN_SIGNAL_PATH = 3401
    r'''
    The notch filter is automatically enabled when it is in the signal path and automatically disabled when it is not in the signal path.
    '''
    ENABLED = 3402
    r'''
    Enables the notch filter. If the notch filter is not in the signal path or if the notch filter is not supported on the device, NI-RFSA returns an error. Select NotchFilterEnabled.ENABLED_WHEN_IN_SIGNAL_PATH whenever possible to avoid an error.
    '''


class OutputTerm(Enum):
    DO_NOT_EXPORT = ''
    r'''
    The signal is not exported.
    '''
    CLK_OUT = 'ClkOut'
    r'''
    Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.
    '''
    REF_OUT = 'RefOut'
    r'''
    Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841.
    '''
    REF_OUT2 = 'RefOut2'
    r'''
    Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.
    '''
    PFI0 = 'PFI0'
    r'''
    The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.
    '''
    PFI1 = 'PFI1'
    r'''
    The trigger is received on PFI 1.
    '''
    PXI_TRIG0 = 'PXI_Trig0'
    r'''
    The trigger is received on PXI trigger line 0.
    '''
    PXI_TRIG1 = 'PXI_Trig1'
    r'''
    The trigger is received on PXI trigger line 1.
    '''
    PXI_TRIG2 = 'PXI_Trig2'
    r'''
    The trigger is received on PXI trigger line 2.
    '''
    PXI_TRIG3 = 'PXI_Trig3'
    r'''
    The trigger is received on PXI trigger line 3.
    '''
    PXI_TRIG4 = 'PXI_Trig4'
    r'''
    The trigger is received on PXI trigger line 4.
    '''
    PXI_TRIG5 = 'PXI_Trig5'
    r'''
    The trigger is received on PXI trigger line 5.
    '''
    PXI_TRIG6 = 'PXI_Trig6'
    r'''
    The trigger is received on PXI trigger line 6.
    '''
    PXI_TRIG7 = 'PXI_Trig7'
    r'''
    The trigger is received on PXI trigger line 7.
    '''
    PXI_STAR = 'PXI_STAR'
    r'''
    The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.
    '''
    PXIE_DSTARB = 'PXIe_DStarB'
    r'''
    The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.
    '''
    DIO_PFI0 = 'DIO/PFI0'
    r'''
    The trigger is received on PFI0 from the front panel DIO terminal.
    '''
    DIO_PFI1 = 'DIO/PFI1'
    r'''
    The trigger is received on PFI1 from the front panel DIO terminal.
    '''
    DIO_PFI2 = 'DIO/PFI2'
    r'''
    The trigger is received on PFI2 from the front panel DIO terminal.
    '''
    DIO_PFI3 = 'DIO/PFI3'
    r'''
    The trigger is received on PFI3 from the front panel DIO terminal.
    '''
    DIO_PFI4 = 'DIO/PFI4'
    r'''
    The trigger is received on PFI4 from the front panel DIO terminal.
    '''
    DIO_PFI5 = 'DIO/PFI5'
    r'''
    The trigger is received on PFI5 from the front panel DIO terminal.
    '''
    DIO_PFI6 = 'DIO/PFI6'
    r'''
    The trigger is received on PFI6 from the front panel DIO terminal.
    '''
    DIO_PFI7 = 'DIO/PFI7'
    r'''
    The trigger is received on PFI7 from the front panel DIO terminal.
    '''
    TIMER_EVENT = 'TimerEvent'
    r'''
    The trigger is received from the Timer Event. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841, and for digital edge Advance Triggers on the PXIe-5663E/5665.
    '''


class OverflowErrorReporting(Enum):
    WARNING = 1301
    r'''
    Configures NI-RFSA to return a warning when an ADC or onboard signal processing (OSP) overflow occurs.
    '''
    DISABLED = 1302
    r'''
    Configures NI-RFSA to not return an error or a warning when an ADC or OSP overflow occurs.
    '''


class PowerSpectrumUnits(Enum):
    DBM = 200
    r'''
    Units are dB with reference to 1 milliwatt.
    '''
    VOLTS_SQUARED = 201
    r'''
    Units are in volts squared.
    '''
    DBMV = 202
    r'''
    Units are dB with reference to 1 millivolt.
    '''
    DBUV = 203
    r'''
    Units are dB with reference to 1 microvolt.
    '''
    VOLTS = 204
    r'''
    Units are in volts.
    '''
    WATTS = 205
    r'''
    Units are in watts.
    '''


class PxiChassisClk10Source(Enum):
    NONE = 'None'
    r'''
    The device does not drive the PXI 10 MHz backplane Reference Clock.
    '''
    ONBOARD_CLOCK = 'OnboardClock'
    r'''
    The device drives the PXI 10 MHz backplane Reference Clock with the PXI-5600 onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front panel to use this option.
    '''
    REF_IN = 'RefIn'
    r'''
    The device drives the PXI 10 MHz backplane Reference Clock with the reference source attached to the PXI-5600 FREQ REF IN connector. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front panel to use this option.
    '''


class ReferenceClockExportedRate(Enum):
    _10MHZ = 10000000
    r'''
    Exports a 10 MHz Reference Clock.
    '''
    _100MHZ = 100000000
    r'''
    Exports a 100 MHz Reference Clock.
    '''
    _1GHZ = 1000000000.0
    r'''
    Exports a 1 GHz Reference Clock.
    '''


class ReferenceClockExportedTerminal(Enum):
    NONE = 'None'
    r'''
    The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646.
    '''
    REF_OUT = 'RefOut'
    r'''
    Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841.
    '''
    REF_OUT2 = 'RefOut2'
    r'''
    Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.
    '''
    CLK_OUT = 'ClkOut'
    r'''
    Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.
    '''
    IF_COND_REF_OUT = 'IFCondRefOut'
    r'''
    Export the clock on the REF OUT terminal on the PXIe-5694. This value is valid only for the PXIe-5667.
    '''


class ReferenceClockSource(Enum):
    NONE = 'None'
    r'''
    No Reference Clock is required for the current device configuration. This value is valid only for the PXIe-5694 or the PXIe-5668.
    '''
    ONBOARD_CLOCK = 'OnboardClock'
    r'''
    **PXI-5661 **NI-RFSA locks the NI-RFSA device to the PXI-5600 RF downconverter onboard clock.**PXIe-5663/5663E **NI-RFSA locks the PXIe-5663/5663E to the PXI/PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, connect the REF IN/OUT connector on the PXI/PXIe-5652 to the CLK IN terminal on the PXI5622.**PXIe-5665 **NI-RFSA locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622.**PXIe-5667 **NI-RFSA locks the PXIe-5667 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694.**PXIe-5668 **Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624.**PXIe-5830/5831 **For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector.**PXIe-5831/5832 with PXIe-5653 **Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector.**PXIe-5644/5645/5646, PXIe-5820/5840/5841 **Lock the NI-RFSA device to its onboard clock.**PXIe-5841 with PXIe-5655 **Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector.**PXIe-5842 **Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the User Manual for the instrument.**PXIe-5860 **Lock to the PXIe-5860 onboard clock.
    '''
    REF_IN = 'RefIn'
    r'''
    **PXI-5661 **NI-RFSA locks the NI-RFSA device to the signal at the external FREQ REF IN connector on the PXI-5600**PXIe-5663/5663E **Connect the external signal to the PXI/PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, this configuration can only be used in external digitizer mode.**PXIe-5665 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the ref_clock_rate property according to the frequency of your external clock signal.**PXIe-5667 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. If your external clock signal frequency is set to a frequency other than 10 MHz, set the ref_clock_rate property according to the frequency of your external clock signal.**PXIe-5668 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the **clock rate** parameter according to the frequency of your external clock signal.**PXIe-5694 **Connect the Reference Clock signal to the REF/LO IN connector on the PXIe-5694 front panel.**PXIe-5644/5645/5646, PXIe-5820/5840/5841 **Lock the NI-RFSA device to the signal at the external REF IN connector.**PXIe-5830/5831 **For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831/5832, lock the external signal to the PXIe-3622 REF IN connector.**PXIe-5831/5832 with PXIe-5653 **Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector.**PXIe-5841 with PXIe-5655 **Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. **PXIe-5842 **Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the User Manual for the instrument. PXIe-5860 Lock to the signal at the REF IN connector on the PXIe-5860.
    '''
    PXI_CLK = 'PXI_Clk'
    r'''
    **PXI-5661 **NI-RFSA locks the NI-RFSA device to the PXI backplane clock using the PXI-5600. You must connect the PXI 10 MHz connector to the REF IN connector on the PXI-5600 front panel to use this option. **PXIe-5668 **Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624.**PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655/5842/5860 **Lock the device to the PXI backplane clock.
    '''
    CLK_IN = 'ClkIn'
    r'''
    **PXI-5661 **This configuration does not apply to the PXI-5661.**PXIe-5663/5663E **NI-RFSA locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXI/PXIe-5652.**PXIe-5665 **NI-RFSA locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the ref_clock_rate property to 100 MHz.**PXIe-5667 **NI-RFSA locks the PXIe-5667 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. Set the ref_clock_rate property to 100 MHz.**PXIe-5668 **Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the **clock rate** parameter to 100 MHz.**PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655/5842/5860 **This configuration does not apply.
    '''
    PXI_CLK_MASTER = 'PXI_ClkMaster'
    r'''
    **PXIe-5831/5832 with PXIe-5653 **NI-RFSA configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.**PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5644/5645/5646, PXIe-5820/5840/5841/5841 with PXIe-5655 /5842/5860**This configuration does not apply.
    '''
    REF_IN_2 = 'RefIn2'
    r'''
    **PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655 **This configuration does not apply.
    '''


class ReferenceLevelDataType(Enum):
    MECHANICAL_ATTENUATOR_DISABLED = 1801
    r'''
    The data is the configuration data when the mechanical relay is disabled. Use this option to save uncalibrated measurements for more advanced operations.
    '''
    DEFAULT = 1800
    r'''
    The data is the default configuration data.
    '''


class ReferenceTriggerDigitalEdgeEdge(Enum):
    RISING = 900
    r'''
    The trigger asserts on the rising edge of the signal.
    '''
    FALLING = 901
    r'''
    The trigger asserts on the falling edge of the signal
    '''


class ReferenceTriggerIqPowerEdgeSlope(Enum):
    RISING = 1000
    r'''
    The trigger asserts when the signal power is rising.
    '''
    FALLING = 1001
    r'''
    The trigger asserts when the signal power is falling.
    '''


class ReferenceTriggerOspDelayEnabled(Enum):
    DISABLED = 1900
    r'''
    Disables OSP delay for the Reference Trigger.
    '''
    ENABLED = 1901
    r'''
    Enables OSP delay for the Reference Trigger.
    '''


class ReferenceTriggerType(Enum):
    NONE = 600
    r'''
    No Reference Trigger is configured.
    '''
    DIGITAL_EDGE = 601
    r'''
    The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the digital_edge_ref_trigger_source property.
    '''
    IQ_POWER_EDGE = 603
    r'''
    The Reference Trigger is asserted when the signal is changing past the level specified with the slope (rising or falling) configured with the iq_power_edge_ref_trigger_slope property.
    '''
    SOFTWARE_EDGE = 604
    r'''
    The Reference Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the send_software_edge_trigger method and selecting NIRFSA_VAL_REF_TRIGGER as the **trigger** parameter.
    '''
    IQ_ANALOG_EDGE = 605
    r'''
    The Reference Trigger is asserted when the I or Q signal is changed past the level specified with the slope configured with the IQ_ANALOG_EDGE_REF_TRIGGER_SLOPE property. This value is valid only for PXIe-5644/5645 devices.
    '''


class ResetWithOptionsStepsToOmit(IntFlag):
    DEEMBEDDING_TABLES = 2
    r'''
    Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.
    '''
    NONE = 0
    r'''
    No step is omitted during reset.
    '''
    ROUTES = 1
    r'''
    Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.
    '''


class RfLbSigCondPathSel(Enum):
    EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1 = 3700
    r'''
    yet to be defined
    '''
    EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_2 = 3701
    r'''
    yet to be defined
    '''


class RfOutLoExport(Enum):
    DISABLED = 1900
    r'''
    The LO signal is not exported from the RF OUT LO OUT terminal.
    '''
    ENABLED = 1901
    r'''
    The LO signal is exported from the RF OUT LO OUT terminal.
    '''
    UNSPECIFIED = 1902
    r'''
    The LO signal may or may not be exported to the RF OUT LO OUT terminal, because NI-RFSG may be controlling it.
    '''


class RfPathSelection(Enum):
    EXT_CAL_RF_BAND_1 = 1700
    r'''
    The data is the default configuration data.
    '''
    EXT_CAL_RF_BAND_2 = 1701
    r'''
    The data is the configuration data when the mechanical relay is disabled. Use this option to save uncalibrated measurements for more advanced operations.
    '''
    EXT_CAL_RF_BAND_3 = 1702
    r'''
    The data is the default configuration data.
    '''
    EXT_CAL_RF_BAND_4 = 1703
    r'''
    The data is the default configuration data.
    '''


class SelfCalSteps(IntFlag):
    DIGITIZER_SELF_CAL = 8
    r'''
    Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.
    '''
    PRESELECTOR_ALIGNMENT = 1
    r'''
    Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.
    '''
    OMIT_NONE = 0
    r'''
    No calibration steps are omitted.
    '''
    GAIN_REFERENCE = 2
    r'''
    Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.
    '''
    IF_FLATNESS = 4
    r'''
    Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.
    '''
    LO_SELF_CAL = 10
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''
    AMPLITUDE_ACCURACY = 20
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''
    RESIDUAL_LO_POWER = 40
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''
    IMAGE_SUPPRESSION = 80
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''
    SYNTHESIZER_ALIGNMENT = 100
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''
    DC_OFFSET = 200
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''


class SelfCalibrateRangeStepsToOmit(IntFlag):
    DIGITIZER_SELF_CAL = 8
    r'''
    Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.
    '''
    PRESELECTOR_ALIGNMENT = 1
    r'''
    Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.
    '''
    OMIT_NONE = 0
    r'''
    No calibration steps are omitted.
    '''
    GAIN_REFERENCE = 2
    r'''
    Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.
    '''
    IF_FLATNESS = 4
    r'''
    Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.
    '''
    LO_SELF_CAL = 10
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''
    AMPLITUDE_ACCURACY = 20
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''
    RESIDUAL_LO_POWER = 40
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''
    IMAGE_SUPPRESSION = 80
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''
    SYNTHESIZER_ALIGNMENT = 100
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''
    DC_OFFSET = 200
    r'''
    Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.
    '''


class SelfCalibrationStep(Enum):
    PRESELECTOR_ALIGNMENT = 1
    r'''
    Calls for preselector alignment.
    '''
    GAIN_REFERENCE = 2
    r'''
    Measures the changes in gain since the last external calibration was run.
    '''
    IF_FLATNESS = 4
    r'''
    Measures the IF response of the entire system for each of the supported IF filters
    '''
    DIGITIZER_SELF_CAL = 8
    r'''
    Calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter.
    '''
    LO_SELF_CAL = 16
    r'''
    Calls for LO self-calibration, if the LO source module is associated with the RF downconverter.
    '''
    AMPLITUDE_ACCURACY = 32
    r'''
    Selects the Amplitude Accuracy self-calibration step.
    '''
    RESIDUAL_LO_POWER = 64
    r'''
    Selects the Residual LO Power self-calibration step.
    '''
    IMAGE_SUPPRESSION = 128
    r'''
    Selects the Image Suppression self-calibration step.
    '''
    SYNTHESIZER_ALIGNMENT = 256
    r'''
    Selects the Synthesizer Alignment self-calibration step.
    '''
    DC_OFFSET = 512
    r'''
    Selects the DC Offset self-calibration step.
    '''


class Signal(Enum):
    START_TRIGGER = 1100
    r'''
    NI-RFSA routes a Start Trigger.
    '''
    REF_TRIGGER = 702
    r'''
    NI-RFSA routes a Reference
    '''
    ADVANCE_TRIGGER = 1102
    r'''
    NI-RFSA routes an Advance
    '''
    READY_FOR_START_EVENT = 1200
    r'''
    NI-RFSA routes a Ready for Start Event.
    '''
    READY_FOR_REF_EVENT = 1201
    r'''
    NI-RFSA routes a Ready for Reference Event..
    '''
    END_OF_RECORD_EVENT = 1203
    r'''
    NI-RFSA routes a End of Record Event.
    '''
    DONE_EVENT = 1204
    r'''
    NI-RFSA routes a Done Event.
    '''
    REF_CLOCK = 1205
    r'''
    NI-RFSA routes a Reference Clock.
    '''
    USER = 1206
    r'''
    NI-RFSA routes a User Defined Signal.
    '''


class SignalConditioningEnabled(Enum):
    ENABLED = 3600
    r'''
    Enables signal conditioning.
    '''
    BYPASSED = 3601
    r'''
    Bypasses all signal conditioning.
    '''


class SmoothSpectrumEnabled(Enum):
    DISABLED = 1900
    r'''
    Disables spectrum smoothing.
    '''
    ENABLED = 1901
    r'''
    Enables spectrum smoothing.
    '''


class SoftwareTriggerType(Enum):
    START = 1100
    r'''
    NI-RFSA sends a Start software trigger.
    '''
    REF = 702
    r'''
    NI-RFSA sends a Reference software trigger.
    '''
    ADVANCE = 1102
    r'''
    NI-RFSA sends an Advance software trigger.
    '''
    ARM_REF = 1103
    r'''
    NI-RFSA sends an Arm Reference software trigger. This trigger is not valid for the PXIe-5668.
    '''


class SparameterOrientation(Enum):
    PORT1_TOWARDS_DUT = 3800
    r'''
    Port 1 of the S2P is oriented towards the DUT port.
    '''
    PORT2_TOWARDS_DUT = 3801
    r'''
    Port 2 of the S2P is oriented towards the DUT port.
    '''


class SpectrumAveragingMode(Enum):
    NO = 400
    r'''
    Configures NI-RFSA to perform no averaging on acquisitions.
    '''
    RMS = 401
    r'''
    Configures NI-RFSA for root-mean-square (RMS) averaging. RMS averaging reduces signal fluctuations but not the noise floor. RMS averaging averages the energy, or power, of the signal. This averaging prevents noise floor reduction and gives averaged RMS quantities of single-channel measurements zero phase. RMS averaging for dual-channel measurements preserves important phase information.
    '''
    VECTOR = 402
    r'''
    Configures NI-RFSA for vector averaging. Vector averaging reduces noise from synchronous signals. Vector averaging computes the average of complex quantities directly, which means that it allows separate averaging for real and imaginary parts. Complex averaging such as vector averaging reduces noise and usually requires a trigger to improve block-to-block phase coherence.
    '''
    PEAK_HOLD = 403
    r'''
    Configures NI-RFSA for peak-hold averaging. Peak-hold averaging retains the RMS peak levels of the averaged quantities. The peak-hold averaging process performs peak-hold at each frequency bin separately to retain peak RMS levels from one FFT record to the next.
    '''
    MIN_HOLD = 404
    r'''
    Configures NI-RFSA to perform no averaging on acquisitions.
    '''
    SCALAR = 405
    r'''
    Configures NI-RFSA to perform no averaging on acquisitions.
    '''
    LOG = 406
    r'''
    Configures NI-RFSA to perform no averaging on acquisitions.
    '''


class SpectrumFftWindowType(Enum):
    UNIFORM = 500
    r'''
    No window is applied.
    '''
    HANNING = 501
    r'''
    The Hanning window is useful for analyzing transients longer than the time duration of the window, and also for general-purpose applications.
    '''
    HAMMING = 502
    r'''
    A Hamming window is applied to the waveform using the following equation: y[i] = x[i] * (0.54 - 0.46cos(w)) where w = (2)i/n and n = the waveform size. Note: Hanning and Hamming windows are somewhat similar. However, in the time domain, the Hamming window does not get as close to zero near the edges as does the Hanning window.
    '''
    BLACKMAN_HARRIS = 503
    r'''
    A Blackman-Harris window is applied to the waveform using the following equation: y[i] = x[i] * (0.42323 - 0.49755*cos(w) + 0.07922*cos(2w))
    '''
    EXACT_BLACKMAN = 504
    r'''
    An Exact Blackman window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w))
    '''
    BLACKMAN = 505
    r'''
    A Blackman window is useful for analyzing transient signals, and provides similar windowing to Hanning and Hamming windows but adds one additional cosine term to reduce ripple. A Blackman window is applied to the waveform using the following equation: y[i] = x[i] * (0.42 - 0.50*cos(w) + 0.08*cos(2w))
    '''
    FLAT_TOP = 506
    r'''
    The fifth-order Flat Top window has the best amplitude accuracy of all the window methods. The increased amplitude accuracy (0.02 dB for signals exactly between integral cycles) is at the expense of frequency selectivity. The Flat Top window is most useful in accurately measuring the amplitude of single frequency components with little nearby spectral energy in the signal. A fifth-order Flat Top window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w) + a4*cos(4w))
    '''
    _4_TERM_BLACKMAN_HARRIS = 507
    r'''
    A 4-term Blackman-Harris window is a general purpose window; it has side-lobe rejection in the upper 90 dB, with moderately wide side lobe. A 4-term Blackman Harris window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w))
    '''
    _7_TERM_BLACKMAN_HARRIS = 508
    r'''
    A 7-term Blackman-Harris window has the highest dynamic range; it is ideal for signal-to-noise ratio applications. A 7-term Blackman Harris window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w) + a4*cos(4w) - a5*cos(5w) + a6*cos(6w))
    '''
    LOW_SIDE_LOBE = 509
    r'''
    The Low Side Lobe window further reduces the size of the main lobe. The following equation defines the Low Side Lobe window. where   *N* is the length of window
    '''
    GAUSSIAN = 510
    r'''
    A Gaussian window is applied to the waveform using the following equation: y[i] = x[i] * exp(-0.5*(i - (N-1)/2)^2 / ((N-1)/2)^2) where N is the length of the window
    '''
    KAISER_BESSEL = 511
    r'''
    A Kaiser-Bessel window is applied to the waveform using the following equation: y[i] = x[i] * I0(β*sqrt(1 - (2i/(N-1) - 1)^2))/I0(β) where i is between 0 and N-1, N is the length of the window, β determines the shape of the window, and I0 is the zeroth order Modified Bessel method of the first kind
    '''


class SpectrumResolutionBandwidthType(Enum):
    THREE_DECIBELS = 300
    r'''
    Defines the resolution bandwidth (RBW) in terms of the 3 dB bandwidth of the window specified by the fft_window_type property.
    '''
    SIX_DECIBELS = 301
    r'''
    Defines the RBW in terms of the 6 dB bandwidth of the window specified by the fft_window_type property.
    '''
    BIN_WIDTH = 302
    r'''
    Defines the RBW in terms of the display resolution, which is the ratio of the sampling frequency to the number of samples that you acquire.
    '''
    EQUIVALENT_NOISE_BANDWIDTH = 303
    r'''
    Defines the RBW in terms of the equivalent noise bandwidth (ENBW) of the window specified by the fft_window_type property.
    '''


class StartTriggerDigitalEdgeEdge(Enum):
    RISING = 900
    r'''
    The trigger asserts on the rising edge of the signal.PXI-5661, PXIe-5663/5663E/5665/5668
    '''
    FALLING = 901
    r'''
    The trigger asserts on the falling edge of the signal | PXIe-5668
    '''


class StartTriggerType(Enum):
    NONE = 600
    r'''
    No Start Trigger is configured.
    '''
    DIGITAL_EDGE = 601
    r'''
    The Start Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the digital_edge_start_trigger_source property.
    '''
    SOFTWARE_EDGE = 604
    r'''
    The Start Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the send_software_edge_trigger method and selecting NIRFSA_VAL_START_TRIGGER as the value of the **trigger** parameter.
    '''


class StepsToOmit(Enum):
    DEEMBEDDING_TABLES = 2
    r'''
    Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.
    '''
    NONE = 0
    r'''
    No step is omitted during reset.
    '''
    ROUTES = 1
    r'''
    Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.
    '''


class SyncRefTriggerDelayEnabled(Enum):
    DISABLED = 1900
    r'''
    Disables synchronization reference trigger delay.
    '''
    ENABLED = 1901
    r'''
    Enables synchronization reference trigger delay.
    '''


class UserSourcePulseWidthUnits(Enum):
    SECONDS = 6200
    r'''
    Units are seconds.
    '''
    CLOCK_PERIODS = 6201
    r'''
    Units are clock periods.
    '''
