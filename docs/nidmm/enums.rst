Enums
=====

Enums used in NI-DMM

.. py:currentmodule:: nidmm



.. py:data:: ADCCalibration

    .. py:attribute:: nidmm.ADCCalibration.AUTO



        The DMM enables or disables ADC calibration for you.

        



    .. py:attribute:: nidmm.ADCCalibration.OFF



        The DMM does not compensate for changes to the gain.

        



    .. py:attribute:: nidmm.ADCCalibration.ON



        The DMM measures an internal reference to calculate the correct gain for the  measurement.

        




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



        Seconds

        



    .. py:attribute:: nidmm.ApertureTimeUnits.POWER_LINE_CYCLES



        Powerline Cycles

        




.. py:data:: AutoZero

    .. py:attribute:: nidmm.AutoZero.AUTO



        The drivers chooses the AutoZero setting based on the configured function  and resolution.

        



    .. py:attribute:: nidmm.AutoZero.OFF



        Disables AutoZero.

        



    .. py:attribute:: nidmm.AutoZero.ON



        The DMM internally disconnects the input signal following each measurement  and takes a zero reading. It then subtracts the zero reading from the  preceding reading.

        



    .. py:attribute:: nidmm.AutoZero.ONCE



        The DMM internally disconnects the input signal for the first measurement  and takes a zero reading. It then subtracts the zero reading from the first  reading and the following readings.

        




.. py:data:: CableCompensationType

    .. py:attribute:: nidmm.CableCompensationType.NONE



        No Cable Compensation

        



    .. py:attribute:: nidmm.CableCompensationType.OPEN



        Open Cable Compensation

        



    .. py:attribute:: nidmm.CableCompensationType.SHORT



        Short Cable Compensation

        



    .. py:attribute:: nidmm.CableCompensationType.OPEN_AND_SHORT



        Open and Short Cable Compensation

        




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

    .. py:attribute:: nidmm.DCBias.OFF



        NI-DMM programs the device not to use the DC bias

        



    .. py:attribute:: nidmm.DCBias.ON



        NI-DMM programs the device to use the DC bias

        




.. py:data:: DCNoiseRejection

    .. py:attribute:: nidmm.DCNoiseRejection.AUTO



        The driver chooses the DC noise rejection setting based on the configured  function and resolution.

        



    .. py:attribute:: nidmm.DCNoiseRejection.NORMAL



        NI-DMM weighs all samples equally.

        



    .. py:attribute:: nidmm.DCNoiseRejection.SECOND_ORDER



        NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  triangular weighing function.

        



    .. py:attribute:: nidmm.DCNoiseRejection.HIGH_ORDER



        NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  bell-curve weighing function.

        




.. py:data:: DigitsResolution

    .. py:attribute:: nidmm.DigitsResolution.THREEPOINTFIVE



    .. py:attribute:: nidmm.DigitsResolution.FOURPOINTFIVE



    .. py:attribute:: nidmm.DigitsResolution.FIVEPOINTFIVE



    .. py:attribute:: nidmm.DigitsResolution.SIXPOINTFIVE



    .. py:attribute:: nidmm.DigitsResolution.SEVENPOINTFIVE




.. py:data:: Function

    .. py:attribute:: nidmm.Function.DC_VOLTS



        DC Voltage

        



    .. py:attribute:: nidmm.Function.AC_VOLTS



        AC Voltage

        



    .. py:attribute:: nidmm.Function.DC_CURRENT



        DC Current

        



    .. py:attribute:: nidmm.Function.AC_CURRENT



        AC Current

        



    .. py:attribute:: nidmm.Function._2_WIRE_RES



        2-Wire Resistance

        



    .. py:attribute:: nidmm.Function._4_WIRE_RES



        4-Wire Resistance

        



    .. py:attribute:: nidmm.Function.FREQ



        Frequency

        



    .. py:attribute:: nidmm.Function.PERIOD



        Period

        



    .. py:attribute:: nidmm.Function.TEMPERATURE



        NI 4065, and NI 4070/4071/4072 supported.

        



    .. py:attribute:: nidmm.Function.AC_VOLTS_DC_COUPLED



        AC Voltage with DC Coupling

        



    .. py:attribute:: nidmm.Function.DIODE



        Diode

        



    .. py:attribute:: nidmm.Function.WAVEFORM_VOLTAGE



        Waveform voltage

        



    .. py:attribute:: nidmm.Function.WAVEFORM_CURRENT



        Waveform current

        



    .. py:attribute:: nidmm.Function.CAPACITANCE



        Capacitance

        



    .. py:attribute:: nidmm.Function.INDUCTANCE



        Inductance

        




.. py:data:: InputResistance

    .. py:attribute:: nidmm.InputResistance._1_MEGAOHM



        Input resistance of 1 M Ohm

        



    .. py:attribute:: nidmm.InputResistance._10_MEGAOHM



        Input resistance of 10 M Ohm

        



    .. py:attribute:: nidmm.InputResistance.GREATER_THAN_10_GIGAOHM



        Input resistance greater than 10 G Ohm

        




.. py:data:: LCCalculationModel

    .. py:attribute:: nidmm.LCCalculationModel.AUTO



        NI-DMM chooses the algorithm based on function and range

        



    .. py:attribute:: nidmm.LCCalculationModel.SERIES



        NI-DMM uses the series impedance model to calculate capacitance and inductance

        



    .. py:attribute:: nidmm.LCCalculationModel.PARALLEL



        NI-DMM uses the parallel admittance model to calculate capacitance and inductance

        




.. py:data:: MeasurementCompleteDest

    .. py:attribute:: nidmm.MeasurementCompleteDest.NONE



        No Trigger

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.EXTERNAL



        AUX I/O Connector

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.PXI_TRIG0



        PXI Trigger Line 0

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.PXI_TRIG1



        PXI Trigger Line 1

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.PXI_TRIG2



        PXI Trigger Line 2

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.PXI_TRIG3



        PXI Trigger Line 3

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.PXI_TRIG4



        PXI Trigger Line 4

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.PXI_TRIG5



        PXI Trigger Line 5

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.PXI_TRIG6



        PXI Trigger Line 6

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.PXI_TRIG7



        PXI Trigger Line 7

        



    .. py:attribute:: nidmm.MeasurementCompleteDest.LBR_TRIG0



        Internal Trigger Line of a PXI/SCXI Combination Chassis

        




.. py:data:: MeasurementDestinationSlope

    .. py:attribute:: nidmm.MeasurementDestinationSlope.POSITIVE



        Rising Edgs

        



    .. py:attribute:: nidmm.MeasurementDestinationSlope.NEGATIVE



        Falling Edge

        




.. py:data:: OffsetCompensatedOhms

    .. py:attribute:: nidmm.OffsetCompensatedOhms.OFF



        The DMM disables offset compensated ohms.

        



    .. py:attribute:: nidmm.OffsetCompensatedOhms.ON



        The DMM enables offset compensated ohms.

        




.. py:data:: OperationMode

    .. py:attribute:: nidmm.OperationMode.IVIDMM



        IviDmm Mode

        



    .. py:attribute:: nidmm.OperationMode.WAVEFORM



        Waveform acquisition mode

        




.. py:data:: PowerlineFrequency

    .. py:attribute:: nidmm.PowerlineFrequency._50



        Specifies the powerline frequency as 50 Hz.

        



    .. py:attribute:: nidmm.PowerlineFrequency._60



        Specifies the powerline frequency as 60 Hz.

        




.. py:data:: RTDType

    .. py:attribute:: nidmm.RTDType.CUSTOM



        Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
        and C coefficients.

        



    .. py:attribute:: nidmm.RTDType.PT3750



        Performs scaling for a Pt 3750 RTD.

        



    .. py:attribute:: nidmm.RTDType.PT3851



        Performs scaling for a Pt 3851 RTD.

        



    .. py:attribute:: nidmm.RTDType.PT3911



        Performs scaling for a Pt 3911 RTD.

        



    .. py:attribute:: nidmm.RTDType.PT3916



        Performs scaling for a Pt 3916 RTD.

        



    .. py:attribute:: nidmm.RTDType.PT3920



        Performs scaling for a Pt 3920 RTD.

        



    .. py:attribute:: nidmm.RTDType.PT3928



        Performs scaling for a Pt 3928 RTD.

        




.. py:data:: SampleTrigSlope

    .. py:attribute:: nidmm.SampleTrigSlope.POSITIVE



        Rising Edgs

        



    .. py:attribute:: nidmm.SampleTrigSlope.NEGATIVE



        Falling Edge

        




.. py:data:: SampleTrigger

    .. py:attribute:: nidmm.SampleTrigger.IMMEDIATE



        No Trigger

        



    .. py:attribute:: nidmm.SampleTrigger.EXTERNAL



        AUX I/O Connector Trigger Line 0

        



    .. py:attribute:: nidmm.SampleTrigger.SOFTWARE_TRIG



        Software Trigger

        



    .. py:attribute:: nidmm.SampleTrigger.INTERVAL



        Interval Trigger

        



    .. py:attribute:: nidmm.SampleTrigger.PXI_TRIG0



        PXI Trigger Line 0

        



    .. py:attribute:: nidmm.SampleTrigger.PXI_TRIG1



        PXI Trigger Line 1

        



    .. py:attribute:: nidmm.SampleTrigger.PXI_TRIG2



        PXI Trigger Line 2

        



    .. py:attribute:: nidmm.SampleTrigger.PXI_TRIG3



        PXI Trigger Line 3

        



    .. py:attribute:: nidmm.SampleTrigger.PXI_TRIG4



        PXI Trigger Line 4

        



    .. py:attribute:: nidmm.SampleTrigger.PXI_TRIG5



        PXI Trigger Line 5

        



    .. py:attribute:: nidmm.SampleTrigger.PXI_TRIG6



        PXI Trigger Line 6

        



    .. py:attribute:: nidmm.SampleTrigger.PXI_TRIG7



        PXI Trigger Line 7

        



    .. py:attribute:: nidmm.SampleTrigger.PXI_STAR



        PXI Star Trigger Line

        



    .. py:attribute:: nidmm.SampleTrigger.AUX_TRIG1



        AUX I/0 Connector Trigger Line 1

        



    .. py:attribute:: nidmm.SampleTrigger.LBR_TRIG1



        Internal Trigger Line of a PXI/SCXI Combination Chassis

        




.. py:data:: ThermistorType

    .. py:attribute:: nidmm.ThermistorType.CUSTOM



        Custom

        



    .. py:attribute:: nidmm.ThermistorType._44004



        44004

        



    .. py:attribute:: nidmm.ThermistorType._44006



        44006

        



    .. py:attribute:: nidmm.ThermistorType._44007



        44007

        




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



        Thermocouple

        



    .. py:attribute:: nidmm.TransducerType.THERMISTOR



        Thermistor

        



    .. py:attribute:: nidmm.TransducerType._2_WIRE_RTD



        2-wire RTD

        



    .. py:attribute:: nidmm.TransducerType._4_WIRE_RTD



        4-wire RTD

        




.. py:data:: TriggerSlope

    .. py:attribute:: nidmm.TriggerSlope.POSITIVE



        Rising Edgs

        



    .. py:attribute:: nidmm.TriggerSlope.NEGATIVE



        Falling Edge

        




.. py:data:: TriggerSource

    .. py:attribute:: nidmm.TriggerSource.IMMEDIATE



        No Trigger

        



    .. py:attribute:: nidmm.TriggerSource.EXTERNAL



        AUX I/O Connector Trigger Line 0

        



    .. py:attribute:: nidmm.TriggerSource.SOFTWARE_TRIG



        Software Trigger

        



    .. py:attribute:: nidmm.TriggerSource.PXI_TRIG0



        PXI Trigger Line 0

        



    .. py:attribute:: nidmm.TriggerSource.PXI_TRIG1



        PXI Trigger Line 1

        



    .. py:attribute:: nidmm.TriggerSource.PXI_TRIG2



        PXI Trigger Line 2

        



    .. py:attribute:: nidmm.TriggerSource.PXI_TRIG3



        PXI Trigger Line 3

        



    .. py:attribute:: nidmm.TriggerSource.PXI_TRIG4



        PXI Trigger Line 4

        



    .. py:attribute:: nidmm.TriggerSource.PXI_TRIG5



        PXI Trigger Line 5

        



    .. py:attribute:: nidmm.TriggerSource.PXI_TRIG6



        PXI Trigger Line 6

        



    .. py:attribute:: nidmm.TriggerSource.PXI_TRIG7



        PXI Trigger Line 7

        



    .. py:attribute:: nidmm.TriggerSource.PXI_STAR



        PXI Star Trigger Line

        



    .. py:attribute:: nidmm.TriggerSource.AUX_TRIG1



        AUX I/O Connector Trigger Line 1

        



    .. py:attribute:: nidmm.TriggerSource.LBR_TRIG1



        Internal Trigger Line of a PXI/SCXI Combination Chassis

        




.. py:data:: WaveformCoupling

    .. py:attribute:: nidmm.WaveformCoupling.AC



        AC Coupled

        



    .. py:attribute:: nidmm.WaveformCoupling.DC



        DC Coupled

        


