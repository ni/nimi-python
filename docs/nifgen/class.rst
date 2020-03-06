.. py:module:: nifgen

Session
=======

.. py:class:: Session(self, resource_name, channel_name=None, reset_device=False, options={})

    

    Creates and returns a new NI-FGEN session to the specified channel of a
    waveform generator that is used in all subsequent NI-FGEN method
    calls.

    



    :param resource_name:
        

        .. caution:: Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
            However, all IVI names, such as logical names, are case-sensitive. If
            you use logical names, driver session names, or virtual names in your
            program, you must ensure that the name you use matches the name in the
            IVI Configuration Store file exactly, without any variations in the case
            of the characters.

        | Specifies the resource name of the device to initialize.

        For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
        the device number assigned by MAX, as shown in Example 1.

        For NI-DAQmx devices, the syntax is just the device name specified in
        MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
        in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
        right-clicking on the name in MAX and entering a new name.

        An alternate syntax for NI-DAQmx devices consists of DAQ::\ *NI-DAQmx
        device name*, as shown in Example 3. This naming convention allows for
        the use of an NI-DAQmx device in an application that was originally
        designed for a Traditional NI-DAQ device. For example, if the
        application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
        MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

        If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
        exists with that same name, the NI-DAQmx device is matched first.

        You can also pass in the name of an IVI logical name or an IVI virtual
        name configured with the IVI Configuration utility, as shown in Example
        5. A logical name identifies a particular virtual instrument. A virtual
        name identifies a specific device and specifies the initial settings for
        the session.

        +-----------+--------------------------------------+------------------------+---------------------------------+
        | Example # | Device Type                          | Syntax                 | Variable                        |
        +===========+======================================+========================+=================================+
        | 1         | Traditional NI-DAQ device            | DAQ::\ *1*             | (*1* = device number)           |
        +-----------+--------------------------------------+------------------------+---------------------------------+
        | 2         | NI-DAQmx device                      | *myDAQmxDevice*        | (*myDAQmxDevice* = device name) |
        +-----------+--------------------------------------+------------------------+---------------------------------+
        | 3         | NI-DAQmx device                      | DAQ::\ *myDAQmxDevice* | (*myDAQmxDevice* = device name) |
        +-----------+--------------------------------------+------------------------+---------------------------------+
        | 4         | NI-DAQmx device                      | DAQ::\ *2*             | (*2* = device name)             |
        +-----------+--------------------------------------+------------------------+---------------------------------+
        | 5         | IVI logical name or IVI virtual name | *myLogicalName*        | (*myLogicalName* = name)        |
        +-----------+--------------------------------------+------------------------+---------------------------------+


    :type resource_name: str

    :param channel_name:
        

        Specifies the channel that this VI uses.

        **Default Value**: "0"

        


    :type channel_name: str, list, range, tuple

    :param reset_device:
        

        Specifies whether you want to reset the device during the initialization
        procedure. True specifies that the device is reset and performs the
        same method as the :py:meth:`nifgen.Session.Reset` method.

        ****Defined Values****

        **Default Value**: False

        +-------+---------------------+
        | True  | Reset device        |
        +-------+---------------------+
        | False | Do not reset device |
        +-------+---------------------+


    :type reset_device: bool

    :param options:
        

        Specifies the initial value of certain properties for the session. The
        syntax for **options** is a dictionary of properties with an assigned
        value. For example:

        { 'simulate': False }

        You do not have to specify a value for all the properties. If you do not
        specify a value for a property, the default value is used.

        Advanced Example:
        { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

        +-------------------------+---------+
        | Property                | Default |
        +=========================+=========+
        | range_check             | True    |
        +-------------------------+---------+
        | query_instrument_status | False   |
        +-------------------------+---------+
        | cache                   | True    |
        +-------------------------+---------+
        | simulate                | False   |
        +-------------------------+---------+
        | record_value_coersions  | False   |
        +-------------------------+---------+
        | driver_setup            | {}      |
        +-------------------------+---------+


    :type options: dict


Methods
=======

abort
-----

    .. py:currentmodule:: nifgen.Session

    .. py:method:: abort()

            Aborts any previously initiated signal generation. Call the
            :py:meth:`nifgen.Session.initiate` method to cause the signal generator to
            produce a signal again.

            



allocate_named_waveform
-----------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: allocate_named_waveform(waveform_name, waveform_size)

            Specifies the size of a named waveform up front so that it can be
            allocated in onboard memory before loading the associated data. Data can
            then be loaded in smaller blocks with the niFgen Write (Binary16)
            Waveform methods.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].allocate_named_waveform(waveform_name, waveform_size)


            :param waveform_name:


                Specifies the name to associate with the allocated waveform.

                


            :type waveform_name: str
            :param waveform_size:


                Specifies the size of the waveform to allocate in samples.

                **Default Value**: "4096"

                


            :type waveform_size: int

allocate_waveform
-----------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: allocate_waveform(waveform_size)

            Specifies the size of a waveform so that it can be allocated in onboard
            memory before loading the associated data. Data can then be loaded in
            smaller blocks with the Write Binary 16 Waveform methods.

            

            .. note:: The signal generator must not be in the Generating state when you call
                this method.


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].allocate_waveform(waveform_size)


            :param waveform_size:


                Specifies, in samples, the size of the waveform to allocate.

                


            :type waveform_size: int

            :rtype: int
            :return:


                    The handle that identifies the new waveform. This handle is used later
                    when referring to this waveform.

                    



clear_arb_memory
----------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: clear_arb_memory()

            Removes all previously created arbitrary waveforms, sequences, and
            scripts from the signal generator memory and invalidates all waveform
            handles, sequence handles, and waveform names.

            

            .. note:: The signal generator must not be in the Generating state when you
                call this method.



clear_arb_sequence
------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: clear_arb_sequence(sequence_handle)

            Removes a previously created arbitrary sequence from the signal
            generator memory and invalidates the sequence handle.

            

            .. note:: The signal generator must not be in the Generating state when you
                call this method.



            :param sequence_handle:


                Specifies the handle of the arbitrary sequence that you want the signal
                generator to remove. You can create an arbitrary sequence using the
                :py:meth:`nifgen.Session.create_arb_sequence` or :py:meth:`nifgen.Session.create_advanced_arb_sequence` method.
                These methods return a handle that you use to identify the sequence.

                | **Defined Value**:
                | :py:data:`~nifgen.NIFGEN_VAL_ALL_SEQUENCES`—Remove all sequences from the signal
                  generator

                **Default Value**: None

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type sequence_handle: int

clear_freq_list
---------------

    .. py:currentmodule:: nifgen.Session

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

clear_user_standard_waveform
----------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: clear_user_standard_waveform()

            Clears the user-defined waveform created by the
            :py:meth:`nifgen.Session.define_user_standard_waveform` method.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].clear_user_standard_waveform()


close
-----

    .. py:currentmodule:: nifgen.Session

    .. py:method:: close()

            Performs the following operations:

            -  Closes the instrument I/O session.
            -  Destroys the NI-FGEN session and all of its properties.
            -  Deallocates any memory resources NI-FGEN uses.

            Not all signal routes established by calling the :py:meth:`nifgen.Session.ExportSignal`
            and :py:meth:`nifgen.Session.RouteSignalOut` methods are released when the NI-FGEN
            session is closed. The following table shows what happens to a signal
            route on your device when you call the :py:meth:`nifgen.Session._close` method.

            +--------------------+-------------------+------------------+
            | Routes To          | NI 5401/5411/5431 | Other Devices    |
            +====================+===================+==================+
            | Front Panel        | Remain connected  | Remain connected |
            +--------------------+-------------------+------------------+
            | RTSI/PXI Backplane | Remain connected  | Disconnected     |
            +--------------------+-------------------+------------------+

            .. note:: After calling :py:meth:`nifgen.Session._close`, you cannot use NI-FGEN again until you
                call the :py:meth:`nifgen.Session.init` or :py:meth:`nifgen.Session.InitWithOptions` methods.

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: nifgen.Session

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
            -  A subsequent :py:meth:`nifgen.Session.initiate` method can run faster
               because the device is already configured.

            



configure_arb_sequence
----------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: configure_arb_sequence(sequence_handle, gain, offset)

            Configures the signal generator properties that affect arbitrary
            sequence generation. Sets the :py:attr:`nifgen.Session.arb_sequence_handle`,
            :py:attr:`nifgen.Session.arb_gain`, and :py:attr:`nifgen.Session.arb_offset` properties.

            

            .. note:: The signal generator must not be in the Generating state when you call
                this method.


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].configure_arb_sequence(sequence_handle, gain, offset)


            :param sequence_handle:


                Specifies the handle of the arbitrary sequence that you want the signal
                generator to produce. NI-FGEN sets the
                :py:attr:`nifgen.Session.arb_sequence_handle` property to this value. You can
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
                :py:attr:`nifgen.Session.arb_offset` property to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

                


            :type offset: float

configure_arb_waveform
----------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: configure_arb_waveform(waveform_handle, gain, offset)

            Configures the properties of the signal generator that affect arbitrary
            waveform generation. Sets the :py:attr:`nifgen.Session.arb_waveform_handle`,
            :py:attr:`nifgen.Session.arb_gain`, and :py:attr:`nifgen.Session.arb_offset` properties.

            

            .. note:: The signal generator must not be in the Generating state when you call
                this method.


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].configure_arb_waveform(waveform_handle, gain, offset)


            :param waveform_handle:


                Specifies the handle of the arbitrary waveform you want the signal
                generator to produce. NI-FGEN sets the
                :py:attr:`nifgen.Session.arb_waveform_handle` property to this value. You can
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
                :py:attr:`nifgen.Session.arb_offset` property to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

                


            :type offset: float

configure_freq_list
-------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: configure_freq_list(frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0)

            Configures the properties of the signal generator that affect frequency
            list generation (the :py:attr:`nifgen.Session.freq_list_handle`,
            :py:attr:`nifgen.Session.func_amplitude`, :py:attr:`nifgen.Session.func_dc_offset`, and
            :py:attr:`nifgen.Session.func_start_phase` properties).

            

            .. note:: The signal generator must not be in the Generating state when you call
                this method.


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].configure_freq_list(frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0)


            :param frequency_list_handle:


                Specifies the handle of the frequency list that you want the signal
                generator to produce. NI-FGEN sets the :py:attr:`nifgen.Session.freq_list_handle`
                property to this value. You can create a frequency list using the
                :py:meth:`nifgen.Session.create_freq_list` method, which returns a handle that you use to
                identify the list.
                **Default Value**: None

                


            :type frequency_list_handle: int
            :param amplitude:


                Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the :py:attr:`nifgen.Session.func_amplitude` property to
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
                **dcOffset** to 5.00 V. NI-FGEN sets the :py:attr:`nifgen.Session.func_dc_offset`
                property to this value.

                **Units**: volts

                **Default Value**: None

                


            :type dc_offset: float
            :param start_phase:


                Specifies the horizontal offset of the standard waveform you want the
                signal generator to produce. Specify this property in degrees of one
                waveform cycle. NI-FGEN sets the :py:attr:`nifgen.Session.func_start_phase`
                property to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: None degrees

                

                .. note:: This parameter does not affect signal generator behavior when you set
                    the **waveform** parameter to :py:data:`~nifgen.Waveform.DC`.


            :type start_phase: float

configure_standard_waveform
---------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: configure_standard_waveform(waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0)

            Configures the following properties of the signal generator that affect
            standard waveform generation:

            -  :py:attr:`nifgen.Session.func_waveform`
            -  :py:attr:`nifgen.Session.func_amplitude`
            -  :py:attr:`nifgen.Session.func_dc_offset`
            -  :py:attr:`nifgen.Session.func_frequency`
            -  :py:attr:`nifgen.Session.func_start_phase`

            

            .. note:: You must call the :py:meth:`nifgen.Session.ConfigureOutputMode` method with the
                **outputMode** parameter set to :py:data:`~nifgen.OutputMode.FUNC` before calling
                this method.

            .. note:: One or more of the referenced methods are not in the Python API for this driver.


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].configure_standard_waveform(waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0)


            :param waveform:


                Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the :py:attr:`nifgen.Session.func_waveform` property to this
                value.

                ****Defined Values****

                **Default Value**: :py:data:`~nifgen.Waveform.SINE`

                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.SINE`      | Specifies that the signal generator produces a sinusoid waveform.                                                                                        |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.SQUARE`    | Specifies that the signal generator produces a square waveform.                                                                                          |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.TRIANGLE`  | Specifies that the signal generator produces a triangle waveform.                                                                                        |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.RAMP_UP`   | Specifies that the signal generator produces a positive ramp waveform.                                                                                   |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.RAMP_DOWN` | Specifies that the signal generator produces a negative ramp waveform.                                                                                   |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.DC`        | Specifies that the signal generator produces a constant voltage.                                                                                         |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.NOISE`     | Specifies that the signal generator produces white noise.                                                                                                |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.USER`      | Specifies that the signal generator produces a user-defined waveform as defined with the :py:meth:`nifgen.Session.define_user_standard_waveform` method. |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+


            :type waveform: :py:data:`nifgen.Waveform`
            :param amplitude:


                Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the :py:attr:`nifgen.Session.func_amplitude` property to
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
                  :py:attr:`nifgen.Session.func_frequency` property to this value.

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
                **dcOffset** to 5.00 V. NI-FGEN sets the :py:attr:`nifgen.Session.func_dc_offset`
                property to this value.

                **Units**: volts

                **Default Value**: None

                


            :type dc_offset: float
            :param start_phase:


                Specifies the horizontal offset of the standard waveform that you want
                the signal generator to produce. Specify this parameter in degrees of
                one waveform cycle. NI-FGEN sets the :py:attr:`nifgen.Session.func_start_phase`
                property to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: 0.00

                

                .. note:: This parameter does not affect signal generator behavior when you set
                    the **waveform** parameter to :py:data:`~nifgen.Waveform.DC`.


            :type start_phase: float

create_advanced_arb_sequence
----------------------------

    .. py:currentmodule:: nifgen.Session

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
                You must call the :py:meth:`nifgen.Session.ConfigureOutputMode` method to set the
                **outputMode** parameter to :py:data:`~nifgen.OutputMode.SEQ` before calling this
                method.



            :param waveform_handles_array:


                Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                :py:meth:`nifgen.Session.allocate_waveform` method or one of the following niFgen
                CreateWaveform methods:

                -  :py:meth:`nifgen.Session.create_waveform`
                -  :py:meth:`nifgen.Session.create_waveform`
                -  :py:meth:`nifgen.Session.create_waveform_from_file_i16`
                -  :py:meth:`nifgen.Session.create_waveform_from_file_f64`
                -  :py:meth:`nifgen.Session.CreateWaveformFromFileHWS`

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
                :py:meth:`nifgen.Session.query_arb_seq_capabilities` method.

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
                obtain these values by calling the :py:meth:`nifgen.Session.query_arb_wfm_capabilities`
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
                    pass this handle to :py:meth:`nifgen.Session.configure_arb_sequence` to generate the
                    arbitrary sequence.

                    



create_arb_sequence
-------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: create_arb_sequence(waveform_handles_array, loop_counts_array)

            Creates an arbitrary sequence from an array of waveform handles and an
            array of corresponding loop counts. This method returns a handle that
            identifies the sequence. You pass this handle to the
            :py:meth:`nifgen.Session.configure_arb_sequence` method to specify what arbitrary sequence
            you want the signal generator to produce.

            An arbitrary sequence consists of multiple waveforms. For each waveform,
            you can specify the number of times that the signal generator produces
            the waveform before proceeding to the next waveform. The number of times
            to repeat a specific waveform is called the loop count.

            

            .. note:: You must call the :py:meth:`nifgen.Session.ConfigureOutputMode` method to set the
                **outputMode** parameter to :py:data:`~nifgen.OutputMode.SEQ` before calling this
                method.



            :param waveform_handles_array:


                Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                :py:meth:`nifgen.Session.allocate_waveform` method or one of the following niFgen
                CreateWaveform methods:

                -  :py:meth:`nifgen.Session.create_waveform`
                -  :py:meth:`nifgen.Session.create_waveform`
                -  :py:meth:`nifgen.Session.create_waveform_from_file_i16`
                -  :py:meth:`nifgen.Session.create_waveform_from_file_f64`
                -  :py:meth:`nifgen.Session.CreateWaveformFromFileHWS`

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
                :py:meth:`nifgen.Session.query_arb_seq_capabilities` method.

                **Default Value**: None

                


            :type loop_counts_array: list of int

            :rtype: int
            :return:


                    Returns the handle that identifies the new arbitrary sequence. You can
                    pass this handle to :py:meth:`nifgen.Session.configure_arb_sequence` to generate the
                    arbitrary sequence.

                    



create_freq_list
----------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: create_freq_list(waveform, frequency_array, duration_array)

            Creates a frequency list from an array of frequencies
            (**frequencyArray**) and an array of durations (**durationArray**). The
            two arrays should have the same number of elements, and this value must
            also be the size of the **frequencyListLength**. The method returns a
            handle that identifies the frequency list (the **frequencyListHandle**).
            You can pass this handle to :py:meth:`nifgen.Session.configure_freq_list` to specify what
            frequency list you want the signal generator to produce.

            A frequency list consists of a list of frequencies and durations. The
            signal generator generates each frequency for the given amount of time
            and then proceeds to the next frequency. When the end of the list is
            reached, the signal generator starts over at the beginning of the list.

            

            .. note:: The signal generator must not be in the Generating state when you call
                this method.



            :param waveform:


                Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the :py:attr:`nifgen.Session.func_waveform` property to this
                value.

                ****Defined Values****

                **Default Value**: :py:data:`~nifgen.Waveform.SINE`

                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.SINE`      | Specifies that the signal generator produces a sinusoid waveform.                                                                                        |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.SQUARE`    | Specifies that the signal generator produces a square waveform.                                                                                          |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.TRIANGLE`  | Specifies that the signal generator produces a triangle waveform.                                                                                        |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.RAMP_UP`   | Specifies that the signal generator produces a positive ramp waveform.                                                                                   |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.RAMP_DOWN` | Specifies that the signal generator produces a negative ramp waveform.                                                                                   |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.DC`        | Specifies that the signal generator produces a constant voltage.                                                                                         |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.NOISE`     | Specifies that the signal generator produces white noise.                                                                                                |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.USER`      | Specifies that the signal generator produces a user-defined waveform as defined with the :py:meth:`nifgen.Session.define_user_standard_waveform` method. |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+


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
                    this handle to :py:meth:`nifgen.Session.configure_freq_list` to generate the arbitrary
                    sequence.

                    



create_waveform_from_file_f64
-----------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: create_waveform_from_file_f64(file_name, byte_order)

            This method takes the floating point double (F64) data from the
            specified file and creates an onboard waveform for use in Arbitrary
            Waveform or Arbitrary Sequence output mode. The **waveformHandle**
            returned by this method can later be used for setting the active
            waveform, changing the data in the waveform, building sequences of
            waveforms, or deleting the waveform when it is no longer needed.

            

            .. note:: The F64 data must be between –1.0 and +1.0 V. Use the
                :py:attr:`nifgen.Session.digital_gain` property to generate different voltage
                outputs.


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].create_waveform_from_file_f64(file_name, byte_order)


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

                    



create_waveform_from_file_i16
-----------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: create_waveform_from_file_i16(file_name, byte_order)

            Takes the binary 16-bit signed integer (I16) data from the specified
            file and creates an onboard waveform for use in Arbitrary Waveform or
            Arbitrary Sequence output mode. The **waveformHandle** returned by this
            method can later be used for setting the active waveform, changing the
            data in the waveform, building sequences of waveforms, or deleting the
            waveform when it is no longer needed.

            

            .. note:: The I16 data (values between –32768 and +32767) is assumed to
                represent –1 to +1 V. Use the :py:attr:`nifgen.Session.digital_gain` property to
                generate different voltage outputs.


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].create_waveform_from_file_i16(file_name, byte_order)


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

                    



create_waveform_numpy
---------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: create_waveform_numpy(waveform_data_array)

            Creates an onboard waveform for use in Arbitrary Waveform output mode or Arbitrary Sequence output mode.

            

            .. note:: You must set :py:attr:`nifgen.Session.output_mode` to :py:data:`~nifgen.OutputMode.ARB` or :py:data:`~nifgen.OutputMode.SEQ` before calling this method.


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].create_waveform(waveform_data_array)


            :param waveform_data_array:


                Array of data for the new arbitrary waveform. This may be an iterable of float or int16, or for best performance a numpy.ndarray of dtype int16 or float64.

                


            :type waveform_data_array: iterable of float or int16

            :rtype: int
            :return:


                    The handle that identifies the new waveform. This handle is used in other methods when referring to this waveform.

                    



define_user_standard_waveform
-----------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: define_user_standard_waveform(waveform_data_array)

            Defines a user waveform for use in either Standard Method or Frequency
            List output mode.

            To select the waveform, set the **waveform** parameter to
            :py:data:`~nifgen.Waveform.USER` with either the :py:meth:`nifgen.Session.configure_standard_waveform`
            or the :py:meth:`nifgen.Session.create_freq_list` method.

            The waveform data must be scaled between –1.0 and 1.0. Use the
            **amplitude** parameter in the :py:meth:`nifgen.Session.configure_standard_waveform`
            method to generate different output voltages.

            

            .. note:: You must call the :py:meth:`nifgen.Session.ConfigureOutputMode` method to set the
                **outputMode** parameter to :py:data:`~nifgen.OutputMode.FUNC` or
                :py:data:`~nifgen.OutputMode.FREQ_LIST` before calling this method.


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].define_user_standard_waveform(waveform_data_array)


            :param waveform_data_array:


                Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None

                


            :type waveform_data_array: list of float

delete_script
-------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: delete_script(script_name)

            Deletes the specified script from onboard memory.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].delete_script(script_name)


            :param script_name:


                Specifies the name of the script you want to delete. The script name
                appears in the text of the script following the script keyword.

                


            :type script_name: str

delete_waveform
---------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: delete_waveform(waveform_name_or_handle)

            Removes a previously created arbitrary waveform from the signal generator memory.

            

            .. note:: The signal generator must not be in the Generating state when you call this method.


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].delete_waveform(waveform_name_or_handle)


            :param waveform_name_or_handle:


                The name (str) or handle (int) of an arbitrary waveform previously allocated with :py:meth:`nifgen.Session.allocate_named_waveform`, :py:meth:`nifgen.Session.allocate_waveform` or :py:meth:`nifgen.Session.create_waveform`.

                


            :type waveform_name_or_handle: str or int

disable
-------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: disable()

            Places the instrument in a quiescent state where it has minimal or no
            impact on the system to which it is connected. The analog output and all
            exported signals are disabled.

            



export_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: export_attribute_configuration_buffer()

            Exports the property configuration of the session to a configuration
            buffer.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑FGEN returns an
            error.

            



            :rtype: bytes
            :return:


                    Specifies the byte array buffer to be populated with the exported
                    property configuration.

                    



export_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: export_attribute_configuration_file(file_path)

            Exports the property configuration of the session to the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑FGEN returns an
            error.

            



            :param file_path:


                Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .nifgenconfig

                


            :type file_path: str

get_channel_name
----------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_channel_name(index)

            Returns the channel string that is in the channel table at an index you
            specify.

            

            .. note:: This method is included for compliance with the IviFgen Class
                Specification.



            :param index:


                A 1-based index into the channel table.

                


            :type index: int

            :rtype: str
            :return:


                    Returns the channel string that is in the channel table at the index you
                    specify. Do not modify the contents of the channel string.

                    



get_ext_cal_last_date_and_time
------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_ext_cal_last_date_and_time()

            Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this method returns 14 for the **hour** parameter and 30 for the **minute** parameter.

            



            :rtype: datetime.datetime
            :return:


                    Indicates date and time of the last calibration.

                    



get_ext_cal_last_temp
---------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_ext_cal_last_temp()

            Returns the temperature at the last successful external calibration. The
            temperature is returned in degrees Celsius.

            



            :rtype: float
            :return:


                    Specifies the temperature at the last successful calibration in degrees
                    Celsius.

                    



get_ext_cal_recommended_interval
--------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_ext_cal_recommended_interval()

            Returns the recommended interval between external calibrations in
            months.

            



            :rtype: datetime.timedelta
            :return:


                    Specifies the recommended interval between external calibrations in
                    months.

                    



get_hardware_state
------------------

    .. py:currentmodule:: nifgen.Session

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



get_self_cal_last_date_and_time
-------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_self_cal_last_date_and_time()

            Returns the date and time of the last successful self-calibration.

            



            :rtype: datetime.datetime
            :return:


                    Returns the date and time the device was last calibrated.

                    



get_self_cal_last_temp
----------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_self_cal_last_temp()

            Returns the temperature at the last successful self-calibration. The
            temperature is returned in degrees Celsius.

            



            :rtype: float
            :return:


                    Specifies the temperature at the last successful calibration in degrees
                    Celsius.

                    



get_self_cal_supported
----------------------

    .. py:currentmodule:: nifgen.Session

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



import_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: import_attribute_configuration_buffer(configuration)

            Imports a property configuration to the session from the specified
            configuration buffer.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            

            .. note:: You cannot call this method while the session is in a running state,
                such as while generating a signal.



            :param configuration:


                Specifies the byte array buffer that contains the property
                configuration to import.

                


            :type configuration: bytes

import_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: import_attribute_configuration_file(file_path)

            Imports a property configuration to the session from the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            

            .. note:: You cannot call this method while the session is in a running state,
                such as while generating a signal.



            :param file_path:


                Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .nifgenconfig

                


            :type file_path: str

initiate
--------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: initiate()

            Initiates signal generation. If you want to abort signal generation,
            call the :py:meth:`nifgen.Session.abort` method. After the signal generation
            is aborted, you can call the :py:meth:`nifgen.Session.initiate` method to
            cause the signal generator to produce a signal again.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



is_done
-------

    .. py:currentmodule:: nifgen.Session

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



lock
----

    .. py:currentmodule:: nifgen.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`nifgen.Session.lock` method.
        -  A call to NI-FGEN locked the session.
        -  After a call to the :py:meth:`nifgen.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`nifgen.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`nifgen.Session.lock` method and the
           :py:meth:`nifgen.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nifgen.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nifgen.Session.lock` method with a call to
    the :py:meth:`nifgen.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with nifgen.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`nifgen.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited


query_arb_seq_capabilities
--------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: query_arb_seq_capabilities()

            Returns the properties of the signal generator that are related to
            creating arbitrary sequences (the :py:attr:`nifgen.Session.max_num_sequences`,
            :py:attr:`nifgen.Session.min_sequence_length`,
            :py:attr:`nifgen.Session.max_sequence_length`, and :py:attr:`nifgen.Session.max_loop_count`
            properties).

            



            :rtype: tuple (maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count)

                WHERE

                maximum_number_of_sequences (int): 


                    Returns the maximum number of arbitrary waveform sequences that the
                    signal generator allows. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_num_sequences` property.

                    


                minimum_sequence_length (int): 


                    Returns the minimum number of arbitrary waveforms the signal generator
                    allows in a sequence. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.min_sequence_length` property.

                    


                maximum_sequence_length (int): 


                    Returns the maximum number of arbitrary waveforms the signal generator
                    allows in a sequence. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_sequence_length` property.

                    


                maximum_loop_count (int): 


                    Returns the maximum number of times the signal generator can repeat an
                    arbitrary waveform in a sequence. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_loop_count` property.

                    



query_arb_wfm_capabilities
--------------------------

    .. py:currentmodule:: nifgen.Session

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
                    :py:attr:`nifgen.Session.max_num_waveforms` property.

                    


                waveform_quantum (int): 


                    The size (number of points) of each waveform must be a multiple of a
                    constant quantum value. This parameter obtains the quantum value that
                    the signal generator uses. NI-FGEN returns this value from the
                    :py:attr:`nifgen.Session.waveform_quantum` property.

                    For example, when this property returns a value of 8, all waveform
                    sizes must be a multiple of 8.

                    


                minimum_waveform_size (int): 


                    Returns the minimum number of points that the signal generator allows in
                    a waveform. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.min_waveform_size` property.

                    


                maximum_waveform_size (int): 


                    Returns the maximum number of points that the signal generator allows in
                    a waveform. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_waveform_size` property.

                    



query_freq_list_capabilities
----------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: query_freq_list_capabilities()

            Returns the properties of the signal generator that are related to
            creating frequency lists. These properties are
            :py:attr:`nifgen.Session.max_num_freq_lists`,
            :py:attr:`nifgen.Session.min_freq_list_length`,
            :py:attr:`nifgen.Session.max_freq_list_length`,
            :py:attr:`nifgen.Session.min_freq_list_duration`,
            :py:attr:`nifgen.Session.max_freq_list_duration`, and
            :py:attr:`nifgen.Session.freq_list_duration_quantum`.

            



            :rtype: tuple (maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum)

                WHERE

                maximum_number_of_freq_lists (int): 


                    Returns the maximum number of frequency lists that the signal generator
                    allows. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_num_freq_lists` property.

                    


                minimum_frequency_list_length (int): 


                    Returns the minimum number of steps that the signal generator allows in
                    a frequency list. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.min_freq_list_length` property.

                    


                maximum_frequency_list_length (int): 


                    Returns the maximum number of steps that the signal generator allows in
                    a frequency list. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_freq_list_length` property.

                    


                minimum_frequency_list_duration (float): 


                    Returns the minimum duration that the signal generator allows in a step
                    of a frequency list. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.min_freq_list_duration` property.

                    


                maximum_frequency_list_duration (float): 


                    Returns the maximum duration that the signal generator allows in a step
                    of a frequency list. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_freq_list_duration` property.

                    


                frequency_list_duration_quantum (float): 


                    Returns the quantum of which all durations must be a multiple in a
                    frequency list. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.freq_list_duration_quantum` property.

                    



read_current_temperature
------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: read_current_temperature()

            Reads the current onboard temperature of the device. The temperature is
            returned in degrees Celsius.

            



            :rtype: float
            :return:


                    Returns the current temperature read from onboard temperature sensors,
                    in degrees Celsius.

                    



reset
-----

    .. py:currentmodule:: nifgen.Session

    .. py:method:: reset()

            Resets the instrument to a known state. This method aborts the
            generation, clears all routes, and resets session properties to the
            default values. This method does not, however, commit the session
            properties or configure the device hardware to its default state.

            

            .. note:: For the NI 5401/5404/5411/5431, this method exhibits the same
                behavior as the :py:meth:`nifgen.Session.reset_device` method.



reset_device
------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: reset_device()

            Performs a hard reset on the device. Generation is stopped, all routes
            are released, external bidirectional terminals are tristated, FPGAs are
            reset, hardware is configured to its default state, and all session
            properties are reset to their default states.

            



reset_with_defaults
-------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: reset_with_defaults()

            Resets the instrument and reapplies initial user–specified settings from
            the logical name that was used to initialize the session. If the session
            was created without a logical name, this method is equivalent to the
            :py:meth:`nifgen.Session.reset` method.

            



self_cal
--------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: self_cal()

            Performs a full internal self-calibration on the device. If the
            calibration is successful, new calibration data and constants are stored
            in the onboard EEPROM.

            



self_test
---------

    .. py:currentmodule:: nifgen.Session

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



send_software_edge_trigger
--------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: send_software_edge_trigger(trigger, trigger_id)

            Sends a command to trigger the signal generator. This VI can act as an
            override for an external edge trigger.

            

            .. note:: This VI does not override external digital edge triggers of the
                NI 5401/5411/5431.



            :param trigger:


                Trigger specifies the type of software trigger to send

                +-----------------------------------+
                | Defined Values                    |
                +===================================+
                | :py:data:`~nifgen.Trigger.START`  |
                +-----------------------------------+
                | :py:data:`~nifgen.Trigger.SCRIPT` |
                +-----------------------------------+

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger: :py:data:`nifgen.Trigger`
            :param trigger_id:


                Trigger ID specifies the Script Trigger to use for triggering.

                


            :type trigger_id: str

set_next_write_position
-----------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: set_next_write_position(waveform_name_or_handle, relative_to, offset)

            Sets the position in the waveform at which the next waveform data is
            written. This method allows you to write to arbitrary locations within
            the waveform. These settings apply only to the next write to the
            waveform specified by the waveformHandle parameter. Subsequent writes to
            that waveform begin where the last write left off, unless this method
            is called again. The waveformHandle passed in must have been created by
            a call to the :py:meth:`nifgen.Session.allocate_waveform` method or one of the following
            :py:meth:`nifgen.Session.create_waveform` method.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].set_next_write_position(waveform_name_or_handle, relative_to, offset)


            :param waveform_name_or_handle:


                The name (str) or handle (int) of an arbitrary waveform previously allocated with :py:meth:`nifgen.Session.allocate_named_waveform`, :py:meth:`nifgen.Session.allocate_waveform` or :py:meth:`nifgen.Session.create_waveform`.

                


            :type waveform_name_or_handle: str or int
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

unlock
------

    .. py:currentmodule:: nifgen.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`nifgen.Session.lock`. Refer to :py:meth:`nifgen.Session.unlock` for additional
    information on session locks.



wait_until_done
---------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: wait_until_done(max_time=datetime.timedelta(seconds=10.0))

            Waits until the device is done generating or until the maximum time has
            expired.

            



            :param max_time:


                Specifies the timeout value in milliseconds.

                


            :type max_time: int in milliseconds or datetime.timedelta

write_script
------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: write_script(script)

            Writes a string containing one or more scripts that govern the
            generation of waveforms.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].write_script(script)


            :param script:


                Contains the text of the script you want to use for your generation
                operation. Refer to `scripting
                Instructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__
                for more information about writing scripts.

                


            :type script: str

write_waveform
--------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: write_waveform(waveform_name_or_handle, data)

            Writes data to the waveform in onboard memory.

            By default, subsequent calls to this method
            continue writing data from the position of the last sample written. You
            can set the write position and offset by calling the :py:meth:`nifgen.Session.set_next_write_position`
            :py:meth:`nifgen.Session.set_next_write_position` method.

            


            .. tip:: This method requires repeated capabilities (channels). If called directly on the
                nifgen.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                nifgen.Session repeated capabilities container, and calling this method on the result.:

                .. code:: python

                    session.channels[0,1].write_waveform(waveform_name_or_handle, data)


            :param waveform_name_or_handle:


                The name (str) or handle (int) of an arbitrary waveform previously allocated with :py:meth:`nifgen.Session.allocate_named_waveform`, :py:meth:`nifgen.Session.allocate_waveform` or :py:meth:`nifgen.Session.create_waveform`.

                


            :type waveform_name_or_handle: str or int
            :param data:


                Array of data to load into the waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.

                


            :type data: list of float


.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`niFgen_SetAttributeViInt32()`.

    Repeated capbilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

channels
--------

    .. py:attribute:: nifgen.Session.channels[]

        .. code:: python

            session.channels['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


script_triggers
---------------

    .. py:attribute:: nifgen.Session.script_triggers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.script_triggers['0-2'].channel_enabled = True

        passes a string of :python:`'ScriptTrigger0, ScriptTrigger1, ScriptTrigger2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.script_triggers['ScriptTrigger0-ScriptTrigger2'].channel_enabled = True

        passes a string of :python:`'ScriptTrigger0, ScriptTrigger1, ScriptTrigger2'` to the set attribute function.


markers
-------

    .. py:attribute:: nifgen.Session.markers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.markers['0-2'].channel_enabled = True

        passes a string of :python:`'Marker0, Marker1, Marker2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.markers['Marker0-Marker2'].channel_enabled = True

        passes a string of :python:`'Marker0, Marker1, Marker2'` to the set attribute function.



Properties
==========

absolute_delay
--------------

    .. py:attribute:: absolute_delay

        Specifies the sub-Sample Clock delay, in seconds, to apply to the
        waveform. Use this property to reduce the trigger jitter when
        synchronizing multiple devices with NI-TClk. This property can also help
        maintain synchronization repeatability by writing the absolute delay
        value of a previous measurement to the current session.
        To set this property, the waveform generator must be in the Idle
        (Configuration) state.
        **Units**: seconds (s)
        **Valid Values**: Plus or minus half of one Sample Clock period
        **Default Value**: 0.0
        **Supported Waveform Generators**: PXIe-5413/5423/5433



        .. note:: If this property is set, NI-TClk cannot perform any sub-Sample Clock
            adjustment.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Absolute Delay**
                - C Attribute: **NIFGEN_ATTR_ABSOLUTE_DELAY**

all_marker_events_latched_status
--------------------------------

    .. py:attribute:: all_marker_events_latched_status

        Returns a bit field of the latched status of all Marker Events.  Write 0 to this property to clear the latched status of all Marker Events.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Advanced:All Marker Events Latched Status**
                - C Attribute: **NIFGEN_ATTR_ALL_MARKER_EVENTS_LATCHED_STATUS**

all_marker_events_live_status
-----------------------------

    .. py:attribute:: all_marker_events_live_status

        Returns a bit field of the live status of all Marker Events.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Advanced:All Marker Events Live Status**
                - C Attribute: **NIFGEN_ATTR_ALL_MARKER_EVENTS_LIVE_STATUS**

analog_data_mask
----------------

    .. py:attribute:: analog_data_mask

        Specifies the mask to apply to the analog output. The masked data is replaced with the data in :py:attr:`nifgen.Session.analog_static_value`.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Data Mask:Analog Data Mask**
                - C Attribute: **NIFGEN_ATTR_ANALOG_DATA_MASK**

analog_filter_enabled
---------------------

    .. py:attribute:: analog_filter_enabled

        Controls whether the signal generator applies to an analog filter to the output signal. This property is valid in arbitrary waveform, arbitrary sequence, and script modes. This property can also be used in standard method and frequency list modes for user-defined waveforms.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Filters:Analog Filter Enabled**
                - C Attribute: **NIFGEN_ATTR_ANALOG_FILTER_ENABLED**

analog_path
-----------

    .. py:attribute:: analog_path

        Specifies the analog signal path that should be used. The main path allows you to configure gain, offset, analog filter status, output impedance, and output enable. The main path has two amplifier options, high- and low-gain.
        The direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The direct path also provides a smaller output range but also lower distortion. NI-FGEN normally chooses the amplifier based on the user-specified gain.

        The following table lists the characteristics of this property.

            +----------------+------------------+
            | Characteristic | Value            |
            +================+==================+
            | Datatype       | enums.AnalogPath |
            +----------------+------------------+
            | Permissions    | read-write       |
            +----------------+------------------+
            | Channel Based  | No               |
            +----------------+------------------+
            | Resettable     | Yes              |
            +----------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Analog Path**
                - C Attribute: **NIFGEN_ATTR_ANALOG_PATH**

analog_static_value
-------------------

    .. py:attribute:: analog_static_value

        Specifies the static value that replaces data masked by :py:attr:`nifgen.Session.analog_data_mask`.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Data Mask:Analog Static Value**
                - C Attribute: **NIFGEN_ATTR_ANALOG_STATIC_VALUE**

arb_gain
--------

    .. py:attribute:: arb_gain

        Specifies the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to scale the arbitrary waveform to other ranges.
        For example, when you set this property to 2.0, the output signal ranges from -2.0 V to +2.0 V.
        Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.ARB` or :py:data:`~nifgen.OutputMode.SEQ`.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Gain**
                - C Attribute: **NIFGEN_ATTR_ARB_GAIN**

arb_marker_position
-------------------

    .. py:attribute:: arb_marker_position

        Specifies the position for a marker to be asserted in the arbitrary waveform. This property defaults to -1 when no marker position is specified. Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.ARB`.
        Use :py:meth:`nifgen.Session.ExportSignal` to export the marker signal.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can use repeated capabilities (markers). If set or get directly on the
            nifgen.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nifgen.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.markers[0,1].arb_marker_position = var
                var = session.markers[0,1].arb_marker_position

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Waveform Mode:Marker Position**
                - C Attribute: **NIFGEN_ATTR_ARB_MARKER_POSITION**

arb_offset
----------

    .. py:attribute:: arb_offset

        Specifies the value that the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to shift the arbitrary waveform range.
        For example, when you set this property to 1.0, the output signal ranges from 2.0 V to 0.0 V.
        Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.ARB` or :py:data:`~nifgen.OutputMode.SEQ`.
        Units: Volts

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Offset**
                - C Attribute: **NIFGEN_ATTR_ARB_OFFSET**

arb_repeat_count
----------------

    .. py:attribute:: arb_repeat_count

        Specifies number of times to repeat the arbitrary waveform when the triggerMode parameter of :py:meth:`nifgen.Session.ConfigureTriggerMode` is set to :py:data:`~nifgen.TriggerMode.SINGLE` or :py:data:`~nifgen.TriggerMode.STEPPED`. This property is ignored if the triggerMode parameter is set to :py:data:`~nifgen.TriggerMode.CONTINUOUS` or :py:data:`~nifgen.TriggerMode.BURST`. Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.ARB`.
        When used during streaming, this property specifies the number of times to repeat the streaming waveform (the onboard memory allocated for streaming).  For more information about streaming, refer to the Streaming topic.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Waveform Mode:Repeat Count**
                - C Attribute: **NIFGEN_ATTR_ARB_REPEAT_COUNT**

arb_sample_rate
---------------

    .. py:attribute:: arb_sample_rate

        Specifies the rate at which the signal generator outputs the points in arbitrary waveforms.  Use this property when :py:attr:`nifgen.Session.output_mode` is set  to :py:data:`~nifgen.OutputMode.ARB` or :py:data:`~nifgen.OutputMode.SEQ`.
        Units: Samples/s

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock:Rate**
                - C Attribute: **NIFGEN_ATTR_ARB_SAMPLE_RATE**

arb_sequence_handle
-------------------

    .. py:attribute:: arb_sequence_handle

        This channel-based property identifies which sequence the signal generator produces. You can create multiple sequences using :py:meth:`nifgen.Session.create_arb_sequence`. :py:meth:`nifgen.Session.create_arb_sequence` returns a handle that you can use to identify the particular sequence. To configure the signal generator to produce a particular sequence, set this property to the sequence handle.
        Use this property only when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.SEQ`.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Arbitrary Sequence Handle**
                - C Attribute: **NIFGEN_ATTR_ARB_SEQUENCE_HANDLE**

arb_waveform_handle
-------------------

    .. py:attribute:: arb_waveform_handle

        Selects which arbitrary waveform the signal generator produces. You can create multiple arbitrary waveforms using one of the following niFgen Create Waveform methods:
        :py:meth:`nifgen.Session.create_waveform`
        :py:meth:`nifgen.Session.create_waveform`
        :py:meth:`nifgen.Session.create_waveform_from_file_i16`
        :py:meth:`nifgen.Session.create_waveform_from_file_f64`
        :py:meth:`nifgen.Session.CreateWaveformFromFileHWS`
        These methods return a handle that you can use to identify the particular waveform. To configure the signal generator to produce a particular waveform, set this property to the waveform handle.
        Use this property only when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.ARB`.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Waveform Mode:Arbitrary Waveform Handle**
                - C Attribute: **NIFGEN_ATTR_ARB_WAVEFORM_HANDLE**

aux_power_enabled
-----------------

    .. py:attribute:: aux_power_enabled

        Controls the specified auxiliary power pin. Setting this property to TRUE energizes the auxiliary power when the session is committed. When this property is FALSE, the power pin of the connector outputs no power.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Advanced:AUX Power Enabled**
                - C Attribute: **NIFGEN_ATTR_AUX_POWER_ENABLED**

bus_type
--------

    .. py:attribute:: bus_type

        The bus type of the signal generator.

        The following table lists the characteristics of this property.

            +----------------+---------------+
            | Characteristic | Value         |
            +================+===============+
            | Datatype       | enums.BusType |
            +----------------+---------------+
            | Permissions    | read only     |
            +----------------+---------------+
            | Channel Based  | No            |
            +----------------+---------------+
            | Resettable     | No            |
            +----------------+---------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Bus Type**
                - C Attribute: **NIFGEN_ATTR_BUS_TYPE**

channel_delay
-------------

    .. py:attribute:: channel_delay

        Specifies, in seconds, the delay to apply to the analog output of the channel specified by the channel string. You can use the channel delay to configure the timing relationship between channels on a multichannel device. Values for this property can be zero or positive. A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Channel Delay**
                - C Attribute: **NIFGEN_ATTR_CHANNEL_DELAY**

clock_mode
----------

    .. py:attribute:: clock_mode

        Controls which clock mode is used for the signal generator.
        For signal generators that support it, this property allows switching the sample  clock to High-Resolution mode. When in Divide-Down  mode, the sample rate can only be set to certain frequences, based on  dividing down the update clock. However, in High-Resolution mode, the  sample rate may be set to any value.

        The following table lists the characteristics of this property.

            +----------------+-----------------+
            | Characteristic | Value           |
            +================+=================+
            | Datatype       | enums.ClockMode |
            +----------------+-----------------+
            | Permissions    | read-write      |
            +----------------+-----------------+
            | Channel Based  | No              |
            +----------------+-----------------+
            | Resettable     | Yes             |
            +----------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock:Mode**
                - C Attribute: **NIFGEN_ATTR_CLOCK_MODE**

common_mode_offset
------------------

    .. py:attribute:: common_mode_offset

        Specifies, in volts, the value the signal generator adds to or subtracts from the arbitrary waveform data. This property applies only when you set the :py:attr:`nifgen.Session.terminal_configuration` property to :py:data:`~nifgen.TerminalConfiguration.DIFFERENTIAL`. Common mode offset is applied to the signals generated at each differential output terminal.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Common Mode Offset**
                - C Attribute: **NIFGEN_ATTR_COMMON_MODE_OFFSET**

data_marker_events_count
------------------------

    .. py:attribute:: data_marker_events_count

        Returns the number of Data Marker Events supported by the device.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Data Marker Events Count**
                - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENTS_COUNT**

data_marker_event_data_bit_number
---------------------------------

    .. py:attribute:: data_marker_event_data_bit_number

        Specifies the bit number to assign to the Data Marker Event.




        .. tip:: This property can use repeated capabilities (markers). If set or get directly on the
            nifgen.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nifgen.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.markers[0,1].data_marker_event_data_bit_number = var
                var = session.markers[0,1].data_marker_event_data_bit_number

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Data Marker:Data Bit Number**
                - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENT_DATA_BIT_NUMBER**

data_marker_event_level_polarity
--------------------------------

    .. py:attribute:: data_marker_event_level_polarity

        Specifies the output polarity of the Data marker event.




        .. tip:: This property can use repeated capabilities (markers). If set or get directly on the
            nifgen.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nifgen.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.markers[0,1].data_marker_event_level_polarity = var
                var = session.markers[0,1].data_marker_event_level_polarity

        The following table lists the characteristics of this property.

            +----------------+------------------------------------+
            | Characteristic | Value                              |
            +================+====================================+
            | Datatype       | enums.DataMarkerEventLevelPolarity |
            +----------------+------------------------------------+
            | Permissions    | read-write                         |
            +----------------+------------------------------------+
            | Channel Based  | No                                 |
            +----------------+------------------------------------+
            | Resettable     | Yes                                |
            +----------------+------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Data Marker:Level:Active Level**
                - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENT_LEVEL_POLARITY**

data_marker_event_output_terminal
---------------------------------

    .. py:attribute:: data_marker_event_output_terminal

        Specifies the destination terminal for the Data Marker Event.




        .. tip:: This property can use repeated capabilities (markers). If set or get directly on the
            nifgen.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nifgen.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.markers[0,1].data_marker_event_output_terminal = var
                var = session.markers[0,1].data_marker_event_output_terminal

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Data Marker:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENT_OUTPUT_TERMINAL**

data_transfer_block_size
------------------------

    .. py:attribute:: data_transfer_block_size

        The number of samples at a time to download to onboard memory. Useful when the total data to be transferred to onboard memory is large.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Data Transfer Block Size**
                - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_BLOCK_SIZE**

data_transfer_maximum_bandwidth
-------------------------------

    .. py:attribute:: data_transfer_maximum_bandwidth

        Specifies the maximum amount of bus bandwidth (in bytes per second) to use for data transfers. The signal generator limits data transfer speeds on the PCIe bus to the value you specify for this property. Set this property to optimize bus bandwidth usage for multi-device streaming applications by preventing the signal generator from consuming all of the available bandwidth on a PCI express link when waveforms are being written to the onboard memory of the device.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Maximum Bandwidth**
                - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH**

data_transfer_maximum_in_flight_reads
-------------------------------------

    .. py:attribute:: data_transfer_maximum_in_flight_reads

        Specifies the maximum number of concurrent PCI Express read requests the signal generator can issue.
        When transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this property is set to the highest value the signal generator supports.
        If other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the NI signal generator issues. This helps to reduce the amount of data the signal generator reads at one time.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Advanced:Maximum In-Flight Read Requests**
                - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS**

data_transfer_preferred_packet_size
-----------------------------------

    .. py:attribute:: data_transfer_preferred_packet_size

        Specifies the preferred size of the data field in a PCI Express read request packet. In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.
        Recommended values for this property are powers of two between 64 and 512.
        In some cases, the signal generator generates packets smaller than  the preferred size you set with this property.
        You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the :py:meth:`nifgen.Session.abort` method or wait for the generation to complete.



        .. note:: :

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Advanced:Preferred Packet Size**
                - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE**

digital_data_mask
-----------------

    .. py:attribute:: digital_data_mask

        Specifies the mask to apply to the output on the digital connector. The masked data is replaced with the data in :py:attr:`nifgen.Session.digital_static_value`.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Data Mask:Digital Data Mask**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_DATA_MASK**

digital_edge_script_trigger_edge
--------------------------------

    .. py:attribute:: digital_edge_script_trigger_edge

        Specifies the active edge for the Script trigger. This property is used when :py:attr:`nifgen.Session.script_trigger_type` is set to Digital Edge.




        .. tip:: This property can use repeated capabilities (script_triggers). If set or get directly on the
            nifgen.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nifgen.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.script_triggers[0,1].digital_edge_script_trigger_edge = var
                var = session.script_triggers[0,1].digital_edge_script_trigger_edge

        The following table lists the characteristics of this property.

            +----------------+------------------------------------+
            | Characteristic | Value                              |
            +================+====================================+
            | Datatype       | enums.ScriptTriggerDigitalEdgeEdge |
            +----------------+------------------------------------+
            | Permissions    | read-write                         |
            +----------------+------------------------------------+
            | Channel Based  | No                                 |
            +----------------+------------------------------------+
            | Resettable     | Yes                                |
            +----------------+------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Digital Edge:Edge**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE**

digital_edge_script_trigger_source
----------------------------------

    .. py:attribute:: digital_edge_script_trigger_source

        Specifies the source terminal for the Script trigger. This property is used when :py:attr:`nifgen.Session.script_trigger_type` is set to Digital Edge.




        .. tip:: This property can use repeated capabilities (script_triggers). If set or get directly on the
            nifgen.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nifgen.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.script_triggers[0,1].digital_edge_script_trigger_source = var
                var = session.script_triggers[0,1].digital_edge_script_trigger_source

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Digital Edge:Source**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE**

digital_edge_start_trigger_edge
-------------------------------

    .. py:attribute:: digital_edge_start_trigger_edge

        Specifies the active edge for the Start trigger. This property is used only when :py:attr:`nifgen.Session.start_trigger_type` is set to Digital Edge.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------------+
            | Characteristic | Value                             |
            +================+===================================+
            | Datatype       | enums.StartTriggerDigitalEdgeEdge |
            +----------------+-----------------------------------+
            | Permissions    | read-write                        |
            +----------------+-----------------------------------+
            | Channel Based  | No                                |
            +----------------+-----------------------------------+
            | Resettable     | Yes                               |
            +----------------+-----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Digital Edge:Edge**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

digital_edge_start_trigger_source
---------------------------------

    .. py:attribute:: digital_edge_start_trigger_source

        Specifies the source terminal for the Start trigger. This property is used only when :py:attr:`nifgen.Session.start_trigger_type` is set to Digital Edge.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Digital Edge:Source**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE**

digital_filter_enabled
----------------------

    .. py:attribute:: digital_filter_enabled

        Controls whether the signal generator applies a digital filter to the output signal. This property is valid in arbitrary waveform, arbitrary sequence, and script modes. This property can also be used in standard method and frequency list modes for user-defined waveforms.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Filters:Digital Filter Enabled**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_FILTER_ENABLED**

digital_filter_interpolation_factor
-----------------------------------

    .. py:attribute:: digital_filter_interpolation_factor

        This property only affects the device when :py:attr:`nifgen.Session.digital_filter_enabled` is set to True. If you do not set this property directly, NI-FGEN automatically selects the maximum interpolation factor allowed for the current sample rate. Valid values are 2, 4, and 8.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Filters:Digital Filter Interpolation Factor**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_FILTER_INTERPOLATION_FACTOR**

digital_gain
------------

    .. py:attribute:: digital_gain

        Specifies a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the DAC. For a digital gain greater than 1.0, the product of digital gain times the generated data must be inside the range plus or minus 1.0 (assuming floating point data).  If the product exceeds these limits, the signal generator clips the output signal, and an error results.
        Some signal generators support both digital gain and an analog gain (analog gain is specified with the :py:attr:`nifgen.Session.func_amplitude` property or the :py:attr:`nifgen.Session.arb_gain` property). Digital gain can be changed during generation without the glitches that may occur when changing analog gains, due to relay switching. However, the DAC output resolution is a method of analog gain, so only analog gain makes full use of the resolution of the DAC.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Digital Gain**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_GAIN**

digital_pattern_enabled
-----------------------

    .. py:attribute:: digital_pattern_enabled

        Controls whether the signal generator generates a digital pattern of the output signal.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Advanced:Digital Pattern Enabled**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_PATTERN_ENABLED**

digital_static_value
--------------------

    .. py:attribute:: digital_static_value

        Specifies the static value that replaces data masked by :py:attr:`nifgen.Session.digital_data_mask`.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Data Mask:Digital Static Value**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_STATIC_VALUE**

done_event_output_terminal
--------------------------

    .. py:attribute:: done_event_output_terminal

        Specifies the destination terminal for the Done Event.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Done:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_DONE_EVENT_OUTPUT_TERMINAL**

driver_setup
------------

    .. py:attribute:: driver_setup

        Specifies the driver setup portion of the option string that was passed into the :py:meth:`nifgen.Session.InitWithOptions` method.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIFGEN_ATTR_DRIVER_SETUP**

exported_onboard_reference_clock_output_terminal
------------------------------------------------

    .. py:attribute:: exported_onboard_reference_clock_output_terminal

        Specifies the terminal to which to export the Onboard Reference Clock.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Reference Clock:Onboard Reference Clock:Export Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL**

exported_reference_clock_output_terminal
----------------------------------------

    .. py:attribute:: exported_reference_clock_output_terminal

        Specifies the terminal to which to export the Reference Clock.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Reference Clock:Export Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL**

exported_sample_clock_divisor
-----------------------------

    .. py:attribute:: exported_sample_clock_divisor

        Specifies the factor by which to divide the Sample clock, also known as the Update clock, before it is exported.  To export the Sample clock, use the :py:meth:`nifgen.Session.ExportSignal` method or the  :py:attr:`nifgen.Session.exported_sample_clock_output_terminal` property.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock:Exported Sample Clock Divisor**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR**

exported_sample_clock_output_terminal
-------------------------------------

    .. py:attribute:: exported_sample_clock_output_terminal

        Specifies the terminal to which to export the Sample Clock.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock:Export Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL**

exported_sample_clock_timebase_divisor
--------------------------------------

    .. py:attribute:: exported_sample_clock_timebase_divisor

        Specifies the factor by which to divide the sample clock timebase (board clock) before it is exported.  To export the Sample clock timebase, use the :py:meth:`nifgen.Session.ExportSignal` method or the  :py:attr:`nifgen.Session.exported_sample_clock_timebase_output_terminal` property.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock Timebase:Exported Sample Clock Timebase Divisor**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR**

exported_sample_clock_timebase_output_terminal
----------------------------------------------

    .. py:attribute:: exported_sample_clock_timebase_output_terminal

        Specifies the terminal to which to export the Sample clock timebase. If you specify a divisor with the :py:attr:`nifgen.Session.exported_sample_clock_timebase_divisor` property,   the Sample clock exported with the :py:attr:`nifgen.Session.exported_sample_clock_timebase_output_terminal`  property is the value of the Sample clock timebase after it is divided-down.  For a list of the terminals available on your device, refer to the Device Routes tab in MAX.
        To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.



        .. note:: The signal generator must not be in the Generating state when you change this property.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock Timebase:Export Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL**

exported_script_trigger_output_terminal
---------------------------------------

    .. py:attribute:: exported_script_trigger_output_terminal

        Specifies the output terminal for the exported Script trigger.
        Setting this property to an empty string means that when you commit the session, the signal is removed from that terminal and, if possible, the terminal is tristated.




        .. tip:: This property can use repeated capabilities (script_triggers). If set or get directly on the
            nifgen.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nifgen.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.script_triggers[0,1].exported_script_trigger_output_terminal = var
                var = session.script_triggers[0,1].exported_script_trigger_output_terminal

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_start_trigger_output_terminal

        Specifies the destination terminal for exporting the Start trigger.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

external_clock_delay_binary_value
---------------------------------

    .. py:attribute:: external_clock_delay_binary_value

        Binary value of the external clock delay.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Advanced:External Clock Delay Binary Value**
                - C Attribute: **NIFGEN_ATTR_EXTERNAL_CLOCK_DELAY_BINARY_VALUE**

external_sample_clock_multiplier
--------------------------------

    .. py:attribute:: external_sample_clock_multiplier

        Specifies a multiplication factor to use to obtain a desired sample rate from an external Sample clock.  The resulting sample rate is equal to this factor multiplied by the external Sample clock rate.  You can use this property to generate samples at a rate higher than your external clock rate.  When using this property, you do not need to explicitly set the external clock rate.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Advanced:External Sample Clock Multiplier**
                - C Attribute: **NIFGEN_ATTR_EXTERNAL_SAMPLE_CLOCK_MULTIPLIER**

file_transfer_block_size
------------------------

    .. py:attribute:: file_transfer_block_size

        The number of samples at a time to read from the file and download to onboard memory. Used in conjunction with the Create From File and Write From File methods.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:File Transfer Block Size**
                - C Attribute: **NIFGEN_ATTR_FILE_TRANSFER_BLOCK_SIZE**

filter_correction_frequency
---------------------------

    .. py:attribute:: filter_correction_frequency

        Controls the filter correction frequency of the analog filter. This property corrects for the ripples in the analog filter frequency response at the frequency specified. For standard waveform output, the filter correction frequency should be set to be the same as the frequency of the standard waveform. To have no filter correction, set this property to 0 Hz.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:5401/5411/5431:Filter Correction Frequency**
                - C Attribute: **NIFGEN_ATTR_FILTER_CORRECTION_FREQUENCY**

flatness_correction_enabled
---------------------------

    .. py:attribute:: flatness_correction_enabled

        When True, the signal generator applies a flatness correction factor to the generated sine wave in order to ensure the same output power level at all frequencies.
        This property should be set to False when performing Flatness Calibration.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Filters:Flatness Correction Enabled**
                - C Attribute: **NIFGEN_ATTR_FLATNESS_CORRECTION_ENABLED**

fpga_bitfile_path
-----------------

    .. py:attribute:: fpga_bitfile_path

        Gets the absolute file path to the bitfile loaded on the FPGA.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:FPGA Bitfile Path**
                - C Attribute: **NIFGEN_ATTR_FPGA_BITFILE_PATH**

freq_list_duration_quantum
--------------------------

    .. py:attribute:: freq_list_duration_quantum

        Returns the quantum of which all durations must be a multiple in a  frequency list.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Frequency List Mode:Frequency List Duration Quantum**
                - C Attribute: **NIFGEN_ATTR_FREQ_LIST_DURATION_QUANTUM**

freq_list_handle
----------------

    .. py:attribute:: freq_list_handle

        Sets which frequency list the signal generator  produces. Create a frequency list using :py:meth:`nifgen.Session.create_freq_list`.  :py:meth:`nifgen.Session.create_freq_list` returns a handle that you can  use to identify the list.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Frequency List Mode:Frequency List Handle**
                - C Attribute: **NIFGEN_ATTR_FREQ_LIST_HANDLE**

func_amplitude
--------------

    .. py:attribute:: func_amplitude

        Controls the amplitude of the standard waveform that the  signal generator produces. This value is the amplitude at the  output terminal.
        For example, to produce a waveform ranging from -5.00 V to +5.00 V, set  the amplitude to 10.00 V.
        set the Waveform parameter to :py:data:`~nifgen.Waveform.DC`.
        Units: Vpk-pk



        .. note:: This parameter does not affect signal generator behavior when you

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Amplitude**
                - C Attribute: **NIFGEN_ATTR_FUNC_AMPLITUDE**

func_buffer_size
----------------

    .. py:attribute:: func_buffer_size

        This property contains the number of samples used in the standard method waveform  buffer. This property is only valid on devices that implement standard method mode  in software, and is read-only for all other devices.
        implementation of Standard Method Mode on your device.



        .. note:: Refer to the Standard Method Mode topic for more information on the

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Standard Function Mode:Buffer Size**
                - C Attribute: **NIFGEN_ATTR_FUNC_BUFFER_SIZE**

func_dc_offset
--------------

    .. py:attribute:: func_dc_offset

        Controls the DC offset of the standard waveform that the  signal generator produces.  This value is the offset at the output  terminal. The value is the offset from ground to the center of the  waveform that you specify with the Waveform parameter.
        For example, to configure a waveform with an amplitude of 10.00 V to  range from 0.00 V to +10.00 V, set DC Offset to 5.00 V.
        Units: volts

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:DC Offset**
                - C Attribute: **NIFGEN_ATTR_FUNC_DC_OFFSET**

func_duty_cycle_high
--------------------

    .. py:attribute:: func_duty_cycle_high

        Controls the duty cycle of the square wave the signal generator  produces. Specify this property as a percentage of  the time the square wave is high in a cycle.
        set the Waveform parameter to :py:data:`~nifgen.Waveform.SQUARE`.
        Units: Percentage of time the waveform is high



        .. note:: This parameter only affects signal generator behavior when you

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Duty Cycle High**
                - C Attribute: **NIFGEN_ATTR_FUNC_DUTY_CYCLE_HIGH**

func_frequency
--------------

    .. py:attribute:: func_frequency

        Controls the frequency of the standard waveform that the  signal generator produces.
        Units: hertz
        (1) This parameter does not affect signal generator behavior when you  set the Waveform parameter of the :py:meth:`nifgen.Session.configure_standard_waveform` method  to :py:data:`~nifgen.Waveform.DC`.
        (2) For :py:data:`~nifgen.Waveform.SINE`, the range is between 0 MHz and 16 MHz, but the  range is between 0 MHz and 1 MHz for all other waveforms.



        .. note:: :

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Standard Function Mode:Frequency**
                - C Attribute: **NIFGEN_ATTR_FUNC_FREQUENCY**

func_max_buffer_size
--------------------

    .. py:attribute:: func_max_buffer_size

        This property sets the maximum number of samples that can be used in the standard  method waveform buffer. Increasing this value may increase the quality of  the waveform. This property is only valid on devices that implement standard  method mode in software, and is read-only for all other devices.
        implementation of Standard Method Mode on your device.



        .. note:: Refer to the Standard Method Mode topic for more information on the

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Standard Function Mode:Maximum Buffer Size**
                - C Attribute: **NIFGEN_ATTR_FUNC_MAX_BUFFER_SIZE**

func_start_phase
----------------

    .. py:attribute:: func_start_phase

        Controls horizontal offset of the standard waveform the  signal generator produces. Specify this property in degrees of  one waveform cycle.
        A start phase of 180 degrees means output generation begins halfway  through the waveform. A start phase of 360 degrees offsets the output by  an entire waveform cycle, which is identical to a start phase of 0  degrees.
        set the Waveform parameter to :py:data:`~nifgen.Waveform.DC`.
        Units: Degrees of one cycle



        .. note:: This parameter does not affect signal generator behavior when you

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Start Phase**
                - C Attribute: **NIFGEN_ATTR_FUNC_START_PHASE**

func_waveform
-------------

    .. py:attribute:: func_waveform

        This channel-based property specifies which standard waveform the signal generator produces.
        Use this property only when :py:attr:`nifgen.Session.output_mode` is set to  :py:data:`~nifgen.OutputMode.FUNC`.
        :py:data:`~nifgen.Waveform.SINE`      - Sinusoid waveform
        :py:data:`~nifgen.Waveform.SQUARE`    - Square waveform
        :py:data:`~nifgen.Waveform.TRIANGLE`  - Triangle waveform
        :py:data:`~nifgen.Waveform.RAMP_UP`   - Positive ramp waveform
        :py:data:`~nifgen.Waveform.RAMP_DOWN` - Negative ramp waveform
        :py:data:`~nifgen.Waveform.DC`        - Constant voltage
        :py:data:`~nifgen.Waveform.NOISE`     - White noise
        :py:data:`~nifgen.Waveform.USER`      - User-defined waveform as defined with
        :py:meth:`nifgen.Session.define_user_standard_waveform`

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.Waveform |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+
            | Channel Based  | No             |
            +----------------+----------------+
            | Resettable     | No             |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Waveform**
                - C Attribute: **NIFGEN_ATTR_FUNC_WAVEFORM**

idle_behavior
-------------

    .. py:attribute:: idle_behavior

        Specifies the behavior of the output during the Idle state.  The output can be configured to hold the last generated voltage before entering the Idle state or jump to the Idle Value.

        The following table lists the characteristics of this property.

            +----------------+--------------------+
            | Characteristic | Value              |
            +================+====================+
            | Datatype       | enums.IdleBehavior |
            +----------------+--------------------+
            | Permissions    | read-write         |
            +----------------+--------------------+
            | Channel Based  | No                 |
            +----------------+--------------------+
            | Resettable     | Yes                |
            +----------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Advanced:Idle Behavior**
                - C Attribute: **NIFGEN_ATTR_IDLE_BEHAVIOR**

idle_value
----------

    .. py:attribute:: idle_value

        Specifies the value to generate in the Idle state.  The Idle Behavior must be configured to jump to this value.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Advanced:Idle Value**
                - C Attribute: **NIFGEN_ATTR_IDLE_VALUE**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        A string that contains the firmware revision information  for the device that you are currently using.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Firmware Revision**
                - C Attribute: **NIFGEN_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        A string that contains the name of the device manufacturer you are currently  using.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Manufacturer**
                - C Attribute: **NIFGEN_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        A string that contains the model number or name of the device that you  are currently using.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Model**
                - C Attribute: **NIFGEN_ATTR_INSTRUMENT_MODEL**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Indicates the resource descriptor that NI-FGEN uses to identify the physical device.
        If you initialize NI-FGEN with a logical name, this  property contains the resource descriptor that corresponds  to the entry in the IVI Configuration Utility.
        If you initialize NI-FGEN with the resource  descriptor, this property contains that value.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Advanced Session Information:Resource Descriptor**
                - C Attribute: **NIFGEN_ATTR_IO_RESOURCE_DESCRIPTOR**

load_impedance
--------------

    .. py:attribute:: load_impedance

        This channel-based property specifies the load impedance connected to the analog output of the channel. If you set this property to :py:data:`~nifgen.NIFGEN_VAL_MATCHED_LOAD_IMPEDANCE` (-1.0), NI-FGEN assumes that the load impedance matches the output impedance. NI-FGEN compensates to give the desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V).



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Load Impedance**
                - C Attribute: **NIFGEN_ATTR_LOAD_IMPEDANCE**

logical_name
------------

    .. py:attribute:: logical_name

        A string containing the logical name that you specified when opening the  current IVI session.
        You may pass a logical name to :py:meth:`nifgen.Session.init` or  :py:meth:`nifgen.Session.InitWithOptions`.  The IVI Configuration Utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NIFGEN_ATTR_LOGICAL_NAME**

marker_events_count
-------------------

    .. py:attribute:: marker_events_count

        Returns the number of markers supported by the device. Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.SCRIPT`.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Marker Events Count**
                - C Attribute: **NIFGEN_ATTR_MARKER_EVENTS_COUNT**

marker_event_output_terminal
----------------------------

    .. py:attribute:: marker_event_output_terminal

        Specifies the destination terminal for the Marker Event.




        .. tip:: This property can use repeated capabilities (markers). If set or get directly on the
            nifgen.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nifgen.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.markers[0,1].marker_event_output_terminal = var
                var = session.markers[0,1].marker_event_output_terminal

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_OUTPUT_TERMINAL**

max_freq_list_duration
----------------------

    .. py:attribute:: max_freq_list_duration

        Returns the maximum duration of any one step in the frequency  list.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Frequency List Mode:Maximum Frequency List Duration**
                - C Attribute: **NIFGEN_ATTR_MAX_FREQ_LIST_DURATION**

max_freq_list_length
--------------------

    .. py:attribute:: max_freq_list_length

        Returns the maximum number of steps that can be in a frequency  list.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Frequency List Mode:Maximum Frequency List Length**
                - C Attribute: **NIFGEN_ATTR_MAX_FREQ_LIST_LENGTH**

max_loop_count
--------------

    .. py:attribute:: max_loop_count

        Returns the maximum number of times that the signal generator can repeat a waveform in a sequence. Typically, this value is constant for the signal generator.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Max Loop Count**
                - C Attribute: **NIFGEN_ATTR_MAX_LOOP_COUNT**

max_num_freq_lists
------------------

    .. py:attribute:: max_num_freq_lists

        Returns the maximum number of frequency lists the signal generator allows.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Frequency List Mode:Maximum Number Of Frequency Lists**
                - C Attribute: **NIFGEN_ATTR_MAX_NUM_FREQ_LISTS**

max_num_sequences
-----------------

    .. py:attribute:: max_num_sequences

        Returns the maximum number of arbitrary sequences that the signal generator allows. Typically, this value is constant for the signal generator.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Max Number of Sequences**
                - C Attribute: **NIFGEN_ATTR_MAX_NUM_SEQUENCES**

max_num_waveforms
-----------------

    .. py:attribute:: max_num_waveforms

        Returns the maximum number of arbitrary waveforms that the signal generator allows. Typically, this value is constant for the signal generator.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Capabilities:Max Number of Waveforms**
                - C Attribute: **NIFGEN_ATTR_MAX_NUM_WAVEFORMS**

max_sequence_length
-------------------

    .. py:attribute:: max_sequence_length

        Returns the maximum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Max Sequence Length**
                - C Attribute: **NIFGEN_ATTR_MAX_SEQUENCE_LENGTH**

max_waveform_size
-----------------

    .. py:attribute:: max_waveform_size

        Returns the size, in samples, of the largest waveform that can be created. This property reflects the space currently available, taking into account previously allocated waveforms and instructions.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Capabilities:Max Waveform Size**
                - C Attribute: **NIFGEN_ATTR_MAX_WAVEFORM_SIZE**

memory_size
-----------

    .. py:attribute:: memory_size

        The total amount of memory, in bytes, on the signal generator.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Memory Size**
                - C Attribute: **NIFGEN_ATTR_MEMORY_SIZE**

min_freq_list_duration
----------------------

    .. py:attribute:: min_freq_list_duration

        Returns the minimum number of steps that can be in a frequency  list.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Frequency List Mode:Minimum Frequency List Duration**
                - C Attribute: **NIFGEN_ATTR_MIN_FREQ_LIST_DURATION**

min_freq_list_length
--------------------

    .. py:attribute:: min_freq_list_length

        Returns the minimum number of frequency lists that the signal generator allows.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Frequency List Mode:Minimum Frequency List Length**
                - C Attribute: **NIFGEN_ATTR_MIN_FREQ_LIST_LENGTH**

min_sequence_length
-------------------

    .. py:attribute:: min_sequence_length

        Returns the minimum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Min Sequence Length**
                - C Attribute: **NIFGEN_ATTR_MIN_SEQUENCE_LENGTH**

min_waveform_size
-----------------

    .. py:attribute:: min_waveform_size

        Returns the minimum number of points that the signal generator allows in an arbitrary waveform. Typically, this value is constant for the signal generator.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Capabilities:Min Waveform Size**
                - C Attribute: **NIFGEN_ATTR_MIN_WAVEFORM_SIZE**

module_revision
---------------

    .. py:attribute:: module_revision

        A string that contains the module revision  for the device that you are currently using.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Module Revision**
                - C Attribute: **NIFGEN_ATTR_MODULE_REVISION**

channel_count
-------------

    .. py:attribute:: channel_count

        Indicates the number of channels that the specific instrument  driver supports.
        For each property for which IVI_VAL_MULTI_CHANNEL is set, the IVI Engine maintains a separate cache value for each channel.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Capabilities:Channel Count**
                - C Attribute: **NIFGEN_ATTR_NUM_CHANNELS**

output_enabled
--------------

    .. py:attribute:: output_enabled

        This channel-based property specifies whether the signal that the signal generator produces appears at the output connector.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Output Enabled**
                - C Attribute: **NIFGEN_ATTR_OUTPUT_ENABLED**

output_impedance
----------------

    .. py:attribute:: output_impedance

        This channel-based property specifies the signal generator output impedance at the output connector. NI signal sources modules have an output impedance of 50 ohms and an optional 75 ohms on select modules. If the load impedance matches the output impedance, then the voltage at the signal output connector is at the needed level. The voltage at the signal output connector varies with load output impedance, up to doubling the voltage for a high-impedance load.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Output Impedance**
                - C Attribute: **NIFGEN_ATTR_OUTPUT_IMPEDANCE**

output_mode
-----------

    .. py:attribute:: output_mode

        Sets which output mode the signal generator will use. The value you specify determines which methods and properties you use to configure the waveform the signal generator produces.



        .. note:: The signal generator must not be in the Generating state when you change this property. To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.

        The following table lists the characteristics of this property.

            +----------------+------------------+
            | Characteristic | Value            |
            +================+==================+
            | Datatype       | enums.OutputMode |
            +----------------+------------------+
            | Permissions    | read-write       |
            +----------------+------------------+
            | Channel Based  | No               |
            +----------------+------------------+
            | Resettable     | No               |
            +----------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Output Mode**
                - C Attribute: **NIFGEN_ATTR_OUTPUT_MODE**

ready_for_start_event_output_terminal
-------------------------------------

    .. py:attribute:: ready_for_start_event_output_terminal

        Specifies the destination terminal for the Ready for Start Event.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Start:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL**

reference_clock_source
----------------------

    .. py:attribute:: reference_clock_source

        Specifies the reference clock source used by the signal generator.
        The signal generator derives the frequencies and sample rates that it uses  to generate waveforms from the source you specify.  For example, when you set this property to ClkIn, the signal  generator uses the signal it receives at the CLK IN front  panel connector as the Reference clock.
        To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.



        .. note:: The signal generator must not be in the Generating state when you change this property.

        The following table lists the characteristics of this property.

            +----------------+----------------------------+
            | Characteristic | Value                      |
            +================+============================+
            | Datatype       | enums.ReferenceClockSource |
            +----------------+----------------------------+
            | Permissions    | read-write                 |
            +----------------+----------------------------+
            | Channel Based  | No                         |
            +----------------+----------------------------+
            | Resettable     | Yes                        |
            +----------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Reference Clock:Source**
                - C Attribute: **NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE**

ref_clock_frequency
-------------------

    .. py:attribute:: ref_clock_frequency

        Sets the frequency of the signal generator reference  clock. The signal generator uses the reference clock to derive  frequencies and sample rates when generating output.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Reference Clock:Frequency**
                - C Attribute: **NIFGEN_ATTR_REF_CLOCK_FREQUENCY**

sample_clock_source
-------------------

    .. py:attribute:: sample_clock_source

        Specifies the Sample clock source. If you specify a divisor with the :py:attr:`nifgen.Session.exported_sample_clock_divisor`  property, the Sample clock exported with the :py:attr:`nifgen.Session.exported_sample_clock_output_terminal` property is the  value of the Sample clock after it is divided-down. For a list of the terminals available on your device, refer  to the Device Routes tab in MAX.
        To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.



        .. note:: The signal generator must not be in the Generating state when you change this property.

        The following table lists the characteristics of this property.

            +----------------+-------------------------+
            | Characteristic | Value                   |
            +================+=========================+
            | Datatype       | enums.SampleClockSource |
            +----------------+-------------------------+
            | Permissions    | read-write              |
            +----------------+-------------------------+
            | Channel Based  | No                      |
            +----------------+-------------------------+
            | Resettable     | Yes                     |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock:Source**
                - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE**

sample_clock_timebase_rate
--------------------------

    .. py:attribute:: sample_clock_timebase_rate

        Specifies the Sample clock timebase rate. This property applies only to external Sample clock timebases.
        To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.



        .. note:: The signal generator must not be in the Generating state when you change this property.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock Timebase:Rate**
                - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE**

sample_clock_timebase_source
----------------------------

    .. py:attribute:: sample_clock_timebase_source

        Specifies the Sample Clock Timebase source.
        To change the device configuration, call the :py:meth:`nifgen.Session.abort` method or wait for the generation to complete.



        .. note:: The signal generator must not be in the Generating state when you change this property.

        The following table lists the characteristics of this property.

            +----------------+---------------------------------+
            | Characteristic | Value                           |
            +================+=================================+
            | Datatype       | enums.SampleClockTimebaseSource |
            +----------------+---------------------------------+
            | Permissions    | read-write                      |
            +----------------+---------------------------------+
            | Channel Based  | No                              |
            +----------------+---------------------------------+
            | Resettable     | Yes                             |
            +----------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock Timebase:Source**
                - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE**

script_to_generate
------------------

    .. py:attribute:: script_to_generate

        Specifies which script the generator produces. To configure the generator to run a particular script, set this property to the name of the script. Use :py:meth:`nifgen.Session.write_script` to create multiple scripts. Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.SCRIPT`.



        .. note:: The signal generator must not be in the Generating state when you change this property. To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Script Mode:Script to Generate**
                - C Attribute: **NIFGEN_ATTR_SCRIPT_TO_GENERATE**

script_triggers_count
---------------------

    .. py:attribute:: script_triggers_count

        Specifies the number of Script triggers supported by the device. Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.SCRIPT`.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Script Triggers Count**
                - C Attribute: **NIFGEN_ATTR_SCRIPT_TRIGGERS_COUNT**

script_trigger_type
-------------------

    .. py:attribute:: script_trigger_type

        Specifies the Script trigger type. Depending upon the value of this property, additional properties may need to be configured to fully configure the trigger.




        .. tip:: This property can use repeated capabilities (script_triggers). If set or get directly on the
            nifgen.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            nifgen.Session repeated capabilities container, and calling set/get value on the result.:

            .. code:: python

                session.script_triggers[0,1].script_trigger_type = var
                var = session.script_triggers[0,1].script_trigger_type

        The following table lists the characteristics of this property.

            +----------------+-------------------------+
            | Characteristic | Value                   |
            +================+=========================+
            | Datatype       | enums.ScriptTriggerType |
            +----------------+-------------------------+
            | Permissions    | read-write              |
            +----------------+-------------------------+
            | Channel Based  | No                      |
            +----------------+-------------------------+
            | Resettable     | Yes                     |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Trigger Type**
                - C Attribute: **NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE**

serial_number
-------------

    .. py:attribute:: serial_number

        The signal generator's serial number.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Serial Number**
                - C Attribute: **NIFGEN_ATTR_SERIAL_NUMBER**

simulate
--------

    .. py:attribute:: simulate

        Specifies whether to simulate NI-FGEN I/O  operations. If simulation is enabled, NI-FGEN  methods perform range checking and call Ivi_GetAttribute and  Ivi_SetAttribute, but they do not perform device I/O.   For output parameters that represent device data, NI-FGEN  methods return calculated values.
        Default Value: False
        Use :py:meth:`nifgen.Session.InitWithOptions` to override default value.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NIFGEN_ATTR_SIMULATE**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        Returns a brief description of NI-FGEN.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Identification:Description**
                - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

major_version
-------------

    .. py:attribute:: major_version

        Returns the major version number of NI-FGEN.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Obsolete:Major Version**
                - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION**

minor_version
-------------

    .. py:attribute:: minor_version

        Returns the minor version number of NI-FGEN.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Obsolete:Minor Version**
                - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_MINOR_VERSION**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        A string that contains additional version information about  NI-FGEN.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Identification:Revision**
                - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        A string that contains the name of the vendor that supplies NI-FGEN.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Identification:Driver Vendor**
                - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_VENDOR**

started_event_output_terminal
-----------------------------

    .. py:attribute:: started_event_output_terminal

        Specifies the destination terminal for the Started Event.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Started:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_OUTPUT_TERMINAL**

start_trigger_type
------------------

    .. py:attribute:: start_trigger_type

        Specifies whether you want the Start trigger to be a Digital Edge, or Software trigger. You can also choose None as the value for this property.

        The following table lists the characteristics of this property.

            +----------------+------------------------+
            | Characteristic | Value                  |
            +================+========================+
            | Datatype       | enums.StartTriggerType |
            +----------------+------------------------+
            | Permissions    | read-write             |
            +----------------+------------------------+
            | Channel Based  | No                     |
            +----------------+------------------------+
            | Resettable     | Yes                    |
            +----------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Trigger Type**
                - C Attribute: **NIFGEN_ATTR_START_TRIGGER_TYPE**

streaming_space_available_in_waveform
-------------------------------------

    .. py:attribute:: streaming_space_available_in_waveform

        Indicates the space available (in samples) in the streaming waveform for writing new data. During generation, this available space may be in multiple locations with, for example, part of the available space at the end of the streaming waveform and the rest at the beginning. In this situation, writing a block of waveform data the size of the  total space available in the streaming waveform causes NI-FGEN to return an error, as  NI-FGEN will not wrap the data from the end of the waveform to the beginning and cannot write data past the end of the waveform buffer.
        To avoid writing data past the end of the waveform, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform.
        Used in conjunction with the :py:attr:`nifgen.Session.streaming_waveform_handle` or :py:attr:`nifgen.Session.streaming_waveform_name` properties.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Space Available in Streaming Waveform**
                - C Attribute: **NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM**

streaming_waveform_handle
-------------------------

    .. py:attribute:: streaming_waveform_handle

        Specifies the waveform handle of the waveform used to continuously stream data during generation. This property defaults to -1 when no streaming waveform is specified.
        Used in conjunction with :py:attr:`nifgen.Session.streaming_space_available_in_waveform`.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Handle**
                - C Attribute: **NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE**

streaming_waveform_name
-----------------------

    .. py:attribute:: streaming_waveform_name

        Specifies the name of the waveform used to continuously stream data during generation. This property defaults to // when no streaming waveform is specified.
        Use in conjunction with :py:attr:`nifgen.Session.streaming_space_available_in_waveform`.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Name**
                - C Attribute: **NIFGEN_ATTR_STREAMING_WAVEFORM_NAME**

streaming_write_timeout
-----------------------

    .. py:attribute:: streaming_write_timeout

        Specifies the maximum amount of time allowed to complete a streaming write operation.

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | No                                     |
            +----------------+----------------------------------------+
            | Resettable     | Yes                                    |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Streaming Write Timeout**
                - C Attribute: **NIFGEN_ATTR_STREAMING_WRITE_TIMEOUT**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        Returns a model code of the device. For NI-FGEN versions that support more than one device, this  property contains a comma-separated list of supported device  models.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NIFGEN_ATTR_SUPPORTED_INSTRUMENT_MODELS**

terminal_configuration
----------------------

    .. py:attribute:: terminal_configuration

        Specifies whether gain and offset values will be analyzed based on single-ended or differential operation.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------+
            | Characteristic | Value                       |
            +================+=============================+
            | Datatype       | enums.TerminalConfiguration |
            +----------------+-----------------------------+
            | Permissions    | read-write                  |
            +----------------+-----------------------------+
            | Channel Based  | No                          |
            +----------------+-----------------------------+
            | Resettable     | Yes                         |
            +----------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Terminal Configuration**
                - C Attribute: **NIFGEN_ATTR_TERMINAL_CONFIGURATION**

trigger_mode
------------

    .. py:attribute:: trigger_mode

        Controls the trigger mode.

        The following table lists the characteristics of this property.

            +----------------+-------------------+
            | Characteristic | Value             |
            +================+===================+
            | Datatype       | enums.TriggerMode |
            +----------------+-------------------+
            | Permissions    | read-write        |
            +----------------+-------------------+
            | Channel Based  | No                |
            +----------------+-------------------+
            | Resettable     | No                |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Trigger Mode**
                - C Attribute: **NIFGEN_ATTR_TRIGGER_MODE**

wait_behavior
-------------

    .. py:attribute:: wait_behavior

        Specifies the behavior of the output while waiting for a script trigger or during a wait instruction.  The output can be configured to hold the last generated voltage before waiting or jump to the Wait Value.

        The following table lists the characteristics of this property.

            +----------------+--------------------+
            | Characteristic | Value              |
            +================+====================+
            | Datatype       | enums.WaitBehavior |
            +----------------+--------------------+
            | Permissions    | read-write         |
            +----------------+--------------------+
            | Channel Based  | No                 |
            +----------------+--------------------+
            | Resettable     | Yes                |
            +----------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Advanced:Wait Behavior**
                - C Attribute: **NIFGEN_ATTR_WAIT_BEHAVIOR**

wait_value
----------

    .. py:attribute:: wait_value

        Specifies the value to generate while waiting.  The Wait Behavior must be configured to jump to this value.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Advanced:Wait Value**
                - C Attribute: **NIFGEN_ATTR_WAIT_VALUE**

waveform_quantum
----------------

    .. py:attribute:: waveform_quantum

        The size of each arbitrary waveform must be a multiple of a quantum value. This property returns the quantum value that the signal generator allows.
        For example, when this property returns a value of 8, all waveform sizes must be a multiple of 8. Typically, this value is constant for the signal generator.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arbitrary Waveform:Capabilities:Waveform Quantum**
                - C Attribute: **NIFGEN_ATTR_WAVEFORM_QUANTUM**


NI-TClk Support
===============

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:attr:`nitclk.SessionReference` for a complete list of attributes.


.. contents:: Session


