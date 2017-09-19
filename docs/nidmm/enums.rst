Enums
=====

Enums used in NI-DMM

.. py:currentmodule:: nidmm



.. py:data:: ADCCalibration

    .. py:attribute:: AUTO



        The DMM enables or disables ADC calibration based on the configured
        function and resolution.

        


    .. py:attribute:: OFF



        The DMM does not compensate for changes to the gain.

        


    .. py:attribute:: ON



        The DMM measures an internal reference to calculate the correct gain for
        the measurement.

        



.. py:data:: AcquisitionStatus

    .. py:attribute:: RUNNING



        Running

        


    .. py:attribute:: FINISHED_WITH_BACKLOG



        Finished with **Backlog**

        


    .. py:attribute:: FINISHED_WITH_NO_BACKLOG



        Finished with no **Backlog**

        


    .. py:attribute:: PAUSED



        Paused

        


    .. py:attribute:: NO_ACQUISITION_IN_PROGRESS



        No acquisition in progress

        



.. py:data:: ApertureTimeUnits

    .. py:attribute:: SECONDS



        Units are seconds.

        


    .. py:attribute:: POWER_LINE_CYCLES



        Units are powerline cycles (PLCs).

        



.. py:data:: AutoZero

    .. py:attribute:: AUTO



        NI-DMM chooses the Auto Zero setting based on the configured function
        and resolution.

        


    .. py:attribute:: OFF



        Disables AutoZero.

        


    .. py:attribute:: ON



        The DMM internally disconnects the input signal following each
        measurement and takes a zero reading. It then subtracts the zero reading
        from the preceding reading. For NI 4065 devices, Auto Zero is always ON.
        Auto Zero is an integral part of the signal measurement phase and adds
        no extra time to the overall measurement.

        


    .. py:attribute:: ONCE



        The DMM internally disconnects the input signal for the first
        measurement and takes a zero reading. It then subtracts the zero reading
        from the first reading and the following readings. The NI 4060/4065 does
        not support this setting.

        



.. py:data:: CableCompensationType

    .. py:attribute:: NONE



        No cable compensation.

        


    .. py:attribute:: OPEN



        Open cable compensation.

        


    .. py:attribute:: SHORT



        Short cable compensation.

        


    .. py:attribute:: OPEN_AND_SHORT



        Open and short cable compensation.

        



.. py:data:: CurrentSource

    .. py:attribute:: _1_MICROAMP



        NI 4070/4071/4072 are supported.

        


    .. py:attribute:: _10_MICROAMP



        NI 4080/4081/4082 and NI 4070/4071/4072 are supported.

        


    .. py:attribute:: _100_MICROAMP



        NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.

        


    .. py:attribute:: _1_MILLIAMP



        NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.

        



.. py:data:: DCBias

    .. py:attribute:: DC_BIAS_OFF



        NI-DMM programs the device not to use the DC bias.

        


    .. py:attribute:: DC_BIAS_ON



        NI-DMM programs the device to use the DC bias.

        



.. py:data:: DCNoiseRejection

    .. py:attribute:: AUTO



        The driver chooses the DC noise rejection setting based on the
        configured function and resolution.

        


    .. py:attribute:: NORMAL



        NI-DMM weighs all samples equally.

        


    .. py:attribute:: SECOND_ORDER



        NI-DMM weighs the samples taken in the middle of the aperture time more
        than samples taken at the beginning and the end of the measurement using
        a triangular weighing function.

        


    .. py:attribute:: HIGH_ORDER



        NI-DMM weighs the samples taken in the middle of the aperture time more
        than samples taken at the beginning and the end of the measurement using
        a bell-curve weighing function.

        



.. py:data:: DigitsResolution

    .. py:attribute:: _3_5



        Specifies 3.5 digits resolution.

        


    .. py:attribute:: _4_5



        Specifies 4.5 digits resolution.

        


    .. py:attribute:: _5_5



        Specifies 5.5 digits resolution.

        


    .. py:attribute:: _6_5



        Specifies 6.5 digits resolution.

        


    .. py:attribute:: _7_5



        Specifies 7.5 digits resolution.

        



.. py:data:: Function

    .. py:attribute:: DC_VOLTS



        All devices supported.

        


    .. py:attribute:: AC_VOLTS



        All devices supported.

        


    .. py:attribute:: DC_CURRENT



        All devices supported.

        


    .. py:attribute:: AC_CURRENT



        All devices supported.

        


    .. py:attribute:: _2_WIRE_RESISTANCE



        All devices supported.

        


    .. py:attribute:: _4_WIRE_RESISTANCE



        NI 4065, and NI 4070/4071/4072 supported.

        


    .. py:attribute:: FREQUENCY



        NI 4070/4071/4072 supported.

        


    .. py:attribute:: PERIOD



        NI 4070/4071/4072 supported.

        


    .. py:attribute:: TEMPERATURE



        NI 4065, and NI 4070/4071/4072 supported.

        


    .. py:attribute:: _AC_VOLTS_DC_COUPLED



        NI 4070/4071/4072 supported.

        


    .. py:attribute:: DIODE



        All devices supported.

        


    .. py:attribute:: WAVEFORM_VOLTAGE



        NI 4070/4071/4072 supported.

        


    .. py:attribute:: _WAVEFORM_CURRENT



        NI 4070/4071/4072 supported.

        


    .. py:attribute:: CAPACITANCE



        NI 4072 supported.

        


    .. py:attribute:: INDUCTANCE



        NI 4072 supported.

        



.. py:data:: InputResistance

    .. py:attribute:: _1_M_OHM



        Input resistance of 1 M Ohm

        


    .. py:attribute:: _10_M_OHM



        Input resistance of 10 M Ohm

        


    .. py:attribute:: GREATER_THAN_10_G_OHM



        Input resistance greater than 10 G Ohm

        



.. py:data:: LCCalculationModel

    .. py:attribute:: AUTO



        NI-DMM chooses the algorithm based on function and range.

        


    .. py:attribute:: SERIES



        NI-DMM uses the series impedance model to calculate capacitance and
        inductance.

        


    .. py:attribute:: PARALLEL



        NI-DMM uses the parallel admittance model to calculate capacitance and
        inductance.

        



.. py:data:: MeasurementCompleteDest

    .. py:attribute:: NONE



        No destination specified.

        


    .. py:attribute:: EXTERNAL



        Pin 6 on the AUX Connector

        


    .. py:attribute:: TTL_0



        PXI Trigger Line 0

        


    .. py:attribute:: TTL_1



        PXI Trigger Line 1

        


    .. py:attribute:: TL_2



        PXI Trigger Line 2

        


    .. py:attribute:: TTL_3



        PXI Trigger Line 3

        


    .. py:attribute:: TL_4



        PXI Trigger Line 4

        


    .. py:attribute:: TTL_5



        PXI Trigger Line 5

        


    .. py:attribute:: TTL_6



        PXI Trigger Line 6

        


    .. py:attribute:: TTL_7



        PXI Trigger Line 7

        


    .. py:attribute:: _LBR_TRIG_0



        Local Bus Right Trigger Line 0 of PXI/SCXI combination chassis

        



.. py:data:: MeasurementDestinationSlope

    .. py:attribute:: POSITIVE



        The driver triggers on the rising edge of the trigger signal.

        


    .. py:attribute:: NEGATIVE



        The driver triggers on the falling edge of the trigger signal.

        



.. py:data:: OffsetCompensatedOhms

    .. py:attribute:: OFF



        Disables Offset Compensated Ohms.

        


    .. py:attribute:: ON



        Enables Offset Compensated Ohms.

        



.. py:data:: OperationMode

    .. py:attribute:: _IVIDMM_MODE



        Single or multipoint measurements: When the Trigger Count and Sample
        Count properties are both set to 1, the NI 4065, NI 4070/4071/4072, and
        NI 4080/4081/4082 take a single-point measurement; otherwise, NI-DMM
        takes multipoint measurements.

        


    .. py:attribute:: WAVEFORM_MODE



        Configures the NI 4080/4081/4082 and NI 4070/4071/4072 to take waveform
        measurements.

        



.. py:data:: PowerlineFrequency

    .. py:attribute:: _50_HZ



        Specifies the powerline frequency as 50 Hz.

        


    .. py:attribute:: _60_HZ



        Specifies the powerline frequency as 60 Hz.

        



.. py:data:: RTDType

    .. py:attribute:: CUSTOM



        Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
        and C coefficients.

        


    .. py:attribute:: PT_3750



        Performs scaling for a Pt 3750 RTD.

        


    .. py:attribute:: PT_3851



        Performs scaling for a Pt 3851 RTD.

        


    .. py:attribute:: PT_3911



        Performs scaling for a Pt 3911 RTD.

        


    .. py:attribute:: PT_3916



        Performs scaling for a Pt 3916 RTD.

        


    .. py:attribute:: PT_3920



        Performs scaling for a Pt 3920 RTD.

        


    .. py:attribute:: PT_3928



        Performs scaling for a Pt 3928 RTD.

        



.. py:data:: SampleTrigSlope

    .. py:attribute:: POSITIVE



        The driver triggers on the rising edge of the trigger signal.

        


    .. py:attribute:: NEGATIVE



        The driver triggers on the falling edge of the trigger signal.

        



.. py:data:: SampleTrigger

    .. py:attribute:: IMMEDIATE



        No trigger specified

        


    .. py:attribute:: _EXTERNAL



        Pin 9 on the AUX Connector

        


    .. py:attribute:: SOFTWARE_TRIG



        Configures the DMM to wait until `niDMM Send Software
        Trigger <dmmviref.chm::/niDMM_Send_Software_Trigger.html>`__ is called.

        


    .. py:attribute:: INTERVAL



        Interval trigger

        


    .. py:attribute:: TTL_0



        PXI Trigger Line 0

        


    .. py:attribute:: TTL_1



        PXI Trigger Line 1

        


    .. py:attribute:: TTL_2



        PXI Trigger Line 2

        


    .. py:attribute:: _TTL_3



        PXI Trigger Line 3

        


    .. py:attribute:: TTL_4



        PXI Trigger Line 4

        


    .. py:attribute:: TTL_5



        PXI Trigger Line 5

        


    .. py:attribute:: TTL_6



        PXI Trigger Line 6

        


    .. py:attribute:: TTL_7



        PXI Trigger Line 7

        


    .. py:attribute:: PXI_STAR



        PXI Star trigger line

        


    .. py:attribute:: AUX_TRIG_1



        Pin 3 on the AUX connector

        


    .. py:attribute:: LBR_TRIG_1



        Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis

        



.. py:data:: ThermistorType

    .. py:attribute:: CUSTOM



        Performs Steinhart-Hart thermistor scaling with the user-specified A, B,
        and C coefficients.

        


    .. py:attribute:: _44004



        Performs scaling for an Omega Series 44004 thermistor.

        


    .. py:attribute:: _44006



        Performs scaling for an Omega Series 44006 thermistor.

        


    .. py:attribute:: _44007



        Performs scaling for an Omega Series 44007 thermistor.

        



.. py:data:: ThermocoupleReferenceJunctionType

    .. py:attribute:: FIXED



        Thermocouple reference juction is fixed at the user-specified
        temperature.

        



.. py:data:: ThermocoupleType

    .. py:attribute:: B



        Thermocouple type B

        


    .. py:attribute:: E



        Thermocouple type E

        


    .. py:attribute:: J



        Thermocouple type J

        


    .. py:attribute:: K



        Thermocouple type K

        


    .. py:attribute:: N



        Thermocouple type N

        


    .. py:attribute:: R



        Thermocouple type R

        


    .. py:attribute:: S



        Thermocouple type S

        


    .. py:attribute:: T



        Thermocouple type T

        



.. py:data:: TransducerType

    .. py:attribute:: THERMOCOUPLE



        Use for thermocouple measurements.

        


    .. py:attribute:: THERMISTOR



        Use for thermistor measurements.

        


    .. py:attribute:: _2_WIRE_RTD



        Use for 2-wire RTD measurements.

        


    .. py:attribute:: _4_WIRE_RTD



        Use for 4-wire RTD measurements.

        



.. py:data:: TriggerSlope

    .. py:attribute:: POSITIVE



        The driver triggers on the rising edge of the trigger signal.

        


    .. py:attribute:: NEGATIVE



        The driver triggers on the falling edge of the trigger signal.

        



.. py:data:: TriggerSource

    .. py:attribute:: IMMEDIATE



        No trigger specified.

        


    .. py:attribute:: EXTERNAL



        Pin 9 on the AUX Connector

        


    .. py:attribute:: SOFTWARE_TRIG



        Waits until `niDMM Send Software
        Trigger <dmmviref.chm::/niDMM_Send_Software_Trigger.html>`__ is called.

        


    .. py:attribute:: _TTL_0



        PXI Trigger Line 0

        


    .. py:attribute:: TTL_1



        PXI Trigger Line 1

        


    .. py:attribute:: TTL_2



        PXI Trigger Line 2

        


    .. py:attribute:: _TTL_3



        PXI Trigger Line 3

        


    .. py:attribute:: TTL_4



        PXI Trigger Line 4

        


    .. py:attribute:: TTL_5



        PXI Trigger Line 5

        


    .. py:attribute:: TTL_6



        PXI Trigger Line 6

        


    .. py:attribute:: _TTL_7



        PXI Trigger Line 7

        


    .. py:attribute:: _PXI_STAR



        PXI Star Trigger Line

        


    .. py:attribute:: AUX_TRIG_1



        Pin 3 on the AUX connector

        


    .. py:attribute:: LBR_TRIG_1



        Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis

        



.. py:data:: WaveformCoupling

    .. py:attribute:: AC



        Specifies AC coupling.

        


    .. py:attribute:: DC



        Specifies DC coupling.

        

