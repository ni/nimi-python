nifgen.Session methods
======================

.. py:currentmodule:: nifgen.Session

.. py:method:: abort()

    Aborts any previously initiated signal generation. Call the
    nifgen_InitiateGeneration method to cause the signal generator to
    produce a signal again.

    



.. py:method:: allocate_named_waveform(waveform_name, waveform_size)

    Specifies the size of a named waveform up front so that it can be
    allocated in onboard memory before loading the associated data. Data can
    then be loaded in smaller blocks with the niFgen Write (Binary16)
    Waveform methods.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].allocate_named_waveform(waveform_name, waveform_size)


    :param waveform_name:


        Specifies the name to associate with the allocated waveform.

        


    :type waveform_name: str
    :param waveform_size:


        Specifies the size of the waveform to allocate in samples.

        **Default Value**: "4096"

        


    :type waveform_size: int

.. py:method:: allocate_waveform(waveform_size)

    Specifies the size of a waveform so that it can be allocated in onboard
    memory before loading the associated data. Data can then be loaded in
    smaller blocks with the Write Binary 16 Waveform methods.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this method.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].allocate_waveform(waveform_size)


    :param waveform_size:


        Specifies, in samples, the size of the waveform to allocate.

        


    :type waveform_size: int

    :rtype: int
    :return:


            The handle that identifies the new waveform. This handle is used later
            when referring to this waveform.

            



.. py:method:: clear_arb_memory()

    Removes all previously created arbitrary waveforms, sequences, and
    scripts from the signal generator memory and invalidates all waveform
    handles, sequence handles, and waveform names.

    

    .. note:: The signal generator must not be in the Generating state when you
        call this method.



.. py:method:: clear_arb_sequence(sequence_handle)

    Removes a previously created arbitrary sequence from the signal
    generator memory and invalidates the sequence handle.

    

    .. note:: The signal generator must not be in the Generating state when you
        call this method.



    :param sequence_handle:


        Specifies the handle of the arbitrary sequence that you want the signal
        generator to remove. You can create an arbitrary sequence using the
        nifgen_CreateArbSequence or nifgen_CreateAdvancedArbSequence method.
        These methods return a handle that you use to identify the sequence.

        | **Defined Value**:
        | :py:data:`~nifgen.NIFGEN_VAL_ALL_SEQUENCES`—Remove all sequences from the signal
          generator

        **Default Value**: None

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type sequence_handle: int

.. py:method:: clear_arb_waveform(waveform_handle)

    Removes a previously created arbitrary waveform from the signal
    generator memory and invalidates the waveform handle.

    

    .. note:: The signal generator must not be in the Generating state when you
        call this method.



    :param waveform_handle:


        Specifies the handle of the arbitrary waveform that you want the signal
        generator to remove.

        You can create multiple arbitrary waveforms using one of the following
        niFgen Create Waveform methods:

        -  :py:meth:`nifgen.Session.create_waveform`
        -  :py:meth:`nifgen.Session.create_waveform`
        -  :py:meth:`nifgen.Session.create_waveform_from_file_i16`
        -  :py:meth:`nifgen.Session.create_waveform_from_file_f64`
        -  :py:meth:`nifgen.Session.CreateWaveformFromFileHWS`

        **Defined Value**:

        :py:data:`~nifgen.NIFGEN_VAL_ALL_WAVEFORMS`—Remove all waveforms from the signal
        generator.

        **Default Value**: None

        

        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type waveform_handle: int

.. py:method:: clear_freq_list(frequency_list_handle)

    Removes a previously created frequency list from the signal generator
    memory and invalidates the frequency list handle.

    

    .. note:: The signal generator must not be in the Generating state when you
        call this method.



    :param frequency_list_handle:


        Specifies the handle of the frequency list you want the signal generator
        to remove. You create multiple frequency lists using
        :py:meth:`nifgen.Session.create_freq_list`. :py:meth:`nifgen.Session.create_freq_list` returns a handle that you
        use to identify each list. Specify a value of -1 to clear all frequency
        lists.

        **Defined Value**

        :py:data:`~nifgen.NIFGEN_VAL_ALL_FLISTS`—Remove all frequency lists from the signal
        generator.

        **Default Value**: None

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type frequency_list_handle: int

.. py:method:: clear_user_standard_waveform()

    Clears the user-defined waveform created by the
    nifgen_DefineUserStandardWaveform method.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].clear_user_standard_waveform()


.. py:method:: commit()

    Causes a transition to the Committed state. This method verifies
    property values, reserves the device, and commits the property values
    to the device. If the property values are all valid, NI-FGEN sets the
    device hardware configuration to match the session configuration. This
    method does not support the NI 5401/5404/5411/5431 signal generators.

    In the Committed state, you can load waveforms, scripts, and sequences
    into memory. If any properties are changed, NI-FGEN implicitly
    transitions back to the Idle state, where you can program all session
    properties before applying them to the device. This method has no
    effect if the device is already in the Committed or Generating state and
    returns a successful status value.

    Calling this VI before the niFgen Initiate Generation VI is optional but
    has the following benefits:

    -  Routes are committed, so signals are exported or imported.
    -  Any Reference Clock and external clock circuits are phase-locked.
    -  A subsequent :py:meth:`nifgen.Session._initiate_generation` method can run faster
       because the device is already configured.

    



.. py:method:: configure_arb_sequence(sequence_handle, gain, offset)

    Configures the signal generator properties that affect arbitrary
    sequence generation. Sets the :py:data:`nifgen.Session.arb_sequence_handle`,
    :py:data:`nifgen.Session.arb_gain`, and :py:data:`nifgen.Session.arb_offset` properties.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this method.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].configure_arb_sequence(sequence_handle, gain, offset)


    :param sequence_handle:


        Specifies the handle of the arbitrary sequence that you want the signal
        generator to produce. NI-FGEN sets the
        :py:data:`nifgen.Session.arb_sequence_handle` property to this value. You can
        create an arbitrary sequence using the :py:meth:`nifgen.Session.create_arb_sequence` or
        :py:meth:`nifgen.Session.create_advanced_arb_sequence` method. These methods return a
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
        :py:data:`nifgen.Session.arb_offset` property to this value.

        For example, to configure the output signal to range from 0.00 to 2.00 V
        instead of –1.00 to 1.00 V, set the offset to 1.00.

        **Units**: volts

        **Default Value**: None

        


    :type offset: float

.. py:method:: configure_arb_waveform(waveform_handle, gain, offset)

    Configures the properties of the signal generator that affect arbitrary
    waveform generation. Sets the :py:data:`nifgen.Session.arb_waveform_handle`,
    :py:data:`nifgen.Session.arb_gain`, and :py:data:`nifgen.Session.arb_offset` properties.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this method.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].configure_arb_waveform(waveform_handle, gain, offset)


    :param waveform_handle:


        Specifies the handle of the arbitrary waveform you want the signal
        generator to produce. NI-FGEN sets the
        :py:data:`nifgen.Session.arb_waveform_handle` property to this value. You can
        create an arbitrary waveform using one of the following niFgen Create
        Waveform methods:

        -  :py:meth:`nifgen.Session.create_waveform`
        -  :py:meth:`nifgen.Session.create_waveform`
        -  :py:meth:`nifgen.Session.create_waveform_from_file_i16`
        -  :py:meth:`nifgen.Session.create_waveform_from_file_f64`
        -  :py:meth:`nifgen.Session.CreateWaveformFromFileHWS`

        These methods return a handle that you use to identify the waveform.

        **Default Value**: None

        

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


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
        :py:data:`nifgen.Session.arb_offset` property to this value.

        For example, to configure the output signal to range from 0.00 to 2.00 V
        instead of –1.00 to 1.00 V, set the offset to 1.00.

        **Units**: volts

        **Default Value**: None

        


    :type offset: float

.. py:method:: configure_custom_fir_filter_coefficients(coefficients_array)

    Sets the FIR filter coefficients used by the onboard signal processing
    block. The values are coerced to the closest settings achievable by the
    signal generator.

    Refer to the *FIR Filter* topic for your device in the *NI Signal
    Generators Help* for more information about FIR filter coefficients.
    This method is supported only for the NI 5441.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this method.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].configure_custom_fir_filter_coefficients(coefficients_array)


    :param coefficients_array:


        Specifies the array of data the onboard signal processor uses for the
        FIR filter coefficients. For the NI 5441, provide a symmetric array of
        95 coefficients to this parameter. The array must have at least as many
        elements as the value that you specify in the **numberOfCoefficients**
        parameter in this method.
        The coefficients should range between –1.00 and +1.00.

        


    :type coefficients_array: list of float

.. py:method:: configure_digital_edge_script_trigger(source, edge=nifgen.ScriptTriggerDigitalEdgeEdge.RISING)

    Configures the specified Script Trigger for digital edge triggering.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].configure_digital_edge_script_trigger(source, edge=nifgen.ScriptTriggerDigitalEdgeEdge.RISING)


    :param source:


        Specifies which trigger source the signal generator uses.

        **Defined Values**

        **Default Value**: "PFI0"

        +-------------+-----------------------------------+
        | "PFI0"      | PFI 0                             |
        +-------------+-----------------------------------+
        | "PFI1"      | PFI 1                             |
        +-------------+-----------------------------------+
        | "PFI2"      | PFI 2                             |
        +-------------+-----------------------------------+
        | "PFI3"      | PFI 3                             |
        +-------------+-----------------------------------+
        | "PFI4"      | PFI 4                             |
        +-------------+-----------------------------------+
        | "PFI5"      | PFI 5                             |
        +-------------+-----------------------------------+
        | "PFI6"      | PFI 6                             |
        +-------------+-----------------------------------+
        | "PFI7"      | PFI 7                             |
        +-------------+-----------------------------------+
        | "PXI_Trig0" | PXI trigger line 0 or RTSI line 0 |
        +-------------+-----------------------------------+
        | "PXI_Trig1" | PXI trigger line 1 or RTSI line 1 |
        +-------------+-----------------------------------+
        | "PXI_Trig2" | PXI trigger line 2 or RTSI line 2 |
        +-------------+-----------------------------------+
        | "PXI_Trig3" | PXI trigger line 3 or RTSI line 3 |
        +-------------+-----------------------------------+
        | "PXI_Trig4" | PXI trigger line 4 or RTSI line 4 |
        +-------------+-----------------------------------+
        | "PXI_Trig5" | PXI trigger line 5 or RTSI line 5 |
        +-------------+-----------------------------------+
        | "PXI_Trig6" | PXI trigger line 6 or RTSI line 6 |
        +-------------+-----------------------------------+
        | "PXI_Trig7" | PXI trigger line 7 or RTSI line 7 |
        +-------------+-----------------------------------+
        | "PXI_Star"  | PXI star trigger line             |
        +-------------+-----------------------------------+


    :type source: str
    :param edge:


        Specifies the edge to detect.

        ****Defined Values****

        ****Default Value**:** :py:data:`~nifgen.ScriptTriggerDigitalEdgeEdge.RISING`

        +---------------------------------------------------------+------------------------------------------------------------------+
        | :py:data:`~nifgen.ScriptTriggerDigitalEdgeEdge.RISING`  | Occurs when the signal transitions from low level to high level. |
        +---------------------------------------------------------+------------------------------------------------------------------+
        | :py:data:`~nifgen.ScriptTriggerDigitalEdgeEdge.FALLING` | Occurs when the signal transitions from high level to low level. |
        +---------------------------------------------------------+------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type edge: :py:data:`nifgen.ScriptTriggerDigitalEdgeEdge`

.. py:method:: configure_digital_edge_start_trigger(source, edge=nifgen.StartTriggerDigitalEdgeEdge.RISING)

    Configures the Start Trigger for digital edge triggering.

    



    :param source:


        Specifies which trigger source the signal generator uses.

        **Defined Values**

        **Default Value**: "PFI0"

        +-------------+-----------------------------------+
        | "PFI0"      | PFI 0                             |
        +-------------+-----------------------------------+
        | "PFI1"      | PFI 1                             |
        +-------------+-----------------------------------+
        | "PFI2"      | PFI 2                             |
        +-------------+-----------------------------------+
        | "PFI3"      | PFI 3                             |
        +-------------+-----------------------------------+
        | "PFI4"      | PFI 4                             |
        +-------------+-----------------------------------+
        | "PFI5"      | PFI 5                             |
        +-------------+-----------------------------------+
        | "PFI6"      | PFI 6                             |
        +-------------+-----------------------------------+
        | "PFI7"      | PFI 7                             |
        +-------------+-----------------------------------+
        | "PXI_Trig0" | PXI trigger line 0 or RTSI line 0 |
        +-------------+-----------------------------------+
        | "PXI_Trig1" | PXI trigger line 1 or RTSI line 1 |
        +-------------+-----------------------------------+
        | "PXI_Trig2" | PXI trigger line 2 or RTSI line 2 |
        +-------------+-----------------------------------+
        | "PXI_Trig3" | PXI trigger line 3 or RTSI line 3 |
        +-------------+-----------------------------------+
        | "PXI_Trig4" | PXI trigger line 4 or RTSI line 4 |
        +-------------+-----------------------------------+
        | "PXI_Trig5" | PXI trigger line 5 or RTSI line 5 |
        +-------------+-----------------------------------+
        | "PXI_Trig6" | PXI trigger line 6 or RTSI line 6 |
        +-------------+-----------------------------------+
        | "PXI_Trig7" | PXI trigger line 7 or RTSI line 7 |
        +-------------+-----------------------------------+
        | "PXI_Star"  | PXI star trigger line             |
        +-------------+-----------------------------------+


    :type source: str
    :param edge:


        Specifies the edge to detect.

        ****Defined Values****

        ****Default Value**:** :py:data:`~nifgen.StartTriggerDigitalEdgeEdge.RISING`

        +--------------------------------------------------------+------------------------------------------------------------------+
        | :py:data:`~nifgen.StartTriggerDigitalEdgeEdge.RISING`  | Occurs when the signal transitions from low level to high level. |
        +--------------------------------------------------------+------------------------------------------------------------------+
        | :py:data:`~nifgen.StartTriggerDigitalEdgeEdge.FALLING` | Occurs when the signal transitions from high level to low level. |
        +--------------------------------------------------------+------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type edge: :py:data:`nifgen.StartTriggerDigitalEdgeEdge`

.. py:method:: configure_digital_level_script_trigger(source, trigger_when)

    Configures the specified Script Trigger for digital level triggering.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].configure_digital_level_script_trigger(source, trigger_when)


    :param source:


        Specifies which trigger source the signal generator uses.

        **Defined Values**

        **Default Value**: "PFI0"

        +-------------+-----------------------------------+
        | "PFI0"      | PFI 0                             |
        +-------------+-----------------------------------+
        | "PFI1"      | PFI 1                             |
        +-------------+-----------------------------------+
        | "PFI2"      | PFI 2                             |
        +-------------+-----------------------------------+
        | "PFI3"      | PFI 3                             |
        +-------------+-----------------------------------+
        | "PFI4"      | PFI 4                             |
        +-------------+-----------------------------------+
        | "PFI5"      | PFI 5                             |
        +-------------+-----------------------------------+
        | "PFI6"      | PFI 6                             |
        +-------------+-----------------------------------+
        | "PFI7"      | PFI 7                             |
        +-------------+-----------------------------------+
        | "PXI_Trig0" | PXI trigger line 0 or RTSI line 0 |
        +-------------+-----------------------------------+
        | "PXI_Trig1" | PXI trigger line 1 or RTSI line 1 |
        +-------------+-----------------------------------+
        | "PXI_Trig2" | PXI trigger line 2 or RTSI line 2 |
        +-------------+-----------------------------------+
        | "PXI_Trig3" | PXI trigger line 3 or RTSI line 3 |
        +-------------+-----------------------------------+
        | "PXI_Trig4" | PXI trigger line 4 or RTSI line 4 |
        +-------------+-----------------------------------+
        | "PXI_Trig5" | PXI trigger line 5 or RTSI line 5 |
        +-------------+-----------------------------------+
        | "PXI_Trig6" | PXI trigger line 6 or RTSI line 6 |
        +-------------+-----------------------------------+
        | "PXI_Trig7" | PXI trigger line 7 or RTSI line 7 |
        +-------------+-----------------------------------+
        | "PXI_Star"  | PXI star trigger line             |
        +-------------+-----------------------------------+


    :type source: str
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


    :type trigger_when: :py:data:`nifgen.TriggerWhen`

.. py:method:: configure_freq_list(frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0)

    Configures the properties of the signal generator that affect frequency
    list generation (the :py:data:`nifgen.Session.freq_list_handle`,
    :py:data:`nifgen.Session.func_amplitude`, :py:data:`nifgen.Session.func_dc_offset`, and
    :py:data:`nifgen.Session.func_start_phase` properties).

    

    .. note:: The signal generator must not be in the Generating state when you call
        this method.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].configure_freq_list(frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0)


    :param frequency_list_handle:


        Specifies the handle of the frequency list that you want the signal
        generator to produce. NI-FGEN sets the :py:data:`nifgen.Session.freq_list_handle`
        property to this value. You can create a frequency list using the
        :py:meth:`nifgen.Session.create_freq_list` method, which returns a handle that you use to
        identify the list.
        **Default Value**: None

        


    :type frequency_list_handle: int
    :param amplitude:


        Specifies the amplitude of the standard waveform that you want the
        signal generator to produce. This value is the amplitude at the output
        terminal. NI-FGEN sets the :py:data:`nifgen.Session.func_amplitude` property to
        this value.

        For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
        the amplitude to 10.00 V.

        **Units**: peak-to-peak voltage

        **Default Value**: None

        

        .. note:: This parameter does not affect signal generator behavior when you set
            the **waveform** parameter of the :py:meth:`nifgen.Session.configure_standard_waveform`
            method to :py:data:`~nifgen.Waveform.DC`.


    :type amplitude: float
    :param dc_offset:


        Specifies the DC offset of the standard waveform that you want the
        signal generator to produce. The value is the offset from ground to the
        center of the waveform you specify with the **waveform** parameter,
        observed at the output terminal. For example, to configure a waveform
        with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
        **dcOffset** to 5.00 V. NI-FGEN sets the :py:data:`nifgen.Session.func_dc_offset`
        property to this value.

        **Units**: volts

        **Default Value**: None

        


    :type dc_offset: float
    :param start_phase:


        Specifies the horizontal offset of the standard waveform you want the
        signal generator to produce. Specify this property in degrees of one
        waveform cycle. NI-FGEN sets the :py:data:`nifgen.Session.func_start_phase`
        property to this value. A start phase of 180 degrees means output
        generation begins halfway through the waveform. A start phase of 360
        degrees offsets the output by an entire waveform cycle, which is
        identical to a start phase of 0 degrees.

        **Units**: degrees of one cycle

        **Default Value**: None degrees

        

        .. note:: This parameter does not affect signal generator behavior when you set
            the **waveform** parameter to :py:data:`~nifgen.Waveform.DC`.


    :type start_phase: float

.. py:method:: configure_standard_waveform(waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0)

    Configures the following properties of the signal generator that affect
    standard waveform generation:

    -  :py:data:`nifgen.Session.func_waveform`
    -  :py:data:`nifgen.Session.func_amplitude`
    -  :py:data:`nifgen.Session.func_dc_offset`
    -  :py:data:`nifgen.Session.func_frequency`
    -  :py:data:`nifgen.Session.func_start_phase`

    

    .. note:: You must call the :py:meth:`nifgen.Session.ConfigureOutputMode` method with the
        **outputMode** parameter set to :py:data:`~nifgen.OutputMode.FUNC` before calling
        this method.

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].configure_standard_waveform(waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0)


    :param waveform:


        Specifies the standard waveform that you want the signal generator to
        produce. NI-FGEN sets the :py:data:`nifgen.Session.func_waveform` property to this
        value.

        ****Defined Values****

        **Default Value**: :py:data:`~nifgen.Waveform.SINE`

        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.SINE`      | Specifies that the signal generator produces a sinusoid waveform.                                                                  |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.SQUARE`    | Specifies that the signal generator produces a square waveform.                                                                    |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.TRIANGLE`  | Specifies that the signal generator produces a triangle waveform.                                                                  |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.RAMP_UP`   | Specifies that the signal generator produces a positive ramp waveform.                                                             |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.RAMP_DOWN` | Specifies that the signal generator produces a negative ramp waveform.                                                             |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.DC`        | Specifies that the signal generator produces a constant voltage.                                                                   |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.NOISE`     | Specifies that the signal generator produces white noise.                                                                          |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.USER`      | Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform method. |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+


    :type waveform: :py:data:`nifgen.Waveform`
    :param amplitude:


        Specifies the amplitude of the standard waveform that you want the
        signal generator to produce. This value is the amplitude at the output
        terminal. NI-FGEN sets the :py:data:`nifgen.Session.func_amplitude` property to
        this value.

        For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
        the amplitude to 10.00 V.

        **Units**: peak-to-peak voltage

        **Default Value**: None

        

        .. note:: This parameter does not affect signal generator behavior when you set
            the **waveform** parameter of the :py:meth:`nifgen.Session.configure_standard_waveform`
            method to :py:data:`~nifgen.Waveform.DC`.


    :type amplitude: float
    :param frequency:


        | Specifies the frequency of the standard waveform that you want the
          signal generator to produce. NI-FGEN sets the
          :py:data:`nifgen.Session.func_frequency` property to this value.

        **Units**: hertz

        **Default Value**: None

        

        .. note:: This parameter does not affect signal generator behavior when you set
            the **waveform** parameter of the :py:meth:`nifgen.Session.configure_standard_waveform`
            method to :py:data:`~nifgen.Waveform.DC`.


    :type frequency: float
    :param dc_offset:


        Specifies the DC offset of the standard waveform that you want the
        signal generator to produce. The value is the offset from ground to the
        center of the waveform you specify with the **waveform** parameter,
        observed at the output terminal. For example, to configure a waveform
        with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
        **dcOffset** to 5.00 V. NI-FGEN sets the :py:data:`nifgen.Session.func_dc_offset`
        property to this value.

        **Units**: volts

        **Default Value**: None

        


    :type dc_offset: float
    :param start_phase:


        Specifies the horizontal offset of the standard waveform that you want
        the signal generator to produce. Specify this parameter in degrees of
        one waveform cycle. NI-FGEN sets the :py:data:`nifgen.Session.func_start_phase`
        property to this value. A start phase of 180 degrees means output
        generation begins halfway through the waveform. A start phase of 360
        degrees offsets the output by an entire waveform cycle, which is
        identical to a start phase of 0 degrees.

        **Units**: degrees of one cycle

        **Default Value**: 0.00

        

        .. note:: This parameter does not affect signal generator behavior when you set
            the **waveform** parameter to :py:data:`~nifgen.Waveform.DC`.


    :type start_phase: float

.. py:method:: create_advanced_arb_sequence(waveform_handles_array, loop_counts_array, sample_counts_array=None, marker_location_array=None)

    Creates an arbitrary sequence from an array of waveform handles and an
    array of corresponding loop counts. This method returns a handle that
    identifies the sequence. You pass this handle to the
    :py:meth:`nifgen.Session.configure_arb_sequence` method to specify what arbitrary sequence
    you want the signal generator to produce.

    The :py:meth:`nifgen.Session.create_advanced_arb_sequence` method extends on the
    :py:meth:`nifgen.Session.create_arb_sequence` method by adding the ability to set the
    number of samples in each sequence step and to set marker locations.

    An arbitrary sequence consists of multiple waveforms. For each waveform,
    you specify the number of times the signal generator produces the
    waveform before proceeding to the next waveform. The number of times to
    repeat a specific waveform is called the loop count.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this method.
        You must call the nifgen_ConfigureOutputMode method to set the
        **outputMode** parameter to :py:data:`~nifgen.OutputMode.SEQ` before calling this
        method.



    :param waveform_handles_array:


        Specifies the array of waveform handles from which you want to create a
        new arbitrary sequence. The array must have at least as many elements as
        the value that you specify in **sequenceLength**. Each
        **waveformHandlesArray** element has a corresponding **loopCountsArray**
        element that indicates how many times that waveform is repeated. You
        obtain waveform handles when you create arbitrary waveforms with the
        nifgen_AllocateWaveform method or one of the following niFgen
        CreateWaveform methods:

        -  nifgen_CreateWaveformF64
        -  nifgen_CreateWaveformI16
        -  nifgen_CreateWaveformFromFileI16
        -  nifgen_CreateWaveformFromFileF64
        -  nifgen_CreateWaveformFromFileHWS

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
        nifgen_QueryArbSeqCapabilities method.

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
        obtain these values by calling the nifgen_QueryArbWfmCapabilities
        method.

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
        set this parameter to :py:data:`~nifgen.NIFGEN_VAL_NO_MARKER`.

        **Defined Value**: :py:data:`~nifgen.NIFGEN_VAL_NO_MARKER`

        **Default Value**: None

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type marker_location_array: list of int

    :rtype: tuple (coerced_markers_array, sequence_handle)

        WHERE

        coerced_markers_array (list of int): 


            Returns an array of all given markers that are coerced (rounded) to the
            nearest marker quantum. Not all devices coerce markers.

            **Default Value**: None

            


        sequence_handle (int): 


            Returns the handle that identifies the new arbitrary sequence. You can
            pass this handle to nifgen_ConfigureArbSequence to generate the
            arbitrary sequence.

            



.. py:method:: create_arb_sequence(waveform_handles_array, loop_counts_array)

    Creates an arbitrary sequence from an array of waveform handles and an
    array of corresponding loop counts. This method returns a handle that
    identifies the sequence. You pass this handle to the
    nifgen_ConfigureArbSequence method to specify what arbitrary sequence
    you want the signal generator to produce.

    An arbitrary sequence consists of multiple waveforms. For each waveform,
    you can specify the number of times that the signal generator produces
    the waveform before proceeding to the next waveform. The number of times
    to repeat a specific waveform is called the loop count.

    

    .. note:: You must call the nifgen_ConfigureOutputMode method to set the
        **outputMode** parameter to :py:data:`~nifgen.OutputMode.SEQ` before calling this
        method.



    :param waveform_handles_array:


        Specifies the array of waveform handles from which you want to create a
        new arbitrary sequence. The array must have at least as many elements as
        the value that you specify in **sequenceLength**. Each
        **waveformHandlesArray** element has a corresponding **loopCountsArray**
        element that indicates how many times that waveform is repeated. You
        obtain waveform handles when you create arbitrary waveforms with the
        nifgen_AllocateWaveform method or one of the following niFgen
        CreateWaveform methods:

        -  nifgen_CreateWaveformF64
        -  nifgen_CreateWaveformI16
        -  nifgen_CreateWaveformFromFileI16
        -  nifgen_CreateWaveformFromFileF64
        -  nifgen_CreateWaveformFromFileHWS

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
        nifgen_QueryArbSeqCapabilities method.

        **Default Value**: None

        


    :type loop_counts_array: list of int

    :rtype: int
    :return:


            Returns the handle that identifies the new arbitrary sequence. You can
            pass this handle to nifgen_ConfigureArbSequence to generate the
            arbitrary sequence.

            



.. py:method:: create_freq_list(waveform, frequency_array, duration_array)

    Creates a frequency list from an array of frequencies
    (**frequencyArray**) and an array of durations (**durationArray**). The
    two arrays should have the same number of elements, and this value must
    also be the size of the **frequencyListLength**. The method returns a
    handle that identifies the frequency list (the **frequencyListHandle**).
    You can pass this handle to nifgen_ConfigureFreqList to specify what
    frequency list you want the signal generator to produce.

    A frequency list consists of a list of frequencies and durations. The
    signal generator generates each frequency for the given amount of time
    and then proceeds to the next frequency. When the end of the list is
    reached, the signal generator starts over at the beginning of the list.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this method.



    :param waveform:


        Specifies the standard waveform that you want the signal generator to
        produce. NI-FGEN sets the :py:data:`nifgen.Session.func_waveform` property to this
        value.

        ****Defined Values****

        **Default Value**: :py:data:`~nifgen.Waveform.SINE`

        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.SINE`      | Specifies that the signal generator produces a sinusoid waveform.                                                                  |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.SQUARE`    | Specifies that the signal generator produces a square waveform.                                                                    |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.TRIANGLE`  | Specifies that the signal generator produces a triangle waveform.                                                                  |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.RAMP_UP`   | Specifies that the signal generator produces a positive ramp waveform.                                                             |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.RAMP_DOWN` | Specifies that the signal generator produces a negative ramp waveform.                                                             |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.DC`        | Specifies that the signal generator produces a constant voltage.                                                                   |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.NOISE`     | Specifies that the signal generator produces white noise.                                                                          |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.Waveform.USER`      | Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform method. |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+


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
            this handle to nifgen_ConfigureFreqList to generate the arbitrary
            sequence.

            



.. py:method:: create_waveform_from_file_f64(file_name, byte_order)

    This method takes the floating point double (F64) data from the
    specified file and creates an onboard waveform for use in Arbitrary
    Waveform or Arbitrary Sequence output mode. The **waveformHandle**
    returned by this method can later be used for setting the active
    waveform, changing the data in the waveform, building sequences of
    waveforms, or deleting the waveform when it is no longer needed.

    

    .. note:: The F64 data must be between –1.0 and +1.0 V. Use the
        :py:data:`nifgen.Session.digital_gain` property to generate different voltage
        outputs.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].create_waveform_from_file_f64(file_name, byte_order)


    :param file_name:


        The full path and name of the file where the waveform data resides.

        


    :type file_name: str
    :param byte_order:


        Specifies the byte order of the data in the file.

        ****Defined Values****

        |
        | ****Default Value**:** :py:data:`~nifgen.ByteOrder.LITTLE`

        +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.ByteOrder.LITTLE` | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
        +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.ByteOrder.BIG`    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
        +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

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

            



.. py:method:: create_waveform_from_file_i16(file_name, byte_order)

    Takes the binary 16-bit signed integer (I16) data from the specified
    file and creates an onboard waveform for use in Arbitrary Waveform or
    Arbitrary Sequence output mode. The **waveformHandle** returned by this
    method can later be used for setting the active waveform, changing the
    data in the waveform, building sequences of waveforms, or deleting the
    waveform when it is no longer needed.

    

    .. note:: The I16 data (values between –32768 and +32767) is assumed to
        represent –1 to +1 V. Use the :py:data:`nifgen.Session.digital_gain` property to
        generate different voltage outputs.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].create_waveform_from_file_i16(file_name, byte_order)


    :param file_name:


        The full path and name of the file where the waveform data resides.

        


    :type file_name: str
    :param byte_order:


        Specifies the byte order of the data in the file.

        ****Defined Values****

        |
        | ****Default Value**:** :py:data:`~nifgen.ByteOrder.LITTLE`

        +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.ByteOrder.LITTLE` | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
        +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nifgen.ByteOrder.BIG`    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
        +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

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

            



.. py:method:: create_waveform_numpy(waveform_data_array)

    Creates an onboard waveform for use in Arbitrary Waveform output mode or Arbitrary Sequence output mode.

    

    .. note:: You must set :py:data:`nifgen.Session.output_mode` to :py:data:`~nifgen.OutputMode.ARB` or :py:data:`~nifgen.OutputMode.SEQ` before calling this method.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].create_waveform(waveform_data_array)


    :param waveform_data_array:


        Array of data for the new arbitrary waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.

        


    :type waveform_data_array: list of float

    :rtype: int
    :return:


            The handle that identifies the new waveform. This handle is used in other methods when referring to this waveform.

            



.. py:method:: define_user_standard_waveform(waveform_data_array)

    Defines a user waveform for use in either Standard Method or Frequency
    List output mode.

    To select the waveform, set the **waveform** parameter to
    :py:data:`~nifgen.Waveform.USER` with either the nifgen_ConfigureStandardWaveform
    or the nifgen_CreateFreqList method.

    The waveform data must be scaled between –1.0 and 1.0. Use the
    **amplitude** parameter in the :py:meth:`nifgen.Session.configure_standard_waveform`
    method to generate different output voltages.

    

    .. note:: You must call the nifgen_ConfigureOutputMode method to set the
        **outputMode** parameter to :py:data:`~nifgen.OutputMode.FUNC` or
        :py:data:`~nifgen.OutputMode.FREQ_LIST` before calling this method.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].define_user_standard_waveform(waveform_data_array)


    :param waveform_data_array:


        Specifies the array of data you want to use for the new arbitrary
        waveform. The array must have at least as many elements as the value
        that you specify in **waveformSize**.

        You must normalize the data points in the array to be between –1.00 and
        +1.00.

        **Default Value**: None

        


    :type waveform_data_array: list of float

.. py:method:: delete_named_waveform(waveform_name)

    Removes a previously created arbitrary waveform from the signal
    generator memory and invalidates the waveform handle.

    

    .. note:: The signal generator must not be in the Generating state when you call
        this method.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].delete_named_waveform(waveform_name)


    :param waveform_name:


        Specifies the name to associate with the allocated waveform.

        


    :type waveform_name: str

.. py:method:: delete_script(script_name)

    Deletes the specified script from onboard memory.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].delete_script(script_name)


    :param script_name:


        Specifies the name of the script you want to delete. The script name
        appears in the text of the script following the script keyword.

        


    :type script_name: str

.. py:method:: disable()

    Places the instrument in a quiescent state where it has minimal or no
    impact on the system to which it is connected. The analog output and all
    exported signals are disabled.

    



.. py:method:: get_ext_cal_last_date_and_time()

    Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this method returns 14 for the **hour** parameter and 30 for the **minute** parameter.

    



    :rtype: datetime.datetime
    :return:


            Indicates date and time of the last calibration.

            



.. py:method:: get_ext_cal_last_temp()

    Returns the temperature at the last successful external calibration. The
    temperature is returned in degrees Celsius.

    



    :rtype: float
    :return:


            Specifies the temperature at the last successful calibration in degrees
            Celsius.

            



.. py:method:: get_ext_cal_recommended_interval()

    Returns the recommended interval between external calibrations in
    months.

    



    :rtype: datetime.timedelta
    :return:


            Specifies the recommended interval between external calibrations in
            months.

            



.. py:method:: get_fir_filter_coefficients()

    | Returns the FIR filter coefficients used by the onboard signal
      processing block. These coefficients are determined by NI-FGEN and
      based on the FIR filter type and corresponding property (Alpha,
      Passband, BT) unless you are using the custom filter. If you are using
      a custom filter, the coefficients returned are those set with the
      nifgen_ConfigureCustomFIRFilterCoefficients method coerced to the
      quantized values used by the device.
    | To use this method, first call an instance of the
      :py:meth:`nifgen.Session.get_fir_filter_coefficients` method with the
      **coefficientsArray** parameter set to VI_NULL. Calling the method
      in this state returns the current size of the **coefficientsArray** as
      the value of the **numberOfCoefficientsRead** parameter. Create an
      array of this size, and call the :py:meth:`nifgen.Session.get_fir_filter_coefficients`
      method a second time, passing the new array as the
      **coefficientsArray** parameter and the size as the **arraySize**
      parameter. This second method call populates the array with the FIR
      filter coefficients.
    | Refer to the FIR Filter topic for your device in the *NI Signal
      Generators Help* for more information about FIR filter coefficients.
      This method is supported only for the NI 5441.
    | **Default Value**: None

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].get_fir_filter_coefficients()


    :rtype: int
    :return:


            Specifies the array of data containing the number of coefficients you
            want to read.

            



.. py:method:: get_hardware_state()

    Returns the current hardware state of the device and, if the device is
    in the hardware error state, the current hardware error.

    

    .. note:: Hardware states do not necessarily correspond to NI-FGEN states.



    :rtype: :py:data:`nifgen.HardwareState`
    :return:


            Returns the hardware state of the signal generator.

            **Defined Values**

            +------------------------------------------------------------+--------------------------------------------+
            | :py:data:`~nifgen.HardwareState.IDLE`                      | The device is in the Idle state.           |
            +------------------------------------------------------------+--------------------------------------------+
            | :py:data:`~nifgen.HardwareState.WAITING_FOR_START_TRIGGER` | The device is waiting for Start Trigger.   |
            +------------------------------------------------------------+--------------------------------------------+
            | :py:data:`~nifgen.HardwareState.RUNNING`                   | The device is in the Running state.        |
            +------------------------------------------------------------+--------------------------------------------+
            | :py:data:`~nifgen.HardwareState.DONE`                      | The generation has completed successfully. |
            +------------------------------------------------------------+--------------------------------------------+
            | :py:data:`~nifgen.HardwareState.HARDWARE_ERROR`            | There is a hardware error.                 |
            +------------------------------------------------------------+--------------------------------------------+



.. py:method:: get_self_cal_last_date_and_time()

    Returns the date and time of the last successful self-calibration.

    



    :rtype: datetime.datetime
    :return:


            Returns the date and time the device was last calibrated.

            



.. py:method:: get_self_cal_last_temp()

    Returns the temperature at the last successful self-calibration. The
    temperature is returned in degrees Celsius.

    



    :rtype: float
    :return:


            Specifies the temperature at the last successful calibration in degrees
            Celsius.

            



.. py:method:: get_self_cal_supported()

    Returns whether the device supports self–calibration.

    



    :rtype: bool
    :return:


            Returns whether the device supports self-calibration.

            ****Defined Values****

            +-------+------------------------------------+
            | True  | Self–calibration is supported.     |
            +-------+------------------------------------+
            | False | Self–calibration is not supported. |
            +-------+------------------------------------+



.. py:method:: is_done()

    Determines whether the current generation is complete. This method
    sets the **done** parameter to True if the session is in the Idle or
    Committed states.

    

    .. note:: NI-FGEN only reports the **done** parameter as True after the
        current generation is complete in Single trigger mode.



    :rtype: bool
    :return:


            Returns information about the completion of waveform generation.

            **Defined Values**

            +-------+-----------------------------+
            | True  | Generation is complete.     |
            +-------+-----------------------------+
            | False | Generation is not complete. |
            +-------+-----------------------------+



.. py:method:: query_arb_seq_capabilities()

    Returns the properties of the signal generator that are related to
    creating arbitrary sequences (the :py:data:`nifgen.Session.max_num_sequences`,
    :py:data:`nifgen.Session.min_sequence_length`,
    :py:data:`nifgen.Session.max_sequence_length`, and :py:data:`nifgen.Session.max_loop_count`
    properties).

    



    :rtype: tuple (maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count)

        WHERE

        maximum_number_of_sequences (int): 


            Returns the maximum number of arbitrary waveform sequences that the
            signal generator allows. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.max_num_sequences` property.

            


        minimum_sequence_length (int): 


            Returns the minimum number of arbitrary waveforms the signal generator
            allows in a sequence. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.min_sequence_length` property.

            


        maximum_sequence_length (int): 


            Returns the maximum number of arbitrary waveforms the signal generator
            allows in a sequence. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.max_sequence_length` property.

            


        maximum_loop_count (int): 


            Returns the maximum number of times the signal generator can repeat an
            arbitrary waveform in a sequence. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.max_loop_count` property.

            



.. py:method:: query_arb_wfm_capabilities()

    Returns the properties of the signal generator that are related to
    creating arbitrary waveforms. These properties are the maximum number of
    waveforms, waveform quantum, minimum waveform size, and maximum waveform
    size.

    

    .. note:: If you do not want to obtain the waveform quantum, pass a value of
        VI_NULL for this parameter.



    :rtype: tuple (maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size)

        WHERE

        maximum_number_of_waveforms (int): 


            Returns the maximum number of arbitrary waveforms that the signal
            generator allows. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.max_num_waveforms` property.

            


        waveform_quantum (int): 


            The size (number of points) of each waveform must be a multiple of a
            constant quantum value. This parameter obtains the quantum value that
            the signal generator uses. NI-FGEN returns this value from the
            :py:data:`nifgen.Session.waveform_quantum` property.

            For example, when this property returns a value of 8, all waveform
            sizes must be a multiple of 8.

            


        minimum_waveform_size (int): 


            Returns the minimum number of points that the signal generator allows in
            a waveform. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.min_waveform_size` property.

            


        maximum_waveform_size (int): 


            Returns the maximum number of points that the signal generator allows in
            a waveform. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.max_waveform_size` property.

            



.. py:method:: query_freq_list_capabilities()

    Returns the properties of the signal generator that are related to
    creating frequency lists. These properties are
    :py:data:`nifgen.Session.max_num_freq_lists`,
    :py:data:`nifgen.Session.min_freq_list_length`,
    :py:data:`nifgen.Session.max_freq_list_length`,
    :py:data:`nifgen.Session.min_freq_list_duration`,
    :py:data:`nifgen.Session.max_freq_list_duration`, and
    :py:data:`nifgen.Session.freq_list_duration_quantum`.

    



    :rtype: tuple (maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum)

        WHERE

        maximum_number_of_freq_lists (int): 


            Returns the maximum number of frequency lists that the signal generator
            allows. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.max_num_freq_lists` property.

            


        minimum_frequency_list_length (int): 


            Returns the minimum number of steps that the signal generator allows in
            a frequency list. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.min_freq_list_length` property.

            


        maximum_frequency_list_length (int): 


            Returns the maximum number of steps that the signal generator allows in
            a frequency list. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.max_freq_list_length` property.

            


        minimum_frequency_list_duration (float): 


            Returns the minimum duration that the signal generator allows in a step
            of a frequency list. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.min_freq_list_duration` property.

            


        maximum_frequency_list_duration (float): 


            Returns the maximum duration that the signal generator allows in a step
            of a frequency list. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.max_freq_list_duration` property.

            


        frequency_list_duration_quantum (float): 


            Returns the quantum of which all durations must be a multiple in a
            frequency list. NI-FGEN obtains this value from the
            :py:data:`nifgen.Session.freq_list_duration_quantum` property.

            



.. py:method:: read_current_temperature()

    Reads the current onboard temperature of the device. The temperature is
    returned in degrees Celsius.

    



    :rtype: float
    :return:


            Returns the current temperature read from onboard temperature sensors,
            in degrees Celsius.

            



.. py:method:: reset()

    Resets the instrument to a known state. This method aborts the
    generation, clears all routes, and resets session properties to the
    default values. This method does not, however, commit the session
    properties or configure the device hardware to its default state.

    

    .. note:: For the NI 5401/5404/5411/5431, this method exhibits the same
        behavior as the nifgen_ResetDevice method.



.. py:method:: reset_device()

    Performs a hard reset on the device. Generation is stopped, all routes
    are released, external bidirectional terminals are tristated, FPGAs are
    reset, hardware is configured to its default state, and all session
    properties are reset to their default states.

    



.. py:method:: reset_with_defaults()

    Resets the instrument and reapplies initial user–specified settings from
    the logical name that was used to initialize the session. If the session
    was created without a logical name, this method is equivalent to the
    nifgen_reset method.

    



.. py:method:: self_cal()

    Performs a full internal self-calibration on the device. If the
    calibration is successful, new calibration data and constants are stored
    in the onboard EEPROM.

    



.. py:method:: self_test()

    Runs the instrument self-test routine and returns the test result(s).

    Raises `SelfTestError` on self test failure. Properties on exception object:

    - code - failure code from driver
    - message - status message from driver

    +----------------+------------------+
    | Self-Test Code | Description      |
    +================+==================+
    | 0              | Passed self-test |
    +----------------+------------------+
    | 1              | Self-test failed |
    +----------------+------------------+

    .. note:: When used on some signal generators, the device is reset after the
        :py:meth:`nifgen.Session.self_test` method runs. If you use the :py:meth:`nifgen.Session.self_test`
        method, your device may not be in its previously configured state
        after the method runs.



.. py:method:: send_software_edge_trigger(trigger, trigger_id)

    Sends a command to trigger the signal generator. This VI can act as an
    override for an external edge trigger.

    

    .. note:: This VI does not override external digital edge triggers of the
        NI 5401/5411/5431.



    :param trigger:


        Sets the clock mode of the signal generator.

        ****Defined Values****

        +----------------------------------------------+
        | :py:data:`~nifgen.ClockMode.DIVIDE_DOWN`     |
        +----------------------------------------------+
        | :py:data:`~nifgen.ClockMode.HIGH_RESOLUTION` |
        +----------------------------------------------+
        | :py:data:`~nifgen.ClockMode.AUTOMATIC`       |
        +----------------------------------------------+


    :type trigger: :py:data:`nifgen.Trigger`
    :param trigger_id:

    :type trigger_id: str

.. py:method:: set_named_waveform_next_write_position(waveform_name, relative_to, offset)

    Sets the position in the waveform to which data is written at the next
    write. This method allows you to write to arbitrary locations within
    the waveform. These settings apply only to the next write to the
    waveform specified by the **waveformHandle** parameter. Subsequent
    writes to that waveform begin where the last write left off, unless this
    method is called again. The **waveformHandle** passed in must have
    been created with a call to one of the following methods:

    -  nifgen_AllocateWaveform
    -  nifgen_CreateWaveformF64
    -  nifgen_CreateWaveformI16
    -  nifgen_CreateWaveformFromFileI16
    -  nifgen_CreateWaveformFromFileF64
    -  nifgen_CreateWaveformFromFileHWS

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].set_named_waveform_next_write_position(waveform_name, relative_to, offset)


    :param waveform_name:


        Specifies the name to associate with the allocated waveform.

        


    :type waveform_name: str
    :param relative_to:


        Specifies the reference position in the waveform. This position and
        **offset** together determine where to start loading data into the
        waveform.

        ****Defined Values****

        +-------------------------------------------+-------------------------------------------------------------------------+
        | :py:data:`~nifgen.RelativeTo.START` (0)   | Use the start of the waveform as the reference position.                |
        +-------------------------------------------+-------------------------------------------------------------------------+
        | :py:data:`~nifgen.RelativeTo.CURRENT` (1) | Use the current position within the waveform as the reference position. |
        +-------------------------------------------+-------------------------------------------------------------------------+


    :type relative_to: :py:data:`nifgen.RelativeTo`
    :param offset:


        Specifies the offset from the **relativeTo** parameter at which to start
        loading the data into the waveform.

        


    :type offset: int

.. py:method:: set_waveform_next_write_position(waveform_handle, relative_to, offset)

    Sets the position in the waveform at which the next waveform data is
    written. This method allows you to write to arbitrary locations within
    the waveform. These settings apply only to the next write to the
    waveform specified by the waveformHandle parameter. Subsequent writes to
    that waveform begin where the last write left off, unless this method
    is called again. The waveformHandle passed in must have been created by
    a call to the nifgen_AllocateWaveform method or one of the following
    niFgen CreateWaveform methods:

    -  nifgen_CreateWaveformF64
    -  nifgen_CreateWaveformI16
    -  nifgen_CreateWaveformFromFileI16
    -  nifgen_CreateWaveformFromFileF64
    -  nifgen_CreateWaveformFromFileHWS

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].set_waveform_next_write_position(waveform_handle, relative_to, offset)


    :param waveform_handle:


        Specifies the handle of the arbitrary waveform previously allocated with
        the nifgen_AllocateWaveform method.

        


    :type waveform_handle: int
    :param relative_to:


        Specifies the reference position in the waveform. This position and
        **offset** together determine where to start loading data into the
        waveform.

        ****Defined Values****

        +-------------------------------------------+-------------------------------------------------------------------------+
        | :py:data:`~nifgen.RelativeTo.START` (0)   | Use the start of the waveform as the reference position.                |
        +-------------------------------------------+-------------------------------------------------------------------------+
        | :py:data:`~nifgen.RelativeTo.CURRENT` (1) | Use the current position within the waveform as the reference position. |
        +-------------------------------------------+-------------------------------------------------------------------------+


    :type relative_to: :py:data:`nifgen.RelativeTo`
    :param offset:


        Specifies the offset from **relativeTo** at which to start loading the
        data into the waveform.

        


    :type offset: int

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`nidcpower.Session.lock_session`. Refer to :py:meth:`nidcpower.Session.lock_session` for additional
    information on session locks.



.. py:method:: wait_until_done(max_time=10000)

    Waits until the device is done generating or until the maximum time has
    expired.

    



    :param max_time:


        Specifies the timeout value in milliseconds.

        


    :type max_time: float in seconds or datetime.timedelta

.. py:method:: write_script(script)

    Writes a string containing one or more scripts that govern the
    generation of waveforms.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].write_script(script)


    :param script:


        Contains the text of the script you want to use for your generation
        operation. Refer to `scripting
        Instructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__
        for more information about writing scripts.

        


    :type script: str

.. py:method:: write_waveform(waveform_name_or_handle, data)

    Writes data to the waveform in onboard memory.

    By default, subsequent calls to this method
    continue writing data from the position of the last sample written. You
    can set the write position and offset by calling the nifgen_SetNamedWaveformNextWritePosition
    nifgen_SetWaveformNextWritePosition method.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nifgen.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifgen.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].write_waveform(waveform_name_or_handle, data)


    :param waveform_name_or_handle:


        The name (str) or handle (int) of an arbitrary waveform previously allocated with :py:meth:`nifgen.Session.allocate_named_waveform` or :py:meth:`nifgen.Session.allocate_waveform`.

        


    :type waveform_name_or_handle: int
    :param data:


        Array of data to load into the waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.

        


    :type data: list of float


