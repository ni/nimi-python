Enums
=====

Enums used in NI-DCPower

.. py:currentmodule:: nidcpower


ApertureTimeUnits
-----------------

.. py:class:: ApertureTimeUnits

    .. py:attribute:: ApertureTimeUnits.SECONDS



        Specifies aperture time in seconds.

        



    .. py:attribute:: ApertureTimeUnits.POWER_LINE_CYCLES



        Specifies aperture time in power line cycles (PLCs).

        



AutoZero
--------

.. py:class:: AutoZero

    .. py:attribute:: AutoZero.OFF



        Disables auto zero.

        



    .. py:attribute:: AutoZero.ON



        Makes zero conversions for every measurement.

        



    .. py:attribute:: AutoZero.ONCE



        Makes zero conversions following the first measurement after initiating the device.  The device uses these zero conversions for the preceding measurement and future  measurements until the device is reinitiated.

        



AutorangeApertureTimeMode
-------------------------

.. py:class:: AutorangeApertureTimeMode

    .. py:attribute:: AutorangeApertureTimeMode.AUTO



        NI-DCPower optimizes the aperture time for the autorange algorithm based on the module range.

        



    .. py:attribute:: AutorangeApertureTimeMode.CUSTOM



        The user specifies a minimum aperture time for the algorithm using the :py:attr:`nidcpower.Session.autorange_minimum_aperture_time` property and the corresponding :py:attr:`nidcpower.Session.autorange_minimum_aperture_time_units` property.

        



AutorangeBehavior
-----------------

.. py:class:: AutorangeBehavior

    .. py:attribute:: AutorangeBehavior.UP_TO_LIMIT_THEN_DOWN



        Go to limit range then range down as needed until measured value is within thresholds.

        



    .. py:attribute:: AutorangeBehavior.UP



        go up one range when the upper threshold is reached.

        



    .. py:attribute:: AutorangeBehavior.UP_AND_DOWN



        go up or down one range when the upper/lower threshold is reached.

        



AutorangeThresholdMode
----------------------

.. py:class:: AutorangeThresholdMode

    .. py:attribute:: AutorangeThresholdMode.NORMAL



        Thresholds are selected based on a balance between accuracy and hysteresis.

        



    .. py:attribute:: AutorangeThresholdMode.FAST_STEP



        Optimized for faster changes in the measured signal. Thresholds are configured to be a smaller percentage of the range.

        



    .. py:attribute:: AutorangeThresholdMode.HIGH_HYSTERESIS



        Optimized for noisy signals to minimize frequent and unpredictable range changes. Thresholds are configured to be a larger percentage of the range.

        



    .. py:attribute:: AutorangeThresholdMode.MEDIUM_HYSTERESIS



        Optimized for noisy signals to minimize frequent and unpredictable range changes. Thresholds are configured to be a medium percentage of the range.

        



    .. py:attribute:: AutorangeThresholdMode.HOLD



        Attempt to maintain the active range. Thresholds will favor the active range.

        



ComplianceLimitSymmetry
-----------------------

.. py:class:: ComplianceLimitSymmetry

    .. py:attribute:: ComplianceLimitSymmetry.SYMMETRIC



        Compliance limits are specified symmetrically about 0.

        



    .. py:attribute:: ComplianceLimitSymmetry.ASYMMETRIC



        Compliance limits can be specified asymmetrically with respect to 0.

        



DCNoiseRejection
----------------

.. py:class:: DCNoiseRejection

    .. py:attribute:: DCNoiseRejection.SECOND_ORDER



        Second-order rejection of DC noise.

        



    .. py:attribute:: DCNoiseRejection.NORMAL



        Normal rejection of DC noise.

        



Event
-----

.. py:class:: Event

    .. py:attribute:: Event.SOURCE_COMPLETE



    .. py:attribute:: Event.MEASURE_COMPLETE



    .. py:attribute:: Event.SEQUENCE_ITERATION_COMPLETE



    .. py:attribute:: Event.SEQUENCE_ENGINE_DONE



    .. py:attribute:: Event.PULSE_COMPLETE



    .. py:attribute:: Event.READY_FOR_PULSE_TRIGGER



MeasureWhen
-----------

.. py:class:: MeasureWhen

    .. py:attribute:: MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE



        Acquires a measurement after each Source Complete event completes.

        



    .. py:attribute:: MeasureWhen.ON_DEMAND



        Acquires a measurement when the :py:meth:`nidcpower.Session.measure` method or :py:meth:`nidcpower.Session.measure_multiple` method is called.

        



    .. py:attribute:: MeasureWhen.ON_MEASURE_TRIGGER



        Acquires a measurement when a Measure trigger is received.

        



MeasurementTypes
----------------

.. py:class:: MeasurementTypes

    .. py:attribute:: MeasurementTypes.CURRENT



        The device measures current.

        



    .. py:attribute:: MeasurementTypes.VOLTAGE



        The device measures voltage.

        



OutputCapacitance
-----------------

.. py:class:: OutputCapacitance

    .. py:attribute:: OutputCapacitance.LOW



        Output Capacitance is low.

        



    .. py:attribute:: OutputCapacitance.HIGH



        Output Capacitance is high.

        



OutputCutoffReason
------------------

.. py:class:: OutputCutoffReason

    .. py:attribute:: OutputCutoffReason.ALL



        Queries any output cutoff condition; clears all output cutoff conditions.

        



    .. py:attribute:: OutputCutoffReason.VOLTAGE_OUTPUT_HIGH



        Queries or clears cutoff conditions when the output exceeded the high cutoff limit for voltage output.

        



    .. py:attribute:: OutputCutoffReason.VOLTAGE_OUTPUT_LOW



        Queries or clears cutoff conditions when the output fell below the low cutoff limit for voltage output.

        



    .. py:attribute:: OutputCutoffReason.CURRENT_MEASURE_HIGH



        Queries or clears cutoff conditions when the measured current exceeded the high cutoff limit for current output.

        



    .. py:attribute:: OutputCutoffReason.CURRENT_MEASURE_LOW



        Queries or clears cutoff conditions when the measured current fell below the low cutoff limit for current output.

        



    .. py:attribute:: OutputCutoffReason.VOLTAGE_CHANGE_HIGH



        Queries or clears cutoff conditions when the voltage slew rate increased beyond the positive change cutoff for voltage output.

        



    .. py:attribute:: OutputCutoffReason.VOLTAGE_CHANGE_LOW



        Queries or clears cutoff conditions when the voltage slew rate decreased beyond the negative change cutoff for voltage output.

        



    .. py:attribute:: OutputCutoffReason.CURRENT_CHANGE_HIGH



        Queries or clears cutoff conditions when the current slew rate increased beyond the positive change cutoff for current output.

        



    .. py:attribute:: OutputCutoffReason.CURRENT_CHANGE_LOW



        Queries or clears cutoff conditions when the current slew rate decreased beyond the negative change cutoff for current output.

        



OutputFunction
--------------

.. py:class:: OutputFunction

    .. py:attribute:: OutputFunction.DC_VOLTAGE



        Sets the output method to DC voltage.

        



    .. py:attribute:: OutputFunction.DC_CURRENT



        Sets the output method to DC current.

        



    .. py:attribute:: OutputFunction.PULSE_VOLTAGE



        Sets the output method to pulse voltage.

        



    .. py:attribute:: OutputFunction.PULSE_CURRENT



        Sets the output method to pulse current.

        



OutputStates
------------

.. py:class:: OutputStates

    .. py:attribute:: OutputStates.VOLTAGE



        The device maintains a constant voltage by adjusting the current

        



    .. py:attribute:: OutputStates.CURRENT



        The device maintains a constant current by adjusting the voltage.

        



Polarity
--------

.. py:class:: Polarity

    .. py:attribute:: Polarity.HIGH



        A high pulse occurs when the event is generated.  The exported signal is low level both before and after the event is generated.

        



    .. py:attribute:: Polarity.LOW



        A low pulse occurs when the event is generated.  The exported signal is high level both before and after the event is generated.

        



PowerAllocationMode
-------------------

.. py:class:: PowerAllocationMode

    .. py:attribute:: PowerAllocationMode.DISABLED



        The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower does not perform a sourcing power check. If the required power is greater than the maximum sourcing power, the device attempts to source the required amount and may shut down to prevent damage.

        



    .. py:attribute:: PowerAllocationMode.AUTOMATIC



        The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower performs a sourcing power check. If the required power is greater than the maximum sourcing power, the device does not exceed the maximum power, and NI-DCPower returns an error.

        



    .. py:attribute:: PowerAllocationMode.MANUAL



        The device attempts to source, on each active channel, the power you request with the :py:attr:`nidcpower.Session.requested_power_allocation` property; NI-DCPower performs a sourcing power check. If the requested power is either less than the required power for the present source configuration or greater than the maximum sourcing power, the device does not exceed the requested or allowed power, respectively, and NI-DCPower returns an error.

        



PowerSource
-----------

.. py:class:: PowerSource

    .. py:attribute:: PowerSource.INTERNAL



        Uses the PXI chassis power source.

        



    .. py:attribute:: PowerSource.AUXILIARY



        Uses the auxiliary power source connected to the device.

        



    .. py:attribute:: PowerSource.AUTOMATIC



        Uses the auxiliary power source if it is available; otherwise uses the PXI chassis power source.

        



PowerSourceInUse
----------------

.. py:class:: PowerSourceInUse

    .. py:attribute:: PowerSourceInUse.INTERNAL



        Uses the PXI chassis power source.

        



    .. py:attribute:: PowerSourceInUse.AUXILIARY



        Uses the auxiliary power source connected to the device. Only the NI PXI-4110,  NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this value. This is the only supported value  for the NI PXIe-4112 and NI PXIe-4113.

        



SelfCalibrationPersistence
--------------------------

.. py:class:: SelfCalibrationPersistence

    .. py:attribute:: SelfCalibrationPersistence.KEEP_IN_MEMORY



        Keep new self calibration values in memory only.

        



    .. py:attribute:: SelfCalibrationPersistence.WRITE_TO_EEPROM



        Write new self calibration values to hardware.

        



SendSoftwareEdgeTriggerType
---------------------------

.. py:class:: SendSoftwareEdgeTriggerType

    .. py:attribute:: SendSoftwareEdgeTriggerType.START



    .. py:attribute:: SendSoftwareEdgeTriggerType.SOURCE



    .. py:attribute:: SendSoftwareEdgeTriggerType.MEASURE



    .. py:attribute:: SendSoftwareEdgeTriggerType.SEQUENCE_ADVANCE



    .. py:attribute:: SendSoftwareEdgeTriggerType.PULSE



    .. py:attribute:: SendSoftwareEdgeTriggerType.SHUTDOWN



Sense
-----

.. py:class:: Sense

    .. py:attribute:: Sense.LOCAL



        Local sensing is selected.

        



    .. py:attribute:: Sense.REMOTE



        Remote sensing is selected.

        



SourceMode
----------

.. py:class:: SourceMode

    .. py:attribute:: SourceMode.SINGLE_POINT



        The source unit applies a single source configuration.

        



    .. py:attribute:: SourceMode.SEQUENCE



        The source unit applies a list of voltage or current configurations sequentially.

        



TransientResponse
-----------------

.. py:class:: TransientResponse

    .. py:attribute:: TransientResponse.NORMAL



        The output responds to changes in load at a normal speed.

        



    .. py:attribute:: TransientResponse.FAST



        The output responds to changes in load quickly.

        



    .. py:attribute:: TransientResponse.SLOW



        The output responds to changes in load slowly.

        



    .. py:attribute:: TransientResponse.CUSTOM



        The output responds to changes in load based on specified values.

        



TriggerType
-----------

.. py:class:: TriggerType

    .. py:attribute:: TriggerType.NONE



        No trigger is configured.

        



    .. py:attribute:: TriggerType.DIGITAL_EDGE



        The data operation starts when a digital edge is detected.

        



    .. py:attribute:: TriggerType.SOFTWARE_EDGE



        The data operation starts when a software trigger occurs.

        





