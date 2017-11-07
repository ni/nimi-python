Enums
=====

Enums used in NI-DMM

.. py:currentmodule:: nidmm



.. py:data:: ADCCalibration

    .. py:attribute:: nidmm.ADCCalibration.AUTO



        The DMM enables or disables ADC calibration based on the configured
        function and resolution.

        



    .. py:attribute:: nidmm.ADCCalibration.OFF



        The DMM does not compensate for changes to the gain.

        



    .. py:attribute:: nidmm.ADCCalibration.ON



        The DMM measures an internal reference to calculate the correct gain for
        the measurement.

        




.. py:data:: AcquisitionStatus

    .. py:attribute:: nidmm.AcquisitionStatus.RUNNING



        Running

        



    .. py:attribute:: nidmm.AcquisitionStatus.FINISHED_WITH_BACKLOG



        Finished with **Backlog**

        



    .. py:attribute:: nidmm.AcquisitionStatus.FINISHED_WITH_NO_BACKLOG



        Finished with no **Backlog**

        



    .. py:attribute:: nidmm.AcquisitionStatus.PAUSED



        Paused

        



    .. py:attribute:: nidmm.AcquisitionStatus.NO_ACQUISITION_IN_PROGRESS



        No acquisition in progress

        




.. py:data:: ApertureTimeUnits

    .. py:attribute:: nidmm.ApertureTimeUnits.SECONDS



        Units are seconds.

        



    .. py:attribute:: nidmm.ApertureTimeUnits.POWER_LINE_CYCLES



        Units are powerline cycles (PLCs).

        




.. py:data:: AutoZero

    .. py:attribute:: nidmm.AutoZero.AUTO



        NI-DMM chooses the Auto Zero setting based on the configured function
        and resolution.

        



    .. py:attribute:: nidmm.AutoZero.OFF



        Disables AutoZero.

        



    .. py:attribute:: nidmm.AutoZero.ON



        The DMM internally disconnects the input signal following each
        measurement and takes a zero reading. It then subtracts the zero reading
        from the preceding reading. For NI 4065 devices, Auto Zero is always ON.
        Auto Zero is an integral part of the signal measurement phase and adds
        no extra time to the overall measurement.

        



    .. py:attribute:: nidmm.AutoZero.ONCE



        The DMM internally disconnects the input signal for the first
        measurement and takes a zero reading. It then subtracts the zero reading
        from the first reading and the following readings. The NI 4060/4065 does
        not support this setting.

        




.. py:data:: CableCompensationType

    .. py:attribute:: nidmm.CableCompensationType.NONE



        No cable compensation.

        



    .. py:attribute:: nidmm.CableCompensationType.OPEN



        Open cable compensation.

        



    .. py:attribute:: nidmm.CableCompensationType.SHORT



        Short cable compensation.

        



    .. py:attribute:: nidmm.CableCompensationType.OPEN_AND_SHORT



        Open and short cable compensation.

        




.. py:data:: CurrentSource

    .. py:attribute:: nidmm.CurrentSource._1_MICROAMP



        NI 4070/4071/4072 are supported.

        



    .. py:attribute:: nidmm.CurrentSource._10_MICROAMP



        NI 4080/4081/4082 and NI 4070/4071/4072 are supported.

        



    .. py:attribute:: nidmm.CurrentSource._100_MICROAMP



        NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.

        



    .. py:attribute:: nidmm.CurrentSource._1_MILLIAMP



        NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.

        




.. py:data:: DCBias

    .. py:attribute:: nidmm.DCBias.DC_BIAS_OFF



        NI-DMM programs the device not to use the DC bias.

        



    .. py:attribute:: nidmm.DCBias.DC_BIAS_ON



        NI-DMM programs the device to use the DC bias.

        




.. py:data:: DCNoiseRejection

    .. py:attribute:: nidmm.DCNoiseRejection.AUTO



        The driver chooses the DC noise rejection setting based on the
        configured function and resolution.

        



    .. py:attribute:: nidmm.DCNoiseRejection.NORMAL



        NI-DMM weighs all samples equally.

        



    .. py:attribute:: nidmm.DCNoiseRejection.SECOND_ORDER



        NI-DMM weighs the samples taken in the middle of the aperture time more
        than samples taken at the beginning and the end of the measurement using
        a triangular weighing function.

        



    .. py:attribute:: nidmm.DCNoiseRejection.HIGH_ORDER



        NI-DMM weighs the samples taken in the middle of the aperture time more
        than samples taken at the beginning and the end of the measurement using
        a bell-curve weighing function.

        




.. py:data:: Function

    .. py:attribute:: nidmm.Function.DC_VOLTS



        All devices supported.

        



    .. py:attribute:: nidmm.Function.AC_VOLTS



        All devices supported.

        



    .. py:attribute:: nidmm.Function.DC_CURRENT



        All devices supported.

        



    .. py:attribute:: nidmm.Function.AC_CURRENT



        All devices supported.

        



    .. py:attribute:: nidmm.Function._2_WIRE_RESISTANCE



        All devices supported.

        



    .. py:attribute:: nidmm.Function._4_WIRE_RESISTANCE



        NI 4065, and NI 4070/4071/4072 supported.

        



    .. py:attribute:: nidmm.Function.FREQUENCY



        NI 4070/4071/4072 supported.

        



    .. py:attribute:: nidmm.Function.PERIOD



        NI 4070/4071/4072 supported.

        



    .. py:attribute:: nidmm.Function.TEMPERATURE



        NI 4065, and NI 4070/4071/4072 supported.

        



    .. py:attribute:: nidmm.Function.AC_VOLTS_DC_COUPLED



        NI 4070/4071/4072 supported.

        



    .. py:attribute:: nidmm.Function.DIODE



        All devices supported.

        



    .. py:attribute:: nidmm.Function.WAVEFORM_VOLTAGE



        NI 4070/4071/4072 supported.

        



    .. py:attribute:: nidmm.Function.WAVEFORM_CURRENT



        NI 4070/4071/4072 supported.

        



    .. py:attribute:: nidmm.Function.CAPACITANCE



        NI 4072 supported.

        



    .. py:attribute:: nidmm.Function.INDUCTANCE



        NI 4072 supported.

        




.. py:data:: InputResistance

    .. py:attribute:: nidmm.InputResistance._1_M_OHM



        Input resistance of 1 M Ohm

        



    .. py:attribute:: nidmm.InputResistance._10_M_OHM



        Input resistance of 10 M Ohm

        



    .. py:attribute:: nidmm.InputResistance.GREATER_THAN_10_G_OHM



        Input resistance greater than 10 G Ohm

        




.. py:data:: LCCalculationModel

    .. py:attribute:: nidmm.LCCalculationModel.AUTO



        NI-DMM chooses the algorithm based on function and range.

        



    .. py:attribute:: nidmm.LCCalculationModel.SERIES



        NI-DMM uses the series impedance model to calculate capacitance and
        inductance.

        



    .. py:attribute:: nidmm.LCCalculationModel.PARALLEL



        NI-DMM uses the parallel admittance model to calculate capacitance and
        inductance.

        




.. py:data:: MeasurementCompleteDest

    .. py:attribute:: nidmm.MeasurementCompleteDest.NONE



        No destination specified.

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.EXTERNAL



        Pin 6 on the AUX Connector

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.TTL_0



        PXI Trigger Line 0

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.TTL_1



        PXI Trigger Line 1

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.TL_2



        PXI Trigger Line 2

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.TTL_3



        PXI Trigger Line 3

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.TL_4



        PXI Trigger Line 4

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.TTL_5



        PXI Trigger Line 5

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.TTL_6



        PXI Trigger Line 6

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.TTL_7



        PXI Trigger Line 7

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.LBR_TRIG_0



        Local Bus Right Trigger Line 0 of PXI/SCXI combination chassis

        




.. py:data:: MeasurementDestinationSlope

    .. py:attribute:: nidmm.MeasurementDestinationSlope.POSITIVE



        The driver triggers on the rising edge of the trigger signal.

        



    .. py:attribute:: nidmm.MeasurementDestinationSlope.NEGATIVE



        The driver triggers on the falling edge of the trigger signal.

        




.. py:data:: OffsetCompensatedOhms

    .. py:attribute:: nidmm.OffsetCompensatedOhms.OFF



        Disables Offset Compensated Ohms.

        



    .. py:attribute:: nidmm.OffsetCompensatedOhms.ON



        Enables Offset Compensated Ohms.

        




.. py:data:: OperationMode

    .. py:attribute:: nidmm.OperationMode.IVIDMM_MODE



        Single or multipoint measurements: When the Trigger Count and Sample
        Count properties are both set to 1, the NI 4065, NI 4070/4071/4072, and
        NI 4080/4081/4082 take a single-point measurement; otherwise, NI-DMM
        takes multipoint measurements.

        



    .. py:attribute:: nidmm.OperationMode.WAVEFORM_MODE



        Configures the NI 4080/4081/4082 and NI 4070/4071/4072 to take waveform
        measurements.

        




.. py:data:: PowerlineFrequency

    .. py:attribute:: nidmm.PowerlineFrequency._50_HZ



        Specifies the powerline frequency as 50 Hz.

        



    .. py:attribute:: nidmm.PowerlineFrequency._60_HZ



        Specifies the powerline frequency as 60 Hz.

        




.. py:data:: RTDType

    .. py:attribute:: nidmm.RTDType.CUSTOM



        Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
        and C coefficients.

        



    .. py:attribute:: nidmm.RTDType.PT_3750



        Performs scaling for a Pt 3750 RTD.

        



    .. py:attribute:: nidmm.RTDType.PT_3851



        Performs scaling for a Pt 3851 RTD.

        



    .. py:attribute:: nidmm.RTDType.PT_3911



        Performs scaling for a Pt 3911 RTD.

        



    .. py:attribute:: nidmm.RTDType.PT_3916



        Performs scaling for a Pt 3916 RTD.

        



    .. py:attribute:: nidmm.RTDType.PT_3920



        Performs scaling for a Pt 3920 RTD.

        



    .. py:attribute:: nidmm.RTDType.PT_3928



        Performs scaling for a Pt 3928 RTD.

        




.. py:data:: SampleTrigSlope

    .. py:attribute:: nidmm.SampleTrigSlope.POSITIVE



        The driver triggers on the rising edge of the trigger signal.

        



    .. py:attribute:: nidmm.SampleTrigSlope.NEGATIVE



        The driver triggers on the falling edge of the trigger signal.

        




.. py:data:: SampleTrigger

    .. py:attribute:: nidmm.SampleTrigger.IMMEDIATE



        No trigger specified

        



    .. py:attribute:: nidmm.SampleTrigger.EXTERNAL



        Pin 9 on the AUX Connector

        



    .. py:attribute:: nidmm.SampleTrigger.SOFTWARE_TRIG



        Configures the DMM to wait until `niDMM Send Software
        Trigger <dmmviref.chm::/niDMM_Send_Software_Trigger.html>`__ is called.

        



    .. py:attribute:: nidmm.SampleTrigger.INTERVAL



        Interval trigger

        



    .. py:attribute:: nidmm.SampleTrigger.TTL_0



        PXI Trigger Line 0

        



    .. py:attribute:: nidmm.SampleTrigger.TTL_1



        PXI Trigger Line 1

        



    .. py:attribute:: nidmm.SampleTrigger.TTL_2



        PXI Trigger Line 2

        



    .. py:attribute:: nidmm.SampleTrigger.TTL_3



        PXI Trigger Line 3

        



    .. py:attribute:: nidmm.SampleTrigger.TTL_4



        PXI Trigger Line 4

        



    .. py:attribute:: nidmm.SampleTrigger.TTL_5



        PXI Trigger Line 5

        



    .. py:attribute:: nidmm.SampleTrigger.TTL_6



        PXI Trigger Line 6

        



    .. py:attribute:: nidmm.SampleTrigger.TTL_7



        PXI Trigger Line 7

        



    .. py:attribute:: nidmm.SampleTrigger.PXI_STAR



        PXI Star trigger line

        



    .. py:attribute:: nidmm.SampleTrigger.AUX_TRIG_1



        Pin 3 on the AUX connector

        



    .. py:attribute:: nidmm.SampleTrigger.LBR_TRIG_1



        Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis

        




.. py:data:: ThermistorType

    .. py:attribute:: nidmm.ThermistorType.CUSTOM



        Performs Steinhart-Hart thermistor scaling with the user-specified A, B,
        and C coefficients.

        



    .. py:attribute:: nidmm.ThermistorType._44004



        Performs scaling for an Omega Series 44004 thermistor.

        



    .. py:attribute:: nidmm.ThermistorType._44006



        Performs scaling for an Omega Series 44006 thermistor.

        



    .. py:attribute:: nidmm.ThermistorType._44007



        Performs scaling for an Omega Series 44007 thermistor.

        




.. py:data:: ThermocoupleReferenceJunctionType

    .. py:attribute:: nidmm.ThermocoupleReferenceJunctionType.FIXED



        Thermocouple reference juction is fixed at the user-specified
        temperature.

        




.. py:data:: ThermocoupleType

    .. py:attribute:: nidmm.ThermocoupleType.B



        Thermocouple type B

        



    .. py:attribute:: nidmm.ThermocoupleType.E



        Thermocouple type E

        



    .. py:attribute:: nidmm.ThermocoupleType.J



        Thermocouple type J

        



    .. py:attribute:: nidmm.ThermocoupleType.K



        Thermocouple type K

        



    .. py:attribute:: nidmm.ThermocoupleType.N



        Thermocouple type N

        



    .. py:attribute:: nidmm.ThermocoupleType.R



        Thermocouple type R

        



    .. py:attribute:: nidmm.ThermocoupleType.S



        Thermocouple type S

        



    .. py:attribute:: nidmm.ThermocoupleType.T



        Thermocouple type T

        




.. py:data:: TransducerType

    .. py:attribute:: nidmm.TransducerType.THERMOCOUPLE



        Use for thermocouple measurements.

        



    .. py:attribute:: nidmm.TransducerType.THERMISTOR



        Use for thermistor measurements.

        



    .. py:attribute:: nidmm.TransducerType._2_WIRE_RTD



        Use for 2-wire RTD measurements.

        



    .. py:attribute:: nidmm.TransducerType._4_WIRE_RTD



        Use for 4-wire RTD measurements.

        




.. py:data:: TriggerSlope

    .. py:attribute:: nidmm.TriggerSlope.POSITIVE



        The driver triggers on the rising edge of the trigger signal.

        



    .. py:attribute:: nidmm.TriggerSlope.NEGATIVE



        The driver triggers on the falling edge of the trigger signal.

        




.. py:data:: TriggerSource

    .. py:attribute:: nidmm.TriggerSource.IMMEDIATE



        No trigger specified.

        



    .. py:attribute:: nidmm.TriggerSource.EXTERNAL



        Pin 9 on the AUX Connector

        



    .. py:attribute:: nidmm.TriggerSource.SOFTWARE_TRIG



        Waits until `niDMM Send Software
        Trigger <dmmviref.chm::/niDMM_Send_Software_Trigger.html>`__ is called.

        



    .. py:attribute:: nidmm.TriggerSource.TTL_0



        PXI Trigger Line 0

        



    .. py:attribute:: nidmm.TriggerSource.TTL_1



        PXI Trigger Line 1

        



    .. py:attribute:: nidmm.TriggerSource.TTL_2



        PXI Trigger Line 2

        



    .. py:attribute:: nidmm.TriggerSource.TTL_3



        PXI Trigger Line 3

        



    .. py:attribute:: nidmm.TriggerSource.TTL_4



        PXI Trigger Line 4

        



    .. py:attribute:: nidmm.TriggerSource.TTL_5



        PXI Trigger Line 5

        



    .. py:attribute:: nidmm.TriggerSource.TTL_6



        PXI Trigger Line 6

        



    .. py:attribute:: nidmm.TriggerSource.TTL_7



        PXI Trigger Line 7

        



    .. py:attribute:: nidmm.TriggerSource.PXI_STAR



        PXI Star Trigger Line

        



    .. py:attribute:: nidmm.TriggerSource.AUX_TRIG_1



        Pin 3 on the AUX connector

        



    .. py:attribute:: nidmm.TriggerSource.LBR_TRIG_1



        Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis

        




.. py:data:: WaveformCoupling

    .. py:attribute:: nidmm.WaveformCoupling.AC



        Specifies AC coupling.

        



    .. py:attribute:: nidmm.WaveformCoupling.DC



        Specifies DC coupling.

        


