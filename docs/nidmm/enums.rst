NI-DMM Enums
============

Enums used in NI-DMM

Enums
-----



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


   .. py:attribute:: FINISHED_WITH_BACKLOG


   .. py:attribute:: FINISHED_WITH_NO_BACKLOG


   .. py:attribute:: PAUSED


   .. py:attribute:: NO_ACQUISITION_IN_PROGRESS



.. py:data:: ApertureTimeUnits

   .. py:attribute:: SECONDS

      Units are seconds.

   .. py:attribute:: POWER_LINE_CYCLES

      Units are powerline cycles (PLCs).

   .. py:attribute:: RAW_SAMPLES



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

   .. py:attribute:: CABLE_COMP_NONE

      No cable compensation.

   .. py:attribute:: CABLE_COMP_OPEN

      Open cable compensation.

   .. py:attribute:: CABLE_COMP_SHORT

      Short cable compensation.

   .. py:attribute:: CABLE_COMP_OPEN_AND_SHORT

      Open and short cable compensation.


.. py:data:: CurrentSource

   .. py:attribute:: ONE_MICRO_AMP

      NI 4070/4071/4072 are supported.

   .. py:attribute:: TEN_MICRO_AMP

      NI 4080/4081/4082 and NI 4070/4071/4072 are supported.

   .. py:attribute:: HUNDRED_MICRO_AMP

      NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.

   .. py:attribute:: ONE_MILLI_AMP

      NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 are supported.


.. py:data:: DCNoiseRejectionMode

   .. py:attribute:: DCNR_AUTO

      The driver chooses the DC noise rejection setting based on the
      configured function and resolution.

   .. py:attribute:: DCNR_NORMAL

      NI-DMM weighs all samples equally.

   .. py:attribute:: DCNR_SECOND_ORDERT

      NI-DMM weighs the samples taken in the middle of the aperture time more
      than samples taken at the beginning and the end of the measurement using
      a triangular weighing function.

   .. py:attribute:: DCNR_HIGH_ORDER

      NI-DMM weighs the samples taken in the middle of the aperture time more
      than samples taken at the beginning and the end of the measurement using
      a bell-curve weighing function.


.. py:data:: Function

   .. py:attribute:: DC_VOLTS

      All devices supported.

   .. py:attribute:: AC_VOLTS

      All devices supported.

   .. py:attribute:: DC_CURRENT

      All devices supported.

   .. py:attribute:: AC_CURRENT

      All devices supported.

   .. py:attribute:: RES_2_WIRE

      All devices supported.

   .. py:attribute:: RES_4_WIRE

      NI 4065, and NI 4070/4071/4072 supported.

   .. py:attribute:: FREQ

      NI 4070/4071/4072 supported.

   .. py:attribute:: PERIOD

      NI 4070/4071/4072 supported.

   .. py:attribute:: TEMPERATURE

      NI 4065, and NI 4070/4071/4072 supported.

   .. py:attribute:: AC_VOLTS_DC_COUPLED

      NI 4070/4071/4072 supported.

   .. py:attribute:: DIODE

      All devices supported.

   .. py:attribute:: WAVEFORM_VOLTAGE

      NI 4070/4071/4072 supported.

   .. py:attribute:: WAVEFORM_CURRENT

      NI 4070/4071/4072 supported.

   .. py:attribute:: CAPACITANCE

      NI 4072 supported.

   .. py:attribute:: INDUCTANCE

      NI 4072 supported.


.. py:data:: LCCalculationModel

   .. py:attribute:: CALC_MODEL_AUTO

      NI-DMM chooses the algorithm based on function and range.

   .. py:attribute:: CALC_MODEL_SERIES

      NI-DMM uses the series impedance model to calculate capacitance and
      inductance.

   .. py:attribute:: CALC_MODEL_PARALLEL

      NI-DMM uses the parallel admittance model to calculate capacitance and
      inductance.


.. py:data:: MeasurementCompleteDest

   .. py:attribute:: NONE

      No destination specified.

   .. py:attribute:: EXTERNAL

      Pin 6 on the AUX Connector

   .. py:attribute:: SOFTWARE_TRIG


   .. py:attribute:: PXI_TRIG0

      PXI Trigger Line 0

   .. py:attribute:: PXI_TRIG1

      PXI Trigger Line 1

   .. py:attribute:: PXI_TRIG2

      PXI Trigger Line 2

   .. py:attribute:: PXI_TRIG3

      PXI Trigger Line 3

   .. py:attribute:: PXI_TRIG4

      PXI Trigger Line 4

   .. py:attribute:: PXI_TRIG5

      PXI Trigger Line 5

   .. py:attribute:: PXI_TRIG6

      PXI Trigger Line 6

   .. py:attribute:: PXI_TRIG7

      PXI Trigger Line 7

   .. py:attribute:: LBR_TRIG0

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

   .. py:attribute:: DMM_MODE

      Single or multipoint measurements: When the Trigger Count and Sample
      Count properties are both set to 1, the NI 4065, NI 4070/4071/4072, and
      NI 4080/4081/4082 take a single-point measurement; otherwise, NI-DMM
      takes multipoint measurements.

   .. py:attribute:: WAVEFORM_MODE

      Configures the NI 4080/4081/4082 and NI 4070/4071/4072 to take waveform
      measurements.


.. py:data:: SampleTrigSlope

   .. py:attribute:: POSITIVE

      The driver triggers on the rising edge of the trigger signal.

   .. py:attribute:: NEGATIVE

      The driver triggers on the falling edge of the trigger signal.


.. py:data:: SampleTrigger

   .. py:attribute:: NONE


   .. py:attribute:: IMMEDIATE

      No trigger specified

   .. py:attribute:: EXTERNAL

      Pin 9 on the AUX Connector

   .. py:attribute:: SOFTWARE_TRIG

      Configures the DMM to wait until niDMM Send Software Trigger is called.

   .. py:attribute:: INTERVAL

      Interval trigger

   .. py:attribute:: AUX_TRIG1

      Pin 3 on the AUX connector

   .. py:attribute:: LBR_TRIG1

      Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis

   .. py:attribute:: PXI_TRIG0

      PXI Trigger Line 0

   .. py:attribute:: PXI_TRIG1

      PXI Trigger Line 1

   .. py:attribute:: PXI_TRIG2

      PXI Trigger Line 2

   .. py:attribute:: PXI_TRIG3

      PXI Trigger Line 3

   .. py:attribute:: PXI_TRIG4

      PXI Trigger Line 4

   .. py:attribute:: PXI_TRIG5

      PXI Trigger Line 5

   .. py:attribute:: PXI_TRIG6

      PXI Trigger Line 6

   .. py:attribute:: PXI_TRIG7

      PXI Trigger Line 7

   .. py:attribute:: PXI_STAR

      PXI Star trigger line


.. py:data:: TemperatureRTDType

   .. py:attribute:: CustomRTD

      Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
      and C coefficients.

   .. py:attribute:: PT3750

      Performs scaling for a Pt 3750 RTD.

   .. py:attribute:: PT3851

      Performs scaling for a Pt 3851 RTD.

   .. py:attribute:: PT3911

      Performs scaling for a Pt 3911 RTD.

   .. py:attribute:: PT3916

      Performs scaling for a Pt 3916 RTD.

   .. py:attribute:: PT3920

      Performs scaling for a Pt 3920 RTD.

   .. py:attribute:: PT3928

      Performs scaling for a Pt 3928 RTD.


.. py:data:: TemperatureThermistorType

   .. py:attribute:: THERMISTOR_CUSTOM

      Performs Steinhart-Hart thermistor scaling with the user-specified A, B,
      and C coefficients.

   .. py:attribute:: THERMISTOR_44004

      Performs scaling for an Omega Series 44004 thermistor.

   .. py:attribute:: THERMISTOR_44006

      Performs scaling for an Omega Series 44006 thermistor.

   .. py:attribute:: THERMISTOR_44007

      Performs scaling for an Omega Series 44007 thermistor.


.. py:data:: TemperatureThermocoupleReferenceJunctionType

   .. py:attribute:: Fixed

      Thermocouple reference juction is fixed at the user-specified
      temperature.


.. py:data:: TemperatureThermocoupleType

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


.. py:data:: TemperatureTransducerType

   .. py:attribute:: THERMOCOUPLE

      Use for thermocouple measurements.

   .. py:attribute:: THERMISTOR

      Use for thermistor measurements.

   .. py:attribute:: TWO_WIRE_RTD

      Use for 2-wire RTD measurements.

   .. py:attribute:: FOUR_WIRE_RTD

      Use for 4-wire RTD measurements.


.. py:data:: TriggerSlope

   .. py:attribute:: POSITIVE

      The driver triggers on the rising edge of the trigger signal.

   .. py:attribute:: NEGATIVE

      The driver triggers on the falling edge of the trigger signal.


.. py:data:: TriggerSource

   .. py:attribute:: NONE


   .. py:attribute:: IMMEDIATE

      No trigger specified.

   .. py:attribute:: EXTERNAL

      Pin 9 on the AUX Connector

   .. py:attribute:: SOFTWARE_TRIG

      Waits until niDMM Send Software Trigger is called.

   .. py:attribute:: PXI_TRIG0

      PXI Trigger Line 0

   .. py:attribute:: PXI_TRIG1

      PXI Trigger Line 1

   .. py:attribute:: PXI_TRIG2

      PXI Trigger Line 2

   .. py:attribute:: PXI_TRIG3

      PXI Trigger Line 3

   .. py:attribute:: PXI_TRIG4

      PXI Trigger Line 4

   .. py:attribute:: PXI_TRIG5

      PXI Trigger Line 5

   .. py:attribute:: PXI_TRIG6

      PXI Trigger Line 6

   .. py:attribute:: PXI_TRIG7

      PXI Trigger Line 7

   .. py:attribute:: PXI_STAR

      PXI Star Trigger Line

   .. py:attribute:: AUX_TRIG1

      Pin 3 on the AUX connector

   .. py:attribute:: LBR_TRIG1

      Local Bus Right Trigger Line 1 of PXI/SCXI combination chassis


.. py:data:: WaveformCouplingMode

   .. py:attribute:: WAVEFORM_COUPLING_AC

      Specifies AC coupling.

   .. py:attribute:: WAVEFORM_COUPLING_DC

      Specifies DC coupling.
