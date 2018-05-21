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

        



DigitalEdge
-----------

.. py:class:: DigitalEdge

    .. py:attribute:: DigitalEdge.RISING



        Asserts the trigger on the rising edge of the digital signal.

        



    .. py:attribute:: DigitalEdge.FALLING



        Asserts the trigger on the falling edge of the digital signal.

        



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

        





