Enums
=====

Enums used in NI-DCPower

.. py:currentmodule:: nidcpower



.. py:data:: ApertureTimeUnits

    .. py:attribute:: SECONDS



        Specifies aperture time in seconds.

        


    .. py:attribute:: POWER_LINE_CYCLES



        Specifies aperture time in power line cycles (PLCs).

        



.. py:data:: AutoZero

    .. py:attribute:: OFF



        Disables auto-zero.

        


    .. py:attribute:: ON



        Makes zero conversions for every measurement.

        


    .. py:attribute:: ONCE



        Makes zero conversions following the first measurement after initiating
        the device. The device uses these zero conversions for the preceding
        measurement and future measurements until the device is reinitiated.

        



.. py:data:: CurrentLevelAutorange

    .. py:attribute:: OFF



        NI-DCPower does not automatically select the current level range.

        


    .. py:attribute:: ON



        NI-DCPower automatically selects the current level range.

        



.. py:data:: CurrentLimitAutorange

    .. py:attribute:: OFF



        NI-DCPower does not automatically select the current limit range.

        


    .. py:attribute:: ON



        NI-DCPower automatically selects the current limit range.

        



.. py:data:: CurrentLimitBehavior

    .. py:attribute:: CURRENT_REGULATE



        

        


    .. py:attribute:: CURRENT_TRIP



        

        



.. py:data:: DCNoiseRejection

    .. py:attribute:: SECOND_ORDER



        Second-order DC noise rejection. Refer to `Configuring the Measure
        Unit <NI_DC_Power_Supplies_Help.chm::/ConfiguringTheMeasureUnit.html>`__
        for supported devices.

        


    .. py:attribute:: NORMAL



        Normal DC noise rejection.

        



.. py:data:: DigitalEdge

    .. py:attribute:: RISING



        Asserts the trigger on the rising edge of the digital signal.

        


    .. py:attribute:: FALLING



        Asserts the trigger on the falling edge of the digital signal.

        



.. py:data:: MeasureWhen

    .. py:attribute:: AUTOMATICALLY_AFTER_SOURCE_COMPLETE



        Acquires a measurement after each Source Complete event completes. Use
        the `niDCPower Fetch
        Multiple <NIDCPowerVIRef.chm::/niDCPower_Fetch_Multiple.html>`__ VI to
        retrieve the measurements.

        


    .. py:attribute:: ON_DEMAND



        Acquires a measurement when the `niDCPower
        Measure <NIDCPowerVIRef.chm::/niDCPower_Measure.html>`__ VI or
        `niDCPower Measure
        Multiple <NIDCPowerVIRef.chm::/niDCPower_Measure_Multiple.html>`__ VI is
        called.

        


    .. py:attribute:: ON_MEASURE_TRIGGER



        Acquires a measurement when a Measure trigger is received. Use the
        `niDCPower Fetch
        Multiple <NIDCPowerVIRef.chm::/niDCPower_Fetch_Multiple.html>`__ VI to
        retrieve the measurements.

        



.. py:data:: OutputCapacitance

    .. py:attribute:: LOW



        Output capacitance is low.

        


    .. py:attribute:: HIGH



        Output capacitance is high.

        



.. py:data:: OutputFunction

    .. py:attribute:: DC_VOLTAGE



        Sets the output function to DC voltage.

        


    .. py:attribute:: DC_CURRENT



        Sets the output function to DC current.

        


    .. py:attribute:: PULSE_VOLTAGE



        Sets the output function to pulse voltage.

        


    .. py:attribute:: PULSE_CURRENT



        Sets the output function to pulse current.

        



.. py:data:: Polarity

    .. py:attribute:: ACTIVE_HIGH



        A high pulse occurs when the event is generated. The exported signal is
        low level both before and after the event is generated.

        


    .. py:attribute:: ACTIVE_LOW



        A low pulse occurs when the event is generated. The exported signal is
        high level both before and after the event is generated.

        



.. py:data:: PowerLineFrequency

    .. py:attribute:: _50_HERTZ



        Specifies a power line frequency of 50 Hz.

        


    .. py:attribute:: _60_HERTZ



        Specifies a power line frequency of 60 Hz.

        



.. py:data:: PowerSource

    .. py:attribute:: INTERNAL



        Uses the PXI chassis power source.

        


    .. py:attribute:: AUXILIARY



        Uses the auxiliary power source connected to the device.

        


    .. py:attribute:: AUTOMATIC



        Uses the auxiliary power source if it is available; otherwise, use the
        PXI chassis power source.

        



.. py:data:: PowerSourceInUse

    .. py:attribute:: INTERNAL



        Uses the PXI chassis power source.

        


    .. py:attribute:: AUXILIARY



        Uses the auxiliary power source connected to the device. Only the NI
        PXI-4110, NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this
        value. This is the only supported value for the NI PXIe-4112 and NI
        PXIe-4113.

        



.. py:data:: SelfCalibrationPersistence

    .. py:attribute:: KEEP_IN_MEMORY



        Keep new self-calibration values in memory only.

        


    .. py:attribute:: WRITE_TO_EEPROM



        Write new self-calibration values to hardware. Refer to your device
        documentation for more information about the implications of frequent
        writes to the EEPROM.

        



.. py:data:: Sense

    .. py:attribute:: LOCAL



        Local sensing is selected.

        


    .. py:attribute:: REMOTE



        Remote sensing is selected.

        



.. py:data:: SourceMode

    .. py:attribute:: SINGLE_POINT



        The source unit applies a single source configuration.

        


    .. py:attribute:: SEQUENCE



        The source unit sequentially applies a list of voltage or current
        configurations.

        



.. py:data:: TransientResponse

    .. py:attribute:: NORMAL



        Normal transient response time.

        


    .. py:attribute:: FAST



        Fast transient response time.

        


    .. py:attribute:: SLOW



        Slow transient response time. Refer to `Configuring Transient
        Response <NI_DC_Power_Supplies_Help.chm::/CompensatingforLoad.html>`__
        for supported devices.

        


    .. py:attribute:: CUSTOM



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

    .. py:attribute:: NONE



        No trigger is configured.

        


    .. py:attribute:: DIGITAL_EDGE



        The data operation starts when a digital edge is detected.

        


    .. py:attribute:: SOFTWARE_EDGE



        The data operation starts when a software trigger occurs.

        



.. py:data:: VoltageLevelAutorange

    .. py:attribute:: OFF



        NI-DCPower does not automatically select the voltage level range.

        


    .. py:attribute:: ON



        NI-DCPower automatically selects the voltage level range.

        



.. py:data:: VoltageLimitAutorange

    .. py:attribute:: OFF



        NI-DCPower does not automatically select the voltage limit range.

        


    .. py:attribute:: ON



        NI-DCPower automatically selects the voltage limit range.

        



.. py:data:: tBoolean

    .. py:attribute:: FALSE



        

        


    .. py:attribute:: TRUE



        

        

