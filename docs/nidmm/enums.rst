Enums
=====

Enums used in NI-DMM

.. py:currentmodule:: nidmm


ADCCalibration
--------------

.. py:class:: ADCCalibration

    .. py:attribute:: ADCCalibration.AUTO



        The DMM enables or disables ADC calibration for you.

        



    .. py:attribute:: ADCCalibration.OFF



        The DMM does not compensate for changes to the gain.

        



    .. py:attribute:: ADCCalibration.ON



        The DMM measures an internal reference to calculate the correct gain for the  measurement.

        



AcquisitionStatus
-----------------

.. py:class:: AcquisitionStatus

    .. py:attribute:: AcquisitionStatus.RUNNING



        Running

        



    .. py:attribute:: AcquisitionStatus.FINISHED_WITH_BACKLOG



        Finished with **Backlog**

        



    .. py:attribute:: AcquisitionStatus.FINISHED_WITH_NO_BACKLOG



        Finished with no **Backlog**

        



    .. py:attribute:: AcquisitionStatus.PAUSED



        Paused

        



    .. py:attribute:: AcquisitionStatus.NO_ACQUISITION_IN_PROGRESS



        No acquisition in progress

        



ApertureTimeUnits
-----------------

.. py:class:: ApertureTimeUnits

    .. py:attribute:: ApertureTimeUnits.SECONDS



        Seconds

        



    .. py:attribute:: ApertureTimeUnits.POWER_LINE_CYCLES



        Powerline Cycles

        



AutoZero
--------

.. py:class:: AutoZero

    .. py:attribute:: AutoZero.AUTO



        The drivers chooses the AutoZero setting based on the configured method  and resolution.

        



    .. py:attribute:: AutoZero.OFF



        Disables AutoZero.

        



    .. py:attribute:: AutoZero.ON



        The DMM internally disconnects the input signal following each measurement  and takes a zero reading. It then subtracts the zero reading from the  preceding reading.

        



    .. py:attribute:: AutoZero.ONCE



        The DMM internally disconnects the input signal for the first measurement  and takes a zero reading. It then subtracts the zero reading from the first  reading and the following readings.

        



CableCompensationType
---------------------

.. py:class:: CableCompensationType

    .. py:attribute:: CableCompensationType.NONE



        No Cable Compensation

        



    .. py:attribute:: CableCompensationType.OPEN



        Open Cable Compensation

        



    .. py:attribute:: CableCompensationType.SHORT



        Short Cable Compensation

        



    .. py:attribute:: CableCompensationType.OPEN_AND_SHORT



        Open and Short Cable Compensation

        



DCNoiseRejection
----------------

.. py:class:: DCNoiseRejection

    .. py:attribute:: DCNoiseRejection.AUTO



        The driver chooses the DC noise rejection setting based on the configured  method and resolution.

        



    .. py:attribute:: DCNoiseRejection.NORMAL



        NI-DMM weighs all samples equally.

        



    .. py:attribute:: DCNoiseRejection.SECOND_ORDER



        NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  triangular weighing method.

        



    .. py:attribute:: DCNoiseRejection.HIGH_ORDER



        NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  bell-curve weighing method.

        



DigitsResolution
----------------

.. py:class:: DigitsResolution

    .. py:attribute:: DigitsResolution._3



        Specifies 3.5 digits resolution.

        



    .. py:attribute:: DigitsResolution._4



        Specifies 4.5 digits resolution.

        



    .. py:attribute:: DigitsResolution._5



        Specifies 5.5 digits resolution.

        



    .. py:attribute:: DigitsResolution._6



        Specifies 6.5 digits resolution.

        



    .. py:attribute:: DigitsResolution._7



        Specifies 7.5 digits resolution.

        



Function
--------

.. py:class:: Function

    .. py:attribute:: Function.DC_VOLTS



        DC Voltage

        



    .. py:attribute:: Function.AC_VOLTS



        AC Voltage

        



    .. py:attribute:: Function.DC_CURRENT



        DC Current

        



    .. py:attribute:: Function.AC_CURRENT



        AC Current

        



    .. py:attribute:: Function.TWO_WIRE_RES



        2-Wire Resistance

        



    .. py:attribute:: Function.FOUR_WIRE_RES



        4-Wire Resistance

        



    .. py:attribute:: Function.FREQ



        Frequency

        



    .. py:attribute:: Function.PERIOD



        Period

        



    .. py:attribute:: Function.TEMPERATURE



        NI 4065, NI 4070/4071/4072, and NI 4080/4081/4182 supported.

        



    .. py:attribute:: Function.AC_VOLTS_DC_COUPLED



        AC Voltage with DC Coupling

        



    .. py:attribute:: Function.DIODE



        Diode

        



    .. py:attribute:: Function.WAVEFORM_VOLTAGE



        Waveform voltage

        



    .. py:attribute:: Function.WAVEFORM_CURRENT



        Waveform current

        



    .. py:attribute:: Function.CAPACITANCE



        Capacitance

        



    .. py:attribute:: Function.INDUCTANCE



        Inductance

        



LCCalculationModel
------------------

.. py:class:: LCCalculationModel

    .. py:attribute:: LCCalculationModel.AUTO



        NI-DMM chooses the algorithm based on method and range

        



    .. py:attribute:: LCCalculationModel.SERIES



        NI-DMM uses the series impedance model to calculate capacitance and inductance

        



    .. py:attribute:: LCCalculationModel.PARALLEL



        NI-DMM uses the parallel admittance model to calculate capacitance and inductance

        



MeasurementCompleteDest
-----------------------

.. py:class:: MeasurementCompleteDest

    .. py:attribute:: MeasurementCompleteDest.NONE



        No Trigger

        



    .. py:attribute:: MeasurementCompleteDest.EXTERNAL



        AUX I/O Connector

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG0



        PXI Trigger Line 0

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG1



        PXI Trigger Line 1

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG2



        PXI Trigger Line 2

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG3



        PXI Trigger Line 3

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG4



        PXI Trigger Line 4

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG5



        PXI Trigger Line 5

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG6



        PXI Trigger Line 6

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG7



        PXI Trigger Line 7

        



    .. py:attribute:: MeasurementCompleteDest.LBR_TRIG0



        Internal Trigger Line of a PXI/SCXI Combination Chassis

        



OperationMode
-------------

.. py:class:: OperationMode

    .. py:attribute:: OperationMode.IVIDMM



        IviDmm Mode

        



    .. py:attribute:: OperationMode.WAVEFORM



        Waveform acquisition mode

        



RTDType
-------

.. py:class:: RTDType

    .. py:attribute:: RTDType.CUSTOM



        Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
        and C coefficients.

        



    .. py:attribute:: RTDType.PT3750



        Performs scaling for a Pt 3750 RTD.

        



    .. py:attribute:: RTDType.PT3851



        Performs scaling for a Pt 3851 RTD.

        



    .. py:attribute:: RTDType.PT3911



        Performs scaling for a Pt 3911 RTD.

        



    .. py:attribute:: RTDType.PT3916



        Performs scaling for a Pt 3916 RTD.

        



    .. py:attribute:: RTDType.PT3920



        Performs scaling for a Pt 3920 RTD.

        



    .. py:attribute:: RTDType.PT3928



        Performs scaling for a Pt 3928 RTD.

        



SampleTrigger
-------------

.. py:class:: SampleTrigger

    .. py:attribute:: SampleTrigger.IMMEDIATE



        No Trigger

        



    .. py:attribute:: SampleTrigger.EXTERNAL



        AUX I/O Connector Trigger Line 0

        



    .. py:attribute:: SampleTrigger.SOFTWARE_TRIG



        Software Trigger

        



    .. py:attribute:: SampleTrigger.INTERVAL



        Interval Trigger

        



    .. py:attribute:: SampleTrigger.PXI_TRIG0



        PXI Trigger Line 0

        



    .. py:attribute:: SampleTrigger.PXI_TRIG1



        PXI Trigger Line 1

        



    .. py:attribute:: SampleTrigger.PXI_TRIG2



        PXI Trigger Line 2

        



    .. py:attribute:: SampleTrigger.PXI_TRIG3



        PXI Trigger Line 3

        



    .. py:attribute:: SampleTrigger.PXI_TRIG4



        PXI Trigger Line 4

        



    .. py:attribute:: SampleTrigger.PXI_TRIG5



        PXI Trigger Line 5

        



    .. py:attribute:: SampleTrigger.PXI_TRIG6



        PXI Trigger Line 6

        



    .. py:attribute:: SampleTrigger.PXI_TRIG7



        PXI Trigger Line 7

        



    .. py:attribute:: SampleTrigger.PXI_STAR



        PXI Star Trigger Line

        



    .. py:attribute:: SampleTrigger.AUX_TRIG1



        AUX I/0 Connector Trigger Line 1

        



    .. py:attribute:: SampleTrigger.LBR_TRIG1



        Internal Trigger Line of a PXI/SCXI Combination Chassis

        



ThermistorType
--------------

.. py:class:: ThermistorType

    .. py:attribute:: ThermistorType.CUSTOM



        Custom

        



    .. py:attribute:: ThermistorType.THERMISTOR_44004



        44004

        



    .. py:attribute:: ThermistorType.THERMISTOR_44006



        44006

        



    .. py:attribute:: ThermistorType.THERMISTOR_44007



        44007

        



ThermocoupleReferenceJunctionType
---------------------------------

.. py:class:: ThermocoupleReferenceJunctionType

    .. py:attribute:: ThermocoupleReferenceJunctionType.FIXED



        Thermocouple reference juction is fixed at the user-specified
        temperature.

        



ThermocoupleType
----------------

.. py:class:: ThermocoupleType

    .. py:attribute:: ThermocoupleType.B



        Thermocouple type B

        



    .. py:attribute:: ThermocoupleType.E



        Thermocouple type E

        



    .. py:attribute:: ThermocoupleType.J



        Thermocouple type J

        



    .. py:attribute:: ThermocoupleType.K



        Thermocouple type K

        



    .. py:attribute:: ThermocoupleType.N



        Thermocouple type N

        



    .. py:attribute:: ThermocoupleType.R



        Thermocouple type R

        



    .. py:attribute:: ThermocoupleType.S



        Thermocouple type S

        



    .. py:attribute:: ThermocoupleType.T



        Thermocouple type T

        



TransducerType
--------------

.. py:class:: TransducerType

    .. py:attribute:: TransducerType.THERMOCOUPLE



        Thermocouple

        



    .. py:attribute:: TransducerType.THERMISTOR



        Thermistor

        



    .. py:attribute:: TransducerType.TWO_WIRE_RTD



        2-wire RTD

        



    .. py:attribute:: TransducerType.FOUR_WIRE_RTD



        4-wire RTD

        



TriggerSource
-------------

.. py:class:: TriggerSource

    .. py:attribute:: TriggerSource.IMMEDIATE



        No Trigger

        



    .. py:attribute:: TriggerSource.EXTERNAL



        AUX I/O Connector Trigger Line 0

        



    .. py:attribute:: TriggerSource.SOFTWARE_TRIG



        Software Trigger

        



    .. py:attribute:: TriggerSource.PXI_TRIG0



        PXI Trigger Line 0

        



    .. py:attribute:: TriggerSource.PXI_TRIG1



        PXI Trigger Line 1

        



    .. py:attribute:: TriggerSource.PXI_TRIG2



        PXI Trigger Line 2

        



    .. py:attribute:: TriggerSource.PXI_TRIG3



        PXI Trigger Line 3

        



    .. py:attribute:: TriggerSource.PXI_TRIG4



        PXI Trigger Line 4

        



    .. py:attribute:: TriggerSource.PXI_TRIG5



        PXI Trigger Line 5

        



    .. py:attribute:: TriggerSource.PXI_TRIG6



        PXI Trigger Line 6

        



    .. py:attribute:: TriggerSource.PXI_TRIG7



        PXI Trigger Line 7

        



    .. py:attribute:: TriggerSource.PXI_STAR



        PXI Star Trigger Line

        



    .. py:attribute:: TriggerSource.AUX_TRIG1



        AUX I/O Connector Trigger Line 1

        



    .. py:attribute:: TriggerSource.LBR_TRIG1



        Internal Trigger Line of a PXI/SCXI Combination Chassis

        



WaveformCoupling
----------------

.. py:class:: WaveformCoupling

    .. py:attribute:: WaveformCoupling.AC



        AC Coupled

        



    .. py:attribute:: WaveformCoupling.DC



        DC Coupled

        





