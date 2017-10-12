Enums
=====

Enums used in NI-DCPower

.. py:currentmodule:: nidcpower



.. py:data:: ApertureTimeUnits

    .. py:attribute:: nidcpower.ApertureTimeUnits.SECONDS



        Specifies aperture time in seconds.

        



    .. py:attribute:: nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES



        Specifies aperture time in power line cycles (PLCs).

        




.. py:data:: AutoZero

    .. py:attribute:: nidcpower.AutoZero.OFF



        Disables auto-zero.

        



    .. py:attribute:: nidcpower.AutoZero.ON



        Makes zero conversions for every measurement.

        



    .. py:attribute:: nidcpower.AutoZero.ONCE



        Makes zero conversions following the first measurement after initiating
        the device. The device uses these zero conversions for the preceding
        measurement and future measurements until the device is reinitiated.

        




.. py:data:: CurrentLevelAutorange

    .. py:attribute:: nidcpower.CurrentLevelAutorange.OFF



        NI-DCPower does not automatically select the current level range.

        



    .. py:attribute:: nidcpower.CurrentLevelAutorange.ON



        NI-DCPower automatically selects the current level range.

        




.. py:data:: CurrentLimitAutorange

    .. py:attribute:: nidcpower.CurrentLimitAutorange.OFF



        NI-DCPower does not automatically select the current limit range.

        



    .. py:attribute:: nidcpower.CurrentLimitAutorange.ON



        NI-DCPower automatically selects the current limit range.

        




.. py:data:: CurrentLimitBehavior

    .. py:attribute:: nidcpower.CurrentLimitBehavior.CURRENT_REGULATE



        

        



    .. py:attribute:: nidcpower.CurrentLimitBehavior.CURRENT_TRIP



        

        




.. py:data:: DCNoiseRejection

    .. py:attribute:: nidcpower.DCNoiseRejection.SECOND_ORDER



        Second-order DC noise rejection. Refer to `Configuring the Measure
        Unit <NI_DC_Power_Supplies_Help.chm::/ConfiguringTheMeasureUnit.html>`__
        for supported devices.

        



    .. py:attribute:: nidcpower.DCNoiseRejection.NORMAL



        Normal DC noise rejection.

        




.. py:data:: DigitalEdge

    .. py:attribute:: nidcpower.DigitalEdge.RISING



        Asserts the trigger on the rising edge of the digital signal.

        



    .. py:attribute:: nidcpower.DigitalEdge.FALLING



        Asserts the trigger on the falling edge of the digital signal.

        




.. py:data:: Event

    .. py:attribute:: nidcpower.Event.SOURCE_COMPLETE



        



    .. py:attribute:: nidcpower.Event.MEASURE_COMPLETE



        



    .. py:attribute:: nidcpower.Event.SEQUENCE_ITERATION_COMPLETE



        



    .. py:attribute:: nidcpower.Event.SEQUENCE_ENGINE_DONE



        



    .. py:attribute:: nidcpower.Event.PULSE_COMPLETE



        



    .. py:attribute:: nidcpower.Event.READY_FOR_PULSE_TRIGGER



        




.. py:data:: MeasureWhen

    .. py:attribute:: nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE



        Acquires a measurement after each Source Complete event completes. Use
        the `niDCPower Fetch
        Multiple <NIDCPowerVIRef.chm::/niDCPower_Fetch_Multiple.html>`__ VI to
        retrieve the measurements.

        



    .. py:attribute:: nidcpower.MeasureWhen.ON_DEMAND



        Acquires a measurement when the `niDCPower
        Measure <NIDCPowerVIRef.chm::/niDCPower_Measure.html>`__ VI or
        `niDCPower Measure
        Multiple <NIDCPowerVIRef.chm::/niDCPower_Measure_Multiple.html>`__ VI is
        called.

        



    .. py:attribute:: nidcpower.MeasureWhen.ON_MEASURE_TRIGGER



        Acquires a measurement when a Measure trigger is received. Use the
        `niDCPower Fetch
        Multiple <NIDCPowerVIRef.chm::/niDCPower_Fetch_Multiple.html>`__ VI to
        retrieve the measurements.

        




.. py:data:: MeasurementTypes

    .. py:attribute:: nidcpower.MeasurementTypes.MEASURE_VOLTAGE



        The device measures voltage.

        



    .. py:attribute:: nidcpower.MeasurementTypes.MEASURE_CURRENT



        The device measures current.

        




.. py:data:: OutputCapacitance

    .. py:attribute:: nidcpower.OutputCapacitance.LOW



        Output capacitance is low.

        



    .. py:attribute:: nidcpower.OutputCapacitance.HIGH



        Output capacitance is high.

        




.. py:data:: OutputFunction

    .. py:attribute:: nidcpower.OutputFunction.DC_VOLTAGE



        Sets the output function to DC voltage.

        



    .. py:attribute:: nidcpower.OutputFunction.DC_CURRENT



        Sets the output function to DC current.

        



    .. py:attribute:: nidcpower.OutputFunction.PULSE_VOLTAGE



        Sets the output function to pulse voltage.

        



    .. py:attribute:: nidcpower.OutputFunction.PULSE_CURRENT



        Sets the output function to pulse current.

        




.. py:data:: OutputStates

    .. py:attribute:: nidcpower.OutputStates.OUTPUT_CONSTANT_VOLTAGE



        The device maintains a constant voltage by adjusting the current

        



    .. py:attribute:: nidcpower.OutputStates.OUTPUT_CONSTANT_CURRENT



        The device maintains a constant current by adjusting the voltage.

        




.. py:data:: Polarity

    .. py:attribute:: nidcpower.Polarity.ACTIVE_HIGH



        A high pulse occurs when the event is generated. The exported signal is
        low level both before and after the event is generated.

        



    .. py:attribute:: nidcpower.Polarity.ACTIVE_LOW



        A low pulse occurs when the event is generated. The exported signal is
        high level both before and after the event is generated.

        




.. py:data:: PowerLineFrequency

    .. py:attribute:: nidcpower.PowerLineFrequency._50_HERTZ



        Specifies a power line frequency of 50 Hz.

        



    .. py:attribute:: nidcpower.PowerLineFrequency._60_HERTZ



        Specifies a power line frequency of 60 Hz.

        




.. py:data:: PowerSource

    .. py:attribute:: nidcpower.PowerSource.INTERNAL



        Uses the PXI chassis power source.

        



    .. py:attribute:: nidcpower.PowerSource.AUXILIARY



        Uses the auxiliary power source connected to the device.

        



    .. py:attribute:: nidcpower.PowerSource.AUTOMATIC



        Uses the auxiliary power source if it is available; otherwise, use the
        PXI chassis power source.

        




.. py:data:: PowerSourceInUse

    .. py:attribute:: nidcpower.PowerSourceInUse.INTERNAL



        Uses the PXI chassis power source.

        



    .. py:attribute:: nidcpower.PowerSourceInUse.AUXILIARY



        Uses the auxiliary power source connected to the device. Only the NI
        PXI-4110, NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this
        value. This is the only supported value for the NI PXIe-4112 and NI
        PXIe-4113.

        




.. py:data:: SelfCalibrationPersistence

    .. py:attribute:: nidcpower.SelfCalibrationPersistence.KEEP_IN_MEMORY



        Keep new self-calibration values in memory only.

        



    .. py:attribute:: nidcpower.SelfCalibrationPersistence.WRITE_TO_EEPROM



        Write new self-calibration values to hardware. Refer to your device
        documentation for more information about the implications of frequent
        writes to the EEPROM.

        




.. py:data:: SendSoftwareEdgeTriggerType

    .. py:attribute:: nidcpower.SendSoftwareEdgeTriggerType.START



        



    .. py:attribute:: nidcpower.SendSoftwareEdgeTriggerType.SOURCE



        



    .. py:attribute:: nidcpower.SendSoftwareEdgeTriggerType.MEASURE



        



    .. py:attribute:: nidcpower.SendSoftwareEdgeTriggerType.SEQUENCE_ADVANCE



        



    .. py:attribute:: nidcpower.SendSoftwareEdgeTriggerType.PULSE



        




.. py:data:: Sense

    .. py:attribute:: nidcpower.Sense.LOCAL



        Local sensing is selected.

        



    .. py:attribute:: nidcpower.Sense.REMOTE



        Remote sensing is selected.

        




.. py:data:: Signals

    .. py:attribute:: nidcpower.Signals.SOURCE_COMPLETE_EVENT



        Exports the Source Complete event.

        



    .. py:attribute:: nidcpower.Signals.MEASURE_COMPLETE_EVENT



        Exports the Measure Complete event.

        



    .. py:attribute:: nidcpower.Signals.SEQUENCE_ITERATION_COMPLETE_EVENT



        Exports the Sequence Iteration Complete event.

        



    .. py:attribute:: nidcpower.Signals.SEQUENCE_ENGINE_DONE_EVENT



        Exports the Sequence Engine Done event.

        



    .. py:attribute:: nidcpower.Signals.PULSE_COMPLETE_EVENT



        Exports the Pulse Complete event.

        



    .. py:attribute:: nidcpower.Signals.READY_FOR_PULSE_TRIGGER_EVENT



        Exports the Ready Pulse Trigger event.

        



    .. py:attribute:: nidcpower.Signals.START_TRIGGER



        Exports the Start trigger.

        



    .. py:attribute:: nidcpower.Signals.SOURCE_TRIGGER



        Exports the Source trigger.

        



    .. py:attribute:: nidcpower.Signals.MEASURE_TRIGGER



        Exports the Measure trigger.

        



    .. py:attribute:: nidcpower.Signals.SEQUENCE_ADVANCE_TRIGGER



        Exports the Sequence Advance trigger.

        



    .. py:attribute:: nidcpower.Signals.PULSE_TRIGGER



        Exports the Pulse trigger.

        




.. py:data:: SourceMode

    .. py:attribute:: nidcpower.SourceMode.SINGLE_POINT



        The source unit applies a single source configuration.

        



    .. py:attribute:: nidcpower.SourceMode.SEQUENCE



        The source unit sequentially applies a list of voltage or current
        configurations.

        




.. py:data:: TransientResponse

    .. py:attribute:: nidcpower.TransientResponse.NORMAL



        Normal transient response time.

        



    .. py:attribute:: nidcpower.TransientResponse.FAST



        Fast transient response time.

        



    .. py:attribute:: nidcpower.TransientResponse.SLOW



        Slow transient response time. Refer to `Configuring Transient
        Response <NI_DC_Power_Supplies_Help.chm::/CompensatingforLoad.html>`__
        for supported devices.

        



    .. py:attribute:: nidcpower.TransientResponse.CUSTOM



        Custom transient response time. If you select this value, you can then
        specify values for the `Voltage Gain
        Bandwidth <pniDCPower_VoltageGainBandwidth.html>`__, `Voltage
        Compensation
        Frequency <pniDCPower_VoltageCompensationFrequency.html>`__, `Voltage
        Pole-Zero Frequency <pniDCPower_VoltagePoleZeroRatio.html>`__, `Current
        Gain Bandwidth <pniDCPower_CurrentGainBandwidth.html>`__, `Current
        Compensation
        Frequency <pniDCPower_CurrentCompensationFrequency.html>`__, and
        `Current Pole-Zero Ratio <pniDCPower_CurrentPoleZeroRatio.html>`__
        properties. Refer to `Configuring Transient
        Response <NI_DC_Power_Supplies_Help.chm::/CompensatingforLoad.html>`__
        for supported devices.

        




.. py:data:: TriggerType

    .. py:attribute:: nidcpower.TriggerType.NONE



        No trigger is configured.

        



    .. py:attribute:: nidcpower.TriggerType.DIGITAL_EDGE



        The data operation starts when a digital edge is detected.

        



    .. py:attribute:: nidcpower.TriggerType.SOFTWARE_EDGE



        The data operation starts when a software trigger occurs.

        




.. py:data:: VoltageLevelAutorange

    .. py:attribute:: nidcpower.VoltageLevelAutorange.OFF



        NI-DCPower does not automatically select the voltage level range.

        



    .. py:attribute:: nidcpower.VoltageLevelAutorange.ON



        NI-DCPower automatically selects the voltage level range.

        




.. py:data:: VoltageLimitAutorange

    .. py:attribute:: nidcpower.VoltageLimitAutorange.OFF



        NI-DCPower does not automatically select the voltage limit range.

        



    .. py:attribute:: nidcpower.VoltageLimitAutorange.ON



        NI-DCPower automatically selects the voltage limit range.

        


