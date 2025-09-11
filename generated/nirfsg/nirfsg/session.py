# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import nirfsg._attributes as _attributes
import nirfsg._converters as _converters
import nirfsg._library_interpreter as _library_interpreter
import nirfsg.enums as enums
import nirfsg.errors as errors

import hightime
import nitclk

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class _Generation(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    @wraps(f)
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.unlock()


class _RepeatedCapabilities(object):
    def __init__(self, session, prefix, current_repeated_capability_list):
        self._session = session
        self._prefix = prefix
        # We need at least one element. If we get an empty list, make the one element an empty string
        self._current_repeated_capability_list = current_repeated_capability_list if len(current_repeated_capability_list) > 0 else ['']
        # Now we know there is at lease one entry, so we look if it is an empty string or not
        self._separator = '/' if len(self._current_repeated_capability_list[0]) > 0 else ''

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)
        complete_rep_cap_list = [current_rep_cap + self._separator + rep_cap for current_rep_cap in self._current_repeated_capability_list for rep_cap in rep_caps_list]

        return _SessionBase(
            repeated_capability_list=complete_rep_cap_list,
            all_channels_in_session=self._session._all_channels_in_session,
            interpreter=self._session._interpreter,
            freeze_it=True
        )


# This is a very simple context manager we can use when we need to set/get attributes
# or call functions from _SessionBase that require no channels. It is tied to the specific
# implementation of _SessionBase and how repeated capabilities are handled.
class _NoChannel(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._repeated_capability_cache = self._session._repeated_capability
        self._session._repeated_capability = ''

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._repeated_capability = self._repeated_capability_cache


class _SessionBase(object):
    '''Base class for all NI-RFSG sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    absolute_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150225)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the sub-Sample Clock delay, in seconds, to apply to the I/Q waveform. Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Units:** Seconds

    **Valid Values:** Plus or minus half of one Sample Clock period

    **Supported Devices:** PXIe-5820/5840/5841/5842

    Note: - The resolution of this property is a method of the I/Q sample period at 15E(-6) times that sample period.

     - If this property is set, NI-TClk cannot perform any sub-Sample Clock adjustment.
    '''
    ae_temperature = _attributes.AttributeViReal64(1150182)
    '''Type: float

    Returns the amplitude extender module temperature in degrees Celsius.

    **Units**: degrees Celsius (°C)

    **Supported Devices:** PXIe-5654 with PXIe-5696
    '''
    alc_control = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutomaticLevelControl, 1150195)
    '''Type: enums.AutomaticLevelControl

    Enables or disables the automatic leveling control (ALC).

    PXIe-5654 with PXIe-5696: If this property is enabled, the ALC is closed (closed-loop mode) and allows for better amplitude accuracy and wider amplitude dynamic range. If this property is disabled, the ALC is open (open-loop mode), which is ideal when using modulation. Disabling the alc_control property also allows for NI-RFSG to perform an automatic power search.

    PXIe-5654: AutomaticLevelControl.DISABLE is the only supported value for this device. The PXIe-5654 does not support the ALC when used as a stand-alone device.

    **Default Value:**

    PXIe-5654: AutomaticLevelControl.DISABLE

    PXIe-5654 with PXIe-5696: AutomaticLevelControl.ENABLE

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Power Level Adjustment <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_level_adjustment.html>`_

    `ALC Closed Loop Versus Open Loop <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_alc_closed_loop_vs_open_loop.html>`_

    `Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_

    **Defined Values**:

    +-------------------------------+---------+------------------+
    | Name                          | Value   | Description      |
    +===============================+=========+==================+
    | AutomaticLevelControl.DISABLE | 0 (0x0) | Disables ALC.    |
    +-------------------------------+---------+------------------+
    | AutomaticLevelControl.ENABLE  | 1 (0x1) | Enables the ALC. |
    +-------------------------------+---------+------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    allow_out_of_specification_user_settings = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AllowOutOfSpecificationUserSettings, 1150014)
    '''Type: enums.AllowOutOfSpecificationUserSettings

    Enables or disables warnings or errors when you set the frequency, power, and bandwidth values beyond the limits of the NI-RFSG device specifications. When you enable the allow_out_of_specification_user_settings property, the driver does not report out-of-specification warnings or errors.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** AllowOutOfSpecificationUserSettings.DISABLE

    **Supported Devices:** PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +---------------------------------------------+---------+----------------------------------------------+
    | Name                                        | Value   | Description                                  |
    +=============================================+=========+==============================================+
    | AllowOutOfSpecificationUserSettings.DISABLE | 0 (0x0) | Disables out-of-specification user settings. |
    +---------------------------------------------+---------+----------------------------------------------+
    | AllowOutOfSpecificationUserSettings.ENABLE  | 1 (0x1) | Enables out-of-specification user settings.  |
    +---------------------------------------------+---------+----------------------------------------------+

    Note: Accuracy cannot be guaranteed outside of device specifications, and results may vary by module.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    amplitude_settling = _attributes.AttributeViReal64(1150137)
    '''Type: float

    Configures the amplitude settling accuracy in decibels. NI-RFSG waits until the RF power settles within the specified accuracy level after calling the _initiate method or wait_until_settled method or prior to advancing to next step if using RF list mode.

    Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.

    PXI/PXIe-5650/5651/5652: This property is for NI internal use only.

    **Units**: dB

    **Default Value:**

    PXIe-5654: 4

    PXIe-5654 with PXIe-5696 (ALC disabled): 4

    PXIe-5654 with PXIe-5696 (ALC enabled): 0.2

    PXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.5

    **Valid Values:**

    PXIe-5654: 1.5, 2, 4

    PXIe-5654 with PXIe-5696 (ALC disabled): 1.5, 2, 4

    PXIe-5654 with PXIe-5696 (ALC enabled): 0.2, 0.5

    PXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.01 to 1

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Amplitude Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_amplitude_settling_times.html>`_
    '''
    amp_path = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AmpPath, 1150185)
    '''Type: enums.AmpPath

    Specifies the amplification path to use. The low harmonic path provides greater second and third harmonic spurious response, and the high power path provides higher output power.

    NI-RFSG automatically sets the value of this property based on power and frequency settings. Setting this property overrides the value chosen by NI-RFSG.

    **Default Value:** AmpPath.LOW_HARMONIC

    **Supported Devices:** PXIe-5654 with PXIe-5696

    **Related Topics**

    `Low Harmonic Path Versus High Power Path <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/low_harmonic_path_vs_high_power_path.html>`_

    **Defined Values**:

    +----------------------+----------------+-----------------------------------------------------------+
    | Name                 | Value          | Description                                               |
    +======================+================+===========================================================+
    | AmpPath.HIGH_POWER   | 16000 (0x3e80) | Sets the amplification path to use the high power path.   |
    +----------------------+----------------+-----------------------------------------------------------+
    | AmpPath.LOW_HARMONIC | 16001 (0x3e81) | Sets the amplification path to use the low harmonic path. |
    +----------------------+----------------+-----------------------------------------------------------+

    Note: Resetting this property reverts back to the default unset behavior.
    '''
    analog_modulation_am_sensitivity = _attributes.AttributeViReal64(1150167)
    '''Type: float

    Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.

    When using the PXIe-5654 with PXIe-5696, NI-RFSG may coerce AM sensitivity. Coercing the AM sensitivity prevents overpower conditions at the PXIe-5696 input. Read this property to determine the coerced value.

    **Default Value:** 100

    **Valid Values:** 0 to 100

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Amplitude Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_amplitude_modulation.html>`_
    '''
    analog_modulation_fm_band = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AnalogModulationFmBand, 1150191)
    '''Type: enums.AnalogModulationFmBand

    Specifies the analog modulation frequency modulation (FM) band to use. Wideband FM allows for modulating signals higher than 100kHz. Narrowband FM allows for modulating lower frequency signals.

    **Default Value:** AnalogModulationFmBand.WIDEBAND

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_

    **Defined Values**:

    +-----------------------------------+----------------+--------------------------------------------+
    | Name                              | Value          | Description                                |
    +===================================+================+============================================+
    | AnalogModulationFmBand.NARROWBAND | 17000 (0x4268) | Specifies narrowband frequency modulation. |
    +-----------------------------------+----------------+--------------------------------------------+
    | AnalogModulationFmBand.WIDEBAND   | 17001 (0x4269) | Specifies wideband frequency modulation.   |
    +-----------------------------------+----------------+--------------------------------------------+
    '''
    analog_modulation_fm_deviation = _attributes.AttributeViReal64(1150035)
    '''Type: float

    Specifies the frequency deviation to use in frequency modulation.

    **Units**: hertz (Hz)

    **Default Value:** 1kHz

    **Supported Devices:** PXI/PXIe-5650/5651/5652

    **Related Topics**

    `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_
    '''
    analog_modulation_fm_narrowband_integrator = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AnalogModulationFmNarrowbandIntegrator, 1150165)
    '''Type: enums.AnalogModulationFmNarrowbandIntegrator

    Specifies the narrowband frequency modulation (FM) range to apply by sending the signal through an integrator.

    This property is valid only when you set the analog_modulation_type property to AnalogModulationType.FM and the analog_modulation_fm_band property to AnalogModulationFmBand.NARROWBAND.

    **Default Value:** AnalogModulationFmNarrowbandIntegrator.RANGE_100_HERTZ_TO_1_KILOHERTZ

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_

    **Defined Values**:

    +----------------------------------------------------------------------------+----------------+---------------------------------------------+
    | Name                                                                       | Value          | Description                                 |
    +============================================================================+================+=============================================+
    | AnalogModulationFmNarrowbandIntegrator.RANGE_100_HERTZ_TO_1_KILOHERTZ      | 18000 (0x4650) | Specifies a range from 100Â Hz to 1Â kHz.   |
    +----------------------------------------------------------------------------+----------------+---------------------------------------------+
    | AnalogModulationFmNarrowbandIntegrator.RANGE_10_KILOHERTZ_TO_100_KILOHERTZ | 18002 (0x4652) | Specifies a range from 10Â kHz to 100Â kHz. |
    +----------------------------------------------------------------------------+----------------+---------------------------------------------+
    | AnalogModulationFmNarrowbandIntegrator.RANGE_1_KILOHERTZ_TO_10_KILOHERTZ   | 18001 (0x4651) | Specifies a range from 1Â kHz to 10Â kHz.   |
    +----------------------------------------------------------------------------+----------------+---------------------------------------------+
    '''
    analog_modulation_fm_sensitivity = _attributes.AttributeViReal64(1150166)
    '''Type: float

    Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.

    **Default Value:** 100

    **Valid Values:** 0 to 100

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_
    '''
    analog_modulation_pm_deviation = _attributes.AttributeViReal64(1150062)
    '''Type: float

    Specifies the `deviation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/glossary.html>`_ to use in phase modulation, in degrees.

    **Units**: degrees (°)

    **Default Value:** 90°

    **Supported Devices:** PXI/PXIe-5650/5651/5652, PXIe-5653

    **Related Topics**

    `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_
    '''
    analog_modulation_pm_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AnalogModulationPmMode, 1150192)
    '''Type: enums.AnalogModulationPmMode

    Specifies the phase modulation (PM) mode to use.

    **Default Value:** AnalogModulationPmMode.LOW_PHASE_NOISE

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Phase Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_phase_modulation.html>`_

    **Defined Values**:

    +----------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
    | Name                                   | Value          | Description                                                                                   |
    +========================================+================+===============================================================================================+
    | AnalogModulationPmMode.HIGH_DEVIATION  | 19000 (0x4a38) | Specifies high deviation. High deviation comes at the expense of a higher phase noise.        |
    +----------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
    | AnalogModulationPmMode.LOW_PHASE_NOISE | 19001 (0x4a39) | Specifies low phase noise. Low phase noise comes at the expense of a lower maximum deviation. |
    +----------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
    '''
    analog_modulation_pm_sensitivity = _attributes.AttributeViReal64(1150168)
    '''Type: float

    Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.

    **Default Value:** 100

    **Valid Values:** 0 to 100

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Phase Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_phase_modulation.html>`_
    '''
    analog_modulation_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AnalogModulationType, 1150032)
    '''Type: enums.AnalogModulationType

    Specifies the analog modulation format to use.

    **Default Value:** AnalogModulationType.NONE

    **Supported Devices:** PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation.html>`_

    `PXI/PXIe-5650/5651/5652 Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

    `PXIe-5654/5654 with PXIe-5696 Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_modulation_modes.html>`_

    **Defined Values**:

    +---------------------------+--------------+--------------------------------------------------+
    | Name                      | Value        | Description                                      |
    +===========================+==============+==================================================+
    | AnalogModulationType.AM   | 2002 (0x7d2) | Specifies that the analog modulation type is AM. |
    +---------------------------+--------------+--------------------------------------------------+
    | AnalogModulationType.FM   | 2000 (0x7d0) | Specifies that the analog modulation type is FM. |
    +---------------------------+--------------+--------------------------------------------------+
    | AnalogModulationType.NONE | 0 (0x0)      | Disables analog modulation.                      |
    +---------------------------+--------------+--------------------------------------------------+
    | AnalogModulationType.PM   | 2001 (0x7d1) | Specifies that the analog modulation type is PM. |
    +---------------------------+--------------+--------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    analog_modulation_waveform_frequency = _attributes.AttributeViReal64(1150034)
    '''Type: float

    Specifies the frequency of the waveform to use as the message signal in analog modulation.

    **Units:** hertz (Hz)

    **Default Value:** 1kHz

    **Supported Devices:** PXI/PXIe-5650/5651/5652

    **Related Topics**

    `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_
    '''
    analog_modulation_waveform_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AnalogModulationWaveformType, 1150033)
    '''Type: enums.AnalogModulationWaveformType

    Specifies the type of waveform to use as the message signal for analog modulation.

    **Default Value:** AnalogModulationWaveformType.SINE

    **Supported Devices:** PXI/PXIe-5650/5651/5652

    **Related Topics**

    `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

    **Defined Values**:

    +---------------------------------------+--------------+-----------------------------------------------------------------+
    | Name                                  | Value        | Description                                                     |
    +=======================================+==============+=================================================================+
    | AnalogModulationWaveformType.SINE     | 3000 (0xbb8) | Specifies that the analog modulation waveform type is sine.     |
    +---------------------------------------+--------------+-----------------------------------------------------------------+
    | AnalogModulationWaveformType.SQUARE   | 3001 (0xbb9) | Specifies that the analog modulation waveform type is square.   |
    +---------------------------------------+--------------+-----------------------------------------------------------------+
    | AnalogModulationWaveformType.TRIANGLE | 3002 (0xbba) | Specifies that the analog modulation waveform type is triangle. |
    +---------------------------------------+--------------+-----------------------------------------------------------------+
    '''
    arb_carrier_frequency = _attributes.AttributeViReal64(1150015)
    '''Type: float

    **Units**: hertz (Hz)

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate a carrier frequency with a waveform.
    Indicates the carrier frequency generated by the arbitrary waveform generator (AWG) module. The specified carrier frequency is related to the RF output as shown in the following equations:

    +-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Device                                                                        | Equations                                                                                                                                                                                                                                                                                                     |
    +===============================================================================+===============================================================================================================================================================================================================================================================================================================+
    | PXI-5610, PXI-5670/5671, PXIe-5672                                            | RF Frequency (MHz) = *Upconverter Center Frequency* + *Arb Carrier Frequency* – 25 MHz                                                                                                                                                                                                                        |
    +-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860 | RF Frequency (MHz) = *Upconverter Center Frequency* + *Arb Carrier Frequency*.Note that - the upconverter_center_frequency property and the arb_carrier_frequency property cannot be set at the same time. The only time the carrier frequency is nonzero on these devices is when in-band retuning is used.  |
    +-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: - Use this property to associate a carrier frequency with a waveform.

     - This property is read-only on the PXI-5670/5671 and PXIe-5672.
    '''
    arb_digital_gain = _attributes.AttributeViReal64(1150204)
    '''Type: float

    Specifies the digital gain, in decibels. The digital gain is applied to the waveform data after filtering. Use this property to adjust the output power of the device while keeping the analog path fixed. This may cause clipping, overflows, or quantization noise if used improperly.

    To set this property, the NI-RFSG device must be in the Configuration or Generation state.

    **Default Value:** 0 dB

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    arb_filter_raised_cosine_alpha = _attributes.AttributeViReal64(1150060)
    '''Type: float

    Specifies the alpha value to use when calculating the pulse-shaping filter coefficients. You can use this property only when the arb_filter_type property is set to FilterType.ARB_FILTER_TYPE_RAISED_COSINE and with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this property with a device that does not support OSP.

    **Supported Devices:** PXI-5671, PXIe-5672/5673/5673E
    '''
    arb_filter_root_raised_cosine_alpha = _attributes.AttributeViReal64(1150057)
    '''Type: float

    Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients. You can use this property only when the arb_filter_type property is set to FilterType.ARB_FILTER_TYPE_ROOT_RAISED_COSINE and with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this property with a device that does not support OSP.

    **Supported Devices:** PXI-5671, PXIe-5672/5673/5673E
    '''
    arb_filter_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.FilterType, 1150056)
    '''Type: enums.FilterType

    Specifies the pulse-shaping filter type for the FIR filter. You can use this property only with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this property with a device that does not support OSP.

    **Default Value:** FilterType.NONE

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

    **Defined Values**:

    +-----------------------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------+
    | Name                                          | Value          | Description                                                                                                                           |
    +===============================================+================+=======================================================================================================================================+
    | FilterType.NONE                               | 0 (0x0)        | Disables analog modulation.                                                                                                           |
    +-----------------------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------+
    | FilterType.ARB_FILTER_TYPE_RAISED_COSINE      | 10002 (0x2712) | Applies a raised cosine filter to the data with the alpha value specified with the arb_filter_raised_cosine_alpha property.           |
    +-----------------------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------+
    | FilterType.ARB_FILTER_TYPE_ROOT_RAISED_COSINE | 10001 (0x2711) | Applies a root-raised cosine filter to the data with the alpha value specified with the arb_filter_root_raised_cosine_alpha property. |
    +-----------------------------------------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    arb_max_number_waveforms = _attributes.AttributeViInt32(1250454)
    '''Type: int

    Returns the maximum number of waveforms the device can hold in memory.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - query_arb_waveform_capabilities
    '''
    arb_onboard_sample_clock_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ArbOnboardSampleClockMode, 1150029)
    '''Type: enums.ArbOnboardSampleClockMode

    Specifies the Sample Clock mode on the device. To set this property, the device must be in the Configuration state.

    PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: ArbOnboardSampleClockMode.DIVIDE_DOWN is the only supported value for this device.

    **Default Values:**

    PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: ArbOnboardSampleClockMode.DIVIDE_DOWN

    PXIe-5673/5673E: ArbOnboardSampleClockMode.HIGH_RESOLUTION

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Clocking Modes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/clocking.html>`_

    **Valid Values**:

    +-------------------------------------------+--------------------------------------------------------------+
    | Name                                      | Description                                                  |
    +===========================================+==============================================================+
    | ArbOnboardSampleClockMode.HIGH_RESOLUTION | Sample rates are generated by a high-resolution clock.       |
    +-------------------------------------------+--------------------------------------------------------------+
    | ArbOnboardSampleClockMode.DIVIDE_DOWN     | Sample rates are generated by dividing the source frequency. |
    +-------------------------------------------+--------------------------------------------------------------+

    Note: Using the high resolution clock may result in increased phase noise.
    '''
    arb_oscillator_phase_dac_value = _attributes.AttributeViInt32(1150089)
    '''Type: int

    Specifies the oscillator phase digital-to-analog converter (DAC) value on the arbitrary waveform generator (AWG). Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing a previous measurement's phase DAC value to the current session. This property is applicable only when using the arb_sample_clock_source property set to ClkIn.

    **Supported Devices:** PXIe-5673/5673E

    **Related Topics**

    `NI-TClk Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_tclk_help.html>`_
    '''
    arb_power = _attributes.AttributeViReal64(1150016)
    '''Type: float

    Indicates the average output power from the PXI-5421, PXI-5441, PXIe-5442, and PXIe-5450 AWG module. If an arbitrary waveform is being generated, this property specifies either the average power or the peak power of the signal, depending on the power_level_type property setting.

    **Units**: dBm

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E
    '''
    arb_pre_filter_gain = _attributes.AttributeViReal64(1150025)
    '''Type: float

    Specifies the AWG prefilter gain. The prefilter gain is applied to the waveform data before any other signal processing. Reduce this value to prevent overflow in the AWG interpolation filters. Other gains on the NI-RFSG device are automatically adjusted to compensate for nonunity AWG prefilter gain. The PXI-5671, PXIe-5672 must be in the Configuration state to use this property. However, the PXIe-5644/5645/5646, PXIe-5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842 can be in either the Configuration or the Generation state to use this property. PXIe-5860 can only be in the Configuration state to use this property.

    On the PXI-5671, this property applies only when the iq_rate property is set to a value less than or equal to 8.33MS/s. On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, this property is always applicable.

    **Units**: dB

    **Default Value:** 0dB

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    arb_sample_clock_rate = _attributes.AttributeViReal64(1150031)
    '''Type: float

    Returns the rate of the Sample Clock on the device.

    **Units**: hertz (Hz)

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    arb_sample_clock_source = _attributes.AttributeViString(1150030)
    '''Type: str

    Specifies the Sample Clock source for the device. To set this property, the NI-RFSG device must be in the Configuration state.

    PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: OnboardClock is the only supported value for this device.

    **Default Value:** OnboardClock

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

    **Possible Values**:

    +----------------+---------------------------------------------------------------+
    | Possible Value | Description                                                   |
    +================+===============================================================+
    | "ClkIn"        | Uses the external clock as the Sample Clock source.           |
    +----------------+---------------------------------------------------------------+
    | "OnboardClock" | Uses the AWG module onboard clock as the Sample Clock source. |
    +----------------+---------------------------------------------------------------+
    '''
    arb_selected_waveform = _attributes.AttributeViString(1250451)
    '''Type: str

    Specifies the waveform in onboard memory to generate upon calling the Init method when the generation_mode property is set to GenerationMode.ARB_WAVEFORM. The arb_selected_waveform property is ignored when the generation_mode property is set to GenerationMode.SCRIPT or GenerationMode.CW. To set the arb_selected_waveform property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

    **High-Level Methods**:

    - select_arb_waveform
    '''
    arb_temperature = _attributes.AttributeViReal64(1150068)
    '''Type: float

    Returns the AWG module temperature in degrees Celsius.

    PXIe-5820/5840/5841/5842: If you query this property during RF list mode, list steps may take longer to complete during list execution.

    **Units**: degrees Celsius (°C)

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860
    '''
    arb_waveform_quantum = _attributes.AttributeViInt32(1250455)
    '''Type: int

    Returns the waveform quantum for the device. The number of samples in a waveform must be an integer multiple of the waveform quantum. The other restrictions on the length of the waveform are the arb_waveform_size_min and arb_waveform_size_max arbitrary waveform sizes.

    PXI-5671, PXIe-5672: The value of this property depends on the I/Q rate. Set the iq_rate property before reading this property.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - query_arb_waveform_capabilities
    '''
    arb_waveform_repeat_count = _attributes.AttributeViInt32(1150158)
    '''Type: int

    Specifies the repeat count of a waveform when you set the arb_waveform_repeat_count_is_finite property to True. This property is valid only when you set the generation_mode property to GenerationMode.ARB_WAVEFORM. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** 1

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    arb_waveform_repeat_count_is_finite = _attributes.AttributeViBoolean(1150157)
    '''Type: bool

    Specifies the repetition mode of a waveform when you set the generation_mode property to GenerationMode.ARB_WAVEFORM. If you set this property to True, the number of repetitions is determined by the arb_waveform_repeat_count property. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +-------+-------------------------------------------------------------------+
    | Value | Description                                                       |
    +=======+===================================================================+
    | True  | Repeats the waveform a finite number of times.                    |
    +-------+-------------------------------------------------------------------+
    | False | Repeats the waveform continuously until you abort the generation. |
    +-------+-------------------------------------------------------------------+
    '''
    arb_waveform_size_max = _attributes.AttributeViInt32(1250457)
    '''Type: int

    Returns the size of the largest waveform that is allowed.

    To read this property, the NI-RFSG device must be in the Configuration state.

    For the PXI-5671 and PXIe-5672, the value of this property depends on the I/Q rate. Set the iq_rate before reading this property. For the PXIe-5673/5673E, the maximum waveform size is reduced to account for the amount of device memory currently used.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - query_arb_waveform_capabilities

    Note: Not all onboard memory is available for waveform storage. A portion of onboard memory stores scripts that specify how the waveforms are generated. These scripts typically require less than 1KB of onboard memory.
    '''
    arb_waveform_size_min = _attributes.AttributeViInt32(1250456)
    '''Type: int

    Returns the smallest allowable waveform size. For the PXI-5671 and PXIe-5672, the value of this property depends on the I/Q rate. Set the iq_rate property before reading this property.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - query_arb_waveform_capabilities
    '''
    arb_waveform_software_scaling_factor = _attributes.AttributeViReal64(1150052)
    '''Type: float

    Specifies how much to scale the data before writing it with the WriteArbWaveform method. The resulting waveform must be smaller than 1.0 in complex magnitude. This property is supported only if you set the power_level_type property to PowerLevelType.PEAK.

    **Default Value:** 1.0

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_
    '''
    attenuator_hold_enabled = _attributes.AttributeViBoolean(1150009)
    '''Type: bool

    Specifies whether attenuator hold is enabled. While this property is set to True, changing the power level causes NI-RFSG to scale the digital data sent to the AWG instead of adjusting the attenuators. Changing power levels in this manner allows the device to increase or decrease the power level in more accurate increments, but it may affect signal-to-noise ratios (noise density).

    Setting the attenuator_hold_enabled property to True limits the power levels that can be attained. With attenuator hold enabled, the power level must satisfy the following conditions:

    - Power level less than or equal to attenuator_hold_max_power
    - Power level greater than or equal to (maximum power level -70dB)
    - Power level greater than or equal to -145dBm

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

    **Related Topics**

    `Attenuator Hold <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/attenuator_hold_mode.html>`_

    `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_

    **Defined Values**:

    +-------+---------------------------+
    | Value | Description               |
    +=======+===========================+
    | True  | Enables attenuator hold.  |
    +-------+---------------------------+
    | False | Disables attenuator hold. |
    +-------+---------------------------+

    Note: The frequency cannot be changed on the PXI-5670/5671 or PXIe-5672 while this property is set to True.
    '''
    attenuator_hold_max_power = _attributes.AttributeViReal64(1150010)
    '''Type: float

    Specifies the maximum power level of the RF output signal when the attenuator_hold_enabled property is set to True.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Units**: dBm

    **Defined Values**:
    Refer to the specifications document for your device for allowable maximum power levels.

    **Default Value:**

    PXI-5670/5671, PXIe-5672: 17

    PXIe-5673/5673E: 10

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

    **Related Topics**

    `Attenuator Hold <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/attenuator_hold_mode.html>`_

    `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_
    '''
    attenuator_setting = _attributes.AttributeViReal64(1150173)
    '''Type: float

    Specifies the level of attenuation in the attenuator path. Setting this property overrides the value chosen by NI-RFSG. Not all power levels are achievable if you set this property.

    **Units**: dB

    **Valid Values**: 0dB to 110dB in steps of 10

    **Supported Devices:** PXIe-5654 with PXIe-5696

    Note: Resetting this property reverts back to the default unset behavior.
    '''
    automatic_thermal_correction = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutomaticThermalCorrection, 1150008)
    '''Type: enums.AutomaticThermalCorrection

    Enables or disables automatic thermal correction. When this property is enabled, changes to settings cause NI-RFSG to check whether the device temperature has changed and adjusts the settings as needed. When this property is disabled, you must explicitly call the perform_thermal_correction method to adjust the device for temperature changes.

    **Default Value:** AutomaticThermalCorrection.ENABLE

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Temperature Monitoring <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5611_temperature_monitoring.html>`_

    `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_

    **Defined Values**:

    +------------------------------------+---------+-------------------------------------------+
    | Name                               | Value   | Description                               |
    +====================================+=========+===========================================+
    | AutomaticThermalCorrection.DISABLE | 0 (0x0) | Automatic thermal correction is disabled. |
    +------------------------------------+---------+-------------------------------------------+
    | AutomaticThermalCorrection.ENABLE  | 1 (0x1) | Automatic thermal correction is enabled.  |
    +------------------------------------+---------+-------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    auto_power_search = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AutomaticPowerSearch, 1150196)
    '''Type: enums.AutomaticPowerSearch

    Enables or disables automatic power search. When this property is enabled, a power search performs after the device is initiated, after output power is enabled, or when the frequency or power level changes while the device is generating. When this property is disabled, NI-RFSG does not perform a power search unless you call the perform_power_search method.

    This property is ignored when the alc_control property is enabled.

    PXIe-5654: AutomaticPowerSearch.DISABLE is the only supported value for this device.

    **Default Value:**

    PXIe-5654: AutomaticPowerSearch.DISABLE

    PXIe-5654 with PXIe-5696: AutomaticPowerSearch.ENABLE

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_

    **Defined Values**:

    +------------------------------+---------+----------------------------------+
    | Name                         | Value   | Description                      |
    +==============================+=========+==================================+
    | AutomaticPowerSearch.DISABLE | 0 (0x0) | Disables automatic power search. |
    +------------------------------+---------+----------------------------------+
    | AutomaticPowerSearch.ENABLE  | 1 (0x1) | Enables automatic power search.  |
    +------------------------------+---------+----------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    available_paths = _attributes.AttributeViString(1150312)
    '''Type: str

    Returns a comma separated list of the configurable paths available for use based on your instrument configuration.
    '''
    available_ports = _attributes.AttributeViString(1150249)
    '''Type: str

    Returns a comma-separated list of the ports available for use based on your instrument configuration.

    **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    cache = _attributes.AttributeViBoolean(1050004)
    '''Type: bool

    Specifies whether to cache the value of properties. When caching is enabled, NI-RFSG tracks the current NI-RFSG device settings and avoids sending redundant commands to the device. NI-RFSG can always cache or never cache particular properties, regardless of the setting of this property. Call the __init__ method to override the default value.

    **Default Value:** True

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +-------+-------------------+
    | Value | Description       |
    +=======+===================+
    | True  | Enables caching.  |
    +-------+-------------------+
    | False | Disables caching. |
    +-------+-------------------+
    '''
    compensate_for_filter_group_delay = _attributes.AttributeViBoolean(1152832)
    '''Type: bool

    Enables or disables compensation for filter group delay on the AWG module. This property also accounts for the upconverter group delay and aligns the RF output with the Started Event, Done Event, and Marker Events.

    At a low I/Q rate, the group delay can become so large that some devices may not be able to align the events with the RF output, in which case you must increase the I/Q rate or disable this property.

    **Default Value:** False

    **Supported Devices:** PXIe-5672

    **Defined Values**:

    +-------+-----------------------------------------------+
    | Value | Description                                   |
    +=======+===============================================+
    | True  | Enables compensation for filter group delay.  |
    +-------+-----------------------------------------------+
    | False | Disables compensation for filter group delay. |
    +-------+-----------------------------------------------+
    '''
    configuration_settled_event_terminal_name = _attributes.AttributeViString(1150194)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Default Values**:

    PXIe-5654/5654 with PXIe-5696: /*ModuleName*/ConfigurationSettledEvent, where *ModuleName* is the name of your device in MAX.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/ConfigurationSettledEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.

    PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/ConfigurationSettledEvent, where *ModuleName* is the name of your device in MAX.

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_
    '''
    correction_temperature = _attributes.AttributeViReal64(1150104)
    '''Type: float

    Specifies the temperature, in degrees Celsius, to use for adjusting the device settings to correct for temperature changes. If you set this property, NI-RFSG uses the value you specify and therefore no longer uses the actual device temperature as the correction temperature. If you do not set this property, NI-RFSG checks the current device temperature in the Committed state and automatically sets the value of this property.

    PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This property is read only.

    **Units**: Degrees Celsius

    **Supported Devices**: PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: - Resetting this property reverts back to the default unset behavior.

     - Use this property only when your application requires the same settings to be used every time, regardless of the temperature variation. In these cases, it is best to ensure that the temperature does not vary too much.
    '''
    data_transfer_block_size = _attributes.AttributeViInt32(1150048)
    '''Type: int

    Indicates the number of samples to transfer at one time from the device to host memory. This property is useful when the total data to be transferred to onboard memory is large.

    **Units**: samples (s)

    **Default Value**: 1Ms

    **Supported Devices:** PXIe-5672/5673/5673E
    '''
    data_transfer_maximum_bandwidth = _attributes.AttributeViReal64(1150086)
    '''Type: float

    Specifies the maximum amount of bus bandwidth to use for data transfers.

    **Units**: bytes per second

    **Default Value**: Device maximum

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

    **Related Topics**

    `Improving Streaming Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/improving_streaming_performance.html>`_
    '''
    data_transfer_maximum_in_flight_reads = _attributes.AttributeViInt32(1150088)
    '''Type: int

    Specifies the maximum number of concurrent PCI Express read requests the RF signal generator can issue.

    When transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this property is set to the highest value the RF signal generator supports.

    If other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the RF signal generator issues. This helps to reduce the amount of data the signal generator reads at one time.

    **Units**: number of packets

    **Default Value**: Device maximum

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

    **Related Topics**

    `Improving Streaming Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/improving_streaming_performance.html>`_
    '''
    data_transfer_preferred_packet_size = _attributes.AttributeViInt32(1150087)
    '''Type: int

    Specifies the preferred size of the data field in a PCI Express read request packet.

    In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI RF signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.

    Recommended values for this property are powers of two between 64 and 512.

    **Units**: bytes

    **Default Value**: Device maximum

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

    **Related Topics**

    `Improving Streaming Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/improving_streaming_performance.html>`_

    Note: In some cases, the RF signal generator generates packets smaller than the preferred size you set with this property.
    '''
    deembedding_compensation_gain = _attributes.AttributeViReal64(1150289)
    '''Type: float

    Returns the de-embedding gain applied to compensate for the mismatch on the specified port. If de-embedding is enabled, NI-RFSG uses the returned compensation gain to remove the effects of the external network between the instrument and the DUT.

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

    Tip:
    This property can be set/get on specific ports within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container ports to specify a subset.

    Example: :py:attr:`my_session.ports[ ... ].deembedding_compensation_gain`

    To set/get on all ports, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.deembedding_compensation_gain`
    '''
    deembedding_selected_table = _attributes.AttributeViString(1150253)
    '''Type: str

    Selects the de-embedding table to apply to the measurements on the specified port.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_string method to specify the name of the port to configure for de-embedding.

    If de-embedding is enabled, NI-RFSG uses the specified table to remove the effects of the external network between the instrument and the DUT.

    Use the create deembedding sparameter table array method to create tables.

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

    Tip:
    This property can be set/get on specific ports within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container ports to specify a subset.

    Example: :py:attr:`my_session.ports[ ... ].deembedding_selected_table`

    To set/get on all ports, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.deembedding_selected_table`
    '''
    deembedding_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DeembeddingType, 1150252)
    '''Type: enums.DeembeddingType

    Specifies the type of de-embedding to apply to measurements on the specified port.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_int32 method to specify the name of the port to configure for de-embedding.

    If you set this property to DeembeddingType.SCALAR or DeembeddingType.VECTOR, NI-RFSG adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT.

    **Default Value**: DeembeddingType.SCALAR

    **Valid Values for PXIe-5830/5832/5840/5841/5842/5860** : DeembeddingType.SCALAR or DeembeddingType.NONE

    **Valid Values for PXIe-5831** DeembeddingType.SCALAR, DeembeddingType.VECTOR, or DeembeddingType.NONE. DeembeddingType.VECTOR is only supported for TRX Ports in a Semiconductor Test System (STS).

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +------------------------+----------------+------------------------------------------------------------------------+
    | Name                   | Value          | Description                                                            |
    +========================+================+========================================================================+
    | DeembeddingType.NONE   | 25000 (0x61a8) | De-embedding is not applied to the measurement.                        |
    +------------------------+----------------+------------------------------------------------------------------------+
    | DeembeddingType.SCALAR | 25001 (0x61a9) | De-embeds the measurement using only the gain term.                    |
    +------------------------+----------------+------------------------------------------------------------------------+
    | DeembeddingType.VECTOR | 25002 (0x61aa) | De-embeds the measurement using the gain term and the reflection term. |
    +------------------------+----------------+------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific ports within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container ports to specify a subset.

    Example: :py:attr:`my_session.ports[ ... ].deembedding_type`

    To set/get on all ports, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.deembedding_type`
    '''
    device_instantaneous_bandwidth = _attributes.AttributeViReal64(1150226)
    '''Type: float

    Specifies the bandwidth of the device. The instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration.

    The signal_bandwidth centered at the frequency must fit within the device instantaneous bandwidth, which is centered at the upconverter_center_frequency.

    **Units**: Hz

    **Default Value**: N/A

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_
    '''
    device_temperature = _attributes.AttributeViReal64(1150017)
    '''Type: float

    Returns the device temperature. If the NI-RFSG session is controlling multiple devices, this property returns the temperature of the primary NI RF device. The NI-RFSG session is opened using the primary RF device name.

    Serial signals between the sensor and the system control unit could modulate the signal being generated, thus causing phase spurs. After the device thoroughly warms up, its temperature varies only slightly (less than 1 degree Celsius) and slowly, and it is not necessary to constantly poll this temperature sensor.

    PXIe-5644/5645/5646, PXIe-5820/5840/5841: If you query this property during RF list mode, list steps may take longer to complete during list execution.

    PXIe-5830/5831/5832: To use this property, you must first set the channelName parameter of the _set_attribute_vi_real64 method to using the appropriate string for your instrument configuration. Setting the _set_attribute_vi_real64 method is not required for the PXIe-3621/3622. Refer to the following table to determine which strings are valid for your configuration.

    **Units**: degrees Celsius (°C)

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Temperature Monitoring <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5611_temperature_monitoring.html>`_

    `Thermal Shutdown <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_shutdown_monitoring_5650_5651_5652.html>`_

    +----------------------------+--------------------------+-------------------------+
    | Hardware Module            | TRX Port Type            | Active Channel String   |
    +============================+==========================+=========================+
    | PXIe-3621/3622             | —                        | if or "" (empty string) |
    +----------------------------+--------------------------+-------------------------+
    | PXIe-5820                  | —                        | fpga                    |
    +----------------------------+--------------------------+-------------------------+
    | First connected mmRH-5582  | DIRECT TRX PORTS Only    | rf0                     |
    +----------------------------+--------------------------+-------------------------+
    | First connected mmRH-5582  | SWITCHED TRX PORTS [0-7] | rf0switch0              |
    +----------------------------+--------------------------+-------------------------+
    | First connected mmRH-5582  | SWITCHED TRX PORTS [0-7] | rf0switch1              |
    +----------------------------+--------------------------+-------------------------+
    | Second connected mmRH-5582 | DIRECT TRX PORTS Only    | rf1                     |
    +----------------------------+--------------------------+-------------------------+
    | Second connected mmRH-5582 | SWITCHED TRX PORTS [0-7] | rf1switch0              |
    +----------------------------+--------------------------+-------------------------+
    | Second connected mmRH-5582 | SWITCHED TRX PORTS [0-7] | rf1switch1              |
    +----------------------------+--------------------------+-------------------------+

    Tip:
    This property can be set/get on specific device_temperatures within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container device_temperatures to specify a subset.

    Example: :py:attr:`my_session.device_temperatures[ ... ].device_temperature`

    To set/get on all device_temperatures, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.device_temperature`
    '''
    digital_edge_script_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerDigitalEdgeEdge, 1150021)
    '''Type: enums.ScriptTriggerDigitalEdgeEdge

    Specifies the active edge for the Script Trigger. This property is used when the script_trigger_type property is set to digital edge. To set the digital_edge_script_trigger_edge property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** ScriptTriggerDigitalEdgeEdge.RISING

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

    **High-Level Methods**:

    - configure_digital_edge_script_trigger

    **Defined Values**:

    +--------------------------------------+---------+-------------------------------------------------------------------------------+
    | Name                                 | Value   | Description                                                                   |
    +======================================+=========+===============================================================================+
    | ScriptTriggerDigitalEdgeEdge.FALLING | 1 (0x1) | Asserts the trigger when the signal transitions from high level to low level. |
    +--------------------------------------+---------+-------------------------------------------------------------------------------+
    | ScriptTriggerDigitalEdgeEdge.RISING  | 0 (0x0) | Asserts the trigger when the signal transitions from low level to high level. |
    +--------------------------------------+---------+-------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].digital_edge_script_trigger_edge`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.digital_edge_script_trigger_edge`
    '''
    digital_edge_script_trigger_source = _attributes.AttributeViString(1150020)
    '''Type: str

    Specifies the source terminal for the Script Trigger. This property is used when the script_trigger_type property is set to digital edge. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **High-Level Methods**:

    - configure_digital_edge_script_trigger

    **Possible Values**:

    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                             |
    +================+=========================================================================================================================================+
    | "PFI0"         | The trigger is received on PFI 0.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The trigger is received on PFI 1.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI2"         | The trigger is received on PFI 2.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI3"         | The trigger is received on PFI 3.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Star"     | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                              |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig7"    | The trigger is received on PXI trigger line 7.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarB"  | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PulseIn"      | The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.                                            |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "Sync_Script"  | The trigger is received on the Sync Script trigger line. This value is valid on only the PXIe-5644/5645/5646.                           |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].digital_edge_script_trigger_source`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.digital_edge_script_trigger_source`
    '''
    digital_edge_start_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.StartTriggerDigitalEdgeEdge, 1250459)
    '''Type: enums.StartTriggerDigitalEdgeEdge

    Specifies the active edge for the Start Trigger. This property is used when the start_trigger_type property is set to digital edge. To set the digital_edge_start_trigger_edge property, the NI-RFSG device must be in the Configuration state.

    PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.

    **Default Value:** StartTriggerDigitalEdgeEdge.RISING

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

    **High-Level Methods**:

    - configure_digital_edge_start_trigger

    **Defined Values**:

    +-------------------------------------+---------+------------------------------------------------------------------+
    | Name                                | Value   | Description                                                      |
    +=====================================+=========+==================================================================+
    | StartTriggerDigitalEdgeEdge.FALLING | 1 (0x1) | Occurs when the signal transitions from high level to low level. |
    +-------------------------------------+---------+------------------------------------------------------------------+
    | StartTriggerDigitalEdgeEdge.RISING  | 0 (0x0) | Occurs when the signal transitions from low level to high level. |
    +-------------------------------------+---------+------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_edge_start_trigger_source = _attributes.AttributeViString(1150002)
    '''Type: str

    Specifies the source terminal for the Start Trigger. This property is used when the start_trigger_type property is set to digital edge. The digital_edge_start_trigger_source property is not case-sensitive. To set the digital_edge_start_trigger_source property, the NI-RFSG device must be in the Configuration state.

    PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **High-Level Methods**:

    - configure_digital_edge_start_trigger

     **Possible Values**:

    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                            |
    +================+========================================================================================================================================+
    | "PFI0"         | The trigger is received on PFI 0.                                                                                                      |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The trigger is received on PFI 1.                                                                                                      |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI2"         | The trigger is received on PFI 2.                                                                                                      |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI3"         | The trigger is received on PFI 3.                                                                                                      |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Star"     | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                             |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig7"    | The trigger is received on PXI trigger line 7.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarB"  | The trigger is received on the PXI DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "TrigIn"       | The trigger is received on the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.                    |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "Sync_Script"  | The trigger is received on the Sync Script trigger line. This value is valid on only the PXIe-5644/5645/5646.                          |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    '''
    digital_equalization_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalEqualizationEnabled, 1150012)
    '''Type: enums.DigitalEqualizationEnabled

    When this property is enabled, NI-RFSG equalizes the waveform data to correct for variations in the response of the NI-RFSG device. Enabling digital equalization improves the modulation error rates (MER) and error vector magnitude (EVM) for signals with large bandwidths (>500 kHz), but it increases tuning times.

    On the PXI-5670/5671, equalization is performed in the software, so tuning time is increased. On the PXIe-5672, equalization is performed in the hardware so that there is no compromise in performance.

    This property applies only when the generation_mode property is set to GenerationMode.ARB_WAVEFORM or GenerationMode.SCRIPT. To set this property, the NI-RFSG device must be in the Configuration state.

    PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: DigitalEqualizationEnabled.ENABLE is the only supported value for this device.

    **Default Value:**

    PXI-5670/5671: DigitalEqualizationEnabled.DISABLE

    PXIe-5644/5645/5646, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: DigitalEqualizationEnabled.ENABLE

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Response and Software Equalization <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/if_response_and_equalizer.html>`_—Refer to this topic for more information about equalization performed in software.

    `Frequency Tuning Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.html>`_

    **Defined Values**:

    +------------------------------------+---------+-----------------------+
    | Name                               | Value   | Description           |
    +====================================+=========+=======================+
    | DigitalEqualizationEnabled.DISABLE | 0 (0x0) | Filter is not applied |
    +------------------------------------+---------+-----------------------+
    | DigitalEqualizationEnabled.ENABLE  | 1 (0x1) | Filter is applied.    |
    +------------------------------------+---------+-----------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_level_script_trigger_active_level = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerDigitalLevelActiveLevel, 1150055)
    '''Type: enums.ScriptTriggerDigitalLevelActiveLevel

    Specifies the active level for the Script Trigger. This property is used when the script_trigger_type property is set to ScriptTriggerType.DIGITAL_LEVEL.

    **Default Value:** ScriptTriggerDigitalLevelActiveLevel.HIGH

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `Digital Level Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_level.html>`_

    **Defined Values**:

    +-------------------------------------------+---------------+--------------------------------------------------+
    | Name                                      | Value         | Description                                      |
    +===========================================+===============+==================================================+
    | ScriptTriggerDigitalLevelActiveLevel.HIGH | 9000 (0x2328) | Trigger when the digital trigger signal is high. |
    +-------------------------------------------+---------------+--------------------------------------------------+
    | ScriptTriggerDigitalLevelActiveLevel.LOW  | 9001 (0x2329) | Trigger when the digital trigger signal is low.  |
    +-------------------------------------------+---------------+--------------------------------------------------+

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].digital_level_script_trigger_active_level`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.digital_level_script_trigger_active_level`
    '''
    digital_level_script_trigger_source = _attributes.AttributeViString(1150054)
    '''Type: str

    Specifies the source terminal for the Script Trigger. This property is used when the script_trigger_type property is set to ScriptTriggerType.DIGITAL_LEVEL. The digital_level_script_trigger_source property is not case-sensitive.

    To set the digital_level_script_trigger_source property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                             |
    +================+=========================================================================================================================================+
    | "PFI0"         | The trigger is received on PFI 0.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The trigger is received on PFI 1.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI2"         | The trigger is received on PFI 2.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI3"         | The trigger is received on PFI 3.                                                                                                       |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Star"     | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                              |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig7"    | The trigger is received on PXI trigger line 7.                                                                                          |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarB"  | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "PulseIn"      | The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.                                            |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                                      |
    +----------------+-----------------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].digital_level_script_trigger_source`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.digital_level_script_trigger_source`
    '''
    digital_modulation_fsk_deviation = _attributes.AttributeViReal64(1150041)
    '''Type: float

    Specifies the deviation to use in FSK modulation.

    **Units**: hertz (Hz)

    **Default Value:** 1,000

    **Supported Devices:** PXI/PXIe-5650/5651/5652

    **Related Topics**

    `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_
    '''
    digital_modulation_prbs_order = _attributes.AttributeViInt32(1150039)
    '''Type: int

    Specifies the order of pseudorandom bit sequence (PRBS) internally generated by hardware and used as the message signal in digital modulation.

    **Default Value:** 16

    **Supported Devices:** PXI/PXIe-5650/5651/5652

    **Related Topics**

    `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_
    '''
    digital_modulation_prbs_seed = _attributes.AttributeViInt32(1150040)
    '''Type: int

    Specifies the seed of the internally generated pseudorandom bit sequence (PRBS).

    **Default Value:** 1

    **Supported Devices:** PXI/PXIe-5650/5651/5652

    **Related Topics**

    `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_
    '''
    digital_modulation_symbol_rate = _attributes.AttributeViReal64(1150037)
    '''Type: float

    Specifies the symbol rate of the bit stream for digital modulation.

    **Units**: hertz (Hz)

    **Default Value:** 1kHz

    **Supported Devices:** PXI/PXIe-5650/5651/5652

    **Related Topics**

    `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_
    '''
    digital_modulation_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalModulationType, 1150036)
    '''Type: enums.DigitalModulationType

    Specifies the digital modulation format to use.

    **Default Value:** DigitalModulationType.NONE

    **Supported Devices:** PXI/PXIe-5650/5651/5652

    **Related Topics**

    `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

    **Defined Values**:

    +----------------------------+--------------+-----------------------------------------------------------------------------+
    | Name                       | Value        | Description                                                                 |
    +============================+==============+=============================================================================+
    | DigitalModulationType.FSK  | 4000 (0xfa0) | Specifies that the digital modulation type is frequency-shift keying (FSK). |
    +----------------------------+--------------+-----------------------------------------------------------------------------+
    | DigitalModulationType.NONE | 0 (0x0)      | Disables digital modulation.                                                |
    +----------------------------+--------------+-----------------------------------------------------------------------------+
    | DigitalModulationType.OOK  | 4001 (0xfa1) | Specifies that the digital modulation type is on-off keying (OOK).          |
    +----------------------------+--------------+-----------------------------------------------------------------------------+
    | DigitalModulationType.PSK  | 4002 (0xfa2) | Specifies that the digital modulation type is phase-shift keying (PSK).     |
    +----------------------------+--------------+-----------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_modulation_waveform_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DigitalModulationWaveformType, 1150038)
    '''Type: enums.DigitalModulationWaveformType

    Specifies the type of waveform to use as the message signal in digital modulation.

    **Default Value:** DigitalModulationWaveformType.PRBS

    **Supported Devices:** PXI/PXIe-5650/5651/5652

    **Related Topics**

    `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

    **Defined Values**:

    +--------------------------------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Name                                       | Value         | Description                                                                                                                                                                    |
    +============================================+===============+================================================================================================================================================================================+
    | DigitalModulationWaveformType.PRBS         | 5000 (0x1388) | Specifies that the digital modulation waveform type is pseudorandom bit sequence (PRBS).                                                                                       |
    +--------------------------------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | DigitalModulationWaveformType.USER_DEFINED | 5001 (0x1389) | Specifies that the digital modulation waveform type is user defined. To specify the user-defined waveform, call the configure_digital_modulation_user_defined_waveform method. |
    +--------------------------------------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    digital_pattern = _attributes.AttributeViBoolean(1150044)
    '''Type: bool

    Enables or disables digital pattern on the PXI-5421/5441 AWG module. This property must be set to True to enable signal routing to and from the Digital Data & Control connector.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXI-5670/5671

    **Defined Values**:

    +-------+--------------------------+
    | Value | Description              |
    +=======+==========================+
    | True  | Signal routing enabled.  |
    +-------+--------------------------+
    | False | Signal routing disabled. |
    +-------+--------------------------+
    '''
    direct_download = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DirectDownload, 1150042)
    '''Type: enums.DirectDownload

    Specifies whether the WriteArbWaveform method immediately writes waveforms to the device or copies the waveform to host memory for later download. NI-RFSG reads and validates this property when an arbitrary waveform is first allocated.

    For the PXI-5670, direct download is always disabled. For all other devices, direct download is always enabled.

    PXI-5671: To increase performance when using large waveforms, enable direct download. To maximize reconfigurability, disable direct download.

    Perform the following steps to enable direct download:

    1. Set the I/Q rate to less than or equal to 8.33MS/s with the iq_rate property.

    2. Set the power_level_type property to PowerLevelType.PEAK.

    3. Disable the iq_swap_enabled property.

    4. Disable the digital_equalization_enabled property.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860

    **Defined Values**:

    +----------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Name                       | Value     | Description                                                                                                                             |
    +============================+===========+=========================================================================================================================================+
    | DirectDownload.DISABLE     | 0 (0x0)   | The RF In local oscillator signal is not present at the front panel LO OUT connector.                                                   |
    +----------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | DirectDownload.ENABLE      | 1 (0x1)   | The RF In local oscillator signal is present at the front panel LO OUT connector.                                                       |
    +----------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | DirectDownload.UNSPECIFIED | -2 (-0x2) | The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it. |
    +----------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    done_event_terminal_name = _attributes.AttributeViString(1150113)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Default Values**:

    PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/DoneEvent, where *AWGName* is the name of your associated AWG module in MAX.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/DoneEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.

    PXIe-5820/5840/5841: /*ModuleName*/ao/0/DoneEvent, where *ModuleName* is the name of your device in MAX.

    PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/DoneEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    events_delay = _attributes.AttributeViReal64TimeDeltaSeconds(1150154)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the delay, in seconds, applied to the Started Event, Done Event, and all Marker Events with respect to the analog output of the RF signal generator. To set this property, the NI-RFSG device must be in the Configuration or Generation state.

    By default, markers and events are delayed to align with the waveform data generated from the device. This property adds an additional delay to markers and events. Use this property to adjust the time delay between events and the corresponding data.

    **Units:** Seconds

    **Valid Values:**

    PXIe-5644/5645: -1.217 μs to 67.050 μs

    PXIe-5646: -0.896 μs to 64.640 μs

    PXIe-5820/5830/5831/5832/5840/5841/5842: 0 μs to 3.276 μs

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    Note: If you decrease the event delay during generation, some markers may be dropped.
    '''
    exported_configuration_settled_event_output_terminal = _attributes.AttributeViString(1150129)
    '''Type: str

    Specifies the destination terminal for exporting the Configuration Settled event. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                        |
    +================+====================================================================================================================+
    | ""             | The signal is not exported.                                                                                        |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                     |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC"  | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5840/5841/5842. |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    | "TrigOut"      | TRIG IN/OUT terminal.                                                                                              |
    +----------------+--------------------------------------------------------------------------------------------------------------------+
    '''
    exported_done_event_output_terminal = _attributes.AttributeViString(1150063)
    '''Type: str

    Specifies the destination terminal for exporting the Done event. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | Posible Value | Description                                                                                                                     |
    +===============+=================================================================================================================================+
    | ""            | The signal is not exported.                                                                                                     |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI0"        | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"        | The signal is exported to the PFI 1 connector.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI4"        | The signal is exported to the PFI 4 connector.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI5"        | The signal is exported to the PFI 5 connector.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"   | The trigger is received on PXI trigger line 0.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"   | The trigger is received on PXI trigger line 1.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"   | The trigger is received on PXI trigger line 2.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"   | The trigger is received on PXI trigger line 3.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"   | The trigger is received on PXI trigger line 4.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"   | The trigger is received on PXI trigger line 5.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"   | The trigger is received on PXI trigger line 6.                                                                                  |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC" | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.    |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"    | The trigger is received on PFI0 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"    | The trigger is received on PFI1 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"    | The trigger is received on PFI2 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"    | The trigger is received on PFI3 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"    | The trigger is received on PFI4 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"    | The trigger is received on PFI5 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"    | The trigger is received on PFI6 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"    | The trigger is received on PFI7 from the front panel DIO terminal.                                                              |
    +---------------+---------------------------------------------------------------------------------------------------------------------------------+
    '''
    exported_marker_event_output_terminal = _attributes.AttributeViString(1150064)
    '''Type: str

    Specifies the destination terminal for exporting the Marker Event. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                     |
    +================+=================================================================================================================================+
    | ""             | The signal is not exported.                                                                                                     |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI0"         | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The signal is exported to the PFI 1 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI4"         | The signal is exported to the PFI 4 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI5"         | The signal is exported to the PFI 5 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC"  | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.    |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].exported_marker_event_output_terminal`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.exported_marker_event_output_terminal`
    '''
    exported_pulse_modulation_event_active_level = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerDigitalLevelActiveLevel, 1150310)
    '''Type: enums.ScriptTriggerDigitalLevelActiveLevel

    Specifies the active level of the exported Pulse Modulation Event. When `property pulse modulation enabled` is Enabled, `pulse modulation active level` is `active high`, `exported pulse modulation event output terminal` is `PulseOut`, and this property is `active high`, then the Pulse Modulation Event will transition from Low to High after the the Pulse In signal is set to logic high, and the RF Output has settled. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** ScriptTriggerDigitalLevelActiveLevel.HIGH

    **Supported Devices:**  PXIe-5842

    **Defined Values**:

    +-------------------------------------------+---------------+--------------------------------------------------+
    | Name                                      | Value         | Description                                      |
    +===========================================+===============+==================================================+
    | ScriptTriggerDigitalLevelActiveLevel.HIGH | 9000 (0x2328) | Trigger when the digital trigger signal is high. |
    +-------------------------------------------+---------------+--------------------------------------------------+
    | ScriptTriggerDigitalLevelActiveLevel.LOW  | 9001 (0x2329) | Trigger when the digital trigger signal is low.  |
    +-------------------------------------------+---------------+--------------------------------------------------+
    '''
    exported_pulse_modulation_event_output_terminal = _attributes.AttributeViString(1150309)
    '''Type: str

    Specifies the destination terminal for exporting the Pulse Modulation Event. The Pulse Modulation Event tracks the RF Envelope when Pulse Modulation is Enabled. If this property is set to a value other than `do not export str`, calling NI-RFSG Commit will cause the output terminal to be pulled to the logic level that is the inverse of `exported pulse modulation event active level`. You can tri-state this terminal by setting this property to `do not export str` or by calling `niRFSG Reset`. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** PulseOut

    **Supported Devices:**  PXIe-5842

    **Possible Values**:

    +----------------+---------------------------------------------------------------------+
    | Possible Value | Description                                                         |
    +================+=====================================================================+
    | ""             | Pulse modulation video signal is not exported.                      |
    +----------------+---------------------------------------------------------------------+
    | "PulseOut"     | Export the pulse modulation video signal on the pulse out terminal. |
    +----------------+---------------------------------------------------------------------+
    '''
    exported_ref_clock_output_terminal = _attributes.AttributeViString(1150053)
    '''Type: str

    Specifies the destination terminal for exporting the Reference Clock on the RF signal generators. To set this property, the NI-RFSG device must be in the Configuration state.

    **Possible Values**:

    Possible Value: Description

    "" :The Reference Clock signal is not exported.

    "RefOut" :Exports the Reference Clock signal to the REF OUT connector of the device.

    "RefOut2" :Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable.

    "ClkOut" :Exports the Reference Clock signal to the CLK OUT connector of the device.

    **Default Value:** '""'

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Interconnecting Multiple NI 5673E Modules <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/interconnecting_multiple_ni_5673_modules.html>`_

    +----------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                | Supported devices                                                                                                                                                     |
    +================+============================================================================================+=======================================================================================================================================================================+
    | "ClkOut"       | Exports the Reference Clock signal to the CLK OUT connector of the device.                 | Supported on PXIe-5673, 5673E                                                                                                                                         |
    +----------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ""             | The Reference Clock signal is not exported.                                                | Supported on PXIe-5644/5645/5646, 5820/5830/5831/5832/5840/5841/5842/5860, 5650/5651/5652, 5654, 5673, 5673E, PXIe-5654 with PXIe-5696, PXI-5650/5651/5652 (See Note) |
    +----------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "RefOut"       | Exports the Reference Clock signal to the REF OUT connector of the device.                 | Supported on PXIe-5644/5645/5646, 5820/5830/5831/5832/5840/5841/5842/5860, 5650/5651/5653, 5653, 5654, 5673, 5673E, PXIe-5654 with PXIe-5696, PXI-5650/5651/5653,     |
    +----------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "RefOut2"      | Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable. | Supported on PXIe-5650/5651/5652, 5654, 5673E, PXIe-5654 with PXIe-5696                                                                                               |
    +----------------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: The RefOut2 output terminal value is valid for only the PXIe-5650/5651/5652, not the PXI-5650/5651/5652.
    '''
    exported_ref_clock_rate = _attributes.AttributeEnum(_attributes.AttributeViReal64, enums.ReferenceClockExportedRate, 1150292)
    '''Type: enums.ReferenceClockExportedRate

    Specifies the Reference Clock Rate, in Hz, of the signal sent to the Reference Clock Export Output Terminal. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** ReferenceClockExportedRate.CLOCK_RATE_10_MEGAHERTZ

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +-----------------------------------------------------+--------------+-------------------------------------+
    | Name                                                | Value        | Description                         |
    +=====================================================+==============+=====================================+
    | ReferenceClockExportedRate.CLOCK_RATE_10_MEGAHERTZ  | 10000000.0   | Uses a 10MHz Reference Clock rate.  |
    +-----------------------------------------------------+--------------+-------------------------------------+
    | ReferenceClockExportedRate.CLOCK_RATE_100_MEGAHERTZ | 100000000.0  | Uses a 100MHz Reference Clock rate. |
    +-----------------------------------------------------+--------------+-------------------------------------+
    | ReferenceClockExportedRate.CLOCK_RATE_1_GIGAHERTZ   | 1000000000.0 | Uses a 1GHz Reference Clock rate.   |
    +-----------------------------------------------------+--------------+-------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    exported_script_trigger_output_terminal = _attributes.AttributeViString(1150022)
    '''Type: str

    Specifies the destination terminal for exporting the Script Trigger. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_ —Refer to this topic for information about trigger delay.

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                     |
    +================+=================================================================================================================================+
    | ""             | The signal is not exported.                                                                                                     |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI0"         | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The signal is exported to the PFI 1 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI4"         | The signal is exported to the PFI 4 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PFI5"         | The signal is exported to the PFI 5 connector.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                  |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC"  | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.    |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                              |
    +----------------+---------------------------------------------------------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].exported_script_trigger_output_terminal`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.exported_script_trigger_output_terminal`
    '''
    exported_started_event_output_terminal = _attributes.AttributeViString(1150065)
    '''Type: str

    Specifies the destination terminal for exporting the Started event. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                            |
    +================+========================================================================================================================================+
    | ""             | The signal is not exported.                                                                                                            |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI0"         | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.        |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The signal is exported to the PFI 1 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI4"         | The signal is exported to the PFI 4 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI5"         | The signal is exported to the PFI 5 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC"  | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeViString(1150003)
    '''Type: str

    Specifies the destination terminal for exporting the Start Trigger. To set this property, the NI-RFSG device must be in the Configuration state.

    PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

    `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

    **Possible Values**:

    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                                                            |
    +================+========================================================================================================================================+
    | ""             | The signal is not exported.                                                                                                            |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI0"         | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.        |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI1"         | The signal is exported to the PFI 1 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI4"         | The signal is exported to the PFI 4 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PFI5"         | The signal is exported to the PFI 5 connector.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig0"    | The trigger is received on PXI trigger line 0.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig1"    | The trigger is received on PXI trigger line 1.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig2"    | The trigger is received on PXI trigger line 2.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig3"    | The trigger is received on PXI trigger line 3.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig4"    | The trigger is received on PXI trigger line 4.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig5"    | The trigger is received on PXI trigger line 5.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_Trig6"    | The trigger is received on PXI trigger line 6.                                                                                         |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "PXIe_DStarC"  | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "TrigOut"      | The signal is exported to the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI0"     | The trigger is received on PFI0 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI1"     | The trigger is received on PFI1 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI2"     | The trigger is received on PFI2 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI3"     | The trigger is received on PFI3 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI4"     | The trigger is received on PFI4 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI5"     | The trigger is received on PFI5 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI6"     | The trigger is received on PFI6 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    | "DIO/PFI7"     | The trigger is received on PFI7 from the front panel DIO terminal.                                                                     |
    +----------------+----------------------------------------------------------------------------------------------------------------------------------------+
    '''
    external_calibration_recommended_interval = _attributes.AttributeViInt32(1150076)
    '''Type: int

    Returns the recommended interval between each external calibration of the device.

    **Units**: months

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    external_calibration_temperature = _attributes.AttributeViReal64(1150077)
    '''Type: float

    Returns the temperature of the device at the time of the last external calibration.

    **Units**: degrees Celsius (°C)

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E
    '''
    external_gain = _attributes.AttributeViReal64(1150085)
    '''Type: float

    Specifies the external amplification or attenuation, if any, between the RF signal generator and the device under test.

    Positive values for this property represent amplification, and negative values for this property represent attenuation.

    **Valid Values:** -INF dB to +INF dB

    **Default Value:** 0dB

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: - Setting this property adjusts the actual device output power to compensate for any amplification or attenuation between the RF signal generator and the device under test.

     - For the PXIe-5645, this property is ignored if you are using the I/Q ports.
    '''
    fast_tuning_option = _attributes.AttributeViBoolean(1150188)
    '''Type: bool

    Returns whether the NI RF signal generator has the fast tuning option available.

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696

    **Related Topics**

    `Frequency Tuning Times for 5654 <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.5654.html>`_

    **Defined Values**:

    +-------+------------------------------------------------------------+
    | Value | Description                                                |
    +=======+============================================================+
    | True  | The RF signal generator has the fast 100 µs tuning option. |
    +-------+------------------------------------------------------------+
    | False | The RF signal generator has the 1 ms tuning option.        |
    +-------+------------------------------------------------------------+
    '''
    fixed_group_delay_across_ports = _attributes.AttributeViString(1150271)
    '''Type: str

    Specifies a comma-separated list of ports for which to fix the group delay.


    **Supported Devices:** PXIe-5831/5832
    '''
    fpga_bitfile_path = _attributes.AttributeViString(1150186)
    '''Type: str

    Returns a string containing the path to the location of the current NI-RFSG instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device. You can specify the bitfile location using the Driver Setup string in the **optionString** parameter of the __init__ method.

    NI-RFSG instrument driver FPGA extensions enable you to use pre-compiled FPGA bitfiles to customize the behavior of the vector signal transceiver FPGA while maintaining the functionality of the NI-RFSG instrument driver.

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `NI-RFSG Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/fpga_extensions.html>`_
    '''
    fpga_target_name = _attributes.AttributeViString(1150251)
    '''Type: str

    Returns a string that contains the name of the FPGA target being used. This name can be used with the RIO open session to open a reference to the FPGA.

    This property is channel dependent if multiple FPGA targets are supported.

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    fpga_temperature = _attributes.AttributeViReal64(1150211)
    '''Type: float

    Returns the FPGA temperature in degrees Celsius.

    Serial signals between the sensor and the system control unit can potentially modulate the signal being generated, thus causing phase spurs. After the device thoroughly warms up, its temperature varies only slightly (less than 1 degree Celsius) and slowly, and it is not necessary to constantly poll this temperature sensor.

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: If you query this property during RF list mode, list steps may take longer to complete during list execution.
    '''
    frequency = _attributes.AttributeViReal64(1250001)
    '''Type: float

    Specifies the frequency of the generated RF signal. For arbitrary waveform generation, this property specifies the center frequency of the signal.

    The PXI-5670/5671, PXIe-5672, PXIe-5820, and PXIe-5860 must be in the Configuration state to use this property. However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 can be in the Configuration or the Generation state to use this property.

    **Units**: hertz (Hz)

    **Defined Values**:
    Refer to the specifications document for your device allowable frequency settings.

    **Default Value:**

    PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E: 100MHz

    PXIe-5653: 4GHz

    PXIe-5820: 0Hz

    PXIe-5830/5831/5832: 6.5 GHz

    PXIe-5840/5841/5860, PXI-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options): 1GHz

    PXIe-5842 (4 GHz bandwidth option) using the Standard personality: 1GHz

    PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality: 6.5GHz

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

    **High-Level Methods**:

    - ConfigureRf

    Note: For the PXIe-5645, this property is ignored if you are using the I/Q ports.
    '''
    frequency_settling = _attributes.AttributeViReal64TimeDeltaSeconds(1150083)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the frequency settling time. Interpretation of this value depends on the frequency_settling_units property.

    **Valid Values:**

    The valid values for this property depend on the frequency_settling_units property.



    **Default Value**: 1.0

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_
    '''
    frequency_settling_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.FrequencySettlingUnits, 1150082)
    '''Type: enums.FrequencySettlingUnits

    Specifies the interpretation of the value passed to the frequency_settling property.

    PXIe-5650/5651/5652/5653, PXIe-5673E: When the ACTIVE_CONFIGURATION_LIST property is set to a valid list name, the frequency_settling_units property supports only FrequencySettlingUnits.TIME_AFTER_IO as a valid value.

    PXIe-5654/5654 with PXIe-5696: The frequency_settling_units property supports only FrequencySettlingUnits.TIME_AFTER_IO and FrequencySettlingUnits.PPM as valid values.

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Default Value**: FrequencySettlingUnits.PPM

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    **Defined Values**:

    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
    | Name                                   | Description                                                                                                     |
    +========================================+=================================================================================================================+
    | FrequencySettlingUnits.TIME_AFTER_LOCK | Specifies the time to wait after the frequency PLL locks.                                                       |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
    | FrequencySettlingUnits.TIME_AFTER_IO   | Specifies the time to wait after all writes occur to change the frequency.                                      |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
    | FrequencySettlingUnits.PPM             | Specifies the minimum frequency accuracy when settling completes. Units are in parts per million (PPM or 1E-6). |
    +----------------------------------------+-----------------------------------------------------------------------------------------------------------------+

    Note: If you set this property to FrequencySettlingUnits.TIME_AFTER_IO, the definition of settled for the Configuration Settled event changes.

    Note:
    One or more of the referenced properties are not in the Python API for this driver.
    '''
    frequency_tolerance = _attributes.AttributeViReal64(1150006)
    '''Type: float

    Specifies the allowable frequency error introduced during the software upconversion process. NI-RFSG may introduce a frequency error up to the specified amount to optimize computational speed and onboard memory usage while upconverting phase-continuous signals.

    If the phase_continuity_enabled property is set to NIRFSG_VAL_DISABLE, the frequency_tolerance property is ignored, and the driver does not introduce a frequency error. On devices that do not use software upconversion, this property is ignored. The PXI-5670 always uses software upconversion, and the PXI-5671 uses software upconversion for I/Q rates greater than 8.33MS/s.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Units**: hertz (Hz)

    **Default Value:** 50

    **Supported Devices:** PXI-5670/5671

    **Related Topics**

    `Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    generation_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.GenerationMode, 1150018)
    '''Type: enums.GenerationMode

    Specifies whether to generate a continuous wave (CW) signal, the arbitrary waveform specified by the arb_selected_waveform property, or the script specified by the selected_script property, upon calling the _initiate method.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** GenerationMode.CW

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696 (CW support only), PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

    `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_—Refer to this topic for more information about scripting.

    **Defined Values**:

    +-----------------------------+--------------+------------------------------------------------------------------------------------------------------------------------+
    | Name                        | Value        | Description                                                                                                            |
    +=============================+==============+========================================================================================================================+
    | GenerationMode.ARB_WAVEFORM | 1001 (0x3e9) | Configures the RF signal generator to generate the arbitrary waveform specified by the arb_selected_waveform property. |
    +-----------------------------+--------------+------------------------------------------------------------------------------------------------------------------------+
    | GenerationMode.CW           | 1000 (0x3e8) | Configures the RF signal generator to generate a CW signal.                                                            |
    +-----------------------------+--------------+------------------------------------------------------------------------------------------------------------------------+
    | GenerationMode.SCRIPT       | 1002 (0x3ea) | Configures the RF signal generator to generate arbitrary waveforms as directed by the selected_script property..       |
    +-----------------------------+--------------+------------------------------------------------------------------------------------------------------------------------+
    '''
    group_capabilities = _attributes.AttributeViString(1050401)
    '''Type: str

    Returns a string that contains a comma-separated list of class-extension groups that NI-RFSG implements.

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    host_dma_buffer_size = _attributes.AttributeViInt64(1150239)
    '''Type: int

    Specifies the size of the DMA buffer in computer memory, in bytes. To set this property, the NI-RFSG device must be in the Configuration state.

    A sufficiently large host DMA buffer improves performance by allowing large writes to be transferred more efficiently.

    **Units:** bytes

    **Default Value:** 8MB

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    Returns a string that contains the firmware revision information for the NI-RFSG device you are currently using.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **High-Level Methods**:

    - revision_query
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    Returns a string that contains the name of the manufacturer of the NI-RFSG device you are currently using.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    Returns a string that contains the model number or name of the NI-RFSG device that you are currently using. For drivers that support more than one device, this property returns a comma-separated list of supported devices.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    interchange_check = _attributes.AttributeViBoolean(1050021)
    '''Type: bool

    Specifies whether to perform interchangeability checking and retrieve interchangeability warnings.

    **Default Value:** False

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +-------+--------------------------------+
    | Value | Description                    |
    +=======+================================+
    | True  | Interchange check is enabled.  |
    +-------+--------------------------------+
    | False | Interchange check is disabled. |
    +-------+--------------------------------+

    Note: Enabling interchangeability check is not supported.
    '''
    interpolation_delay = _attributes.AttributeViReal64(1150153)
    '''Type: float

    Specifies the delay, in seconds, to apply to the I/Q waveform. To set this property, the NI-RFSG device must be in the Configuration state.

    **Units:** Seconds

    **Valid Values:** Plus or minus half of one I/Q sample period

    **Supported Devices:** PXIe-5644/5645/5646
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    Returns a string that contains the resource name NI-RFSG uses to identify the physical device. If you initialize NI-RFSG with a logical name, this property contains the resource name that corresponds to the entry in the IVI Configuration Utility. If you initialize NI-RFSG with the resource name, this property contains that value.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    iq_gain_imbalance = _attributes.AttributeViReal64(1150072)
    '''Type: float

    Specifies the gain imbalance of the I/Q modulator (I versus Q).

    Gain imbalance is calculated with the following equation:

    **Units**: dB

    **Valid Values:**-6dB to 6dB

    **Default Value:** 0dB

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_

    `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_
    '''
    iq_impairment_enabled = _attributes.AttributeViBoolean(1150069)
    '''Type: bool

    Enables or disables I/Q impairment. The iq_i_offset, iq_q_offset, iq_gain_imbalance, and iq_skew properties are ignored when the iq_impairment_enabled property is disabled.

    **Default Value:** True

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Defined Values**:

    +-------+-----------------------------+
    | Value | Description                 |
    +=======+=============================+
    | True  | I/Q impairment is enabled.  |
    +-------+-----------------------------+
    | False | I/Q impairment is disabled. |
    +-------+-----------------------------+
    '''
    iq_i_offset = _attributes.AttributeViReal64(1150070)
    '''Type: float

    When using a National Instruments AWG module or vector signal transceiver (VST), this property specifies the I-signal DC offset. Units are either percent (%) or volts (V), depending on the iq_offset_units property setting.

    PXIe-5673/5673E: Actual AWG signal offset is equal to the I/Q modulator offset correction plus the value specified by this property. When using an external AWG (non–National Instruments AWG), this property is read-only and indicates the I/Q modulator I-offset. Units are volts, as specified by the iq_offset_units property.

    **Valid Values:**-100 to 100% or -0.2V to 0.2V

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_
    '''
    iq_offset_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OffsetUnits, 1150081)
    '''Type: enums.OffsetUnits

    Specifies the units of the iq_i_offset property and iq_q_offset property. Offset units are either percent or volts.

    The AWG or VST offset is the specified percentage of the AWG or VST peak power level when the iq_offset_units property is set to OffsetUnits.PERCENT. Given perfect carrier leakage suppression, the following equation is satisfied


    or equivalently

    If the iq_i_offset property is set to 100%, iq_q_offset property is set to 0%, and power_level property set to 0 dBm, the desired RF signal is at 0 dBm and the carrier leakage is also at 0 dBm.

    The AWG or VST peak power level changes when settings change in other properties such as the power_level, frequency, iq_skew, iq_gain_imbalance, attenuator_hold_enabled, and arb_pre_filter_gain properties. When the iq_offset_units property is set to OffsetUnits.PERCENT, the actual AWG or VST offset changes as the AWG or VST peak power level changes to satisfy the preceding equations. These changes are useful if you are intentionally adding carrier leakage to test the tolerance of a receiver. When the iq_offset_units property is set to OffsetUnits.PERCENT, the carrier leakage, in dBc, remains at a consistent level.

    If you are trying to eliminate residual carrier leakage due to calibration inaccuracies or drift, set the iq_offset_units property to OffsetUnits.VOLTS. Offset correction voltage is applied to the I/Q modulator or VST, regardless of changes to the AWG or VST peak power level.

    **Default Value**: OffsetUnits.PERCENT

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Defined Values**:

    +---------------------+----------------------------------------------------------------------+
    | Name                | Description                                                          |
    +=====================+======================================================================+
    | OffsetUnits.PERCENT | Specifies the iq_i_offset and iq_q_offset property units as percent. |
    +---------------------+----------------------------------------------------------------------+
    | OffsetUnits.VOLTS   | Specifies the iq_i_offset and iq_q_offset property units as volts.   |
    +---------------------+----------------------------------------------------------------------+

    Note: For any devices except PXIe-5820, if the iq_offset_units property is set to OffsetUnits.VOLTS, a 0.1 I offset results in a 0.1 V offset in the output. For PXIe-5820 devices, 0.1 I offset results in a 10% offset in the output.
    '''
    iq_out_port_carrier_frequency = _attributes.AttributeViReal64(1150145)
    '''Type: float

    Specifies the frequency of the I/Q OUT port signal. The onboard signal processing (OSP) applies the specified frequency shift to the I/Q data before the data is sent to the digital-to-analog converter (DAC). To set this property, the NI-RFSG device must be in the Configuration state.

    **Units:** hertz (Hz)

    **Valid Values:**

    PXIe-5645: -60MHz to 60MHz

    PXIe-5820: -500MHz to 500MHz

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: - For the PXIe-5820, NI recommends using the frequency property.

     - For the PXIe-5645, this property is ignored if you are using the RF ports.
    '''
    iq_out_port_common_mode_offset = _attributes.AttributeViReal64(1150148)
    '''Type: float

    Specifies the common-mode offset applied to the signals generated at each differential output terminal. This property applies only when you set the iq_out_port_terminal_configuration property to IQOutPortTerminalConfiguration.DIFFERENTIAL. Common-mode offset shifts both positive and negative terminals in the same direction.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Units:** Volts

    **Valid Values:**

    PXIe-5645: -0.8V to 0.8V if you set the iq_out_port_load_impedance property to 50 Ω. The valid values are -1.2V to 1.2V if you set the iq_out_port_load_impedance property to 100 Ω.

    PXIe-5820: -0.25V to 1.5V

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: - For the PXIe-5645, this property is ignored if you are using the RF ports.

     - The valid range is dependent on the load impedance.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].iq_out_port_common_mode_offset`

    To set/get on all channels, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.iq_out_port_common_mode_offset`
    '''
    iq_out_port_level = _attributes.AttributeViReal64(1150147)
    '''Type: float

    Specifies the amplitude of the generated signal in volts, peak-to-peak (V). For example, if you set this property to 1.0, the output signal ranges from -0.5 volts to 0.5 volts.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    To set this property, the NI-RFSG device must be in the Configuration state.

    Refer to the specifications document for your device for allowable output levels.

    **Units:** Volts, peak-to-peak (V :sub:`pk-pk` )

    **Valid Values:**

    PXIe-5645: 1V :sub:`pk-pk`  maximum if you set the iq_out_port_terminal_configuration property to IQOutPortTerminalConfiguration.DIFFERENTIAL, and 0.5V :sub:`pk-pk`

    maximum if you set the iq_out_port_terminal_configuration property to IQOutPortTerminalConfiguration.SINGLE_ENDED.

    PXIe-5820: 3.4V :sub:`pk-pk` maximum for signal bandwidth less than 160MHz, and 2V :sub:`pk-pk`

    maximum for signal bandwidth greater than 160MHz.

    **Default Value:** 0.5volts

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: - For the PXIe-5645, this property is ignored if you are using the RF ports.

     - The valid values are only applicable when you set the iq_out_port_load_impedance property to 50 Ω and when you set the iq_out_port_offset property to 0.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].iq_out_port_level`

    To set/get on all channels, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.iq_out_port_level`
    '''
    iq_out_port_load_impedance = _attributes.AttributeViReal64(1150163)
    '''Type: float

    Specifies the load impedance connected to the I/Q OUT port. To set this property, the NI-RFSG device must be in the Configuration state.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    **Units:** Ohms

    **Valid Values:** Any value greater than 0. Values greater than or equal to 1 megaohms (MΩ) are interpreted as high impedance.

    **Default Value:** 50 Ω if you set the iq_out_port_terminal_configuration property to IQOutPortTerminalConfiguration.SINGLE_ENDED, and 100 Ω if you set the iq_out_port_terminal_configuration property to IQOutPortTerminalConfiguration.DIFFERENTIAL.

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: For the PXIe-5645, this property is ignored if you are using the RF ports.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].iq_out_port_load_impedance`

    To set/get on all channels, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.iq_out_port_load_impedance`
    '''
    iq_out_port_offset = _attributes.AttributeViReal64(1150149)
    '''Type: float

    Specifies the value, in volts, that the signal generator adds to the arbitrary waveform data. To set this property, the NI-RFSG device must be in the Configuration state.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    PXIe-5645: The waveform may be scaled in DSP prior to adding offset and the device state may be changed in order to accommodate the requested offset.

    PXIe-5820: The waveform is not automatically scaled in DSP. To prevent DSP overflows, use the arb_pre_filter_gain property to scale the waveform to provide additional headroom for offsets.

    **Units:** Volts

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: For the PXIe-5645, this property is ignored if you are using the RF ports.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].iq_out_port_offset`

    To set/get on all channels, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.iq_out_port_offset`
    '''
    iq_out_port_temperature = _attributes.AttributeViReal64(1150161)
    '''Type: float

    Returns the temperature, in degrees Celsius, of the I/Q Out circuitry on the device.

    **Units:** Degrees Celsius

    **Supported Devices:** PXIe-5645, PXIe-5820

    Note: If you query this property during RF list mode, list steps may take longer to complete during list execution.
    '''
    iq_out_port_terminal_configuration = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.IQOutPortTerminalConfiguration, 1150146)
    '''Type: enums.IQOutPortTerminalConfiguration

    Specifies whether to use the I/Q OUT port for differential configuration or single-ended configuration. If you set this property to IQOutPortTerminalConfiguration.SINGLE_ENDED, you must terminate the negative I and Q output connectors with a 50 Ohm termination.

    If you set this property to IQOutPortTerminalConfiguration.SINGLE_ENDED, the positive I and Q connectors generate the resulting waveform. If you set this property to IQOutPortTerminalConfiguration.DIFFERENTIAL, both the positive and negative I and Q connectors generate the resulting waveform.

    To use this property, you must use the channelName parameter of the _set_attribute_vi_int32 method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** IQOutPortTerminalConfiguration.DIFFERENTIAL

    PXIe-5820: The only valid value for this property is IQOutPortTerminalConfiguration.DIFFERENTIAL.

    **Supported Devices:** PXIe-5645, PXIe-5820

    **Related Topics**

    `Differential and Single-Ended Operation (I/O Interface) <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/differential_single_ended_operation.html>`_

    **Defined Values**:

    +---------------------------------------------+----------------+--------------------------------------------------+
    | Name                                        | Value          | Description                                      |
    +=============================================+================+==================================================+
    | IQOutPortTerminalConfiguration.DIFFERENTIAL | 15000 (0x3a98) | Sets the terminal configuration to differential. |
    +---------------------------------------------+----------------+--------------------------------------------------+
    | IQOutPortTerminalConfiguration.SINGLE_ENDED | 15001 (0x3a99) | Sets the terminal configuration to single-ended. |
    +---------------------------------------------+----------------+--------------------------------------------------+

    Note: For the PXIe-5645, this property is ignored if you are using the RF ports.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].iq_out_port_terminal_configuration`

    To set/get on all channels, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.iq_out_port_terminal_configuration`
    '''
    iq_q_offset = _attributes.AttributeViReal64(1150071)
    '''Type: float

    When using a National Instruments AWG module or VST device, this property specifies the Q-signal DC offset. Units are either percent (%) or volts (V), depending on the iq_offset_units property setting.
    PXIe-5673/5673E: Actual AWG signal offset is equal to the I/Q modulator offset correction plus the value specified by this property. When using an external AWG (non–National Instruments AWG), the iq_q_offset property is read-only and indicates the I/Q modulator Q-offset. Units are volts, as indicated by the iq_offset_units property.
    **Valid Values**: -100% to 100% or -0.2V to 0.2V
    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842
    **Related Topics**
    `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_
    '''
    iq_rate = _attributes.AttributeViReal64(1250452)
    '''Type: float

    This property specifies the I/Q rate of the arbitrary waveform. The I/Q rate is coerced to a value the hardware can achieve. Read this value back after setting it to see the actual I/Q rate. NI-RFSG internally uses an FIR filter with flat response up to (0.4 × IQ rate). Given a desired signal with the maximum frequency content *f*, sample the signal at an I/Q rate greater than or equal to ( *f*/0.4).

    This property applies only when the generation_mode property is set to GenerationMode.ARB_WAVEFORM or GenerationMode.SCRIPT.

    To set this property, the NI-RFSG device must be in the Configuration state.

    Setting this property to 50 MS/s on the PXI-5670/5671 and PXIe-5672 has the following implications:
    - NI-RFSG is forced to place the carrier frequency at 18 MHz ± 1 MHz to avoid aliasing. This means that NI-RFSG cannot select a carrier frequency that could optimize waveform size if phase continuity is enabled.
    - Output signal bandwidth must be <5 MHz to avoid aliasing.
    - Close-in phase noise is higher.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate an I/Q rate with a waveform.

    `Digital Upconverter <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/duc.html>`_

    **Valid Values**:

    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Device                                                                   | I/Q Rates                                                                                                                                                                                                                                          |
    +==========================================================================+====================================================================================================================================================================================================================================================+
    | PXIe-5644/5645                                                           | Up to 120 MS/s.                                                                                                                                                                                                                                    |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5646                                                                | Up to 250 MS/s.                                                                                                                                                                                                                                    |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXI-5670                                                                 | 50 MS/s ((100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12, 14, 16, ..., 512, 516, 520, ..., 1,024). Setting the I/Q rate to one of these value enables the DUC.)                         |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |                                                                          | 100 MS/s ((100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12, 14, 16, ..., 512, 516, 520, ..., 1,024). Setting the I/Q rate to one of these value enables the DUC.)                        |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXI-5671                                                                 | 50 MS/s ((100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12, 14, 16, ..., 512, 516, 520, ..., 1,024). Setting the I/Q rate to one of these value enables the DUC.)                         |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |                                                                          | 100 MS/s                                                                                                                                                                                                                                           |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5672                                                                | Up to 100 MS/s.                                                                                                                                                                                                                                    |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5673/5673E                                                          | Up to 200 MS/s. Note that -  If an PXIe-5450 with module revisions A or B is used as part of your PXIe-5673/5673E, the NI-FGEN NIFGEN_ATTR_COMPENSATE_FOR_FILTER_GROUP_DELAY property is disabled if the requested I/Q rate is less than 1.5 MS/s. |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5820/5830/5831/5832/5840/5841/5860                                  | Up to 1.25 GS/s.                                                                                                                                                                                                                                   |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXI-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options)                   | Up to 2.5 GS/s                                                                                                                                                                                                                                     |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |  PXIe-5842 (4 GHz bandwidth option) using the Standard personality       | Up to 2.5 GS/s                                                                                                                                                                                                                                     |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality | 5 GS/s only.                                                                                                                                                                                                                                       |
    +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: Use this property to associate an I/Q rate with a waveform.
    '''
    iq_skew = _attributes.AttributeViReal64(1150073)
    '''Type: float

    Specifies the adjustment of the phase angle between the I and Q vectors. If the skew is zero, the phase angle is 90 degrees.

    This property is ignored when the iq_impairment_enabled property is disabled.

    **Units**: degrees (°)

    **Valid Values:**-30° to 30°

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_
    '''
    iq_swap_enabled = _attributes.AttributeViBoolean(1250404)
    '''Type: bool

    Enables or disables the inverse phase rotation of the I/Q signal by swapping the I and Q inputs.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Defined Values**:

    +-------+---------------------------------------------------------------------+
    | Value | Description                                                         |
    +=======+=====================================================================+
    | True  | NI-RFSG device applies noninverse phase rotation of the I/Q signal. |
    +-------+---------------------------------------------------------------------+
    | False | NI-RFSG device applies inverse phase rotation of the I/Q signal.    |
    +-------+---------------------------------------------------------------------+
    '''
    load_configurations_from_file_load_options = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoadOptions, 1150290)
    '''Type: enums.LoadOptions

    Specifies the configurations to skip while loading from a file.

    **Default Value:**  NIRFSG_VAL_SKIP_NONE

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +--------------------------------------------------------------------+-------------------------------------------------------------------+
    | Value                                                              | Description                                                       |
    +====================================================================+===================================================================+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_NONE      | NI-RFSG loads all the configurations to the session.              |
    +--------------------------------------------------------------------+-------------------------------------------------------------------+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_WAVEFORMS | NI-RFSG skips loading the waveform configurations to the session. |
    +--------------------------------------------------------------------+-------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    load_configurations_from_file_reset_options = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoadConfigurationResetOptions, 1150291)
    '''Type: enums.LoadConfigurationResetOptions

    Specifies the configurations to skip to reset while loading configurations from a file.

    **Default Value:**  NIRFSG_VAL_SKIP_NONE
    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +------------------------------------------------------------------------------+------------------------------------------------------+
    | Value                                                                        | Description                                          |
    +==============================================================================+======================================================+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE               | NI-RFSG resets all configurations.                   |
    +------------------------------------------------------------------------------+------------------------------------------------------+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_WAVEFORMS          | NI-RFSG skips resetting the waveform configurations. |
    +------------------------------------------------------------------------------+------------------------------------------------------+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_SCRIPTS            | NI-RFSG skips resetting the scripts.                 |
    +------------------------------------------------------------------------------+------------------------------------------------------+
    | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_DEEMBEDDING_TABLES | NI-RFSG skips resetting the de-embedding tables.     |
    +------------------------------------------------------------------------------+------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    Returns a string that contains the logical name you specified when opening the current IVI session. You can pass a logical name to the Init method or the __init__ method. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a driver session section in the IVI Configuration file. The driver session section specifies a physical device and initial user options.

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    loop_bandwidth = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoopBandwidth, 1150027)
    '''Type: enums.LoopBandwidth

    Configures the loop bandwidth of the tuning PLLs. This property is ignored on the PXI-5610, PXI-5670/5671, and PXIe-5672 for signal bandwidths greater than or equal to 10MHz. This property is ignored on the PXI/PXIe-5650/5651/5652 for RF frequencies less than 50MHz.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_int32 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Default Value:**

    PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842: LoopBandwidth.MEDIUM

    PXI/PXIe-5650/5651/5652, PXIe-5673/5673E: LoopBandwidth.NARROW

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_

    `Modulation Implementation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5650_5651_5652_modulation_implementation.html>`_

    `Sinusoidal Tone Versus Modulation Operation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sinusoidal_tone_versus_modulation_implementation.html>`_

    **Defined Values**:

    +----------------------+---------+--------------------------------------------------------+
    | Name                 | Value   | Description                                            |
    +======================+=========+========================================================+
    | LoopBandwidth.MEDIUM | 1 (0x1) | Uses the medium loop bandwidth setting for the PLL.    |
    +----------------------+---------+--------------------------------------------------------+
    | LoopBandwidth.NARROW | 0 (0x0) | Uses the narrowest loop bandwidth setting for the PLL. |
    +----------------------+---------+--------------------------------------------------------+
    | LoopBandwidth.WIDE   | 2 (0x2) | Uses the widest loop bandwidth setting for the PLL.    |
    +----------------------+---------+--------------------------------------------------------+

    Note: Setting this property to LoopBandwidth.WIDE on the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, or the PXIe-5673/5673E allows the frequency to settle significantly faster at the expense of increased phase noise. Setting this property to LoopBandwidth.MEDIUM is not a valid option on the PXI/PXIe-5650/5651/5652 or PXIe-5673/5673E. LoopBandwidth.MEDIUM is the only supported value for the PXIe-5840/5841/5842.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].loop_bandwidth`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.loop_bandwidth`
    '''
    lo_frequency = _attributes.AttributeViReal64(1150199)
    '''Type: float

    Specifies the frequency of the LO source.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `PXIe-5830 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_configuration.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_configuration.html>`_

    Note: This property is read/write if you are using an external LO. Otherwise, this property is read-only.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_frequency`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_frequency`
    '''
    lo_frequency_step_size = _attributes.AttributeViReal64(1150151)
    '''Type: float

    Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).

    When the lo_pll_fractional_mode_enabled property is enabled, the specified step size affects the fractional spur performance of the device. When the lo_pll_fractional_mode_enabled property is disabled, the specified step size affects the phase noise performance of the device.

    The valid values for this property depend on the lo_pll_fractional_mode_enabled property.

    **PXIe-5644/5645/5646**—If you disable the lo_pll_fractional_mode_enabled property, the specified value is coerced to the nearest valid value.

    **PXIe-5840/5841**—If you disable the lo_pll_fractional_mode_enabled property, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.

    **Units:** hertz (Hz)

    **Default Values:**

    PXIe-5644/5645/5646: 200kHz

    PXIe-5830: 2MHz

    PXIe-5831/5832 (RF port): 8MHz

    PXIe-5831/5832 (IF port): 2MHz, 4MHz

    PXIe-5840/5841:

    - Fractional mode: 500 kHz
    - Integer mode: 10 MHz for frequencies less than or equal to 4 GHz. 20 MHz for frequencies greater than 4 GHz.

    PXIe-5841 with PXIe-5655: 500kHz

    PXIe-5842: 1Hz

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_pll_fractional_mode_enabled Property Setting                                                  | NIRFSG_VAL_ENABLE | NIRFSG_VAL_DISABLE                               |
    +==================================================================================================+===================+==================================================+
    | lo_frequency_step_size Property Valid Values on PXIe-5644/5645                                   | 50 kHz to 24 MHz  | 4 MHz, 5 MHz, 6 MHz, 12 MHz, or 24 MHz           |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_frequency_step_size Property Valid Values on PXIe-5646                                        | 50 kHz to 25 MHz  | 2 MHz, 5 MHz, 10 MHz, or 25 MHz                  |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_frequency_step_size Property Valid Values on PXIe-5840/5841                                   | 50 kHz to 100 MHz | 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, or 100 MHz |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_frequency_step_size Property Valid Values on PXIe-5830/5831/ 5832 LO1                         | 8 Hz to 400 MHz   | —                                                |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_frequency_step_size Property Valid Values on PXIe-5830/5831/ 5832 LO2                         | 4 Hz to 400 MHz   | —                                                |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+
    | lo_frequency_step_size Property Valid Values on PXIe-5841 with PXIe-5655/NI PXIe-5842 (See note) | 1 nHz to 100 MHz  | 1 nHz to 50 MHz                                  |
    +--------------------------------------------------------------------------------------------------+-------------------+--------------------------------------------------+

    Note: Values up to 100 MHz are coerced to 50 MHz.
    '''
    lo_in_power = _attributes.AttributeViReal64(1150067)
    '''Type: float

    Specifies the power level of the signal at the LO IN front panel connector.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Units**: dBm

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_

    Note: - This property is read/write if you are using an external LO. Otherwise, this property is read-only.

     - For the PXIe-5644/5645/5646, this property is always read-only.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_in_power`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_in_power`
    '''
    lo_out_enabled = _attributes.AttributeViBoolean(1150013)
    '''Type: bool

    Specifies whether the local oscillator signal is present at the LO OUT front panel connector. The local oscillator signal remains at the LO OUT front panel connector until this property is set to False, even if the output_enabled property is set to False, the abort method is called, or the NI-RFSG session is closed.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_boolean method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Default Value:** NIRFSG_VAL_DISABLE

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_

    **Defined Values**:

    +--------------------+---------------------------------------------------------------------------------+
    | Name               | Description                                                                     |
    +====================+=================================================================================+
    | NIRFSG_VAL_ENABLE  | The local oscillator signal is present at the LO OUT front panel connector.     |
    +--------------------+---------------------------------------------------------------------------------+
    | NIRFSG_VAL_DISABLE | The local oscillator signal is not present at the LO OUT front panel connector. |
    +--------------------+---------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_out_enabled`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_out_enabled`
    '''
    lo_out_export_configure_from_rfsa = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoOutExportConfigureFromRfsaEnable, 1150242)
    '''Type: enums.LoOutExportConfigureFromRfsaEnable

    Specifies whether to allow NI-RFSA to control the NI-RFSG LO out export.

    Set this property to LoOutExportConfigureFromRfsaEnable.ENABLE to allow NI-RFSA to control the LO out export. Use the RF OUT LO EXPORT ENABLED property to control the LO out export from NI-RFSA.

    **Default Value:** LoOutExportConfigureFromRfsaEnable.DISABLE

    **Supported Devices**: PXIe-5840/5841/5842

    **Defined Values**:

    +--------------------------------------------+---------+----------------------------------------------------------------------+
    | Name                                       | Value   | Description                                                          |
    +============================================+=========+======================================================================+
    | LoOutExportConfigureFromRfsaEnable.ENABLE  | 0 (0x0) | Do not allow NI-RFSA to control the NI-RFSG local oscillator export. |
    +--------------------------------------------+---------+----------------------------------------------------------------------+
    | LoOutExportConfigureFromRfsaEnable.DISABLE | 1 (0x1) | Allow NI-RFSA to control the NI-RFSG local oscillator export.        |
    +--------------------------------------------+---------+----------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    lo_out_power = _attributes.AttributeViReal64(1150066)
    '''Type: float

    Specifies the power level of the signal at the LO OUT front panel connector.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_real64 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Units**: dBm

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_

    Note: For the PXIe-5644/5645/5646 and PXIe-5673/5673E, this property is always read-only.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_out_power`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_out_power`
    '''
    lo_pll_fractional_mode_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.LoPllFractionalModeEnabled, 1150152)
    '''Type: enums.LoPllFractionalModeEnabled

    Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL). This property enables or disables fractional frequency tuning in the LO. Fractional mode provides a finer frequency step resolution and allows smaller values for the lo_frequency_step_size property. However, fractional mode may introduce non-harmonic spurs.

    This property applies only if you set the lo_source property to Onboard.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_int32 method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" .

    **Default Value:** LoPllFractionalModeEnabled.ENABLE

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    Refer to the local oscillators topic appropriate to your device for more information about using fractional mode.

    **Defined Values**:

    +------------------------------------+---------+------------------------------------------+
    | Name                               | Value   | Description                              |
    +====================================+=========+==========================================+
    | LoPllFractionalModeEnabled.ENABLE  | 0 (0x0) | Disables fractional mode for the LO PLL. |
    +------------------------------------+---------+------------------------------------------+
    | LoPllFractionalModeEnabled.DISABLE | 1 (0x1) | Enables fractional mode for the LO PLL.  |
    +------------------------------------+---------+------------------------------------------+

    Note: For the PXIe-5841 with PXIe-5655, this property is ignored if the PXIe-5655 is used as the LO source.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_pll_fractional_mode_enabled`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_pll_fractional_mode_enabled`
    '''
    lo_source = _attributes.AttributeViString(1150150)
    '''Type: str

    Specifies whether to use the internal or external local oscillator (LO) source. If the lo_source property is set to "" (empty string), NI-RFSG uses the internal LO source. To set this property, the NI-RFSG device must be in the Configuration state.

    To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the _set_attribute_vi_string method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

    **Default Value:** Onboard

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `PXIe-5830 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/lo_sharing_using_rfsa_rfsg.html>`_

    `PXIe-5831/5832 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/lo_sharing_using_rfsa_rfsg.html>`_

    **Possible Values**:

    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value           | Description                                                                                                                                                                                                                                                      |
    +==========================+==================================================================================================================================================================================================================================================================+
    | "Automatic_SG_SA_Shared" | NI-RFSG internally makes the configuration to share the LO between NI-RFSA and NI-RFSG. This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841/5842.                                                                                                 |
    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "LO_In"                  | Uses an external LO as the LO source. Connect a signal to the LO IN connector on the device and use the upconverter_center_frequency property to specify the LO frequency.                                                                                       |
    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "Onboard"                | Uses an internal LO as the LO source. If you specify an internal LO source, the LO is generated inside the device itself.                                                                                                                                        |
    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "SG_SA_Shared"           | Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSG selects an internal synthesizer and the synthesizer signal is switched to both the RF In and RF Out mixers. This value is valid only on the PXIe-5830/5831/5832/5841 with PXIe-5655/5842. |
    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "Secondary"              | Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid only on the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653.                                                                                                                     |
    +--------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this property is set to SG_SA_Shared.

    Tip:
    This property can be set/get on specific los within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container los to specify a subset.

    Example: :py:attr:`my_session.los[ ... ].lo_source`

    To set/get on all los, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.lo_source`
    '''
    lo_temperature = _attributes.AttributeViReal64(1150075)
    '''Type: float

    Returns the LO module temperature in degrees Celsius.

    PXIe-5840/5841: If you query this property during RF list mode, list steps may take longer to complete during list execution.

    **Units**: degrees Celsius (°C)

    **Supported Devices:** PXIe-5673/5673E, PXIe-5840/5841/5842
    '''
    lo_vco_frequency_step_size = _attributes.AttributeViReal64(1150257)
    '''Type: float

    Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal.

    **Valid Values**:

    LO1: 1 Hz to 50 MHz

    LO2: 1 Hz to 100 MHz

    **Default Value**: 1 MHz

    **Supported Devices**: PXIe-5830/5831/5832
    '''
    marker_event_output_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.MarkerEventOutputBehavior, 1150206)
    '''Type: enums.MarkerEventOutputBehavior

    Specifies the output behavior for the Marker Event. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** MarkerEventOutputBehavior.PULSE

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    **Defined Values**:

    +----------------------------------+----------------+-------------------------------------------------------+
    | Name                             | Value          | Description                                           |
    +==================================+================+=======================================================+
    | MarkerEventOutputBehavior.PULSE  | 23000 (0x59d8) | Specifies the Marker Event output behavior as pulse.  |
    +----------------------------------+----------------+-------------------------------------------------------+
    | MarkerEventOutputBehavior.TOGGLE | 23001 (0x59d9) | Specifies the Marker Event output behavior as toggle. |
    +----------------------------------+----------------+-------------------------------------------------------+

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_output_behavior`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.marker_event_output_behavior`
    '''
    marker_event_pulse_width = _attributes.AttributeViReal64(1150207)
    '''Type: float

    Specifies the pulse width value for the Marker Event. Use the marker_event_pulse_width_units property to set the units for the pulse width value. This property is valid only when the marker_event_output_behavior property is set to MarkerEventOutputBehavior.PULSE.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** 200 ns

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_pulse_width`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.marker_event_pulse_width`
    '''
    marker_event_pulse_width_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.MarkerEventPulseWidthUnits, 1150208)
    '''Type: enums.MarkerEventPulseWidthUnits

    Specifies the pulse width units for the Marker Event. This property is valid only when the marker_event_output_behavior property is set to MarkerEventOutputBehavior.PULSE.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** MarkerEventPulseWidthUnits.SECONDS

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    **Defined Values**:

    +----------------------------------+----------------+-------------------------------------------------------+
    | Name                             | Value          | Description                                           |
    +==================================+================+=======================================================+
    | MarkerEventOutputBehavior.PULSE  | 23000 (0x59d8) | Specifies the Marker Event output behavior as pulse.  |
    +----------------------------------+----------------+-------------------------------------------------------+
    | MarkerEventOutputBehavior.TOGGLE | 23001 (0x59d9) | Specifies the Marker Event output behavior as toggle. |
    +----------------------------------+----------------+-------------------------------------------------------+

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_pulse_width_units`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.marker_event_pulse_width_units`
    '''
    marker_event_terminal_name = _attributes.AttributeViString(1150115)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Default Values**:

    PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/Marker *X* Event, where *AWGName* is the name of your associated AWG module in MAX and *X* is Marker Event 0 through 3.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/Marker *X* Event, where *BasebandModule* is the name of the baseband module of your device in MAX and *X* is Marker Event 0 through 3.

    PXIe-5820/5840/5841: /*ModuleName*/ao/0/Marker *X* Event, where *ModuleName* is the name of your device in MAX and *X* is Marker Event 0 through 3.

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

    **High-Level Methods**:

    - get_terminal_name

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_terminal_name`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.marker_event_terminal_name`
    '''
    marker_event_toggle_initial_state = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.MarkerEventToggleInitialState, 1150209)
    '''Type: enums.MarkerEventToggleInitialState

    Specifies the initial state for the Marker Event when the marker_event_output_behavior property is set to MarkerEventOutputBehavior.TOGGLE.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** MarkerEventToggleInitialState.LOW

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    **Defined Values**:

    +------------------------------------+----------------+----------------------------------------------------------------------------------+
    | Name                               | Value          | Description                                                                      |
    +====================================+================+==================================================================================+
    | MarkerEventToggleInitialState.HIGH | 21001 (0x5209) | Specifies the initial state of the Marker Event toggle behavior as digital high. |
    +------------------------------------+----------------+----------------------------------------------------------------------------------+
    | MarkerEventToggleInitialState.LOW  | 21000 (0x5208) | Specifies the initial state of the Marker Event toggle behavior as digital low.  |
    +------------------------------------+----------------+----------------------------------------------------------------------------------+

    Tip:
    This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_toggle_initial_state`

    To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.marker_event_toggle_initial_state`
    '''
    memory_size = _attributes.AttributeViInt64(1150061)
    '''Type: int

    The total amount of memory on the signal generator in bytes.

    **Units:** bytes

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Memory Options <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/memory_options.html>`_

    `Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_

    Note: Not all onboard memory is available for waveform storage. A portion of onboard memory stores scripts that specify how the waveforms are generated. These scripts typically require less than 1KB of onboard memory.
    '''
    module_power_consumption = _attributes.AttributeViReal64(1150210)
    '''Type: float

    Returns the total power consumption of the device.

    **Units:** watts

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: If you query this property during RF list mode, list steps may take longer to complete during list execution.
    '''
    module_revision = _attributes.AttributeViString(1150084)
    '''Type: str

    Returns the module revision letter. If the NI-RFSG session is controlling multiple modules, this property returns the revision letter of the primary RF module. The NI-RFSG session is opened using the primary RF device name.

    **Supported Devices:** PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Identifying Module Revision <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/identifying_device_revision.html>`_
    '''
    output_enabled = _attributes.AttributeViBoolean(1250004)
    '''Type: bool

    Specifies whether signal output is enabled. Setting the output_enabled property to False while in the Generation state stops signal output, although generation continues internally. For the PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653, PXI-5670/5671, and PXIe-5672/5673/5673E, setting the output_enabled property while in the Committed state does not transition the device to the Configuration state, but output changes immediately.

    **Default Value:** True

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Output Enabled <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/outputenable.html>`_

    `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

    **Defined Values**:

    +-------+-------------------------+
    | Value | Description             |
    +=======+=========================+
    | True  | Enables signal output.  |
    +-------+-------------------------+
    | False | Disables signal output. |
    +-------+-------------------------+

    Note: - For the PXIe-5653, this property controls only the LO1 terminal.

     - For the PXIe-5645, this property is ignored if you are using the I/Q ports.

     - When the ACTIVE_CONFIGURATION_LIST property is set to a valid list name, setting the output_enabled property transitions the device to the Configuration state.

    Note:
    One or more of the referenced properties are not in the Python API for this driver.
    '''
    output_port = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OutputPort, 1150144)
    '''Type: enums.OutputPort

    Specifies the connector(s) to use to generate the signal. To set this property, the NI-RFSG device must be in the Configuration state.

    You must write complex I and Q data for all options. The Q data has no effect if you set this property to I Only and set the iq_out_port_carrier_frequency property to 0. If you set the iq_out_port_carrier_frequency property to a value other than 0, the onboard signal processing (OSP) frequency shifts I and Q as a complex value and outputs the real portion of the result on the I connector(s) of the device.

    If you set the output_port property to OutputPort.I_ONLY or OutputPort.IQ_OUT, the iq_out_port_terminal_configuration property applies.

    **Default Value:**

    PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860: OutputPort.RF_OUT

    PXIe-5820: OutputPort.IQ_OUT

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +--------------------+----------------+------------------------------------------------------------------------------------------+
    | Name               | Value          | Description                                                                              |
    +====================+================+==========================================================================================+
    | OutputPort.CAL_OUT | 14002 (0x36b2) | Enables the CAL OUT port.                                                                |
    +--------------------+----------------+------------------------------------------------------------------------------------------+
    | OutputPort.I_ONLY  | 14003 (0x36b3) | Enables the I connectors of the I/Q OUT port. This value is valid on only the PXIe-5645. |
    +--------------------+----------------+------------------------------------------------------------------------------------------+
    | OutputPort.IQ_OUT  | 14001 (0x36b1) | Enables the I/Q OUT port. This value is valid on only the PXIe-5645 and PXIe-5820.       |
    +--------------------+----------------+------------------------------------------------------------------------------------------+
    | OutputPort.RF_OUT  | 14000 (0x36b0) | Enables the RF OUT port. This value is not valid for the PXIe-5820.                      |
    +--------------------+----------------+------------------------------------------------------------------------------------------+
    '''
    overflow_error_reporting = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OverflowErrorReporting, 1150228)
    '''Type: enums.OverflowErrorReporting

    Configures error reporting for onboard signal processing (OSP) overflows. Overflows lead to clipping of the waveform.

    **Default Value:** OverflowErrorReporting.WARNING

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +---------------------------------+--------------+----------------------------------------------------------------------------+
    | Name                            | Value        | Description                                                                |
    +=================================+==============+============================================================================+
    | OverflowErrorReporting.DISABLED | 1302 (0x516) | NI-RFSG does not return an error or a warning when an OSP overflow occurs. |
    +---------------------------------+--------------+----------------------------------------------------------------------------+
    | OverflowErrorReporting.WARNING  | 1301 (0x515) | NI-RFSG returns a warning when an OSP overflow occurs.                     |
    +---------------------------------+--------------+----------------------------------------------------------------------------+
    '''
    peak_envelope_power = _attributes.AttributeViReal64(1150011)
    '''Type: float

    Returns the maximum instantaneous power of the RF output signal.

    **Units**: dBm

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: - This property is valid only when the power_level_type property is set to PowerLevelType.AVERAGE.

     - The arb_digital_gain property is not included in the calculation of the peak_envelope_power property.
    '''
    peak_power_adjustment = _attributes.AttributeViReal64(1150132)
    '''Type: float

    Specifies the adjustment for the power_level property. This property is valid only when you set the power_level_type property to PowerLevelType.PEAK. The value of the peak_power_adjustment property adds to the power_level property. The peak_power_adjustment property typically specifies the peak-to-average power ratio (PAPR) of a waveform. If the PAPR is specified, the specified power level becomes the average power level of the waveform, even if the power_level_type property is set to PowerLevelType.PEAK.

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate a peak power adjustment with a waveform.

    Note: - For the PXIe-5673/5673E only, use this property to associate a peak power adjustment with a waveform.

     - For the PXIe-5645, this property is ignored if you are using the I/Q ports.
    '''
    peak_power_adjustment_inheritance = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PpaInheritance, 1150141)
    '''Type: enums.PpaInheritance

    Determines the inheritance behavior of the peak_power_adjustment property when a script inherits values from specified waveforms.

    **Default Value:** PpaInheritance.EXACT_MATCH

    **Supported Devices:** PXIe-5673/5673E

    **Related Topics**

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

    **Defined Values**:

    +----------------------------+------------------------------------------------------------+
    | Value                      | Description                                                |
    +============================+============================================================+
    | PpaInheritance.EXACT_MATCH | Errors out if different values are detected in the script. |
    +----------------------------+------------------------------------------------------------+
    | PpaInheritance.MINIMUM     | Uses the minimum value found in the script.                |
    +----------------------------+------------------------------------------------------------+
    '''
    phase_continuity_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PhaseContinuityEnabled, 1150005)
    '''Type: enums.PhaseContinuityEnabled

    Specifies whether the driver maintains phase continuity in the arbitrary waveforms. When this property is set to PhaseContinuityEnabled.ENABLE, NI-RFSG may increase the waveform size. When this property is set to PhaseContinuityEnabled.ENABLE, the frequency_tolerance property specifies the maximum allowable frequency error that can be introduced when keeping the signal phase-continuous. To set the phase_continuity_enabled property, the NI-RFSG device must be in the Configuration state. phase_continuity_enabled applies only when the generation_mode property is set to GenerationMode.ARB_WAVEFORM or GenerationMode.SCRIPT.

    PXI-5671: When using the PXI-5671 with I/Q rates less than or equal to 8.33MS/s, an input phase-continuous signal is always phase-continuous upon output, and this property has no effect.

    PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: Phase continuity is *always* enabled on this device.

    **Default Value:** PhaseContinuityEnabled.AUTO

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_

    `Arb Waveform Mode Tuning Speed Factors <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_arb_waveform_mode_tuning_speed_factors.html>`_

    **Defined Values**:

    +-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | phase_continuity_enabled Property Setting | Value     | With I/Q Rates > 8.33 MS/s.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
    +===========================================+===========+==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
    | PhaseContinuityEnabled.AUTO               | -1 (-0x1) | When the Generation Mode property is set to Arb Waveform, the arbitrary waveform may be repeated to ensure phase continuity after upconversion. This setting could cause waveform size to increase. When the Generation Mode property is set to Script, the Phase Continuity Enabled property indicates a warning condition. NI-RFSG cannot guarantee a phase-continuous output signal in Script mode. Phase continuity is automatically disabled in script mode, and the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. |
    +-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PhaseContinuityEnabled.DISABLE            | 0 (0x0)   | When the Generation Mode property is set to Arb Waveform, the arbitrary waveform is played back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained. When the Generation Mode property is set to Script, the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.                                                                                                              |
    +-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PhaseContinuityEnabled.ENABLE             | 1 (0x1)   | When the Generation Mode property is set to Arb Waveform, the arbitrary waveform may be repeated to ensure phase continuity after upconversion. Enabling this property could cause waveform size to increase. When the Generation Mode property is set to Script, the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.                                                                                                                                           |
    +-------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    phase_offset = _attributes.AttributeViReal64(1150024)
    '''Type: float

    Specifies the phase of the RF output signal. Use this property to align the phase of the RF output with the phase of the RF output of another device, as long as the two devices are phase-coherent.

    **Units**: degrees (°)

    **Default Value:** 0

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Phase Synchronization and Phase Coherency <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phase_synchronization_and_phase_coherency.html>`_
    '''
    power_level = _attributes.AttributeViReal64(1250002)
    '''Type: float

    Specifies either the average power level or peak power level of the generated RF signal, depending on the power_level_type property setting.

    The PXI-5670/5671, PXIe-5672, and PXIe-5860 must be in the Configuration state to use this property. However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E and PXIe-5830/5831/5832/5840/5841/5842 can be in the Configuration or the Generation state to use this property.

    Refer to the specifications document for your device for allowable power level settings.

    **Units**: dBm

    **Default Values:**

    PXIe-5644/5645/5646, PXIe-5673/5673E: -100

    PXI/PXIe-5650/5651/5652: -90

    PXIe-5654: -7

    PXIe-5654 with PXIe-5696: -110

    PXI-5670/5671, PXIe-5672: -145

    PXIe-5830/5831/5832/5840/5841/5842/5860: -174

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860
    **High-Level Methods**:

    - ConfigureRf

    Note: - For the PXIe-5653, this property is read-only.

     - For the PXIe-5645, this property is ignored if you are using the I/Q ports.
    '''
    power_level_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PowerLevelType, 1150043)
    '''Type: enums.PowerLevelType

    Specifies how NI-RFSG interprets the value of the power_level property. The power_level_type property also affects how waveforms are scaled.

    PXI-5670/5671: While in Script generation mode, if this property is set to PowerLevelType.AVERAGE, NI-RFSG scales each waveform so that all waveforms have the same average power. The average power level of each waveform matches the value set with the power_level property. You can disable this scaling operation by setting the power_level_type property to PowerLevelType.PEAK.

    PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: While in Script generation mode, this property must be set to PowerLevelType.PEAK.

    Converting from Average Power to Peak Power

    Typically, this property is set to PowerLevelType.AVERAGE. However, some instrument modes require this property to be set to PowerLevelType.PEAK. Use the following equations to calculate the equivalent peak power given the desired average power for your waveform:

    Where 1 is the highest possible magnitude in the waveform.

    **Default Value:**

    PXIe-5820: PowerLevelType.PEAK

    All other devices: PowerLevelType.AVERAGE

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_

    `Optimizing for Low Power Generation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/optimizing_for_low_power_generation.html>`_

    **Defined Values**:

    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Value                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    +========================+====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
    | PowerLevelType.AVERAGE | Indicates the desired power averaged in time. The driver maximizes the dynamic range by scaling the I/Q waveform so that its peak magnitude is equal to one. If your write more than one waveform, NI-RFSG scales each waveform without preserving the power level ratio between the waveforms. This value is not valid for the PXIe-5820.                                                                                                                                                                                                                                                                                                                                                                                                                         |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | PowerLevelType.PEAK    | Indicates the maximum power level of the RF signal averaged over one period of the RF carrier frequency (the peak envelope power). This setting requires that the magnitude of the I/Q waveform must always be less than or equal to one. When using peak power, the power level of the RF signal matches the specified power level at moments when the magnitude of the I/Q waveform equals one. If you write more than one waveform, the relative scaling between waveforms is preserved. In peak power mode, waveforms are scaled according to the arb_waveform_software_scaling_factor property. You can use the peak_power_adjustment property in conjunction with the power_level property when the power_level_type property is set to PowerLevelType.PEAK. |
    +------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    '''
    pulse_modulation_active_level = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerDigitalLevelActiveLevel, 1150307)
    '''Type: enums.ScriptTriggerDigitalLevelActiveLevel

    Specifies the active level of the pulse modulation signal when pulse modulation is enabled. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** ScriptTriggerDigitalLevelActiveLevel.HIGH

    **Supported Devices:**  PXIe-5842

    **Defined Values**:

    +-------------------------------------------+---------------+--------------------------------------------------+
    | Name                                      | Value         | Description                                      |
    +===========================================+===============+==================================================+
    | ScriptTriggerDigitalLevelActiveLevel.HIGH | 9000 (0x2328) | Trigger when the digital trigger signal is high. |
    +-------------------------------------------+---------------+--------------------------------------------------+
    | ScriptTriggerDigitalLevelActiveLevel.LOW  | 9001 (0x2329) | Trigger when the digital trigger signal is low.  |
    +-------------------------------------------+---------------+--------------------------------------------------+
    '''
    pulse_modulation_enabled = _attributes.AttributeViBoolean(1250051)
    '''Type: bool

    Enables or disables pulse modulation.

    PXIe-5654/5654 with PXIe-5696: If this property is enabled and the signal at the PULSEIN front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled.

    PXIe-5673/5673E: If this property is enabled and the signal at the PLSMOD front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled.

    PXIe-5842: If this property is enabled and the signal at the PULSE IN front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled. This behavior can be modified by setting pulse modulation active level.

    **Default Value:** False

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E

    **Related Topics**

    `Pulse Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/pulse_modulation.html>`_

    **Defined Values**:

    +-------+----------------------------+
    | Value | Description                |
    +=======+============================+
    | True  | Enables pulse modulation.  |
    +-------+----------------------------+
    | False | Disables pulse modulation. |
    +-------+----------------------------+
    '''
    pulse_modulation_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.PulseModulationMode, 1150190)
    '''Type: enums.PulseModulationMode

    PXIe-5654/5654 with PXIe-5696: Specifies the pulse modulation mode to use.

    PXIe-5842: This property allows you to choose a tradeoff between switching speed and On/Off Ratio when using pulse modulation. Refer to the product specifications document for the switching characteristics of each mode. This property is settable while the device is generating, but some output pulses may be dropped.

    **Default Value:** PulseModulationMode.ANALOG

    **Supported Devices:** PXIe-5842/5654/5654 with PXIe-5696

    **Defined Values**:

    +---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | Value                                             | Description                                                                                                                                 |
    +===================================================+=============================================================================================================================================+
    | PulseModulationMode.OPTIMAL_MATCH                 | Provides for a more optimal power output match for the device during the off cycle of the pulse mode operation. Not supported on PXIe-5842. |
    +---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | NIRFSG_VAL_PULSE_MODULATION_ANALOG_HIGH_ISOLATION | Allows for the best on/off power ratio of the pulsed signal.                                                                                |
    +---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | NIRFSG_VAL_PULSE_MODULATION_ANALOG                | Analog switch blanking. Balance between switching speed and on/off power ratio of the pulsed signal.                                        |
    +---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
    | NIRFSG_VAL_PULSE_MODULATION_DIGITAL               | Digital only modulation. Provides the best on/off switching speed of the pulsed signal at the cost of signal isolation.                     |
    +---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    pulse_modulation_source = _attributes.AttributeViString(1150308)
    '''Type: str

    Specifies the source of the pulse modulation signal. When Pulse In in used, the pulse modulation is applied with the lowest latency and jitter, but is not aligned to any particular waveform sample. When a marker is used, the RF pulse is aligned to a specific sample in the arbitrary waveform. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** PulseIn

    **Supported Devices:**  PXIe-5842

     **Possible Values**:

    +----------------+----------------------------------------------------------------------------------------------+
    | Possible Value | Description                                                                                  |
    +================+==============================================================================================+
    | "PulseIn"      | The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842. |
    +----------------+----------------------------------------------------------------------------------------------+
    | "Marker0"      | The trigger is received from the Marker 0.                                                   |
    +----------------+----------------------------------------------------------------------------------------------+
    | "Marker1"      | The trigger is received from the Marker 1.                                                   |
    +----------------+----------------------------------------------------------------------------------------------+
    | "Marker2"      | The trigger is received from the Marker 2.                                                   |
    +----------------+----------------------------------------------------------------------------------------------+
    | "Marker3"      | The trigger is received from the Marker 3.                                                   |
    +----------------+----------------------------------------------------------------------------------------------+
    '''
    pxi_chassis_clk10_source = _attributes.AttributeViString(1150004)
    '''Type: str

    Specifies the clock source for driving the PXI 10 MHz backplane Reference Clock. This property is configurable if the PXI-5610 upconverter module is installed in *only* Slot 2 of a PXI chassis. To set this property, the NI-RFSG device must be in the Configuration state.

    **Possible Values**:

    Possible Value: Description

    "" :Do not drive the PXI_CLK10 signal.

    "OnboardClock" :Uses the highly stable oven-controlled onboard Reference Clock to drive the PXI_CLK signal.

    "RefIn" :Uses the clock present at the front panel REF IN connector to drive the PXI_CLK signal.

    **Default Value:** ""

    **Supported Devices:** PXI-5610, PXI-5670/5671

    **Related Topics**

    `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

    `System Reference Clock <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_clk10.html>`_

    **High-Level Methods**:

    - configure_pxi_chassis_clk10


    Only certain combinations of this property and the ref_clock_source property are valid, as shown in the following table.

    +----------------------------------+--------------------------+
    | pxi_chassis_clk10_source Setting | ref_clock_source Setting |
    +==================================+==========================+
    | "", OnboardClock                 | OnboardClock             |
    +----------------------------------+--------------------------+
    | "", RefIn                        | RefIn                    |
    +----------------------------------+--------------------------+
    | "", RefIn                        | PXI_CLK                  |
    +----------------------------------+--------------------------+
    '''
    query_instrument_status = _attributes.AttributeViBoolean(1050003)
    '''Type: bool

    Specifies whether NI-RFSG queries the NI-RFSG device status after each operation. Querying the device status is useful for debugging. After you validate your program, set this property to False to disable status checking and maximize performance.

    NI-RFSG can choose to ignore status checking for particular properties, regardless of the setting of this property. Use the __init__ method to override the default value.

    **Default Value:** False

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +-------+-------------------------------------------------------------+
    | Value | Description                                                 |
    +=======+=============================================================+
    | True  | NI-RFSG queries the instrument status after each operation. |
    +-------+-------------------------------------------------------------+
    | False | NI-RFSG does not query the instrument status.               |
    +-------+-------------------------------------------------------------+
    '''
    range_check = _attributes.AttributeViBoolean(1050002)
    '''Type: bool

    Specifies whether to validate property values and method parameters. Range checking parameters is very useful for debugging. After you validate your program, set this property to False to disable range checking and maximize performance. NI-RFSG can choose to ignore range checking for particular properties, regardless of the setting of this property. Use the __init__ method to override the default value.

    **Default Value:** True

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +-------+-------------------------+
    | Value | Description             |
    +=======+=========================+
    | True  | Enable range checking.  |
    +-------+-------------------------+
    | False | Disable range checking. |
    +-------+-------------------------+
    '''
    record_coercions = _attributes.AttributeViBoolean(1050006)
    '''Type: bool

    Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties.

    **Default Value:** False

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +-------+---------------------------------------------------+
    | Value | Description                                       |
    +=======+===================================================+
    | True  | The IVI engine keeps a list of coercions.         |
    +-------+---------------------------------------------------+
    | False | The IVI engine does not keep a list of coercions. |
    +-------+---------------------------------------------------+

    Note: Enabling record value coercions is not supported.
    '''
    ref_clock_rate = _attributes.AttributeEnum(_attributes.AttributeViReal64, enums.ReferenceClockRate, 1250322)
    '''Type: enums.ReferenceClockRate

    Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector. This property is only valid when the ref_clock_source property is set to ClkIn, RefIn, or RefIn2

    To set this property, the NI-RFSG device must be in the Configuration state. If you are using the PXIe-5654/5654 with PXIe-5696, the NI-RFSG device must be in the Committed state to read this property. When you read this property, it returns the frequency the device is locked to during the Committed state.

    If you set this property to ReferenceClockRate.AUTO, NI-RFSG uses the default Reference Clock rate for the device or automatically detects the Reference Clock rate if automatic detection is supported by the device.

    **Valid Values:**

    PXIe-5654/5654 with PXIe-5696: Values between 1MHz to 20MHz in 1MHz steps are supported in addition to the ReferenceClockRate.AUTO and ReferenceClockRate.CLOCK_RATE_10_MEGAHERTZ values.

    PXIe-5841 with PXIe-5655, PXIe-5842: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz

    y, where

    y is 4, 8, 16, 24, 25, or 32.

    PXIe-5860: 10 MHz, 100 MHz

    **Units**: hertz (Hz)

    **Default Value:** ReferenceClockRate.AUTO

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

    **High-Level Methods**:

    - configure_ref_clock

    **Defined Values**:

    +--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | Value                                      | Description                                                                                                                       |
    +============================================+===================================================================================================================================+
    | ReferenceClockRate.AUTO                    | Uses the default Reference Clock rate for the device or automatically detects the Reference Clock rate if the device supports it. |
    +--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
    | ReferenceClockRate.CLOCK_RATE_10_MEGAHERTZ | Uses a 10 MHz Reference Clock rate.                                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

    Note: Automatic detection of the Reference Clock rate is supported on only the PXIe-5654/5654 with PXIe-5696. For all other supported devices, NI-RFSG uses the default Reference Clock rate of 10MHz.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    ref_clock_source = _attributes.AttributeViString(1150001)
    '''Type: str

    Specifies the Reference Clock source. To set this property, the NI-RFSG device must be in the Configuration state. Only certain combinations of this property and the pxi_chassis_clk10_source property are valid, as shown in the following table.

    **Default Value:** OnboardClock

    **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

    **High-Level Methods**:

    - configure_ref_clock

    **Possible Values**:

    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Possible Value  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    +=================+=========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
    | "OnboardClock"  | Uses the onboard Reference Clock as the clock source. **PXIe-5830/5831** —For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. ** PXIe-5831/5832 with PXIe-5653** —Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. **PXIe-5841 with PXIe-5655** —Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector.                                                                                                                                                                                                                                                                                                      |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "ClkIn"         | Uses the clock signal present at the front panel CLK IN connector as the Reference Clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "RefIn"         | Uses the clock signal present at the front panel REF IN connector as the Reference Clock source. **PXIe-5830/5831** —For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831/5832, lock the external signal to the PXIe-3622 REF IN connector. **PXIe-5831/5832 with PXIe-5653** —Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. **PXIe-5841 with PXIe-5655** —Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_CLK"       | Uses the PXI_CLK signal, which is present on the PXI backplane, as the Reference Clock source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "RefIn2"        | This value is not valid on any supported devices.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | "PXI_ClkMaster" | This value is valid on only the PXIe-5831/5832 with PXIe-5653. **PXIe-5831/5832 with PXIe-5653** —NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_CLK as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
    +-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: The PXI-5670/5671 and PXIe-5672 devices also allow you to drive the PXI 10 MHz backplane clock on PXI chassis *only* using the pxi_chassis_clk10_source property.
    '''
    ref_pll_bandwidth = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ReferencePllBandwidth, 1150133)
    '''Type: enums.ReferencePllBandwidth

    Configures the loop bandwidth of the reference PLL.

    **Default Value:** ReferencePllBandwidth.NARROW

    **Supported Devices:** PXIe-5653

    **Related Topics**

    `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_

    **Defined Values**:

    +------------------------------+--------------------------------------------------------+
    | Value                        | Description                                            |
    +==============================+========================================================+
    | ReferencePllBandwidth.NARROW | Uses the narrowest loop bandwidth setting for the PLL. |
    +------------------------------+--------------------------------------------------------+
    | ReferencePllBandwidth.MEDIUM | Uses the medium loop bandwidth setting for the PLL.    |
    +------------------------------+--------------------------------------------------------+
    | ReferencePllBandwidth.WIDE   | Uses the widest loop bandwidth setting for the PLL.    |
    +------------------------------+--------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    relative_delay = _attributes.AttributeViReal64(1150220)
    '''Type: float

    Specifies the delay, in seconds, to apply to the I/Q waveform.

    Relative delay allows for delaying the generated signal from one device relative to the generated signal of another device after those devices have been synchronized. You can achieve a negative relative delay by delaying both synchronized devices by the same value (1 μs) before generation begins and then changing the relative delay to a smaller amount than the initial value on only one of the devices.

    To set this property, the NI-RFSG device must be in the Configuration or Generation state.

    **Units:** Seconds

    **Valid Values:**

    PXIe-PXIe-5820/5830/5831/5832/5840/5841: 0 μs to 3.2 μs

    PXIe-5842: 0 μs to 6.5 μs

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `NI-TClk Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_tclk_help.html>`_

    Note: - To obtain a negative relative delay when synchronizing the PXIe-5840/5841 with a module that does not support this property, use the NITCLK_ATTR_SAMPLE_CLOCK_DELAY property.

     - The resolution of this property is a method of the I/Q sample period at 15E(-6) of the sample period but not worse than one Sample Clock period.
    '''
    rf_blanking_source = _attributes.AttributeViString(1150162)
    '''Type: str

    Specifies the Marker Event at which RF blanking occurs. RF blanking quickly attenuates the RF OUT signal. Use Marker Events to toggle the state of RF blanking. The RF Output always starts in the unblanked state.

    To set this property, the NI-RFSG device must be in the Configuration state.

    You can specify Marker Events by using scripts to trigger blanking at a certain point in a waveform. For example, if you set this property to marker0 str}, and marker0 occurs on samples 1,000 and 2,000 of a script, then the RF Output will be blanked (attenuated) between samples 1,000 and 2,000.

    PXIe-5645: This property is ignored if you are using the I/Q ports.

    PXIe-5840/5841: RF blanking does not occur for frequencies below 120MHz.

    For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking properties. Alternatively, you can call reset_with_options or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    **Valid Values**:

    +-----------+---------------------------------+
    | Value     | Description                     |
    +===========+=================================+
    | ""        | RF blanking is disabled.        |
    +-----------+---------------------------------+
    | "Marker0" | RF blanking is tied to marker0. |
    +-----------+---------------------------------+
    | "Marker1" | RF blanking is tied to marker1. |
    +-----------+---------------------------------+
    | "Marker2" | RF blanking is tied to marker2. |
    +-----------+---------------------------------+
    | "Marker3" | RF blanking is tied to marker3. |
    +-----------+---------------------------------+

    Note: The shortest supported blanking interval is eight microseconds.
    '''
    rf_in_lo_export_enabled = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RFInLoExportEnabled, 1150243)
    '''Type: enums.RFInLoExportEnabled

    Specifies whether to enable the RF IN LO OUT terminal on the PXIe-5840/5841.

    Set this property to RFInLoExportEnabled.ENABLE to export the LO signal from the RF IN LO OUT terminal.

    When this property is enabled, if the lo_source property is set to LO_In and you do not set the lo_frequency or upconverter_center_frequency properties, NI-RFSG rounds the LO frequency to approximately an LO step size as if the source was OnboardClock. This ensures that when you configure NI-RFSA and NI-RFSG with compatible settings that result in the same LO frequency, the rounding also is compatible.

    **Default Value:** RFInLoExportEnabled.UNSPECIFIED

    **Supported Devices**: PXIe-5840/5841/5842

    **Defined Values**:

    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | Value                           | Description                                                                                                                             |
    +=================================+=========================================================================================================================================+
    | RFInLoExportEnabled.DISABLE     | The RF In local oscillator signal is not present at the front panel LO OUT connector.                                                   |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | RFInLoExportEnabled.ENABLE      | The RF In local oscillator signal is present at the front panel LO OUT connector.                                                       |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
    | RFInLoExportEnabled.UNSPECIFIED | The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it. |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    script_trigger_terminal_name = _attributes.AttributeViString(1150116)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Default Values**:

    PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/ScriptTrigger *X*, where *AWGName* is the name of your associated AWG module in MAX and *X* is Script Trigger 0 through 3.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/ScriptTrigger *X*, where *BasebandModule* is the name of the baseband module of your device in MAX and *X* is Script Trigger 0 through 3.

    PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/ScriptTrigger *X*, where *ModuleName* is the name of your device in MAX and *X* is Script Trigger 0 through 3.

    PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/ScriptTrigger *X*, where *ModuleName* is the name of your device in MAX, *ChannelNumber* is the channel number (0 or 1), and *X* is Script Trigger 0 through 3.

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

    **High-Level Methods**:

    - get_terminal_name

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].script_trigger_terminal_name`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.script_trigger_terminal_name`
    '''
    script_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerType, 1150019)
    '''Type: enums.ScriptTriggerType

    Specifies the Script Trigger type. Depending upon the value of this property, more properties may be needed to fully configure the trigger. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** ScriptTriggerType.NONE

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_

    **High-Level Methods**:

    - configure_digital_edge_script_trigger

    **Defined Values**:

    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Value                           | Description                                                                                                                                                                                                                                                           |
    +=================================+=======================================================================================================================================================================================================================================================================+
    | ScriptTriggerType.NONE          | No trigger is configured. Signal generation starts immediately.                                                                                                                                                                                                       |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ScriptTriggerType.DIGITAL_EDGE  | The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the digital_edge_start_trigger_source property, and the active edge is specified with the digital_edge_start_trigger_edge property.              |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ScriptTriggerType.DIGITAL_LEVEL | The data operation does not start until the digital level is detected. The source of the digital level is specified in the digital_level_script_trigger_source property, and the active level is specified in the digital_level_script_trigger_active_level property. |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | ScriptTriggerType.SOFTWARE      | The data operation does not start until a software trigger occurs. You can create a software event by calling the send_software_edge_trigger method.                                                                                                                  |
    +---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].script_trigger_type`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.script_trigger_type`
    '''
    selected_path = _attributes.AttributeViString(1150311)
    '''Type: str

    Specifies which path to configure to generate a signal.
    '''
    selected_ports = _attributes.AttributeViString(1150241)
    '''Type: str

    Specifies the port to configure.

    **Valid Values**:

    PXIe-5644/5645/5646, PXIe-5820/5840/5841: "" (empty string)

    PXIe-5830: if0, if1

    PXIe-5831/5832: if0, if1, rf*0-1*/port*x*, where *0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and *x* is the port number on the mmRH-5582 front panel.

    **Default Value:**

    PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string)

    PXIe-5830/5831/5832: if0

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    available_ports

    Note: When using RF list mode, ports cannot be shared with NI-RFSA.
    '''
    selected_script = _attributes.AttributeViString(1150023)
    '''Type: str

    Specifies the script in onboard memory to generate upon calling the _initiate method when the generation_mode property is set to GenerationMode.SCRIPT.

    The selected_script property is ignored when the generation_mode property is set to GenerationMode.ARB_WAVEFORM or GenerationMode.CW. To set the selected_script property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

    `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_
    '''
    self_calibration_temperature = _attributes.AttributeViReal64(1150136)
    '''Type: float

    Indicates, in degrees Celsius, the temperature of the device at the time of the last self calibration.

    **Supported Devices:** PXIe-5644/5645/5646
    '''
    serial_number = _attributes.AttributeViString(1150026)
    '''Type: str

    Returns the serial number of the RF module. If the NI-RFSG session is controlling multiple modules, this property returns the serial number of the primary RF module.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    signal_bandwidth = _attributes.AttributeViReal64(1150007)
    '''Type: float

    Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8× iq_rate).

    NI-RFSG defines *signal bandwidth* as twice the maximum baseband signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the signal bandwidth is simply the baseband signal's minimum frequency subtracted from its maximum frequency, or *f* :sub:`max` - *f* :sub:`min` .

    This property applies only when the generation_mode property is set to GenerationMode.ARB_WAVEFORM or GenerationMode.SCRIPT, except for when using the PXIe-5830/5831/5832/5840/5841, which supports setting this property in all supported generation modes. To set the signal_bandwidth property, the NI-RFSG device must be in the Configuration state.

    PXI-5670/5671, PXIe-5672: Based on your signal bandwidth, NI-RFSG determines whether to configure the upconverter center frequency in increments of 1MHz or 5MHz. Failure to configure this property may result in the signal being placed outside the upconverter passband.

    PXIe-5644/5645/5646, PXIe-5673/5673E: This property is used only for error-checking purposes. Otherwise, this property is ignored.

    PXIe-5820/5830/5831/5832/5840/5841/5842/5860: Based on your signal bandwidth, NI-RFSG decides the equalized bandwidth. If this property is not set, NI-RFSG uses the maximum available signal bandwidth. For the PXIe-5840/5841, the maximum allowed signal bandwidth depends on the upconverter center frequency. Refer to the specifications document for your device for more information about signal bandwidth. The device specifications depend on the signal bandwidth.

    **Units**: hertz (Hz)

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_

    `Frequency Tuning Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.html>`_

    `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Returns whether NI-RFSG simulates I/O operations. This property is useful for debugging applications without using hardware. After a session is opened, you cannot change the simulation state. Use the __init__ method to enable simulation.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +-------+-------------------------+
    | Value | Description             |
    +=======+=========================+
    | True  | Simulation is enabled.  |
    +-------+-------------------------+
    | False | Simulation is disabled. |
    +-------+-------------------------+
    '''
    specific_driver_class_spec_major_version = _attributes.AttributeViInt32(1050515)
    '''Type: int

    Returns the major version number of the class specification with which NI-RFSG is compliant.

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_class_spec_minor_version = _attributes.AttributeViInt32(1050516)
    '''Type: int

    Returns the minor version number of the class specification with which NI-RFSG is compliant.

    **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    Returns a string that contains a brief description of NI-RFSG. This property returns

    National Instruments RF Signal Generator Instrument Driver.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_prefix = _attributes.AttributeViString(1050302)
    '''Type: str

    Returns a string that contains the prefix for NI-RFSG. The name of each user-callable method in NI-RFSG starts with this prefix. This property returns

    niRFSG.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    Returns a string that contains additional version information about NI-RFSG. For example, NI-RFSG can return

    Driver: NI-RFSG14.5.0, Compiler: MSVC9.00, Components: IVI Engine4.00, VISA-Spec4.00 as the value of this property.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    Returns a string that contains the name of the vendor that supplies NI-RFSG. This property returns

    National Instruments.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    started_event_terminal_name = _attributes.AttributeViString(1150112)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Default Values**:

    PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/StartedEvent, where *AWGName* is the name of your associated AWG module in MAX.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/StartedEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.

    PXIe-5820/5840/5841: /*ModuleName*/ao/0/StartedEvent, where *ModuleName* is the name of your device in MAX.

    PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/StartedEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    start_trigger_terminal_name = _attributes.AttributeViString(1150114)
    '''Type: str

    Returns the name of the fully qualified signal name as a string.

    **Default Values**:

    PXIe-5654/5654 with PXIe-5696: /*ModuleName*/StartTrigger, where *ModuleName* is the name of your device in MAX.

    PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/StartTrigger, where *ModuleName* is the name of your associated AWG module in MAX.

    PXIe-5830/5831/5832: /*BasebandModule*/ao/0/StartTrigger, where *BasebandModule* is the name of the baseband module of your device in MAX.

    PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/StartTrigger, where *ModuleName* is the name of your device in MAX.

    PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/StartTrigger, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

    **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

    **High-Level Methods**:

    - get_terminal_name
    '''
    start_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.StartTriggerType, 1250458)
    '''Type: enums.StartTriggerType

    Specifies the Start Trigger type. Depending upon the value of this property, more properties may be needed to fully configure the trigger. To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** StartTriggerType.NONE

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_

    **High-Level Methods**:

    - configure_digital_edge_start_trigger
    - configure_software_start_trigger
    - disable_start_trigger

    **Defined Values**:

    +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Value                         | Description                                                                                                                                                                                                                                            |
    +===============================+========================================================================================================================================================================================================================================================+
    | StartTriggerType.NONE         | No trigger is configured.                                                                                                                                                                                                                              |
    +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | StartTriggerType.DIGITAL_EDGE | The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the digital_edge_start_trigger_source property, and the active edge is specified in the digital_edge_start_trigger_edge property. |
    +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | StartTriggerType.SOFTWARE     | The data operation does not start until a software event occurs. You may create a software trigger by calling the send_software_edge_trigger method.                                                                                                   |
    +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    streaming_enabled = _attributes.AttributeViBoolean(1150045)
    '''Type: bool

    Enables and disables continuous streaming of waveform data.

    **Default Value:** False

    **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

    **Defined Values**:

    +-------+------------------------+
    | Value | Description            |
    +=======+========================+
    | True  | Streaming is enabled.  |
    +-------+------------------------+
    | False | Streaming is disabled. |
    +-------+------------------------+
    '''
    streaming_space_available_in_waveform = _attributes.AttributeViInt64(1150047)
    '''Type: int

    Indicates the space available, in samples, in the streaming waveform for writing new data. For optimal performance, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform. This waveform size ensures that writes do not have to wrap around from the end to the beginning of the waveform buffer.

    To read this property, the NI-RFSG device must be in the Committed state.

    **Units**: samples

    **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_
    '''
    streaming_waveform_name = _attributes.AttributeViString(1150046)
    '''Type: str

    Specifies the name of the waveform used to continually stream data during generation.

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

    `Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_
    '''
    streaming_write_timeout = _attributes.AttributeViReal64TimeDeltaSeconds(1150140)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Indicates the maximum amount of time allowed to complete a streaming write operation.

    **Default Value:** 10.0seconds

    **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

    `Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    Returns a string that contains a model code of the NI-RFSG device. For drivers that support more than one device, this property contains a comma-separated list of supported devices.

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    sync_sample_clock_dist_line = _attributes.AttributeViString(1150181)
    '''Type: str

    Specifies which external trigger line distributes the Sample Clock sync signal. When synchronizing the Sample Clock between multiple devices, configure all devices to use the same Sample Clock sync distribution line.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5646

    **Related Topics**

    `Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/synchronization_rfsa_g.html>`_—Refer to this topic for more information about PXIe-5646 device synchronization.
    '''
    sync_sample_clock_master = _attributes.AttributeViBoolean(1150180)
    '''Type: bool

    Specifies whether the device is the master device when synchronizing the Sample Clock between multiple devices. The master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line.

    When synchronizing the Sample Clock, one device must always be designated as the master. The master device actively drives the Sample Clock sync distribution line.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXIe-5646

    **Related Topics**

    `Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/synchronization_rfsa_g.html>`_—Refer to this topic for more information about PXIe-5646 device synchronization.

    **Defined Values**:

    +-------+---------------------------------------------------------------------+
    | Value | Description                                                         |
    +=======+=====================================================================+
    | True  | The device is the master device for synchronizing the Sample Clock. |
    +-------+---------------------------------------------------------------------+
    | False | The device is not the master for synchronizing the Sample Clock.    |
    +-------+---------------------------------------------------------------------+
    '''
    sync_script_trigger_dist_line = _attributes.AttributeViString(1150143)
    '''Type: str

    Specifies which external trigger line distributes the synchronized Script Trigger signal. When synchronizing the Script Trigger, configure all devices to use the same Script Trigger distribution line.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5644/5645/5646

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `Synchronizing Sample Clock and Sampled Reference Clock Signals <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sample_clock_sync.html>`_

    Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.
    '''
    sync_script_trigger_master = _attributes.AttributeViBoolean(1150142)
    '''Type: bool

    Specifies whether the device is the master device when synchronizing the Script Trigger.

    The master device distributes the synchronized Script Trigger to all devices in the system through the Script Trigger distribution line.

    When synchronizing the Script trigger, one device must always be designated as the master. The master device actively drives the Script Trigger distribution line. For slave devices, set the script_trigger_type property to digital edge, and set the digital_edge_script_trigger_source property to sync_script.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXIe-5644/5645/5646

    **Related Topics**

    `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

    `Synchronizing Sample Clock and Sampled Reference Clock Signals <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sample_clock_sync.html>`_

    Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.

    **Defined Values**:

    +-------+-----------------------------------------------------------------------+
    | Value | Description                                                           |
    +=======+=======================================================================+
    | True  | The device is the master device for synchronizing the Script Trigger. |
    +-------+-----------------------------------------------------------------------+
    | False | The device is not the master for synchronizing the Script Trigger.    |
    +-------+-----------------------------------------------------------------------+
    '''
    sync_start_trigger_dist_line = _attributes.AttributeViString(1150156)
    '''Type: str

    Specifies which external trigger line distributes the synchronized Start Trigger signal. When synchronizing the Start Trigger, configure all devices to use the same Start Trigger distribution line.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

    **Default Value:** "" (empty string)

    **Supported Devices:** PXIe-5644/5645/5646

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.
    '''
    sync_start_trigger_master = _attributes.AttributeViBoolean(1150155)
    '''Type: bool

    Specifies whether the device is the master device when synchronizing the Start Trigger. The master device distributes the synchronized Start Trigger to all devices in the system through the Start Trigger distribution line.

    When synchronizing the Start Trigger, one device must always be designated as the master. The master device actively drives the Start Trigger distribution line. For slave devices, set the start_trigger_type property to digital edge, and set the digital_edge_start_trigger_source property to sync_script.

    To set this property, the NI-RFSG device must be in the Configuration state.

    **Default Value:** False

    **Supported Devices:** PXIe-5644/5645/5646

    **Related Topics**

    `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

    Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.

    **Defined Values**:

    +-------+----------------------------------------------------------------------+
    | Value | Description                                                          |
    +=======+======================================================================+
    | True  | The device is the master device for synchronizing the Start Trigger. |
    +-------+----------------------------------------------------------------------+
    | False | The device is not the master for synchronizing the Start Trigger.    |
    +-------+----------------------------------------------------------------------+
    '''
    temperature_read_interval = _attributes.AttributeViReal64TimeDeltaSeconds(1150212)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the minimum time between temperature sensor readings.

    **Units:** Seconds

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860
    '''
    thermal_correction_headroom_range = _attributes.AttributeViReal64(1150258)
    '''Type: float

    Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the device_temperature property.

    For example, if this property is set to 5.0, and the device is self-calibrated at 35°C, then you can expect to run the device from 30°C to 40°C with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance or DSP overflows.

    **Units:** degrees Celsius (°C)

    **Default Value**:

    **PXIe-5830/5831/5832/5842/5860**: 5

    **PXIe-5840/5841**: 10

    **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860
    '''
    thermal_correction_temperature_resolution = _attributes.AttributeViReal64(1150244)
    '''Type: float

    Specifies the temperature change, in degrees Celsius, that is required before NI-RFSG recalculates the thermal correction settings when entering the Generation state.

    **Units:** degrees Celsius (°C)

    **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Default Values:**

    PXIe-5830/5831/5832/5842/5860: 0.2

    PXIe-5840/5841: 1.0
    '''
    timer_event_interval = _attributes.AttributeViReal64TimeDeltaSeconds(1150100)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the time before the timer emits an event after the task is started and specifies the time interval between Timer events after the first event.

    **Units**: seconds (s)

    **Default Value:** 0

    **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

    Note: For the PXIe-5820/5840/5841/5842/5860, this property must be set for the timer to start. If you do not set this property, the timer is disabled.
    '''
    upconverter_center_frequency = _attributes.AttributeViReal64(1154098)
    '''Type: float

    Indicates the center frequency of the passband containing the upconverted RF signal. Writing a value to this property while using the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, or PXIe-5820/5840/5841 device enables in-band retuning. In-band retuning increases the speed of frequency sweeps by reducing the amount of upconverter retunes.

    **Units**: hertz (Hz)

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

    Note: - This property is read/write on the PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842, and is read-only on the PXI-5670/5671.

     - Resetting this property disables in-band retuning, however, for the PXIe-5820, in-band retuning is always enabled.

     - For the PXIe-5820, the only valid value for this property is 0.

     - Setting this property while the PXIe-5644/5645/5646, PXIe-5673/5673E, or PXIe-5820/5830/5831/5832/5840/5841/5842 device is generating has no effect until a dynamic property is set.
    '''
    upconverter_frequency_offset = _attributes.AttributeViReal64(1150160)
    '''Type: float

    This property offsets the upconverter_center_frequency from the RF frequency. Use this property to keep the local oscillator (LO) leakage at a determined offset from the RF signal.

    **Valid Values:**

    PXIe-5644/5645: -42MHz to +42MHz

    PXIe-5646: -100MHz to +100MHz

    PXIe-5830/5831/5832/5840/5841: -500MHz to +500MHz

    PXI-5842 (500 MHz bandwidth option): -250MHz to +250MHz

    PXI-5842 (1 GHz bandwidth option): -500MHz to +500MHz

    PXI-5842 (2 GHz bandwidth option): -1GHz to +1GHz

    PXIe-5842 (4 GHz bandwidth option) using the Standard personality: -1GHz to +1GHz

    PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality: -2GHz to +2GHz

    **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

    **Related Topics**

    `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

    Note: - You cannot set the upconverter_center_frequency property or the arb_carrier_frequency property at the same time as the upconverter_frequency_offset property.

     - Resetting this property disables the upconverter frequency offset.
    '''
    upconverter_frequency_offset_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.UpconverterFrequencyOffsetMode, 1150248)
    '''Type: enums.UpconverterFrequencyOffsetMode

    Specifies whether to allow NI-RFSG to select the upconverter frequency offset. You can either set an offset yourself or let NI-RFSG select one for you.

    Placing the upconverter center frequency outside the bandwidth of your waveform can help avoid issues such as LO leakage.

    To set an offset yourself, set this property to UpconverterFrequencyOffsetMode.AUTO or UpconverterFrequencyOffsetMode.USER_DEFINED, and set either the upconverter_center_frequency or the upconverter_frequency_offset property.

    To allow NI-RFSG to automatically select the upconverter frequency offset, set this property to UpconverterFrequencyOffsetMode.AUTO or UpconverterFrequencyOffsetMode.ENABLE and set the signal_bandwidth to describe the bandwidth of your waveform. The signal bandwidth must be no greater than half the value of the device_instantaneous_bandwidth property, minus a device-specific guard band. Do not set the upconverter_center_frequency or upconverter_frequency_offset properties. If all conditions are met, NI-RFSG places the upconverter center frequency outside the signal bandwidth. Set this property to UpconverterFrequencyOffsetMode.ENABLE if you want to receive an error any time NI-RFSG is unable to apply automatic offset.

    When you set an offset yourself or do not use an offset, the reference frequency for gain is near the upconverter center frequency, and upconverter_frequency_offset_mode returns UpconverterFrequencyOffsetMode.USER_DEFINED. When NI-RFSG automatically sets an offset, the reference frequency for gain is near the frequency and upconverter_frequency_offset_mode returns UpconverterFrequencyOffsetMode.ENABLE.

    **Default Value:** UpconverterFrequencyOffsetMode.AUTO

    **Supported Devices**: PXIe-5830/5831/5832/5841/5842

    **Related Topics**

    `PXIe-5830 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_

    `PXIe-5831/5832 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_

    `PXIe-5841 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_

    **Defined Values**:

    +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Value                                       | Description                                                                                                                                                                                                                                                            |
    +=============================================+========================================================================================================================================================================================================================================================================+
    | UpconverterFrequencyOffsetMode.ENABLE       | NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the signal_bandwidth property has been set and can be avoided. NI-RFSG returns an error if the signal_bandwidth property has not been set, or if the signal bandwidth is too large. |
    +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | UpconverterFrequencyOffsetMode.AUTO         | NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the signal_bandwidth property has been set and can be avoided.                                                                                                                      |
    +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | UpconverterFrequencyOffsetMode.USER_DEFINED | NI-RFSG uses the offset that you specified with the upconverter_frequency_offset or upconverter_center_frequency properties.                                                                                                                                           |
    +---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    Note: Below 120 MHz, the PXIe-5841 does not use an LO and UpconverterFrequencyOffsetMode.ENABLE is unavailable. Refer to the *PXIe-5841 Automatic Frequency Offset* topic for more information about using an automatic offset with an external LO.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    upconverter_gain = _attributes.AttributeViReal64(1154097)
    '''Type: float

    Specifies the gain the upconverter applies to the signal.

    **Units**: dB

    **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note: This property is read/write on the PXI-5610 and PXIe-5611 and is read-only on the PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.
    '''
    waveform_iq_rate = _attributes.AttributeViReal64(1150263)
    '''Type: float

    Specifies the I/Q rate of the waveform. To set this property, the NI-RFSG device must be in the Configuration state.

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

    `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate an I/Q rate with a waveform.

    `Digital Upconverter <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/duc.html>`_

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_iq_rate`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_iq_rate`
    '''
    waveform_papr = _attributes.AttributeViReal64(1150266)
    '''Type: float

    Specifies the peak-to-average power ratio (PAPR).

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_papr`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_papr`
    '''
    waveform_rf_blanking = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.RFBlanking, 1150278)
    '''Type: enums.RFBlanking

    **Defined Values**:

    Name (Value): Description

    RFBlanking.DISABLE (0):	RF blanking is disabled.

    RFBlanking.ENABLE (1):	RF blanking is enabled.

    **Default Value:** RFBlanking.DISABLE

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

    **Related Topics**

    `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

    Enables or disables RF blanking.

    +-----------------------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------+
    | rf_blanking_source                                                                | waveform_rf_blanking | Behaviour                                                                                                 |
    +===================================================================================+======================+===========================================================================================================+
    | "" (empty string)                                                                 | RFBlanking.DISABLE   | No blanking performed.                                                                                    |
    +-----------------------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------+
    | "" (empty string)                                                                 | RFBlanking.ENABLE    | Blanking performed based on burst start and stop values and blanking source set to private marker.        |
    +-----------------------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------+
    | NIRFSG_VAL_MARKER0, NIRFSG_VAL_MARKER1, NIRFSG_VAL_MARKER2, or NIRFSG_VAL_MARKER3 | RFBlanking.DISABLE   | Blanking performed based on the marker locations for the marker that the user set in the blanking source. |
    +-----------------------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------+
    | NIRFSG_VAL_MARKER0, NIRFSG_VAL_MARKER1, NIRFSG_VAL_MARKER2, or NIRFSG_VAL_MARKER3 | RFBlanking.ENABLE    | Error is shown.                                                                                           |
    +-----------------------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------------------------------+

    Note: For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking properties. Alternatively, you can call reset_with_options or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_rf_blanking`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_rf_blanking`
    '''
    waveform_runtime_scaling = _attributes.AttributeViReal64(1150265)
    '''Type: float

    Specifies the waveform runtime scaling. The waveform runtime scaling is applied to the waveform data before any other signal processing.

    **Units**: dB

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5841 with PXIe-5655

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_runtime_scaling`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_runtime_scaling`
    '''
    waveform_signal_bandwidth = _attributes.AttributeViReal64(1150264)
    '''Type: float

    Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8× iq_rate).

    **Units**: hertz (Hz)

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_signal_bandwidth`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_signal_bandwidth`
    '''
    waveform_waveform_size = _attributes.AttributeViInt32(1150297)
    '''Type: int

    Specifies the size of the waveform specified by an active channel.

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5841 with PXIe-5655/5842/5860

    Tip:
    This property can be set/get on specific waveforms within your :py:class:`nirfsg.Session` instance.
    Use Python index notation on the repeated capabilities container waveforms to specify a subset.

    Example: :py:attr:`my_session.waveforms[ ... ].waveform_waveform_size`

    To set/get on all waveforms, you can call the property directly on the :py:class:`nirfsg.Session`.

    Example: :py:attr:`my_session.waveform_waveform_size`
    '''
    write_waveform_burst_detection = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WriteWaveformBurstDetection, 1150273)
    '''Type: enums.WriteWaveformBurstDetection

    Enables the detection of burst start and burst stop locations in the waveform. You can read the detected burst start and burst stop locations using get_waveform_burst_start_locations and get_waveform_burst_stop_locations methods respectively.

    **Default Value:** WriteWaveformBurstDetection.DISABLE

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +-------------------------------------+------------------------------+
    | Value                               | Description                  |
    +=====================================+==============================+
    | WriteWaveformBurstDetection.ENABLE  | Burst detection is enabled.  |
    +-------------------------------------+------------------------------+
    | WriteWaveformBurstDetection.DISABLE | Burst detection is disabled. |
    +-------------------------------------+------------------------------+

    Note: - When you download a waveform using ReadAndDownloadWaveformFromFileTdms method and if waveform_rf_blanking property is enabled, you must set the write_waveform_burst_detection property to WriteWaveformBurstDetection.DISABLE.

     - For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any Reset or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking properties. Alternatively, you can call reset_with_options or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    write_waveform_burst_detection_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WriteWaveformBurstDetectionMode, 1150274)
    '''Type: enums.WriteWaveformBurstDetectionMode

    Specifies the algorithm that NI-RFSG uses to detect the burst start and burst stop locations in the waveform when burst detection is enabled using the write_waveform_burst_detection property. When you set write_waveform_burst_detection_mode to WriteWaveformBurstDetectionMode.AUTO, NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform. To fine-tune the burst detection process parameters yourself, you can set this property to WriteWaveformBurstDetectionMode.MANUAL and specify the burst detection parameters using the write waveform burst detection minimum quiet time, write_waveform_burst_detection_power_threshold, write waveform burst detection minimum burst time properties.

    **Default Value:** WriteWaveformBurstDetectionMode.AUTO

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +----------------------------------------+---------------------------------------------------------------------------------------------------+
    | Value                                  | Description                                                                                       |
    +========================================+===================================================================================================+
    | WriteWaveformBurstDetectionMode.AUTO   | NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform. |
    +----------------------------------------+---------------------------------------------------------------------------------------------------+
    | WriteWaveformBurstDetectionMode.MANUAL | User sets the burst detection parameters.                                                         |
    +----------------------------------------+---------------------------------------------------------------------------------------------------+

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    write_waveform_burst_detection_power_threshold = _attributes.AttributeViReal64(1150276)
    '''Type: float

    Specifies the relative power level at which burst start or stop locations are detected. The threshold is relative to the peak power in the waveform. NI-RFSG detects burst start (or burst stop) locations when the signal exceeds (or falls below) the level specified by this property. This property is ignored when you disable the write_waveform_burst_detection property or when you set the write_waveform_burst_detection_mode property to NIRFSG_VAL_AUTO.

    **Units:** dB

    **Default Value:** 0

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    write_waveform_normalization = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WriteWaveformNormalization, 1150293)
    '''Type: enums.WriteWaveformNormalization

    Specifies whether to perform the normalization on a waveform.

    **Default Value:** WriteWaveformNormalization.DISABLE

    **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Defined Values**:

    +------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
    | Value                              | Description                                                                                                             |
    +====================================+=========================================================================================================================+
    | WriteWaveformNormalization.ENABLE  | Enables normalization on a waveform to transform the waveform data so that its maximum is 1.00 and its minimum is -1.00 |
    +------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
    | WriteWaveformNormalization.DISABLE | Disables normalization on the waveform.                                                                                 |
    +------------------------------------+-------------------------------------------------------------------------------------------------------------------------+

    Note: You can not set write_waveform_normalization and power_level_type properties at the same time.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    yig_main_coil_drive = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.YigMainCoilDrive, 1150118)
    '''Type: enums.YigMainCoilDrive

    Adjusts the dynamics of the current driving the YIG main coil.

    **Default Value:** YigMainCoilDrive.MANUAL

    **Supported Devices:** PXIe-5653

    **Defined Values**:

    +-----------------------+--------------------------------------------------------+
    | Value                 | Description                                            |
    +=======================+========================================================+
    | NIRFSG_VAL_SLOW       | Adjusts the YIG main coil for an underdamped response. |
    +-----------------------+--------------------------------------------------------+
    | YigMainCoilDrive.FAST | Adjusts the YIG main coil for an overdamped response.  |
    +-----------------------+--------------------------------------------------------+

    Note: Setting this property to YigMainCoilDrive.FAST on the PXIe-5653 allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise.

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''

    def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._interpreter = interpreter

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("interpreter=" + pp.pformat(interpreter))
        self._param_list = ', '.join(param_list)

        # Instantiate any repeated capability objects
        self.markers = _RepeatedCapabilities(self, 'marker', repeated_capability_list)
        self.script_triggers = _RepeatedCapabilities(self, 'scripttrigger', repeated_capability_list)
        self.waveforms = _RepeatedCapabilities(self, 'waveform::', repeated_capability_list)
        self.ports = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.los = _RepeatedCapabilities(self, 'LO', repeated_capability_list)
        self.device_temperatures = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nirfsg', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    ''' These are code-generated '''

    @ivi_synchronized
    def check_attribute_vi_boolean(self, attribute, value):
        r'''check_attribute_vi_boolean

        Checks the validity of a value you specify for a ViBoolean property.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.check_attribute_vi_boolean`

        Args:
            attribute (int): Pass the ID of a property.

            value (bool): Pass the value that you want to verify as a valid value for the property.

                Note: Some of the values might not be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.check_attribute_vi_boolean(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def check_attribute_vi_int32(self, attribute, value):
        r'''check_attribute_vi_int32

        Checks the validity of a value you specify for a ViInt32 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.check_attribute_vi_int32`

        Args:
            attribute (int): Pass the ID of a property.

            value (int): Pass the value that you want to verify as a valid value for the property.

                Note: Some of the values might not be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.check_attribute_vi_int32(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def check_attribute_vi_int64(self, attribute, value):
        r'''check_attribute_vi_int64

        Checks the validity of a value you specify for a ViInt64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.check_attribute_vi_int64`

        Args:
            attribute (int): Pass the ID of a property.

            value (int): Pass the value that you want to verify as a valid value for the property.

                Note: Some of the values might not be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.check_attribute_vi_int64(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def check_attribute_vi_real64(self, attribute, value):
        r'''check_attribute_vi_real64

        Checks the validity of a value you specify for a ViReal64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.check_attribute_vi_real64`

        Args:
            attribute (int): Pass the ID of a property.

            value (float): Pass the value that you want to verify as a valid value for the property.

                Note: Some of the values might not be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.check_attribute_vi_real64(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def check_attribute_vi_session(self, attribute):
        r'''check_attribute_vi_session

        Checks the validity of a value you specify for a ViSession property.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_session`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.check_attribute_vi_session`

        Args:
            attribute (int): Pass the ID of a property.

        '''
        self._interpreter.check_attribute_vi_session(self._repeated_capability, attribute)

    @ivi_synchronized
    def check_attribute_vi_string(self, attribute, value):
        r'''check_attribute_vi_string

        Checks the validity of a value you specify for a ViString property.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.check_attribute_vi_string`

        Args:
            attribute (int): Pass the ID of a property.

            value (str): Pass the value that you want to verify as a valid value for the property. The value must be a NULL-terminated string.

                Note: Some of the values might not be valid depending on the current settings of the instrument session.

        '''
        self._interpreter.check_attribute_vi_string(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def configure_digital_edge_script_trigger(self, source, edge):
        r'''configure_digital_edge_script_trigger

        Configures the specified Script Trigger for digital edge triggering.

        The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].configure_digital_edge_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.configure_digital_edge_script_trigger`

        Args:
            source (str): Specifies the source terminal for the digital edge Script Trigger. NI-RFSG sets the digital_edge_script_trigger_source property to this value.

            edge (enums.ScriptTriggerDigitalEdgeEdge): Specifies the active edge for the digital edge Script Trigger. NI-RFSG sets the digital_edge_script_trigger_edge property to this value.

        '''
        if type(edge) is not enums.ScriptTriggerDigitalEdgeEdge:
            raise TypeError('Parameter edge must be of type ' + str(enums.ScriptTriggerDigitalEdgeEdge))
        self._interpreter.configure_digital_edge_script_trigger(self._repeated_capability, source, edge)

    @ivi_synchronized
    def configure_digital_level_script_trigger(self, source, level):
        r'''configure_digital_level_script_trigger

        Configures a specified Script Trigger for digital level triggering.

        The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        `Digital Level Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_level.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].configure_digital_level_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.configure_digital_level_script_trigger`

        Args:
            source (str): Specifies the trigger source terminal for the digital level Script Trigger. NI-RFSG sets the digital_level_script_trigger_source property to this value.

            level (int): Specifies the active level for the digital level Script Trigger. NI-RFSG sets the digital_level_script_trigger_active_level property to this value.

        '''
        self._interpreter.configure_digital_level_script_trigger(self._repeated_capability, source, level)

    @ivi_synchronized
    def configure_software_script_trigger(self):
        r'''configure_software_script_trigger

        Configures the Script Trigger for software triggering.

        Refer to the send_software_edge_trigger method for more information about using the software Script Trigger. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].configure_software_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.configure_software_script_trigger`
        '''
        self._interpreter.configure_software_script_trigger(self._repeated_capability)

    @ivi_synchronized
    def disable_script_trigger(self):
        r'''disable_script_trigger

        Configures the device not to wait for the specified Script Trigger.

        Call this method only if you previously configured a Script Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].disable_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.disable_script_trigger`
        '''
        self._interpreter.disable_script_trigger(self._repeated_capability)

    def error_message(self, error_code, error_message):
        r'''error_message

        Converts an error code returned by an NI-RFSG method into a user-readable string.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            error_code (int): Pass the status parameter that is returned from any NI-RFSG method.

                **Default Value** : 0 (VI_SUCCESS)

            error_message (str): Returns the user-readable message string that corresponds to the status code you specify.

                You must pass a ViChar array with at least 256 bytes to this parameter.

        '''
        self._interpreter.error_message(error_code, error_message)

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute):
        r'''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (bool): Returns the current value of the property. Pass the address of a ViBoolean variable.

        '''
        value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute):
        r'''_get_attribute_vi_int32

        Queries the value of a ViInt32 property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViInt32 variable.

        '''
        value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_int64(self, attribute):
        r'''_get_attribute_vi_int64

        Queries the value of a ViInt64 property.

        You can use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViInt64 variable.

        '''
        value = self._interpreter.get_attribute_vi_int64(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute):
        r'''_get_attribute_vi_real64

        Queries the value of a ViReal64 property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (float): Returns the current value of the property. Pass the address of a ViReal64 variable.

        '''
        value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_session(self, attribute):
        r'''_get_attribute_vi_session

        Queries the value of a ViSession property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_session`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_session`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViSession variable.

        '''
        value = self._interpreter.get_attribute_vi_session(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute):
        r'''_get_attribute_vi_string

        Queries the value of a ViString property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        You must provide a ViString (ViChar array) to serve as a buffer for the value. Pass the number of bytes in the buffer as the Buffer Size parameter. If the current value of the property, including the terminating NULL byte, is larger than the size you indicate in the buffer size parameter, the method copies buffer size-1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the method places "123" into the buffer and returns 7.

        To call this method to get only the required buffer size, pass 0 for the buffer size and VI_NULL for the property value buffer.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (str): The buffer in which the method returns the current value of the property. The buffer must be of type ViChar and have at least as many bytes as indicated in the **bufferSize** parameter.

                If you specify 0 for the **bufferSize** parameter, you can pass VI_NULL for this parameter.

        '''
        value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute)
        return value

    @ivi_synchronized
    def get_waveform_burst_start_locations(self):
        r'''get_waveform_burst_start_locations

        Returns the burst start locations of the waveform stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].get_waveform_burst_start_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.get_waveform_burst_start_locations`

        Returns:
            locations (list of float): Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        locations = self._interpreter.get_waveform_burst_start_locations(self._repeated_capability)
        return locations

    @ivi_synchronized
    def get_waveform_burst_stop_locations(self):
        r'''get_waveform_burst_stop_locations

        Returns the burst stop locations of the waveform stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].get_waveform_burst_stop_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.get_waveform_burst_stop_locations`

        Returns:
            locations (list of float): Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        locations = self._interpreter.get_waveform_burst_stop_locations(self._repeated_capability)
        return locations

    @ivi_synchronized
    def get_waveform_marker_event_locations(self):
        r'''get_waveform_marker_event_locations

        Returns the marker locations associated with the waveform and the marker stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific markers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container markers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.markers[ ... ].get_waveform_marker_event_locations`

        To call the method on all markers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.get_waveform_marker_event_locations`

        Returns:
            locations (list of float): Returns the marker locations stored in the NI-RFSG database for the channel you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        locations = self._interpreter.get_waveform_marker_event_locations(self._repeated_capability)
        return locations

    @ivi_synchronized
    def load_configurations_from_file(self, file_path):
        r'''load_configurations_from_file

        Loads the configurations from the specified file to the NI-RFSG driver session.

        The VI does an implicit reset before loading the configurations from the file.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].load_configurations_from_file`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.load_configurations_from_file`

        Args:
            file_path (str): Specifies the absolute path of the file from which the NI-RFSG loads the configurations.

        '''
        self._interpreter.load_configurations_from_file(self._repeated_capability, file_path)

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-RFSG locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, nirfsg.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    @ivi_synchronized
    def reset_attribute(self, attribute_id):
        r'''reset_attribute

        Resets the property to its default value.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].reset_attribute`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.reset_attribute`

        Args:
            attribute_id (int): Pass the ID of a property.

        '''
        self._interpreter.reset_attribute(self._repeated_capability, attribute_id)

    @ivi_synchronized
    def save_configurations_to_file(self, file_path):
        r'''save_configurations_to_file

        Saves the configurations of the session to the specified file.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].save_configurations_to_file`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.save_configurations_to_file`

        Args:
            file_path (str): Specifies the absolute path of the file to which the NI-RFSG saves the configurations.

        '''
        self._interpreter.save_configurations_to_file(self._repeated_capability, file_path)

    @ivi_synchronized
    def send_software_edge_trigger(self, trigger, trigger_identifier):
        r'''send_software_edge_trigger

        Forces a trigger to occur.

        The specified trigger generates regardless of whether the trigger has been configured as a software trigger.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

        Args:
            trigger (enums.SoftwareTriggerType): Specifies the trigger to send.

                **Default Value:** SoftwareTriggerType.START

                **Defined Values:**

                +----------------------------+---------+-------------------------------+
                | Name                       | Value   | Description                   |
                +============================+=========+===============================+
                | SoftwareTriggerType.START  | 0 (0x0) | Specifies the Start Trigger.  |
                +----------------------------+---------+-------------------------------+
                | SoftwareTriggerType.SCRIPT | 1 (0x1) | Specifies the Script Trigger. |
                +----------------------------+---------+-------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            trigger_identifier (str): Specifies the Script Trigger to configure. This parameter is valid only when you set the TRIGGER parameter to NIRFSG_VAL_START_TRIGGER. Otherwise, set the TRIGGER_IDENTIFIER parameter to "" (empty string).

                **Default Value:** "" (empty string)

                **Possible Values:**

                +----------------+-----------------------------+
                | Possible Value | Description                 |
                +================+=============================+
                | scriptTrigger0 | Specifies Script Trigger 0. |
                +----------------+-----------------------------+
                | scriptTrigger1 | Specifies Script Trigger 1. |
                +----------------+-----------------------------+
                | scriptTrigger2 | Specifies Script Trigger 2. |
                +----------------+-----------------------------+
                | scriptTrigger3 | Specifies Script Trigger 3. |
                +----------------+-----------------------------+
                |                | None (no signal to export)  |
                +----------------+-----------------------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        if type(trigger) is not enums.SoftwareTriggerType:
            raise TypeError('Parameter trigger must be of type ' + str(enums.SoftwareTriggerType))
        self._interpreter.send_software_edge_trigger(trigger, trigger_identifier)

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute, value):
        r'''_set_attribute_vi_boolean

        Sets the value of a ViBoolean property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute (int): Pass the ID of a property.

            value (bool): Pass the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_boolean(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute, value):
        r'''_set_attribute_vi_int32

        Sets the value of a ViInt32 property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute (int): Pass the ID of a property.

            value (int): Specifies the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_int64(self, attribute, value):
        r'''_set_attribute_vi_int64

        Sets the value of a ViInt64 property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute (int): Pass the ID of a property.

            value (int): Pass the value to which you want to set the property.

                <blockquote>
                Some values may not be valid. The allowed values depend on the current settings of the instrument session.
                </blockquote>

        '''
        self._interpreter.set_attribute_vi_int64(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute, value):
        r'''_set_attribute_vi_real64

        Sets the value of a ViReal64 property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute (int): Pass the ID of a property.

            value (float): Pass the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_real64(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def _set_attribute_vi_session(self, attribute):
        r'''_set_attribute_vi_session

        Sets the value of a ViSession property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_session`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_session`

        Args:
            attribute (int): Pass the ID of a property.

        '''
        self._interpreter.set_attribute_vi_session(self._repeated_capability, attribute)

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute, value):
        r'''_set_attribute_vi_string

        Sets the value of a ViString property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute (int): Pass the ID of a property.

            value (str): Pass the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_string(self._repeated_capability, attribute, value)

    @ivi_synchronized
    def set_waveform_burst_start_locations(self, locations):
        r'''set_waveform_burst_start_locations

        Configures the start location of the burst in samples where the burst refers to the active portion of a waveform.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].set_waveform_burst_start_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.set_waveform_burst_start_locations`

        Args:
            locations (list of float): Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        self._interpreter.set_waveform_burst_start_locations(self._repeated_capability, locations)

    @ivi_synchronized
    def set_waveform_burst_stop_locations(self, locations):
        r'''set_waveform_burst_stop_locations

        Configures the stop location of the burst in samples where the burst refers to the active portion of a waveform.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].set_waveform_burst_stop_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.set_waveform_burst_stop_locations`

        Args:
            locations (list of float): Specifies the burst stop locations, in samples, to store in the NI-RFSG session.

        '''
        self._interpreter.set_waveform_burst_stop_locations(self._repeated_capability, locations)

    @ivi_synchronized
    def set_waveform_marker_event_locations(self, locations):
        r'''set_waveform_marker_event_locations

        Configures the marker locations associated with waveform and marker in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific markers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container markers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.markers[ ... ].set_waveform_marker_event_locations`

        To call the method on all markers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.set_waveform_marker_event_locations`

        Args:
            locations (list of float): Specifies the marker location, in samples, to store in the NI-RFSG database.

        '''
        self._interpreter.set_waveform_marker_event_locations(self._repeated_capability, locations)

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()


class Session(_SessionBase):
    '''An NI-RFSG session to the NI-RFSG driver'''

    def __init__(self, resource_name, id_query=False, reset_device=False, options={}):
        r'''An NI-RFSG session to the NI-RFSG driver

        Opens a session to the device you specify as the RESOURCE_NAME and returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        This method also configures the device through the OPTION_STRING input.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Simulating an NI RF Signal Generator <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/simulate.html>`_

        Note: For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending /*ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Specifies the resource name of the device to initialize.

                For NI-DAQmx devices, the syntax is the device name specified in MAX. Typical default names for NI-DAQmx devices in MAX are Dev2 or PXISlot2. You can rename an NI-DAQmx device in MAX.

                You can also specify the name of an IVI logical name configured with the IVI Configuration utility. Refer to the *IVI* topic of the *Measurement & Automation Explorer Help* for more information.

                Note: NI-RFSG device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use an IVI logical name, make sure the name is identical to the name shown in the IVI Configuration Utility.

            id_query (bool): Specifies whether you want NI-RFSG to perform an ID query.

                **Defined Values** :

                +-----------+--------------------------+
                | Value     | Description              |
                +===========+==========================+
                | True (1)  | Perform ID query.        |
                +-----------+--------------------------+
                | False (0) | Do not perform ID query. |
                +-----------+--------------------------+

            reset_device (bool): Specifies whether you want to reset the NI-RFSG device during the initialization procedure.

                **Defined Values** :

                +-----------+----------------------+
                | Value     | Description          |
                +===========+======================+
                | True (1)  | Reset device.        |
                +-----------+----------------------+
                | False (0) | Do not reset device. |
                +-----------+----------------------+

            options (dict): Specifies the initial value of certain properties for the session. The
                syntax for **options** is a dictionary of properties with an assigned
                value. For example:

                { 'simulate': False }

                You do not have to specify a value for all the properties. If you do not
                specify a value for a property, the default value is used.

                Advanced Example:
                { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

                +-------------------------+---------+
                | Property                | Default |
                +=========================+=========+
                | range_check             | True    |
                +-------------------------+---------+
                | query_instrument_status | False   |
                +-------------------------+---------+
                | cache                   | True    |
                +-------------------------+---------+
                | simulate                | False   |
                +-------------------------+---------+
                | record_value_coersions  | False   |
                +-------------------------+---------+
                | driver_setup            | {}      |
                +-------------------------+---------+


        Returns:
            new_vi (int): Returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        '''
        interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')

        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            interpreter=interpreter,
            freeze_it=False,
            all_channels_in_session=None
        )
        options = _converters.convert_init_with_options_dictionary(options)

        # Call specified init function
        # Note that _interpreter default-initializes the session handle in its constructor, so that
        # if _init_with_options fails, the error handler can reference it.
        # And then here, once _init_with_options succeeds, we call set_session_handle
        # with the actual session handle.
        self._interpreter.set_session_handle(self._init_with_options(resource_name, id_query, reset_device, options))

        self.tclk = nitclk.SessionReference(self._interpreter.get_session_handle())

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("id_query=" + pp.pformat(id_query))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def initiate(self):
        '''initiate

        Initiates signal generation, causing the NI-RFSG device to leave the Configuration state and enter the Generation state.

        If the settings have not been committed to the device before you call this method, they are committed by this method. The operation returns when the RF output signal settles. To return to the Configuration state, call the abort method.

        **Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Generation(self)

    def close(self):
        '''close

        Aborts any signal generation in progress and destroys the instrument driver session.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Stops signal generation.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_
        '''
        self._interpreter.abort()

    @ivi_synchronized
    def allocate_arb_waveform(self, waveform_name, size_in_samples):
        r'''allocate_arb_waveform

        Allocates onboard memory space for the arbitrary waveform.

        Use this method to specify the total size of a waveform before writing the data. Use this method only if you are calling the WriteArbWaveform method multiple times to write a large waveform in smaller blocks.

        The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            size_in_samples (int): Specifies the number of samples to reserve in the onboard memory for the specified waveform. Each I/Q pair is considered one sample.

        '''
        self._interpreter.allocate_arb_waveform(waveform_name, size_in_samples)

    @ivi_synchronized
    def change_external_calibration_password(self, old_password, new_password):
        r'''change_external_calibration_password

        Changes the external calibration password of the device.

        **Supported Devices:** PXIe-5611, PXIe-5653/5654, PXIe-5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            old_password (str): Specifies the old (current) external calibration password. This password is case sensitive.

            new_password (str): Specifies the new (desired) external calibration password.

        '''
        self._interpreter.change_external_calibration_password(old_password, new_password)

    @ivi_synchronized
    def check_generation_status(self):
        r'''check_generation_status

        Checks the status of the generation.

        Call this method to check for any errors that might occur during the signal generation or to check whether the device has finished generating.

        **Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`

        Returns:
            is_done (bool): Returns information about the completion of signal generation.

                **Defined Values** :

                +-------+---------------------------------+
                | Value | Description                     |
                +=======+=================================+
                | True  | Signal generation is complete.  |
                +-------+---------------------------------+
                | False | Signal generation is occurring. |
                +-------+---------------------------------+

        '''
        is_done = self._interpreter.check_generation_status()
        return is_done

    @ivi_synchronized
    def check_if_script_exists(self, script_name):
        r'''check_if_script_exists

        Returns whether the script that you specify as SCRIPT_NAME exists.

        **Supported Devices** : PXIe-5673/5673E. PXIe-5830/5831/5840/5841/5842/5860

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            script_name (str): Specifies the name of the script. This string is case-insensitive.


        Returns:
            script_exists (bool): Returns True if the script exists.

                **Defined Values** :

                +-------+----------------------------+
                | Value | Description                |
                +=======+============================+
                | True  | The script exists.         |
                +-------+----------------------------+
                | False | The script does not exist. |
                +-------+----------------------------+

        '''
        script_exists = self._interpreter.check_if_script_exists(script_name)
        return script_exists

    @ivi_synchronized
    def check_if_waveform_exists(self, waveform_name):
        r'''check_if_waveform_exists

        Returns whether the waveform that you specify as WAVEFORM_NAME exists.

        **Supported Devices** : PXIe-5673/5673E, PXIe-5830/5831/5840/5841/5842/5860

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            waveform_name (str): Specifies the name used to store the waveform. This string is case-insensitive.


        Returns:
            waveform_exists (bool): Returns True if the waveform exists.

                **Defined Values** :

                +-------+------------------------------+
                | Value | Description                  |
                +=======+==============================+
                | True  | The waveform exists.         |
                +-------+------------------------------+
                | False | The waveform does not exist. |
                +-------+------------------------------+

        '''
        waveform_exists = self._interpreter.check_if_waveform_exists(waveform_name)
        return waveform_exists

    @ivi_synchronized
    def clear_all_arb_waveforms(self):
        r'''clear_all_arb_waveforms

        Deletes all currently defined waveforms and scripts.

        The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
        '''
        self._interpreter.clear_all_arb_waveforms()

    @ivi_synchronized
    def clear_arb_waveform(self, name):
        r'''clear_arb_waveform

        Deletes a specified waveform from the pool of currently defined waveforms.

        The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            name (str): Name of the stored waveform to delete.

        '''
        self._interpreter.clear_arb_waveform(name)

    @ivi_synchronized
    def clear_error(self):
        r'''clear_error

        Clears the error information associated with the session.

        If you pass VI_NULL for the VI parameter, this method clears the error information for the current execution thread.

        The IVI Engine also maintains this error information separately for each thread. This feature of the IVI Engine is useful if you do not have a session handle to pass to the clear_error method or the get_error method, which occurs when a call to the Init method or the __init__ method fails.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860

        Note: The get_error method clears the error information after it is retrieved. A call to the clear_error method is necessary only when you do not use a call to the get_error method to retrieve error information.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.
        '''
        self._interpreter.clear_error()

    @ivi_synchronized
    def clear_self_calibrate_range(self):
        r'''clear_self_calibrate_range

        Clears the data obtained from the self_calibrate_range method.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842
        '''
        self._interpreter.clear_self_calibrate_range()

    @ivi_synchronized
    def commit(self):
        r'''commit

        Programs the device with the correct settings.

        Calling this method moves the NI-RFSG device from the Configuration state to the Committed state. After this method executes, a change to any property reverts the NI-RFSG device to the Configuration state.

        **Supported devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_
        '''
        self._interpreter.commit()

    @ivi_synchronized
    def configure_deembedding_table_interpolation_linear(self, port, table_name, format):
        r'''configure_deembedding_table_interpolation_linear

        Selects the linear interpolation method.

        If the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

            format (enums.Format): Specifies the format of parameters to interpolate. **Defined Values** :

                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | Name                          | Value          | Description                                                                                                                             |
                +===============================+================+=========================================================================================================================================+
                | Format.REAL_AND_IMAGINARY     | 26000 (0x6590) | Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion. |
                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | Format.MAGNITUDE_AND_PHASE    | 26001 (0x6591) | Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.                                    |
                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | Format.MAGNITUDE_DB_AND_PHASE | 26002 (0x6592) | Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.                      |
                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+

        '''
        if type(format) is not enums.Format:
            raise TypeError('Parameter format must be of type ' + str(enums.Format))
        self._interpreter.configure_deembedding_table_interpolation_linear(port, table_name, format)

    @ivi_synchronized
    def configure_deembedding_table_interpolation_nearest(self, port, table_name):
        r'''configure_deembedding_table_interpolation_nearest

        Selects the nearest interpolation method.

        NI-RFSG uses the parameters of the table nearest to the carrier frequency for de-embedding.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        '''
        self._interpreter.configure_deembedding_table_interpolation_nearest(port, table_name)

    @ivi_synchronized
    def configure_deembedding_table_interpolation_spline(self, port, table_name):
        r'''configure_deembedding_table_interpolation_spline

        Selects the spline interpolation method.

        If the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        '''
        self._interpreter.configure_deembedding_table_interpolation_spline(port, table_name)

    @ivi_synchronized
    def configure_digital_edge_start_trigger(self, source, edge):
        r'''configure_digital_edge_start_trigger

        Configures the Start Trigger for digital edge triggering.

        The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

        `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

        Note: For the PXIe-5654/5654 with PXIe-5696, the Start Trigger is valid only with a timer-based list when RF list mode is enabled.

        Args:
            source (str): Specifies the source terminal for the digital edge trigger. NI-RFSG sets the digital_edge_start_trigger_source property to this value.

            edge (enums.StartTriggerDigitalEdgeEdge): Specifies the active edge for the Start Trigger. NI-RFSG sets the digital_edge_start_trigger_edge property to this value.

        '''
        if type(edge) is not enums.StartTriggerDigitalEdgeEdge:
            raise TypeError('Parameter edge must be of type ' + str(enums.StartTriggerDigitalEdgeEdge))
        self._interpreter.configure_digital_edge_start_trigger(source, edge)

    @ivi_synchronized
    def configure_digital_modulation_user_defined_waveform(self, number_of_samples, user_defined_waveform):
        r'''configure_digital_modulation_user_defined_waveform

        Specifies the message signal used for digital modulation when the digital_modulation_waveform_type property is set to NIRFSG_VAL_USER_DEFINED.

        **Supported Devices** : PXI/PXIe-5650/5651/5652

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        Args:
            number_of_samples (int): Specifies the number of samples in the message signal.

            user_defined_waveform (list of int): Specifies the user-defined message signal used for digital modulation.

        '''
        self._interpreter.configure_digital_modulation_user_defined_waveform(number_of_samples, user_defined_waveform)

    @ivi_synchronized
    def configure_pxi_chassis_clk10(self, pxi_clk10_source):
        r'''configure_pxi_chassis_clk10

        Specifies the signal to drive the 10MHz Reference Clock on the PXI backplane.

        This option can only be configured when the PXI-5610 is in Slot 2 of the PXI chassis. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXI-5610, PXI-5670/5671

        **Related Topics**

        `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

        `System Reference Clock <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_clk10.html>`_

        Args:
            pxi_clk10_source (str): Specifies the source of the Reference Clock signal.

        '''
        self._interpreter.configure_pxi_chassis_clk10(pxi_clk10_source)

    @ivi_synchronized
    def configure_rf(self, frequency, power_level):
        r'''configure_rf

        Configures the frequency and power level of the RF output signal.

        The PXI-5670/5671, PXIe-5672, and PXIe-5860 device must be in the Configuration state before calling this method. The PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 device can be in the Configuration or Generation state when you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        Args:
            frequency (float): Specifies the frequency of the generated RF signal, in hertz. For arbitrary waveform generation, this parameter specifies the center frequency of the signal.

                **Units** : hertz (Hz)

            power_level (float): Specifies either the average power level or peak power level of the generated RF signal, depending on the power_level_type property.

                **Units** : dBm

        '''
        self._interpreter.configure_rf(frequency, power_level)

    @ivi_synchronized
    def configure_ref_clock(self, ref_clock_source, ref_clock_rate):
        r'''configure_ref_clock

        Configures the NI-RFSG device Reference Clock.

        The Reference Clock ensures that the NI-RFSG devices are operating from a common timebase. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `PXIe-5672 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

        `PXIe-5673 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/10mhzreference_phase1.html>`_

        `PXIe-5673E Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/10mhzreference.html>`_

        `PXIe-5830 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

        `PXIe-5831 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

        Args:
            ref_clock_source (str): Specifies the source of Reference Clock signal.

                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Possible Values | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
                +=================+=================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
                | "OnboardClock"  |  Uses the onboard Reference Clock as the clock source. **PXIe-5830/5831/5832** :For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. **PXIe-5831 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. **PXIe-5832 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. **PXIe-5841 with PXIe-5655** :Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. **PXIe-5842** :Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "RefIn"         | Uses the clock signal present at the front panel REF IN connector as the clock source. **PXIe-5830/5831/5832** :For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. **PXIe-5831 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. **PXIe-5832 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector.  **PXIe-5841 with PXIe-5655** :Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. **PXIe-5842** :Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "PXI_CLK"       | Uses the PXI_CLK signal, which is present on the PXI backplane, as the clock source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "ClkIn"         | Uses the clock signal present at the front panel CLK IN connector as the clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655/5842.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "RefIn2"        | \-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "PXI_ClkMaster" | This value is valid on only the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. **PXIe-5831 with PXIe-5653** :NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. **PXIe-5832 with PXIe-5653** :NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

            ref_clock_rate (float): Specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. The default value is NIRFSG_VAL_AUTO, which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. This parameter is only valid when the ref_clock_source parameter is set to ClkIn, RefIn or RefIn2. Refer to the ref_clock_rate property for possible values.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        self._interpreter.configure_ref_clock(ref_clock_source, ref_clock_rate)

    @ivi_synchronized
    def configure_software_start_trigger(self):
        r'''configure_software_start_trigger

        Configures the Start Trigger for software triggering.

        Refer to the send_software_edge_trigger method for more information about using a software trigger. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

        `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_
        '''
        self._interpreter.configure_software_start_trigger()

    @ivi_synchronized
    def _create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation):
        r'''_create_deembedding_sparameter_table_array

        Creates an s-parameter de-embedding table for the port from the input data.

        If you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

            frequencies (numpy.array(dtype=numpy.float64)): Specifies the frequencies for the SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            sparameter_table (numpy.array(dtype=numpy.complex128)): Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.

            sparameter_orientation (enums.SparameterOrientation): Specifies the orientation of the input data relative to the port on the DUT port.

                **Defined Values** :

                +-----------------------------------------+----------------+-----------------------------------------------------+
                | Name                                    | Value          | Description                                         |
                +=========================================+================+=====================================================+
                | SparameterOrientation.PORT1_TOWARDS_DUT | 24000 (0x5dc0) | Port 1 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+
                | SparameterOrientation.PORT2_TOWARDS_DUT | 24001 (0x5dc1) | Port 2 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+

        '''
        import numpy

        if type(sparameter_orientation) is not enums.SparameterOrientation:
            raise TypeError('Parameter sparameter_orientation must be of type ' + str(enums.SparameterOrientation))
        if type(frequencies) is not numpy.ndarray:
            raise TypeError('frequencies must be {0}, is {1}'.format(numpy.ndarray, type(frequencies)))
        if numpy.isfortran(frequencies) is True:
            raise TypeError('frequencies must be in C-order')
        if frequencies.dtype is not numpy.dtype('float64'):
            raise TypeError('frequencies must be numpy.ndarray of dtype=float64, is ' + str(frequencies.dtype))
        if frequencies.ndim != 1:
            raise TypeError('frequencies must be numpy.ndarray of dimension=1, is ' + str(frequencies.ndim))
        if type(sparameter_table) is not numpy.ndarray:
            raise TypeError('sparameter_table must be {0}, is {1}'.format(numpy.ndarray, type(sparameter_table)))
        if numpy.isfortran(sparameter_table) is True:
            raise TypeError('sparameter_table must be in C-order')
        if sparameter_table.dtype is not numpy.dtype('complex128'):
            raise TypeError('sparameter_table must be numpy.ndarray of dtype=complex128, is ' + str(sparameter_table.dtype))
        if sparameter_table.ndim != 3:
            raise TypeError('sparameter_table must be numpy.ndarray of dimension=3, is ' + str(sparameter_table.ndim))
        self._interpreter.create_deembedding_sparameter_table_array(port, table_name, frequencies, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation)

    @ivi_synchronized
    def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation):
        r'''create_deembedding_sparameter_table_s2p_file

        Creates an S-parameter de-embedding table for the port based on the specified S2P file.

        If you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/de_embedding_overview.html>`_

        `S-parameters <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/s_parameters.html>`_

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842 is empty string.

            table_name (str): Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

            s2p_file_path (str): Specifies the path to the S2P file that contains de-embedding information for the specified port.

            sparameter_orientation (enums.SparameterOrientation): Specifies the orientation of the data in the S2P file relative to the port on the DUT port. **Defined Values** :

                +-----------------------------------------+----------------+-----------------------------------------------------+
                | Name                                    | Value          | Description                                         |
                +=========================================+================+=====================================================+
                | SparameterOrientation.PORT1_TOWARDS_DUT | 24000 (0x5dc0) | Port 1 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+
                | SparameterOrientation.PORT2_TOWARDS_DUT | 24001 (0x5dc1) | Port 2 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+

        '''
        if type(sparameter_orientation) is not enums.SparameterOrientation:
            raise TypeError('Parameter sparameter_orientation must be of type ' + str(enums.SparameterOrientation))
        self._interpreter.create_deembedding_sparameter_table_s2p_file(port, table_name, s2p_file_path, sparameter_orientation)

    @ivi_synchronized
    def delete_all_deembedding_tables(self):
        r'''delete_all_deembedding_tables

        Deletes all configured de-embedding tables for the session.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860
        '''
        self._interpreter.delete_all_deembedding_tables()

    @ivi_synchronized
    def delete_deembedding_table(self, port, table_name):
        r'''delete_deembedding_table

        Deletes the selected de-embedding table for a given port.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        '''
        self._interpreter.delete_deembedding_table(port, table_name)

    @ivi_synchronized
    def disable(self):
        r'''disable

        Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E
        '''
        self._interpreter.disable()

    @ivi_synchronized
    def disable_start_trigger(self):
        r'''disable_start_trigger

        Configures the device not to wait for a Start Trigger.

        This method is necessary only if you previously configured a Start Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_
        '''
        self._interpreter.disable_start_trigger()

    @ivi_synchronized
    def error_query(self):
        r'''error_query

        Reads an error code and an error message from the instrument error queue.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860

        Returns:
            error_code (int): Returns the error code read from the instrument error queue.

            error_message (str): Returns the error message string read from the instrument error message queue.

                You must pass a ViChar array with at least 256 bytes.

        '''
        error_code, error_message = self._interpreter.error_query()
        return error_code, error_message

    def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, sparameter_orientation):
        '''create_deembedding_sparameter_table_array

        Creates an s-parameter de-embedding table for the port from the input data.

        If you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `De-embedding Overview<https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

            frequencies (numpy.array(dtype=numpy.float64)): Specifies the frequencies for the SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            sparameter_table (numpy.array(dtype=numpy.complex128)): Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.

            sparameter_orientation (enums.SparameterOrientation): Specifies the orientation of the input data relative to the port on the DUT port.

                **Defined Values** :

                +-----------------------------------------+----------------+-----------------------------------------------------+
                | Name                                    | Value          | Description                                         |
                +=========================================+================+=====================================================+
                | SparameterOrientation.PORT1_TOWARDS_DUT | 24000 (0x5dc0) | Port 1 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+
                | SparameterOrientation.PORT2_TOWARDS_DUT | 24001 (0x5dc1) | Port 2 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+

        '''
        if (str(type(sparameter_table)).find("'numpy.ndarray'") != -1) or (str(type(frequencies)).find("'numpy.ndarray'") != -1):
            if sparameter_table.ndim == 3:
                if frequencies.size == sparameter_table.shape[0]:
                    if sparameter_table.shape[1] == sparameter_table.shape[2]:
                        number_of_ports = sparameter_table.shape[1]
                        sparameter_table_size = sparameter_table.size
                        return self._create_deembedding_sparameter_table_array(port, table_name, frequencies, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation)
                    else:
                        raise ValueError("Row and column count of sparameter table should be equal. Table row count is {} and column count is {}.".format(sparameter_table.shape[1], sparameter_table.shape[2]))
                else:
                    raise ValueError("Frequencies count does not match the sparameter table count. Frequencies count is {} and sparameter table count is {}.".format(frequencies.size, sparameter_table.shape[0]))
            else:
                raise ValueError("Unsupported array dimension. Is {}, expected 3".format(sparameter_table.ndim))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array.")

    def get_deembedding_sparameters(self):
        '''get_deembedding_sparameters

        Returns the S-parameters used for de-embedding a measurement on the selected port.

        This includes interpolation of the parameters based on the configured carrier frequency. This method returns an empty array if no de-embedding is done.

        If you want to call this method just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Note: The port orientation for the returned S-parameters is normalized to SparameterOrientation.PORT1_TOWARDS_DUT.

        Returns:
            sparameters (numpy.array(dtype=numpy.complex128)): Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.

        '''
        import numpy as np
        number_of_ports = self._get_deembedding_table_number_of_ports()
        sparameter_array_size = number_of_ports ** 2
        sparameters = np.full((number_of_ports, number_of_ports), 0 + 0j, dtype=np.complex128)
        _, number_of_ports = self._get_deembedding_sparameters(sparameters, sparameter_array_size)
        sparameters = sparameters.reshape((number_of_ports, number_of_ports))
        return sparameters

    @ivi_synchronized
    def get_all_named_waveform_names(self):
        r'''get_all_named_waveform_names

        Return names of the waveforms present in the memory.

        **Supported Devices** :PXIe-5830/5831/5840/5841/5842E

        Returns:
            waveform_names (str): Returns a string having waveform names separated by commas.

            actual_buffer_size (int): Fetch the number of bytes needed to pass in the BUFFER_SIZE parameter.

                It can be fetch by passing VI_NULL in the WAVEFORM_NAMES parameter.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        waveform_names, actual_buffer_size = self._interpreter.get_all_named_waveform_names()
        return _converters.convert_comma_separated_string_to_list(waveform_names), actual_buffer_size

    @ivi_synchronized
    def get_all_script_names(self):
        r'''get_all_script_names

        Return names of the scripts present in the memory.

        **Supported Devices** :PXIe-5830/5831/5840/5841/5842E

        Returns:
            script_names (str): Returns a string having script names separated by commas.

            actual_buffer_size (int): Fetch the number of bytes needed to pass in the BUFFER_SIZE parameter.

                It can be fetch by passing VI_NULL in the SCRIPT_NAMES parameter.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        script_names, actual_buffer_size = self._interpreter.get_all_script_names()
        return script_names, actual_buffer_size

    @ivi_synchronized
    def get_channel_name(self, index):
        r'''get_channel_name

        Returns the channel string that is in the channel table at an index you specify.

        **Supported Devices** : PXI-5670/5671, PXIe-5672/5673/5673E

        Args:
            index (int): Specifies a one-based index into the channel table.


        Returns:
            name (str): Returns a channel string from the channel table at the index you specify in the Index parameter. Do not modify the contents of the channel string.

        '''
        name = self._interpreter.get_channel_name(index)
        return name

    @ivi_synchronized
    def _get_deembedding_sparameters(self, sparameters, sparameters_array_size):
        r'''_get_deembedding_sparameters

        Returns the S-parameters used for de-embedding a measurement on the selected port.

        This includes interpolation of the parameters based on the configured carrier frequency. This method returns an empty array if no de-embedding is done.

        If you want to call this method just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Note: The port orientation for the returned S-parameters is normalized to SparameterOrientation.PORT1_TOWARDS_DUT.

        Args:
            sparameters (numpy.array(dtype=numpy.complex128)): Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.

            sparameters_array_size (int): Specifies the size of the array that is returned by the SPARAMETERS output.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            number_of_sparameters (int): Returns the number of S-parameters.

            number_of_ports (int): Returns the number of S-parameter ports. The **sparameter** array is always *n* x *n*, where span *n* is the number of ports.

        '''
        import numpy

        if type(sparameters) is not numpy.ndarray:
            raise TypeError('sparameters must be {0}, is {1}'.format(numpy.ndarray, type(sparameters)))
        if numpy.isfortran(sparameters) is True:
            raise TypeError('sparameters must be in C-order')
        if sparameters.dtype is not numpy.dtype('complex128'):
            raise TypeError('sparameters must be numpy.ndarray of dtype=complex128, is ' + str(sparameters.dtype))
        number_of_sparameters, number_of_ports = self._interpreter.get_deembedding_sparameters(sparameters, sparameters_array_size)
        return number_of_sparameters, number_of_ports

    @ivi_synchronized
    def _get_deembedding_table_number_of_ports(self):
        r'''_get_deembedding_table_number_of_ports

        Returns the number of S-parameter ports.

        Returns:
            number_of_ports (int): Returns the number of S-parameter ports. The **sparameter** array is always *n* x *n*, where span *n* is the number of ports.

        '''
        number_of_ports = self._interpreter.get_deembedding_table_number_of_ports()
        return number_of_ports

    @ivi_synchronized
    def _get_external_calibration_last_date_and_time(self):
        r'''_get_external_calibration_last_date_and_time

        Returns the date and time of the last successful external calibration.

        The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            year (int): Returns the year of the last successful calibration.

            month (int): Returns the month of the last successful calibration.

            day (int): Returns the day of the last successful calibration.

            hour (int): Returns the hour of the last successful calibration.

            minute (int): Returns the minute of the last successful calibration.

            second (int): Returns the second of the last successful calibration.

        '''
        year, month, day, hour, minute, second = self._interpreter.get_external_calibration_last_date_and_time()
        return year, month, day, hour, minute, second

    @ivi_synchronized
    def get_external_calibration_last_date_and_time(self):
        '''get_external_calibration_last_date_and_time

        Returns the date and time of the last successful external calibration.

        The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            last_cal_datetime (hightime.datetime):

        '''
        year, month, day, hour, minute, second = self._get_external_calibration_last_date_and_time()
        return hightime.datetime(year, month, day, hour, minute, second)

    @ivi_synchronized
    def get_self_calibration_last_date_and_time(self, module):
        '''get_self_calibration_last_date_and_time

        Returns the date and time of the last successful self-calibration.

        The time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            module (enums.Module): Specifies from which stand-alone module to retrieve the last successful self-calibration date and time.


        Returns:
            last_cal_datetime (hightime.datetime):

        '''
        year, month, day, hour, minute, second = self._get_self_calibration_date_and_time(module)
        return hightime.datetime(year, month, day, hour, minute, second)

    @ivi_synchronized
    def get_max_settable_power(self):
        r'''get_max_settable_power

        Returns the maximum settable output power level for the current configuration.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Returns:
            value (float): Returns maximum settable power level in dBm.

        '''
        value = self._interpreter.get_max_settable_power()
        return value

    @ivi_synchronized
    def _get_self_calibration_date_and_time(self, module):
        r'''_get_self_calibration_date_and_time

        Returns the date and time of the last successful self-calibration.

        The time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            module (enums.Module): Specifies from which stand-alone module to retrieve the last successful self-calibration date and time.


        Returns:
            year (int): Returns the year of the last successful calibration.

            month (int): Returns the month of the last successful calibration.

            day (int): Returns the day of the last successful calibration.

            hour (int): Returns the hour of the last successful calibration.

            minute (int): Returns the minute of the last successful calibration.

            second (int): Returns the second of the last successful calibration.

        '''
        if type(module) is not enums.Module:
            raise TypeError('Parameter module must be of type ' + str(enums.Module))
        year, month, day, hour, minute, second = self._interpreter.get_self_calibration_date_and_time(module)
        return year, month, day, hour, minute, second

    @ivi_synchronized
    def get_self_calibration_temperature(self, module):
        r'''get_self_calibration_temperature

        Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

        **Supported Devices** : PXI-5610, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860

        Args:
            module (enums.Module): Specifies from which stand-alone module to retrieve the last successful self-calibration temperature.
                                    **Default Value** : Module.PRIMARY_MODULE
                                    **Defined Values** :

                +-----------------------+----------------+---------------------------------------------------------------------+
                | Name                  | Value          | Description                                                         |
                +=======================+================+=====================================================================+
                | Module.PRIMARY_MODULE | 13000 (0x32c8) | The stand-alone device or the main module in a multi-module device. |
                +-----------------------+----------------+---------------------------------------------------------------------+
                | Module.AWG            | 13001 (0x32c9) | The AWG associated with the primary module.                         |
                +-----------------------+----------------+---------------------------------------------------------------------+
                | Module.LO             | 13002 (0x32ca) | The LO associated with the primary module.                          |
                +-----------------------+----------------+---------------------------------------------------------------------+


        Returns:
            temperature (float): Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

        '''
        if type(module) is not enums.Module:
            raise TypeError('Parameter module must be of type ' + str(enums.Module))
        temperature = self._interpreter.get_self_calibration_temperature(module)
        return temperature

    @ivi_synchronized
    def get_terminal_name(self, signal, signal_identifier):
        r'''get_terminal_name

        Returns the fully-qualified name of the specified signal.

        The fully-qualified name is helpful to automatically route signals in a multisegment chassis.

        **Supported Devices** : PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

        `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

        Args:
            signal (enums.Signal): Specifies the signal to query. **Defined Values** :

                +--------------------------------------------+---------+--------------------------------------------+
                | Name                                       | Value   | Description                                |
                +============================================+=========+============================================+
                | Signal.START_TRIGGER                       | 0 (0x0) | Exports a Start Trigger.                   |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.SCRIPT_TRIGGER                      | 1 (0x1) | Exports a Script Trigger.                  |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.MARKER_EVENT                        | 2 (0x2) | Exports a Marker Event.                    |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.REF_CLOCK                           | 3 (0x3) | Exports the Reference Clock.               |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.STARTED_EVENT                       | 4 (0x4) | Exports a Started Event.                   |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.DONE_EVENT                          | 5 (0x5) | Exports a Done Event.                      |
                +--------------------------------------------+---------+--------------------------------------------+
                | NIRFSG_VAL_CONFIGURATION_LIST_STEP_TRIGGER | 6 (0x6) | Exports a Configuration List Step Trigger. |
                +--------------------------------------------+---------+--------------------------------------------+
                | NIRFSG_VAL_CONFIGURATION_SETTLED_EVENT     | 7 (0x7) | Exports a Configuration Settled Event.     |
                +--------------------------------------------+---------+--------------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            signal_identifier (str): Specifies which instance of the selected signal to query. This parameter is necessary when you set the SIGNAL parameter to NIRFSG_VAL_SCRIPT_TRIGGER or Signal.MARKER_EVENT  . Otherwise, set the SIGNAL_IDENTIFIER parameter to "" (empty string). **Possible Values** :

                +------------------+-----------------------------+
                | Possible Value   | Description                 |
                +==================+=============================+
                | "marker0"        | Specifies Marker 0.         |
                +------------------+-----------------------------+
                | "marker1"        | Specifies Marker 1.         |
                +------------------+-----------------------------+
                | "marker2"        | Specifies Marker 2.         |
                +------------------+-----------------------------+
                | "marker3"        | Specifies Marker 3.         |
                +------------------+-----------------------------+
                | "scriptTrigger0" | Specifies Script Trigger 0. |
                +------------------+-----------------------------+
                | "scriptTrigger1" | Specifies Script Trigger 1. |
                +------------------+-----------------------------+
                | "scriptTrigger2" | Specifies Script Trigger 2. |
                +------------------+-----------------------------+
                | "scriptTrigger3" | Specifies Script Trigger 3. |
                +------------------+-----------------------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            terminal_name (str): Returns the string to use as the source for other devices.

        '''
        if type(signal) is not enums.Signal:
            raise TypeError('Parameter signal must be of type ' + str(enums.Signal))
        terminal_name = self._interpreter.get_terminal_name(signal, signal_identifier)
        return terminal_name

    def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string=""):
        r'''_init_with_options

        Opens a session to the device you specify as the RESOURCE_NAME and returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        This method also configures the device through the OPTION_STRING input.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Simulating an NI RF Signal Generator <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/simulate.html>`_

        Note: For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending /*ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Specifies the resource name of the device to initialize.

                For NI-DAQmx devices, the syntax is the device name specified in MAX. Typical default names for NI-DAQmx devices in MAX are Dev2 or PXISlot2. You can rename an NI-DAQmx device in MAX.

                You can also specify the name of an IVI logical name configured with the IVI Configuration utility. Refer to the *IVI* topic of the *Measurement & Automation Explorer Help* for more information.

                Note: NI-RFSG device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use an IVI logical name, make sure the name is identical to the name shown in the IVI Configuration Utility.

            id_query (bool): Specifies whether you want NI-RFSG to perform an ID query.

                **Defined Values** :

                +-----------+--------------------------+
                | Value     | Description              |
                +===========+==========================+
                | True (1)  | Perform ID query.        |
                +-----------+--------------------------+
                | False (0) | Do not perform ID query. |
                +-----------+--------------------------+

            reset_device (bool): Specifies whether you want to reset the NI-RFSG device during the initialization procedure.

                **Defined Values** :

                +-----------+----------------------+
                | Value     | Description          |
                +===========+======================+
                | True (1)  | Reset device.        |
                +-----------+----------------------+
                | False (0) | Do not reset device. |
                +-----------+----------------------+

            option_string (dict): Specifies the initial value of certain properties for the session. The following table lists the properties and the name you pass in this parameter to identify the property.

                The format of this string consists of the following relations:
                "AttributeName=Value"

                where
                *AttributeName* is the name of the property and *Value* is the value to which the property is set. To set multiple properties, separate their assignments with a comma, as shown in the following option string:

                "RangeCheck=1,QueryInstrStatus=0,Cache=1,DriverSetup=AWG:pxi1slot4"

                The `DriverSetup string <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/driver_setup_string.html>`_ is required in order to simulate a specific device.

                +------------------+-------------------------+
                | Name             | Property Name           |
                +==================+=========================+
                | RangeCheck       | range_check             |
                +------------------+-------------------------+
                | QueryInstrStatus | query_instrument_status |
                +------------------+-------------------------+
                | Cache            | cache                   |
                +------------------+-------------------------+
                | RecordCoercions  | record_coercions        |
                +------------------+-------------------------+
                | Simulate         | simulate                |
                +------------------+-------------------------+


        Returns:
            new_vi (int): Returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        '''
        option_string = _converters.convert_init_with_options_dictionary(option_string)
        new_vi = self._interpreter.init_with_options(resource_name, id_query, reset_device, option_string)
        return new_vi

    @ivi_synchronized
    def _initiate(self):
        r'''_initiate

        Initiates signal generation, causing the NI-RFSG device to leave the Configuration state and enter the Generation state.

        If the settings have not been committed to the device before you call this method, they are committed by this method. The operation returns when the RF output signal settles. To return to the Configuration state, call the abort method.

        **Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_
        '''
        self._interpreter.initiate()

    @ivi_synchronized
    def perform_power_search(self):
        r'''perform_power_search

        Performs a power search if the alc_control property is disabled.

        Calling this method disables modulation for a short time while the device levels the output signal.

        **Supported Devices** : PXIe-5654 with PXIe-5696

        **Related Topics**

        `Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_

        Note: Power search temporarily enables the ALC, so ensure the appropriate included cable is connected between the PXIe-5654 ALCIN connector and the PXIe-5696 ALCOUT connector to successfully perform a power search.
        '''
        self._interpreter.perform_power_search()

    @ivi_synchronized
    def perform_thermal_correction(self):
        r'''perform_thermal_correction

        Corrects for any signal drift due to environmental temperature variation when generating the same signal for extended periods of time without a parameter change.

        Under normal circumstances of short-term signal generation, NI-RFSG performs thermal correction automatically by ensuring stable power levels, and you do not need to call this method.

        Use this method when generating the same signal for an extended period of time in a temperature-fluctuating environment. The NI-RFSG device must be in the Generation state before calling this method.

        **Supported Devices** : PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Thermal Management <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_management.html>`_

        `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_
        '''
        self._interpreter.perform_thermal_correction()

    @ivi_synchronized
    def query_arb_waveform_capabilities(self):
        r'''query_arb_waveform_capabilities

        Queries and returns the waveform capabilities of the NI-RFSG device.

        These capabilities are related to the current device configuration. The NI-RFSG device must be in the Configuration or the Generation state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            max_number_waveforms (int): Returns the value of the arb_max_number_waveforms property. This value is the maximum number of waveforms you can write.

            waveform_quantum (int): Returns the value of the arb_waveform_quantum property. If the waveform quantum is *q*, then the size of the waveform that you write should be a multiple of *q*. The units are expressed in samples.

            min_waveform_size (int): Returns the value of the arb_waveform_size_min property. The number of samples of the waveform that you write must be greater than or equal to this value.

            max_waveform_size (int): Returns the value of the arb_waveform_size_max property. The number of samples of the waveform that you write must be less than or equal to this value.

        '''
        max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size = self._interpreter.query_arb_waveform_capabilities()
        return max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size

    @ivi_synchronized
    def read_and_download_waveform_from_file_tdms(self, waveform_name, file_path, waveform_index):
        r'''read_and_download_waveform_from_file_tdms

        Reads the waveforms from a TDMS file and downloads one waveform into each of the NI RF vector signal generators.

        This method reads the following information from the TDMS file and writes it into the NI-RFSG session:

        - Sample Rate
        - PAPR
        - Runtime Scaling
        - RF Blanking Marker Locations
        - RF Blanking Enabled
        - Burst Start Locations
        - Burst Stop Locations
        - RF Blanking Marker Source
        - Signal Bandwidth
        - Waveform Size

        If RF blanking marker locations are present in the file but burst locations are not present, burst locations are calculated from RF blanking marker locations and stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Args:
            waveform_name (str): Specifies the name used to store the waveform. This string is case-insensitive.

                Example:

                "waveform::waveform0"

            file_path (str): Specifies the absolute path to the TDMS file from which the NI-RFSG reads the waveforms.

            waveform_index (int): Specifies the index of the waveform to be read from the TDMS file.

        '''
        self._interpreter.read_and_download_waveform_from_file_tdms(waveform_name, file_path, waveform_index)

    @ivi_synchronized
    def reset_device(self):
        r'''reset_device

        Performs a hard reset on the device which consists of the following actions:

        - Signal generation is stopped.
        - All routes are released.
        - External bidirectional terminals are tristated.
        - FPGAs are reset.
        - Hardware is configured to its default state.
        - All session properties are reset to their default states.

        During a device reset, routes of signals between this and other devices are released, regardless of which device created the route.

        - PXI-5610, PXI-5670/5671, PXIe-5672-- After calling this method, the device requires 25 seconds before returning to full functionality. NI-RFSG enforces this condition by adding a wait, if needed, the next time you try to access the device.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E

        **Related Topics**

        `Thermal Shutdown <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_shutdown_monitoring_5650_5651_5652.html>`_

        Note: You must call the reset_device method if the NI-RFSG device has shut down because of a high-temperature condition.
        '''
        self._interpreter.reset_device()

    @ivi_synchronized
    def reset_with_defaults(self):
        r'''reset_with_defaults

        Performs a software reset of the device, returning it to the default state and applying any initial default settings from the IVI Configuration Store.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696,PXI-5670/5671, PXIe-5672/5673/5673E
        '''
        self._interpreter.reset_with_defaults()

    @ivi_synchronized
    def reset_with_options(self, steps_to_omit):
        r'''reset_with_options

        Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes.

        By default, this method exhibits the same behavior as Reset. You can specify steps to omit using the steps to omit parameter. For example, if you specify ResetWithOptionsStepsToOmit.ROUTES for the STEPS_TO_OMIT parameter, this method does not release signal routes during the reset process.

        When routes of signals between two devices are released, they are released regardless of which device created the route.

        To avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSA sessions, NI recommends using this method instead of Reset, with STEPS_TO_OMIT set to ResetWithOptionsStepsToOmit.ROUTES.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            steps_to_omit (Bitwise combination of enums.ResetWithOptionsStepsToOmit flags): Specifies a list of steps to skip during the reset process. The default value is ResetWithOptionsStepsToOmit.NONE, which specifies that no step is omitted during reset. **Defined Values** :

                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Name                                           | Value   | Description                                                                                                                                                                                                |
                +================================================+=========+============================================================================================================================================================================================================+
                | ResetWithOptionsStepsToOmit.NONE               | 0 (0x0) | No step is omitted during reset.                                                                                                                                                                           |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.WAVEFORMS          | 1 (0x1) | Omits clearing waveforms.                                                                                                                                                                                  |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.SCRIPTS            | 2 (0x2) | Omits clearing scripts.                                                                                                                                                                                    |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.ROUTES             | 4 (0x4) | Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset. |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.DEEMBEDDING_TABLES | 8 (0x8) | Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.                                                                                                              |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note: ResetWithOptionsStepsToOmit.ROUTES is not supported in external calibration or alignment sessions.
                You can combine multiple enums.ResetWithOptionsStepsToOmit flags using the bitwise OR (|) operator.

        '''
        if type(steps_to_omit) is not enums.ResetWithOptionsStepsToOmit:
            raise TypeError('Parameter steps_to_omit must be of type ' + str(enums.ResetWithOptionsStepsToOmit))
        self._interpreter.reset_with_options(steps_to_omit)

    @ivi_synchronized
    def revision_query(self):
        r'''revision_query

        Returns the revision numbers of the NI-RFSG driver and the instrument firmware.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            instrument_driver_revision (str): Returns the value of the specific_driver_revision property in the form of a string.

                You must pass a ViChar array with at least 256 bytes.

            firmware_revision (str): Returns the value of the instrument_firmware_revision property in the form of a string.

                You must pass a ViChar array with at least 256 bytes.

        '''
        instrument_driver_revision, firmware_revision = self._interpreter.revision_query()
        return instrument_driver_revision, firmware_revision

    @ivi_synchronized
    def select_arb_waveform(self, name):
        r'''select_arb_waveform

        Specifies the waveform that is generated upon a call to the _initiate method when the generation_mode property is set to GenerationMode.ARB_WAVEFORM.

        You must specify a waveform using the NAME parameter if you have written multiple waveforms. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            name (str): Specifies the name of the stored waveform to generate. This is a case-insensitive alphanumeric string that does not use reserved words. NI-RFSG sets the arb_selected_waveform property to this value.

        '''
        self._interpreter.select_arb_waveform(name)

    @ivi_synchronized
    def self_cal(self):
        r'''self_cal

        Performs an internal self-calibration on the device and associated modules that support self-calibration.

        If the calibration is successful, new calibration data and constants are stored in the onboard nonvolatile memory of the module.

        The PXIe-5841 maintains separate self-calibration data for both the PXIe-5841 standalone and when associated with the PXIe-5655. Use this method once for each intended configuration.

        **Supported Devices** : PXI-5610, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note: If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this method runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate.
        '''
        self._interpreter.self_cal()

    @ivi_synchronized
    def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level):
        r'''self_calibrate_range

        Self-calibrates all configurations within the specified frequency and peak power level limits.

        Self-calibration range data is valid until you restart the system or call the clear_self_calibrate_range method.

        NI recommends that no external signals are present on the RF In or IQ In ports during the calibration.

        For best results, NI recommends that you perform self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit certain steps for faster calibration.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

        Note: - This method does not update self-calibration date and temperature.

         - If there is an existing NI-RFSA session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this method runs.

         - If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842 while this method runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate.

        Args:
            steps_to_omit (Bitwise combination of enums.SelfCalibrateRangeStepsToOmit flags): Specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that no calibration steps are omitted.

                **Default Value** : SelfCalibrateRangeStepsToOmit.OMIT_NONE

                **Defined Values:**

                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | Name                                                | Value     | Description                                                                                                         |
                +=====================================================+===========+=====================================================================================================================+
                | SelfCalibrateRangeStepsToOmit.OMIT_NONE             | 0 (0x0)   | No calibration steps are omitted.                                                                                   |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.LO_SELF_CAL           | 1 (0x1)   | Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.                       |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.POWER_LEVEL_ACCURACY  | 2 (0x2)   | Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted. |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.RESIDUAL_LO_POWER     | 4 (0x4)   | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.         |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.IMAGE_SUPPRESSION     | 8 (0x8)   | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.   |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.SYNTHESIZER_ALIGNMENT | 16 (0x10) | Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.    |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+

                Note: You can combine multiple enums.SelfCalibrateRangeStepsToOmit flags using the bitwise OR (|) operator.

            min_frequency (float): Specifies the minimum frequency to calibrate.

            max_frequency (float): Specifies the maximum frequency to calibrate.

            min_power_level (float): Specifies the minimum power level to calibrate.

            max_power_level (float): Specifies the maximum power level to calibrate.

        '''
        if type(steps_to_omit) is not enums.SelfCalibrateRangeStepsToOmit:
            raise TypeError('Parameter steps_to_omit must be of type ' + str(enums.SelfCalibrateRangeStepsToOmit))
        self._interpreter.self_calibrate_range(steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level)

    @ivi_synchronized
    def self_test(self, self_test_message):
        r'''self_test

        Performs a self-test on the NI-RFSG device and returns the test results.

        This method performs a simple series of tests to ensure that the NI-RFSG device is powered up and responding.

        This method does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this method. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Device Warm-Up <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/warmup.html>`_

        Args:
            self_test_message (str): Returns the self-test response string from the NI-RFSG device. For an explanation of the string contents, refer to the **status** parameter of this method.

                You must pass a ViChar array with at least 256 bytes.


        Returns:
            self_test_result (int): This parameter contains the value returned from the NI-RFSG device self test.

                +----------------+------------------+
                | Self-Test Code | Description      |
                +================+==================+
                | 0              | Self test passed |
                +----------------+------------------+
                | 1              | Self test failed |
                +----------------+------------------+

        '''
        self_test_result = self._interpreter.self_test(self_test_message)
        return self_test_result

    @ivi_synchronized
    def set_arb_waveform_next_write_position(self, waveform_name, relative_to, offset):
        r'''set_arb_waveform_next_write_position

        Configures the start position to use for writing a waveform before calling the WriteArbWaveform method.

        This method allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the **name** input of the allocate_arb_waveform method or the WriteArbWaveform method. Subsequent writes to that waveform begin where the last write ended, unless this method is called again.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note: If you use this method to write the waveform that is currently generating, an undefined output may result.

        Args:
            waveform_name (str): Specifies the name of the waveform. This string is case-insensitive and alphanumeric, and it cannot use `reserved words <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. The position and OFFSET together determine where to start loading data into the waveform.

                **Defined Values:**

                +------------------------------+---------------+------------------------------------------------------------------+
                | Name                         | Value         | Description                                                      |
                +==============================+===============+==================================================================+
                | RelativeTo.START_OF_WAVEFORM | 8000 (0x1f40) | The reference position is relative to the start of the waveform. |
                +------------------------------+---------------+------------------------------------------------------------------+
                | RelativeTo.CURRENT_POSITION  | 8001 (0x1f41) | The reference position is relative to the current position.      |
                +------------------------------+---------------+------------------------------------------------------------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            offset (int): Specifies the offset from the **relative to** parameter at which to start loading the data into the waveform.

        '''
        if type(relative_to) is not enums.RelativeTo:
            raise TypeError('Parameter relative_to must be of type ' + str(enums.RelativeTo))
        self._interpreter.set_arb_waveform_next_write_position(waveform_name, relative_to, offset)

    @ivi_synchronized
    def wait_until_settled(self, max_time_milliseconds):
        r'''wait_until_settled

        Waits until the RF output signal has settled. This method is useful for devices that support changes while in the Generation state.

        Call this method after making a dynamic change to wait for the output signal to settle.

        You can also call this method after calling the commit method to wait for changes to settle. The wait_until_settled method is not required after calling the _initiate method because the _initiate automatically waits for the output to settle.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            max_time_milliseconds (int): Specifies the maximum time the method waits for the output to settle. If the maximum time is exceeded, this method returns an error. The units are expressed in milliseconds.

                **Default Value** : 10000

        '''
        self._interpreter.wait_until_settled(max_time_milliseconds)

    @ivi_synchronized
    def _write_arb_waveform_complex_f32(self, waveform_name, waveform_data_array, more_data_pending):
        r'''_write_arb_waveform_complex_f32

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the complex baseband data in the form of complex singles. If the waveform to write is already allocated using the allocate_arb_waveform method, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, you can call this method when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy.array(dtype=numpy.complex64)): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

            more_data_pending (bool): Specifies whether or not the data block contains the end of the waveform. Set this parameter to True to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the WAVEFORM_NAME parameter. Set more_data_pending to False to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        '''
        import numpy

        if type(waveform_data_array) is not numpy.ndarray:
            raise TypeError('waveform_data_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data_array)))
        if numpy.isfortran(waveform_data_array) is True:
            raise TypeError('waveform_data_array must be in C-order')
        if waveform_data_array.dtype is not numpy.dtype('complex64'):
            raise TypeError('waveform_data_array must be numpy.ndarray of dtype=complex64, is ' + str(waveform_data_array.dtype))
        if waveform_data_array.ndim != 1:
            raise TypeError('waveform_data_array must be numpy.ndarray of dimension=1, is ' + str(waveform_data_array.ndim))
        self._interpreter.write_arb_waveform_complex_f32(waveform_name, waveform_data_array, more_data_pending)

    @ivi_synchronized
    def _write_arb_waveform_complex_f64(self, waveform_name, waveform_data_array, more_data_pending):
        r'''_write_arb_waveform_complex_f64

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the complex baseband data in the form of complex doubles. If the waveform to write is already allocated using the allocate_arb_waveform, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, you can call this method when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy.array(dtype=numpy.complex128)): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

            more_data_pending (bool): Specifies whether or not the data block contains the end of the waveform. Set this parameter to True to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the **name** parameter. Set more_data_pending to False to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.

        '''
        import numpy

        if type(waveform_data_array) is not numpy.ndarray:
            raise TypeError('waveform_data_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data_array)))
        if numpy.isfortran(waveform_data_array) is True:
            raise TypeError('waveform_data_array must be in C-order')
        if waveform_data_array.dtype is not numpy.dtype('complex128'):
            raise TypeError('waveform_data_array must be numpy.ndarray of dtype=complex128, is ' + str(waveform_data_array.dtype))
        if waveform_data_array.ndim != 1:
            raise TypeError('waveform_data_array must be numpy.ndarray of dimension=1, is ' + str(waveform_data_array.ndim))
        self._interpreter.write_arb_waveform_complex_f64(waveform_name, waveform_data_array, more_data_pending)

    @ivi_synchronized
    def _write_arb_waveform_complex_i16(self, waveform_name, waveform_data_array):
        r'''_write_arb_waveform_complex_i16

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the interleaved I/Q data of a complex baseband signal. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, this method can be called when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: This method only supports PowerLevelType.PEAK mode as specified in the power_level_type property. If you download a waveform when using this method, you cannot set the power_level_type to PowerLevelType.AVERAGE without causing error in the output.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy.array(dtype=numpy.int16)): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

        '''
        import numpy

        if type(waveform_data_array) is not numpy.ndarray:
            raise TypeError('waveform_data_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data_array)))
        if numpy.isfortran(waveform_data_array) is True:
            raise TypeError('waveform_data_array must be in C-order')
        if waveform_data_array.dtype is not numpy.dtype('int16'):
            raise TypeError('waveform_data_array must be numpy.ndarray of dtype=int16, is ' + str(waveform_data_array.dtype))
        if waveform_data_array.ndim != 1:
            raise TypeError('waveform_data_array must be numpy.ndarray of dimension=1, is ' + str(waveform_data_array.ndim))
        self._interpreter.write_arb_waveform_complex_i16(waveform_name, waveform_data_array)

    def write_arb_waveform(self, waveform_name, waveform_data_array, more_data_pending=False):
        '''write_arb_waveform

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the complex baseband data in the form of numpy array of numpy.complex64 or numpy.complex128 or interleaved numpy array of numpy.int16. If the waveform to write is already allocated using the allocate_arb_waveform, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, you can call this method when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.
        If you are writing interleaved numpy array of numpy.int16, then this method only supports PowerLevelType.PEAK mode as specified in the power_level_type property. If you download a waveform as interleaved numpy array of numpy.int16 when using this method, you cannot set the power_level_type to PowerLevelType.AVERAGE without causing error in the output.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy array of numpy.complex64, numpy array of numpy.complex128 or interleaved complex data in the form of numpy array of numpy.int16): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

            more_data_pending (bool): Specifies whether or not the data block contains the end of the waveform. Set this parameter to True to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the **name** parameter. Set more_data_pending to False to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.

        '''
        import numpy
        if str(type(waveform_data_array)).find("'numpy.ndarray'") != -1:
            if waveform_data_array.dtype == numpy.complex128:
                return self._write_arb_waveform_complex_f64(waveform_name, waveform_data_array, more_data_pending)
            elif waveform_data_array.dtype == numpy.complex64:
                return self._write_arb_waveform_complex_f32(waveform_name, waveform_data_array, more_data_pending)
            elif waveform_data_array.dtype == numpy.int16:
                return self._write_arb_waveform_complex_i16(waveform_name, waveform_data_array)
            else:
                raise TypeError("Unsupported datatype. Is {}, expected {} or {} or {}".format(waveform_data_array.dtype, numpy.complex128, numpy.complex64, numpy.int16))
        else:
            raise TypeError("Unsupported datatype. Expected numpy array of {} or {} or {}".format(numpy.complex128, numpy.complex64, numpy.int16))

    @ivi_synchronized
    def write_script(self, script):
        r'''write_script

        Writes a script to the device to control waveform generation in Script mode.

        First, configure your device for Script mode by setting the generation_mode property. The NI-RFSG device must be in the Configuration state before calling the write_script method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_--Refer to this topic for more information about VST restrictions on scripts.

        `Common Scripting Use Cases <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_use_cases.html>`_

        Note: If you are using an RF vector signal transceiver (VST) device, some script instructions may not be supported.

        Args:
            script (str): Specifies a string containing a syntactically correct script. NI-RFSG supports multiple scripts that are selected with the selected_script property. Refer to `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_ for more information about using scripts.

        '''
        self._interpreter.write_script(script)

    def _close(self):
        r'''_close

        Aborts any signal generation in progress and destroys the instrument driver session.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_
        '''
        self._interpreter.close()

    @ivi_synchronized
    def reset(self):
        r'''reset

        Resets all properties to their default values and moves the NI-RFSG device to the Configuration state.

        This method aborts the generation, deletes all de-embedding tables, clears all routes, and resets session properties to their initial values. During a reset, routes of signals between this and other devices are released, regardless of which device created the route.

        Generally, calling this method instead of the reset_device method is acceptable. The Reset method executes faster than the reset_device method.

        To avoid resetting routes on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSA sessions, NI recommends using the reset_with_options method, with **stepsToOmit** set to ResetWithOptionsStepsToOmit.ROUTES .

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note: This method resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG.
        '''
        self._interpreter.reset()
