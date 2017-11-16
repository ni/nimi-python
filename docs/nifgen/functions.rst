nifgen.Session methods
======================

.. py:currentmodule:: nifgen

.. function:: adjust_sample_clock_relative_delay(adjustment_time)

    Delays (or phase shifts) the Sample Clock, which delays the generated
    signal. Delaying the Sample Clock can be useful when synchronizing the
    output of multiple modules or when intentionally phase shifting the
    output relative to a fixed reference, such as the PLL Reference Clock.

    Adjustment time can be positive or negative, but it must be less than or
    equal to the Sample Clock period. The delay takes effect immediately
    after this function is called. To delay an external Sample Clock, use
    the :py:data:`nifgen.SAMPLE\_CLOCK\_ABSOLUTE\_DELAY` attribute.

    



    :param adjustment_time:


        Specifies the amount of time to adjust the Sample Clock delay.

        **Units**: Seconds

        **Default Value**: 0

        


    :type adjustment_time: float

.. function:: allocate_named_waveform(waveform_name, waveform_size)

    Specifies the size of a named waveform up front so that it can be
    allocated in onboard memory before loading the associated data. Data can
    then be loaded in smaller blocks with the niFgen Write (Binary16)
    Waveform functions.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].allocate_named_waveform(waveform_name, waveform_size)


    :param waveform_name:


        Specifies the name to associate with the allocated waveform.

        


    :type waveform_name: string
    :param waveform_size:


        Specifies the size of the waveform to allocate in samples.

        **Default Value**: "4096"

        


    :type waveform_size: int

.. function:: allocate_waveform(waveform_size)

    Specifies the size of a waveform so that it can be allocated in onboard
    memory before loading the associated data. Data can then be loaded in
    smaller blocks with the Write Binary 16 Waveform functions.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this function.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].allocate_waveform(waveform_size)


    :param waveform_size:


        Specifies, in samples, the size of the waveform to allocate.

        


    :type waveform_size: int

    :rtype: int
    :return:


            The handle that identifies the new waveform. This handle is used later
            when referring to this waveform.

            



.. function:: clear_arb_memory()

    Removes all previously created arbitrary waveforms, sequences, and
    scripts from the signal generator memory and invalidates all waveform
    handles, sequence handles, and waveform names.

    

    .. note:: The signal generator must not be in the Generating state when you
        call this function.



.. function:: clear_arb_sequence(sequence_handle)

    Removes a previously created arbitrary sequence from the signal
    generator memory and invalidates the sequence handle.

    

    .. note:: The signal generator must not be in the Generating state when you
        call this function.



    :param sequence_handle:


        Specifies the handle of the arbitrary sequence that you want the signal
        generator to remove. You can create an arbitrary sequence using the
        nifgen\_CreateArbSequence or nifgen\_CreateAdvancedArbSequence function.
        These functions return a handle that you use to identify the sequence.

        | **Defined Value**:
        | NIFGEN\_VAL\_ALL\_SEQUENCES—Remove all sequences from the signal
          generator

        **Default Value**: None

        


    :type sequence_handle: int

.. function:: clear_arb_waveform(waveform_handle)

    Removes a previously created arbitrary waveform from the signal
    generator memory and invalidates the waveform handle.

    

    .. note:: The signal generator must not be in the Generating state when you
        call this function.



    :param waveform_handle:


        Specifies the handle of the arbitrary waveform that you want the signal
        generator to remove.

        You can create multiple arbitrary waveforms using one of the following
        niFgen Create Waveform functions:

        -  :py:func:`nifgen.create_waveform_f64`
        -  :py:func:`nifgen.create_waveform_i16`
        -  :py:func:`nifgen.create_waveform_from_file_i16`
        -  :py:func:`nifgen.create_waveform_from_file_f64`
        -  :py:func:`nifgen.CreateWaveformFromFileHWS`

        **Defined Value**:

        NIFGEN\_VAL\_ALL\_WAVEFORMS—Remove all waveforms from the signal
        generator.

        **Default Value**: None

        


    :type waveform_handle: int

.. function:: clear_freq_list(frequency_list_handle)

    Removes a previously created frequency list from the signal generator
    memory and invalidates the frequency list handle.

    

    .. note:: The signal generator must not be in the Generating state when you
        call this function.



    :param frequency_list_handle:


        Specifies the handle of the frequency list you want the signal generator
        to remove. You create multiple frequency lists using
        :py:func:`nifgen.create_freq_list`. :py:func:`nifgen.create_freq_list` returns a handle that you
        use to identify each list. Specify a value of -1 to clear all frequency
        lists.

        **Defined Value**

        NIFGEN\_VAL\_ALL\_FLISTS—Remove all frequency lists from the signal
        generator.

        **Default Value**: None

        


    :type frequency_list_handle: int

.. function:: clear_user_standard_waveform()

    Clears the user-defined waveform created by the
    nifgen\_DefineUserStandardWaveform function.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].clear_user_standard_waveform()


.. function:: commit()

    Causes a transition to the Committed state. This function verifies
    attribute values, reserves the device, and commits the attribute values
    to the device. If the attribute values are all valid, NI-FGEN sets the
    device hardware configuration to match the session configuration. This
    function does not support the NI 5401/5404/5411/5431 signal generators.

    In the Committed state, you can load waveforms, scripts, and sequences
    into memory. If any attributes are changed, NI-FGEN implicitly
    transitions back to the Idle state, where you can program all session
    properties before applying them to the device. This function has no
    effect if the device is already in the Committed or Generating state and
    returns a successful status value.

    Calling this VI before the niFgen Initiate Generation VI is optional but
    has the following benefits:

    -  Routes are committed, so signals are exported or imported.
    -  Any Reference Clock and external clock circuits are phase-locked.
    -  A subsequent :py:func:`nifgen._initiate_generation` function can run faster
       because the device is already configured.

    



.. function:: configure_arb_sequence(sequence_handle, gain, offset)

    Configures the signal generator attributes that affect arbitrary
    sequence generation. Sets the :py:data:`nifgen.ARB\_SEQUENCE\_HANDLE`,
    :py:data:`nifgen.ARB\_GAIN`, and :py:data:`nifgen.ARB\_OFFSET` attributes.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this function.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].configure_arb_sequence(sequence_handle, gain, offset)


    :param sequence_handle:


        Specifies the handle of the arbitrary sequence that you want the signal
        generator to produce. NI-FGEN sets the
        :py:data:`nifgen.ARB\_SEQUENCE\_HANDLE` attribute to this value. You can
        create an arbitrary sequence using the :py:func:`nifgen.create_arb_sequence` or
        :py:func:`nifgen.create_advanced_arb_sequence` function. These functions return a
        handle that you use to identify the sequence.

        **Default Value**: None

        


    :type sequence_handle: int
    :param gain:


        Specifies the factor by which the signal generator scales the arbitrary
        waveforms in the sequence. When you create an arbitrary waveform, you
        must first normalize the data points to a range of –1.00 to +1.00. You
        can use this parameter to scale the waveform to other ranges. The gain
        is applied before the offset is added.

        For example, to configure the output signal to range from –2.00 to
        +2.00 V, set **gain** to 2.00.

        **Units**: unitless

        **Default Value**: None

        


    :type gain: float
    :param offset:


        Specifies the value the signal generator adds to the arbitrary waveform
        data. When you create arbitrary waveforms, you must first normalize the
        data points to a range of –1.00 to +1.00 V. You can use this parameter
        to shift the range of the arbitrary waveform. NI-FGEN sets the
        :py:data:`nifgen.ARB\_OFFSET` attribute to this value.

        For example, to configure the output signal to range from 0.00 to 2.00 V
        instead of –1.00 to 1.00 V, set the offset to 1.00.

        **Units**: volts

        **Default Value**: None

        


    :type offset: float

.. function:: configure_arb_waveform(waveform_handle, gain, offset)

    Configures the attributes of the signal generator that affect arbitrary
    waveform generation. Sets the :py:data:`nifgen.ARB\_WAVEFORM\_HANDLE`,
    :py:data:`nifgen.ARB\_GAIN`, and :py:data:`nifgen.ARB\_OFFSET` attributes.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this function.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].configure_arb_waveform(waveform_handle, gain, offset)


    :param waveform_handle:


        Specifies the handle of the arbitrary waveform you want the signal
        generator to produce. NI-FGEN sets the
        :py:data:`nifgen.ARB\_WAVEFORM\_HANDLE` attribute to this value. You can
        create an arbitrary waveform using one of the following niFgen Create
        Waveform functions:

        -  :py:func:`nifgen.create_waveform_f64`
        -  :py:func:`nifgen.create_waveform_i16`
        -  :py:func:`nifgen.create_waveform_from_file_i16`
        -  :py:func:`nifgen.create_waveform_from_file_f64`
        -  :py:func:`nifgen.CreateWaveformFromFileHWS`

        These functions return a handle that you use to identify the waveform.

        **Default Value**: None

        


    :type waveform_handle: int
    :param gain:


        Specifies the factor by which the signal generator scales the arbitrary
        waveforms in the sequence. When you create an arbitrary waveform, you
        must first normalize the data points to a range of –1.00 to +1.00. You
        can use this parameter to scale the waveform to other ranges. The gain
        is applied before the offset is added.

        For example, to configure the output signal to range from –2.00 to
        +2.00 V, set **gain** to 2.00.

        **Units**: unitless

        **Default Value**: None

        


    :type gain: float
    :param offset:


        Specifies the value the signal generator adds to the arbitrary waveform
        data. When you create arbitrary waveforms, you must first normalize the
        data points to a range of –1.00 to +1.00 V. You can use this parameter
        to shift the range of the arbitrary waveform. NI-FGEN sets the
        :py:data:`nifgen.ARB\_OFFSET` attribute to this value.

        For example, to configure the output signal to range from 0.00 to 2.00 V
        instead of –1.00 to 1.00 V, set the offset to 1.00.

        **Units**: volts

        **Default Value**: None

        


    :type offset: float

.. function:: configure_custom_fir_filter_coefficients(coefficients_array)

    Sets the FIR filter coefficients used by the onboard signal processing
    block. The values are coerced to the closest settings achievable by the
    signal generator.

    Refer to the *FIR Filter* topic for your device in the *NI Signal
    Generators Help* for more information about FIR filter coefficients.
    This function is supported only for the NI 5441.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this function.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].configure_custom_fir_filter_coefficients(coefficients_array)


    :param coefficients_array:


        Specifies the array of data the onboard signal processor uses for the
        FIR filter coefficients. For the NI 5441, provide a symmetric array of
        95 coefficients to this parameter. The array must have at least as many
        elements as the value that you specify in the **numberOfCoefficients**
        parameter in this function.
        The coefficients should range between –1.00 and +1.00.

        


    :type coefficients_array: list of float

.. function:: configure_digital_edge_script_trigger(trigger_id, source, edge=nifgen.ScriptTriggerDigitalEdgeEdge.RISING)

    Configures the specified Script Trigger for digital edge triggering.

    



    :param trigger_id:


        Specifies the Script Trigger used for triggering.

        **Defined Values**

        **Default Value**: "ScriptTrigger0"

        +------------------+------------------+
        | "ScriptTrigger0" | Script Trigger 0 |
        +------------------+------------------+
        | "ScriptTrigger1" | Script Trigger 1 |
        +------------------+------------------+
        | "ScriptTrigger2" | Script Trigger 2 |
        +------------------+------------------+
        | "ScriptTrigger3" | Script Trigger 3 |
        +------------------+------------------+


    :type trigger_id: string
    :param source:


        Specifies which trigger source the signal generator uses.

        **Defined Values**

        **Default Value**: "PFI0"

        +--------------+-----------------------------------+
        | "PFI0"       | PFI 0                             |
        +--------------+-----------------------------------+
        | "PFI1"       | PFI 1                             |
        +--------------+-----------------------------------+
        | "PFI2"       | PFI 2                             |
        +--------------+-----------------------------------+
        | "PFI3"       | PFI 3                             |
        +--------------+-----------------------------------+
        | "PFI4"       | PFI 4                             |
        +--------------+-----------------------------------+
        | "PFI5"       | PFI 5                             |
        +--------------+-----------------------------------+
        | "PFI6"       | PFI 6                             |
        +--------------+-----------------------------------+
        | "PFI7"       | PFI 7                             |
        +--------------+-----------------------------------+
        | "PXI\_Trig0" | PXI trigger line 0 or RTSI line 0 |
        +--------------+-----------------------------------+
        | "PXI\_Trig1" | PXI trigger line 1 or RTSI line 1 |
        +--------------+-----------------------------------+
        | "PXI\_Trig2" | PXI trigger line 2 or RTSI line 2 |
        +--------------+-----------------------------------+
        | "PXI\_Trig3" | PXI trigger line 3 or RTSI line 3 |
        +--------------+-----------------------------------+
        | "PXI\_Trig4" | PXI trigger line 4 or RTSI line 4 |
        +--------------+-----------------------------------+
        | "PXI\_Trig5" | PXI trigger line 5 or RTSI line 5 |
        +--------------+-----------------------------------+
        | "PXI\_Trig6" | PXI trigger line 6 or RTSI line 6 |
        +--------------+-----------------------------------+
        | "PXI\_Trig7" | PXI trigger line 7 or RTSI line 7 |
        +--------------+-----------------------------------+
        | "PXI\_Star"  | PXI star trigger line             |
        +--------------+-----------------------------------+


    :type source: string
    :param edge:


        Specifies the edge to detect.

        ****Defined Values****

        ****Default Value**:** NIFGEN\_VAL\_RISING\_EDGE

        +----------------------------+------------------------------------------------------------------+
        | NIFGEN\_VAL\_RISING\_EDGE  | Occurs when the signal transitions from low level to high level. |
        +----------------------------+------------------------------------------------------------------+
        | NIFGEN\_VAL\_FALLING\_EDGE | Occurs when the signal transitions from high level to low level. |
        +----------------------------+------------------------------------------------------------------+


    :type edge: :py:data:`nifgen.ScriptTriggerDigitalEdgeEdge`

.. function:: configure_digital_edge_start_trigger(source, edge=nifgen.StartTriggerDigitalEdgeEdge.RISING)

    Configures the Start Trigger for digital edge triggering.

    



    :param source:


        Specifies which trigger source the signal generator uses.

        **Defined Values**

        **Default Value**: "PFI0"

        +--------------+-----------------------------------+
        | "PFI0"       | PFI 0                             |
        +--------------+-----------------------------------+
        | "PFI1"       | PFI 1                             |
        +--------------+-----------------------------------+
        | "PFI2"       | PFI 2                             |
        +--------------+-----------------------------------+
        | "PFI3"       | PFI 3                             |
        +--------------+-----------------------------------+
        | "PFI4"       | PFI 4                             |
        +--------------+-----------------------------------+
        | "PFI5"       | PFI 5                             |
        +--------------+-----------------------------------+
        | "PFI6"       | PFI 6                             |
        +--------------+-----------------------------------+
        | "PFI7"       | PFI 7                             |
        +--------------+-----------------------------------+
        | "PXI\_Trig0" | PXI trigger line 0 or RTSI line 0 |
        +--------------+-----------------------------------+
        | "PXI\_Trig1" | PXI trigger line 1 or RTSI line 1 |
        +--------------+-----------------------------------+
        | "PXI\_Trig2" | PXI trigger line 2 or RTSI line 2 |
        +--------------+-----------------------------------+
        | "PXI\_Trig3" | PXI trigger line 3 or RTSI line 3 |
        +--------------+-----------------------------------+
        | "PXI\_Trig4" | PXI trigger line 4 or RTSI line 4 |
        +--------------+-----------------------------------+
        | "PXI\_Trig5" | PXI trigger line 5 or RTSI line 5 |
        +--------------+-----------------------------------+
        | "PXI\_Trig6" | PXI trigger line 6 or RTSI line 6 |
        +--------------+-----------------------------------+
        | "PXI\_Trig7" | PXI trigger line 7 or RTSI line 7 |
        +--------------+-----------------------------------+
        | "PXI\_Star"  | PXI star trigger line             |
        +--------------+-----------------------------------+


    :type source: string
    :param edge:


        Specifies the edge to detect.

        ****Defined Values****

        ****Default Value**:** NIFGEN\_VAL\_RISING\_EDGE

        +----------------------------+------------------------------------------------------------------+
        | NIFGEN\_VAL\_RISING\_EDGE  | Occurs when the signal transitions from low level to high level. |
        +----------------------------+------------------------------------------------------------------+
        | NIFGEN\_VAL\_FALLING\_EDGE | Occurs when the signal transitions from high level to low level. |
        +----------------------------+------------------------------------------------------------------+


    :type edge: :py:data:`nifgen.StartTriggerDigitalEdgeEdge`

.. function:: configure_digital_level_script_trigger(trigger_id, source, trigger_when)

    Configures the specified Script Trigger for digital level triggering.

    



    :param trigger_id:


        Specifies the Script Trigger used for triggering.

        **Defined Values**

        **Default Value**: "ScriptTrigger0"

        +------------------+------------------+
        | "ScriptTrigger0" | Script Trigger 0 |
        +------------------+------------------+
        | "ScriptTrigger1" | Script Trigger 1 |
        +------------------+------------------+
        | "ScriptTrigger2" | Script Trigger 2 |
        +------------------+------------------+
        | "ScriptTrigger3" | Script Trigger 3 |
        +------------------+------------------+


    :type trigger_id: string
    :param source:


        Specifies which trigger source the signal generator uses.

        **Defined Values**

        **Default Value**: "PFI0"

        +--------------+-----------------------------------+
        | "PFI0"       | PFI 0                             |
        +--------------+-----------------------------------+
        | "PFI1"       | PFI 1                             |
        +--------------+-----------------------------------+
        | "PFI2"       | PFI 2                             |
        +--------------+-----------------------------------+
        | "PFI3"       | PFI 3                             |
        +--------------+-----------------------------------+
        | "PFI4"       | PFI 4                             |
        +--------------+-----------------------------------+
        | "PFI5"       | PFI 5                             |
        +--------------+-----------------------------------+
        | "PFI6"       | PFI 6                             |
        +--------------+-----------------------------------+
        | "PFI7"       | PFI 7                             |
        +--------------+-----------------------------------+
        | "PXI\_Trig0" | PXI trigger line 0 or RTSI line 0 |
        +--------------+-----------------------------------+
        | "PXI\_Trig1" | PXI trigger line 1 or RTSI line 1 |
        +--------------+-----------------------------------+
        | "PXI\_Trig2" | PXI trigger line 2 or RTSI line 2 |
        +--------------+-----------------------------------+
        | "PXI\_Trig3" | PXI trigger line 3 or RTSI line 3 |
        +--------------+-----------------------------------+
        | "PXI\_Trig4" | PXI trigger line 4 or RTSI line 4 |
        +--------------+-----------------------------------+
        | "PXI\_Trig5" | PXI trigger line 5 or RTSI line 5 |
        +--------------+-----------------------------------+
        | "PXI\_Trig6" | PXI trigger line 6 or RTSI line 6 |
        +--------------+-----------------------------------+
        | "PXI\_Trig7" | PXI trigger line 7 or RTSI line 7 |
        +--------------+-----------------------------------+
        | "PXI\_Star"  | PXI star trigger line             |
        +--------------+-----------------------------------+


    :type source: string
    :param trigger_when:


        Specifies whether the Script Trigger asserts on a high or low digital
        level.

        **Defined Values**

        **Default Value**: "HighLevel"

        +-------------+-------------------------------------------------+
        | "HighLevel" | Script Trigger asserts on a high digital level. |
        +-------------+-------------------------------------------------+
        | "LowLevel"  | Script Trigger asserts on a low digital level.  |
        +-------------+-------------------------------------------------+


    :type trigger_when: int

.. function:: configure_freq_list(frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0)

    Configures the attributes of the signal generator that affect frequency
    list generation (the :py:data:`nifgen.FREQ\_LIST\_HANDLE`,
    :py:data:`nifgen.FUNC\_AMPLITUDE`, :py:data:`nifgen.FUNC\_DC\_OFFSET`, and
    :py:data:`nifgen.FUNC\_START\_PHASE` attributes).

    

    .. note:: The signal generator must not be in the Generating state when you call
        this function.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].configure_freq_list(frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0)


    :param frequency_list_handle:


        Specifies the handle of the frequency list that you want the signal
        generator to produce. NI-FGEN sets the :py:data:`nifgen.FREQ\_LIST\_HANDLE`
        attribute to this value. You can create a frequency list using the
        :py:func:`nifgen.create_freq_list` function, which returns a handle that you use to
        identify the list.
        **Default Value**: None

        


    :type frequency_list_handle: int
    :param amplitude:


        Specifies the amplitude of the standard waveform that you want the
        signal generator to produce. This value is the amplitude at the output
        terminal. NI-FGEN sets the :py:data:`nifgen.FUNC\_AMPLITUDE` attribute to
        this value.

        For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
        the amplitude to 10.00 V.

        **Units**: peak-to-peak voltage

        **Default Value**: None

        

        .. note:: This parameter does not affect signal generator behavior when you set
            the **waveform** parameter of the :py:func:`nifgen.configure_standard_waveform`
            function to NIFGEN\_VAL\_WFM\_DC.


    :type amplitude: float
    :param dc_offset:


        Specifies the DC offset of the standard waveform that you want the
        signal generator to produce. The value is the offset from ground to the
        center of the waveform you specify with the **waveform** parameter,
        observed at the output terminal. For example, to configure a waveform
        with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
        **dcOffset** to 5.00 V. NI-FGEN sets the :py:data:`nifgen.FUNC\_DC\_OFFSET`
        attribute to this value.

        **Units**: volts

        **Default Value**: None

        


    :type dc_offset: float
    :param start_phase:


        Specifies the horizontal offset of the standard waveform you want the
        signal generator to produce. Specify this attribute in degrees of one
        waveform cycle. NI-FGEN sets the :py:data:`nifgen.FUNC\_START\_PHASE`
        attribute to this value. A start phase of 180 degrees means output
        generation begins halfway through the waveform. A start phase of 360
        degrees offsets the output by an entire waveform cycle, which is
        identical to a start phase of 0 degrees.

        **Units**: degrees of one cycle

        **Default Value**: None degrees

        

        .. note:: This parameter does not affect signal generator behavior when you set
            the **waveform** parameter to NIFGEN\_VAL\_WFM\_DC.


    :type start_phase: float

.. function:: configure_standard_waveform(waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0)

    Configures the following attributes of the signal generator that affect
    standard waveform generation:

    -  :py:data:`nifgen.FUNC\_WAVEFORM`
    -  :py:data:`nifgen.FUNC\_AMPLITUDE`
    -  :py:data:`nifgen.FUNC\_DC\_OFFSET`
    -  :py:data:`nifgen.FUNC\_FREQUENCY`
    -  :py:data:`nifgen.FUNC\_START\_PHASE`

    

    .. note:: You must call the :py:func:`nifgen.ConfigureOutputMode` function with the
        **outputMode** parameter set to NIFGEN\_VAL\_OUTPUT\_FUNC before calling
        this function.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].configure_standard_waveform(waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0)


    :param waveform:


        Specifies the standard waveform that you want the signal generator to
        produce. NI-FGEN sets the :py:data:`nifgen.FUNC\_WAVEFORM` attribute to this
        value.

        ****Defined Values****

        **Default Value**: NIFGEN\_VAL\_WFM\_SINE

        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_SINE       | Specifies that the signal generator produces a sinusoid waveform.                                                                     |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_SQUARE     | Specifies that the signal generator produces a square waveform.                                                                       |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_TRIANGLE   | Specifies that the signal generator produces a triangle waveform.                                                                     |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_RAMP\_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                                |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_RAMP\_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                                |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_DC         | Specifies that the signal generator produces a constant voltage.                                                                      |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_NOISE      | Specifies that the signal generator produces white noise.                                                                             |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_USER       | Specifies that the signal generator produces a user-defined waveform as defined with the nifgen\_DefineUserStandardWaveform function. |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+


    :type waveform: :py:data:`nifgen.Waveform`
    :param amplitude:


        Specifies the amplitude of the standard waveform that you want the
        signal generator to produce. This value is the amplitude at the output
        terminal. NI-FGEN sets the :py:data:`nifgen.FUNC\_AMPLITUDE` attribute to
        this value.

        For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
        the amplitude to 10.00 V.

        **Units**: peak-to-peak voltage

        **Default Value**: None

        

        .. note:: This parameter does not affect signal generator behavior when you set
            the **waveform** parameter of the :py:func:`nifgen.configure_standard_waveform`
            function to NIFGEN\_VAL\_WFM\_DC.


    :type amplitude: float
    :param frequency:


        | Specifies the frequency of the standard waveform that you want the
          signal generator to produce. NI-FGEN sets the
          :py:data:`nifgen.FUNC\_FREQUENCY` attribute to this value.

        **Units**: hertz

        **Default Value**: None

        

        .. note:: This parameter does not affect signal generator behavior when you set
            the **waveform** parameter of the :py:func:`nifgen.configure_standard_waveform`
            function to NIFGEN\_VAL\_WFM\_DC.


    :type frequency: float
    :param dc_offset:


        Specifies the DC offset of the standard waveform that you want the
        signal generator to produce. The value is the offset from ground to the
        center of the waveform you specify with the **waveform** parameter,
        observed at the output terminal. For example, to configure a waveform
        with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
        **dcOffset** to 5.00 V. NI-FGEN sets the :py:data:`nifgen.FUNC\_DC\_OFFSET`
        attribute to this value.

        **Units**: volts

        **Default Value**: None

        


    :type dc_offset: float
    :param start_phase:


        Specifies the horizontal offset of the standard waveform that you want
        the signal generator to produce. Specify this parameter in degrees of
        one waveform cycle. NI-FGEN sets the :py:data:`nifgen.FUNC\_START\_PHASE`
        attribute to this value. A start phase of 180 degrees means output
        generation begins halfway through the waveform. A start phase of 360
        degrees offsets the output by an entire waveform cycle, which is
        identical to a start phase of 0 degrees.

        **Units**: degrees of one cycle

        **Default Value**: 0.00

        

        .. note:: This parameter does not affect signal generator behavior when you set
            the **waveform** parameter to NIFGEN\_VAL\_WFM\_DC.


    :type start_phase: float

.. function:: create_advanced_arb_sequence(waveform_handles_array, loop_counts_array, sample_counts_array=None, marker_location_array=None)

    Creates an arbitrary sequence from an array of waveform handles and an
    array of corresponding loop counts. This function returns a handle that
    identifies the sequence. You pass this handle to the
    :py:func:`nifgen.configure_arb_sequence` function to specify what arbitrary sequence
    you want the signal generator to produce.

    The :py:func:`nifgen.create_advanced_arb_sequence` function extends on the
    :py:func:`nifgen.create_arb_sequence` function by adding the ability to set the
    number of samples in each sequence step and to set marker locations.

    An arbitrary sequence consists of multiple waveforms. For each waveform,
    you specify the number of times the signal generator produces the
    waveform before proceeding to the next waveform. The number of times to
    repeat a specific waveform is called the loop count.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this function.
        You must call the nifgen\_ConfigureOutputMode function to set the
        **outputMode** parameter to NIFGEN\_VAL\_OUTPUT\_SEQ before calling this
        function.



    :param waveform_handles_array:


        Specifies the array of waveform handles from which you want to create a
        new arbitrary sequence. The array must have at least as many elements as
        the value that you specify in **sequenceLength**. Each
        **waveformHandlesArray** element has a corresponding **loopCountsArray**
        element that indicates how many times that waveform is repeated. You
        obtain waveform handles when you create arbitrary waveforms with the
        nifgen\_AllocateWaveform function or one of the following niFgen
        CreateWaveform functions:

        -  nifgen\_CreateWaveformF64
        -  nifgen\_CreateWaveformI16
        -  nifgen\_CreateWaveformFromFileI16
        -  nifgen\_CreateWaveformFromFileF64
        -  nifgen\_CreateWaveformFromFileHWS

        **Default Value**: None

        


    :type waveform_handles_array: list of int
    :param loop_counts_array:


        Specifies the array of loop counts you want to use to create a new
        arbitrary sequence. The array must have at least as many elements as the
        value that you specify in the **sequenceLength** parameter. Each
        **loopCountsArray** element corresponds to a **waveformHandlesArray**
        element and indicates how many times to repeat that waveform. Each
        element of the **loopCountsArray** must be less than or equal to the
        maximum number of loop counts that the signal generator allows. You can
        obtain the maximum loop count from **maximumLoopCount** in the
        nifgen\_QueryArbSeqCapabilities function.

        **Default Value**: None

        


    :type loop_counts_array: list of int
    :param sample_counts_array:


        Specifies the array of sample counts that you want to use to create a
        new arbitrary sequence. The array must have at least as many elements as
        the value you specify in the **sequenceLength** parameter. Each
        **sampleCountsArray** element corresponds to a **waveformHandlesArray**
        element and indicates the subset, in samples, of the given waveform to
        generate. Each element of the **sampleCountsArray** must be larger than
        the minimum waveform size, a multiple of the waveform quantum and no
        larger than the number of samples in the corresponding waveform. You can
        obtain these values by calling the nifgen\_QueryArbWfmCapabilities
        function.

        **Default Value**: None

        


    :type sample_counts_array: list of int
    :param marker_location_array:


        Specifies the array of marker locations to where you want a marker to be
        generated in the sequence. The array must have at least as many elements
        as the value you specify in the **sequenceLength** parameter. Each
        **markerLocationArray** element corresponds to a
        **waveformHandlesArray** element and indicates where in the waveform a
        marker is to generate. The marker location must be less than the size of
        the waveform the marker is in. The markers are coerced to the nearest
        marker quantum and the coerced values are returned in the
        **coercedMarkersArray** parameter.

        If you do not want a marker generated for a particular sequence stage,
        set this parameter to NIFGEN\_VAL\_NO\_MARKER.

        **Defined Value**: NIFGEN\_VAL\_NO\_MARKER

        **Default Value**: None

        


    :type marker_location_array: list of int

    :rtype: tuple (coerced_markers_array, sequence_handle)

        WHERE

        coerced_markers_array (list of int): 


            Returns an array of all given markers that are coerced (rounded) to the
            nearest marker quantum. Not all devices coerce markers.

            **Default Value**: None

            


        sequence_handle (int): 


            Returns the handle that identifies the new arbitrary sequence. You can
            pass this handle to nifgen\_ConfigureArbSequence to generate the
            arbitrary sequence.

            



.. function:: create_arb_sequence(waveform_handles_array, loop_counts_array)

    Creates an arbitrary sequence from an array of waveform handles and an
    array of corresponding loop counts. This function returns a handle that
    identifies the sequence. You pass this handle to the
    nifgen\_ConfigureArbSequence function to specify what arbitrary sequence
    you want the signal generator to produce.

    An arbitrary sequence consists of multiple waveforms. For each waveform,
    you can specify the number of times that the signal generator produces
    the waveform before proceeding to the next waveform. The number of times
    to repeat a specific waveform is called the loop count.

    

    .. note:: You must call the nifgen\_ConfigureOutputMode function to set the
        **outputMode** parameter to NIFGEN\_VAL\_OUTPUT\_SEQ before calling this
        function.



    :param waveform_handles_array:


        Specifies the array of waveform handles from which you want to create a
        new arbitrary sequence. The array must have at least as many elements as
        the value that you specify in **sequenceLength**. Each
        **waveformHandlesArray** element has a corresponding **loopCountsArray**
        element that indicates how many times that waveform is repeated. You
        obtain waveform handles when you create arbitrary waveforms with the
        nifgen\_AllocateWaveform function or one of the following niFgen
        CreateWaveform functions:

        -  nifgen\_CreateWaveformF64
        -  nifgen\_CreateWaveformI16
        -  nifgen\_CreateWaveformFromFileI16
        -  nifgen\_CreateWaveformFromFileF64
        -  nifgen\_CreateWaveformFromFileHWS

        **Default Value**: None

        


    :type waveform_handles_array: list of int
    :param loop_counts_array:


        Specifies the array of loop counts you want to use to create a new
        arbitrary sequence. The array must have at least as many elements as the
        value that you specify in the **sequenceLength** parameter. Each
        **loopCountsArray** element corresponds to a **waveformHandlesArray**
        element and indicates how many times to repeat that waveform. Each
        element of the **loopCountsArray** must be less than or equal to the
        maximum number of loop counts that the signal generator allows. You can
        obtain the maximum loop count from **maximumLoopCount** in the
        nifgen\_QueryArbSeqCapabilities function.

        **Default Value**: None

        


    :type loop_counts_array: list of int

    :rtype: int
    :return:


            Returns the handle that identifies the new arbitrary sequence. You can
            pass this handle to nifgen\_ConfigureArbSequence to generate the
            arbitrary sequence.

            



.. function:: create_freq_list(waveform, frequency_array, duration_array)

    Creates a frequency list from an array of frequencies
    (**frequencyArray**) and an array of durations (**durationArray**). The
    two arrays should have the same number of elements, and this value must
    also be the size of the **frequencyListLength**. The function returns a
    handle that identifies the frequency list (the **frequencyListHandle**).
    You can pass this handle to nifgen\_ConfigureFreqList to specify what
    frequency list you want the signal generator to produce.

    A frequency list consists of a list of frequencies and durations. The
    signal generator generates each frequency for the given amount of time
    and then proceeds to the next frequency. When the end of the list is
    reached, the signal generator starts over at the beginning of the list.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this function.



    :param waveform:


        Specifies the standard waveform that you want the signal generator to
        produce. NI-FGEN sets the :py:data:`nifgen.FUNC\_WAVEFORM` attribute to this
        value.

        ****Defined Values****

        **Default Value**: NIFGEN\_VAL\_WFM\_SINE

        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_SINE       | Specifies that the signal generator produces a sinusoid waveform.                                                                     |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_SQUARE     | Specifies that the signal generator produces a square waveform.                                                                       |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_TRIANGLE   | Specifies that the signal generator produces a triangle waveform.                                                                     |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_RAMP\_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                                |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_RAMP\_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                                |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_DC         | Specifies that the signal generator produces a constant voltage.                                                                      |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_NOISE      | Specifies that the signal generator produces white noise.                                                                             |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WFM\_USER       | Specifies that the signal generator produces a user-defined waveform as defined with the nifgen\_DefineUserStandardWaveform function. |
        +------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+


    :type waveform: :py:data:`nifgen.Waveform`
    :param frequency_array:


        Specifies the array of frequencies to form the frequency list. The array
        must have at least as many elements as the value you specify in
        **frequencyListLength**. Each **frequencyArray** element has a
        corresponding **durationArray** element that indicates how long that
        frequency is repeated.

        **Units**: hertz

        **Default Value**: None

        


    :type frequency_array: list of float
    :param duration_array:


        Specifies the array of durations to form the frequency list. The array
        must have at least as many elements as the value that you specify in
        **frequencyListLength**. Each **durationArray** element has a
        corresponding **frequencyArray** element and indicates how long in
        seconds to generate the corresponding frequency.

        **Units**: seconds

        **Default Value**: None

        


    :type duration_array: list of float

    :rtype: int
    :return:


            Returns the handle that identifies the new frequency list. You can pass
            this handle to nifgen\_ConfigureFreqList to generate the arbitrary
            sequence.

            



.. function:: create_waveform_f64(waveform_data_array)

    Creates an onboard waveform from binary F64 (floating point double) data
    for use in Arbitrary Waveform output mode or Arbitrary Sequence output
    mode. The **waveformHandle** returned can later be used for setting the
    active waveform, changing the data in the waveform, building sequences
    of waveforms, or deleting the waveform when it is no longer needed.

    

    .. note:: You must call the nifgen\_ConfigureOutputMode function to set the
        **outputMode** parameter to NIFGEN\_VAL\_OUTPUT\_ARB or
        NIFGEN\_VAL\_OUTPUT\_SEQ before calling this function.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].create_waveform_f64(waveform_data_array)


    :param waveform_data_array:


        Specifies the array of data you want to use for the new arbitrary
        waveform. The array must have at least as many elements as the value
        that you specify in **waveformSize**.

        You must normalize the data points in the array to be between –1.00 and
        +1.00.

        **Default Value**: None

        


    :type waveform_data_array: list of float

    :rtype: int
    :return:


            The handle that identifies the new waveform. This handle is used later
            when referring to this waveform.

            



.. function:: create_waveform_from_file_f64(file_name, byte_order)

    This function takes the floating point double (F64) data from the
    specified file and creates an onboard waveform for use in Arbitrary
    Waveform or Arbitrary Sequence output mode. The **waveformHandle**
    returned by this function can later be used for setting the active
    waveform, changing the data in the waveform, building sequences of
    waveforms, or deleting the waveform when it is no longer needed.

    

    .. note:: The F64 data must be between –1.0 and +1.0 V. Use the
        :py:data:`nifgen.DIGITAL\_GAIN` attribute to generate different voltage
        outputs.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].create_waveform_from_file_f64(file_name, byte_order)


    :param file_name:


        The full path and name of the file where the waveform data resides.

        


    :type file_name: string
    :param byte_order:


        Specifies the byte order of the data in the file.

        ****Defined Values****

        |
        | ****Default Value**:** NIFGEN\_VAL\_LITTLE\_ENDIAN

        +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_LITTLE\_ENDIAN | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
        +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_BIG\_ENDIAN    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
        +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: Data written by most applications in Windows (including
            LabWindows™/CVI™) is in Little Endian format. Data written to a file
            from LabVIEW is in Big Endian format by default on all platforms. Big
            Endian and Little Endian refer to the way data is stored in memory,
            which can differ on different processors.


    :type byte_order: :py:data:`nifgen.ByteOrder`

    :rtype: int
    :return:


            The handle that identifies the new waveform. This handle is used later
            when referring to this waveform.

            



.. function:: create_waveform_from_file_i16(file_name, byte_order)

    Takes the binary 16-bit signed integer (I16) data from the specified
    file and creates an onboard waveform for use in Arbitrary Waveform or
    Arbitrary Sequence output mode. The **waveformHandle** returned by this
    function can later be used for setting the active waveform, changing the
    data in the waveform, building sequences of waveforms, or deleting the
    waveform when it is no longer needed.

    

    .. note:: The I16 data (values between –32768 and +32767) is assumed to
        represent –1 to +1 V. Use the :py:data:`nifgen.DIGITAL\_GAIN` attribute to
        generate different voltage outputs.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].create_waveform_from_file_i16(file_name, byte_order)


    :param file_name:


        The full path and name of the file where the waveform data resides.

        


    :type file_name: string
    :param byte_order:


        Specifies the byte order of the data in the file.

        ****Defined Values****

        |
        | ****Default Value**:** NIFGEN\_VAL\_LITTLE\_ENDIAN

        +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_LITTLE\_ENDIAN | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
        +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_BIG\_ENDIAN    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
        +-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: Data written by most applications in Windows (including
            LabWindows™/CVI™) is in Little Endian format. Data written to a file
            from LabVIEW is in Big Endian format by default on all platforms. Big
            Endian and Little Endian refer to the way data is stored in memory,
            which can differ on different processors.


    :type byte_order: :py:data:`nifgen.ByteOrder`

    :rtype: int
    :return:


            The handle that identifies the new waveform. This handle is used later
            when referring to this waveform.

            



.. function:: create_waveform_i16(waveform_data_array)

    Creates an onboard waveform from binary 16-bit signed integer (I16) data
    for use in Arbitrary Waveform or Arbitrary Sequence output mode. The
    **waveformHandle** returned can later be used for setting the active
    waveform, changing the data in the waveform, building sequences of
    waveforms, or deleting the waveform when it is no longer needed.

    

    .. note:: You must call the nifgen\_ConfigureOutputMode function to set the
        **outputMode** parameter to NIFGEN\_VAL\_OUTPUT\_ARB or
        NIFGEN\_VAL\_OUTPUT\_SEQ before calling this function.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].create_waveform_i16(waveform_data_array)


    :param waveform_data_array:


        Specify the array of data that you want to use for the new arbitrary
        waveform. The array must have at least as many elements as the value
        that you specify in the Waveform Size parameter.
        You must normalize the data points in the array to be between -32768 and
        +32767.
        ****Default Value**:** None

        


    :type waveform_data_array: list of int

    :rtype: int
    :return:


            The handle that identifies the new waveform. This handle is used later
            when referring to this waveform.

            



.. function:: define_user_standard_waveform(waveform_data_array)

    Defines a user waveform for use in either Standard Function or Frequency
    List output mode.

    To select the waveform, set the **waveform** parameter to
    NIFGEN\_VAL\_WFM\_USER with either the nifgen\_ConfigureStandardWaveform
    or the nifgen\_CreateFreqList function.

    The waveform data must be scaled between –1.0 and 1.0. Use the
    **amplitude** parameter in the :py:func:`nifgen.configure_standard_waveform`
    function to generate different output voltages.

    

    .. note:: You must call the nifgen\_ConfigureOutputMode function to set the
        **outputMode** parameter to NIFGEN\_VAL\_OUTPUT\_FUNC or
        NIFGEN\_VAL\_OUTPUT\_FREQ\_LIST before calling this function.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].define_user_standard_waveform(waveform_data_array)


    :param waveform_data_array:


        Specifies the array of data you want to use for the new arbitrary
        waveform. The array must have at least as many elements as the value
        that you specify in **waveformSize**.

        You must normalize the data points in the array to be between –1.00 and
        +1.00.

        **Default Value**: None

        


    :type waveform_data_array: list of float

.. function:: delete_named_waveform(waveform_name)

    Removes a previously created arbitrary waveform from the signal
    generator memory and invalidates the waveform handle.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this function.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].delete_named_waveform(waveform_name)


    :param waveform_name:


        Specifies the name to associate with the allocated waveform.

        


    :type waveform_name: string

.. function:: delete_script(script_name)

    Deletes the specified script from onboard memory.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].delete_script(script_name)


    :param script_name:


        Specifies the name of the script you want to delete. The script name
        appears in the text of the script following the script keyword.

        


    :type script_name: string

.. function:: disable()

    Places the instrument in a quiescent state where it has minimal or no
    impact on the system to which it is connected. The analog output and all
    exported signals are disabled.

    



.. function:: export_signal(signal, signal_identifier, output_terminal)

    Routes signals (clocks, triggers, and events) to the output terminal you
    specify.

    Any routes created within a session persist after the session closes to
    prevent signal glitching. To unconfigure signal routes created in
    previous sessions, set **resetDevice** in the :py:func:`nifgen.init` function to
    VI\_TRUE or use the :py:func:`nifgen.reset_device` function.

    If you export a signal with this function and commit the session, the
    signal is routed to the output terminal you specify.

    



    :param signal:


        Specifies the source of the signal to route.
        ****Defined Values****

        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_ONBOARD\_REFERENCE\_CLOCK | Onboard 10 MHz synchronization clock (PCI only)                                                                                                               |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_SYNC\_OUT                 | SYNC OUT signal The SYNC OUT signal is normally generated on the SYNC OUT front panel connector.                                                              |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_START\_TRIGGER            | Start Trigger                                                                                                                                                 |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_MARKER\_EVENT             | Marker Event                                                                                                                                                  |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_SAMPLE\_CLOCK\_TIMEBASE   | The clock from which the Sample Clock is derived                                                                                                              |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_SYNCHRONIZATION           | Synchronization strobe (NI 5404/5411/5431 only) A synchronization strobe is used to guarantee absolute synchronization between two or more signal generators. |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_SAMPLE\_CLOCK             | Sample Clock                                                                                                                                                  |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_REFERENCE\_CLOCK          | PLL Reference Clock                                                                                                                                           |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_SCRIPT\_TRIGGER           | Script Trigger                                                                                                                                                |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_READY\_FOR\_START\_EVENT  | Ready For Start Event                                                                                                                                         |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_STARTED\_EVENT            | Started Event                                                                                                                                                 |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_DONE\_EVENT               | Done Event                                                                                                                                                    |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIFGEN\_VAL\_DATA\_MARKER\_EVENT       | Data Marker Event                                                                                                                                             |
        +----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+


    :type signal: :py:data:`nifgen.Signal`
    :param signal_identifier:


        Specifies which instance of the selected signal to export.
        ****Defined Values****

        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "" (empty string)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "ScriptTrigger0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "ScriptTrigger1"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "ScriptTrigger2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "ScriptTrigger3"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "Marker0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "Marker1"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "Marker2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "Marker3"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "DataMarker0"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "DataMarker1"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "DataMarker2"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | "DataMarker3"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | \* These Data Marker values apply only to single-channel devices or to multichannel devices that are configured for single-channel operation. When using a device that is configured for multichannel operation, specify the channel number along with the signal identifier. For example, to export Data Marker 0 on channel 1 of a device configured for multichannel operation, use the value "1/ DataMarker0." If you do not specify a channel when using a device configured for multichannel generation, DataMarker0 generates on all channels. |
        +-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


    :type signal_identifier: string
    :param output_terminal:


        Specifies the output terminal to export the signal.
        ****Defined Values****

        +-------------------+------------------------------+
        | "" (empty string) | Do not export signal         |
        +-------------------+------------------------------+
        | "PFI0"            | PFI line 0                   |
        +-------------------+------------------------------+
        | "PFI1"            | PFI line 1                   |
        +-------------------+------------------------------+
        | "PFI4"            | PFI line 4                   |
        +-------------------+------------------------------+
        | "PFI5"            | PFI line 5                   |
        +-------------------+------------------------------+
        | "PXI\_Trig0"      | PXI or RTSI line 0           |
        +-------------------+------------------------------+
        | "PXI\_Trig1"      | PXI or RTSI line 1           |
        +-------------------+------------------------------+
        | "PXI\_Trig2"      | PXI or RTSI line 2           |
        +-------------------+------------------------------+
        | "PXI\_Trig3"      | PXI or RTSI line 3           |
        +-------------------+------------------------------+
        | "PXI\_Trig4"      | PXI or RTSI line 4           |
        +-------------------+------------------------------+
        | "PXI\_Trig5"      | PXI or RTSI line 5           |
        +-------------------+------------------------------+
        | "PXI\_Trig6"      | PXI or RTSI line 6           |
        +-------------------+------------------------------+
        | "PXI\_Trig7"      | PXI or RTSI line 7           |
        +-------------------+------------------------------+
        | "DDC\_ClkOut"     | Clock out from DDC connector |
        +-------------------+------------------------------+
        | "PXI\_Star"       | PXI star trigger line        |
        +-------------------+------------------------------+

        .. note:: The following **Defined Values** are examples of possible output
            terminals. For a complete list of the output terminals available on your
            device, refer to the Routes topic for your device or the **Device
            Routes** tab in MAX.


    :type output_terminal: string

.. function:: get_ext_cal_last_date_and_time()

    Returns the date and time of the last successful external calibration.
    The time returned is 24-hour (military) local time; for example, if the
    device was calibrated at 2:30 PM, this function returns 14 for the
    **hour** parameter and 30 for the **minute** parameter.

    



    :rtype: tuple (year, month, day, hour, minute)

        WHERE

        year (int): 


            Specifies the year of the last successful calibration.

            


        month (int): 


            Specifies the month of the last successful calibration.

            


        day (int): 


            Specifies the day of the last successful calibration.

            


        hour (int): 


            Specifies the hour of the last successful calibration.

            


        minute (int): 


            Specifies the minute of the last successful calibration.

            



.. function:: get_ext_cal_last_temp()

    Returns the temperature at the last successful external calibration. The
    temperature is returned in degrees Celsius.

    



    :rtype: float
    :return:


            Specifies the temperature at the last successful calibration in degrees
            Celsius.

            



.. function:: get_ext_cal_recommended_interval()

    Returns the recommended interval between external calibrations in
    months.

    



    :rtype: int
    :return:


            Specifies the recommended interval between external calibrations in
            months.

            



.. function:: get_fir_filter_coefficients()

    | Returns the FIR filter coefficients used by the onboard signal
      processing block. These coefficients are determined by NI-FGEN and
      based on the FIR filter type and corresponding attribute (Alpha,
      Passband, BT) unless you are using the custom filter. If you are using
      a custom filter, the coefficients returned are those set with the
      nifgen\_ConfigureCustomFIRFilterCoefficients function coerced to the
      quantized values used by the device.
    | To use this function, first call an instance of the
      :py:func:`nifgen.get_fir_filter_coefficients` function with the
      **coefficientsArray** parameter set to VI\_NULL. Calling the function
      in this state returns the current size of the **coefficientsArray** as
      the value of the **numberOfCoefficientsRead** parameter. Create an
      array of this size, and call the :py:func:`nifgen.get_fir_filter_coefficients`
      function a second time, passing the new array as the
      **coefficientsArray** parameter and the size as the **arraySize**
      parameter. This second function call populates the array with the FIR
      filter coefficients.
    | Refer to the FIR Filter topic for your device in the *NI Signal
      Generators Help* for more information about FIR filter coefficients.
      This function is supported only for the NI 5441.
    | **Default Value**: None

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].get_fir_filter_coefficients()


    :rtype: int
    :return:


            Specifies the array of data containing the number of coefficients you
            want to read.

            



.. function:: get_hardware_state()

    Returns the current hardware state of the device and, if the device is
    in the hardware error state, the current hardware error.

    

    .. note:: Hardware states do not necessarily correspond to NI-FGEN states.



    :rtype: :py:data:`nifgen.HardwareState`
    :return:


            Returns the hardware state of the signal generator.

            **Defined Values**

            +-------------------------------------------+--------------------------------------------+
            | NIFGEN\_VAL\_IDLE                         | The device is in the Idle state.           |
            +-------------------------------------------+--------------------------------------------+
            | NIFGEN\_VAL\_WAITING\_FOR\_START\_TRIGGER | The device is waiting for Start Trigger.   |
            +-------------------------------------------+--------------------------------------------+
            | NIFGEN\_VAL\_RUNNING                      | The device is in the Running state.        |
            +-------------------------------------------+--------------------------------------------+
            | NIFGEN\_VAL\_DONE                         | The generation has completed successfully. |
            +-------------------------------------------+--------------------------------------------+
            | NIFGEN\_VAL\_HARDWARE\_ERROR              | There is a hardware error.                 |
            +-------------------------------------------+--------------------------------------------+



.. function:: get_self_cal_last_date_and_time()

    Returns the date and time of the last successful self-calibration.

    All values are returned as separate parameters. Each parameter is
    returned as an integer, including the year, month, day, hour, minute,
    and second. For example, if the device is calibrated in September 2013,
    this function returns 9 for the **month** parameter and 2013 for the
    **year** parameter.

    The time returned is 24-hour (military) local time. For example, if the
    device was calibrated at 2:30 PM, this function returns 14 for the
    **hours** parameter and 30 for the **minutes** parameter.

    



    :rtype: tuple (year, month, day, hour, minute)

        WHERE

        year (int): 


            Specifies the year of the last successful calibration.

            


        month (int): 


            Specifies the month of the last successful calibration.

            


        day (int): 


            Specifies the day of the last successful calibration.

            


        hour (int): 


            Specifies the hour of the last successful calibration.

            


        minute (int): 


            Specifies the minute of the last successful calibration.

            



.. function:: get_self_cal_last_temp()

    Returns the temperature at the last successful self-calibration. The
    temperature is returned in degrees Celsius.

    



    :rtype: float
    :return:


            Specifies the temperature at the last successful calibration in degrees
            Celsius.

            



.. function:: get_self_cal_supported()

    Returns whether the device supports self–calibration.

    



    :rtype: bool
    :return:


            Returns whether the device supports self-calibration.

            ****Defined Values****

            +-----------+------------------------------------+
            | VI\_TRUE  | Self–calibration is supported.     |
            +-----------+------------------------------------+
            | VI\_FALSE | Self–calibration is not supported. |
            +-----------+------------------------------------+



.. function:: is_done()

    Determines whether the current generation is complete. This function
    sets the **done** parameter to VI\_TRUE if the session is in the Idle or
    Committed states.

    

    .. note:: NI-FGEN only reports the **done** parameter as VI\_TRUE after the
        current generation is complete in Single trigger mode.



    :rtype: bool
    :return:


            Returns information about the completion of waveform generation.

            **Defined Values**

            +-----------+-----------------------------+
            | VI\_TRUE  | Generation is complete.     |
            +-----------+-----------------------------+
            | VI\_FALSE | Generation is not complete. |
            +-----------+-----------------------------+



.. function:: query_arb_seq_capabilities()

    Returns the attributes of the signal generator that are related to
    creating arbitrary sequences (the :py:data:`nifgen.MAX\_NUM\_SEQUENCES`,
    :py:data:`nifgen.MIN\_SEQUENCE\_LENGTH`,
    :py:data:`nifgen.MAX\_SEQUENCE\_LENGTH`, and :py:data:`nifgen.MAX\_LOOP\_COUNT`
    attributes).

    



    :rtype: tuple (maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count)

        WHERE

        maximum_number_of_sequences (int): 


            Returns the maximum number of arbitrary waveform sequences that the
            signal generator allows. NI-FGEN obtains this value from the
            :py:data:`nifgen.MAX\_NUM\_SEQUENCES` attribute.

            


        minimum_sequence_length (int): 


            Returns the minimum number of arbitrary waveforms the signal generator
            allows in a sequence. NI-FGEN obtains this value from the
            :py:data:`nifgen.MIN\_SEQUENCE\_LENGTH` attribute.

            


        maximum_sequence_length (int): 


            Returns the maximum number of arbitrary waveforms the signal generator
            allows in a sequence. NI-FGEN obtains this value from the
            :py:data:`nifgen.MAX\_SEQUENCE\_LENGTH` attribute.

            


        maximum_loop_count (int): 


            Returns the maximum number of times the signal generator can repeat an
            arbitrary waveform in a sequence. NI-FGEN obtains this value from the
            :py:data:`nifgen.MAX\_LOOP\_COUNT` attribute.

            



.. function:: query_arb_wfm_capabilities()

    Returns the attributes of the signal generator that are related to
    creating arbitrary waveforms. These attributes are the maximum number of
    waveforms, waveform quantum, minimum waveform size, and maximum waveform
    size.

    

    .. note:: If you do not want to obtain the waveform quantum, pass a value of
        VI\_NULL for this parameter.



    :rtype: tuple (maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size)

        WHERE

        maximum_number_of_waveforms (int): 


            Returns the maximum number of arbitrary waveforms that the signal
            generator allows. NI-FGEN obtains this value from the
            :py:data:`nifgen.MAX\_NUM\_WAVEFORMS` attribute.

            


        waveform_quantum (int): 


            The size (number of points) of each waveform must be a multiple of a
            constant quantum value. This parameter obtains the quantum value that
            the signal generator uses. NI-FGEN returns this value from the
            :py:data:`nifgen.WAVEFORM\_QUANTUM` attribute.

            For example, when this attribute returns a value of 8, all waveform
            sizes must be a multiple of 8.

            


        minimum_waveform_size (int): 


            Returns the minimum number of points that the signal generator allows in
            a waveform. NI-FGEN obtains this value from the
            :py:data:`nifgen.MIN\_WAVEFORM\_SIZE` attribute.

            


        maximum_waveform_size (int): 


            Returns the maximum number of points that the signal generator allows in
            a waveform. NI-FGEN obtains this value from the
            :py:data:`nifgen.MAX\_WAVEFORM\_SIZE` attribute.

            



.. function:: query_freq_list_capabilities()

    Returns the attributes of the signal generator that are related to
    creating frequency lists. These attributes are
    :py:data:`nifgen.MAX\_NUM\_FREQ\_LISTS`,
    :py:data:`nifgen.MIN\_FREQ\_LIST\_LENGTH`,
    :py:data:`nifgen.MAX\_FREQ\_LIST\_LENGTH`,
    :py:data:`nifgen.MIN\_FREQ\_LIST\_DURATION`,
    :py:data:`nifgen.MAX\_FREQ\_LIST\_DURATION`, and
    :py:data:`nifgen.FREQ\_LIST\_DURATION\_QUANTUM`.

    



    :rtype: tuple (maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum)

        WHERE

        maximum_number_of_freq_lists (int): 


            Returns the maximum number of frequency lists that the signal generator
            allows. NI-FGEN obtains this value from the
            :py:data:`nifgen.MAX\_NUM\_FREQ\_LISTS` attribute.

            


        minimum_frequency_list_length (int): 


            Returns the minimum number of steps that the signal generator allows in
            a frequency list. NI-FGEN obtains this value from the
            :py:data:`nifgen.MIN\_FREQ\_LIST\_LENGTH` attribute.

            


        maximum_frequency_list_length (int): 


            Returns the maximum number of steps that the signal generator allows in
            a frequency list. NI-FGEN obtains this value from the
            :py:data:`nifgen.MAX\_FREQ\_LIST\_LENGTH` attribute.

            


        minimum_frequency_list_duration (float): 


            Returns the minimum duration that the signal generator allows in a step
            of a frequency list. NI-FGEN obtains this value from the
            :py:data:`nifgen.MIN\_FREQ\_LIST\_DURATION` attribute.

            


        maximum_frequency_list_duration (float): 


            Returns the maximum duration that the signal generator allows in a step
            of a frequency list. NI-FGEN obtains this value from the
            :py:data:`nifgen.MAX\_FREQ\_LIST\_DURATION` attribute.

            


        frequency_list_duration_quantum (float): 


            Returns the quantum of which all durations must be a multiple in a
            frequency list. NI-FGEN obtains this value from the
            :py:data:`nifgen.FREQ\_LIST\_DURATION\_QUANTUM` attribute.

            



.. function:: read_current_temperature()

    Reads the current onboard temperature of the device. The temperature is
    returned in degrees Celsius.

    



    :rtype: float
    :return:


            Returns the current temperature read from onboard temperature sensors,
            in degrees Celsius.

            



.. function:: reset_device()

    Performs a hard reset on the device. Generation is stopped, all routes
    are released, external bidirectional terminals are tristated, FPGAs are
    reset, hardware is configured to its default state, and all session
    attributes are reset to their default states.

    



.. function:: reset_with_defaults()

    Resets the instrument and reapplies initial user–specified settings from
    the logical name that was used to initialize the session. If the session
    was created without a logical name, this function is equivalent to the
    nifgen\_reset function.

    



.. function:: self_cal()

    Performs a full internal self-calibration on the device. If the
    calibration is successful, new calibration data and constants are stored
    in the onboard EEPROM.

    



.. function:: send_software_edge_trigger(trigger, trigger_id)

    Sends a command to trigger the signal generator. This VI can act as an
    override for an external edge trigger.

    

    .. note:: This VI does not override external digital edge triggers of the
        NI 5401/5411/5431.



    :param trigger:


        Sets the clock mode of the signal generator.

        ****Defined Values****

        +-------------------------------+
        | NIFGEN\_VAL\_DIVIDE\_DOWN     |
        +-------------------------------+
        | NIFGEN\_VAL\_HIGH\_RESOLUTION |
        +-------------------------------+
        | NIFGEN\_VAL\_AUTOMATIC        |
        +-------------------------------+


    :type trigger: :py:data:`nifgen.Trigger`
    :param trigger_id:

    :type trigger_id: string

.. function:: set_named_waveform_next_write_position(waveform_name, relative_to, offset)

    Sets the position in the waveform to which data is written at the next
    write. This function allows you to write to arbitrary locations within
    the waveform. These settings apply only to the next write to the
    waveform specified by the **waveformHandle** parameter. Subsequent
    writes to that waveform begin where the last write left off, unless this
    function is called again. The **waveformHandle** passed in must have
    been created with a call to one of the following functions:

    -  nifgen\_AllocateWaveform
    -  nifgen\_CreateWaveformF64
    -  nifgen\_CreateWaveformI16
    -  nifgen\_CreateWaveformFromFileI16
    -  nifgen\_CreateWaveformFromFileF64
    -  nifgen\_CreateWaveformFromFileHWS

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].set_named_waveform_next_write_position(waveform_name, relative_to, offset)


    :param waveform_name:


        Specifies the name to associate with the allocated waveform.

        


    :type waveform_name: string
    :param relative_to:


        Specifies the reference position in the waveform. This position and
        **offset** together determine where to start loading data into the
        waveform.

        ****Defined Values****

        +----------------------------------------------+-------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WAVEFORM\_POSITION\_START (0)   | Use the start of the waveform as the reference position.                |
        +----------------------------------------------+-------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WAVEFORM\_POSITION\_CURRENT (1) | Use the current position within the waveform as the reference position. |
        +----------------------------------------------+-------------------------------------------------------------------------+


    :type relative_to: :py:data:`nifgen.RelativeTo`
    :param offset:


        Specifies the offset from the **relativeTo** parameter at which to start
        loading the data into the waveform.

        


    :type offset: int

.. function:: set_waveform_next_write_position(waveform_handle, relative_to, offset)

    Sets the position in the waveform at which the next waveform data is
    written. This function allows you to write to arbitrary locations within
    the waveform. These settings apply only to the next write to the
    waveform specified by the waveformHandle parameter. Subsequent writes to
    that waveform begin where the last write left off, unless this function
    is called again. The waveformHandle passed in must have been created by
    a call to the nifgen\_AllocateWaveform function or one of the following
    niFgen CreateWaveform functions:

    -  nifgen\_CreateWaveformF64
    -  nifgen\_CreateWaveformI16
    -  nifgen\_CreateWaveformFromFileI16
    -  nifgen\_CreateWaveformFromFileF64
    -  nifgen\_CreateWaveformFromFileHWS

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].set_waveform_next_write_position(waveform_handle, relative_to, offset)


    :param waveform_handle:


        Specifies the handle of the arbitrary waveform previously allocated with
        the nifgen\_AllocateWaveform function.

        


    :type waveform_handle: int
    :param relative_to:


        Specifies the reference position in the waveform. This position and
        **offset** together determine where to start loading data into the
        waveform.

        ****Defined Values****

        +----------------------------------------------+-------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WAVEFORM\_POSITION\_START (0)   | Use the start of the waveform as the reference position.                |
        +----------------------------------------------+-------------------------------------------------------------------------+
        | NIFGEN\_VAL\_WAVEFORM\_POSITION\_CURRENT (1) | Use the current position within the waveform as the reference position. |
        +----------------------------------------------+-------------------------------------------------------------------------+


    :type relative_to: :py:data:`nifgen.RelativeTo`
    :param offset:


        Specifies the offset from **relativeTo** at which to start loading the
        data into the waveform.

        


    :type offset: int

.. function:: wait_until_done(max_time=10000)

    Waits until the device is done generating or until the maximum time has
    expired.

    



    :param max_time:


        Specifies the timeout value in milliseconds.

        


    :type max_time: int

.. function:: write_binary16_waveform(waveform_handle, data)

    Writes binary data to the waveform in onboard memory. The waveform
    handle passed must have been created by a call to the
    nifgen\_AllocateWaveform or the nifgen\_CreateWaveformI16 function.

    By default, the subsequent call to the :py:func:`nifgen.write_binary16_waveform`
    function continues writing data from the position of the last sample
    written. You can set the write position and offset by calling the
    nifgen\_SetWaveformNextWritePosition function. If streaming is enabled,
    you can write more data than the allocated waveform size in onboard
    memory. Refer to the
    `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
    information about streaming data.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].write_binary16_waveform(waveform_handle, data)


    :param waveform_handle:


        Specifies the handle of the arbitrary waveform previously allocated with
        the nifgen\_AllocateWaveform function.

        


    :type waveform_handle: int
    :param data:


        Specifies the array of data to load into the waveform. The array must
        have at least as many elements as the value in **size**. The binary data
        is left-justified.

        


    :type data: list of int

.. function:: write_named_waveform_f64(waveform_name, data)

    Writes floating-point data to the waveform in onboard memory. The
    waveform handle passed in must have been created by a call to the
    nifgen\_AllocateWaveform function or to one of the following niFgen
    Create Waveform functions:

    -  nifgen\_CreateWaveformF64
    -  nifgen\_CreateWaveformI16
    -  nifgen\_CreateWaveformFromFileI16
    -  nifgen\_CreateWaveformFromFileF64
    -  nifgen\_CreateWaveformFromFileHWS

    By default, the subsequent call to the :py:func:`nifgen.write_named_waveform_f64`
    function continues writing data from the position of the last sample
    written. You can set the write position and offset by calling the
    nifgen\_SetNamedWaveformNextWritePosition function. If streaming is
    enabled, you can write more data than the allocated waveform size in
    onboard memory. Refer to the
    `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
    information about streaming data.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].write_named_waveform_f64(waveform_name, data)


    :param waveform_name:


        Specifies the name to associate with the allocated waveform.

        


    :type waveform_name: string
    :param data:


        Specifies the array of data to load into the waveform. The array must
        have at least as many elements as the value in **size**.

        


    :type data: list of float

.. function:: write_named_waveform_i16(waveform_name, data)

    Writes binary data to the named waveform in onboard memory.

    By default, the subsequent call to the :py:func:`nifgen.write_named_waveform_i16`
    function continues writing data from the position of the last sample
    written. You can set the write position and offset by calling the
    nifgen\_SetNamedWaveformNextWritePosition function. If streaming is
    enabled, you can write more data than the allocated waveform size in
    onboard memory. Refer to the
    `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
    information about streaming data.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].write_named_waveform_i16(waveform_name, data)


    :param waveform_name:


        Specifies the name to associate with the allocated waveform.

        


    :type waveform_name: string
    :param data:


        Specifies the array of data to load into the waveform. The array must
        have at least as many elements as the value in **size**.

        


    :type data: list of int

.. function:: write_script(script)

    Writes a string containing one or more scripts that govern the
    generation of waveforms.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].write_script(script)


    :param script:


        Contains the text of the script you want to use for your generation
        operation. Refer to `scripting
        Instructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__
        for more information about writing scripts.

        


    :type script: string

.. function:: write_waveform(waveform_handle, data)

    Writes floating-point data to the waveform in onboard memory. The
    waveform handle passed in must have been created by a call to the
    nifgen\_AllocateWaveform function or one of the following niFgen
    CreateWaveform functions:

    -  nifgen\_CreateWaveformF64
    -  nifgen\_CreateWaveformI16
    -  nifgen\_CreateWaveformFromFileI16
    -  nifgen\_CreateWaveformFromFileF64
    -  nifgen\_CreateWaveformFromFileHWS

    By default, the subsequent call to the :py:func:`nifgen.write_waveform` function
    continues writing data from the position of the last sample written. You
    can set the write position and offset by calling the
    nifgen\_SetWaveformNextWritePosition function. If streaming is enabled,
    you can write more data than the allocated waveform size in onboard
    memory. Refer to the
    `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
    information about streaming data.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].write_waveform(waveform_handle, data)


    :param waveform_handle:


        Specifies the handle of the arbitrary waveform previously allocated with
        the nifgen\_AllocateWaveform function.

        


    :type waveform_handle: int
    :param data:


        Specifies the array of data to load into the waveform. The array must
        have at least as many elements as the value in **size**.

        


    :type data: list of float

.. function:: reset()

    Resets the instrument to a known state. This function aborts the
    generation, clears all routes, and resets session attributes to the
    default values. This function does not, however, commit the session
    properties or configure the device hardware to its default state.

    

    .. note:: For the NI 5401/5404/5411/5431, this function exhibits the same
        behavior as the nifgen\_ResetDevice function.



.. function:: self_test()

    Runs the instrument self-test routine and returns the test result(s).

    

    .. note:: When used on some signal generators, the device is reset after the
        :py:func:`nifgen.self_test` function runs. If you use the :py:func:`nifgen.self_test`
        function, your device may not be in its previously configured state
        after the function runs.



    :rtype: tuple (self_test_result, self_test_message)

        WHERE

        self_test_result (int): 


            Contains the value returned from the instrument self-test. A value of 0
            indicates success.

            +----------------+------------------+
            | Self-Test Code | Description      |
            +================+==================+
            | 0              | Passed self-test |
            +----------------+------------------+
            | 1              | Self-test failed |
            +----------------+------------------+


        self_test_message (string): 


            Returns the self-test response string from the instrument.

            You must pass a ViChar array with at least 256 bytes.

            




