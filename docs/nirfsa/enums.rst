Enums
=====

Enums used in NI-RFSA

.. py:currentmodule:: nirfsa


AcquisitionType
---------------

.. py:class:: AcquisitionType

    .. py:attribute:: AcquisitionType.IQ



        Configures NI-RFSA for I/Q acquisitions.

        



    .. py:attribute:: AcquisitionType.SPECTRUM



        Configures NI-RFSA for spectrum acquisitions.

        



Action
------

.. py:class:: Action

    .. py:attribute:: Action.COMMIT



        The new calibration constants are stored in the EEPROM.

        



    .. py:attribute:: Action.ABORT



        The old calibration constants are kept, and the new ones are discarded.

        



AdvanceTriggerDigitalEdgeEdge
-----------------------------

.. py:class:: AdvanceTriggerDigitalEdgeEdge

    .. py:attribute:: AdvanceTriggerDigitalEdgeEdge.RISING



        The trigger asserts on the rising edge of the signal.

        



    .. py:attribute:: AdvanceTriggerDigitalEdgeEdge.FALLING



        The trigger asserts on the falling edge of the signal.

        



AdvanceTriggerType
------------------

.. py:class:: AdvanceTriggerType

    .. py:attribute:: AdvanceTriggerType.NONE



        No Advance Trigger is configured.

        



    .. py:attribute:: AdvanceTriggerType.DIGITAL_EDGE



        The Advance Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the :py:attr:`nirfsa.Session.digital_edge_advance_trigger_source` property.

        



    .. py:attribute:: AdvanceTriggerType.SOFTWARE_EDGE



        The Advance Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the :py:meth:`nirfsa.Session.send_software_edge_trigger` method and selecting :py:data:`~nirfsa.NIRFSA_VAL_ADVANCE_TRIGGER` as the **trigger** parameter.

        



AllowOutOfSpecificationUserSettings
-----------------------------------

.. py:class:: AllowOutOfSpecificationUserSettings

    .. py:attribute:: AllowOutOfSpecificationUserSettings.DISABLED



        Disables out-of-specification user settings.

        



    .. py:attribute:: AllowOutOfSpecificationUserSettings.ENABLED



        Enables out-of-specification user settings.

        



ArmReferenceTriggerType
-----------------------

.. py:class:: ArmReferenceTriggerType

    .. py:attribute:: ArmReferenceTriggerType.NONE



        No Arm Reference Trigger is configured.

        



    .. py:attribute:: ArmReferenceTriggerType.DIGITAL_EDGE



        The Arm Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the :py:attr:`nirfsa.Session.digital_edge_arm_ref_trigger_source` property.

        



    .. py:attribute:: ArmReferenceTriggerType.SOFTWARE_EDGE



        The Arm Reference Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the :py:meth:`nirfsa.Session.send_software_edge_trigger` method and selecting :py:data:`~nirfsa.SoftwareTriggerType.ARM_REF` as the **trigger** parameter.

        



CalToneMode
-----------

.. py:class:: CalToneMode

    .. py:attribute:: CalToneMode.DISABLED



        Disables the calibration tone for the associated signal path.

        



    .. py:attribute:: CalToneMode.CAL_TONE_LOWBAND_RF



        Injects the calibration tone into the low band RF signal path.

        



    .. py:attribute:: CalToneMode.CAL_TONE_HIGHBAND_RF



        Injects the calibration tone into the high band RF signal path.

        



    .. py:attribute:: CalToneMode.CAL_TONE_HIGHBAND_IF



        Injects the calibration tone into the high band IF signal path.

        



    .. py:attribute:: CalToneMode.CAL_TONE_LOWBAND_RF_WITHOUT_ALC



        Injects the calibration tone into the low band RF signal path, bypassing the ALC.

        



    .. py:attribute:: CalToneMode.CAL_TONE_COMB_GENERATOR



        Injects the calibration tone into the high band RF signal path through the Comb Generator.

        



CalibrateStep
-------------

.. py:class:: CalibrateStep

    .. py:attribute:: CalibrateStep.IF_ATTENUATION



        Initializes the IF Attenuation Calibration step. This step is not supported for the PXIe-5693.

        



    .. py:attribute:: CalibrateStep.IF_RESPONSE



        Initializes the IF Response Calibration step. This step is not supported for the PXIe-5603/5605 or PXIe-5693/5698.

        



    .. py:attribute:: CalibrateStep.IF_REF_LEVEL



        Initializes the Ref Level Calibration step. This step is not supported on the PXIe-5694.

        



    .. py:attribute:: CalibrateStep.LO_EXPORT



        Initializes the LO Export Calibration step. This step calibrates the output power of each LO to be within specification. This step is not supported on the PXIe-5601 or the PXIe-5693/5694/5698.

        



    .. py:attribute:: CalibrateStep.GAIN_REFERENCE



        Initializes the Gain Reference Calibration step. This step calibrates the calibration tone amplitude across supported calibration tone frequencies. This step is not supported on the PXIe-5601/5603/5605 or PXIe-5694.

        



ChannelCoupling
---------------

.. py:class:: ChannelCoupling

    .. py:attribute:: ChannelCoupling.AC



        Specifies that the RF input channel is AC-coupled. For low frequencies (<10 MHz), accuracy decreases because NI-RFSA does not calibrate the configuration.

        



    .. py:attribute:: ChannelCoupling.DC



        Specifies that the RF input channel is DC-coupled. NI-RFSA enforces a minimum RF attenuation for device protection.

        



ConditioningCalToneMode
-----------------------

.. py:class:: ConditioningCalToneMode

    .. py:attribute:: ConditioningCalToneMode.DISABLED



        Disables the calibration tone for the associated signal path.

        



    .. py:attribute:: ConditioningCalToneMode.CAL_TONE_LOWBAND_RF



        Injects the calibration tone into the low band RF signal path.

        



    .. py:attribute:: ConditioningCalToneMode.CAL_TONE_HIGHBAND_RF



        Injects the calibration tone into the high band RF signal path.

        



DeembeddingType
---------------

.. py:class:: DeembeddingType

    .. py:attribute:: DeembeddingType.NONE



        De-embedding is not applied to the measurement.

        



    .. py:attribute:: DeembeddingType.SCALAR



        De-embeds the measurement using only the gain term.

        



    .. py:attribute:: DeembeddingType.VECTOR



        De-embeds the measurement using the gain term and the reflection term.

        



DeviceResponseType
------------------

.. py:class:: DeviceResponseType

    .. py:attribute:: DeviceResponseType.DOWNCONVERTER_IF



        Returns the IF response of the downconverter.

        



    .. py:attribute:: DeviceResponseType.DOWNCONVERTER_RF



        Returns the RF response of the downconverter. This value is supported only for the PXIe-5603/5605/5665/5667/5693..

        



    .. py:attribute:: DeviceResponseType.DOWNCONVERTER_COMBINED



        Returns the combined RF and IF response of the downconverter. The combined response is in terms of IF frequency. This value is supported only for the PXIe-5603/5605/5665/5667.

        



    .. py:attribute:: DeviceResponseType.VSA_IF



        Returns the IF response of the entire NI-RFSA device. This value is supported only for the PXIe-5665/5667.

        



    .. py:attribute:: DeviceResponseType.VSA_COMBINED



        Returns the combined IF and RF response of the entire NI-RFSA device. The combined response is in terms of IF frequency. This value is supported only for the PXIe-5665/5667.

        



DigitizerDitherEnabled
----------------------

.. py:class:: DigitizerDitherEnabled

    .. py:attribute:: DigitizerDitherEnabled.DISABLED



        Disables dither on the digitizer.

        



    .. py:attribute:: DigitizerDitherEnabled.ENABLED



        Enables dither on the digitizer.

        



DigitizerSampleClockExportedTerminal
------------------------------------

.. py:class:: DigitizerSampleClockExportedTerminal

    .. py:attribute:: DigitizerSampleClockExportedTerminal.NONE



        The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646.

        



    .. py:attribute:: DigitizerSampleClockExportedTerminal.CLK_OUT



        Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.

        



DigitizerSampleClockTimebaseSource
----------------------------------

.. py:class:: DigitizerSampleClockTimebaseSource

    .. py:attribute:: DigitizerSampleClockTimebaseSource.ONBOARD_CLOCK



        The digitizer uses its onboard clock as the Sample Clock timebase.

        



    .. py:attribute:: DigitizerSampleClockTimebaseSource.CLK_IN



        The digitizer uses the signal present on the CLK IN connector as the Sample Clock timebase.

        



    .. py:attribute:: DigitizerSampleClockTimebaseSource.LO_REF_CLK



        The digitizer uses the signal generated on the 100 MHz REF OUT terminal on the PXIe-5653 as the Sample Clock timebase. This value is supported only for the PXIe-5665.

        



    .. py:attribute:: DigitizerSampleClockTimebaseSource.PXI_STAR



        The digitizer uses the signal present at the PXI star trigger line as the Sample Clock timebase. This value is not supported for the PXIe-5668.

        



    .. py:attribute:: DigitizerSampleClockTimebaseSource.DOWNCONVERTER_LO2_OUT



        The digitizer uses the signal present on the LO2 OUT connector on the downconverter as the Sample Clock timebase. This value is supported only for the PXIe-5668.

        



DownconverterFrequencyOffsetMode
--------------------------------

.. py:class:: DownconverterFrequencyOffsetMode

    .. py:attribute:: DownconverterFrequencyOffsetMode.AUTOMATIC



        NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the :py:attr:`nirfsa.Session.signal_bandwidth` property has been set and can be avoided.

        



    .. py:attribute:: DownconverterFrequencyOffsetMode.ENABLED



        NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the :py:attr:`nirfsa.Session.signal_bandwidth` property has been set and can be avoided. NI-RFSA returns an error if the :py:attr:`nirfsa.Session.signal_bandwidth` property has not been set, or if the signal bandwidth is too large.

        



    .. py:attribute:: DownconverterFrequencyOffsetMode.USER_DEFINED



        NI-RFSA uses the offset that you specified with the :py:attr:`nirfsa.Session.downconverter_frequency_offset` or :py:attr:`nirfsa.Session.downconverter_center_frequency` properties.

        



DownconverterLoopBandwidth
--------------------------

.. py:class:: DownconverterLoopBandwidth

    .. py:attribute:: DownconverterLoopBandwidth.NARROW



        Specifies that the downconverter module uses a narrow loop bandwidth.

        



    .. py:attribute:: DownconverterLoopBandwidth.MEDIUM



        Specifies that the downconverter module uses a medium loop bandwidth.

        



    .. py:attribute:: DownconverterLoopBandwidth.WIDE



        Specifies that the downconverter module uses a wide loop bandwidth.

        



DownconverterPreselectorEnabled
-------------------------------

.. py:class:: DownconverterPreselectorEnabled

    .. py:attribute:: DownconverterPreselectorEnabled.DISABLED



        Disables the preselector.

        



    .. py:attribute:: DownconverterPreselectorEnabled.ENABLED_WHEN_IN_SIGNAL_PATH



        The preselector is automatically enabled when it is in the signal path and is automatically disabled when it is not in the signal path. Use the :py:attr:`nirfsa.Session.preselector_present` property to determine if the downconverter has an preselector.

        



    .. py:attribute:: DownconverterPreselectorEnabled.ENABLED



        Enables the preselector. If the preselector is not in the signal path or if the preselector is not supported on the device, NI-RFSA returns an error. Select the :py:data:`~nirfsa.DownconverterPreselectorEnabled.ENABLED_WHEN_IN_SIGNAL_PATH` whenever possible avoid an error.

        



EnableAttrVals
--------------

.. py:class:: EnableAttrVals

    .. py:attribute:: EnableAttrVals.DISABLED



        The property is disabled.

        



    .. py:attribute:: EnableAttrVals.ENABLED



        The property is enabled.

        



EnableRfPreamp
--------------

.. py:class:: EnableRfPreamp

    .. py:attribute:: EnableRfPreamp.DISABLED



        Disables the RF preamplifier.

        



    .. py:attribute:: EnableRfPreamp.ENABLED_WHEN_IN_SIGNAL_PATH



        Enables the RF preamplifier when the RF preamplifier is present in the signal path and disables the preamplifier when it is not in the signal path. Only devices with an RF preamplifier on the downconverter and an RF preselector support this option. Use the :py:attr:`nirfsa.Session.rf_preamp_present` property to determine whether the downconverter has a preamplifier.

        



    .. py:attribute:: EnableRfPreamp.ENABLED



        Enables the RF preamplifier. If the RF preamplifier is not in a signal path, NI-RFSA returns an error. Select the :py:data:`~nirfsa.EnableRfPreamp.ENABLED_WHEN_IN_SIGNAL_PATH` value whenever possible to avoid an error.

        



    .. py:attribute:: EnableRfPreamp.AUTOMATIC



        Automatically enables the RF preamplifier based on the value of the :py:attr:`nirfsa.Session.reference_level` property. This value is valid only for the PXIe-5644/5645/5646, PXIe-5667, and PXIe-5830/5831/5832/5840/5841.

        



ExportOutputTerminal
--------------------

.. py:class:: ExportOutputTerminal

    .. py:attribute:: ExportOutputTerminal.DO_NOT_EXPORT



        The signal is not exported.

        



    .. py:attribute:: ExportOutputTerminal.CLK_OUT



        Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.

        



    .. py:attribute:: ExportOutputTerminal.REF_OUT



        Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841.

        



    .. py:attribute:: ExportOutputTerminal.REF_OUT2



        Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.

        



    .. py:attribute:: ExportOutputTerminal.PFI0



        The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.

        



    .. py:attribute:: ExportOutputTerminal.PFI1



        The trigger is received on PFI 1.

        



    .. py:attribute:: ExportOutputTerminal.PXI_TRIG0



        The trigger is received on PXI trigger line 0.

        



    .. py:attribute:: ExportOutputTerminal.PXI_TRIG1



        The trigger is received on PXI trigger line 1.

        



    .. py:attribute:: ExportOutputTerminal.PXI_TRIG2



        The trigger is received on PXI trigger line 2.

        



    .. py:attribute:: ExportOutputTerminal.PXI_TRIG3



        The trigger is received on PXI trigger line 3.

        



    .. py:attribute:: ExportOutputTerminal.PXI_TRIG4



        The trigger is received on PXI trigger line 4.

        



    .. py:attribute:: ExportOutputTerminal.PXI_TRIG5



        The trigger is received on PXI trigger line 5.

        



    .. py:attribute:: ExportOutputTerminal.PXI_TRIG6



        The trigger is received on PXI trigger line 6.

        



    .. py:attribute:: ExportOutputTerminal.PXI_TRIG7



        The trigger is received on PXI trigger line 7.

        



    .. py:attribute:: ExportOutputTerminal.PXI_STAR



        The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.

        



    .. py:attribute:: ExportOutputTerminal.PXIE_DSTARC



        The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.

        



    .. py:attribute:: ExportOutputTerminal.DIO_PFI0



        The trigger is received on PFI0 from the front panel DIO terminal.

        



    .. py:attribute:: ExportOutputTerminal.DIO_PFI1



        The trigger is received on PFI1 from the front panel DIO terminal.

        



    .. py:attribute:: ExportOutputTerminal.DIO_PFI2



        The trigger is received on PFI2 from the front panel DIO terminal.

        



    .. py:attribute:: ExportOutputTerminal.DIO_PFI3



        The trigger is received on PFI3 from the front panel DIO terminal.

        



    .. py:attribute:: ExportOutputTerminal.DIO_PFI4



        The trigger is received on PFI4 from the front panel DIO terminal.

        



    .. py:attribute:: ExportOutputTerminal.DIO_PFI5



        The trigger is received on PFI5 from the front panel DIO terminal.

        



    .. py:attribute:: ExportOutputTerminal.DIO_PFI6



        The trigger is received on PFI6 from the front panel DIO terminal.

        



    .. py:attribute:: ExportOutputTerminal.DIO_PFI7



        The trigger is received on PFI7 from the front panel DIO terminal.

        



FetchRelativeTo
---------------

.. py:class:: FetchRelativeTo

    .. py:attribute:: FetchRelativeTo.MOST_RECENT_SAMPLE



        Fetching occurs relative to the most recently acquired data. The value of the :py:attr:`nirfsa.Session.fetch_offset` property must be negative.

        



    .. py:attribute:: FetchRelativeTo.FIRST_SAMPLE



        Fetching occurs at the first sample acquired by the device. If the device wraps its buffer, the first sample is no longer available. In this case, NI-RFSA returns an error if the fetch offset is in the overwritten data.

        



    .. py:attribute:: FetchRelativeTo.REFERENCE_TRIGGER



        Fetching occurs relative to the Reference Trigger. This value behaves like :py:data:`~nirfsa.FetchRelativeTo.FIRST_SAMPLE` if no Reference Trigger is configured.

        



    .. py:attribute:: FetchRelativeTo.FIRST_PRETRIGGER_SAMPLE



        Fetching occurs relative to the first pretrigger sample acquired.

        



    .. py:attribute:: FetchRelativeTo.CURRENT_READ_POSITION



        Fetching occurs after the last fetched sample.

        



FrequencySettlingUnits
----------------------

.. py:class:: FrequencySettlingUnits

    .. py:attribute:: FrequencySettlingUnits.PPM



        Specifies the frequency settling time in parts per million (PPM).

        



    .. py:attribute:: FrequencySettlingUnits.SECONDS_AFTER_LOCK



        Specifies the frequency settling in time after lock (seconds).

        



    .. py:attribute:: FrequencySettlingUnits.SECONDS_AFTER_IO



        Specifies the frequency settling time after I/O (seconds).

        



IFattenTableSel
---------------

.. py:class:: IFattenTableSel

    .. py:attribute:: IFattenTableSel.STANDARD



        Specifies that the standard IF attenuation table is used for the external calibration.

        



    .. py:attribute:: IFattenTableSel.ACPR



        Specifies that the adjacent channel power ratio (ACPR) IF attenuation table is used for the external calibration. You can only select this value if you set the :py:attr:`nirfsa.Session.CAL_IF_FILTER_SELECTION` property to :py:data:`~nirfsa.IFfilterSelection.EXT_CAL_IF_FILTER_PATH_1` or :py:data:`~nirfsa.IFfilterSelection.EXT_CAL_IF_FILTER_PATH_2`.

        



IFfilter
--------

.. py:class:: IFfilter

    .. py:attribute:: IFfilter._187_5_MHZ_WIDE



        The device uses the 187.5 MHz wide bandwidth filter.

        



    .. py:attribute:: IFfilter._187_5_MHZ_NARROW



        The device uses the 187.5 MHz narrow bandwidth filter.

        



    .. py:attribute:: IFfilter._53_MHZ



        The device uses the 53 MHz filter.

        



    .. py:attribute:: IFfilter.BYPASS



        The device bypasses the IF filter.

        



IFfilterSelection
-----------------

.. py:class:: IFfilterSelection

    .. py:attribute:: IFfilterSelection.EXT_CAL_IF_FILTER_PATH_1



        Specifies that the 5 MHz filter path is used during calibration.

        



    .. py:attribute:: IFfilterSelection.EXT_CAL_IF_FILTER_PATH_2



        Specifies that the 300 kHz filter path is used during calibration. Not supported for the PXIe-5694.

        



    .. py:attribute:: IFfilterSelection.EXT_CAL_IF_FILTER_PATH_3



        None of the IF filter paths are used during calibration.

        



    .. py:attribute:: IFfilterSelection.EXT_CAL_IF_FILTER_PATH_4



        Specifies that the 20 MHz filter path is used during calibration.

        



    .. py:attribute:: IFfilterSelection.EXT_CAL_IF_FILTER_PATH_5



        Specifies that the 1.4 MHz filter path is used during calibration.

        



    .. py:attribute:: IFfilterSelection.EXT_CAL_IF_FILTER_PATH_6



        Specifies that the 400 kHz filter path is used during calibration.

        



    .. py:attribute:: IFfilterSelection.EXT_CAL_IF_FILTER_PATH_7



        Specifies that the 110 kHz filter path is used during calibration.

        



    .. py:attribute:: IFfilterSelection.EXT_CAL_IF_FILTER_PATH_8



        Specifies that the 30 kHz filter path is used during calibration.

        



IfConditioningDownConversionEnabled
-----------------------------------

.. py:class:: IfConditioningDownConversionEnabled

    .. py:attribute:: IfConditioningDownConversionEnabled.DISABLED



        Disables IF conditioning downconversion.

        



    .. py:attribute:: IfConditioningDownConversionEnabled.ENABLED



        Enables IF conditioning downconversion.

        



InputIsolationEnabled
---------------------

.. py:class:: InputIsolationEnabled

    .. py:attribute:: InputIsolationEnabled.DISABLED



        Disables input isolation.

        



    .. py:attribute:: InputIsolationEnabled.ENABLED



        Enables input isolation.

        



InputPort
---------

.. py:class:: InputPort

    .. py:attribute:: InputPort.RF_IN



        Enables the RF IN port.

        



    .. py:attribute:: InputPort.IQ_IN



        Enables the I/Q IN port.

        



    .. py:attribute:: InputPort.CAL_IN



        Enables the CAL IN port.

        



    .. py:attribute:: InputPort.I_ONLY



        Enables the I terminals of the I/Q IN port. It is supported only for PXIe-5645.

        



IqInPortTerminalConfiguration
-----------------------------

.. py:class:: IqInPortTerminalConfiguration

    .. py:attribute:: IqInPortTerminalConfiguration.DIFFERENTIAL



        Sets the terminal configuration to differential.

        



    .. py:attribute:: IqInPortTerminalConfiguration.SINGLE_ENDED



        Sets the terminal configuration to single-ended.

        



LinearInterpolationFormat
-------------------------

.. py:class:: LinearInterpolationFormat

    .. py:attribute:: LinearInterpolationFormat.MAGNITUDE_AND_PHASE



        Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion.

        



    .. py:attribute:: LinearInterpolationFormat.MAGNITUDE_DB_AND_PHASE



        Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.

        



    .. py:attribute:: LinearInterpolationFormat.REAL_AND_IMAGINARY



        Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.

        



Lo2ExportEnabled
----------------

.. py:class:: Lo2ExportEnabled

    .. py:attribute:: Lo2ExportEnabled.DISABLED



        Disables LO2 export.

        



    .. py:attribute:: Lo2ExportEnabled.ENABLED



        Enables LO2 export.

        



LoInjection
-----------

.. py:class:: LoInjection

    .. py:attribute:: LoInjection.HIGH



        Configures the LO signal that the NI-RFSA device generates at a frequency higher than the RF frequency. This LO frequency is given by the formula f<sub>LO</sub> = f<sub>RF</sub> + f<sub>IF</sub>.

        



    .. py:attribute:: LoInjection.LOW



        Configures the LO signal that the NI-RFSA device generates at a frequency lower than the RF frequency. This LO frequency is given by the formula f<sub>LO</sub> = f<sub>RF</sub> - f<sub>IF</sub>.

        



LoNumber
--------

.. py:class:: LoNumber

    .. py:attribute:: LoNumber.LO2



        Selects LO2, which is the 4 GHz signal path.

        



    .. py:attribute:: LoNumber.LO3



        Selects LO3, which is the 800 MHz signal path.

        



    .. py:attribute:: LoNumber.LO1



        Selects LO1, which is the 3.2 GHz to 8.3 GHz variable signal path.

        



LoOutExportConfigureFromRfsg
----------------------------

.. py:class:: LoOutExportConfigureFromRfsg

    .. py:attribute:: LoOutExportConfigureFromRfsg.DISABLED



        Do not allow NI-RFSG to control the NI-RFSA local oscillator export.

        



    .. py:attribute:: LoOutExportConfigureFromRfsg.ENABLED



        Allow NI-RFSG to control the NI-RFSA local oscillator export.

        



LoPathSel
---------

.. py:class:: LoPathSel

    .. py:attribute:: LoPathSel.EXT_CAL_LO_PATH_1



        Specifies that the LO path 1 is used.

        



    .. py:attribute:: LoPathSel.EXT_CAL_LO_PATH_2



        Specifies that the LO path 2 is used.

        



    .. py:attribute:: LoPathSel.EXT_CAL_LO_PATH_3



        Specifies that the LO path 3 is used.

        



    .. py:attribute:: LoPathSel.EXT_CAL_LO_PATH_4



        Specifies that the LO path 4 is used.

        



    .. py:attribute:: LoPathSel.EXT_CAL_LO_PATH_5



        Specifies that the LO path 5 is used.

        



LoPllFractionalModeEnabled
--------------------------

.. py:class:: LoPllFractionalModeEnabled

    .. py:attribute:: LoPllFractionalModeEnabled.DISABLED



        Disables fractional mode for the LO PLL.

        



    .. py:attribute:: LoPllFractionalModeEnabled.ENABLED



        Enables fractional mode for the LO PLL.

        



LoSource
--------

.. py:class:: LoSource

    .. py:attribute:: LoSource.NONE



        Specifies that no LO source is required to downconvert the RF input signal.

        



    .. py:attribute:: LoSource.ONBOARD



        Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal.**PXIe-5831/5832** This configuration uses the onboard LO of the PXIe-3622, using the LO2 stage.**PXIe-5831/5832 with PXIe-5653** This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3622.**PXIe-5841 with PXIe-5655** This configuration uses the onboard LO of the PXIe-5655.

        



    .. py:attribute:: LoSource.LO_IN



        Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel.

        



    .. py:attribute:: LoSource.LO_SOURCE_SECONDARY



        Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid on only the PXIe-5831 with PXIe-5653 (LO1 stage only) or PXIe-5832 with PCIe-5653 (LO1 stage only).

        



    .. py:attribute:: LoSource.LO_SOURCE_SG_SA_SHARED



        Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSA selects an internal synthesizer and the synthesizer signal is switched to both the RF Out and RF In mixers. This value is valid on only the PXIe-5830/5831/5832/5841 with PXIe-5655.

        



LoYigMainCoilDrive
------------------

.. py:class:: LoYigMainCoilDrive

    .. py:attribute:: LoYigMainCoilDrive.NORMAL



        Adjusts the YIG main coil on the LO for an underdamped response.

        



    .. py:attribute:: LoYigMainCoilDrive.FAST



        Adjusts the YIG main coil on the LO for an overdamped response.

        



LoadConfigurationResetOptions
-----------------------------

.. py:class:: LoadConfigurationResetOptions

    .. py:attribute:: LoadConfigurationResetOptions.NONE



        NI-RFSA resets all configurations.

        



    .. py:attribute:: LoadConfigurationResetOptions.DEEMBEDDING_TABLES



        NI-RFSA skips resetting the de-embedding tables.

        



NoiseSourcePowerEnabled
-----------------------

.. py:class:: NoiseSourcePowerEnabled

    .. py:attribute:: NoiseSourcePowerEnabled.DISABLED



        Disables the noise source power.

        



    .. py:attribute:: NoiseSourcePowerEnabled.ENABLED



        Enables the noise source power.

        



NotchFilterEnabled
------------------

.. py:class:: NotchFilterEnabled

    .. py:attribute:: NotchFilterEnabled.DISABLED



        Disables the notch filter.

        



    .. py:attribute:: NotchFilterEnabled.ENABLED_WHEN_IN_SIGNAL_PATH



        The notch filter is automatically enabled when it is in the signal path and automatically disabled when it is not in the signal path.

        



    .. py:attribute:: NotchFilterEnabled.ENABLED



        Enables the notch filter. If the notch filter is not in the signal path or if the notch filter is not supported on the device, NI-RFSA returns an error. Select :py:data:`~nirfsa.NotchFilterEnabled.ENABLED_WHEN_IN_SIGNAL_PATH` whenever possible to avoid an error.

        



OutputTerm
----------

.. py:class:: OutputTerm

    .. py:attribute:: OutputTerm.DO_NOT_EXPORT



        The signal is not exported.

        



    .. py:attribute:: OutputTerm.CLK_OUT



        Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.

        



    .. py:attribute:: OutputTerm.REF_OUT



        Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841.

        



    .. py:attribute:: OutputTerm.REF_OUT2



        Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.

        



    .. py:attribute:: OutputTerm.PFI0



        The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.

        



    .. py:attribute:: OutputTerm.PFI1



        The trigger is received on PFI 1.

        



    .. py:attribute:: OutputTerm.PXI_TRIG0



        The trigger is received on PXI trigger line 0.

        



    .. py:attribute:: OutputTerm.PXI_TRIG1



        The trigger is received on PXI trigger line 1.

        



    .. py:attribute:: OutputTerm.PXI_TRIG2



        The trigger is received on PXI trigger line 2.

        



    .. py:attribute:: OutputTerm.PXI_TRIG3



        The trigger is received on PXI trigger line 3.

        



    .. py:attribute:: OutputTerm.PXI_TRIG4



        The trigger is received on PXI trigger line 4.

        



    .. py:attribute:: OutputTerm.PXI_TRIG5



        The trigger is received on PXI trigger line 5.

        



    .. py:attribute:: OutputTerm.PXI_TRIG6



        The trigger is received on PXI trigger line 6.

        



    .. py:attribute:: OutputTerm.PXI_TRIG7



        The trigger is received on PXI trigger line 7.

        



    .. py:attribute:: OutputTerm.PXI_STAR



        The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.

        



    .. py:attribute:: OutputTerm.PXIE_DSTARB



        The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.

        



    .. py:attribute:: OutputTerm.DIO_PFI0



        The trigger is received on PFI0 from the front panel DIO terminal.

        



    .. py:attribute:: OutputTerm.DIO_PFI1



        The trigger is received on PFI1 from the front panel DIO terminal.

        



    .. py:attribute:: OutputTerm.DIO_PFI2



        The trigger is received on PFI2 from the front panel DIO terminal.

        



    .. py:attribute:: OutputTerm.DIO_PFI3



        The trigger is received on PFI3 from the front panel DIO terminal.

        



    .. py:attribute:: OutputTerm.DIO_PFI4



        The trigger is received on PFI4 from the front panel DIO terminal.

        



    .. py:attribute:: OutputTerm.DIO_PFI5



        The trigger is received on PFI5 from the front panel DIO terminal.

        



    .. py:attribute:: OutputTerm.DIO_PFI6



        The trigger is received on PFI6 from the front panel DIO terminal.

        



    .. py:attribute:: OutputTerm.DIO_PFI7



        The trigger is received on PFI7 from the front panel DIO terminal.

        



    .. py:attribute:: OutputTerm.TIMER_EVENT



        The trigger is received from the Timer Event. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841, and for digital edge Advance Triggers on the PXIe-5663E/5665.

        



OverflowErrorReporting
----------------------

.. py:class:: OverflowErrorReporting

    .. py:attribute:: OverflowErrorReporting.WARNING



        Configures NI-RFSA to return a warning when an ADC or onboard signal processing (OSP) overflow occurs.

        



    .. py:attribute:: OverflowErrorReporting.DISABLED



        Configures NI-RFSA to not return an error or a warning when an ADC or OSP overflow occurs.

        



PowerSpectrumUnits
------------------

.. py:class:: PowerSpectrumUnits

    .. py:attribute:: PowerSpectrumUnits.DBM



        Units are dB with reference to 1 milliwatt.

        



    .. py:attribute:: PowerSpectrumUnits.VOLTS_SQUARED



        Units are in volts squared.

        



    .. py:attribute:: PowerSpectrumUnits.DBMV



        Units are dB with reference to 1 millivolt.

        



    .. py:attribute:: PowerSpectrumUnits.DBUV



        Units are dB with reference to 1 microvolt.

        



    .. py:attribute:: PowerSpectrumUnits.VOLTS



        Units are in volts.

        



    .. py:attribute:: PowerSpectrumUnits.WATTS



        Units are in watts.

        



PxiChassisClk10Source
---------------------

.. py:class:: PxiChassisClk10Source

    .. py:attribute:: PxiChassisClk10Source.NONE



        The device does not drive the PXI 10 MHz backplane Reference Clock.

        



    .. py:attribute:: PxiChassisClk10Source.ONBOARD_CLOCK



        The device drives the PXI 10 MHz backplane Reference Clock with the PXI-5600 onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front panel to use this option.

        



    .. py:attribute:: PxiChassisClk10Source.REF_IN



        The device drives the PXI 10 MHz backplane Reference Clock with the reference source attached to the PXI-5600 FREQ REF IN connector. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front panel to use this option.

        



ReferenceClockExportedRate
--------------------------

.. py:class:: ReferenceClockExportedRate

    .. py:attribute:: ReferenceClockExportedRate._10MHZ



        Exports a 10 MHz Reference Clock.

        



    .. py:attribute:: ReferenceClockExportedRate._100MHZ



        Exports a 100 MHz Reference Clock.

        



    .. py:attribute:: ReferenceClockExportedRate._1GHZ



        Exports a 1 GHz Reference Clock.

        



ReferenceClockExportedTerminal
------------------------------

.. py:class:: ReferenceClockExportedTerminal

    .. py:attribute:: ReferenceClockExportedTerminal.NONE



        The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646.

        



    .. py:attribute:: ReferenceClockExportedTerminal.REF_OUT



        Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841.

        



    .. py:attribute:: ReferenceClockExportedTerminal.REF_OUT2



        Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.

        



    .. py:attribute:: ReferenceClockExportedTerminal.CLK_OUT



        Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.

        



    .. py:attribute:: ReferenceClockExportedTerminal.IF_COND_REF_OUT



        Export the clock on the REF OUT terminal on the PXIe-5694. This value is valid only for the PXIe-5667.

        



ReferenceClockSource
--------------------

.. py:class:: ReferenceClockSource

    .. py:attribute:: ReferenceClockSource.NONE



        No Reference Clock is required for the current device configuration. This value is valid only for the PXIe-5694 or the PXIe-5668.

        



    .. py:attribute:: ReferenceClockSource.ONBOARD_CLOCK



        **PXI-5661 **NI-RFSA locks the NI-RFSA device to the PXI-5600 RF downconverter onboard clock.**PXIe-5663/5663E **NI-RFSA locks the PXIe-5663/5663E to the PXI/PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, connect the REF IN/OUT connector on the PXI/PXIe-5652 to the CLK IN terminal on the PXI5622.**PXIe-5665 **NI-RFSA locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622.**PXIe-5667 **NI-RFSA locks the PXIe-5667 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694.**PXIe-5668 **Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624.**PXIe-5830/5831 **For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector.**PXIe-5831/5832 with PXIe-5653 **Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector.**PXIe-5644/5645/5646, PXIe-5820/5840/5841 **Lock the NI-RFSA device to its onboard clock.**PXIe-5841 with PXIe-5655 **Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector.**PXIe-5842 **Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the User Manual for the instrument.**PXIe-5860 **Lock to the PXIe-5860 onboard clock.

        



    .. py:attribute:: ReferenceClockSource.REF_IN



        **PXI-5661 **NI-RFSA locks the NI-RFSA device to the signal at the external FREQ REF IN connector on the PXI-5600**PXIe-5663/5663E **Connect the external signal to the PXI/PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, this configuration can only be used in external digitizer mode.**PXIe-5665 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the :py:attr:`nirfsa.Session.ref_clock_rate` property according to the frequency of your external clock signal.**PXIe-5667 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. If your external clock signal frequency is set to a frequency other than 10 MHz, set the :py:attr:`nirfsa.Session.ref_clock_rate` property according to the frequency of your external clock signal.**PXIe-5668 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the **clock rate** parameter according to the frequency of your external clock signal.**PXIe-5694 **Connect the Reference Clock signal to the REF/LO IN connector on the PXIe-5694 front panel.**PXIe-5644/5645/5646, PXIe-5820/5840/5841 **Lock the NI-RFSA device to the signal at the external REF IN connector.**PXIe-5830/5831 **For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831/5832, lock the external signal to the PXIe-3622 REF IN connector.**PXIe-5831/5832 with PXIe-5653 **Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector.**PXIe-5841 with PXIe-5655 **Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. **PXIe-5842 **Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the User Manual for the instrument. PXIe-5860 Lock to the signal at the REF IN connector on the PXIe-5860.

        



    .. py:attribute:: ReferenceClockSource.PXI_CLK



        **PXI-5661 **NI-RFSA locks the NI-RFSA device to the PXI backplane clock using the PXI-5600. You must connect the PXI 10 MHz connector to the REF IN connector on the PXI-5600 front panel to use this option. **PXIe-5668 **Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624.**PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655/5842/5860 **Lock the device to the PXI backplane clock.

        



    .. py:attribute:: ReferenceClockSource.CLK_IN



        **PXI-5661 **This configuration does not apply to the PXI-5661.**PXIe-5663/5663E **NI-RFSA locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXI/PXIe-5652.**PXIe-5665 **NI-RFSA locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the :py:attr:`nirfsa.Session.ref_clock_rate` property to 100 MHz.**PXIe-5667 **NI-RFSA locks the PXIe-5667 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. Set the :py:attr:`nirfsa.Session.ref_clock_rate` property to 100 MHz.**PXIe-5668 **Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the **clock rate** parameter to 100 MHz.**PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655/5842/5860 **This configuration does not apply.

        



    .. py:attribute:: ReferenceClockSource.PXI_CLK_MASTER



        **PXIe-5831/5832 with PXIe-5653 **NI-RFSA configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.**PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5644/5645/5646, PXIe-5820/5840/5841/5841 with PXIe-5655 /5842/5860**This configuration does not apply.

        



    .. py:attribute:: ReferenceClockSource.REF_IN_2



        **PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655 **This configuration does not apply.

        



ReferenceLevelDataType
----------------------

.. py:class:: ReferenceLevelDataType

    .. py:attribute:: ReferenceLevelDataType.MECHANICAL_ATTENUATOR_DISABLED



        The data is the configuration data when the mechanical relay is disabled. Use this option to save uncalibrated measurements for more advanced operations.

        



    .. py:attribute:: ReferenceLevelDataType.DEFAULT



        The data is the default configuration data.

        



ReferenceTriggerDigitalEdgeEdge
-------------------------------

.. py:class:: ReferenceTriggerDigitalEdgeEdge

    .. py:attribute:: ReferenceTriggerDigitalEdgeEdge.RISING



        The trigger asserts on the rising edge of the signal.

        



    .. py:attribute:: ReferenceTriggerDigitalEdgeEdge.FALLING



        The trigger asserts on the falling edge of the signal

        



ReferenceTriggerIqPowerEdgeSlope
--------------------------------

.. py:class:: ReferenceTriggerIqPowerEdgeSlope

    .. py:attribute:: ReferenceTriggerIqPowerEdgeSlope.RISING



        The trigger asserts when the signal power is rising.

        



    .. py:attribute:: ReferenceTriggerIqPowerEdgeSlope.FALLING



        The trigger asserts when the signal power is falling.

        



ReferenceTriggerOspDelayEnabled
-------------------------------

.. py:class:: ReferenceTriggerOspDelayEnabled

    .. py:attribute:: ReferenceTriggerOspDelayEnabled.DISABLED



        Disables OSP delay for the Reference Trigger.

        



    .. py:attribute:: ReferenceTriggerOspDelayEnabled.ENABLED



        Enables OSP delay for the Reference Trigger.

        



ReferenceTriggerType
--------------------

.. py:class:: ReferenceTriggerType

    .. py:attribute:: ReferenceTriggerType.NONE



        No Reference Trigger is configured.

        



    .. py:attribute:: ReferenceTriggerType.DIGITAL_EDGE



        The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the :py:attr:`nirfsa.Session.digital_edge_ref_trigger_source` property.

        



    .. py:attribute:: ReferenceTriggerType.IQ_POWER_EDGE



        The Reference Trigger is asserted when the signal is changing past the level specified with the slope (rising or falling) configured with the :py:attr:`nirfsa.Session.iq_power_edge_ref_trigger_slope` property.

        



    .. py:attribute:: ReferenceTriggerType.SOFTWARE_EDGE



        The Reference Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the :py:meth:`nirfsa.Session.send_software_edge_trigger` method and selecting :py:data:`~nirfsa.NIRFSA_VAL_REF_TRIGGER` as the **trigger** parameter.

        



    .. py:attribute:: ReferenceTriggerType.IQ_ANALOG_EDGE



        The Reference Trigger is asserted when the I or Q signal is changed past the level specified with the slope configured with the :py:attr:`nirfsa.Session.IQ_ANALOG_EDGE_REF_TRIGGER_SLOPE` property. This value is valid only for PXIe-5644/5645 devices.

        



ResetWithOptionsStepsToOmit
---------------------------

.. py:class:: ResetWithOptionsStepsToOmit

    .. py:attribute:: ResetWithOptionsStepsToOmit.DEEMBEDDING_TABLES



        Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.

        



    .. py:attribute:: ResetWithOptionsStepsToOmit.NONE



        No step is omitted during reset.

        



    .. py:attribute:: ResetWithOptionsStepsToOmit.ROUTES



        Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.

        



RfLbSigCondPathSel
------------------

.. py:class:: RfLbSigCondPathSel

    .. py:attribute:: RfLbSigCondPathSel.EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1



        yet to be defined

        



    .. py:attribute:: RfLbSigCondPathSel.EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_2



        yet to be defined

        



RfOutLoExport
-------------

.. py:class:: RfOutLoExport

    .. py:attribute:: RfOutLoExport.DISABLED



        The LO signal is not exported from the RF OUT LO OUT terminal.

        



    .. py:attribute:: RfOutLoExport.ENABLED



        The LO signal is exported from the RF OUT LO OUT terminal.

        



    .. py:attribute:: RfOutLoExport.UNSPECIFIED



        The LO signal may or may not be exported to the RF OUT LO OUT terminal, because NI-RFSG may be controlling it.

        



RfPathSelection
---------------

.. py:class:: RfPathSelection

    .. py:attribute:: RfPathSelection.EXT_CAL_RF_BAND_1



        The data is the default configuration data.

        



    .. py:attribute:: RfPathSelection.EXT_CAL_RF_BAND_2



        The data is the configuration data when the mechanical relay is disabled. Use this option to save uncalibrated measurements for more advanced operations.

        



    .. py:attribute:: RfPathSelection.EXT_CAL_RF_BAND_3



        The data is the default configuration data.

        



    .. py:attribute:: RfPathSelection.EXT_CAL_RF_BAND_4



        The data is the default configuration data.

        



SelfCalSteps
------------

.. py:class:: SelfCalSteps

    .. py:attribute:: SelfCalSteps.DIGITIZER_SELF_CAL



        Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.

        



    .. py:attribute:: SelfCalSteps.PRESELECTOR_ALIGNMENT



        Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.

        



    .. py:attribute:: SelfCalSteps.OMIT_NONE



        No calibration steps are omitted.

        



    .. py:attribute:: SelfCalSteps.GAIN_REFERENCE



        Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.

        



    .. py:attribute:: SelfCalSteps.IF_FLATNESS



        Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.

        



    .. py:attribute:: SelfCalSteps.LO_SELF_CAL



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



    .. py:attribute:: SelfCalSteps.AMPLITUDE_ACCURACY



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



    .. py:attribute:: SelfCalSteps.RESIDUAL_LO_POWER



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



    .. py:attribute:: SelfCalSteps.IMAGE_SUPPRESSION



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



    .. py:attribute:: SelfCalSteps.SYNTHESIZER_ALIGNMENT



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



    .. py:attribute:: SelfCalSteps.DC_OFFSET



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



SelfCalibrateRangeStepsToOmit
-----------------------------

.. py:class:: SelfCalibrateRangeStepsToOmit

    .. py:attribute:: SelfCalibrateRangeStepsToOmit.DIGITIZER_SELF_CAL



        Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.

        



    .. py:attribute:: SelfCalibrateRangeStepsToOmit.PRESELECTOR_ALIGNMENT



        Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.

        



    .. py:attribute:: SelfCalibrateRangeStepsToOmit.OMIT_NONE



        No calibration steps are omitted.

        



    .. py:attribute:: SelfCalibrateRangeStepsToOmit.GAIN_REFERENCE



        Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.

        



    .. py:attribute:: SelfCalibrateRangeStepsToOmit.IF_FLATNESS



        Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.

        



    .. py:attribute:: SelfCalibrateRangeStepsToOmit.LO_SELF_CAL



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



    .. py:attribute:: SelfCalibrateRangeStepsToOmit.AMPLITUDE_ACCURACY



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



    .. py:attribute:: SelfCalibrateRangeStepsToOmit.RESIDUAL_LO_POWER



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



    .. py:attribute:: SelfCalibrateRangeStepsToOmit.IMAGE_SUPPRESSION



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



    .. py:attribute:: SelfCalibrateRangeStepsToOmit.SYNTHESIZER_ALIGNMENT



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



    .. py:attribute:: SelfCalibrateRangeStepsToOmit.DC_OFFSET



        Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.

        



SelfCalibrationStep
-------------------

.. py:class:: SelfCalibrationStep

    .. py:attribute:: SelfCalibrationStep.PRESELECTOR_ALIGNMENT



        Calls for preselector alignment.

        



    .. py:attribute:: SelfCalibrationStep.GAIN_REFERENCE



        Measures the changes in gain since the last external calibration was run.

        



    .. py:attribute:: SelfCalibrationStep.IF_FLATNESS



        Measures the IF response of the entire system for each of the supported IF filters

        



    .. py:attribute:: SelfCalibrationStep.DIGITIZER_SELF_CAL



        Calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter.

        



    .. py:attribute:: SelfCalibrationStep.LO_SELF_CAL



        Calls for LO self-calibration, if the LO source module is associated with the RF downconverter.

        



    .. py:attribute:: SelfCalibrationStep.AMPLITUDE_ACCURACY



        Selects the Amplitude Accuracy self-calibration step.

        



    .. py:attribute:: SelfCalibrationStep.RESIDUAL_LO_POWER



        Selects the Residual LO Power self-calibration step.

        



    .. py:attribute:: SelfCalibrationStep.IMAGE_SUPPRESSION



        Selects the Image Suppression self-calibration step.

        



    .. py:attribute:: SelfCalibrationStep.SYNTHESIZER_ALIGNMENT



        Selects the Synthesizer Alignment self-calibration step.

        



    .. py:attribute:: SelfCalibrationStep.DC_OFFSET



        Selects the DC Offset self-calibration step.

        



Signal
------

.. py:class:: Signal

    .. py:attribute:: Signal.START_TRIGGER



        NI-RFSA routes a Start Trigger.

        



    .. py:attribute:: Signal.REF_TRIGGER



        NI-RFSA routes a Reference

        



    .. py:attribute:: Signal.ADVANCE_TRIGGER



        NI-RFSA routes an Advance

        



    .. py:attribute:: Signal.READY_FOR_START_EVENT



        NI-RFSA routes a Ready for Start Event.

        



    .. py:attribute:: Signal.READY_FOR_REF_EVENT



        NI-RFSA routes a Ready for Reference Event..

        



    .. py:attribute:: Signal.END_OF_RECORD_EVENT



        NI-RFSA routes a End of Record Event.

        



    .. py:attribute:: Signal.DONE_EVENT



        NI-RFSA routes a Done Event.

        



    .. py:attribute:: Signal.REF_CLOCK



        NI-RFSA routes a Reference Clock.

        



    .. py:attribute:: Signal.USER



        NI-RFSA routes a User Defined Signal.

        



SignalConditioningEnabled
-------------------------

.. py:class:: SignalConditioningEnabled

    .. py:attribute:: SignalConditioningEnabled.ENABLED



        Enables signal conditioning.

        



    .. py:attribute:: SignalConditioningEnabled.BYPASSED



        Bypasses all signal conditioning.

        



SmoothSpectrumEnabled
---------------------

.. py:class:: SmoothSpectrumEnabled

    .. py:attribute:: SmoothSpectrumEnabled.DISABLED



        Disables spectrum smoothing.

        



    .. py:attribute:: SmoothSpectrumEnabled.ENABLED



        Enables spectrum smoothing.

        



SoftwareTriggerType
-------------------

.. py:class:: SoftwareTriggerType

    .. py:attribute:: SoftwareTriggerType.START



        NI-RFSA sends a Start software trigger.

        



    .. py:attribute:: SoftwareTriggerType.REF



        NI-RFSA sends a Reference software trigger.

        



    .. py:attribute:: SoftwareTriggerType.ADVANCE



        NI-RFSA sends an Advance software trigger.

        



    .. py:attribute:: SoftwareTriggerType.ARM_REF



        NI-RFSA sends an Arm Reference software trigger. This trigger is not valid for the PXIe-5668.

        



SparameterOrientation
---------------------

.. py:class:: SparameterOrientation

    .. py:attribute:: SparameterOrientation.PORT1_TOWARDS_DUT



        Port 1 of the S2P is oriented towards the DUT port.

        



    .. py:attribute:: SparameterOrientation.PORT2_TOWARDS_DUT



        Port 2 of the S2P is oriented towards the DUT port.

        



SpectrumAveragingMode
---------------------

.. py:class:: SpectrumAveragingMode

    .. py:attribute:: SpectrumAveragingMode.NO



        Configures NI-RFSA to perform no averaging on acquisitions.

        



    .. py:attribute:: SpectrumAveragingMode.RMS



        Configures NI-RFSA for root-mean-square (RMS) averaging. RMS averaging reduces signal fluctuations but not the noise floor. RMS averaging averages the energy, or power, of the signal. This averaging prevents noise floor reduction and gives averaged RMS quantities of single-channel measurements zero phase. RMS averaging for dual-channel measurements preserves important phase information.

        



    .. py:attribute:: SpectrumAveragingMode.VECTOR



        Configures NI-RFSA for vector averaging. Vector averaging reduces noise from synchronous signals. Vector averaging computes the average of complex quantities directly, which means that it allows separate averaging for real and imaginary parts. Complex averaging such as vector averaging reduces noise and usually requires a trigger to improve block-to-block phase coherence.

        



    .. py:attribute:: SpectrumAveragingMode.PEAK_HOLD



        Configures NI-RFSA for peak-hold averaging. Peak-hold averaging retains the RMS peak levels of the averaged quantities. The peak-hold averaging process performs peak-hold at each frequency bin separately to retain peak RMS levels from one FFT record to the next.

        



    .. py:attribute:: SpectrumAveragingMode.MIN_HOLD



        Configures NI-RFSA to perform no averaging on acquisitions.

        



    .. py:attribute:: SpectrumAveragingMode.SCALAR



        Configures NI-RFSA to perform no averaging on acquisitions.

        



    .. py:attribute:: SpectrumAveragingMode.LOG



        Configures NI-RFSA to perform no averaging on acquisitions.

        



SpectrumFftWindowType
---------------------

.. py:class:: SpectrumFftWindowType

    .. py:attribute:: SpectrumFftWindowType.UNIFORM



        No window is applied.

        



    .. py:attribute:: SpectrumFftWindowType.HANNING



        The Hanning window is useful for analyzing transients longer than the time duration of the window, and also for general-purpose applications.

        



    .. py:attribute:: SpectrumFftWindowType.HAMMING



        A Hamming window is applied to the waveform using the following equation: y[i] = x[i] * (0.54 - 0.46cos(w)) where w = (2)i/n and n = the waveform size. Note: Hanning and Hamming windows are somewhat similar. However, in the time domain, the Hamming window does not get as close to zero near the edges as does the Hanning window.

        



    .. py:attribute:: SpectrumFftWindowType.BLACKMAN_HARRIS



        A Blackman-Harris window is applied to the waveform using the following equation: y[i] = x[i] * (0.42323 - 0.49755*cos(w) + 0.07922*cos(2w))

        



    .. py:attribute:: SpectrumFftWindowType.EXACT_BLACKMAN



        An Exact Blackman window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w))

        



    .. py:attribute:: SpectrumFftWindowType.BLACKMAN



        A Blackman window is useful for analyzing transient signals, and provides similar windowing to Hanning and Hamming windows but adds one additional cosine term to reduce ripple. A Blackman window is applied to the waveform using the following equation: y[i] = x[i] * (0.42 - 0.50*cos(w) + 0.08*cos(2w))

        



    .. py:attribute:: SpectrumFftWindowType.FLAT_TOP



        The fifth-order Flat Top window has the best amplitude accuracy of all the window methods. The increased amplitude accuracy (0.02 dB for signals exactly between integral cycles) is at the expense of frequency selectivity. The Flat Top window is most useful in accurately measuring the amplitude of single frequency components with little nearby spectral energy in the signal. A fifth-order Flat Top window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w) + a4*cos(4w))

        



    .. py:attribute:: SpectrumFftWindowType._4_TERM_BLACKMAN_HARRIS



        A 4-term Blackman-Harris window is a general purpose window; it has side-lobe rejection in the upper 90 dB, with moderately wide side lobe. A 4-term Blackman Harris window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w))

        



    .. py:attribute:: SpectrumFftWindowType._7_TERM_BLACKMAN_HARRIS



        A 7-term Blackman-Harris window has the highest dynamic range; it is ideal for signal-to-noise ratio applications. A 7-term Blackman Harris window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w) + a4*cos(4w) - a5*cos(5w) + a6*cos(6w))

        



    .. py:attribute:: SpectrumFftWindowType.LOW_SIDE_LOBE



        The Low Side Lobe window further reduces the size of the main lobe. The following equation defines the Low Side Lobe window. where   *N* is the length of window

        



    .. py:attribute:: SpectrumFftWindowType.GAUSSIAN



        A Gaussian window is applied to the waveform using the following equation: y[i] = x[i] * exp(-0.5*(i - (N-1)/2)^2 / ((N-1)/2)^2) where N is the length of the window

        



    .. py:attribute:: SpectrumFftWindowType.KAISER_BESSEL



        A Kaiser-Bessel window is applied to the waveform using the following equation: y[i] = x[i] * I0(β*sqrt(1 - (2i/(N-1) - 1)^2))/I0(β) where i is between 0 and N-1, N is the length of the window, β determines the shape of the window, and I0 is the zeroth order Modified Bessel method of the first kind

        



SpectrumResolutionBandwidthType
-------------------------------

.. py:class:: SpectrumResolutionBandwidthType

    .. py:attribute:: SpectrumResolutionBandwidthType.THREE_DECIBELS



        Defines the resolution bandwidth (RBW) in terms of the 3 dB bandwidth of the window specified by the :py:attr:`nirfsa.Session.fft_window_type` property.

        



    .. py:attribute:: SpectrumResolutionBandwidthType.SIX_DECIBELS



        Defines the RBW in terms of the 6 dB bandwidth of the window specified by the :py:attr:`nirfsa.Session.fft_window_type` property.

        



    .. py:attribute:: SpectrumResolutionBandwidthType.BIN_WIDTH



        Defines the RBW in terms of the display resolution, which is the ratio of the sampling frequency to the number of samples that you acquire.

        



    .. py:attribute:: SpectrumResolutionBandwidthType.EQUIVALENT_NOISE_BANDWIDTH



        Defines the RBW in terms of the equivalent noise bandwidth (ENBW) of the window specified by the :py:attr:`nirfsa.Session.fft_window_type` property.

        



StartTriggerDigitalEdgeEdge
---------------------------

.. py:class:: StartTriggerDigitalEdgeEdge

    .. py:attribute:: StartTriggerDigitalEdgeEdge.RISING



        The trigger asserts on the rising edge of the signal.PXI-5661, PXIe-5663/5663E/5665/5668

        



    .. py:attribute:: StartTriggerDigitalEdgeEdge.FALLING



        The trigger asserts on the falling edge of the signal | PXIe-5668

        



StartTriggerType
----------------

.. py:class:: StartTriggerType

    .. py:attribute:: StartTriggerType.NONE



        No Start Trigger is configured.

        



    .. py:attribute:: StartTriggerType.DIGITAL_EDGE



        The Start Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the :py:attr:`nirfsa.Session.digital_edge_start_trigger_source` property.

        



    .. py:attribute:: StartTriggerType.SOFTWARE_EDGE



        The Start Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the :py:meth:`nirfsa.Session.send_software_edge_trigger` method and selecting :py:data:`~nirfsa.NIRFSA_VAL_START_TRIGGER` as the value of the **trigger** parameter.

        



StepsToOmit
-----------

.. py:class:: StepsToOmit

    .. py:attribute:: StepsToOmit.DEEMBEDDING_TABLES



        Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.

        



    .. py:attribute:: StepsToOmit.NONE



        No step is omitted during reset.

        



    .. py:attribute:: StepsToOmit.ROUTES



        Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.

        



SyncRefTriggerDelayEnabled
--------------------------

.. py:class:: SyncRefTriggerDelayEnabled

    .. py:attribute:: SyncRefTriggerDelayEnabled.DISABLED



        Disables synchronization reference trigger delay.

        



    .. py:attribute:: SyncRefTriggerDelayEnabled.ENABLED



        Enables synchronization reference trigger delay.

        



UserSourcePulseWidthUnits
-------------------------

.. py:class:: UserSourcePulseWidthUnits

    .. py:attribute:: UserSourcePulseWidthUnits.SECONDS



        Units are seconds.

        



    .. py:attribute:: UserSourcePulseWidthUnits.CLOCK_PERIODS



        Units are clock periods.

        





