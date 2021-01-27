Enums
=====

Enums used in NI-Digital Pattern Driver

.. py:currentmodule:: nidigital


BitOrder
--------

.. py:class:: BitOrder

    .. py:attribute:: BitOrder.MSB



        The most significant bit is first. The first bit is in the 2n place, where n is the number of bits.

        



    .. py:attribute:: BitOrder.LSB



        The least significant bit is first. The first bit is in the 20 place.

        



DigitalEdge
-----------

.. py:class:: DigitalEdge

    .. py:attribute:: DigitalEdge.RISING



        Asserts the trigger when the signal transitions from low level to high level.

        



    .. py:attribute:: DigitalEdge.FALLING



        Asserts the trigger when the signal transitions from high level to low level.

        



DriveFormat
-----------

.. py:class:: DriveFormat

    .. py:attribute:: DriveFormat.NR



        Drive format remains at logic level after each bit.

        



    .. py:attribute:: DriveFormat.RL



        Drive format returns to a logic level low after each bit.

        



    .. py:attribute:: DriveFormat.RH



        Drive format returns to a logic level high after each bit.

        



    .. py:attribute:: DriveFormat.SBC



        Drive format returns to the complement logic level of the bit after each bit.

        



HistoryRAMCyclesToAcquire
-------------------------

.. py:class:: HistoryRAMCyclesToAcquire

    .. py:attribute:: HistoryRAMCyclesToAcquire.FAILED



        Acquires failed cycles.

        



    .. py:attribute:: HistoryRAMCyclesToAcquire.ALL



        Acquires all cycles.

        



HistoryRAMTriggerType
---------------------

.. py:class:: HistoryRAMTriggerType

    .. py:attribute:: HistoryRAMTriggerType.FIRST_FAILURE



        First Failure History RAM trigger

        



    .. py:attribute:: HistoryRAMTriggerType.CYCLE_NUMBER



        Cycle Number History RAM trigger.

        



    .. py:attribute:: HistoryRAMTriggerType.PATTERN_LABEL



        Pattern Label History RAM trigger

        



PPMUApertureTimeUnits
---------------------

.. py:class:: PPMUApertureTimeUnits

    .. py:attribute:: PPMUApertureTimeUnits.SECONDS



        Unit in seconds.

        



PPMUCurrentLimitBehavior
------------------------

.. py:class:: PPMUCurrentLimitBehavior

    .. py:attribute:: PPMUCurrentLimitBehavior.REGULATE



        Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached.

        



PPMUMeasurementType
-------------------

.. py:class:: PPMUMeasurementType

    .. py:attribute:: PPMUMeasurementType.CURRENT



        The PPMU measures current.

        



    .. py:attribute:: PPMUMeasurementType.VOLTAGE



        The PPMU measures voltage.

        



PPMUOutputFunction
------------------

.. py:class:: PPMUOutputFunction

    .. py:attribute:: PPMUOutputFunction.VOLTAGE



        The PPMU forces voltage to the DUT.

        



    .. py:attribute:: PPMUOutputFunction.CURRENT



        The PPMU forces current to the DUT.

        



PinState
--------

.. py:class:: PinState

    .. py:attribute:: PinState.ZERO



        A digital state of 0. This state can be used for WriteStatic(PinState).

        



    .. py:attribute:: PinState.ONE



        A digital state of 1. This state can be used for WriteStatic(PinState).

        



    .. py:attribute:: PinState.L



        A digital state of L (low). This state should not be used with WriteStatic(PinState).

        



    .. py:attribute:: PinState.H



        A digital state of H (high). This state should not be used with WriteStatic(PinState).

        



    .. py:attribute:: PinState.X



        A digital state of X (non-drive state). This state can be used for WriteStatic(PinState).

        



    .. py:attribute:: PinState.M



        A digital state of M (midband). This state should not be used with WriteStatic(PinState).

        



    .. py:attribute:: PinState.V



        A digital state of V (compare high or low, not midband; store results from capture functionality if configured). This state should not be used with WriteStatic(PinState).

        



    .. py:attribute:: PinState.D



        A digital state of D (drive data from source functionality if configured). This state should not be used with WriteStatic(PinState).

        



    .. py:attribute:: PinState.E



    .. py:attribute:: PinState.NOT_A_PIN_STATE



        Not a pin state is used for non-existent DUT cycles.

        



    .. py:attribute:: PinState.PIN_STATE_NOT_ACQUIRED



SelectedFunction
----------------

.. py:class:: SelectedFunction

    .. py:attribute:: SelectedFunction.DIGITAL



        The pattern sequencer controls the specified pin(s). If a pattern is currently bursting, the pin immediately switches to bursting the pattern. This option disconnects the PPMU.

        



    .. py:attribute:: SelectedFunction.PPMU



        The PPMU controls the specified pin(s) and connects the PPMU. The pin driver is in a non-drive state, and the active load is disabled. The PPMU does not start sourcing or measuring until Source or Measure(PpmuMeasurementType) is called.

        



    .. py:attribute:: SelectedFunction.OFF



        Puts the digital driver in a non-drive state, disables the active load, disconnects the PPMU, and closes the I/O switch connecting the instrument channel.

        



    .. py:attribute:: SelectedFunction.DISCONNECT



        The I/O switch connecting the instrument channel is open to the I/O connector. If the PPMU is sourcing, it is stopped prior to opening the I/O switch.

        



SequencerFlag
-------------

.. py:class:: SequencerFlag

    .. py:attribute:: SequencerFlag.FLAG0



    .. py:attribute:: SequencerFlag.FLAG1



    .. py:attribute:: SequencerFlag.FLAG2



    .. py:attribute:: SequencerFlag.FLAG3



SequencerRegister
-----------------

.. py:class:: SequencerRegister

    .. py:attribute:: SequencerRegister.REGISTER0



    .. py:attribute:: SequencerRegister.REGISTER1



    .. py:attribute:: SequencerRegister.REGISTER2



    .. py:attribute:: SequencerRegister.REGISTER3



    .. py:attribute:: SequencerRegister.REGISTER4



    .. py:attribute:: SequencerRegister.REGISTER5



    .. py:attribute:: SequencerRegister.REGISTER6



    .. py:attribute:: SequencerRegister.REGISTER7



    .. py:attribute:: SequencerRegister.REGISTER8



    .. py:attribute:: SequencerRegister.REGISTER9



    .. py:attribute:: SequencerRegister.REGISTER10



    .. py:attribute:: SequencerRegister.REGISTER11



    .. py:attribute:: SequencerRegister.REGISTER12



    .. py:attribute:: SequencerRegister.REGISTER13



    .. py:attribute:: SequencerRegister.REGISTER14



    .. py:attribute:: SequencerRegister.REGISTER15



SoftwareTrigger
---------------

.. py:class:: SoftwareTrigger

    .. py:attribute:: SoftwareTrigger.START



    .. py:attribute:: SoftwareTrigger.CONDITIONAL_JUMP



SourceDataMapping
-----------------

.. py:class:: SourceDataMapping

    .. py:attribute:: SourceDataMapping.BROADCAST



        Broadcasts the waveform you specify to all sites.

        



    .. py:attribute:: SourceDataMapping.SITE_UNIQUE



        Sources unique waveform data to each site.

        



TDREndpointTermination
----------------------

.. py:class:: TDREndpointTermination

    .. py:attribute:: TDREndpointTermination.OPEN



        TDR channels are connected to an open circuit.

        



    .. py:attribute:: TDREndpointTermination.SHORT_TO_GROUND



        TDR channels are connected to a short to ground.

        



TerminationMode
---------------

.. py:class:: TerminationMode

    .. py:attribute:: TerminationMode.ACTIVE_LOAD



        The active load provides a constant current to a commutating voltage (Vcom).

        



    .. py:attribute:: TerminationMode.VTERM



        The pin driver drives Vterm.

        



    .. py:attribute:: TerminationMode.HIGH_Z



        The pin driver is in a non-drive state (in a high-impedance state) and the active load is disabled.

        



TimeSetEdgeType
---------------

.. py:class:: TimeSetEdgeType

    .. py:attribute:: TimeSetEdgeType.DRIVE_ON



        Specifies the drive on edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.DRIVE_DATA



        Specifies the drive data edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.DRIVE_RETURN



        Specifies the drive return edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.DRIVE_OFF



        Specifies the drive off edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.COMPARE_STROBE



        Specifies the compare strobe of the time set.

        



    .. py:attribute:: TimeSetEdgeType.DRIVE_DATA2



        Specifies the drive data 2 edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.DRIVE_RETURN2



        Specifies the drive return 2 edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.COMPARE_STROBE2



        Specifies the compare strobe 2 of the time set.

        



TriggerType
-----------

.. py:class:: TriggerType

    .. py:attribute:: TriggerType.NONE



        Disables the start trigger.

        



    .. py:attribute:: TriggerType.DIGITAL_EDGE



        Digital edge trigger.

        



    .. py:attribute:: TriggerType.SOFTWARE



        Software start trigger.

        



WriteStaticPinState
-------------------

.. py:class:: WriteStaticPinState

    .. py:attribute:: WriteStaticPinState.ZERO



    .. py:attribute:: WriteStaticPinState.ONE



    .. py:attribute:: WriteStaticPinState.X





