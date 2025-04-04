.. py:module:: nirfsg

Session
=======

.. py:class:: Session(self, resource_name, id_query, reset_device, options={})

    

    Opens a session to the device you specify as the :py:attr:`nirfsg.Session.RESOURCE_NAME` and returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls. This method also configures the device through the :py:attr:`nirfsg.Session.OPTION_STRING` input.

    

    .. note:: For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending /*ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

    .. note:: One or more of the referenced properties are not in the Python API for this driver.



    :param resource_name:
        

        Specifies the resource name of the device to initialize.

        


    :type resource_name: str

    :param id_query:
        

        Specifies whether you want NI-RFSG to perform an ID query.

        


    :type id_query: bool

    :param reset_device:
        

        Specifies whether you want to reset the NI-RFSG device during the initialization procedure.

        


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


    :type options: str


Methods
=======

abort
-----

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: abort()

            Stops signal generation.

            



allocate_arb_waveform
---------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: allocate_arb_waveform(waveform_name, size_in_samples)

            Allocates onboard memory space for the arbitrary waveform. Use this method to specify the total size of a waveform before writing the data. Use this method only if you are calling the :py:meth:`nirfsg.Session.WriteArbWaveform` method multiple times to write a large waveform in smaller blocks. The NI-RFSG device must be in the Configuration state before you call this method.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :param waveform_name:


                Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

                


            :type waveform_name: str
            :param size_in_samples:


                Specifies the number of samples to reserve in the onboard memory for the specified waveform. Each I/Q pair is considered one sample.

                


            :type size_in_samples: int

change_external_calibration_password
------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: change_external_calibration_password(old_password, new_password)

            Changes the external calibration password of the device.

            



            :param old_password:


                Specifies the old (current) external calibration password. This password is case sensitive.

                


            :type old_password: str
            :param new_password:


                Specifies the new (desired) external calibration password.

                


            :type new_password: str

check_attribute_vi_boolean
--------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: check_attribute_vi_boolean(attribute, value)

            Checks the validity of a value you specify for a ViBoolean property.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_boolean`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

                Example: :py:meth:`my_session.check_attribute_vi_boolean`


            :param attribute:


                Pass the ID of a property.

                


            :type attribute: int
            :param value:


                Pass the value that you want to verify as a valid value for the property.

                


            :type value: bool

check_attribute_vi_int32
------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: check_attribute_vi_int32(attribute, value)

            Checks the validity of a value you specify for a ViInt32 property.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_int32`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

                Example: :py:meth:`my_session.check_attribute_vi_int32`


            :param attribute:


                Pass the ID of a property.

                


            :type attribute: int
            :param value:


                Pass the value that you want to verify as a valid value for the property.

                


            :type value: int

check_attribute_vi_int64
------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: check_attribute_vi_int64(attribute, value)

            Checks the validity of a value you specify for a ViInt64 property.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_int64`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

                Example: :py:meth:`my_session.check_attribute_vi_int64`


            :param attribute:


                Pass the ID of a property.

                


            :type attribute: int
            :param value:


                Pass the value that you want to verify as a valid value for the property.

                


            :type value: int

check_attribute_vi_real64
-------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: check_attribute_vi_real64(attribute, value)

            Checks the validity of a value you specify for a ViReal64 property.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_real64`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

                Example: :py:meth:`my_session.check_attribute_vi_real64`


            :param attribute:


                Pass the ID of a property.

                


            :type attribute: int
            :param value:


                Pass the value that you want to verify as a valid value for the property.

                


            :type value: float

check_attribute_vi_session
--------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: check_attribute_vi_session(attribute)

            Checks the validity of a value you specify for a ViSession property.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_session`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

                Example: :py:meth:`my_session.check_attribute_vi_session`


            :param attribute:


                Pass the ID of a property.

                


            :type attribute: int

check_attribute_vi_string
-------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: check_attribute_vi_string(attribute, value)

            Checks the validity of a value you specify for a ViString property.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].check_attribute_vi_string`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

                Example: :py:meth:`my_session.check_attribute_vi_string`


            :param attribute:


                Pass the ID of a property.

                


            :type attribute: int
            :param value:


                Pass the value that you want to verify as a valid value for the property. The value must be a NULL-terminated string.

                


            :type value: str

check_generation_status
-----------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: check_generation_status()

            Checks the status of the generation. Call this method to check for any errors that might occur during the signal generation or to check whether the device has finished generating.

            



            :rtype: bool
            :return:


                    Returns information about the completion of signal generation.

                    



check_if_script_exists
----------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: check_if_script_exists(script_name)

            Returns whether the script that you specify as :py:attr:`nirfsg.Session.SCRIPT_NAME` exists.

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :param script_name:


                Specifies the name of the script. This string is case-insensitive.

                


            :type script_name: str

            :rtype: bool
            :return:


                    Returns True if the script exists.

                    



check_if_waveform_exists
------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: check_if_waveform_exists(waveform_name)

            Returns whether the waveform that you specify as :py:attr:`nirfsg.Session.WAVEFORM_NAME` exists.

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :param waveform_name:


                Specifies the name used to store the waveform. This string is case-insensitive.

                


            :type waveform_name: str

            :rtype: bool
            :return:


                    Returns True if the waveform exists.

                    



clear_all_arb_waveforms
-----------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: clear_all_arb_waveforms()

            Deletes all currently defined waveforms and scripts. The NI-RFSG device must be in the Configuration state before you call this method.

            



clear_arb_waveform
------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: clear_arb_waveform(name)

            Deletes a specified waveform from the pool of currently defined waveforms. The NI-RFSG device must be in the Configuration state before you call this method.

            



            :param name:


                Name of the stored waveform to delete.

                


            :type name: str

clear_error
-----------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: clear_error()

            Clears the error information associated with the session. If you pass VI_NULL for the :py:attr:`nirfsg.Session.VI` parameter, this method clears the error information for the current execution thread.

            

            .. note:: The :py:meth:`nirfsg.Session.get_error` method clears the error information after it is retrieved. A call to the :py:meth:`nirfsg.Session.clear_error` method is necessary only when you do not use a call to the :py:meth:`nirfsg.Session.get_error` method to retrieve error information.

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



clear_self_calibrate_range
--------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: clear_self_calibrate_range()

            Clears the data obtained from the :py:meth:`nirfsg.Session.self_calibrate_range` method.

            



close
-----

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: close()

            Aborts any signal generation in progress and destroys the instrument driver session.

            

            .. note:: After calling this method, you cannot use NI-RFSG again until you call the :py:meth:`nirfsg.Session.Init` method or the :py:meth:`nirfsg.Session.__init__` method.

            .. note:: One or more of the referenced methods are not in the Python API for this driver.

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: commit()

            Programs the device with the correct settings. Calling this method moves the NI-RFSG device from the Configuration state to the Committed state. After this method executes, a change to any property reverts the NI-RFSG device to the Configuration state.

            



configure_deembedding_table_interpolation_linear
------------------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_deembedding_table_interpolation_linear(port, table_name, format)

            Selects the linear interpolation method. If the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is '' (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str
            :param format:


                Specifies the format of parameters to interpolate.

                


            :type format: :py:data:`nirfsg.Format`

configure_deembedding_table_interpolation_nearest
-------------------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_deembedding_table_interpolation_nearest(port, table_name)

            Selects the nearest interpolation method. NI-RFSG uses the parameters of the table nearest to the carrier frequency for de-embedding.

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is '' (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str

configure_deembedding_table_interpolation_spline
------------------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_deembedding_table_interpolation_spline(port, table_name)

            Selects the spline interpolation method. If the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is '' (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str

configure_digital_edge_script_trigger
-------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_digital_edge_script_trigger(trigger_id, source, edge)

            Configures the specified Script Trigger for digital edge triggering. The NI-RFSG device must be in the Configuration state before calling this method.

            



            :param trigger_id:


                Specifies the Script Trigger to configure.

                


            :type trigger_id: str
            :param source:


                Specifies the source terminal for the digital edge Script Trigger. NI-RFSG sets the :py:attr:`nirfsg.Session.digital_edge_script_trigger_source` property to this value.

                


            :type source: str
            :param edge:


                Specifies the active edge for the digital edge Script Trigger. NI-RFSG sets the :py:attr:`nirfsg.Session.digital_edge_script_trigger_edge` property to this value.

                


            :type edge: int

configure_digital_edge_start_trigger
------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_digital_edge_start_trigger(source, edge)

            Configures the Start Trigger for digital edge triggering. The NI-RFSG device must be in the Configuration state before calling this method.

            

            .. note:: For the PXIe-5654/5654 with PXIe-5696, the Start Trigger is valid only with a timer-based list when RF list mode is enabled.



            :param source:


                Specifies the source terminal for the digital edge trigger. NI-RFSG sets the :py:attr:`nirfsg.Session.digital_edge_start_trigger_source` property to this value.

                


            :type source: str
            :param edge:


                Specifies the active edge for the Start Trigger. NI-RFSG sets the :py:attr:`nirfsg.Session.digital_edge_start_trigger_edge` property to this value.

                


            :type edge: int

configure_digital_level_script_trigger
--------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_digital_level_script_trigger(trigger_id, source, level)

            Configures a specified Script Trigger for digital level triggering. The NI-RFSG device must be in the Configuration state before calling this method.

            



            :param trigger_id:


                Specifies the Script Trigger to configure.

                


            :type trigger_id: str
            :param source:


                Specifies the trigger source terminal for the digital level Script Trigger. NI-RFSG sets the :py:attr:`nirfsg.Session.digital_level_script_trigger_source` property to this value.

                


            :type source: str
            :param level:


                Specifies the active level for the digital level Script Trigger. NI-RFSG sets the :py:attr:`nirfsg.Session.digital_level_script_trigger_active_level` property to this value.

                


            :type level: int

configure_digital_modulation_user_defined_waveform
--------------------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_digital_modulation_user_defined_waveform(number_of_samples, user_defined_waveform)

            Specifies the message signal used for digital modulation when the :py:attr:`nirfsg.Session.digital_modulation_waveform_type` property is set to :py:data:`~nirfsg.NIRFSG_VAL_USER_DEFINED`.

            

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



            :param number_of_samples:


                Specifies the number of samples in the message signal.

                


            :type number_of_samples: int
            :param user_defined_waveform:


                Specifies the user-defined message signal used for digital modulation.

                


            :type user_defined_waveform: list of int

configure_generation_mode
-------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_generation_mode(generation_mode)

            Configures the NI-RFSG device to generate a continuous sine tone (CW), apply I/Q (vector) modulation to the RF output signal, or generate arbitrary waveforms according to scripts. The NI-RFSG device must be in the Configuration state before you call this method.

            



            :param generation_mode:


                Specifies the mode used by NI-RFSG for generating an RF output signal.

                


            :type generation_mode: int

configure_output_enabled
------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_output_enabled(output_enabled)

            Enables or disables signal output. Setting :py:attr:`nirfsg.Session.output_enabled` to False while in the Generation state attenuates the generated signal so that no signal is output.

            



            :param output_enabled:


                Specifies whether you want to enable or disable the output.

                


            :type output_enabled: bool

configure_p2_p_endpoint_fullness_start_trigger
----------------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_p2_p_endpoint_fullness_start_trigger(p2p_endpoint_fullness_level)

            Configures the Start Trigger to detect peer-to-peer endpoint fullness. Generation begins when the number of samples in the peer-to-peer endpoint reaches the threshold specified by the :py:attr:`nirfsg.Session.P2P_ENDPOINT_FULLNESS_LEVEL` parameter. The NI-RFSG device must be in the Configuration state before calling this method.

            

            .. note:: Due to an additional internal FIFO in the RF signal generator, the writer peer actually writes 2,304 bytes more than the quantity of data specified by this method to satisfy the trigger level.

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :param p2p_endpoint_fullness_level:


                Specifies the quantity of data in the FIFO endpoint that asserts the trigger. Units are samples per channel. The default value is -1, which allows NI-RFSG to select the appropriate fullness value.

                


            :type p2p_endpoint_fullness_level: int

configure_power_level_type
--------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_power_level_type(power_level_type)

            Specifies the way the driver interprets the :py:attr:`nirfsg.Session.power_level` property. In average power mode, NI-RFSG automatically scales waveform data to use the maximum dynamic range. In peak power mode, waveforms are scaled according to the :py:attr:`nirfsg.Session.arb_waveform_software_scaling_factor` property.

            



            :param power_level_type:


                Specifies the way the driver interprets the value of the :py:attr:`nirfsg.Session.power_level` property. NI-RFSG sets the :py:attr:`nirfsg.Session.power_level_type` property to this value.

                


            :type power_level_type: int

configure_pxi_chassis_clk10
---------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_pxi_chassis_clk10(pxi_clk10_source)

            Specifies the signal to drive the 10MHz Reference Clock on the PXI backplane. This option can only be configured when the PXI-5610 is in Slot 2 of the PXI chassis. The NI-RFSG device must be in the Configuration state before you call this method.

            



            :param pxi_clk10_source:


                Specifies the source of the Reference Clock signal.

                


            :type pxi_clk10_source: str

configure_ref_clock
-------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_ref_clock(ref_clock_source, ref_clock_rate)

            Configures the NI-RFSG device Reference Clock. The Reference Clock ensures that the NI-RFSG devices are operating from a common timebase. The NI-RFSG device must be in the Configuration state before calling this method.

            



            :param ref_clock_source:


                Specifies the source of Reference Clock signal.

                


            :type ref_clock_source: str
            :param ref_clock_rate:


                Specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. The default value is :py:data:`~nirfsg.NIRFSG_VAL_AUTO`, which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. This parameter is only valid when the :py:attr:`nirfsg.Session.ref_clock_source` parameter is set to :py:data:`~nirfsg.NIRFSG_VAL_CLK_IN_STR`, :py:data:`~nirfsg.NIRFSG_VAL_REF_IN_STR` or :py:data:`~nirfsg.ReferenceClockSource.REF_IN_2`. Refer to the :py:attr:`nirfsg.Session.ref_clock_rate` property for possible values.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type ref_clock_rate: float

configure_rf
------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_rf(frequency, power_level)

            Configures the frequency and power level of the RF output signal. The PXI-5670/5671, PXIe-5672, and PXIe-5860 device must be in the Configuration state before calling this method. The PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 device can be in the Configuration or Generation state when you call this method.

            



            :param frequency:


                Specifies the frequency of the generated RF signal, in hertz. For arbitrary waveform generation, this parameter specifies the center frequency of the signal.

                


            :type frequency: float
            :param power_level:


                Specifies either the average power level or peak power level of the generated RF signal, depending on the :py:attr:`nirfsg.Session.power_level_type` property.

                


            :type power_level: float

configure_signal_bandwidth
--------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_signal_bandwidth(signal_bandwidth)

            Configures the signal bandwidth of the arbitrary waveform. The NI-RFSG device must be in the Configuration state before you call this method. Based on your signal bandwidth, NI-RFSG decides whether to configure the upconverter center frequency on the PXI-5670/5671 or PXIe-5672 in increments of 1MHz or 5MHz. Failure to configure signal bandwidth may result in the signal being placed outside the upconverter passband.

            



            :param signal_bandwidth:


                Specifies the signal bandwidth used by NI-RFSG to generate an RF output signal. NI-RFSG sets the :py:attr:`nirfsg.Session.signal_bandwidth` property to this value.

                


            :type signal_bandwidth: float

configure_software_script_trigger
---------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_software_script_trigger(trigger_id)

            Configures the Script Trigger for software triggering. Refer to the :py:meth:`nirfsg.Session.send_software_edge_trigger` method for more information about using the software Script Trigger. The NI-RFSG device must be in the Configuration state before calling this method.

            



            :param trigger_id:


                Specifies the Script Trigger to configure.

                


            :type trigger_id: str

configure_software_start_trigger
--------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: configure_software_start_trigger()

            Configures the Start Trigger for software triggering. Refer to the :py:meth:`nirfsg.Session.send_software_edge_trigger` method for more information about using a software trigger. The NI-RFSG device must be in the Configuration state before calling this method.

            



create_deembedding_sparameter_table_s2_p_file
---------------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: create_deembedding_sparameter_table_s2_p_file(port, table_name, s2p_file_path, sparameter_orientation)

            Creates an S-parameter de-embedding table for the port based on the specified S2P file.

            



            :param port:


                yet to be defined

                


            :type port: str
            :param table_name:


                yet to be defined

                


            :type table_name: str
            :param s2p_file_path:


                yet to be defined

                


            :type s2p_file_path: str
            :param sparameter_orientation:


                yet to be defined

                


            :type sparameter_orientation: int

delete_all_deembedding_tables
-----------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: delete_all_deembedding_tables()

            Deletes all configured de-embedding tables for the session.

            



delete_deembedding_table
------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: delete_deembedding_table(port, table_name)

            Deletes the selected de-embedding table for a given port.

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is '' (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str

disable
-------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: disable()

            Places the instrument in a quiescent state where it has minimal or no impact on the system to which it is connected.

            



disable_script_trigger
----------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: disable_script_trigger(trigger_id)

            Configures the device not to wait for the specified Script Trigger. Call this method only if you previously configured a Script Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before you call this method.

            



            :param trigger_id:


                Specifies the Script trigger to configure.

                


            :type trigger_id: str

disable_start_trigger
---------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: disable_start_trigger()

            Configures the device not to wait for a Start Trigger. This method is necessary only if you previously configured a Start Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before calling this method.

            



export_signal
-------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: export_signal(signal, signal_identifier, output_terminal)

            Routes signals (triggers, clocks, and events) to a specified output terminal. The NI-RFSG device must be in the Configuration state before you call this method.

            



            :param signal:


                Specifies the type of signal to route.

                


            :type signal: int
            :param signal_identifier:


                Specifies which instance of the selected signal to export. This parameter is useful when you set the :py:attr:`nirfsg.Session.SIGNAL` parameter to :py:data:`~nirfsg.NIRFSG_VAL_SCRIPT_TRIGGER` or :py:data:`~nirfsg.NIRFSG_VAL_MARKER_EVENT`. Otherwise, set the :py:attr:`nirfsg.Session.SIGNAL_IDENTIFIER` parameter to '' (empty string).

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type signal_identifier: str
            :param output_terminal:


                Specifies the terminal where the signal is exported. You can choose not to export any signal. For the PXIe-5841 with PXIe-5655, the signal is exported to the terminal on the PXIe-5841.

                


            :type output_terminal: str

get_error
---------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: get_error()

            Retrieves and then clears the IVI error information for the session or the current execution thread.

            

            .. note:: If the **bufferSize** parameter is 0, this method does not clear the error information. By passing 0 to the **bufferSize** parameter, you can determine the buffer size required to obtain the entire :py:attr:`nirfsg.Session.ERROR_DESCRIPTION` string. You can then call this method again with a sufficiently large buffer. If you specify a valid IVI session for the :py:attr:`nirfsg.Session.VI` parameter, this method retrieves and clears the error information for the session. If you pass VI_NULL for the :py:attr:`nirfsg.Session.VI` parameter, this method retrieves and clears the error information for the current execution thread. If the :py:attr:`nirfsg.Session.VI` parameter is an invalid session, this method does nothing and returns an error. Normally, the error information describes the first error that occurred since the user last called this method or the :py:meth:`nirfsg.Session.clear_error` method.

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :rtype: tuple (error_code, error_description)

                WHERE

                error_code (int): 


                    Returns the error code for the session or execution thread. If you pass 0 for the **BufferSize** parameter, you can pass VI_NULL for this parameter.

                    


                error_description (str): 


                    Returns the :py:attr:`nirfsg.Session.ERROR_DESCRIPTION` for the IVI session or execution thread.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



get_external_calibration_last_date_and_time
-------------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: get_external_calibration_last_date_and_time()

            Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this method returns 14 for the hours parameter and 30 for the minutes parameter.

            



            :rtype: tuple (year, month, day, hour, minute, second)

                WHERE

                year (int): 


                    Returns the year of the last successful calibration.

                    


                month (int): 


                    Returns the month of the last successful calibration.

                    


                day (int): 


                    Returns the day of the last successful calibration.

                    


                hour (int): 


                    Returns the hour of the last successful calibration.

                    


                minute (int): 


                    Returns the minute of the last successful calibration.

                    


                second (int): 


                    Returns the second of the last successful calibration.

                    



get_max_settable_power
----------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: get_max_settable_power()

            Returns the maximum settable output power level for the current configuration.

            



            :rtype: float
            :return:


                    Returns maximum settable power level in dBm.

                    



get_self_calibration_date_and_time
----------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: get_self_calibration_date_and_time(module)

            Returns the date and time of the last successful self-calibration. The time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this method returns 14 for the hours parameter and 30 for the minutes parameter.

            



            :param module:


                Specifies from which stand-alone module to retrieve the last successful self-calibration date and time.

                


            :type module: int

            :rtype: tuple (year, month, day, hour, minute, second)

                WHERE

                year (int): 


                    Returns the year of the last successful calibration.

                    


                month (int): 


                    Returns the month of the last successful calibration.

                    


                day (int): 


                    Returns the day of the last successful calibration.

                    


                hour (int): 


                    Returns the hour of the last successful calibration.

                    


                minute (int): 


                    Returns the minute of the last successful calibration.

                    


                second (int): 


                    Returns the second of the last successful calibration.

                    



get_self_calibration_temperature
--------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: get_self_calibration_temperature(module)

            Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

            



            :param module:


                Specifies from which stand-alone module to retrieve the last successful self-calibration temperature.

                


            :type module: int

            :rtype: float
            :return:


                    Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

                    



get_stream_endpoint_handle
--------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: get_stream_endpoint_handle(stream_endpoint)

            Returns a reader endpoint handle that can be used with NI-P2P to configure a peer-to-peer stream with an RF signal generator endpoint.

            



            :param stream_endpoint:


                Specifies the stream endpoint FIFO to configure.

                


            :type stream_endpoint: str

            :rtype: int
            :return:


                    Returns the reader endpoint handle that is used with NI-P2P to create a stream with the NI-RFSG device as an endpoint.

                    



initiate
--------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: initiate()

            Initiates signal generation, causing the NI-RFSG device to leave the Configuration state and enter the Generation state. If the settings have not been committed to the device before you call this method, they are committed by this method. The operation returns when the RF output signal settles. To return to the Configuration state, call the :py:meth:`nirfsg.Session.abort` method.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



load_configurations_from_file
-----------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: load_configurations_from_file(file_path)

            Loads the configurations from the specified file to the NI-RFSG driver session. The VI does an implicit reset before loading the configurations from the file.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].load_configurations_from_file`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

                Example: :py:meth:`my_session.load_configurations_from_file`


            :param file_path:


                Specifies the absolute path of the file from which the NI-RFSG loads the configurations.

                


            :type file_path: str

lock
----

    .. py:currentmodule:: nirfsg.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`nirfsg.Session.lock` method.
        -  A call to NI-RFSG locked the session.
        -  After a call to the :py:meth:`nirfsg.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`nirfsg.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`nirfsg.Session.lock` method and the
           :py:meth:`nirfsg.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nirfsg.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nirfsg.Session.lock` method with a call to
    the :py:meth:`nirfsg.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with nirfsg.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`nirfsg.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited

perform_power_search
--------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: perform_power_search()

            Performs a power search if the :py:attr:`nirfsg.Session.alc_control` property is disabled. Calling this method disables modulation for a short time while the device levels the output signal.

            

            .. note:: Power search temporarily enables the ALC, so ensure the appropriate included cable is connected between the PXIe-5654 ALCIN connector and the PXIe-5696 ALCOUT connector to successfully perform a power search.



perform_thermal_correction
--------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: perform_thermal_correction()

            Corrects for any signal drift due to environmental temperature variation when generating the same signal for extended periods of time without a parameter change. Under normal circumstances of short-term signal generation, NI-RFSG performs thermal correction automatically by ensuring stable power levels, and you do not need to call this method.

            



query_arb_waveform_capabilities
-------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: query_arb_waveform_capabilities()

            Queries and returns the waveform capabilities of the NI-RFSG device. These capabilities are related to the current device configuration. The NI-RFSG device must be in the Configuration or the Generation state before calling this method.

            



            :rtype: tuple (max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size)

                WHERE

                max_number_waveforms (int): 


                    Returns the value of the :py:attr:`nirfsg.Session.arb_max_number_waveforms` property. This value is the maximum number of waveforms you can write.

                    


                waveform_quantum (int): 


                    Returns the value of the :py:attr:`nirfsg.Session.arb_waveform_quantum` property. If the waveform quantum is *q*, then the size of the waveform that you write should be a multiple of *q*. The units are expressed in samples.

                    


                min_waveform_size (int): 


                    Returns the value of the :py:attr:`nirfsg.Session.arb_waveform_size_min` property. The number of samples of the waveform that you write must be greater than or equal to this value.

                    


                max_waveform_size (int): 


                    Returns the value of the :py:attr:`nirfsg.Session.arb_waveform_size_max` property. The number of samples of the waveform that you write must be less than or equal to this value.

                    



read_and_download_waveform_from_file_tdms
-----------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: read_and_download_waveform_from_file_tdms(waveform_name, file_path, waveform_index)

            Reads the waveforms from a TDMS file and downloads one waveform into each of the NI RF vector signal generators.

            



            :param waveform_name:


                Specifies the name used to store the waveform. This string is case-insensitive.

                


            :type waveform_name: str
            :param file_path:


                Specifies the absolute path to the TDMS file from which the NI-RFSG reads the waveforms.

                


            :type file_path: str
            :param waveform_index:


                Specifies the index of the waveform to be read from the TDMS file.

                


            :type waveform_index: int

reset
-----

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: reset()

            Resets all properties to their default values and moves the NI-RFSG device to the Configuration state. This method aborts the generation, deletes all de-embedding tables, clears all routes, and resets session properties to their initial values. During a reset, routes of signals between this and other devices are released, regardless of which device created the route.

            

            .. note:: This method resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG.



reset_attribute
---------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: reset_attribute(attribute_id)

            Resets the property to its default value.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].reset_attribute`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

                Example: :py:meth:`my_session.reset_attribute`


            :param attribute_id:


                Pass the ID of a property.

                


            :type attribute_id: int

reset_device
------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: reset_device()

            Performs a hard reset on the device.

            

            .. note:: You must call the :py:meth:`nirfsg.Session.reset_device` method if the NI-RFSG device has shut down because of a high-temperature condition.



reset_with_defaults
-------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: reset_with_defaults()

            Performs a software reset of the device, returning it to the default state and applying any initial default settings from the IVI Configuration Store.

            



save_configurations_to_file
---------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: save_configurations_to_file(file_path)

            Saves the configurations of the session to the specified file.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].save_configurations_to_file`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

                Example: :py:meth:`my_session.save_configurations_to_file`


            :param file_path:


                Specifies the absolute path of the file to which the NI-RFSG saves the configurations.

                


            :type file_path: str

select_arb_waveform
-------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: select_arb_waveform(name)

            Specifies the waveform that is generated upon a call to the :py:meth:`nirfsg.Session._initiate` method when the **generationMode** parameter of the :py:meth:`nirfsg.Session.configure_generation_mode` method is set to :py:data:`~nirfsg.GenerationMode.ARB_WAVEFORM`. You must specify a waveform using the :py:attr:`nirfsg.Session.NAME` parameter if you have written multiple waveforms. The NI-RFSG device must be in the Configuration state before you call this method.

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :param name:


                Specifies the name of the stored waveform to generate. This is a case-insensitive alphanumeric string that does not use reserved words. NI-RFSG sets the :py:attr:`nirfsg.Session.arb_selected_waveform` property to this value.

                


            :type name: str

self_cal
--------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: self_cal()

            Performs an internal self-calibration on the device and associated modules that support self-calibration. If the calibration is successful, new calibration data and constants are stored in the onboard nonvolatile memory of the module.

            

            .. note:: If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this method runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate.



self_calibrate_range
--------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: self_calibrate_range(steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level)

            Self-calibrates all configurations within the specified frequency and peak power level limits.

            

            .. note:: If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842 while this method runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate.



            :param steps_to_omit:


                Specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that no calibration steps are omitted.

                


            :type steps_to_omit: int
            :param min_frequency:


                Specifies the minimum frequency to calibrate.

                


            :type min_frequency: float
            :param max_frequency:


                Specifies the maximum frequency to calibrate.

                


            :type max_frequency: float
            :param min_power_level:


                Specifies the minimum power level to calibrate.

                


            :type min_power_level: float
            :param max_power_level:


                Specifies the maximum power level to calibrate.

                


            :type max_power_level: float

self_test
---------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: self_test()

            TBD

            



send_software_edge_trigger
--------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: send_software_edge_trigger(trigger, trigger_identifier)

            Forces a trigger to occur. The specified trigger generates regardless of whether the trigger has been configured as a software trigger.

            



            :param trigger:


                Specifies the trigger to send.

                


            :type trigger: int
            :param trigger_identifier:


                Specifies the Script Trigger to configure. This parameter is valid only when you set the :py:attr:`nirfsg.Session.TRIGGER` parameter to :py:data:`~nirfsg.NIRFSG_VAL_START_TRIGGER`. Otherwise, set the :py:attr:`nirfsg.Session.TRIGGER_IDENTIFIER` parameter to '' (empty string).

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger_identifier: str

set_arb_waveform_next_write_position
------------------------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: set_arb_waveform_next_write_position(waveform_name, relative_to, offset)

            Configures the start position to use for writing a waveform before calling the :py:meth:`nirfsg.Session.WriteArbWaveform` method. This method allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the **name** input of the :py:meth:`nirfsg.Session.allocate_arb_waveform` method or the :py:meth:`nirfsg.Session.WriteArbWaveform` method. Subsequent writes to that waveform begin where the last write ended, unless this method is called again.

            

            .. note:: If you use this method to write the waveform that is currently generating, an undefined output may result.

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :param waveform_name:


                Specifies the name of the waveform. This string is case-insensitive and alphanumeric, and it cannot use `reserved words <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_

                


            :type waveform_name: str
            :param relative_to:


                Specifies the reference position in the waveform. The position and :py:attr:`nirfsg.Session.OFFSET` together determine where to start loading data into the waveform.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type relative_to: int
            :param offset:


                Specifies the offset from the **relative to** parameter at which to start loading the data into the waveform.

                


            :type offset: int

unlock
------

    .. py:currentmodule:: nirfsg.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`nirfsg.Session.lock`. Refer to :py:meth:`nirfsg.Session.unlock` for additional
    information on session locks.

wait_until_settled
------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: wait_until_settled(max_time_milliseconds)

            Waits until the RF output signal has settled. This method is useful for devices that support changes while in the Generation state. Call this method after making a dynamic change to wait for the output signal to settle.

            



            :param max_time_milliseconds:


                Specifies the maximum time the method waits for the output to settle. If the maximum time is exceeded, this method returns an error. The units are expressed in milliseconds.

                


            :type max_time_milliseconds: int

write_p2_p_endpoint_i16
-----------------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: write_p2_p_endpoint_i16(stream_endpoint, number_of_samples, endpoint_data)

            Writes an array of 16-bit integer data to the peer-to-peer endpoint. Use this method to write initial data from the host to the endpoint before starting generation to avoid an underflow when you start the generation.

            



            :param stream_endpoint:


                Specifies the stream endpoint FIFO to configure.

                


            :type stream_endpoint: str
            :param number_of_samples:


                Specifies the number of samples to write into the endpoint FIFO.

                


            :type number_of_samples: int
            :param endpoint_data:


                Specifies the array of data to write into the endpoint FIFO. The binary data is left-justified.

                


            :type endpoint_data: list of int

write_script
------------

    .. py:currentmodule:: nirfsg.Session

    .. py:method:: write_script(script)

            Writes a script to the device to control waveform generation in Script mode. First, configure your device for Script mode by calling the :py:meth:`nirfsg.Session.configure_generation_mode` method. The NI-RFSG device must be in the Configuration state before calling the :py:meth:`nirfsg.Session.write_script` method.

            

            .. note:: If you are using an RF vector signal transceiver (VST) device, some script instructions may not be supported.



            :param script:


                Specifies a string containing a syntactically correct script. NI-RFSG supports multiple scripts that are selected with the :py:attr:`nirfsg.Session.selected_script` property. Refer to `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_ for more information about using scripts.

                


            :type script: str


Properties
==========

absolute_delay
--------------

    .. py:attribute:: absolute_delay

        Specifies the sub-Sample Clock delay, in seconds, to apply to the I/Q waveform. Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Units:** Seconds

                        **Valid Values:** Plus or minus half of one Sample Clock period

                        **Supported Devices:** PXIe-5820/5840/5841/5842



        .. note:: - The resolution of this property is a method of the I/Q sample period at 15E(-6) times that sample period.

             - If this property is set, NI-TClk cannot perform any sub-Sample Clock adjustment.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:Absolute Delay**
                - C Attribute: **NIRFSG_ATTR_ABSOLUTE_DELAY**

ae_temperature
--------------

    .. py:attribute:: ae_temperature

        Returns the amplitude extender module temperature in degrees Celsius.

                        **Units**: degrees Celsius (°C)

                        **Supported Devices:** PXIe-5654 with PXIe-5696

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:AE Temperature (Degrees C)**
                - C Attribute: **NIRFSG_ATTR_AE_TEMPERATURE**

alc_control
-----------

    .. py:attribute:: alc_control

        Enables or disables the automatic leveling control (ALC).

                        PXIe-5654 with PXIe-5696: If this property is enabled, the ALC is closed (closed-loop mode) and allows for better amplitude accuracy and wider amplitude dynamic range. If this property is disabled, the ALC is open (open-loop mode), which is ideal when using modulation. Disabling the :py:attr:`nirfsg.Session.alc_control` property also allows for NI-RFSG to perform an automatic power search.

                        PXIe-5654: :py:data:`~nirfsg.AutomaticLevelControl.DISABLE` is the only supported value for this device. The PXIe-5654 does not support the ALC when used as a stand-alone device.

                        **Default Value:**

                        PXIe-5654: :py:data:`~nirfsg.AutomaticLevelControl.DISABLE`

                        PXIe-5654 with PXIe-5696: :py:data:`~nirfsg.AutomaticLevelControl.ENABLE`

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696

                        **Related Topics**

                        `Power Level Adjustment <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_level_adjustment.html>`_

                        `ALC Closed Loop Versus Open Loop <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_alc_closed_loop_vs_open_loop.html>`_

                        `Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_

                    **Defined Values**:

        +--------------------------------------------------+---------+------------------+
        | Name                                             | Value   | Description      |
        +==================================================+=========+==================+
        | :py:data:`~nirfsg.AutomaticLevelControl.DISABLE` | 0 (0x0) | Disables ALC.    |
        +--------------------------------------------------+---------+------------------+
        | :py:data:`~nirfsg.AutomaticLevelControl.ENABLE`  | 1 (0x1) | Enables the ALC. |
        +--------------------------------------------------+---------+------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.AutomaticLevelControl |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:ALC Control**
                - C Attribute: **NIRFSG_ATTR_ALC_CONTROL**

allow_out_of_specification_user_settings
----------------------------------------

    .. py:attribute:: allow_out_of_specification_user_settings

        Enables or disables warnings or errors when you set the frequency, power, and bandwidth values beyond the limits of the NI-RFSG device specifications. When you enable the :py:attr:`nirfsg.Session.allow_out_of_specification_user_settings` property, the driver does not report out-of-specification warnings or errors.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.AllowOutOfSpecificationUserSettings.DISABLE`

                        **Supported Devices:** PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +----------------------------------------------------------------+---------+----------------------------------------------+
        | Name                                                           | Value   | Description                                  |
        +================================================================+=========+==============================================+
        | :py:data:`~nirfsg.AllowOutOfSpecificationUserSettings.DISABLE` | 0 (0x0) | Disables out-of-specification user settings. |
        +----------------------------------------------------------------+---------+----------------------------------------------+
        | :py:data:`~nirfsg.AllowOutOfSpecificationUserSettings.ENABLE`  | 1 (0x1) | Enables out-of-specification user settings.  |
        +----------------------------------------------------------------+---------+----------------------------------------------+

        .. note:: Accuracy cannot be guaranteed outside of device specifications, and results may vary by module.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------+
            | Characteristic        | Value                                     |
            +=======================+===========================================+
            | Datatype              | enums.AllowOutOfSpecificationUserSettings |
            +-----------------------+-------------------------------------------+
            | Permissions           | read-write                                |
            +-----------------------+-------------------------------------------+
            | Repeated Capabilities | None                                      |
            +-----------------------+-------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Allow Out Of Specification User Settings**
                - C Attribute: **NIRFSG_ATTR_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS**

amplitude_settling
------------------

    .. py:attribute:: amplitude_settling

        Configures the amplitude settling accuracy in decibels. NI-RFSG waits until the RF power settles within the specified accuracy level after calling the :py:meth:`nirfsg.Session._initiate` method or :py:meth:`nirfsg.Session.wait_until_settled` method or prior to advancing to next step if using RF list mode.

                        Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.

                        PXI/PXIe-5650/5651/5652: This property is for NI internal use only.

                        **Units**: dB

                        **Default Value:**

                        PXIe-5654: 4

                        PXIe-5654 with PXIe-5696 (ALC disabled): 4

                        PXIe-5654 with PXIe-5696 (ALC enabled): 0.2

                        PXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.5

                        **Valid Values:**

                        PXIe-5654: 1.5, 2, 4

                        PXIe-5654 with PXIe-5696 (ALC disabled): 1.5, 2, 4

                        PXIe-5654 with PXIe-5696 (ALC enabled): 0.2, 0.5

                        PXIe-5820/5830/5831/5832/5840/5841/5842/5860: 0.01 to 1

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Amplitude Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_amplitude_settling_times.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Amplitude Settling**
                - C Attribute: **NIRFSG_ATTR_AMPLITUDE_SETTLING**

amp_path
--------

    .. py:attribute:: amp_path

        Specifies the amplification path to use. The low harmonic path provides greater second and third harmonic spurious response, and the high power path provides higher output power.

                        NI-RFSG automatically sets the value of this property based on power and frequency settings. Setting this property overrides the value chosen by NI-RFSG.

                        **Default Value:** :py:data:`~nirfsg.AmpPath.LOW_HARMONIC`

                        **Supported Devices:** PXIe-5654 with PXIe-5696

                        **Related Topics**

                        `Low Harmonic Path Versus High Power Path <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/low_harmonic_path_vs_high_power_path.html>`_

                    **Defined Values**:

        +-----------------------------------------+----------------+-----------------------------------------------------------+
        | Name                                    | Value          | Description                                               |
        +=========================================+================+===========================================================+
        | :py:data:`~nirfsg.AmpPath.HIGH_POWER`   | 16000 (0x3e80) | Sets the amplification path to use the high power path.   |
        +-----------------------------------------+----------------+-----------------------------------------------------------+
        | :py:data:`~nirfsg.AmpPath.LOW_HARMONIC` | 16001 (0x3e81) | Sets the amplification path to use the low harmonic path. |
        +-----------------------------------------+----------------+-----------------------------------------------------------+

        .. note:: Resetting this property reverts back to the default unset behavior.

        The following table lists the characteristics of this property.

            +-----------------------+---------------+
            | Characteristic        | Value         |
            +=======================+===============+
            | Datatype              | enums.AmpPath |
            +-----------------------+---------------+
            | Permissions           | read-write    |
            +-----------------------+---------------+
            | Repeated Capabilities | None          |
            +-----------------------+---------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Advanced:Amp Path**
                - C Attribute: **NIRFSG_ATTR_AMP_PATH**

analog_modulation_am_sensitivity
--------------------------------

    .. py:attribute:: analog_modulation_am_sensitivity

        Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.

                        When using the PXIe-5654 with PXIe-5696, NI-RFSG may coerce AM sensitivity. Coercing the AM sensitivity prevents overpower conditions at the PXIe-5696 input. Read this property to determine the coerced value.

                        **Default Value:** 100

                        **Valid Values:** 0 to 100

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696

                        **Related Topics**

                        `Amplitude Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_amplitude_modulation.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Analog:AM Sensitivity**
                - C Attribute: **NIRFSG_ATTR_ANALOG_MODULATION_AM_SENSITIVITY**

analog_modulation_fm_band
-------------------------

    .. py:attribute:: analog_modulation_fm_band

        Specifies the analog modulation frequency modulation (FM) band to use. Wideband FM allows for modulating signals higher than 100kHz. Narrowband FM allows for modulating lower frequency signals.

                        **Default Value:** :py:data:`~nirfsg.AnlgModFmBand.WIDEBAND`

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696

                        **Related Topics**

                        `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_

                    **Defined Values**:

        +---------------------------------------------+----------------+--------------------------------------------+
        | Name                                        | Value          | Description                                |
        +=============================================+================+============================================+
        | :py:data:`~nirfsg.AnlgModFmBand.NARROWBAND` | 17000 (0x4268) | Specifies narrowband frequency modulation. |
        +---------------------------------------------+----------------+--------------------------------------------+
        | :py:data:`~nirfsg.AnlgModFmBand.WIDEBAND`   | 17001 (0x4269) | Specifies wideband frequency modulation.   |
        +---------------------------------------------+----------------+--------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.AnlgModFmBand |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | None                |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Analog:FM Band**
                - C Attribute: **NIRFSG_ATTR_ANALOG_MODULATION_FM_BAND**

analog_modulation_fm_deviation
------------------------------

    .. py:attribute:: analog_modulation_fm_deviation

        Specifies the frequency deviation to use in frequency modulation.

                        **Units**: hertz (Hz)

                        **Default Value:** 1kHz

                        **Supported Devices:** PXI/PXIe-5650/5651/5652

                        **Related Topics**

                        `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Analog:FM Deviation (Hz)**
                - C Attribute: **NIRFSG_ATTR_ANALOG_MODULATION_FM_DEVIATION**

analog_modulation_fm_narrowband_integrator
------------------------------------------

    .. py:attribute:: analog_modulation_fm_narrowband_integrator

        Specifies the narrowband frequency modulation (FM) range to apply by sending the signal through an integrator.

                        This property is valid only when you set the :py:attr:`nirfsg.Session.analog_modulation_type` property to :py:data:`~nirfsg.AnlgModType.FM` and the :py:attr:`nirfsg.Session.analog_modulation_fm_band` property to :py:data:`~nirfsg.AnlgModFmBand.NARROWBAND`.

                        **Default Value:** :py:data:`~nirfsg.AnlgModFmNarrowbandIntegrator._100hzto1khz`

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696

                        **Related Topics**

                        `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_

                        **Defined Values**:

        +-----------------------------------------------------------------+----------------+---------------------------------------------+
        | Name                                                            | Value          | Description                                 |
        +=================================================================+================+=============================================+
        | :py:data:`~nirfsg.AnlgModFmNarrowbandIntegrator._100hzto1khz`   | 18000 (0x4650) | Specifies a range from 100Â Hz to 1Â kHz.   |
        +-----------------------------------------------------------------+----------------+---------------------------------------------+
        | :py:data:`~nirfsg.AnlgModFmNarrowbandIntegrator._10khzto100khz` | 18002 (0x4652) | Specifies a range from 10Â kHz to 100Â kHz. |
        +-----------------------------------------------------------------+----------------+---------------------------------------------+
        | :py:data:`~nirfsg.AnlgModFmNarrowbandIntegrator._1khzto10khz`   | 18001 (0x4651) | Specifies a range from 1Â kHz to 10Â kHz.   |
        +-----------------------------------------------------------------+----------------+---------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------+
            | Characteristic        | Value                               |
            +=======================+=====================================+
            | Datatype              | enums.AnlgModFmNarrowbandIntegrator |
            +-----------------------+-------------------------------------+
            | Permissions           | read-write                          |
            +-----------------------+-------------------------------------+
            | Repeated Capabilities | None                                |
            +-----------------------+-------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Analog:FM Narrowband Integrator**
                - C Attribute: **NIRFSG_ATTR_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR**

analog_modulation_fm_sensitivity
--------------------------------

    .. py:attribute:: analog_modulation_fm_sensitivity

        Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.

                        **Default Value:** 100

                        **Valid Values:** 0 to 100

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696

                        **Related Topics**

                        `Frequency Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_frequency_modulation.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Analog:FM Sensitivity**
                - C Attribute: **NIRFSG_ATTR_ANALOG_MODULATION_FM_SENSITIVITY**

analog_modulation_pm_deviation
------------------------------

    .. py:attribute:: analog_modulation_pm_deviation

        Specifies the `deviation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/glossary.html>`_ to use in phase modulation, in degrees.

                        **Units**: degrees (°)

                        **Default Value:** 90°

                        **Supported Devices:** PXI/PXIe-5650/5651/5652, PXIe-5653

                        **Related Topics**

                        `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Analog:PM Deviation (Degrees)**
                - C Attribute: **NIRFSG_ATTR_ANALOG_MODULATION_PM_DEVIATION**

analog_modulation_pm_mode
-------------------------

    .. py:attribute:: analog_modulation_pm_mode

        Specifies the phase modulation (PM) mode to use.

                        **Default Value:** :py:data:`~nirfsg.AnlgModPmMode.LOW_PHASE_NOISE`

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696

                        **Related Topics**

                        `Phase Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_phase_modulation.html>`_

                    **Defined Values**:

        +--------------------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
        | Name                                             | Value          | Description                                                                                   |
        +==================================================+================+===============================================================================================+
        | :py:data:`~nirfsg.AnlgModPmMode.HIGH_DEVIATION`  | 19000 (0x4a38) | Specifies high deviation. High deviation comes at the expense of a higher phase noise.        |
        +--------------------------------------------------+----------------+-----------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.AnlgModPmMode.LOW_PHASE_NOISE` | 19001 (0x4a39) | Specifies low phase noise. Low phase noise comes at the expense of a lower maximum deviation. |
        +--------------------------------------------------+----------------+-----------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.AnlgModPmMode |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | None                |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Analog:PM Mode**
                - C Attribute: **NIRFSG_ATTR_ANALOG_MODULATION_PM_MODE**

analog_modulation_pm_sensitivity
--------------------------------

    .. py:attribute:: analog_modulation_pm_sensitivity

        Specifies an uncalibrated digital-to-analog converter (DAC) value that scales the input signal before the signal modulates the carrier. A value of 0 completely attenuates the signal, and a value of 100 passes the full-scale signal to the modulator.

                        **Default Value:** 100

                        **Valid Values:** 0 to 100

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696

                        **Related Topics**

                        `Phase Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_phase_modulation.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Analog:PM Sensitivity**
                - C Attribute: **NIRFSG_ATTR_ANALOG_MODULATION_PM_SENSITIVITY**

analog_modulation_type
----------------------

    .. py:attribute:: analog_modulation_type

        Specifies the analog modulation format to use.

                        **Default Value:** :py:data:`~nirfsg.AnlgModType.NONE`

                        **Supported Devices:** PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696

                        **Related Topics**

                        `Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation.html>`_

                        `PXI/PXIe-5650/5651/5652 Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

                        `PXIe-5654/5654 with PXIe-5696 Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_5696_modulation_modes.html>`_

                    **Defined Values**:

        +-------------------------------------+--------------+--------------------------------------------------+
        | Name                                | Value        | Description                                      |
        +=====================================+==============+==================================================+
        | :py:data:`~nirfsg.AnlgModType.AM`   | 2002 (0x7d2) | Specifies that the analog modulation type is AM. |
        +-------------------------------------+--------------+--------------------------------------------------+
        | :py:data:`~nirfsg.AnlgModType.FM`   | 2000 (0x7d0) | Specifies that the analog modulation type is FM. |
        +-------------------------------------+--------------+--------------------------------------------------+
        | :py:data:`~nirfsg.AnlgModType.NONE` | 0 (0x0)      | Disables analog modulation.                      |
        +-------------------------------------+--------------+--------------------------------------------------+
        | :py:data:`~nirfsg.AnlgModType.PM`   | 2001 (0x7d1) | Specifies that the analog modulation type is PM. |
        +-------------------------------------+--------------+--------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.AnlgModType |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Analog:Modulation Type**
                - C Attribute: **NIRFSG_ATTR_ANALOG_MODULATION_TYPE**

analog_modulation_waveform_frequency
------------------------------------

    .. py:attribute:: analog_modulation_waveform_frequency

        Specifies the frequency of the waveform to use as the message signal in analog modulation.

                        **Units:** hertz (Hz)

                        **Default Value:** 1kHz

                        **Supported Devices:** PXI/PXIe-5650/5651/5652

                        **Related Topics**

                        `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Analog:Waveform Frequency (Hz)**
                - C Attribute: **NIRFSG_ATTR_ANALOG_MODULATION_WAVEFORM_FREQUENCY**

analog_modulation_waveform_type
-------------------------------

    .. py:attribute:: analog_modulation_waveform_type

        Specifies the type of waveform to use as the message signal for analog modulation.

                        **Default Value:** :py:data:`~nirfsg.AnlgModWfmType.SINE`

                        **Supported Devices:** PXI/PXIe-5650/5651/5652

                        **Related Topics**

                        `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

                    **Defined Values**:

        +--------------------------------------------+--------------+-----------------------------------------------------------------+
        | Name                                       | Value        | Description                                                     |
        +============================================+==============+=================================================================+
        | :py:data:`~nirfsg.AnlgModWfmType.SINE`     | 3000 (0xbb8) | Specifies that the analog modulation waveform type is sine.     |
        +--------------------------------------------+--------------+-----------------------------------------------------------------+
        | :py:data:`~nirfsg.AnlgModWfmType.SQUARE`   | 3001 (0xbb9) | Specifies that the analog modulation waveform type is square.   |
        +--------------------------------------------+--------------+-----------------------------------------------------------------+
        | :py:data:`~nirfsg.AnlgModWfmType.TRIANGLE` | 3002 (0xbba) | Specifies that the analog modulation waveform type is triangle. |
        +--------------------------------------------+--------------+-----------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.AnlgModWfmType |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Analog:Waveform Type**
                - C Attribute: **NIRFSG_ATTR_ANALOG_MODULATION_WAVEFORM_TYPE**

arb_carrier_frequency
---------------------

    .. py:attribute:: arb_carrier_frequency

        **Units**: hertz (Hz)

                        **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate a carrier frequency with a waveform.
                        Indicates the carrier frequency generated by the arbitrary waveform generator (AWG) module. The specified carrier frequency is related to the RF output as shown in the following equations:

        +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Device                                                                        | Equations                                                                                                                                                                                                                                                                                                                                                         |
        +===============================================================================+===================================================================================================================================================================================================================================================================================================================================================================+
        | PXI-5610, PXI-5670/5671, PXIe-5672                                            | RF Frequency (MHz) = *Upconverter Center Frequency* + *Arb Carrier Frequency* – 25 MHz                                                                                                                                                                                                                                                                            |
        +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860 | RF Frequency (MHz) = *Upconverter Center Frequency* + *Arb Carrier Frequency*.Note that - the :py:attr:`nirfsg.Session.upconverter_center_frequency` property and the :py:attr:`nirfsg.Session.arb_carrier_frequency` property cannot be set at the same time. The only time the carrier frequency is nonzero on these devices is when in-band retuning is used.  |
        +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: - Use this property to associate a carrier frequency with a waveform.

             - This property is read-only on the PXI-5670/5671 and PXIe-5672.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Arb Carrier Frequency (Hz)**
                - C Attribute: **NIRFSG_ATTR_ARB_CARRIER_FREQUENCY**

arb_digital_gain
----------------

    .. py:attribute:: arb_digital_gain

        Specifies the digital gain, in decibels. The digital gain is applied to the waveform data after filtering. Use this property to adjust the output power of the device while keeping the analog path fixed. This may cause clipping, overflows, or quantization noise if used improperly.

                        To set this property, the NI-RFSG device must be in the Configuration or Generation state.

                        **Default Value:** 0 dB

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIRFSG_ATTR_ARB_DIGITAL_GAIN**

arb_filter_raised_cosine_alpha
------------------------------

    .. py:attribute:: arb_filter_raised_cosine_alpha

        Specifies the alpha value to use when calculating the pulse-shaping filter coefficients. You can use this property only when the :py:attr:`nirfsg.Session.arb_filter_type` property is set to :py:data:`~nirfsg.FilterType.ARB_FILTER_TYPE_RAISED_COSINE` and with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this property with a device that does not support OSP.

                        **Supported Devices:** PXI-5671, PXIe-5672/5673/5673E

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Pulse Shaping:Raised Cosine Alpha**
                - C Attribute: **NIRFSG_ATTR_ARB_FILTER_RAISED_COSINE_ALPHA**

arb_filter_root_raised_cosine_alpha
-----------------------------------

    .. py:attribute:: arb_filter_root_raised_cosine_alpha

        Specifies the alpha value to use when calculating the pulse-shaping FIR filter coefficients. You can use this property only when the :py:attr:`nirfsg.Session.arb_filter_type` property is set to :py:data:`~nirfsg.FilterType.ARB_FILTER_TYPE_ROOT_RAISED_COSINE` and with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this property with a device that does not support OSP.

                        **Supported Devices:** PXI-5671, PXIe-5672/5673/5673E

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Pulse Shaping:Root Raised Cosine Alpha**
                - C Attribute: **NIRFSG_ATTR_ARB_FILTER_ROOT_RAISED_COSINE_ALPHA**

arb_filter_type
---------------

    .. py:attribute:: arb_filter_type

        Specifies the pulse-shaping filter type for the FIR filter. You can use this property only with signal generators that support onboard signal processing (OSP). NI-RFSG returns an error if you use this property with a device that does not support OSP.

                        **Default Value:** :py:data:`~nirfsg.FilterType.NONE`

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

                    **Defined Values**:

        +------------------------------------------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                             | Value          | Description                                                                                                                                                     |
        +==================================================================+================+=================================================================================================================================================================+
        | :py:data:`~nirfsg.FilterType.NONE`                               | 0 (0x0)        | Disables analog modulation.                                                                                                                                     |
        +------------------------------------------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.FilterType.ARB_FILTER_TYPE_RAISED_COSINE`      | 10002 (0x2712) | Applies a raised cosine filter to the data with the alpha value specified with the :py:attr:`nirfsg.Session.arb_filter_raised_cosine_alpha` property.           |
        +------------------------------------------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.FilterType.ARB_FILTER_TYPE_ROOT_RAISED_COSINE` | 10001 (0x2711) | Applies a root-raised cosine filter to the data with the alpha value specified with the :py:attr:`nirfsg.Session.arb_filter_root_raised_cosine_alpha` property. |
        +------------------------------------------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------+
            | Characteristic        | Value            |
            +=======================+==================+
            | Datatype              | enums.FilterType |
            +-----------------------+------------------+
            | Permissions           | read-write       |
            +-----------------------+------------------+
            | Repeated Capabilities | None             |
            +-----------------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Pulse Shaping:Filter Type**
                - C Attribute: **NIRFSG_ATTR_ARB_FILTER_TYPE**

arb_max_number_waveforms
------------------------

    .. py:attribute:: arb_max_number_waveforms

        Returns the maximum number of waveforms the device can hold in memory.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.query_arb_waveform_capabilities`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Capabilities:Max Number Waveforms**
                - C Attribute: **NIRFSG_ATTR_ARB_MAX_NUMBER_WAVEFORMS**

arb_onboard_sample_clock_mode
-----------------------------

    .. py:attribute:: arb_onboard_sample_clock_mode

        Specifies the Sample Clock mode on the device. To set this property, the device must be in the Configuration state.

                        PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: :py:data:`~nirfsg.ArbOnboardSampleClockMode.DIVIDE_DOWN` is the only supported value for this device.

                        **Default Values:**

                        PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: :py:data:`~nirfsg.ArbOnboardSampleClockMode.DIVIDE_DOWN`

                        PXIe-5673/5673E: :py:data:`~nirfsg.ArbOnboardSampleClockMode.HIGH_RESOLUTION`

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Clocking Modes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/clocking.html>`_

                    **Valid Values**:

        +--------------------------------------------------------------+--------------------------------------------------------------+
        | Name                                                         | Description                                                  |
        +==============================================================+==============================================================+
        | :py:data:`~nirfsg.ArbOnboardSampleClockMode.HIGH_RESOLUTION` | Sample rates are generated by a high-resolution clock.       |
        +--------------------------------------------------------------+--------------------------------------------------------------+
        | :py:data:`~nirfsg.ArbOnboardSampleClockMode.DIVIDE_DOWN`     | Sample rates are generated by dividing the source frequency. |
        +--------------------------------------------------------------+--------------------------------------------------------------+

        .. note:: Using the high resolution clock may result in increased phase noise.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.ArbOnboardSampleClockMode |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clock:Arb Onboard Sample Clock Mode**
                - C Attribute: **NIRFSG_ATTR_ARB_ONBOARD_SAMPLE_CLOCK_MODE**

arb_oscillator_phase_dac_value
------------------------------

    .. py:attribute:: arb_oscillator_phase_dac_value

        Specifies the oscillator phase digital-to-analog converter (DAC) value on the arbitrary waveform generator (AWG). Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk. This property can also help maintain synchronization repeatability by writing a previous measurement's phase DAC value to the current session. This property is applicable only when using the :py:attr:`nirfsg.Session.arb_sample_clock_source` property set to :py:data:`~nirfsg.NIRFSG_VAL_CLK_IN_STR`.

                        **Supported Devices:** PXIe-5673/5673E

                        **Related Topics**

                        `NI-TClk Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_tclk_help.html>`_



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clock:Advanced:Arb Oscillator Phase DAC Value**
                - C Attribute: **NIRFSG_ATTR_ARB_OSCILLATOR_PHASE_DAC_VALUE**

arb_power
---------

    .. py:attribute:: arb_power

        Indicates the average output power from the PXI-5421, PXI-5441, PXIe-5442, and PXIe-5450 AWG module. If an arbitrary waveform is being generated, this property specifies either the average power or the peak power of the signal, depending on the :py:attr:`nirfsg.Session.power_level_type` property setting.

                        **Units**: dBm

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Arb Power (dBm)**
                - C Attribute: **NIRFSG_ATTR_ARB_POWER**

arb_pre_filter_gain
-------------------

    .. py:attribute:: arb_pre_filter_gain

        Specifies the AWG prefilter gain. The prefilter gain is applied to the waveform data before any other signal processing. Reduce this value to prevent overflow in the AWG interpolation filters. Other gains on the NI-RFSG device are automatically adjusted to compensate for nonunity AWG prefilter gain. The PXI-5671, PXIe-5672 must be in the Configuration state to use this property. However, the PXIe-5644/5645/5646, PXIe-5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842 can be in either the Configuration or the Generation state to use this property. PXIe-5860 can only be in the Configuration state to use this property.

                        On the PXI-5671, this property applies only when the :py:attr:`nirfsg.Session.iq_rate` property is set to a value less than or equal to 8.33MS/s. On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, this property is always applicable.

                        **Units**: dB

                        **Default Value:** 0dB

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Pre-filter Gain (dB)**
                - C Attribute: **NIRFSG_ATTR_ARB_PRE_FILTER_GAIN**

arb_sample_clock_rate
---------------------

    .. py:attribute:: arb_sample_clock_rate

        Returns the rate of the Sample Clock on the device.

                        **Units**: hertz (Hz)

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clock:Arb Sample Clock Rate (Hz)**
                - C Attribute: **NIRFSG_ATTR_ARB_SAMPLE_CLOCK_RATE**

arb_sample_clock_source
-----------------------

    .. py:attribute:: arb_sample_clock_source

        Specifies the Sample Clock source for the device. To set this property, the NI-RFSG device must be in the Configuration state.

                        PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: :py:data:`~nirfsg.ArbSampleClockSource.ONBOARD_CLOCK` is the only supported value for this device.

                        **Default Value:** :py:data:`~nirfsg.ArbSampleClockSource.ONBOARD_CLOCK`

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

                    **Defined Values**:

        +-------------------------------------------------------+--------------+---------------------------------------------------------------+
        | Name                                                  | Value        | Description                                                   |
        +=======================================================+==============+===============================================================+
        | :py:data:`~nirfsg.ArbSampleClockSource.CLK_IN`        | ClkIn        | Uses the external clock as the Sample Clock source.           |
        +-------------------------------------------------------+--------------+---------------------------------------------------------------+
        | :py:data:`~nirfsg.ArbSampleClockSource.ONBOARD_CLOCK` | OnboardClock | Uses the AWG module onboard clock as the Sample Clock source. |
        +-------------------------------------------------------+--------------+---------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ArbSampleClockSource |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clock:Arb Sample Clock Source**
                - C Attribute: **NIRFSG_ATTR_ARB_SAMPLE_CLOCK_SOURCE**

arb_selected_waveform
---------------------

    .. py:attribute:: arb_selected_waveform

        Specifies the waveform in onboard memory to generate upon calling the :py:meth:`nirfsg.Session.Init` method when the :py:attr:`nirfsg.Session.generation_mode` property is set to :py:data:`~nirfsg.GenerationMode.ARB_WAVEFORM`. The :py:attr:`nirfsg.Session.arb_selected_waveform` property is ignored when the :py:attr:`nirfsg.Session.generation_mode` property is set to :py:data:`~nirfsg.GenerationMode.SCRIPT` or :py:data:`~nirfsg.GenerationMode.CW`. To set the :py:attr:`nirfsg.Session.arb_selected_waveform` property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** "" (empty string)

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.select_arb_waveform`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Capabilities:Selected Waveform**
                - C Attribute: **NIRFSG_ATTR_ARB_SELECTED_WAVEFORM**

arb_temperature
---------------

    .. py:attribute:: arb_temperature

        Returns the AWG module temperature in degrees Celsius.

                        PXIe-5820/5840/5841/5842: If you query this property during RF list mode, list steps may take longer to complete during list execution.

                        **Units**: degrees Celsius (°C)

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:AWG Temperature (Degrees C)**
                - C Attribute: **NIRFSG_ATTR_ARB_TEMPERATURE**

arb_waveform_quantum
--------------------

    .. py:attribute:: arb_waveform_quantum

        Returns the waveform quantum for the device. The number of samples in a waveform must be an integer multiple of the waveform quantum. The other restrictions on the length of the waveform are the :py:attr:`nirfsg.Session.arb_waveform_size_min` and :py:attr:`nirfsg.Session.arb_waveform_size_max` arbitrary waveform sizes.

                        PXI-5671, PXIe-5672: The value of this property depends on the I/Q rate. Set the :py:attr:`nirfsg.Session.iq_rate` property before reading this property.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.query_arb_waveform_capabilities`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Capabilities:Waveform Quantum**
                - C Attribute: **NIRFSG_ATTR_ARB_WAVEFORM_QUANTUM**

arb_waveform_repeat_count
-------------------------

    .. py:attribute:: arb_waveform_repeat_count

        Specifies the repeat count of a waveform when you set the :py:attr:`nirfsg.Session.arb_waveform_repeat_count_is_finite` property to True. This property is valid only when you set the :py:attr:`nirfsg.Session.generation_mode` property to :py:data:`~nirfsg.GenerationMode.ARB_WAVEFORM`. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** 1

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Repeat Count**
                - C Attribute: **NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT**

arb_waveform_repeat_count_is_finite
-----------------------------------

    .. py:attribute:: arb_waveform_repeat_count_is_finite

        Specifies the repetition mode of a waveform when you set the :py:attr:`nirfsg.Session.generation_mode` property to :py:data:`~nirfsg.GenerationMode.ARB_WAVEFORM`. If you set this property to True, the number of repetitions is determined by the :py:attr:`nirfsg.Session.arb_waveform_repeat_count` property. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** False

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +-------+-------------------------------------------------------------------+
        | Value | Description                                                       |
        +=======+===================================================================+
        | True  | Repeats the waveform a finite number of times.                    |
        +-------+-------------------------------------------------------------------+
        | False | Repeats the waveform continuously until you abort the generation. |
        +-------+-------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Repeat Count Is Finite**
                - C Attribute: **NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE**

arb_waveform_size_max
---------------------

    .. py:attribute:: arb_waveform_size_max

        Returns the size of the largest waveform that is allowed.

                        To read this property, the NI-RFSG device must be in the Configuration state.

                        For the PXI-5671 and PXIe-5672, the value of this property depends on the I/Q rate. Set the :py:attr:`nirfsg.Session.iq_rate` before reading this property. For the PXIe-5673/5673E, the maximum waveform size is reduced to account for the amount of device memory currently used.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.query_arb_waveform_capabilities`



        .. note:: Not all onboard memory is available for waveform storage. A portion of onboard memory stores scripts that specify how the waveforms are generated. These scripts typically require less than 1KB of onboard memory.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Capabilities:Max Waveform Size**
                - C Attribute: **NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MAX**

arb_waveform_size_min
---------------------

    .. py:attribute:: arb_waveform_size_min

        Returns the smallest allowable waveform size. For the PXI-5671 and PXIe-5672, the value of this property depends on the I/Q rate. Set the :py:attr:`nirfsg.Session.iq_rate` property before reading this property.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.query_arb_waveform_capabilities`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Capabilities:Min Waveform Size**
                - C Attribute: **NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MIN**

arb_waveform_software_scaling_factor
------------------------------------

    .. py:attribute:: arb_waveform_software_scaling_factor

        Specifies how much to scale the data before writing it with the :py:meth:`nirfsg.Session.WriteArbWaveform` method. The resulting waveform must be smaller than 1.0 in complex magnitude. This property is supported only if you set the :py:attr:`nirfsg.Session.power_level_type` property to :py:data:`~nirfsg.PowerLevelType.PEAK`.

                        **Default Value:** 1.0

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Software Scaling Factor**
                - C Attribute: **NIRFSG_ATTR_ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR**

attenuator_hold_enabled
-----------------------

    .. py:attribute:: attenuator_hold_enabled

        Specifies whether attenuator hold is enabled. While this property is set to True, changing the power level causes NI-RFSG to scale the digital data sent to the AWG instead of adjusting the attenuators. Changing power levels in this manner allows the device to increase or decrease the power level in more accurate increments, but it may affect signal-to-noise ratios (noise density).


                        Setting the :py:attr:`nirfsg.Session.attenuator_hold_enabled` property to True limits the power levels that can be attained. With attenuator hold enabled, the power level must satisfy the following conditions:

                        - Power level less than or equal to :py:attr:`nirfsg.Session.attenuator_hold_max_power`
                        - Power level greater than or equal to (maximum power level -70dB)
                        - Power level greater than or equal to -145dBm

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** False

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

                        **Related Topics**

                        `Attenuator Hold <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/attenuator_hold_mode.html>`_

                        `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_

                    **Defined Values**:

        +-------+---------------------------+
        | Value | Description               |
        +=======+===========================+
        | True  | Enables attenuator hold.  |
        +-------+---------------------------+
        | False | Disables attenuator hold. |
        +-------+---------------------------+

        .. note:: The frequency cannot be changed on the PXI-5670/5671 or PXIe-5672 while this property is set to True.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Attenuator Hold Enabled**
                - C Attribute: **NIRFSG_ATTR_ATTENUATOR_HOLD_ENABLED**

attenuator_hold_max_power
-------------------------

    .. py:attribute:: attenuator_hold_max_power

        Specifies the maximum power level of the RF output signal when the :py:attr:`nirfsg.Session.attenuator_hold_enabled` property is set to True.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Units**: dBm

                        **Defined Values**:
                        Refer to the specifications document for your device for allowable maximum power levels.

                        **Default Value:**

                        PXI-5670/5671, PXIe-5672: 17

                        PXIe-5673/5673E: 10

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

                        **Related Topics**

                        `Attenuator Hold <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/attenuator_hold_mode.html>`_

                        `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Attenuator Hold Max Power (dBm)**
                - C Attribute: **NIRFSG_ATTR_ATTENUATOR_HOLD_MAX_POWER**

attenuator_setting
------------------

    .. py:attribute:: attenuator_setting

        Specifies the level of attenuation in the attenuator path. Setting this property overrides the value chosen by NI-RFSG. Not all power levels are achievable if you set this property.

                        **Units**: dB

                        **Valid Values**: 0dB to 110dB in steps of 10

                        **Supported Devices:** PXIe-5654 with PXIe-5696



        .. note:: Resetting this property reverts back to the default unset behavior.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Attenuator Setting (dB)**
                - C Attribute: **NIRFSG_ATTR_ATTENUATOR_SETTING**

automatic_thermal_correction
----------------------------

    .. py:attribute:: automatic_thermal_correction

        Enables or disables automatic thermal correction. When this property is enabled, changes to settings cause NI-RFSG to check whether the device temperature has changed and adjusts the settings as needed. When this property is disabled, you must explicitly call the :py:meth:`nirfsg.Session.perform_thermal_correction` method to adjust the device for temperature changes.

                        **Default Value:** :py:data:`~nirfsg.AutomaticThermalCorrection.ENABLE`

                        **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Temperature Monitoring <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5611_temperature_monitoring.html>`_

                        `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_

                    **Defined Values**:

        +-------------------------------------------------------+---------+-------------------------------------------+
        | Name                                                  | Value   | Description                               |
        +=======================================================+=========+===========================================+
        | :py:data:`~nirfsg.AutomaticThermalCorrection.DISABLE` | 0 (0x0) | Automatic thermal correction is disabled. |
        +-------------------------------------------------------+---------+-------------------------------------------+
        | :py:data:`~nirfsg.AutomaticThermalCorrection.ENABLE`  | 1 (0x1) | Automatic thermal correction is enabled.  |
        +-------------------------------------------------------+---------+-------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.AutomaticThermalCorrection |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | None                             |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Automatic Thermal Correction**
                - C Attribute: **NIRFSG_ATTR_AUTOMATIC_THERMAL_CORRECTION**

auto_power_search
-----------------

    .. py:attribute:: auto_power_search

        Enables or disables automatic power search. When this property is enabled, a power search performs after the device is initiated, after output power is enabled, or when the frequency or power level changes while the device is generating. When this property is disabled, NI-RFSG does not perform a power search unless you call the :py:meth:`nirfsg.Session.perform_power_search` method.

                        This property is ignored when the :py:attr:`nirfsg.Session.alc_control` property is enabled.

                        PXIe-5654: :py:data:`~nirfsg.AutomaticPowerSearch.DISABLE` is the only supported value for this device.

                        **Default Value:**

                        PXIe-5654: :py:data:`~nirfsg.AutomaticPowerSearch.DISABLE`

                        PXIe-5654 with PXIe-5696: :py:data:`~nirfsg.AutomaticPowerSearch.ENABLE`

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696

                        **Related Topics**

                        `Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_

                    **Defined Values**:

        +-------------------------------------------------+---------+----------------------------------+
        | Name                                            | Value   | Description                      |
        +=================================================+=========+==================================+
        | :py:data:`~nirfsg.AutomaticPowerSearch.DISABLE` | 0 (0x0) | Disables automatic power search. |
        +-------------------------------------------------+---------+----------------------------------+
        | :py:data:`~nirfsg.AutomaticPowerSearch.ENABLE`  | 1 (0x1) | Enables automatic power search.  |
        +-------------------------------------------------+---------+----------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.AutomaticPowerSearch |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Automatic Power Search**
                - C Attribute: **NIRFSG_ATTR_AUTO_POWER_SEARCH**

available_paths
---------------

    .. py:attribute:: available_paths

        Returns a comma separated list of the configurable paths available for use based on your instrument configuration.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Available Paths**
                - C Attribute: **NIRFSG_ATTR_AVAILABLE_PATHS**

available_ports
---------------

    .. py:attribute:: available_ports

        Returns a comma-separated list of the ports available for use based on your instrument configuration.

                        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:Available Ports**
                - C Attribute: **NIRFSG_ATTR_AVAILABLE_PORTS**

cache
-----

    .. py:attribute:: cache

        Specifies whether to cache the value of properties. When caching is enabled, NI-RFSG tracks the current NI-RFSG device settings and avoids sending redundant commands to the device. NI-RFSG can always cache or never cache particular properties, regardless of the setting of this property. Call the :py:meth:`nirfsg.Session.__init__` method to override the default value.

                        **Default Value:** True

                        **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +-------+-------------------+
        | Value | Description       |
        +=======+===================+
        | True  | Enables caching.  |
        +-------+-------------------+
        | False | Disables caching. |
        +-------+-------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Cache**
                - C Attribute: **NIRFSG_ATTR_CACHE**

compensate_for_filter_group_delay
---------------------------------

    .. py:attribute:: compensate_for_filter_group_delay

        Enables or disables compensation for filter group delay on the AWG module. This property also accounts for the upconverter group delay and aligns the RF output with the Started Event, Done Event, and Marker Events.

                        At a low I/Q rate, the group delay can become so large that some devices may not be able to align the events with the RF output, in which case you must increase the I/Q rate or disable this property.

                        **Default Value:** False

                        **Supported Devices:** PXIe-5672

                    **Defined Values**:

        +-------+-----------------------------------------------+
        | Value | Description                                   |
        +=======+===============================================+
        | True  | Enables compensation for filter group delay.  |
        +-------+-----------------------------------------------+
        | False | Disables compensation for filter group delay. |
        +-------+-----------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Advanced:Compensate for Filter Group Delay**
                - C Attribute: **NIRFSG_ATTR_COMPENSATE_FOR_FILTER_GROUP_DELAY**

configuration_settled_event_terminal_name
-----------------------------------------

    .. py:attribute:: configuration_settled_event_terminal_name

        Returns the name of the fully qualified signal name as a string.

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Default Values**:

                        PXIe-5654/5654 with PXIe-5696: /*ModuleName*/ConfigurationSettledEvent, where *ModuleName* is the name of your device in MAX.

                        PXIe-5830/5831/5832: /*BasebandModule*/ao/0/ConfigurationSettledEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.

                        PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/ConfigurationSettledEvent, where *ModuleName* is the name of your device in MAX.

                        **Related Topics**

                        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

                        `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Configuration Settled Event Terminal Name**
                - C Attribute: **NIRFSG_ATTR_CONFIGURATION_SETTLED_EVENT_TERMINAL_NAME**

correction_temperature
----------------------

    .. py:attribute:: correction_temperature

        Specifies the temperature, in degrees Celsius, to use for adjusting the device settings to correct for temperature changes. If you set this property, NI-RFSG uses the value you specify and therefore no longer uses the actual device temperature as the correction temperature. If you do not set this property, NI-RFSG checks the current device temperature in the Committed state and automatically sets the value of this property.

                        PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This property is read only.

                        **Units**: Degrees Celsius

                        **Supported Devices**: PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860



        .. note:: - Resetting this property reverts back to the default unset behavior.

             - Use this property only when your application requires the same settings to be used every time, regardless of the temperature variation. In these cases, it is best to ensure that the temperature does not vary too much.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Advanced:Correction Temperature**
                - C Attribute: **NIRFSG_ATTR_CORRECTION_TEMPERATURE**

data_transfer_block_size
------------------------

    .. py:attribute:: data_transfer_block_size

        Indicates the number of samples to transfer at one time from the device to host memory. This property is useful when the total data to be transferred to onboard memory is large.

                        **Units**: samples (s)

                        **Default Value**: 1Ms

                        **Supported Devices:** PXIe-5672/5673/5673E

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Data Transfer:Data Transfer Block Size**
                - C Attribute: **NIRFSG_ATTR_DATA_TRANSFER_BLOCK_SIZE**

data_transfer_maximum_bandwidth
-------------------------------

    .. py:attribute:: data_transfer_maximum_bandwidth

        Specifies the maximum amount of bus bandwidth to use for data transfers.

                        **Units**: bytes per second

                        **Default Value**: Device maximum

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

                        **Related Topics**

                        `Improving Streaming Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/improving_streaming_performance.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Data Transfer:Maximum Bandwidth**
                - C Attribute: **NIRFSG_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH**

data_transfer_maximum_in_flight_reads
-------------------------------------

    .. py:attribute:: data_transfer_maximum_in_flight_reads

        Specifies the maximum number of concurrent PCI Express read requests the RF signal generator can issue.

                        When transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this property is set to the highest value the RF signal generator supports.

                        If other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the RF signal generator issues. This helps to reduce the amount of data the signal generator reads at one time.

                        **Units**: number of packets

                        **Default Value**: Device maximum

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

                        **Related Topics**

                        `Improving Streaming Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/improving_streaming_performance.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Data Transfer:Advanced:Maximum In-Flight Read Requests**
                - C Attribute: **NIRFSG_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS**

data_transfer_preferred_packet_size
-----------------------------------

    .. py:attribute:: data_transfer_preferred_packet_size

        Specifies the preferred size of the data field in a PCI Express read request packet.

                        In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI RF signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.

                        Recommended values for this property are powers of two between 64 and 512.

                        **Units**: bytes

                        **Default Value**: Device maximum

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E

                        **Related Topics**

                        `Improving Streaming Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/improving_streaming_performance.html>`_



        .. note:: In some cases, the RF signal generator generates packets smaller than the preferred size you set with this property.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Data Transfer:Advanced:Preferred Packet Size**
                - C Attribute: **NIRFSG_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE**

deembedding_compensation_gain
-----------------------------

    .. py:attribute:: deembedding_compensation_gain

        Returns the de-embedding gain applied to compensate for the mismatch on the specified port. If de-embedding is enabled, NI-RFSG uses the returned compensation gain to remove the effects of the external network between the instrument and the DUT.

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860




        .. tip:: This property can be set/get on specific deembedding_port within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container deembedding_port to specify a subset.

            Example: :py:attr:`my_session.deembedding_port[ ... ].deembedding_compensation_gain`

            To set/get on all deembedding_port, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.deembedding_compensation_gain`

        The following table lists the characteristics of this property.

            +-----------------------+------------------+
            | Characteristic        | Value            |
            +=======================+==================+
            | Datatype              | float            |
            +-----------------------+------------------+
            | Permissions           | read only        |
            +-----------------------+------------------+
            | Repeated Capabilities | deembedding_port |
            +-----------------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **De-embedding:Compensation Gain**
                - C Attribute: **NIRFSG_ATTR_DEEMBEDDING_COMPENSATION_GAIN**

deembedding_selected_table
--------------------------

    .. py:attribute:: deembedding_selected_table

        Selects the de-embedding table to apply to the measurements on the specified port.

                        To use this property, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_string` method to specify the name of the port to configure for de-embedding.

                        If de-embedding is enabled, NI-RFSG uses the specified table to remove the effects of the external network between the instrument and the DUT.

                        Use the create deembedding sparameter table array method to create tables.

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860




        .. tip:: This property can be set/get on specific deembedding_port within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container deembedding_port to specify a subset.

            Example: :py:attr:`my_session.deembedding_port[ ... ].deembedding_selected_table`

            To set/get on all deembedding_port, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.deembedding_selected_table`

        The following table lists the characteristics of this property.

            +-----------------------+------------------+
            | Characteristic        | Value            |
            +=======================+==================+
            | Datatype              | str              |
            +-----------------------+------------------+
            | Permissions           | read-write       |
            +-----------------------+------------------+
            | Repeated Capabilities | deembedding_port |
            +-----------------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **De-embedding:Selected Table**
                - C Attribute: **NIRFSG_ATTR_DEEMBEDDING_SELECTED_TABLE**

deembedding_type
----------------

    .. py:attribute:: deembedding_type

        Specifies the type of de-embedding to apply to measurements on the specified port.

                        To use this property, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_int32` method to specify the name of the port to configure for de-embedding.

                        If you set this property to :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_SCALAR` or :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_VECTOR`, NI-RFSG adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT.

                        **Default Value**: :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_SCALAR`

                        **Valid Values for PXIe-5830/5832/5840/5841/5842/5860** : :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_SCALAR` or :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_NONE`

                        **Valid Values for PXIe-5831** :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_SCALAR`, :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_VECTOR`, or :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_NONE`. :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_VECTOR` is only supported for TRX Ports in a Semiconductor Test System (STS).

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +--------------------------------------------------------------------+----------------+------------------------------------------------------------------------+
        | Name                                                               | Value          | Description                                                            |
        +====================================================================+================+========================================================================+
        | :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_NONE`   | 25000 (0x61a8) | De-embedding is not applied to the measurement.                        |
        +--------------------------------------------------------------------+----------------+------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_SCALAR` | 25001 (0x61a9) | De-embeds the measurement using only the gain term.                    |
        +--------------------------------------------------------------------+----------------+------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DeembeddingTypeAttrVals.DEEMBEDDING_TYPE_VECTOR` | 25002 (0x61aa) | De-embeds the measurement using the gain term and the reflection term. |
        +--------------------------------------------------------------------+----------------+------------------------------------------------------------------------+


        .. tip:: This property can be set/get on specific deembedding_port within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container deembedding_port to specify a subset.

            Example: :py:attr:`my_session.deembedding_port[ ... ].deembedding_type`

            To set/get on all deembedding_port, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.deembedding_type`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------+
            | Characteristic        | Value                         |
            +=======================+===============================+
            | Datatype              | enums.DeembeddingTypeAttrVals |
            +-----------------------+-------------------------------+
            | Permissions           | read-write                    |
            +-----------------------+-------------------------------+
            | Repeated Capabilities | deembedding_port              |
            +-----------------------+-------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **De-embedding:Type**
                - C Attribute: **NIRFSG_ATTR_DEEMBEDDING_TYPE**

device_instantaneous_bandwidth
------------------------------

    .. py:attribute:: device_instantaneous_bandwidth

        Specifies the bandwidth of the device. The instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration.

                        The :py:attr:`nirfsg.Session.signal_bandwidth` centered at the :py:attr:`nirfsg.Session.frequency` must fit within the device instantaneous bandwidth, which is centered at the :py:attr:`nirfsg.Session.upconverter_center_frequency`.

                        **Units**: Hz

                        **Default Value**: N/A

                        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

                        `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

                        `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Device Instantaneous Bandwidth (Hz)**
                - C Attribute: **NIRFSG_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH**

device_temperature
------------------

    .. py:attribute:: device_temperature

        Returns the device temperature. If the NI-RFSG session is controlling multiple devices, this property returns the temperature of the primary NI RF device. The NI-RFSG session is opened using the primary RF device name.

                        Serial signals between the sensor and the system control unit could modulate the signal being generated, thus causing phase spurs. After the device thoroughly warms up, its temperature varies only slightly (less than 1 degree Celsius) and slowly, and it is not necessary to constantly poll this temperature sensor.

                        PXIe-5644/5645/5646, PXIe-5820/5840/5841: If you query this property during RF list mode, list steps may take longer to complete during list execution.

                        PXIe-5830/5831/5832: To use this property, you must first set the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_real64` method to using the appropriate string for your instrument configuration. Setting the :py:meth:`nirfsg.Session._set_attribute_vi_real64` method is not required for the PXIe-3621/3622. Refer to the following table to determine which strings are valid for your configuration.

                        **Units**: degrees Celsius (°C)

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Temperature Monitoring <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5611_temperature_monitoring.html>`_

                        `Thermal Shutdown <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_shutdown_monitoring_5650_5651_5652.html>`_

        +----------------------------+--------------------------+-------------------------+
        | Hardware Module            | TRX Port Type            | Active Channel String   |
        +============================+==========================+=========================+
        | PXIe-3621/3622             | —                        | if or "" (empty string) |
        +----------------------------+--------------------------+-------------------------+
        | PXIe-5820                  | —                        | fpga                    |
        +----------------------------+--------------------------+-------------------------+
        | First connected mmRH-5582  | DIRECT TRX PORTS Only    | rf0                     |
        +----------------------------+--------------------------+-------------------------+
        | First connected mmRH-5582  | SWITCHED TRX PORTS [0-7] | rf0switch0              |
        +----------------------------+--------------------------+-------------------------+
        | First connected mmRH-5582  | SWITCHED TRX PORTS [0-7] | rf0switch1              |
        +----------------------------+--------------------------+-------------------------+
        | Second connected mmRH-5582 | DIRECT TRX PORTS Only    | rf1                     |
        +----------------------------+--------------------------+-------------------------+
        | Second connected mmRH-5582 | SWITCHED TRX PORTS [0-7] | rf1switch0              |
        +----------------------------+--------------------------+-------------------------+
        | Second connected mmRH-5582 | SWITCHED TRX PORTS [0-7] | rf1switch1              |
        +----------------------------+--------------------------+-------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Device Temperature (Degrees C)**
                - C Attribute: **NIRFSG_ATTR_DEVICE_TEMPERATURE**

digital_edge_script_trigger_edge
--------------------------------

    .. py:attribute:: digital_edge_script_trigger_edge

        Specifies the active edge for the Script Trigger. This property is used when the :py:attr:`nirfsg.Session.script_trigger_type` property is set to digital edge. To set the :py:attr:`nirfsg.Session.digital_edge_script_trigger_edge` property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.ScriptTrigDigEdgeEdge.RISING`

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

                        `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_digital_edge_script_trigger`

                    **Defined Values**:

        +--------------------------------------------------+---------+-------------------------------------------------------------------------------+
        | Name                                             | Value   | Description                                                                   |
        +==================================================+=========+===============================================================================+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeEdge.FALLING` | 1 (0x1) | Asserts the trigger when the signal transitions from high level to low level. |
        +--------------------------------------------------+---------+-------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeEdge.RISING`  | 0 (0x0) | Asserts the trigger when the signal transitions from low level to high level. |
        +--------------------------------------------------+---------+-------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

            Example: :py:attr:`my_session.script_triggers[ ... ].digital_edge_script_trigger_edge`

            To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.digital_edge_script_trigger_edge`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.ScriptTrigDigEdgeEdge |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | script_triggers             |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Digital Edge:Edge**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE**

digital_edge_script_trigger_source
----------------------------------

    .. py:attribute:: digital_edge_script_trigger_source

        Specifies the source terminal for the Script Trigger. This property is used when the :py:attr:`nirfsg.Session.script_trigger_type` property is set to digital edge. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

                        `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

                        `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_digital_edge_script_trigger`

                    **Defined Values**:

        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                           | Value       | Description                                                                                                                             |
        +================================================================+=============+=========================================================================================================================================+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PFI0`                | PFI0        | The trigger is received on PFI 0.                                                                                                       |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PFI1`                | PFI1        | The trigger is received on PFI 1.                                                                                                       |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PFI2`                | PFI2        | The trigger is received on PFI 2.                                                                                                       |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PFI3`                | PFI3        | The trigger is received on PFI 3.                                                                                                       |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PXI_STAR`            | PXI_Star    | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                              |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PXI_TRIG0`           | PXI_Trig0   | The trigger is received on PXI trigger line 0.                                                                                          |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PXI_TRIG1`           | PXI_Trig1   | The trigger is received on PXI trigger line 1.                                                                                          |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PXI_TRIG2`           | PXI_Trig2   | The trigger is received on PXI trigger line 2.                                                                                          |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PXI_TRIG3`           | PXI_Trig3   | The trigger is received on PXI trigger line 3.                                                                                          |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PXI_TRIG4`           | PXI_Trig4   | The trigger is received on PXI trigger line 4.                                                                                          |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PXI_TRIG5`           | PXI_Trig5   | The trigger is received on PXI trigger line 5.                                                                                          |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PXI_TRIG6`           | PXI_Trig6   | The trigger is received on PXI trigger line 6.                                                                                          |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PXI_TRIG7`           | PXI_Trig7   | The trigger is received on PXI trigger line 7.                                                                                          |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PXIE_DSTARB`         | PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.PULSE_IN`            | PulseIn     | The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.                                            |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.DIO0`                | DIO/PFI0    | The trigger is received on PFI0 from the front panel DIO terminal.                                                                      |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.DIO1`                | DIO/PFI1    | The trigger is received on PFI1 from the front panel DIO terminal.                                                                      |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.DIO2`                | DIO/PFI2    | The trigger is received on PFI2 from the front panel DIO terminal.                                                                      |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.DIO3`                | DIO/PFI3    | The trigger is received on PFI3 from the front panel DIO terminal.                                                                      |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.DIO4`                | DIO/PFI4    | The trigger is received on PFI4 from the front panel DIO terminal.                                                                      |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.DIO5`                | DIO/PFI5    | The trigger is received on PFI5 from the front panel DIO terminal.                                                                      |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.DIO6`                | DIO/PFI6    | The trigger is received on PFI6 from the front panel DIO terminal.                                                                      |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.DIO7`                | DIO/PFI7    | The trigger is received on PFI7 from the front panel DIO terminal.                                                                      |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.SYNC_SCRIPT_TRIGGER` | Sync_Script | The trigger is received on the Sync Script trigger line. This value is valid on only the PXIe-5644/5645/5646.                           |
        +----------------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

            Example: :py:attr:`my_session.script_triggers[ ... ].digital_edge_script_trigger_source`

            To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.digital_edge_script_trigger_source`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------+
            | Characteristic        | Value                         |
            +=======================+===============================+
            | Datatype              | enums.ScriptTrigDigEdgeSource |
            +-----------------------+-------------------------------+
            | Permissions           | read-write                    |
            +-----------------------+-------------------------------+
            | Repeated Capabilities | script_triggers               |
            +-----------------------+-------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Digital Edge:Source**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE**

digital_edge_start_trigger_edge
-------------------------------

    .. py:attribute:: digital_edge_start_trigger_edge

        Specifies the active edge for the Start Trigger. This property is used when the :py:attr:`nirfsg.Session.start_trigger_type` property is set to digital edge. To set the :py:attr:`nirfsg.Session.digital_edge_start_trigger_edge` property, the NI-RFSG device must be in the Configuration state.

                        PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.

                        **Default Value:** :py:data:`~nirfsg.StartTrigDigEdgeEdge.RISING`

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

                        `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_digital_edge_start_trigger`

                    **Defined Values**:

        +-------------------------------------------------+---------+------------------------------------------------------------------+
        | Name                                            | Value   | Description                                                      |
        +=================================================+=========+==================================================================+
        | :py:data:`~nirfsg.StartTrigDigEdgeEdge.FALLING` | 1 (0x1) | Occurs when the signal transitions from high level to low level. |
        +-------------------------------------------------+---------+------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeEdge.RISING`  | 0 (0x0) | Occurs when the signal transitions from low level to high level. |
        +-------------------------------------------------+---------+------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.StartTrigDigEdgeEdge |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Digital Edge**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

digital_edge_start_trigger_source
---------------------------------

    .. py:attribute:: digital_edge_start_trigger_source

        Specifies the source terminal for the Start Trigger. This property is used when the :py:attr:`nirfsg.Session.start_trigger_type` property is set to digital edge. The :py:attr:`nirfsg.Session.digital_edge_start_trigger_source` property is not case-sensitive. To set the :py:attr:`nirfsg.Session.digital_edge_start_trigger_source` property, the NI-RFSG device must be in the Configuration state.

                        PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

                        `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

                        `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_digital_edge_start_trigger`

                    **Defined Values**:

        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                           | Value       | Description                                                                                                                            |
        +================================================================+=============+========================================================================================================================================+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PFI0`                 | PFI0        | The trigger is received on PFI 0.                                                                                                      |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PFI1`                 | PFI1        | The trigger is received on PFI 1.                                                                                                      |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PFI2`                 | PFI2        | The trigger is received on PFI 2.                                                                                                      |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PFI3`                 | PFI3        | The trigger is received on PFI 3.                                                                                                      |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PXI_STAR`             | PXI_Star    | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                             |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PXI_TRIG0`            | PXI_Trig0   | The trigger is received on PXI trigger line 0.                                                                                         |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PXI_TRIG1`            | PXI_Trig1   | The trigger is received on PXI trigger line 1.                                                                                         |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PXI_TRIG2`            | PXI_Trig2   | The trigger is received on PXI trigger line 2.                                                                                         |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PXI_TRIG3`            | PXI_Trig3   | The trigger is received on PXI trigger line 3.                                                                                         |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PXI_TRIG4`            | PXI_Trig4   | The trigger is received on PXI trigger line 4.                                                                                         |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PXI_TRIG5`            | PXI_Trig5   | The trigger is received on PXI trigger line 5.                                                                                         |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PXI_TRIG6`            | PXI_Trig6   | The trigger is received on PXI trigger line 6.                                                                                         |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PXI_TRIG7`            | PXI_Trig7   | The trigger is received on PXI trigger line 7.                                                                                         |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.PXIE_DSTARB`          | PXIe_DStarB | The trigger is received on the PXI DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.TRIG_IN`              | TrigIn      | The trigger is received on the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.                    |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.DIO0`                 | DIO/PFI0    | The trigger is received on PFI0 from the front panel DIO terminal.                                                                     |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.DIO1`                 | DIO/PFI1    | The trigger is received on PFI1 from the front panel DIO terminal.                                                                     |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.DIO2`                 | DIO/PFI2    | The trigger is received on PFI2 from the front panel DIO terminal.                                                                     |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.DIO3`                 | DIO/PFI3    | The trigger is received on PFI3 from the front panel DIO terminal.                                                                     |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.DIO4`                 | DIO/PFI4    | The trigger is received on PFI4 from the front panel DIO terminal.                                                                     |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.DIO5`                 | DIO/PFI5    | The trigger is received on PFI5 from the front panel DIO terminal.                                                                     |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.DIO6`                 | DIO/PFI6    | The trigger is received on PFI6 from the front panel DIO terminal.                                                                     |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigDigEdgeSource.DIO7`                 | DIO/PFI7    | The trigger is received on PFI7 from the front panel DIO terminal.                                                                     |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigEdgeSource.SYNC_SCRIPT_TRIGGER` | Sync_Script | The trigger is received on the Sync Script trigger line. This value is valid on only the PXIe-5644/5645/5646.                          |
        +----------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------+
            | Characteristic        | Value                        |
            +=======================+==============================+
            | Datatype              | enums.StartTrigDigEdgeSource |
            +-----------------------+------------------------------+
            | Permissions           | read-write                   |
            +-----------------------+------------------------------+
            | Repeated Capabilities | None                         |
            +-----------------------+------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Digital Edge:Source**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE**

digital_equalization_enabled
----------------------------

    .. py:attribute:: digital_equalization_enabled

        When this property is enabled, NI-RFSG equalizes the waveform data to correct for variations in the response of the NI-RFSG device. Enabling digital equalization improves the modulation error rates (MER) and error vector magnitude (EVM) for signals with large bandwidths (\>500 kHz), but it increases tuning times.

                        On the PXI-5670/5671, equalization is performed in the software, so tuning time is increased. On the PXIe-5672, equalization is performed in the hardware so that there is no compromise in performance.

                        This property applies only when the :py:attr:`nirfsg.Session.generation_mode` property is set to :py:data:`~nirfsg.GenerationMode.ARB_WAVEFORM` or :py:data:`~nirfsg.GenerationMode.SCRIPT`. To set this property, the NI-RFSG device must be in the Configuration state.

                        PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: :py:data:`~nirfsg.DigitalEqualizationEnabled.ENABLE` is the only supported value for this device.

                        **Default Value:**

                        PXI-5670/5671: :py:data:`~nirfsg.DigitalEqualizationEnabled.DISABLE`

                        PXIe-5644/5645/5646, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: :py:data:`~nirfsg.DigitalEqualizationEnabled.ENABLE`

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Response and Software Equalization <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/if_response_and_equalizer.html>`_—Refer to this topic for more information about equalization performed in software.

                        `Frequency Tuning Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.html>`_

                    **Defined Values**:

        +-------------------------------------------------------+---------+-----------------------+
        | Name                                                  | Value   | Description           |
        +=======================================================+=========+=======================+
        | :py:data:`~nirfsg.DigitalEqualizationEnabled.DISABLE` | 0 (0x0) | Filter is not applied |
        +-------------------------------------------------------+---------+-----------------------+
        | :py:data:`~nirfsg.DigitalEqualizationEnabled.ENABLE`  | 1 (0x1) | Filter is applied.    |
        +-------------------------------------------------------+---------+-----------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.DigitalEqualizationEnabled |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | None                             |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Digital Equalization Enabled**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_EQUALIZATION_ENABLED**

digital_level_script_trigger_active_level
-----------------------------------------

    .. py:attribute:: digital_level_script_trigger_active_level

        Specifies the active level for the Script Trigger. This property is used when the :py:attr:`nirfsg.Session.script_trigger_type` property is set to :py:data:`~nirfsg.ScriptTrigType.DIGITAL_LEVEL`.

                        **Default Value:** :py:data:`~nirfsg.ScriptTrigDigLevelActiveLevel.HIGH`

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860



                        **Related Topics**

                        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

                        `Digital Level Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_level.html>`_

                    **Defined Values**:

        +-------------------------------------------------------+---------------+--------------------------------------------------+
        | Name                                                  | Value         | Description                                      |
        +=======================================================+===============+==================================================+
        | :py:data:`~nirfsg.ScriptTrigDigLevelActiveLevel.HIGH` | 9000 (0x2328) | Trigger when the digital trigger signal is high. |
        +-------------------------------------------------------+---------------+--------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelActiveLevel.LOW`  | 9001 (0x2329) | Trigger when the digital trigger signal is low.  |
        +-------------------------------------------------------+---------------+--------------------------------------------------+


        .. tip:: This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

            Example: :py:attr:`my_session.script_triggers[ ... ].digital_level_script_trigger_active_level`

            To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.digital_level_script_trigger_active_level`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------+
            | Characteristic        | Value                               |
            +=======================+=====================================+
            | Datatype              | enums.ScriptTrigDigLevelActiveLevel |
            +-----------------------+-------------------------------------+
            | Permissions           | read-write                          |
            +-----------------------+-------------------------------------+
            | Repeated Capabilities | script_triggers                     |
            +-----------------------+-------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Digital Level:Active Level**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL**

digital_level_script_trigger_source
-----------------------------------

    .. py:attribute:: digital_level_script_trigger_source

        Specifies the source terminal for the Script Trigger. This property is used when the :py:attr:`nirfsg.Session.script_trigger_type` property is set to :py:data:`~nirfsg.ScriptTrigType.DIGITAL_LEVEL`. The :py:attr:`nirfsg.Session.digital_level_script_trigger_source` property is not case-sensitive.

                        To set the :py:attr:`nirfsg.Session.digital_level_script_trigger_source` property, the NI-RFSG device must be in the Configuration state.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

                        `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

                        `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

                    **Defined Values**:

        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                    | Value       | Description                                                                                                                             |
        +=========================================================+=============+=========================================================================================================================================+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PFI0`        | PFI0        | The trigger is received on PFI 0.                                                                                                       |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PFI1`        | PFI1        | The trigger is received on PFI 1.                                                                                                       |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PFI2`        | PFI2        | The trigger is received on PFI 2.                                                                                                       |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PFI3`        | PFI3        | The trigger is received on PFI 3.                                                                                                       |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PXI_STAR`    | PXI_Star    | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                              |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PXI_TRIG0`   | PXI_Trig0   | The trigger is received on PXI trigger line 0.                                                                                          |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PXI_TRIG1`   | PXI_Trig1   | The trigger is received on PXI trigger line 1.                                                                                          |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PXI_TRIG2`   | PXI_Trig2   | The trigger is received on PXI trigger line 2.                                                                                          |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PXI_TRIG3`   | PXI_Trig3   | The trigger is received on PXI trigger line 3.                                                                                          |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PXI_TRIG4`   | PXI_Trig4   | The trigger is received on PXI trigger line 4.                                                                                          |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PXI_TRIG5`   | PXI_Trig5   | The trigger is received on PXI trigger line 5.                                                                                          |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PXI_TRIG6`   | PXI_Trig6   | The trigger is received on PXI trigger line 6.                                                                                          |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PXI_TRIG7`   | PXI_Trig7   | The trigger is received on PXI trigger line 7.                                                                                          |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PXIE_DSTARB` | PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.PULSE_IN`    | PulseIn     | The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.                                            |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.DIO0`        | DIO/PFI0    | The trigger is received on PFI0 from the front panel DIO terminal.                                                                      |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.DIO1`        | DIO/PFI1    | The trigger is received on PFI1 from the front panel DIO terminal.                                                                      |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.DIO2`        | DIO/PFI2    | The trigger is received on PFI2 from the front panel DIO terminal.                                                                      |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.DIO3`        | DIO/PFI3    | The trigger is received on PFI3 from the front panel DIO terminal.                                                                      |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.DIO4`        | DIO/PFI4    | The trigger is received on PFI4 from the front panel DIO terminal.                                                                      |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.DIO5`        | DIO/PFI5    | The trigger is received on PFI5 from the front panel DIO terminal.                                                                      |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.DIO6`        | DIO/PFI6    | The trigger is received on PFI6 from the front panel DIO terminal.                                                                      |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelSource.DIO7`        | DIO/PFI7    | The trigger is received on PFI7 from the front panel DIO terminal.                                                                      |
        +---------------------------------------------------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

            Example: :py:attr:`my_session.script_triggers[ ... ].digital_level_script_trigger_source`

            To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.digital_level_script_trigger_source`

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------------+
            | Characteristic        | Value                          |
            +=======================+================================+
            | Datatype              | enums.ScriptTrigDigLevelSource |
            +-----------------------+--------------------------------+
            | Permissions           | read-write                     |
            +-----------------------+--------------------------------+
            | Repeated Capabilities | script_triggers                |
            +-----------------------+--------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Digital Level:Source**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE**

digital_modulation_fsk_deviation
--------------------------------

    .. py:attribute:: digital_modulation_fsk_deviation

        Specifies the deviation to use in FSK modulation.

                        **Units**: hertz (Hz)

                        **Default Value:** 1,000

                        **Supported Devices:** PXI/PXIe-5650/5651/5652

                        **Related Topics**

                        `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Digital:FSK Deviation (Hz)**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_MODULATION_FSK_DEVIATION**

digital_modulation_prbs_order
-----------------------------

    .. py:attribute:: digital_modulation_prbs_order

        Specifies the order of pseudorandom bit sequence (PRBS) internally generated by hardware and used as the message signal in digital modulation.

                        **Default Value:** 16

                        **Supported Devices:** PXI/PXIe-5650/5651/5652

                        **Related Topics**

                        `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Digital:PRBS Order**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_MODULATION_PRBS_ORDER**

digital_modulation_prbs_seed
----------------------------

    .. py:attribute:: digital_modulation_prbs_seed

        Specifies the seed of the internally generated pseudorandom bit sequence (PRBS).

                        **Default Value:** 1

                        **Supported Devices:** PXI/PXIe-5650/5651/5652

                        **Related Topics**

                        `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Digital:PRBS Seed**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_MODULATION_PRBS_SEED**

digital_modulation_symbol_rate
------------------------------

    .. py:attribute:: digital_modulation_symbol_rate

        Specifies the symbol rate of the bit stream for digital modulation.

                        **Units**: hertz (Hz)

                        **Default Value:** 1kHz

                        **Supported Devices:** PXI/PXIe-5650/5651/5652

                        **Related Topics**

                        `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Digital:Symbol Rate**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_MODULATION_SYMBOL_RATE**

digital_modulation_type
-----------------------

    .. py:attribute:: digital_modulation_type

        Specifies the digital modulation format to use.

                        **Default Value:** :py:data:`~nirfsg.DigModType.NONE`

                        **Supported Devices:** PXI/PXIe-5650/5651/5652

                        **Related Topics**

                        `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

                    **Defined Values**:

        +------------------------------------+--------------+-----------------------------------------------------------------------------+
        | Name                               | Value        | Description                                                                 |
        +====================================+==============+=============================================================================+
        | :py:data:`~nirfsg.DigModType.FSK`  | 4000 (0xfa0) | Specifies that the digital modulation type is frequency-shift keying (FSK). |
        +------------------------------------+--------------+-----------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DigModType.NONE` | 0 (0x0)      | Disables digital modulation.                                                |
        +------------------------------------+--------------+-----------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DigModType.OOK`  | 4001 (0xfa1) | Specifies that the digital modulation type is on-off keying (OOK).          |
        +------------------------------------+--------------+-----------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DigModType.PSK`  | 4002 (0xfa2) | Specifies that the digital modulation type is phase-shift keying (PSK).     |
        +------------------------------------+--------------+-----------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------+
            | Characteristic        | Value            |
            +=======================+==================+
            | Datatype              | enums.DigModType |
            +-----------------------+------------------+
            | Permissions           | read-write       |
            +-----------------------+------------------+
            | Repeated Capabilities | None             |
            +-----------------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Digital:Modulation Type**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_MODULATION_TYPE**

digital_modulation_waveform_type
--------------------------------

    .. py:attribute:: digital_modulation_waveform_type

        Specifies the type of waveform to use as the message signal in digital modulation.

                        **Default Value:** :py:data:`~nirfsg.DigModWfmType.PRBS`

                        **Supported Devices:** PXI/PXIe-5650/5651/5652

                        **Related Topics**

                        `Modulation Schemes <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/modulation_modes.html>`_

                    **Defined Values**:

        +-----------------------------------------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                          | Value         | Description                                                                                                                                                                                              |
        +===============================================+===============+==========================================================================================================================================================================================================+
        | :py:data:`~nirfsg.DigModWfmType.PRBS`         | 5000 (0x1388) | Specifies that the digital modulation waveform type is pseudorandom bit sequence (PRBS).                                                                                                                 |
        +-----------------------------------------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DigModWfmType.USER_DEFINED` | 5001 (0x1389) | Specifies that the digital modulation waveform type is user defined. To specify the user-defined waveform, call the :py:meth:`nirfsg.Session.configure_digital_modulation_user_defined_waveform` method. |
        +-----------------------------------------------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.DigModWfmType |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | None                |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Digital:Waveform Type**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_MODULATION_WAVEFORM_TYPE**

digital_pattern
---------------

    .. py:attribute:: digital_pattern

        Enables or disables digital pattern on the PXI-5421/5441 AWG module. This property must be set to True to enable signal routing to and from the Digital Data & Control connector.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** False

                        **Supported Devices:** PXI-5670/5671

                    **Defined Values**:

        +-------+--------------------------+
        | Value | Description              |
        +=======+==========================+
        | True  | Signal routing enabled.  |
        +-------+--------------------------+
        | False | Signal routing disabled. |
        +-------+--------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Digital Pattern**
                - C Attribute: **NIRFSG_ATTR_DIGITAL_PATTERN**

direct_download
---------------

    .. py:attribute:: direct_download

        Specifies whether the :py:meth:`nirfsg.Session.WriteArbWaveform` method immediately writes waveforms to the device or copies the waveform to host memory for later download. NI-RFSG reads and validates this property when an arbitrary waveform is first allocated.

                        For the PXI-5670, direct download is always disabled. For all other devices, direct download is always enabled.

                        PXI-5671: To increase performance when using large waveforms, enable direct download. To maximize reconfigurability, disable direct download.

                        Perform the following steps to enable direct download:



                        1\. Set the I/Q rate to less than or equal to 8.33MS/s with the :py:attr:`nirfsg.Session.iq_rate` property.

                        2\. Set the :py:attr:`nirfsg.Session.power_level_type` property to :py:data:`~nirfsg.PowerLevelType.PEAK`.

                        3\. Disable the :py:attr:`nirfsg.Session.iq_swap_enabled` property.

                        4\. Disable the :py:attr:`nirfsg.Session.digital_equalization_enabled` property.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5840/5841/5842/5860

                    **Defined Values**:

        +-----------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                          | Value     | Description                                                                                                                             |
        +===============================================+===========+=========================================================================================================================================+
        | :py:data:`~nirfsg.DirectDownload.DISABLE`     | 0 (0x0)   | The RF In local oscillator signal is not present at the front panel LO OUT connector.                                                   |
        +-----------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DirectDownload.ENABLE`      | 1 (0x1)   | The RF In local oscillator signal is present at the front panel LO OUT connector.                                                       |
        +-----------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DirectDownload.UNSPECIFIED` | -2 (-0x2) | The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it. |
        +-----------------------------------------------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.DirectDownload |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Data Transfer:Direct Download**
                - C Attribute: **NIRFSG_ATTR_DIRECT_DOWNLOAD**

done_event_terminal_name
------------------------

    .. py:attribute:: done_event_terminal_name

        Returns the name of the fully qualified signal name as a string.

                        **Default Values**:

                        PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/DoneEvent, where *AWGName* is the name of your associated AWG module in MAX.

                        PXIe-5830/5831/5832: /*BasebandModule*/ao/0/DoneEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.

                        PXIe-5820/5840/5841: /*ModuleName*/ao/0/DoneEvent, where *ModuleName* is the name of your device in MAX.

                        PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/DoneEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

                        `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.GetTerminalName`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Done Event Terminal Name**
                - C Attribute: **NIRFSG_ATTR_DONE_EVENT_TERMINAL_NAME**

events_delay
------------

    .. py:attribute:: events_delay

        Specifies the delay, in seconds, applied to the Started Event, Done Event, and all Marker Events with respect to the analog output of the RF signal generator. To set this property, the NI-RFSG device must be in the Configuration or Generation state.

                        By default, markers and events are delayed to align with the waveform data generated from the device. This property adds an additional delay to markers and events. Use this property to adjust the time delay between events and the corresponding data.

                        **Units:** Seconds

                        **Valid Values:**

                        PXIe-5644/5645: -1.217 μs to 67.050 μs

                        PXIe-5646: -0.896 μs to 64.640 μs

                        PXIe-5820/5830/5831/5832/5840/5841/5842: 0 μs to 3.276 μs

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_



        .. note:: If you decrease the event delay during generation, some markers may be dropped.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Events:Events Delay**
                - C Attribute: **NIRFSG_ATTR_EVENTS_DELAY**

exported_configuration_settled_event_output_terminal
----------------------------------------------------

    .. py:attribute:: exported_configuration_settled_event_output_terminal

        Specifies the destination terminal for exporting the Configuration Settled event. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

                        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

                        `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

                        `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

                    **Defined Values**:

        +----------------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
        | Name                                                                       | Value       | Description                                                                                                        |
        +============================================================================+=============+====================================================================================================================+
        | :py:data:`~nirfsg.ConfigurationSettledEventExportOutputTerm.DO_NOT_EXPORT` |             | The signal is not exported.                                                                                        |
        +----------------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ConfigurationSettledEventExportOutputTerm.PXI_TRIG0`     | PXI_Trig0   | The trigger is received on PXI trigger line 0.                                                                     |
        +----------------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ConfigurationSettledEventExportOutputTerm.PXI_TRIG1`     | PXI_Trig1   | The trigger is received on PXI trigger line 1.                                                                     |
        +----------------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ConfigurationSettledEventExportOutputTerm.PXI_TRIG2`     | PXI_Trig2   | The trigger is received on PXI trigger line 2.                                                                     |
        +----------------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ConfigurationSettledEventExportOutputTerm.PXI_TRIG3`     | PXI_Trig3   | The trigger is received on PXI trigger line 3.                                                                     |
        +----------------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ConfigurationSettledEventExportOutputTerm.PXI_TRIG4`     | PXI_Trig4   | The trigger is received on PXI trigger line 4.                                                                     |
        +----------------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ConfigurationSettledEventExportOutputTerm.PXI_TRIG5`     | PXI_Trig5   | The trigger is received on PXI trigger line 5.                                                                     |
        +----------------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ConfigurationSettledEventExportOutputTerm.PXI_TRIG6`     | PXI_Trig6   | The trigger is received on PXI trigger line 6.                                                                     |
        +----------------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ConfigurationSettledEventExportOutputTerm.PXIE_DSTARC`   | PXIe_DStarC | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5840/5841/5842. |
        +----------------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ConfigurationSettledEventExportOutputTerm.TRIG_OUT`      | TrigOut     | TRIG IN/OUT terminal.                                                                                              |
        +----------------------------------------------------------------------------+-------------+--------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------+
            | Characteristic        | Value                                           |
            +=======================+=================================================+
            | Datatype              | enums.ConfigurationSettledEventExportOutputTerm |
            +-----------------------+-------------------------------------------------+
            | Permissions           | read-write                                      |
            +-----------------------+-------------------------------------------------+
            | Repeated Capabilities | None                                            |
            +-----------------------+-------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Configuration Settled Event Export Output Terminal**
                - C Attribute: **NIRFSG_ATTR_EXPORTED_CONFIGURATION_SETTLED_EVENT_OUTPUT_TERMINAL**

exported_done_event_output_terminal
-----------------------------------

    .. py:attribute:: exported_done_event_output_terminal

        Specifies the destination terminal for exporting the Done event. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

                        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

                        `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

                        `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.export_signal`

                    **Defined Values**:

        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                       | Value       | Description                                                                                                                     |
        +============================================================+=============+=================================================================================================================================+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.DO_NOT_EXPORT` |             | The signal is not exported.                                                                                                     |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PFI0`          | PFI0        | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PFI1`          | PFI1        | The signal is exported to the PFI 1 connector.                                                                                  |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PFI4`          | PFI4        | The signal is exported to the PFI 4 connector.                                                                                  |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PFI5`          | PFI5        | The signal is exported to the PFI 5 connector.                                                                                  |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PXI_TRIG0`     | PXI_Trig0   | The trigger is received on PXI trigger line 0.                                                                                  |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PXI_TRIG1`     | PXI_Trig1   | The trigger is received on PXI trigger line 1.                                                                                  |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PXI_TRIG2`     | PXI_Trig2   | The trigger is received on PXI trigger line 2.                                                                                  |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PXI_TRIG3`     | PXI_Trig3   | The trigger is received on PXI trigger line 3.                                                                                  |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PXI_TRIG4`     | PXI_Trig4   | The trigger is received on PXI trigger line 4.                                                                                  |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PXI_TRIG5`     | PXI_Trig5   | The trigger is received on PXI trigger line 5.                                                                                  |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PXI_TRIG6`     | PXI_Trig6   | The trigger is received on PXI trigger line 6.                                                                                  |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.PXIE_DSTARC`   | PXIe_DStarC | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.    |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.DIO0`          | DIO/PFI0    | The trigger is received on PFI0 from the front panel DIO terminal.                                                              |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.DIO1`          | DIO/PFI1    | The trigger is received on PFI1 from the front panel DIO terminal.                                                              |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.DIO2`          | DIO/PFI2    | The trigger is received on PFI2 from the front panel DIO terminal.                                                              |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.DIO3`          | DIO/PFI3    | The trigger is received on PFI3 from the front panel DIO terminal.                                                              |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.DIO4`          | DIO/PFI4    | The trigger is received on PFI4 from the front panel DIO terminal.                                                              |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.DIO5`          | DIO/PFI5    | The trigger is received on PFI5 from the front panel DIO terminal.                                                              |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.DIO6`          | DIO/PFI6    | The trigger is received on PFI6 from the front panel DIO terminal.                                                              |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.DoneEventExportOutputTerm.DIO7`          | DIO/PFI7    | The trigger is received on PFI7 from the front panel DIO terminal.                                                              |
        +------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.DoneEventExportOutputTerm |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Done Event Export Output Terminal**
                - C Attribute: **NIRFSG_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL**

exported_marker_event_output_terminal
-------------------------------------

    .. py:attribute:: exported_marker_event_output_terminal

        Specifies the destination terminal for exporting the Marker Event. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

                        `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

                        `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.export_signal`

                    **Defined Values**:

        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                         | Value       | Description                                                                                                                     |
        +==============================================================+=============+=================================================================================================================================+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.DO_NOT_EXPORT` |             | The signal is not exported.                                                                                                     |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PFI0`          | PFI0        | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PFI1`          | PFI1        | The signal is exported to the PFI 1 connector.                                                                                  |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PFI4`          | PFI4        | The signal is exported to the PFI 4 connector.                                                                                  |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PFI5`          | PFI5        | The signal is exported to the PFI 5 connector.                                                                                  |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PXI_TRIG0`     | PXI_Trig0   | The trigger is received on PXI trigger line 0.                                                                                  |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PXI_TRIG1`     | PXI_Trig1   | The trigger is received on PXI trigger line 1.                                                                                  |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PXI_TRIG2`     | PXI_Trig2   | The trigger is received on PXI trigger line 2.                                                                                  |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PXI_TRIG3`     | PXI_Trig3   | The trigger is received on PXI trigger line 3.                                                                                  |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PXI_TRIG4`     | PXI_Trig4   | The trigger is received on PXI trigger line 4.                                                                                  |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PXI_TRIG5`     | PXI_Trig5   | The trigger is received on PXI trigger line 5.                                                                                  |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PXI_TRIG6`     | PXI_Trig6   | The trigger is received on PXI trigger line 6.                                                                                  |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.PXIE_DSTARC`   | PXIe_DStarC | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.    |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.DIO0`          | DIO/PFI0    | The trigger is received on PFI0 from the front panel DIO terminal.                                                              |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.DIO1`          | DIO/PFI1    | The trigger is received on PFI1 from the front panel DIO terminal.                                                              |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.DIO2`          | DIO/PFI2    | The trigger is received on PFI2 from the front panel DIO terminal.                                                              |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.DIO3`          | DIO/PFI3    | The trigger is received on PFI3 from the front panel DIO terminal.                                                              |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.DIO4`          | DIO/PFI4    | The trigger is received on PFI4 from the front panel DIO terminal.                                                              |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.DIO5`          | DIO/PFI5    | The trigger is received on PFI5 from the front panel DIO terminal.                                                              |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.DIO6`          | DIO/PFI6    | The trigger is received on PFI6 from the front panel DIO terminal.                                                              |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventExportOutputTerm.DIO7`          | DIO/PFI7    | The trigger is received on PFI7 from the front panel DIO terminal.                                                              |
        +--------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container markers to specify a subset.

            Example: :py:attr:`my_session.markers[ ... ].exported_marker_event_output_terminal`

            To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.exported_marker_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------------+
            | Characteristic        | Value                             |
            +=======================+===================================+
            | Datatype              | enums.MarkerEventExportOutputTerm |
            +-----------------------+-----------------------------------+
            | Permissions           | read-write                        |
            +-----------------------+-----------------------------------+
            | Repeated Capabilities | markers                           |
            +-----------------------+-----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Output Terminal**
                - C Attribute: **NIRFSG_ATTR_EXPORTED_MARKER_EVENT_OUTPUT_TERMINAL**

exported_pulse_modulation_event_active_level
--------------------------------------------

    .. py:attribute:: exported_pulse_modulation_event_active_level

        Specifies the active level of the exported Pulse Modulation Event. When `property pulse modulation enabled` is Enabled, `pulse modulation active level` is `active high`, `exported pulse modulation event output terminal` is `PulseOut`, and this property is `active high`, then the Pulse Modulation Event will transition from Low to High after the the Pulse In signal is set to logic high, and the RF Output has settled. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.ScriptTrigDigLevelActiveLevel.HIGH`

                        **Supported Devices:**  PXIe-5842

                    **Defined Values**:

        +-------------------------------------------------------+---------------+--------------------------------------------------+
        | Name                                                  | Value         | Description                                      |
        +=======================================================+===============+==================================================+
        | :py:data:`~nirfsg.ScriptTrigDigLevelActiveLevel.HIGH` | 9000 (0x2328) | Trigger when the digital trigger signal is high. |
        +-------------------------------------------------------+---------------+--------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelActiveLevel.LOW`  | 9001 (0x2329) | Trigger when the digital trigger signal is low.  |
        +-------------------------------------------------------+---------------+--------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------+
            | Characteristic        | Value                               |
            +=======================+=====================================+
            | Datatype              | enums.ScriptTrigDigLevelActiveLevel |
            +-----------------------+-------------------------------------+
            | Permissions           | read-write                          |
            +-----------------------+-------------------------------------+
            | Repeated Capabilities | None                                |
            +-----------------------+-------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Pulse Modulation:Exported Pulse Modulation Event Active Level**
                - C Attribute: **NIRFSG_ATTR_EXPORTED_PULSE_MODULATION_EVENT_ACTIVE_LEVEL**

exported_pulse_modulation_event_output_terminal
-----------------------------------------------

    .. py:attribute:: exported_pulse_modulation_event_output_terminal

        Specifies the destination terminal for exporting the Pulse Modulation Event. The Pulse Modulation Event tracks the RF Envelope when Pulse Modulation is Enabled. If this property is set to a value other than `do not export str`, calling NI-RFSG Commit will cause the output terminal to be pulled to the logic level that is the inverse of `exported pulse modulation event active level`. You can tri-state this terminal by setting this property to `do not export str` or by calling `niRFSG Reset`. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.PulseModulationOutputTerm.PULSE_OUT`

                        **Supported Devices:**  PXIe-5842

                    **Defined Values**:

        +------------------------------------------------------------+----------+-------------------+
        | Name                                                       | Value    | Description       |
        +============================================================+==========+===================+
        | :py:data:`~nirfsg.PulseModulationOutputTerm.DO_NOT_EXPORT` |          | yet to be defined |
        +------------------------------------------------------------+----------+-------------------+
        | :py:data:`~nirfsg.PulseModulationOutputTerm.PULSE_OUT`     | PulseOut | yet to be defined |
        +------------------------------------------------------------+----------+-------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.PulseModulationOutputTerm |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Pulse Modulation:Exported Pulse Modulation Event Output Terminal**
                - C Attribute: **NIRFSG_ATTR_EXPORTED_PULSE_MODULATION_EVENT_OUTPUT_TERMINAL**

exported_ref_clock_output_terminal
----------------------------------

    .. py:attribute:: exported_ref_clock_output_terminal

        Specifies the destination terminal for exporting the Reference Clock on the RF signal generators. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.ReferenceClockExportOutputTerminal.DO_NOT_EXPORT`

                        **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Interconnecting Multiple NI 5673E Modules <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/interconnecting_multiple_ni_5673_modules.html>`_

                    **Defined Values**:

        Name (Value): Description

        :py:data:`~nirfsg.ReferenceClockExportOutputTerminal.DO_NOT_EXPORT` () :The Reference Clock signal is not exported.

        :py:data:`~nirfsg.ReferenceClockExportOutputTerminal.REF_OUT` (RefOut) :Exports the Reference Clock signal to the REF OUT connector of the device.

        :py:data:`~nirfsg.ReferenceClockExportOutputTerminal.REF_OUT2` (RefOut2) :Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable.

        :py:data:`~nirfsg.ReferenceClockExportOutputTerminal.CLK_OUT` (ClkOut) :Exports the Reference Clock signal to the CLK OUT connector of the device.

        +---------------------------------------------------------------------+---------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                                | Value   | Description                                                                                | Supported devices                                                                                                                                                     |
        +=====================================================================+=========+============================================================================================+=======================================================================================================================================================================+
        | :py:data:`~nirfsg.ReferenceClockExportOutputTerminal.CLK_OUT`       | ClkOut  | Exports the Reference Clock signal to the CLK OUT connector of the device.                 | Supported on PXIe-5673, 5673E                                                                                                                                         |
        +---------------------------------------------------------------------+---------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ReferenceClockExportOutputTerminal.DO_NOT_EXPORT` |         | The Reference Clock signal is not exported.                                                | Supported on PXIe-5644/5645/5646, 5820/5830/5831/5832/5840/5841/5842/5860, 5650/5651/5652, 5654, 5673, 5673E, PXIe-5654 with PXIe-5696, PXI-5650/5651/5652 (See Note) |
        +---------------------------------------------------------------------+---------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ReferenceClockExportOutputTerminal.REF_OUT`       | RefOut  | Exports the Reference Clock signal to the REF OUT connector of the device.                 | Supported on PXIe-5644/5645/5646, 5820/5830/5831/5832/5840/5841/5842/5860, 5650/5651/5653, 5653, 5654, 5673, 5673E, PXIe-5654 with PXIe-5696, PXI-5650/5651/5653,     |
        +---------------------------------------------------------------------+---------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ReferenceClockExportOutputTerminal.REF_OUT2`      | RefOut2 | Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable. | Supported on PXIe-5650/5651/5652, 5654, 5673E, PXIe-5654 with PXIe-5696                                                                                               |
        +---------------------------------------------------------------------+---------+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: The :py:data:`~nirfsg.ReferenceClockExportOutputTerminal.REF_OUT2` output terminal value is valid for only the PXIe-5650/5651/5652, not the PXI-5650/5651/5652.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------------------+
            | Characteristic        | Value                                    |
            +=======================+==========================================+
            | Datatype              | enums.ReferenceClockExportOutputTerminal |
            +-----------------------+------------------------------------------+
            | Permissions           | read-write                               |
            +-----------------------+------------------------------------------+
            | Repeated Capabilities | None                                     |
            +-----------------------+------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clock:Reference Clock Export Output Terminal**
                - C Attribute: **NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL**

exported_ref_clock_rate
-----------------------

    .. py:attribute:: exported_ref_clock_rate

        Specifies the Reference Clock Rate, in Hz, of the signal sent to the Reference Clock Export Output Terminal. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.ReferenceClockExportedRate._10mhz`

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +-------------------------------------------------------+---------------------+-------------------------------------+
        | Name                                                  | Value               | Description                         |
        +=======================================================+=====================+=====================================+
        | :py:data:`~nirfsg.ReferenceClockExportedRate._10mhz`  | 10000000 (0x989680) | Uses a 10MHz Reference Clock rate.  |
        +-------------------------------------------------------+---------------------+-------------------------------------+
        | :py:data:`~nirfsg.ReferenceClockExportedRate._100mhz` |                     | Uses a 100MHz Reference Clock rate. |
        +-------------------------------------------------------+---------------------+-------------------------------------+
        | :py:data:`~nirfsg.ReferenceClockExportedRate._1ghz`   |                     | Uses a 1GHz Reference Clock rate.   |
        +-------------------------------------------------------+---------------------+-------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.ReferenceClockExportedRate |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | None                             |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clock:Reference Clock Exported Rate (Hz)**
                - C Attribute: **NIRFSG_ATTR_EXPORTED_REF_CLOCK_RATE**

exported_script_trigger_output_terminal
---------------------------------------

    .. py:attribute:: exported_script_trigger_output_terminal

        Specifies the destination terminal for exporting the Script Trigger. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_ —Refer to this topic for information about trigger delay.

                        `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

                        `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.export_signal`

                    **Defined Values**:

        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                        | Value       | Description                                                                                                                     |
        +=============================================================+=============+=================================================================================================================================+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.DO_NOT_EXPORT` |             | The signal is not exported.                                                                                                     |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PFI0`          | PFI0        | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PFI1`          | PFI1        | The signal is exported to the PFI 1 connector.                                                                                  |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PFI4`          | PFI4        | The signal is exported to the PFI 4 connector.                                                                                  |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PFI5`          | PFI5        | The signal is exported to the PFI 5 connector.                                                                                  |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PXI_TRIG0`     | PXI_Trig0   | The trigger is received on PXI trigger line 0.                                                                                  |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PXI_TRIG1`     | PXI_Trig1   | The trigger is received on PXI trigger line 1.                                                                                  |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PXI_TRIG2`     | PXI_Trig2   | The trigger is received on PXI trigger line 2.                                                                                  |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PXI_TRIG3`     | PXI_Trig3   | The trigger is received on PXI trigger line 3.                                                                                  |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PXI_TRIG4`     | PXI_Trig4   | The trigger is received on PXI trigger line 4.                                                                                  |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PXI_TRIG5`     | PXI_Trig5   | The trigger is received on PXI trigger line 5.                                                                                  |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PXI_TRIG6`     | PXI_Trig6   | The trigger is received on PXI trigger line 6.                                                                                  |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.PXIE_DSTARC`   | PXIe_DStarC | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.    |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.DIO0`          | DIO/PFI0    | The trigger is received on PFI0 from the front panel DIO terminal.                                                              |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.DIO1`          | DIO/PFI1    | The trigger is received on PFI1 from the front panel DIO terminal.                                                              |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.DIO2`          | DIO/PFI2    | The trigger is received on PFI2 from the front panel DIO terminal.                                                              |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.DIO3`          | DIO/PFI3    | The trigger is received on PFI3 from the front panel DIO terminal.                                                              |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.DIO4`          | DIO/PFI4    | The trigger is received on PFI4 from the front panel DIO terminal.                                                              |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.DIO5`          | DIO/PFI5    | The trigger is received on PFI5 from the front panel DIO terminal.                                                              |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.DIO6`          | DIO/PFI6    | The trigger is received on PFI6 from the front panel DIO terminal.                                                              |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigExportOutputTerm.DIO7`          | DIO/PFI7    | The trigger is received on PFI7 from the front panel DIO terminal.                                                              |
        +-------------------------------------------------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

            Example: :py:attr:`my_session.script_triggers[ ... ].exported_script_trigger_output_terminal`

            To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.exported_script_trigger_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.ScriptTrigExportOutputTerm |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | script_triggers                  |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Export Output Terminal**
                - C Attribute: **NIRFSG_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL**

exported_started_event_output_terminal
--------------------------------------

    .. py:attribute:: exported_started_event_output_terminal

        Specifies the destination terminal for exporting the Started event. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

                        `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

                        `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.export_signal`

                    **Defined Values**:

        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                          | Value       | Description                                                                                                                            |
        +===============================================================+=============+========================================================================================================================================+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.DO_NOT_EXPORT` |             | The signal is not exported.                                                                                                            |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PFI0`          | PFI0        | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.        |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PFI1`          | PFI1        | The signal is exported to the PFI 1 connector.                                                                                         |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PFI4`          | PFI4        | The signal is exported to the PFI 4 connector.                                                                                         |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PFI5`          | PFI5        | The signal is exported to the PFI 5 connector.                                                                                         |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PXI_TRIG0`     | PXI_Trig0   | The trigger is received on PXI trigger line 0.                                                                                         |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PXI_TRIG1`     | PXI_Trig1   | The trigger is received on PXI trigger line 1.                                                                                         |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PXI_TRIG2`     | PXI_Trig2   | The trigger is received on PXI trigger line 2.                                                                                         |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PXI_TRIG3`     | PXI_Trig3   | The trigger is received on PXI trigger line 3.                                                                                         |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PXI_TRIG4`     | PXI_Trig4   | The trigger is received on PXI trigger line 4.                                                                                         |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PXI_TRIG5`     | PXI_Trig5   | The trigger is received on PXI trigger line 5.                                                                                         |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PXI_TRIG6`     | PXI_Trig6   | The trigger is received on PXI trigger line 6.                                                                                         |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.PXIE_DSTARC`   | PXIe_DStarC | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.DIO0`          | DIO/PFI0    | The trigger is received on PFI0 from the front panel DIO terminal.                                                                     |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.DIO1`          | DIO/PFI1    | The trigger is received on PFI1 from the front panel DIO terminal.                                                                     |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.DIO2`          | DIO/PFI2    | The trigger is received on PFI2 from the front panel DIO terminal.                                                                     |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.DIO3`          | DIO/PFI3    | The trigger is received on PFI3 from the front panel DIO terminal.                                                                     |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.DIO4`          | DIO/PFI4    | The trigger is received on PFI4 from the front panel DIO terminal.                                                                     |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.DIO5`          | DIO/PFI5    | The trigger is received on PFI5 from the front panel DIO terminal.                                                                     |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.DIO6`          | DIO/PFI6    | The trigger is received on PFI6 from the front panel DIO terminal.                                                                     |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartedEventExportOutputTerm.DIO7`          | DIO/PFI7    | The trigger is received on PFI7 from the front panel DIO terminal.                                                                     |
        +---------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------------+
            | Characteristic        | Value                              |
            +=======================+====================================+
            | Datatype              | enums.StartedEventExportOutputTerm |
            +-----------------------+------------------------------------+
            | Permissions           | read-write                         |
            +-----------------------+------------------------------------+
            | Repeated Capabilities | None                               |
            +-----------------------+------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Started Event Export Output Terminal**
                - C Attribute: **NIRFSG_ATTR_EXPORTED_STARTED_EVENT_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_start_trigger_output_terminal

        Specifies the destination terminal for exporting the Start Trigger. To set this property, the NI-RFSG device must be in the Configuration state.

                        PXIe-5654/5654 with PXIe-5696: The Start Trigger is valid only with a timer-based list when RF list mode is enabled.

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

                        `PFI Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pfi_lines.html>`_

                        `PXI Trigger Lines <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_trigger.html>`_

                    **Defined Values**:

        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                       | Value       | Description                                                                                                                            |
        +============================================================+=============+========================================================================================================================================+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.DO_NOT_EXPORT` |             | The signal is not exported.                                                                                                            |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PFI0`          | PFI0        | The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.        |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PFI1`          | PFI1        | The signal is exported to the PFI 1 connector.                                                                                         |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PFI4`          | PFI4        | The signal is exported to the PFI 4 connector.                                                                                         |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PFI5`          | PFI5        | The signal is exported to the PFI 5 connector.                                                                                         |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PXI_TRIG0`     | PXI_Trig0   | The trigger is received on PXI trigger line 0.                                                                                         |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PXI_TRIG1`     | PXI_Trig1   | The trigger is received on PXI trigger line 1.                                                                                         |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PXI_TRIG2`     | PXI_Trig2   | The trigger is received on PXI trigger line 2.                                                                                         |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PXI_TRIG3`     | PXI_Trig3   | The trigger is received on PXI trigger line 3.                                                                                         |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PXI_TRIG4`     | PXI_Trig4   | The trigger is received on PXI trigger line 4.                                                                                         |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PXI_TRIG5`     | PXI_Trig5   | The trigger is received on PXI trigger line 5.                                                                                         |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PXI_TRIG6`     | PXI_Trig6   | The trigger is received on PXI trigger line 6.                                                                                         |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.PXIE_DSTARC`   | PXIe_DStarC | The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.TRIG_OUT`      | TrigOut     | The signal is exported to the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.                     |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.DIO0`          | DIO/PFI0    | The trigger is received on PFI0 from the front panel DIO terminal.                                                                     |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.DIO1`          | DIO/PFI1    | The trigger is received on PFI1 from the front panel DIO terminal.                                                                     |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.DIO2`          | DIO/PFI2    | The trigger is received on PFI2 from the front panel DIO terminal.                                                                     |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.DIO3`          | DIO/PFI3    | The trigger is received on PFI3 from the front panel DIO terminal.                                                                     |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.DIO4`          | DIO/PFI4    | The trigger is received on PFI4 from the front panel DIO terminal.                                                                     |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.DIO5`          | DIO/PFI5    | The trigger is received on PFI5 from the front panel DIO terminal.                                                                     |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.DIO6`          | DIO/PFI6    | The trigger is received on PFI6 from the front panel DIO terminal.                                                                     |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigExportOutputTerm.DIO7`          | DIO/PFI7    | The trigger is received on PFI7 from the front panel DIO terminal.                                                                     |
        +------------------------------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.StartTrigExportOutputTerm |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Export Output Terminal**
                - C Attribute: **NIRFSG_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

external_calibration_recommended_interval
-----------------------------------------

    .. py:attribute:: external_calibration_recommended_interval

        Returns the recommended interval between each external calibration of the device.

                        **Units**: months

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **External Calibration:Recommended Interval**
                - C Attribute: **NIRFSG_ATTR_EXTERNAL_CALIBRATION_RECOMMENDED_INTERVAL**

external_calibration_temperature
--------------------------------

    .. py:attribute:: external_calibration_temperature

        Returns the temperature of the device at the time of the last external calibration.

                        **Units**: degrees Celsius (°C)

                        **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **External Calibration:Last External Calibration Temperature**
                - C Attribute: **NIRFSG_ATTR_EXTERNAL_CALIBRATION_TEMPERATURE**

external_gain
-------------

    .. py:attribute:: external_gain

        Specifies the external amplification or attenuation, if any, between the RF signal generator and the device under test.

                        Positive values for this property represent amplification, and negative values for this property represent attenuation.

                        **Valid Values:** -INF dB to +INF dB

                        **Default Value:** 0dB

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860



        .. note:: - Setting this property adjusts the actual device output power to compensate for any amplification or attenuation between the RF signal generator and the device under test.

             - For the PXIe-5645, this property is ignored if you are using the I/Q ports.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:External Gain (dB)**
                - C Attribute: **NIRFSG_ATTR_EXTERNAL_GAIN**

fast_tuning_option
------------------

    .. py:attribute:: fast_tuning_option

        Returns whether the NI RF signal generator has the fast tuning option available.

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696

                        **Related Topics**

                        `Frequency Tuning Times for 5654 <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.5654.html>`_

                    **Defined Values**:

        +-------+------------------------------------------------------------+
        | Value | Description                                                |
        +=======+============================================================+
        | True  | The RF signal generator has the fast 100 µs tuning option. |
        +-------+------------------------------------------------------------+
        | False | The RF signal generator has the 1 ms tuning option.        |
        +-------+------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Options:Fast Tuning Option**
                - C Attribute: **NIRFSG_ATTR_FAST_TUNING_OPTION**

fixed_group_delay_across_ports
------------------------------

    .. py:attribute:: fixed_group_delay_across_ports

        Specifies a comma-separated list of ports for which to fix the group delay.


                        **Supported Devices:** PXIe-5831/5832

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:Fixed Group Delay Across Ports**
                - C Attribute: **NIRFSG_ATTR_FIXED_GROUP_DELAY_ACROSS_PORTS**

fpga_bitfile_path
-----------------

    .. py:attribute:: fpga_bitfile_path

        Returns a string containing the path to the location of the current NI-RFSG instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device. You can specify the bitfile location using the Driver Setup string in the **optionString** parameter of the :py:meth:`nirfsg.Session.__init__` method.

                        NI-RFSG instrument driver FPGA extensions enable you to use pre-compiled FPGA bitfiles to customize the behavior of the vector signal transceiver FPGA while maintaining the functionality of the NI-RFSG instrument driver.

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `NI-RFSG Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/fpga_extensions.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Device Characteristics:FPGA Bitfile Path**
                - C Attribute: **NIRFSG_ATTR_FPGA_BITFILE_PATH**

fpga_target_name
----------------

    .. py:attribute:: fpga_target_name

        Returns a string that contains the name of the FPGA target being used. This name can be used with the RIO open session to open a reference to the FPGA.

                        This property is channel dependent if multiple FPGA targets are supported.

                        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:FPGA Target Name**
                - C Attribute: **NIRFSG_ATTR_FPGA_TARGET_NAME**

fpga_temperature
----------------

    .. py:attribute:: fpga_temperature

        Returns the FPGA temperature in degrees Celsius.

                        Serial signals between the sensor and the system control unit can potentially modulate the signal being generated, thus causing phase spurs. After the device thoroughly warms up, its temperature varies only slightly (less than 1 degree Celsius) and slowly, and it is not necessary to constantly poll this temperature sensor.

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860



        .. note:: If you query this property during RF list mode, list steps may take longer to complete during list execution.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:FPGA Temperature (Degrees C)**
                - C Attribute: **NIRFSG_ATTR_FPGA_TEMPERATURE**

frequency
---------

    .. py:attribute:: frequency

        Specifies the frequency of the generated RF signal. For arbitrary waveform generation, this property specifies the center frequency of the signal.

                        The PXI-5670/5671, PXIe-5672, PXIe-5820, and PXIe-5860 must be in the Configuration state to use this property. However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 can be in the Configuration or the Generation state to use this property.

                        **Units**: hertz (Hz)

                        **Defined Values**:
                        Refer to the specifications document for your device allowable frequency settings.

                        **Default Value:**

                        PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E: 100MHz

                        PXIe-5653: 4GHz

                        PXIe-5820: 0Hz

                        PXIe-5830/5831/5832: 6.5 GHz

                        PXIe-5840/5841/5860, PXI-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options): 1GHz

                        PXIe-5842 (4 GHz bandwidth option) using the Standard personality: 1GHz

                        PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality: 6.5GHz

                        **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.ConfigureRf`



        .. note:: For the PXIe-5645, this property is ignored if you are using the I/Q ports.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Frequency (Hz)**
                - C Attribute: **NIRFSG_ATTR_FREQUENCY**

frequency_settling
------------------

    .. py:attribute:: frequency_settling

        Specifies the frequency settling time. Interpretation of this value depends on the :py:attr:`nirfsg.Session.frequency_settling_units` property.

                        **Valid Values:**

                        The valid values for this property depend on the :py:attr:`nirfsg.Session.frequency_settling_units` property.




                        **Default Value**: 1.0

                        **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Settling Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/settling_times.html>`_

                        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Frequency Settling**
                - C Attribute: **NIRFSG_ATTR_FREQUENCY_SETTLING**

frequency_settling_units
------------------------

    .. py:attribute:: frequency_settling_units

        Specifies the interpretation of the value passed to the :py:attr:`nirfsg.Session.frequency_settling` property.

                        PXIe-5650/5651/5652/5653, PXIe-5673E: When the :py:attr:`nirfsg.Session.ACTIVE_CONFIGURATION_LIST` property is set to a valid list name, the :py:attr:`nirfsg.Session.frequency_settling_units` property supports only :py:data:`~nirfsg.FrequencySettlingUnits.TIME_AFTER_IO` as a valid value.

                        PXIe-5654/5654 with PXIe-5696: The :py:attr:`nirfsg.Session.frequency_settling_units` property supports only :py:data:`~nirfsg.FrequencySettlingUnits.TIME_AFTER_IO` and :py:data:`~nirfsg.FrequencySettlingUnits.PPM` as valid values.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

                        **Default Value**: :py:data:`~nirfsg.FrequencySettlingUnits.PPM`

                        **Related Topics**

                        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

                    **Defined Values**:

        +-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
        | Name                                                      | Description                                                                                                     |
        +===========================================================+=================================================================================================================+
        | :py:data:`~nirfsg.FrequencySettlingUnits.TIME_AFTER_LOCK` | Specifies the time to wait after the frequency PLL locks.                                                       |
        +-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.FrequencySettlingUnits.TIME_AFTER_IO`   | Specifies the time to wait after all writes occur to change the frequency.                                      |
        +-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.FrequencySettlingUnits.PPM`             | Specifies the minimum frequency accuracy when settling completes. Units are in parts per million (PPM or 1E-6). |
        +-----------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

        .. note:: If you set this property to :py:data:`~nirfsg.FrequencySettlingUnits.TIME_AFTER_IO`, the definition of settled for the Configuration Settled event changes.

        .. note:: One or more of the referenced properties are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------+
            | Characteristic        | Value                        |
            +=======================+==============================+
            | Datatype              | enums.FrequencySettlingUnits |
            +-----------------------+------------------------------+
            | Permissions           | read-write                   |
            +-----------------------+------------------------------+
            | Repeated Capabilities | None                         |
            +-----------------------+------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Frequency Settling Units**
                - C Attribute: **NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS**

frequency_tolerance
-------------------

    .. py:attribute:: frequency_tolerance

        Specifies the allowable frequency error introduced during the software upconversion process. NI-RFSG may introduce a frequency error up to the specified amount to optimize computational speed and onboard memory usage while upconverting phase-continuous signals.

                        If the :py:attr:`nirfsg.Session.phase_continuity_enabled` property is set to :py:data:`~nirfsg.NIRFSG_VAL_DISABLE`, the :py:attr:`nirfsg.Session.frequency_tolerance` property is ignored, and the driver does not introduce a frequency error. On devices that do not use software upconversion, this property is ignored. The PXI-5670 always uses software upconversion, and the PXI-5671 uses software upconversion for I/Q rates greater than 8.33MS/s.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Units**: hertz (Hz)

                        **Default Value:** 50

                        **Supported Devices:** PXI-5670/5671

                        **Related Topics**

                        `Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Frequency Tolerance (Hz)**
                - C Attribute: **NIRFSG_ATTR_FREQUENCY_TOLERANCE**

generation_mode
---------------

    .. py:attribute:: generation_mode

        Specifies whether to generate a continuous wave (CW) signal, the arbitrary waveform specified by the :py:attr:`nirfsg.Session.arb_selected_waveform` property, or the script specified by the :py:attr:`nirfsg.Session.selected_script` property, upon calling the :py:meth:`nirfsg.Session._initiate` method.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.GenerationMode.CW`

                        **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696 (CW support only), PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

                        `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_—Refer to this topic for more information about scripting.

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_generation_mode`

                    **Defined Values**:

        +------------------------------------------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                           | Value        | Description                                                                                                                                      |
        +================================================+==============+==================================================================================================================================================+
        | :py:data:`~nirfsg.GenerationMode.ARB_WAVEFORM` | 1001 (0x3e9) | Configures the RF signal generator to generate the arbitrary waveform specified by the :py:attr:`nirfsg.Session.arb_selected_waveform` property. |
        +------------------------------------------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.GenerationMode.CW`           | 1000 (0x3e8) | Configures the RF signal generator to generate a CW signal.                                                                                      |
        +------------------------------------------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.GenerationMode.SCRIPT`       | 1002 (0x3ea) | Configures the RF signal generator to generate arbitrary waveforms as directed by the :py:attr:`nirfsg.Session.selected_script` property..       |
        +------------------------------------------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.GenerationMode |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Generation Mode**
                - C Attribute: **NIRFSG_ATTR_GENERATION_MODE**

group_capabilities
------------------

    .. py:attribute:: group_capabilities

        Returns a string that contains a comma-separated list of class-extension groups that NI-RFSG implements.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities**
                - C Attribute: **NIRFSG_ATTR_GROUP_CAPABILITIES**

host_dma_buffer_size
--------------------

    .. py:attribute:: host_dma_buffer_size

        Specifies the size of the DMA buffer in computer memory, in bytes. To set this property, the NI-RFSG device must be in the Configuration state.

                        A sufficiently large host DMA buffer improves performance by allowing large writes to be transferred more efficiently.

                        **Units:** bytes

                        **Default Value:** 8MB

                        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Data Transfer:Advanced:Host DMA Buffer Size**
                - C Attribute: **NIRFSG_ATTR_HOST_DMA_BUFFER_SIZE**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        Returns a string that contains the firmware revision information for the NI-RFSG device you are currently using.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.RevisionQuery`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Firmware Revision**
                - C Attribute: **NIRFSG_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        Returns a string that contains the name of the manufacturer of the NI-RFSG device you are currently using.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Manufacturer**
                - C Attribute: **NIRFSG_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        Returns a string that contains the model number or name of the NI-RFSG device that you are currently using. For drivers that support more than one device, this property returns a comma-separated list of supported devices.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Model**
                - C Attribute: **NIRFSG_ATTR_INSTRUMENT_MODEL**

interchange_check
-----------------

    .. py:attribute:: interchange_check

        Specifies whether to perform interchangeability checking and retrieve interchangeability warnings.

                        **Default Value:** False

                        **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +-------+--------------------------------+
        | Value | Description                    |
        +=======+================================+
        | True  | Interchange check is enabled.  |
        +-------+--------------------------------+
        | False | Interchange check is disabled. |
        +-------+--------------------------------+

        .. note:: Enabling interchangeability check is not supported.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Interchange Check**
                - C Attribute: **NIRFSG_ATTR_INTERCHANGE_CHECK**

interpolation_delay
-------------------

    .. py:attribute:: interpolation_delay

        Specifies the delay, in seconds, to apply to the I/Q waveform. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Units:** Seconds

                        **Valid Values:** Plus or minus half of one I/Q sample period

                        **Supported Devices:** PXIe-5644/5645/5646

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:Interpolation Delay**
                - C Attribute: **NIRFSG_ATTR_INTERPOLATION_DELAY**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Returns a string that contains the resource name NI-RFSG uses to identify the physical device. If you initialize NI-RFSG with a logical name, this property contains the resource name that corresponds to the entry in the IVI Configuration Utility. If you initialize NI-RFSG with the resource name, this property contains that value.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Resource Descriptor**
                - C Attribute: **NIRFSG_ATTR_IO_RESOURCE_DESCRIPTOR**

iq_gain_imbalance
-----------------

    .. py:attribute:: iq_gain_imbalance

        Specifies the gain imbalance of the I/Q modulator (I versus Q).

                        Gain imbalance is calculated with the following equation:


                        **Units**: dB

                        **Valid Values:**-6dB to 6dB

                        **Default Value:** 0dB

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_

                        `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **IQ Impairment:Gain Imbalance (dB)**
                - C Attribute: **NIRFSG_ATTR_IQ_GAIN_IMBALANCE**

iq_impairment_enabled
---------------------

    .. py:attribute:: iq_impairment_enabled

        Enables or disables I/Q impairment. The :py:attr:`nirfsg.Session.iq_i_offset`, :py:attr:`nirfsg.Session.iq_q_offset`, :py:attr:`nirfsg.Session.iq_gain_imbalance`, and :py:attr:`nirfsg.Session.iq_skew` properties are ignored when the :py:attr:`nirfsg.Session.iq_impairment_enabled` property is disabled.

                        **Default Value:** True

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                    **Defined Values**:

        +-------+-----------------------------+
        | Value | Description                 |
        +=======+=============================+
        | True  | I/Q impairment is enabled.  |
        +-------+-----------------------------+
        | False | I/Q impairment is disabled. |
        +-------+-----------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **IQ Impairment:Enabled**
                - C Attribute: **NIRFSG_ATTR_IQ_IMPAIRMENT_ENABLED**

iq_i_offset
-----------

    .. py:attribute:: iq_i_offset

        When using a National Instruments AWG module or vector signal transceiver (VST), this property specifies the I-signal DC offset. Units are either percent (%) or volts (V), depending on the :py:attr:`nirfsg.Session.iq_offset_units` property setting.

                        PXIe-5673/5673E: Actual AWG signal offset is equal to the I/Q modulator offset correction plus the value specified by this property. When using an external AWG (non–National Instruments AWG), this property is read-only and indicates the I/Q modulator I-offset. Units are volts, as specified by the :py:attr:`nirfsg.Session.iq_offset_units` property.

                        **Valid Values:**-100 to 100% or -0.2V to 0.2V

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **IQ Impairment:I Offset**
                - C Attribute: **NIRFSG_ATTR_IQ_I_OFFSET**

iq_offset_units
---------------

    .. py:attribute:: iq_offset_units

        Specifies the units of the :py:attr:`nirfsg.Session.iq_i_offset` property and :py:attr:`nirfsg.Session.iq_q_offset` property. Offset units are either percent or volts.

                        The AWG or VST offset is the specified percentage of the AWG or VST peak power level when the :py:attr:`nirfsg.Session.iq_offset_units` property is set to :py:data:`~nirfsg.OffsetUnits.PERCENT`. Given perfect carrier leakage suppression, the following equation is satisfied


                        or equivalently


                        If the :py:attr:`nirfsg.Session.iq_i_offset` property is set to 100%, :py:attr:`nirfsg.Session.iq_q_offset` property is set to 0%, and :py:attr:`nirfsg.Session.power_level` property set to 0 dBm, the desired RF signal is at 0 dBm and the carrier leakage is also at 0 dBm.

                        The AWG or VST peak power level changes when settings change in other properties such as the :py:attr:`nirfsg.Session.power_level`, :py:attr:`nirfsg.Session.frequency`, :py:attr:`nirfsg.Session.iq_skew`, :py:attr:`nirfsg.Session.iq_gain_imbalance`, :py:attr:`nirfsg.Session.attenuator_hold_enabled`, and :py:attr:`nirfsg.Session.arb_pre_filter_gain` properties. When the :py:attr:`nirfsg.Session.iq_offset_units` property is set to :py:data:`~nirfsg.OffsetUnits.PERCENT`, the actual AWG or VST offset changes as the AWG or VST peak power level changes to satisfy the preceding equations. These changes are useful if you are intentionally adding carrier leakage to test the tolerance of a receiver. When the :py:attr:`nirfsg.Session.iq_offset_units` property is set to :py:data:`~nirfsg.OffsetUnits.PERCENT`, the carrier leakage, in dBc, remains at a consistent level.

                        If you are trying to eliminate residual carrier leakage due to calibration inaccuracies or drift, set the :py:attr:`nirfsg.Session.iq_offset_units` property to :py:data:`~nirfsg.OffsetUnits.VOLTS`. Offset correction voltage is applied to the I/Q modulator or VST, regardless of changes to the AWG or VST peak power level.

                        **Default Value**: :py:data:`~nirfsg.OffsetUnits.PERCENT`

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                    **Defined Values**:

        +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
        | Name                                   | Description                                                                                                              |
        +========================================+==========================================================================================================================+
        | :py:data:`~nirfsg.OffsetUnits.PERCENT` | Specifies the :py:attr:`nirfsg.Session.iq_i_offset` and :py:attr:`nirfsg.Session.iq_q_offset` property units as percent. |
        +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.OffsetUnits.VOLTS`   | Specifies the :py:attr:`nirfsg.Session.iq_i_offset` and :py:attr:`nirfsg.Session.iq_q_offset` property units as volts.   |
        +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

        .. note:: For any devices except PXIe-5820, if the :py:attr:`nirfsg.Session.iq_offset_units` property is set to :py:data:`~nirfsg.OffsetUnits.VOLTS`, a 0.1 I offset results in a 0.1 V offset in the output. For PXIe-5820 devices, 0.1 I offset results in a 10% offset in the output.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.OffsetUnits |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **IQ Impairment:Offset Units**
                - C Attribute: **NIRFSG_ATTR_IQ_OFFSET_UNITS**

iq_out_port_carrier_frequency
-----------------------------

    .. py:attribute:: iq_out_port_carrier_frequency

        Specifies the frequency of the I/Q OUT port signal. The onboard signal processing (OSP) applies the specified frequency shift to the I/Q data before the data is sent to the digital-to-analog converter (DAC). To set this property, the NI-RFSG device must be in the Configuration state.

                        **Units:** hertz (Hz)

                        **Valid Values:**

                        PXIe-5645: -60MHz to 60MHz

                        PXIe-5820: -500MHz to 500MHz

                        **Supported Devices:** PXIe-5645, PXIe-5820



        .. note:: - For the PXIe-5820, NI recommends using the :py:attr:`nirfsg.Session.frequency` property.

             - For the PXIe-5645, this property is ignored if you are using the RF ports.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ Out Port:Carrier Frequency**
                - C Attribute: **NIRFSG_ATTR_IQ_OUT_PORT_CARRIER_FREQUENCY**

iq_out_port_common_mode_offset
------------------------------

    .. py:attribute:: iq_out_port_common_mode_offset

        Specifies the common-mode offset applied to the signals generated at each differential output terminal. This property applies only when you set the :py:attr:`nirfsg.Session.iq_out_port_terminal_configuration` property to :py:data:`~nirfsg.IQOutPortTermCfg.DIFFERENTIAL`. Common-mode offset shifts both positive and negative terminals in the same direction.

                        To use this property, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_real64` method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Units:** Volts

                        **Valid Values:**

                        PXIe-5645: -0.8V to 0.8V if you set the :py:attr:`nirfsg.Session.iq_out_port_load_impedance` property to 50 Ω. The valid values are -1.2V to 1.2V if you set the :py:attr:`nirfsg.Session.iq_out_port_load_impedance` property to 100 Ω.

                        PXIe-5820: -0.25V to 1.5V

                        **Supported Devices:** PXIe-5645, PXIe-5820



        .. note:: - For the PXIe-5645, this property is ignored if you are using the RF ports.

             - The valid range is dependent on the load impedance.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ Out Port:Common Mode Offset**
                - C Attribute: **NIRFSG_ATTR_IQ_OUT_PORT_COMMON_MODE_OFFSET**

iq_out_port_level
-----------------

    .. py:attribute:: iq_out_port_level

        Specifies the amplitude of the generated signal in volts, peak-to-peak (V). For example, if you set this property to 1.0, the output signal ranges from -0.5 volts to 0.5 volts.

                        To use this property, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_real64` method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        Refer to the specifications document for your device for allowable output levels.

                        **Units:** Volts, peak-to-peak (V\ :sub:`pk-pk`\ )

                        **Valid Values:**

                        PXIe-5645: 1V\ :sub:`pk-pk`\  maximum if you set the :py:attr:`nirfsg.Session.iq_out_port_terminal_configuration` property to :py:data:`~nirfsg.IQOutPortTermCfg.DIFFERENTIAL`, and 0.5V\ :sub:`pk-pk`\

        maximum if you set the :py:attr:`nirfsg.Session.iq_out_port_terminal_configuration` property to :py:data:`~nirfsg.IQOutPortTermCfg.SINGLE_ENDED`.

                        PXIe-5820: 3.4V\ :sub:`pk-pk`\ maximum for signal bandwidth less than 160MHz, and 2V\ :sub:`pk-pk`\

        maximum for signal bandwidth greater than 160MHz.

                        **Default Value:** 0.5volts

                        **Supported Devices:** PXIe-5645, PXIe-5820



        .. note:: - For the PXIe-5645, this property is ignored if you are using the RF ports.

             - The valid values are only applicable when you set the :py:attr:`nirfsg.Session.iq_out_port_load_impedance` property to 50 Ω and when you set the :py:attr:`nirfsg.Session.iq_out_port_offset` property to 0.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ Out Port:Level**
                - C Attribute: **NIRFSG_ATTR_IQ_OUT_PORT_LEVEL**

iq_out_port_load_impedance
--------------------------

    .. py:attribute:: iq_out_port_load_impedance

        Specifies the load impedance connected to the I/Q OUT port. To set this property, the NI-RFSG device must be in the Configuration state.

                        To use this property, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_real64` method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

                        **Units:** Ohms

                        **Valid Values:** Any value greater than 0. Values greater than or equal to 1 megaohms (MΩ) are interpreted as high impedance.

                        **Default Value:** 50 Ω if you set the :py:attr:`nirfsg.Session.iq_out_port_terminal_configuration` property to :py:data:`~nirfsg.IQOutPortTermCfg.SINGLE_ENDED`, and 100 Ω if you set the :py:attr:`nirfsg.Session.iq_out_port_terminal_configuration` property to :py:data:`~nirfsg.IQOutPortTermCfg.DIFFERENTIAL`.

                        **Supported Devices:** PXIe-5645, PXIe-5820



        .. note:: For the PXIe-5645, this property is ignored if you are using the RF ports.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ Out Port:Load Impedance**
                - C Attribute: **NIRFSG_ATTR_IQ_OUT_PORT_LOAD_IMPEDANCE**

iq_out_port_offset
------------------

    .. py:attribute:: iq_out_port_offset

        Specifies the value, in volts, that the signal generator adds to the arbitrary waveform data. To set this property, the NI-RFSG device must be in the Configuration state.

                        To use this property, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_real64` method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

                        PXIe-5645: The waveform may be scaled in DSP prior to adding offset and the device state may be changed in order to accommodate the requested offset.

                        PXIe-5820: The waveform is not automatically scaled in DSP. To prevent DSP overflows, use the :py:attr:`nirfsg.Session.arb_pre_filter_gain` property to scale the waveform to provide additional headroom for offsets.

                        **Units:** Volts

                        **Supported Devices:** PXIe-5645, PXIe-5820



        .. note:: For the PXIe-5645, this property is ignored if you are using the RF ports.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ Out Port:Offset**
                - C Attribute: **NIRFSG_ATTR_IQ_OUT_PORT_OFFSET**

iq_out_port_temperature
-----------------------

    .. py:attribute:: iq_out_port_temperature

        Returns the temperature, in degrees Celsius, of the I/Q Out circuitry on the device.

                        **Units:** Degrees Celsius

                        **Supported Devices:** PXIe-5645, PXIe-5820



        .. note:: If you query this property during RF list mode, list steps may take longer to complete during list execution.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ Out Port:Temperature (Degrees C)**
                - C Attribute: **NIRFSG_ATTR_IQ_OUT_PORT_TEMPERATURE**

iq_out_port_terminal_configuration
----------------------------------

    .. py:attribute:: iq_out_port_terminal_configuration

        Specifies whether to use the I/Q OUT port for differential configuration or single-ended configuration. If you set this property to :py:data:`~nirfsg.IQOutPortTermCfg.SINGLE_ENDED`, you must terminate the negative I and Q output connectors with a 50 Ohm termination.

                        If you set this property to :py:data:`~nirfsg.IQOutPortTermCfg.SINGLE_ENDED`, the positive I and Q connectors generate the resulting waveform. If you set this property to :py:data:`~nirfsg.IQOutPortTermCfg.DIFFERENTIAL`, both the positive and negative I and Q connectors generate the resulting waveform.

                        To use this property, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_int32` method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.IQOutPortTermCfg.DIFFERENTIAL`

                        PXIe-5820: The only valid value for this property is :py:data:`~nirfsg.IQOutPortTermCfg.DIFFERENTIAL`.

                        **Supported Devices:** PXIe-5645, PXIe-5820

                        **Related Topics**

                        `Differential and Single-Ended Operation (I/O Interface) <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/differential_single_ended_operation.html>`_

                    **Defined Values**:

        +--------------------------------------------------+----------------+--------------------------------------------------+
        | Name                                             | Value          | Description                                      |
        +==================================================+================+==================================================+
        | :py:data:`~nirfsg.IQOutPortTermCfg.DIFFERENTIAL` | 15000 (0x3a98) | Sets the terminal configuration to differential. |
        +--------------------------------------------------+----------------+--------------------------------------------------+
        | :py:data:`~nirfsg.IQOutPortTermCfg.SINGLE_ENDED` | 15001 (0x3a99) | Sets the terminal configuration to single-ended. |
        +--------------------------------------------------+----------------+--------------------------------------------------+

        .. note:: For the PXIe-5645, this property is ignored if you are using the RF ports.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.IQOutPortTermCfg |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ Out Port:Terminal Configuration**
                - C Attribute: **NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION**

iq_q_offset
-----------

    .. py:attribute:: iq_q_offset

        When using a National Instruments AWG module or VST device, this property specifies the Q-signal DC offset. Units are either percent (%) or volts (V), depending on the :py:attr:`nirfsg.Session.iq_offset_units` property setting.

                        PXIe-5673/5673E: Actual AWG signal offset is equal to the I/Q modulator offset correction plus the value specified by this property. When using an external AWG (non–National Instruments AWG), the :py:attr:`nirfsg.Session.iq_q_offset` property is read-only and indicates the I/Q modulator Q-offset. Units are volts, as indicated by the :py:attr:`nirfsg.Session.iq_offset_units` property.

                        **Valid Values**: -100% to 100% or -0.2V to 0.2V

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **IQ Impairment:Q Offset**
                - C Attribute: **NIRFSG_ATTR_IQ_Q_OFFSET**

iq_rate
-------

    .. py:attribute:: iq_rate

        This property specifies the I/Q rate of the arbitrary waveform. The I/Q rate is coerced to a value the hardware can achieve. Read this value back after setting it to see the actual I/Q rate. NI-RFSG internally uses an FIR filter with flat response up to (0.4 × IQ rate). Given a desired signal with the maximum frequency content *f*, sample the signal at an I/Q rate greater than or equal to ( *f*/0.4).

                        This property applies only when the :py:attr:`nirfsg.Session.generation_mode` property is set to :py:data:`~nirfsg.GenerationMode.ARB_WAVEFORM` or :py:data:`~nirfsg.GenerationMode.SCRIPT`.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        Setting this property to 50 MS/s on the PXI-5670/5671 and PXIe-5672 has the following implications:
                        - NI-RFSG is forced to place the carrier frequency at 18 MHz ± 1 MHz to avoid aliasing. This means that NI-RFSG cannot select a carrier frequency that could optimize waveform size if phase continuity is enabled.
                        - Output signal bandwidth must be <5 MHz to avoid aliasing.
                        - Close-in phase noise is higher.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

                        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate an I/Q rate with a waveform.

                        `Digital Upconverter <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/duc.html>`_

                    **Valid Values**:

        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Device                                                                   | I/Q Rates                                                                                                                                                                                                                                          |
        +==========================================================================+====================================================================================================================================================================================================================================================+
        | PXIe-5644/5645                                                           | Up to 120 MS/s.                                                                                                                                                                                                                                    |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXIe-5646                                                                | Up to 250 MS/s.                                                                                                                                                                                                                                    |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXI-5670                                                                 | 50 MS/s*                                                                                                                                                                                                                                           |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        |                                                                          | 100 MS/s*                                                                                                                                                                                                                                          |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXI-5671                                                                 | 50 MS/s*                                                                                                                                                                                                                                           |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        |                                                                          | 100 MS/s                                                                                                                                                                                                                                           |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        |                                                                          | \*(100 MS/s)/n, where n is divisible by 2 between 12 to 512, and divisible by 4 between 512 to 1,024 (n = 12, 14, 16, ..., 512, 516, 520, ..., 1,024). Setting the I/Q rate to one of these value enables the DUC.                                 |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXIe-5672                                                                | Up to 100 MS/s.                                                                                                                                                                                                                                    |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXIe-5673/5673E                                                          | Up to 200 MS/s. Note that -  If an PXIe-5450 with module revisions A or B is used as part of your PXIe-5673/5673E, the NI-FGEN NIFGEN_ATTR_COMPENSATE_FOR_FILTER_GROUP_DELAY property is disabled if the requested I/Q rate is less than 1.5 MS/s. |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXIe-5820/5830/5831/5832/5840/5841/5860                                  | Up to 1.25 GS/s.                                                                                                                                                                                                                                   |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXI-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options)                   | Up to 2.5 GS/s                                                                                                                                                                                                                                     |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        |  PXIe-5842 (4 GHz bandwidth option) using the Standard personality       | Up to 2.5 GS/s                                                                                                                                                                                                                                     |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality | 5 GS/s only.                                                                                                                                                                                                                                       |
        +--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: Use this property to associate an I/Q rate with a waveform.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:IQ**
                - C Attribute: **NIRFSG_ATTR_IQ_RATE**

iq_skew
-------

    .. py:attribute:: iq_skew

        Specifies the adjustment of the phase angle between the I and Q vectors. If the skew is zero, the phase angle is 90 degrees.

                        This property is ignored when the :py:attr:`nirfsg.Session.iq_impairment_enabled` property is disabled.

                        **Units**: degrees (°)

                        **Valid Values:**-30° to 30°

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **IQ Impairment:IQ Skew (Degrees)**
                - C Attribute: **NIRFSG_ATTR_IQ_SKEW**

iq_swap_enabled
---------------

    .. py:attribute:: iq_swap_enabled

        Enables or disables the inverse phase rotation of the I/Q signal by swapping the I and Q inputs.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** False

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                    **Defined Values**:

        +-------+---------------------------------------------------------------------+
        | Value | Description                                                         |
        +=======+=====================================================================+
        | True  | NI-RFSG device applies noninverse phase rotation of the I/Q signal. |
        +-------+---------------------------------------------------------------------+
        | False | NI-RFSG device applies inverse phase rotation of the I/Q signal.    |
        +-------+---------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIRFSG_ATTR_IQ_SWAP_ENABLED**

load_configurations_from_file_load_options
------------------------------------------

    .. py:attribute:: load_configurations_from_file_load_options

        Specifies the configurations to skip while loading from a file.

                        **Default Value:**  :py:data:`~nirfsg.LoadOptions.SKIP_NONE`

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +----------------------------------------------+-------------------------------------------------------------------+
        | Value                                        | Description                                                       |
        +==============================================+===================================================================+
        | :py:data:`~nirfsg.LoadOptions.SKIP_NONE`     | NI-RFSG loads all the configurations to the session.              |
        +----------------------------------------------+-------------------------------------------------------------------+
        | :py:data:`~nirfsg.LoadOptions.SKIP_WAVEFORM` | NI-RFSG skips loading the waveform configurations to the session. |
        +----------------------------------------------+-------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.LoadOptions |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Load Configurations:Load Options**
                - C Attribute: **NIRFSG_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS**

load_configurations_from_file_reset_options
-------------------------------------------

    .. py:attribute:: load_configurations_from_file_reset_options

        Specifies the configurations to skip to reset while loading configurations from a file.

                        **Default Value:**  :py:data:`~nirfsg.ResetOptions.SKIP_NONE`
                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +---------------------------------------------------------+------------------------------------------------------+
        | Value                                                   | Description                                          |
        +=========================================================+======================================================+
        | :py:data:`~nirfsg.ResetOptions.SKIP_NONE`               | NI-RFSG resets all configurations.                   |
        +---------------------------------------------------------+------------------------------------------------------+
        | :py:data:`~nirfsg.ResetOptions.SKIP_WAVEFORMS`          | NI-RFSG skips resetting the waveform configurations. |
        +---------------------------------------------------------+------------------------------------------------------+
        | :py:data:`~nirfsg.ResetOptions.SKIP_SCRIPTS`            | NI-RFSG skips resetting the scripts.                 |
        +---------------------------------------------------------+------------------------------------------------------+
        | :py:data:`~nirfsg.ResetOptions.SKIP_DEEMBEDDING_TABLES` | NI-RFSG skips resetting the de-embedding tables.     |
        +---------------------------------------------------------+------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------+
            | Characteristic        | Value              |
            +=======================+====================+
            | Datatype              | enums.ResetOptions |
            +-----------------------+--------------------+
            | Permissions           | read-write         |
            +-----------------------+--------------------+
            | Repeated Capabilities | None               |
            +-----------------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Load Configurations:Reset Options**
                - C Attribute: **NIRFSG_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS**

logical_name
------------

    .. py:attribute:: logical_name

        Returns a string that contains the logical name you specified when opening the current IVI session. You can pass a logical name to the :py:meth:`nirfsg.Session.Init` method or the :py:meth:`nirfsg.Session.__init__` method. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a driver session section in the IVI Configuration file. The driver session section specifies a physical device and initial user options.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NIRFSG_ATTR_LOGICAL_NAME**

loop_bandwidth
--------------

    .. py:attribute:: loop_bandwidth

        Configures the loop bandwidth of the tuning PLLs. This property is ignored on the PXI-5610, PXI-5670/5671, and PXIe-5672 for signal bandwidths greater than or equal to 10MHz. This property is ignored on the PXI/PXIe-5650/5651/5652 for RF frequencies less than 50MHz.

                        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_int32` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

                        **Default Value:**

                        PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842: :py:data:`~nirfsg.LoopBandwidth.MEDIUM`

                        PXI/PXIe-5650/5651/5652, PXIe-5673/5673E: :py:data:`~nirfsg.LoopBandwidth.NARROW`

                        **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_

                        `Modulation Implementation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5650_5651_5652_modulation_implementation.html>`_

                        `Sinusoidal Tone Versus Modulation Operation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sinusoidal_tone_versus_modulation_implementation.html>`_

                    **Defined Values**:

        +-----------------------------------------+---------+--------------------------------------------------------+
        | Name                                    | Value   | Description                                            |
        +=========================================+=========+========================================================+
        | :py:data:`~nirfsg.LoopBandwidth.MEDIUM` | 1 (0x1) | Uses the medium loop bandwidth setting for the PLL.    |
        +-----------------------------------------+---------+--------------------------------------------------------+
        | :py:data:`~nirfsg.LoopBandwidth.NARROW` | 0 (0x0) | Uses the narrowest loop bandwidth setting for the PLL. |
        +-----------------------------------------+---------+--------------------------------------------------------+
        | :py:data:`~nirfsg.LoopBandwidth.WIDE`   | 2 (0x2) | Uses the widest loop bandwidth setting for the PLL.    |
        +-----------------------------------------+---------+--------------------------------------------------------+

        .. note:: Setting this property to :py:data:`~nirfsg.LoopBandwidth.WIDE` on the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, or the PXIe-5673/5673E allows the frequency to settle significantly faster at the expense of increased phase noise. Setting this property to :py:data:`~nirfsg.LoopBandwidth.MEDIUM` is not a valid option on the PXI/PXIe-5650/5651/5652 or PXIe-5673/5673E. :py:data:`~nirfsg.LoopBandwidth.MEDIUM` is the only supported value for the PXIe-5840/5841/5842.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.LoopBandwidth |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | None                |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Loop Bandwidth**
                - C Attribute: **NIRFSG_ATTR_LOOP_BANDWIDTH**

lo_frequency
------------

    .. py:attribute:: lo_frequency

        Specifies the frequency of the LO source.

                        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_real64` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

                        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `PXIe-5830 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_configuration.html>`_

                        `PXIe-5831/5832 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_configuration.html>`_



        .. note:: This property is read/write if you are using an external LO. Otherwise, this property is read-only.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:LO Frequency (Hz)**
                - C Attribute: **NIRFSG_ATTR_LO_FREQUENCY**

lo_frequency_step_size
----------------------

    .. py:attribute:: lo_frequency_step_size

        Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).

                        When the :py:attr:`nirfsg.Session.lo_pll_fractional_mode_enabled` property is enabled, the specified step size affects the fractional spur performance of the device. When the :py:attr:`nirfsg.Session.lo_pll_fractional_mode_enabled` property is disabled, the specified step size affects the phase noise performance of the device.

                        The valid values for this property depend on the :py:attr:`nirfsg.Session.lo_pll_fractional_mode_enabled` property.

                        **PXIe-5644/5645/5646**—If you disable the :py:attr:`nirfsg.Session.lo_pll_fractional_mode_enabled` property, the specified value is coerced to the nearest valid value.

                        **PXIe-5840/5841**—If you disable the :py:attr:`nirfsg.Session.lo_pll_fractional_mode_enabled` property, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.

                        **Units:** hertz (Hz)

                        **Default Values:**

                        PXIe-5644/5645/5646: 200kHz

                        PXIe-5830: 2MHz

                        PXIe-5831/5832 (RF port): 8MHz

                        PXIe-5831/5832 (IF port): 2MHz, 4MHz

                        PXIe-5840/5841:

                        - Fractional mode: 500 kHz
                        - Integer mode: 10 MHz for frequencies less than or equal to 4 GHz. 20 MHz for frequencies greater than 4 GHz.

                        PXIe-5841 with PXIe-5655: 500kHz

                        PXIe-5842: 1Hz

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

        +----------------------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------+
        | :py:attr:`nirfsg.Session.lo_pll_fractional_mode_enabled` Property Setting                                                  | :py:data:`~nirfsg.NIRFSG_VAL_ENABLE` | :py:data:`~nirfsg.NIRFSG_VAL_DISABLE`            |
        +============================================================================================================================+======================================+==================================================+
        | :py:attr:`nirfsg.Session.lo_frequency_step_size` Property Valid Values on PXIe-5644/5645                                   | 50 kHz to 24 MHz                     | 4 MHz, 5 MHz, 6 MHz, 12 MHz, or 24 MHz           |
        +----------------------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------+
        | :py:attr:`nirfsg.Session.lo_frequency_step_size` Property Valid Values on PXIe-5646                                        | 50 kHz to 25 MHz                     | 2 MHz, 5 MHz, 10 MHz, or 25 MHz                  |
        +----------------------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------+
        | :py:attr:`nirfsg.Session.lo_frequency_step_size` Property Valid Values on PXIe-5840/5841                                   | 50 kHz to 100 MHz                    | 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, or 100 MHz |
        +----------------------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------+
        | :py:attr:`nirfsg.Session.lo_frequency_step_size` Property Valid Values on PXIe-5830/5831/ 5832 LO1                         | 8 Hz to 400 MHz                      | —                                                |
        +----------------------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------+
        | :py:attr:`nirfsg.Session.lo_frequency_step_size` Property Valid Values on PXIe-5830/5831/ 5832 LO2                         | 4 Hz to 400 MHz                      | —                                                |
        +----------------------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------+
        | :py:attr:`nirfsg.Session.lo_frequency_step_size` Property Valid Values on PXIe-5841 with PXIe-5655/NI PXIe-5842 (See note) | 1 nHz to 100 MHz                     | 1 nHz to 50 MHz                                  |
        +----------------------------------------------------------------------------------------------------------------------------+--------------------------------------+--------------------------------------------------+

        .. note:: Values up to 100 MHz are coerced to 50 MHz.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO Frequency Step Size (Hz)**
                - C Attribute: **NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE**

lo_in_power
-----------

    .. py:attribute:: lo_in_power

        Specifies the power level of the signal at the LO IN front panel connector.

                        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_real64` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

                        **Units**: dBm

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_



        .. note:: - This property is read/write if you are using an external LO. Otherwise, this property is read-only.

             - For the PXIe-5644/5645/5646, this property is always read-only.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:LO In Power (dBm)**
                - C Attribute: **NIRFSG_ATTR_LO_IN_POWER**

lo_out_enabled
--------------

    .. py:attribute:: lo_out_enabled

        Specifies whether the local oscillator signal is present at the LO OUT front panel connector. The local oscillator signal remains at the LO OUT front panel connector until this property is set to False, even if the :py:attr:`nirfsg.Session.output_enabled` property is set to False, the :py:meth:`nirfsg.Session.abort` method is called, or the NI-RFSG session is closed.

                        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_boolean` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

                        **Default Value:** :py:data:`~nirfsg.NIRFSG_VAL_DISABLE`

                        **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_

                    **Defined Values**:

        +---------------------------------------+---------------------------------------------------------------------------------+
        | Name                                  | Description                                                                     |
        +=======================================+=================================================================================+
        | :py:data:`~nirfsg.NIRFSG_VAL_ENABLE`  | The local oscillator signal is present at the LO OUT front panel connector.     |
        +---------------------------------------+---------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.NIRFSG_VAL_DISABLE` | The local oscillator signal is not present at the LO OUT front panel connector. |
        +---------------------------------------+---------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:LO Out Enabled**
                - C Attribute: **NIRFSG_ATTR_LO_OUT_ENABLED**

lo_out_export_configure_from_rfsa
---------------------------------

    .. py:attribute:: lo_out_export_configure_from_rfsa

        Specifies whether to allow NI-RFSA to control the NI-RFSG LO out export.

                        Set this property to :py:data:`~nirfsg.LoOutExportConfigureFromRFSaEnable.ENABLE` to allow NI-RFSA to control the LO out export. Use the RF OUT LO EXPORT ENABLED property to control the LO out export from NI-RFSA.

                        **Default Value:** :py:data:`~nirfsg.LoOutExportConfigureFromRFSaEnable.DISABLE`

                        **Supported Devices**: PXIe-5840/5841/5842

                    **Defined Values**:

        +---------------------------------------------------------------+---------+----------------------------------------------------------------------+
        | Name                                                          | Value   | Description                                                          |
        +===============================================================+=========+======================================================================+
        | :py:data:`~nirfsg.LoOutExportConfigureFromRFSaEnable.ENABLE`  | 0 (0x0) | Do not allow NI-RFSA to control the NI-RFSG local oscillator export. |
        +---------------------------------------------------------------+---------+----------------------------------------------------------------------+
        | :py:data:`~nirfsg.LoOutExportConfigureFromRFSaEnable.DISABLE` | 1 (0x1) | Allow NI-RFSA to control the NI-RFSG local oscillator export.        |
        +---------------------------------------------------------------+---------+----------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------------------+
            | Characteristic        | Value                                    |
            +=======================+==========================================+
            | Datatype              | enums.LoOutExportConfigureFromRFSaEnable |
            +-----------------------+------------------------------------------+
            | Permissions           | read-write                               |
            +-----------------------+------------------------------------------+
            | Repeated Capabilities | None                                     |
            +-----------------------+------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:LO Out Export Configure From RFSA**
                - C Attribute: **NIRFSG_ATTR_LO_OUT_EXPORT_CONFIGURE_FROM_RFSA**

lo_out_power
------------

    .. py:attribute:: lo_out_power

        Specifies the power level of the signal at the LO OUT front panel connector.

                        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_real64` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

                        **Units**: dBm

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `LO OUT <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/loout.html>`_



        .. note:: For the PXIe-5644/5645/5646 and PXIe-5673/5673E, this property is always read-only.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:LO Out Power (dBm)**
                - C Attribute: **NIRFSG_ATTR_LO_OUT_POWER**

lo_pll_fractional_mode_enabled
------------------------------

    .. py:attribute:: lo_pll_fractional_mode_enabled

        Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL). This property enables or disables fractional frequency tuning in the LO. Fractional mode provides a finer frequency step resolution and allows smaller values for the :py:attr:`nirfsg.Session.lo_frequency_step_size` property. However, fractional mode may introduce non-harmonic spurs.

                        This property applies only if you set the :py:attr:`nirfsg.Session.lo_source` property to :py:data:`~nirfsg.LoSource.ONBOARD`.

                        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_int32` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

                        **Default Value:** :py:data:`~nirfsg.LoPlLfractionalModeEnabled.ENABLE`

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        Refer to the local oscillators topic appropriate to your device for more information about using fractional mode.

                    **Defined Values**:

        +-------------------------------------------------------+---------+------------------------------------------+
        | Name                                                  | Value   | Description                              |
        +=======================================================+=========+==========================================+
        | :py:data:`~nirfsg.LoPlLfractionalModeEnabled.ENABLE`  | 0 (0x0) | Disables fractional mode for the LO PLL. |
        +-------------------------------------------------------+---------+------------------------------------------+
        | :py:data:`~nirfsg.LoPlLfractionalModeEnabled.DISABLE` | 1 (0x1) | Enables fractional mode for the LO PLL.  |
        +-------------------------------------------------------+---------+------------------------------------------+

        .. note:: For the PXIe-5841 with PXIe-5655, this property is ignored if the PXIe-5655 is used as the LO source.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.LoPlLfractionalModeEnabled |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | None                             |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO PLL Fractional Mode Enabled**
                - C Attribute: **NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED**

lo_source
---------

    .. py:attribute:: lo_source

        Specifies whether to use the internal or external local oscillator (LO) source. If the :py:attr:`nirfsg.Session.lo_source` property is set to "" (empty string), NI-RFSG uses the internal LO source. To set this property, the NI-RFSG device must be in the Configuration state.

                        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsg.Session._set_attribute_vi_string` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

                        **Default Value:** :py:data:`~nirfsg.LoSource.ONBOARD`

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `PXIe-5830 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/lo_sharing_using_rfsa_rfsg.html>`_

                        `PXIe-5831/5832 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/lo_sharing_using_rfsa_rfsg.html>`_

                    **Defined Values**:

        +----------------------------------------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                               | Value                  | Description                                                                                                                                                                                                                                                      |
        +====================================================+========================+==================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsg.LoSource.AUTOMATIC_SG_SA_SHARED` | Automatic_SG_SA_Shared | NI-RFSG internally makes the configuration to share the LO between NI-RFSA and NI-RFSG. This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841/5842.                                                                                                 |
        +----------------------------------------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.LoSource.LO_IN`                  | LO_In                  | Uses an external LO as the LO source. Connect a signal to the LO IN connector on the device and use the :py:attr:`nirfsg.Session.upconverter_center_frequency` property to specify the LO frequency.                                                             |
        +----------------------------------------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.LoSource.ONBOARD`                | Onboard                | Uses an internal LO as the LO source. If you specify an internal LO source, the LO is generated inside the device itself.                                                                                                                                        |
        +----------------------------------------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.LoSource.SG_SA_SHARED`           | SG_SA_Shared           | Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSG selects an internal synthesizer and the synthesizer signal is switched to both the RF In and RF Out mixers. This value is valid only on the PXIe-5830/5831/5832/5841 with PXIe-5655/5842. |
        +----------------------------------------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.LoSource.SECONDARY`              | Secondary              | Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid only on the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653.                                                                                                                     |
        +----------------------------------------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this property is set to :py:data:`~nirfsg.LoSource.SG_SA_SHARED`.

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.LoSource |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | None           |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO Source**
                - C Attribute: **NIRFSG_ATTR_LO_SOURCE**

lo_temperature
--------------

    .. py:attribute:: lo_temperature

        Returns the LO module temperature in degrees Celsius.

                        PXIe-5840/5841: If you query this property during RF list mode, list steps may take longer to complete during list execution.

                        **Units**: degrees Celsius (°C)

                        **Supported Devices:** PXIe-5673/5673E, PXIe-5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:LO Temperature (Degrees C)**
                - C Attribute: **NIRFSG_ATTR_LO_TEMPERATURE**

lo_vco_frequency_step_size
--------------------------

    .. py:attribute:: lo_vco_frequency_step_size

        Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal.

                        **Valid Values**:

                        LO1: 1 Hz to 50 MHz

                        LO2: 1 Hz to 100 MHz

                        **Default Value**: 1 MHz

                        **Supported Devices**: PXIe-5830/5831/5832

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO VCO Frequency Step Size (Hz)**
                - C Attribute: **NIRFSG_ATTR_LO_VCO_FREQUENCY_STEP_SIZE**

marker_event_output_behavior
----------------------------

    .. py:attribute:: marker_event_output_behavior

        Specifies the output behavior for the Marker Event. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.MarkerEventOutputBehavior.PULSE`

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

                    **Defined Values**:

        +-----------------------------------------------------+----------------+-------------------------------------------------------+
        | Name                                                | Value          | Description                                           |
        +=====================================================+================+=======================================================+
        | :py:data:`~nirfsg.MarkerEventOutputBehavior.PULSE`  | 23000 (0x59d8) | Specifies the Marker Event output behavior as pulse.  |
        +-----------------------------------------------------+----------------+-------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventOutputBehavior.TOGGLE` | 23001 (0x59d9) | Specifies the Marker Event output behavior as toggle. |
        +-----------------------------------------------------+----------------+-------------------------------------------------------+


        .. tip:: This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container markers to specify a subset.

            Example: :py:attr:`my_session.markers[ ... ].marker_event_output_behavior`

            To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.marker_event_output_behavior`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.MarkerEventOutputBehavior |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | markers                         |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Output Behavior**
                - C Attribute: **NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR**

marker_event_pulse_width
------------------------

    .. py:attribute:: marker_event_pulse_width

        Specifies the pulse width value for the Marker Event. Use the :py:attr:`nirfsg.Session.marker_event_pulse_width_units` property to set the units for the pulse width value. This property is valid only when the :py:attr:`nirfsg.Session.marker_event_output_behavior` property is set to :py:data:`~nirfsg.MarkerEventOutputBehavior.PULSE`.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** 200 ns

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_




        .. tip:: This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container markers to specify a subset.

            Example: :py:attr:`my_session.markers[ ... ].marker_event_pulse_width`

            To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.marker_event_pulse_width`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | markers    |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Pulse:Width Value**
                - C Attribute: **NIRFSG_ATTR_MARKER_EVENT_PULSE_WIDTH**

marker_event_pulse_width_units
------------------------------

    .. py:attribute:: marker_event_pulse_width_units

        Specifies the pulse width units for the Marker Event. This property is valid only when the :py:attr:`nirfsg.Session.marker_event_output_behavior` property is set to :py:data:`~nirfsg.MarkerEventOutputBehavior.PULSE`.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.MarkerEventPulseWidthUnits.SECONDS`

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

                    **Defined Values**:

        +-----------------------------------------------------+----------------+-------------------------------------------------------+
        | Name                                                | Value          | Description                                           |
        +=====================================================+================+=======================================================+
        | :py:data:`~nirfsg.MarkerEventOutputBehavior.PULSE`  | 23000 (0x59d8) | Specifies the Marker Event output behavior as pulse.  |
        +-----------------------------------------------------+----------------+-------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventOutputBehavior.TOGGLE` | 23001 (0x59d9) | Specifies the Marker Event output behavior as toggle. |
        +-----------------------------------------------------+----------------+-------------------------------------------------------+


        .. tip:: This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container markers to specify a subset.

            Example: :py:attr:`my_session.markers[ ... ].marker_event_pulse_width_units`

            To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.marker_event_pulse_width_units`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.MarkerEventPulseWidthUnits |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | markers                          |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Pulse:Width Units**
                - C Attribute: **NIRFSG_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS**

marker_event_terminal_name
--------------------------

    .. py:attribute:: marker_event_terminal_name

        Returns the name of the fully qualified signal name as a string.

                        **Default Values**:

                        PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/Marker *X* Event, where *AWGName* is the name of your associated AWG module in MAX and *X* is Marker Event 0 through 3.

                        PXIe-5830/5831/5832: /*BasebandModule*/ao/0/Marker *X* Event, where *BasebandModule* is the name of the baseband module of your device in MAX and *X* is Marker Event 0 through 3.

                        PXIe-5820/5840/5841: /*ModuleName*/ao/0/Marker *X* Event, where *ModuleName* is the name of your device in MAX and *X* is Marker Event 0 through 3.

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

                        `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.GetTerminalName`




        .. tip:: This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container markers to specify a subset.

            Example: :py:attr:`my_session.markers[ ... ].marker_event_terminal_name`

            To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.marker_event_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | markers   |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Terminal Name**
                - C Attribute: **NIRFSG_ATTR_MARKER_EVENT_TERMINAL_NAME**

marker_event_toggle_initial_state
---------------------------------

    .. py:attribute:: marker_event_toggle_initial_state

        Specifies the initial state for the Marker Event when the :py:attr:`nirfsg.Session.marker_event_output_behavior` property is set to :py:data:`~nirfsg.MarkerEventOutputBehavior.TOGGLE`.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.MarkerEventToggleInitialState.LOW`

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

                    **Defined Values**:

        +-------------------------------------------------------+----------------+----------------------------------------------------------------------------------+
        | Name                                                  | Value          | Description                                                                      |
        +=======================================================+================+==================================================================================+
        | :py:data:`~nirfsg.MarkerEventToggleInitialState.HIGH` | 21001 (0x5209) | Specifies the initial state of the Marker Event toggle behavior as digital high. |
        +-------------------------------------------------------+----------------+----------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.MarkerEventToggleInitialState.LOW`  | 21000 (0x5208) | Specifies the initial state of the Marker Event toggle behavior as digital low.  |
        +-------------------------------------------------------+----------------+----------------------------------------------------------------------------------+


        .. tip:: This property can be set/get on specific markers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container markers to specify a subset.

            Example: :py:attr:`my_session.markers[ ... ].marker_event_toggle_initial_state`

            To set/get on all markers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.marker_event_toggle_initial_state`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------+
            | Characteristic        | Value                               |
            +=======================+=====================================+
            | Datatype              | enums.MarkerEventToggleInitialState |
            +-----------------------+-------------------------------------+
            | Permissions           | read-write                          |
            +-----------------------+-------------------------------------+
            | Repeated Capabilities | markers                             |
            +-----------------------+-------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Toggle:Initial State**
                - C Attribute: **NIRFSG_ATTR_MARKER_EVENT_TOGGLE_INITIAL_STATE**

memory_size
-----------

    .. py:attribute:: memory_size

        The total amount of memory on the signal generator in bytes.

                        **Units:** bytes

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Memory Options <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/memory_options.html>`_

                        `Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_



        .. note:: Not all onboard memory is available for waveform storage. A portion of onboard memory stores scripts that specify how the waveforms are generated. These scripts typically require less than 1KB of onboard memory.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Memory Size**
                - C Attribute: **NIRFSG_ATTR_MEMORY_SIZE**

module_power_consumption
------------------------

    .. py:attribute:: module_power_consumption

        Returns the total power consumption of the device.

                        **Units:** watts

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860



        .. note:: If you query this property during RF list mode, list steps may take longer to complete during list execution.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Module Power Consumption (W)**
                - C Attribute: **NIRFSG_ATTR_MODULE_POWER_CONSUMPTION**

module_revision
---------------

    .. py:attribute:: module_revision

        Returns the module revision letter. If the NI-RFSG session is controlling multiple modules, this property returns the revision letter of the primary RF module. The NI-RFSG session is opened using the primary RF device name.

                        **Supported Devices:** PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Identifying Module Revision <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/identifying_device_revision.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Module Revision**
                - C Attribute: **NIRFSG_ATTR_MODULE_REVISION**

output_enabled
--------------

    .. py:attribute:: output_enabled

        Specifies whether signal output is enabled. Setting the :py:attr:`nirfsg.Session.output_enabled` property to False while in the Generation state stops signal output, although generation continues internally. For the PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653, PXI-5670/5671, and PXIe-5672/5673/5673E, setting the :py:attr:`nirfsg.Session.output_enabled` property while in the Committed state does not transition the device to the Configuration state, but output changes immediately.

                        **Default Value:** True

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Output Enabled <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/outputenable.html>`_

                        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_output_enabled`

                    **Defined Values**:

        +-------+-------------------------+
        | Value | Description             |
        +=======+=========================+
        | True  | Enables signal output.  |
        +-------+-------------------------+
        | False | Disables signal output. |
        +-------+-------------------------+

        .. note:: - For the PXIe-5653, this property controls only the LO1 terminal.

             - For the PXIe-5645, this property is ignored if you are using the I/Q ports.

             - When the :py:attr:`nirfsg.Session.ACTIVE_CONFIGURATION_LIST` property is set to a valid list name, setting the :py:attr:`nirfsg.Session.output_enabled` property transitions the device to the Configuration state.

        .. note:: One or more of the referenced properties are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Output Enabled**
                - C Attribute: **NIRFSG_ATTR_OUTPUT_ENABLED**

output_port
-----------

    .. py:attribute:: output_port

        Specifies the connector(s) to use to generate the signal. To set this property, the NI-RFSG device must be in the Configuration state.

                        You must write complex I and Q data for all options. The Q data has no effect if you set this property to I Only and set the :py:attr:`nirfsg.Session.iq_out_port_carrier_frequency` property to 0. If you set the :py:attr:`nirfsg.Session.iq_out_port_carrier_frequency` property to a value other than 0, the onboard signal processing (OSP) frequency shifts I and Q as a complex value and outputs the real portion of the result on the I connector(s) of the device.

                        If you set the :py:attr:`nirfsg.Session.output_port` property to :py:data:`~nirfsg.OutputPort.I_ONLY`\_ONLY or :py:data:`~nirfsg.OutputPort.IQ_OUT`, the :py:attr:`nirfsg.Session.iq_out_port_terminal_configuration` property applies.

                        **Default Value:**

                        PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860: :py:data:`~nirfsg.OutputPort.RF_OUT`

                        PXIe-5820: :py:data:`~nirfsg.OutputPort.IQ_OUT`

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +---------------------------------------+----------------+------------------------------------------------------------------------------------------+
        | Name                                  | Value          | Description                                                                              |
        +=======================================+================+==========================================================================================+
        | :py:data:`~nirfsg.OutputPort.CAL_OUT` | 14002 (0x36b2) | Enables the CAL OUT port.                                                                |
        +---------------------------------------+----------------+------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.OutputPort.I_ONLY`  | 14003 (0x36b3) | Enables the I connectors of the I/Q OUT port. This value is valid on only the PXIe-5645. |
        +---------------------------------------+----------------+------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.OutputPort.IQ_OUT`  | 14001 (0x36b1) | Enables the I/Q OUT port. This value is valid on only the PXIe-5645 and PXIe-5820.       |
        +---------------------------------------+----------------+------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.OutputPort.RF_OUT`  | 14000 (0x36b0) | Enables the RF OUT port. This value is not valid for the PXIe-5820.                      |
        +---------------------------------------+----------------+------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------------+
            | Characteristic        | Value            |
            +=======================+==================+
            | Datatype              | enums.OutputPort |
            +-----------------------+------------------+
            | Permissions           | read-write       |
            +-----------------------+------------------+
            | Repeated Capabilities | None             |
            +-----------------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:Output Port**
                - C Attribute: **NIRFSG_ATTR_OUTPUT_PORT**

overflow_error_reporting
------------------------

    .. py:attribute:: overflow_error_reporting

        Configures error reporting for onboard signal processing (OSP) overflows. Overflows lead to clipping of the waveform.

                        **Default Value:** :py:data:`~nirfsg.OverflowErrorReporting.WARNING`

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +----------------------------------------------------+--------------+----------------------------------------------------------------------------+
        | Name                                               | Value        | Description                                                                |
        +====================================================+==============+============================================================================+
        | :py:data:`~nirfsg.OverflowErrorReporting.DISABLED` | 1302 (0x516) | NI-RFSG does not return an error or a warning when an OSP overflow occurs. |
        +----------------------------------------------------+--------------+----------------------------------------------------------------------------+
        | :py:data:`~nirfsg.OverflowErrorReporting.WARNING`  | 1301 (0x515) | NI-RFSG returns a warning when an OSP overflow occurs.                     |
        +----------------------------------------------------+--------------+----------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------+
            | Characteristic        | Value                        |
            +=======================+==============================+
            | Datatype              | enums.OverflowErrorReporting |
            +-----------------------+------------------------------+
            | Permissions           | read-write                   |
            +-----------------------+------------------------------+
            | Repeated Capabilities | None                         |
            +-----------------------+------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Advanced:Overflow Error Reporting**
                - C Attribute: **NIRFSG_ATTR_OVERFLOW_ERROR_REPORTING**

p2p_data_transfer_permission_initial_credits
--------------------------------------------

    .. py:attribute:: p2p_data_transfer_permission_initial_credits

        Specifies the initial amount of data that the writer peer can transfer over the bus into the configured endpoint when the peer-to-peer data stream is enabled. If this property is not set and the endpoint is empty, credits equal to the full endpoint size are issued to the writer peer. If data is written to the endpoint using the :py:meth:`nirfsg.Session.WriteP2pEndpointI16` method prior to enabling the stream, credits equal to the remaining space available in the endpoint are issued to the writer peer. This property is coerced up by NI-RFSG to 8-byte boundaries. This property is endpoint-based.

                        **Units**: samples per channel

                        **Default Value:** 1,024

                        **Supported Devices:** PXIe-5673E

                        **Related Topics**

                        `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_

                        `Configuring Flow Control <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_flow_control.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Data Transfer Permission Initial Credits**
                - C Attribute: **NIRFSG_ATTR_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS**

p2p_data_transfer_permission_interval
-------------------------------------

    .. py:attribute:: p2p_data_transfer_permission_interval

        Specifies the interval at which the RF signal generator issues credits to allow the writer peer to transfer data over the bus into the configured endpoint. This property is coerced up by NI-RFSG to the nearest 128-byte boundary. This property is endpoint-based.

                        **Units**: samples per channel

                        **Supported Devices:** PXIe-5673E

                        **Related Topics**

                        `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_

                        `Configuring Flow Control <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_flow_control.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Data Transfer Permission Interval**
                - C Attribute: **NIRFSG_ATTR_P2P_DATA_TRANSFER_PERMISSION_INTERVAL**

p2p_enabled
-----------

    .. py:attribute:: p2p_enabled

        Specifies whether the RF signal generator reads data from the peer-to-peer endpoint. This property is endpoint-based.

                        **Default Value**: False

                        **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_

                    **Defined Values**:

        +-------+------------------------------------------+
        | Value | Description                              |
        +=======+==========================================+
        | True  | Peer-to-peer data streaming is enabled.  |
        +-------+------------------------------------------+
        | False | Peer-to-peer data streaming is disabled. |
        +-------+------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Enabled**
                - C Attribute: **NIRFSG_ATTR_P2P_ENABLED**

p2p_endpoint_count
------------------

    .. py:attribute:: p2p_endpoint_count

        Returns the number of peer-to-peer FIFO endpoints supported by the device.

                        **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Endpoint Count**
                - C Attribute: **NIRFSG_ATTR_P2P_ENDPOINT_COUNT**

p2p_endpoint_fullness_start_trigger_level
-----------------------------------------

    .. py:attribute:: p2p_endpoint_fullness_start_trigger_level

        Specifies the number of samples the endpoint must receive before the device starts generation. If no level is specified, NI-RFSG automatically sets this value to -1. This property applies only when the :py:attr:`nirfsg.Session.start_trigger_type` property is set to :py:data:`~nirfsg.StartTrigType.P2P_ENDPOINT_FULLNESS`

                        **Default Value:** -1, which allows NI-RFSG to select the appropriate fullness value.

                        **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_



        .. note:: Due to an additional internal FIFO in the RF signal generator, the writer peer actually needs to write 2,304 bytes more than the quantity of data specified by this property to satisfy the trigger level.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:P2P Endpoint Fullness:Level**
                - C Attribute: **NIRFSG_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL**

p2p_endpoint_size
-----------------

    .. py:attribute:: p2p_endpoint_size

        Returns the size, in samples, of the device endpoint. This property is endpoint-based.

                        **Units**: samples (s)

                        **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Endpoint Size**
                - C Attribute: **NIRFSG_ATTR_P2P_ENDPOINT_SIZE**

p2p_generation_fifo_sample_quantum
----------------------------------

    .. py:attribute:: p2p_generation_fifo_sample_quantum

        Returns how many samples NI-RFSG pulls from the peer-to-peer FIFO per read. You can use this property to determine how many samples to send across the peer-to-peer bus to ensure that no samples are ignored. If you send a number of samples that is not a multiple of this value, the remaining samples are not read from the FIFO during generation. This property is endpoint-based.

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Generation FIFO Sample Quantum**
                - C Attribute: **NIRFSG_ATTR_P2P_GENERATION_FIFO_SAMPLE_QUANTUM**

p2p_is_finite_generation
------------------------

    .. py:attribute:: p2p_is_finite_generation

        Specifies whether peer-to-peer should continuously generate data from the peer-to-peer stream or from only a finite number of samples, according to the :py:attr:`nirfsg.Session.p2p_number_of_samples_to_generate` property. To use this property, peer-to-peer must be enabled. This property is endpoint-based.

                        **Default Value**: False

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

                    **Defined Values**:

        +-------+--------------------------------------------------------------+
        | Value | Description                                                  |
        +=======+==============================================================+
        | True  | Data is generated from only a finite number of samples.      |
        +-------+--------------------------------------------------------------+
        | False | Data is continuously generated from the peer-to-peer stream. |
        +-------+--------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Is Finite Generation**
                - C Attribute: **NIRFSG_ATTR_P2P_IS_FINITE_GENERATION**

p2p_most_space_available_in_endpoint
------------------------------------

    .. py:attribute:: p2p_most_space_available_in_endpoint

        Returns the largest number of samples per channel available in the endpoint since this property was last read. You can use this property to determine how much endpoint space to use as a buffer against bus traffic latencies by reading the property and keeping track of the largest value returned. This property is endpoint-based.

                        If you want to minimize the latency for data to move through the endpoint and be generated by the RF signal generator, use the :py:attr:`nirfsg.Session.p2p_data_transfer_permission_initial_credits` property to grant fewer initial credits than the default of the entire endpoint size.

                        **Units**: samples per channel

                        **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Most Space Available in Endpoint**
                - C Attribute: **NIRFSG_ATTR_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT**

p2p_number_of_samples_to_generate
---------------------------------

    .. py:attribute:: p2p_number_of_samples_to_generate

        Specifies how many samples are generated from the peer-to-peer subsystem when it is enabled. To use this property, peer-to-peer must be enabled and set to finite generation. This property is endpoint-based.

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Number Of Samples To Generate**
                - C Attribute: **NIRFSG_ATTR_P2P_NUMBER_OF_SAMPLES_TO_GENERATE**

p2p_space_available_in_endpoint
-------------------------------

    .. py:attribute:: p2p_space_available_in_endpoint

        Returns the current space available in the endpoint. You can use this property when priming the endpoint with initial data using the :py:meth:`nirfsg.Session.WriteP2pEndpointI16` method to determine how many samples you can write. You also can use this property to characterize the performance and measure the latency of the peer-to-peer stream as data moves across the bus. This property is endpoint-based.

                        **Units**: samples per channel

                        **Supported Devices:** PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Configuring a Peer-to-Peer Endpoint <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_configuring_an_endpoint.html>`_

                        `Starting Peer-to-Peer Generation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/p2p_starting_generation.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Peer-to-Peer:Space Available In Endpoint**
                - C Attribute: **NIRFSG_ATTR_P2P_SPACE_AVAILABLE_IN_ENDPOINT**

peak_envelope_power
-------------------

    .. py:attribute:: peak_envelope_power

        Returns the maximum instantaneous power of the RF output signal.

                        **Units**: dBm

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860



        .. note:: - This property is valid only when the :py:attr:`nirfsg.Session.power_level_type` property is set to :py:data:`~nirfsg.PowerLevelType.AVERAGE`.

             - The :py:attr:`nirfsg.Session.arb_digital_gain` property is not included in the calculation of the :py:attr:`nirfsg.Session.peak_envelope_power` property.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Peak Envelope Power (dBm)**
                - C Attribute: **NIRFSG_ATTR_PEAK_ENVELOPE_POWER**

peak_power_adjustment
---------------------

    .. py:attribute:: peak_power_adjustment

        Specifies the adjustment for the :py:attr:`nirfsg.Session.power_level` property. This property is valid only when you set the :py:attr:`nirfsg.Session.power_level_type` property to :py:data:`~nirfsg.PowerLevelType.PEAK`. The value of the :py:attr:`nirfsg.Session.peak_power_adjustment` property adds to the :py:attr:`nirfsg.Session.power_level` property. The :py:attr:`nirfsg.Session.peak_power_adjustment` property typically specifies the peak-to-average power ratio (PAPR) of a waveform. If the PAPR is specified, the specified power level becomes the average power level of the waveform, even if the :py:attr:`nirfsg.Session.power_level_type` property is set to :py:data:`~nirfsg.PowerLevelType.PEAK`.

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate a peak power adjustment with a waveform.



        .. note:: - For the PXIe-5673/5673E only, use this property to associate a peak power adjustment with a waveform.

             - For the PXIe-5645, this property is ignored if you are using the I/Q ports.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Peak Power Adjustment (dB)**
                - C Attribute: **NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT**

peak_power_adjustment_inheritance
---------------------------------

    .. py:attribute:: peak_power_adjustment_inheritance

        Determines the inheritance behavior of the :py:attr:`nirfsg.Session.peak_power_adjustment` property when a script inherits values from specified waveforms.

                        **Default Value:** :py:data:`~nirfsg.PpaInheritance.EXACT_MATCH`

                        **Supported Devices:** PXIe-5673/5673E

                        **Related Topics**

                        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

                    **Defined Values**:

        +-----------------------------------------------+------------------------------------------------------------+
        | Value                                         | Description                                                |
        +===============================================+============================================================+
        | :py:data:`~nirfsg.PpaInheritance.EXACT_MATCH` | Errors out if different values are detected in the script. |
        +-----------------------------------------------+------------------------------------------------------------+
        | :py:data:`~nirfsg.PpaInheritance.MINIMUM`     | Uses the minimum value found in the script.                |
        +-----------------------------------------------+------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.PpaInheritance |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Peak Power Adjustment Inheritance**
                - C Attribute: **NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT_INHERITANCE**

phase_continuity_enabled
------------------------

    .. py:attribute:: phase_continuity_enabled

        Specifies whether the driver maintains phase continuity in the arbitrary waveforms. When this property is set to :py:data:`~nirfsg.PhaseContinuityEnabled.ENABLE`, NI-RFSG may increase the waveform size. When this property is set to :py:data:`~nirfsg.PhaseContinuityEnabled.ENABLE`, the :py:attr:`nirfsg.Session.frequency_tolerance` property specifies the maximum allowable frequency error that can be introduced when keeping the signal phase-continuous. To set the :py:attr:`nirfsg.Session.phase_continuity_enabled` property, the NI-RFSG device must be in the Configuration state. :py:attr:`nirfsg.Session.phase_continuity_enabled` applies only when the :py:attr:`nirfsg.Session.generation_mode` property is set to :py:data:`~nirfsg.GenerationMode.ARB_WAVEFORM` or :py:data:`~nirfsg.GenerationMode.SCRIPT`.

                        PXI-5671: When using the PXI-5671 with I/Q rates less than or equal to 8.33MS/s, an input phase-continuous signal is always phase-continuous upon output, and this property has no effect.

                        PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: Phase continuity is *always* enabled on this device.

                        **Default Value:** :py:data:`~nirfsg.PhaseContinuityEnabled.AUTO`

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Phase Continuity <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phasecontinuity.html>`_

                        `Arb Waveform Mode Tuning Speed Factors <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_arb_waveform_mode_tuning_speed_factors.html>`_

                    **Defined Values**:

        +---------------------------------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:attr:`nirfsg.Session.phase_continuity_enabled` Property Setting | Value     | With I/Q Rates > 8.33 MS/s.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
        +=====================================================================+===========+==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsg.PhaseContinuityEnabled.AUTO`                      | -1 (-0x1) | When the Generation Mode property is set to Arb Waveform, the arbitrary waveform may be repeated to ensure phase continuity after upconversion. This setting could cause waveform size to increase. When the Generation Mode property is set to Script, the Phase Continuity Enabled property indicates a warning condition. NI-RFSG cannot guarantee a phase-continuous output signal in Script mode. Phase continuity is automatically disabled in script mode, and the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. |
        +---------------------------------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.PhaseContinuityEnabled.DISABLE`                   | 0 (0x0)   | When the Generation Mode property is set to Arb Waveform, the arbitrary waveform is played back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained. When the Generation Mode property is set to Script, the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.                                                                                                              |
        +---------------------------------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.PhaseContinuityEnabled.ENABLE`                    | 1 (0x1)   | When the Generation Mode property is set to Arb Waveform, the arbitrary waveform may be repeated to ensure phase continuity after upconversion. Enabling this property could cause waveform size to increase. When the Generation Mode property is set to Script, the arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.                                                                                                                                           |
        +---------------------------------------------------------------------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------+
            | Characteristic        | Value                        |
            +=======================+==============================+
            | Datatype              | enums.PhaseContinuityEnabled |
            +-----------------------+------------------------------+
            | Permissions           | read-write                   |
            +-----------------------+------------------------------+
            | Repeated Capabilities | None                         |
            +-----------------------+------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Phase Continuity Enabled**
                - C Attribute: **NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED**

phase_offset
------------

    .. py:attribute:: phase_offset

        Specifies the phase of the RF output signal. Use this property to align the phase of the RF output with the phase of the RF output of another device, as long as the two devices are phase-coherent.

                        **Units**: degrees (°)

                        **Default Value:** 0

                        **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653, PXIe-5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Phase Synchronization and Phase Coherency <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phase_synchronization_and_phase_coherency.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Phase Offset (Degrees)**
                - C Attribute: **NIRFSG_ATTR_PHASE_OFFSET**

power_level
-----------

    .. py:attribute:: power_level

        Specifies either the average power level or peak power level of the generated RF signal, depending on the :py:attr:`nirfsg.Session.power_level_type` property setting.

                        The PXI-5670/5671, PXIe-5672, and PXIe-5860 must be in the Configuration state to use this property. However, the PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E and PXIe-5830/5831/5832/5840/5841/5842 can be in the Configuration or the Generation state to use this property.

                        Refer to the specifications document for your device for allowable power level settings.

                        **Units**: dBm

                        **Default Values:**

                        PXIe-5644/5645/5646, PXIe-5673/5673E: -100

                        PXI/PXIe-5650/5651/5652: -90

                        PXIe-5654: -7

                        PXIe-5654 with PXIe-5696: -110

                        PXI-5670/5671, PXIe-5672: -145

                        PXIe-5830/5831/5832/5840/5841/5842/5860: -174

                        **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860
                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.ConfigureRf`



        .. note:: - For the PXIe-5653, this property is read-only.

             - For the PXIe-5645, this property is ignored if you are using the I/Q ports.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Power Level (dBm)**
                - C Attribute: **NIRFSG_ATTR_POWER_LEVEL**

power_level_type
----------------

    .. py:attribute:: power_level_type

        Specifies how NI-RFSG interprets the value of the :py:attr:`nirfsg.Session.power_level` property. The :py:attr:`nirfsg.Session.power_level_type` property also affects how waveforms are scaled.

                        PXI-5670/5671: While in Script generation mode, if this property is set to :py:data:`~nirfsg.PowerLevelType.AVERAGE`, NI-RFSG scales each waveform so that all waveforms have the same average power. The average power level of each waveform matches the value set with the :py:attr:`nirfsg.Session.power_level` property. You can disable this scaling operation by setting the :py:attr:`nirfsg.Session.power_level_type` property to :py:data:`~nirfsg.PowerLevelType.PEAK`.

                        PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: While in Script generation mode, this property must be set to :py:data:`~nirfsg.PowerLevelType.PEAK`.

                        Converting from Average Power to Peak Power

                        Typically, this property is set to :py:data:`~nirfsg.PowerLevelType.AVERAGE`. However, some instrument modes require this property to be set to :py:data:`~nirfsg.PowerLevelType.PEAK`. Use the following equations to calculate the equivalent peak power given the desired average power for your waveform:


                        Where 1 is the highest possible magnitude in the waveform.



                        **Default Value:**

                        PXIe-5820: :py:data:`~nirfsg.PowerLevelType.PEAK`

                        All other devices: :py:data:`~nirfsg.PowerLevelType.AVERAGE`

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Spurious Performance <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/spurious_performance.html>`_

                        `Optimizing for Low Power Generation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/optimizing_for_low_power_generation.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_power_level_type`

                    **Defined Values**:

        +-------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Value                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
        +===========================================+===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsg.PowerLevelType.AVERAGE` | Indicates the desired power averaged in time. The driver maximizes the dynamic range by scaling the I/Q waveform so that its peak magnitude is equal to one. If your write more than one waveform, NI-RFSG scales each waveform without preserving the power level ratio between the waveforms. This value is not valid for the PXIe-5820.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
        +-------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.PowerLevelType.PEAK`    | Indicates the maximum power level of the RF signal averaged over one period of the RF carrier frequency (the peak envelope power). This setting requires that the magnitude of the I/Q waveform must always be less than or equal to one. When using peak power, the power level of the RF signal matches the specified power level at moments when the magnitude of the I/Q waveform equals one. If you write more than one waveform, the relative scaling between waveforms is preserved. In peak power mode, waveforms are scaled according to the :py:attr:`nirfsg.Session.arb_waveform_software_scaling_factor` property. You can use the :py:attr:`nirfsg.Session.peak_power_adjustment` property in conjunction with the :py:attr:`nirfsg.Session.power_level` property when the :py:attr:`nirfsg.Session.power_level_type` property is set to :py:data:`~nirfsg.PowerLevelType.PEAK`. |
        +-------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.PowerLevelType |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Power Level Type**
                - C Attribute: **NIRFSG_ATTR_POWER_LEVEL_TYPE**

pulse_modulation_active_level
-----------------------------

    .. py:attribute:: pulse_modulation_active_level

        Specifies the active level of the pulse modulation signal when pulse modulation is enabled. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.ScriptTrigDigLevelActiveLevel.HIGH`

                        **Supported Devices:**  PXIe-5842

                    **Defined Values**:

        +-------------------------------------------------------+---------------+--------------------------------------------------+
        | Name                                                  | Value         | Description                                      |
        +=======================================================+===============+==================================================+
        | :py:data:`~nirfsg.ScriptTrigDigLevelActiveLevel.HIGH` | 9000 (0x2328) | Trigger when the digital trigger signal is high. |
        +-------------------------------------------------------+---------------+--------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigDigLevelActiveLevel.LOW`  | 9001 (0x2329) | Trigger when the digital trigger signal is low.  |
        +-------------------------------------------------------+---------------+--------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------+
            | Characteristic        | Value                               |
            +=======================+=====================================+
            | Datatype              | enums.ScriptTrigDigLevelActiveLevel |
            +-----------------------+-------------------------------------+
            | Permissions           | read-write                          |
            +-----------------------+-------------------------------------+
            | Repeated Capabilities | None                                |
            +-----------------------+-------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Advanced:Pulse Modulation Active Level**
                - C Attribute: **NIRFSG_ATTR_PULSE_MODULATION_ACTIVE_LEVEL**

pulse_modulation_enabled
------------------------

    .. py:attribute:: pulse_modulation_enabled

        Enables or disables pulse modulation.

                        PXIe-5654/5654 with PXIe-5696: If this property is enabled and the signal at the PULSEIN front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled.

                        PXIe-5673/5673E: If this property is enabled and the signal at the PLSMOD front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled.

                        PXIe-5842: If this property is enabled and the signal at the PULSE IN front panel connector is high, the device generates a signal. If the signal is low, output generation is disabled. This behavior can be modified by setting pulse modulation active level.

                        **Default Value:** False

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E

                        **Related Topics**

                        `Pulse Modulation <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/pulse_modulation.html>`_

                    **Defined Values**:

        +-------+----------------------------+
        | Value | Description                |
        +=======+============================+
        | True  | Enables pulse modulation.  |
        +-------+----------------------------+
        | False | Disables pulse modulation. |
        +-------+----------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Pulse:Pulse Modulation Enabled**
                - C Attribute: **NIRFSG_ATTR_PULSE_MODULATION_ENABLED**

pulse_modulation_mode
---------------------

    .. py:attribute:: pulse_modulation_mode

        PXIe-5654/5654 with PXIe-5696: Specifies the pulse modulation mode to use.

                        PXIe-5842: This property allows you to choose a tradeoff between switching speed and On/Off Ratio when using pulse modulation. Refer to the product specifications document for the switching characteristics of each mode. This property is settable while the device is generating, but some output pulses may be dropped.

                        **Default Value:** :py:data:`~nirfsg.PulseModulationMode.ANALOG`

                        **Supported Devices:** PXIe-5842/5654/5654 with PXIe-5696

                    **Defined Values**:

        +----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
        | Value                                                                | Description                                                                                                                                 |
        +======================================================================+=============================================================================================================================================+
        | :py:data:`~nirfsg.PulseModulationMode.OPTIMAL_MATCH`                 | Provides for a more optimal power output match for the device during the off cycle of the pulse mode operation. Not supported on PXIe-5842. |
        +----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.NIRFSG_VAL_PULSE_MODULATION_ANALOG_HIGH_ISOLATION` | Allows for the best on/off power ratio of the pulsed signal.                                                                                |
        +----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.NIRFSG_VAL_PULSE_MODULATION_ANALOG`                | Analog switch blanking. Balance between switching speed and on/off power ratio of the pulsed signal.                                        |
        +----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.NIRFSG_VAL_PULSE_MODULATION_DIGITAL`               | Digital only modulation. Provides the best on/off switching speed of the pulsed signal at the cost of signal isolation.                     |
        +----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | enums.PulseModulationMode |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | None                      |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Advanced:Pulse Modulation Mode**
                - C Attribute: **NIRFSG_ATTR_PULSE_MODULATION_MODE**

pulse_modulation_source
-----------------------

    .. py:attribute:: pulse_modulation_source

        Specifies the source of the pulse modulation signal. When Pulse In in used, the pulse modulation is applied with the lowest latency and jitter, but is not aligned to any particular waveform sample. When a marker is used, the RF pulse is aligned to a specific sample in the arbitrary waveform. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.PulseModulationSource.PULSE_IN`

                        **Supported Devices:**  PXIe-5842

                    **Defined Values**:

        +---------------------------------------------------+---------+----------------------------------------------------------------------------------------------+
        | Name                                              | Value   | Description                                                                                  |
        +===================================================+=========+==============================================================================================+
        | :py:data:`~nirfsg.PulseModulationSource.PULSE_IN` | PulseIn | The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842. |
        +---------------------------------------------------+---------+----------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.PulseModulationSource.MARKER0`  |         | The trigger is received from the Marker 0.                                                   |
        +---------------------------------------------------+---------+----------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.PulseModulationSource.MARKER1`  |         | The trigger is received from the Marker 1.                                                   |
        +---------------------------------------------------+---------+----------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.PulseModulationSource.MARKER2`  |         | The trigger is received from the Marker 2.                                                   |
        +---------------------------------------------------+---------+----------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.PulseModulationSource.MARKER3`  |         | The trigger is received from the Marker 3.                                                   |
        +---------------------------------------------------+---------+----------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.PulseModulationSource |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Modulation:Pulse:Pulse Modulation Source**
                - C Attribute: **NIRFSG_ATTR_PULSE_MODULATION_SOURCE**

pxi_chassis_clk10_source
------------------------

    .. py:attribute:: pxi_chassis_clk10_source

        Specifies the clock source for driving the PXI 10 MHz backplane Reference Clock. This property is configurable if the PXI-5610 upconverter module is installed in *only* Slot 2 of a PXI chassis. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Defined Values**:

        Name (Value): Description

        :py:data:`~nirfsg.PxiChassisClk10Source.NONE` (0) :Do not drive the PXI_CLK10 signal.

        :py:data:`~nirfsg.PxiChassisClk10Source.ONBOARD_CLOCK_STR` (OnboardClock) :Uses the highly stable oven-controlled onboard Reference Clock to drive the PXI_CLK signal.

        :py:data:`~nirfsg.PxiChassisClk10Source.REF_IN_STR` (RefIn) :Uses the clock present at the front panel REF IN connector to drive the PXI_CLK signal.

                        **Default Value:** :py:data:`~nirfsg.PxiChassisClk10Source.NONE`

                        **Supported Devices:** PXI-5610, PXI-5670/5671

                        **Related Topics**

                        `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

                        `System Reference Clock <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/integration_pxi_clk10.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_pxi_chassis_clk10`


                        Only certain combinations of this property and the :py:attr:`nirfsg.Session.ref_clock_source` property are valid, as shown in the following table.

        +-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
        | :py:attr:`nirfsg.Session.pxi_chassis_clk10_source` Setting                                                | :py:attr:`nirfsg.Session.ref_clock_source` Setting         |
        +===========================================================================================================+============================================================+
        | :py:data:`~nirfsg.PxiChassisClk10Source.NONE`, :py:data:`~nirfsg.PxiChassisClk10Source.ONBOARD_CLOCK_STR` | :py:data:`~nirfsg.PxiChassisClk10Source.ONBOARD_CLOCK_STR` |
        +-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
        | :py:data:`~nirfsg.PxiChassisClk10Source.NONE`, :py:data:`~nirfsg.PxiChassisClk10Source.REF_IN_STR`        | :py:data:`~nirfsg.PxiChassisClk10Source.REF_IN_STR`        |
        +-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
        | :py:data:`~nirfsg.PxiChassisClk10Source.NONE`, :py:data:`~nirfsg.PxiChassisClk10Source.REF_IN_STR`        | :py:data:`~nirfsg.ReferenceClockSource.PXI_CLK`            |
        +-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.PxiChassisClk10Source |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clock:PXI Chassis Clk 10 Source**
                - C Attribute: **NIRFSG_ATTR_PXI_CHASSIS_CLK10_SOURCE**

query_instrument_status
-----------------------

    .. py:attribute:: query_instrument_status

        Specifies whether NI-RFSG queries the NI-RFSG device status after each operation. Querying the device status is useful for debugging. After you validate your program, set this property to False to disable status checking and maximize performance.

                        NI-RFSG can choose to ignore status checking for particular properties, regardless of the setting of this property. Use the :py:meth:`nirfsg.Session.__init__` method to override the default value.

                        **Default Value:** False

                        **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +-------+-------------------------------------------------------------+
        | Value | Description                                                 |
        +=======+=============================================================+
        | True  | NI-RFSG queries the instrument status after each operation. |
        +-------+-------------------------------------------------------------+
        | False | NI-RFSG does not query the instrument status.               |
        +-------+-------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Query Instrument Status**
                - C Attribute: **NIRFSG_ATTR_QUERY_INSTRUMENT_STATUS**

range_check
-----------

    .. py:attribute:: range_check

        Specifies whether to validate property values and method parameters. Range checking parameters is very useful for debugging. After you validate your program, set this property to False to disable range checking and maximize performance. NI-RFSG can choose to ignore range checking for particular properties, regardless of the setting of this property. Use the :py:meth:`nirfsg.Session.__init__` method to override the default value.

                        **Default Value:** True

                        **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +-------+-------------------------+
        | Value | Description             |
        +=======+=========================+
        | True  | Enable range checking.  |
        +-------+-------------------------+
        | False | Disable range checking. |
        +-------+-------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Range Check**
                - C Attribute: **NIRFSG_ATTR_RANGE_CHECK**

record_coercions
----------------

    .. py:attribute:: record_coercions

        Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties.

                        **Default Value:** False

                        **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +-------+---------------------------------------------------+
        | Value | Description                                       |
        +=======+===================================================+
        | True  | The IVI engine keeps a list of coercions.         |
        +-------+---------------------------------------------------+
        | False | The IVI engine does not keep a list of coercions. |
        +-------+---------------------------------------------------+

        .. note:: Enabling record value coercions is not supported.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Record Value Coercions**
                - C Attribute: **NIRFSG_ATTR_RECORD_COERCIONS**

ref_clock_rate
--------------

    .. py:attribute:: ref_clock_rate

        Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector. This property is only valid when the :py:attr:`nirfsg.Session.ref_clock_source` property is set to :py:data:`~nirfsg.NIRFSG_VAL_CLK_IN_STR`, :py:data:`~nirfsg.NIRFSG_VAL_REF_IN_STR`, or :py:data:`~nirfsg.ReferenceClockSource.REF_IN_2`

                        To set this property, the NI-RFSG device must be in the Configuration state. If you are using the PXIe-5654/5654 with PXIe-5696, the NI-RFSG device must be in the Committed state to read this property. When you read this property, it returns the frequency the device is locked to during the Committed state.

                        If you set this property to :py:data:`~nirfsg.ReferenceClockRate.AUTO`, NI-RFSG uses the default Reference Clock rate for the device or automatically detects the Reference Clock rate if automatic detection is supported by the device.

                        **Valid Values:**

                        PXIe-5654/5654 with PXIe-5696: Values between 1MHz to 20MHz in 1MHz steps are supported in addition to the :py:data:`~nirfsg.ReferenceClockRate.AUTO` and :py:data:`~nirfsg.ReferenceClockRate._10mhz` values.

                        PXIe-5841 with PXIe-5655, PXIe-5842: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz

                        y, where

                        y is 4, 8, 16, 24, 25, or 32.

                        PXIe-5860: 10 MHz, 100 MHz

                        **Units**: hertz (Hz)

                        **Default Value:** :py:data:`~nirfsg.ReferenceClockRate.AUTO`

                        **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_ref_clock`

                    **Defined Values**:

        +----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | Value                                        | Description                                                                                                                       |
        +==============================================+===================================================================================================================================+
        | :py:data:`~nirfsg.ReferenceClockRate.AUTO`   | Uses the default Reference Clock rate for the device or automatically detects the Reference Clock rate if the device supports it. |
        +----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ReferenceClockRate._10mhz` | Uses a 10 MHz Reference Clock rate.                                                                                               |
        +----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

        .. note:: Automatic detection of the Reference Clock rate is supported on only the PXIe-5654/5654 with PXIe-5696. For all other supported devices, NI-RFSG uses the default Reference Clock rate of 10MHz.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.ReferenceClockRate |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | None                     |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clock:Reference Clock Rate (Hz)**
                - C Attribute: **NIRFSG_ATTR_REF_CLOCK_RATE**

ref_clock_source
----------------

    .. py:attribute:: ref_clock_source

        Specifies the Reference Clock source. To set this property, the NI-RFSG device must be in the Configuration state. Only certain combinations of this property and the :py:attr:`nirfsg.Session.pxi_chassis_clk10_source` property are valid, as shown in the following table.

                        **Default Value:** :py:data:`~nirfsg.ReferenceClockSource.ONBOARD_CLOCK`

                        **Supported Devices:** PXI-5610, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_ref_clock`

                    **Defined Values**:

        +--------------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                   | Value         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
        +========================================================+===============+=========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsg.ReferenceClockSource.ONBOARD_CLOCK`  | OnboardClock  | Uses the onboard Reference Clock as the clock source. **PXIe-5830/5831** —For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. ** PXIe-5831/5832 with PXIe-5653** —Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. **PXIe-5841 with PXIe-5655** —Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector.                                                                                                                                                                                                                                                                                                      |
        +--------------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ReferenceClockSource.CLK_IN`         | ClkIn         | Uses the clock signal present at the front panel CLK IN connector as the Reference Clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
        +--------------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ReferenceClockSource.REF_IN`         | RefIn         | Uses the clock signal present at the front panel REF IN connector as the Reference Clock source. **PXIe-5830/5831** —For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831/5832, lock the external signal to the PXIe-3622 REF IN connector. **PXIe-5831/5832 with PXIe-5653** —Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. **PXIe-5841 with PXIe-5655** —Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. |
        +--------------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ReferenceClockSource.PXI_CLK`        | PXI_CLK       | Uses the PXI_CLK signal, which is present on the PXI backplane, as the Reference Clock source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
        +--------------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ReferenceClockSource.REF_IN_2`       | RefIn2        | This value is not valid on any supported devices.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
        +--------------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ReferenceClockSource.PXI_CLK_MASTER` | PXI_ClkMaster | This value is valid on only the PXIe-5831/5832 with PXIe-5653. **PXIe-5831/5832 with PXIe-5653** —NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use :py:data:`~nirfsg.ReferenceClockSource.PXI_CLK` as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
        +--------------------------------------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: The PXI-5670/5671 and PXIe-5672 devices also allow you to drive the PXI 10 MHz backplane clock on PXI chassis *only* using the :py:attr:`nirfsg.Session.pxi_chassis_clk10_source` property.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ReferenceClockSource |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clock:Reference Clock Source**
                - C Attribute: **NIRFSG_ATTR_REF_CLOCK_SOURCE**

ref_pll_bandwidth
-----------------

    .. py:attribute:: ref_pll_bandwidth

        Configures the loop bandwidth of the reference PLL.

                        **Default Value:** :py:data:`~nirfsg.LoopBandwidth.NARROW`

                        **Supported Devices:** PXIe-5653

                        **Related Topics**

                        `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_

                    **Defined Values**:

        +-----------------------------------------+--------------------------------------------------------+
        | Value                                   | Description                                            |
        +=========================================+========================================================+
        | :py:data:`~nirfsg.LoopBandwidth.NARROW` | Uses the narrowest loop bandwidth setting for the PLL. |
        +-----------------------------------------+--------------------------------------------------------+
        | :py:data:`~nirfsg.LoopBandwidth.MEDIUM` | Uses the medium loop bandwidth setting for the PLL.    |
        +-----------------------------------------+--------------------------------------------------------+
        | :py:data:`~nirfsg.LoopBandwidth.WIDE`   | Uses the widest loop bandwidth setting for the PLL.    |
        +-----------------------------------------+--------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.LoopBandwidth |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | None                |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Advanced:Ref PLL Bandwidth**
                - C Attribute: **NIRFSG_ATTR_REF_PLL_BANDWIDTH**

relative_delay
--------------

    .. py:attribute:: relative_delay

        Specifies the delay, in seconds, to apply to the I/Q waveform.

                        Relative delay allows for delaying the generated signal from one device relative to the generated signal of another device after those devices have been synchronized. You can achieve a negative relative delay by delaying both synchronized devices by the same value (1 μs) before generation begins and then changing the relative delay to a smaller amount than the initial value on only one of the devices.

        To set this property, the NI-RFSG device must be in the Configuration or Generation state.

                        **Units:** Seconds

                        **Valid Values:**

                        PXIe-PXIe-5820/5830/5831/5832/5840/5841: 0 μs to 3.2 μs

                        PXIe-5842: 0 μs to 6.5 μs

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `NI-TClk Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_tclk_help.html>`_



        .. note:: - To obtain a negative relative delay when synchronizing the PXIe-5840/5841 with a module that does not support this property, use the NITCLK_ATTR_SAMPLE_CLOCK_DELAY property.

             - The resolution of this property is a method of the I/Q sample period at 15E(-6) of the sample period but not worse than one Sample Clock period.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:Relative Delay**
                - C Attribute: **NIRFSG_ATTR_RELATIVE_DELAY**

rf_blanking_source
------------------

    .. py:attribute:: rf_blanking_source

        Specifies the Marker Event at which RF blanking occurs. RF blanking quickly attenuates the RF OUT signal. Use Marker Events to toggle the state of RF blanking. The RF Output always starts in the unblanked state.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        You can specify Marker Events by using scripts to trigger blanking at a certain point in a waveform. For example, if you set this property to marker0 str}, and marker0 occurs on samples 1,000 and 2,000 of a script, then the RF Output will be blanked (attenuated) between samples 1,000 and 2,000.

                        PXIe-5645: This property is ignored if you are using the I/Q ports.

                        PXIe-5840/5841: RF blanking does not occur for frequencies below 120MHz.

                        For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any :py:meth:`nirfsg.Session.reset` or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking properties. Alternatively, you can call :py:meth:`nirfsg.Session.ResetWithOptions` or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.

                        **Default Value:** "" (empty string)

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

                    **Valid Values**:

        +-------------------+---------------------------------+
        | Value             | Description                     |
        +===================+=================================+
        | "" (empty string) | RF blanking is disabled.        |
        +-------------------+---------------------------------+
        | Marker0           | RF blanking is tied to marker0. |
        +-------------------+---------------------------------+
        | Marker1           | RF blanking is tied to marker1. |
        +-------------------+---------------------------------+
        | Marker2           | RF blanking is tied to marker2. |
        +-------------------+---------------------------------+
        | Marker3           | RF blanking is tied to marker3. |
        +-------------------+---------------------------------+

        .. note:: The shortest supported blanking interval is eight microseconds.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:RF Blanking Source**
                - C Attribute: **NIRFSG_ATTR_RF_BLANKING_SOURCE**

rf_in_lo_export_enabled
-----------------------

    .. py:attribute:: rf_in_lo_export_enabled

        Specifies whether to enable the RF IN LO OUT terminal on the PXIe-5840/5841.

                        Set this property to :py:data:`~nirfsg.RFInLoExportEnabled.ENABLE` to export the LO signal from the RF IN LO OUT terminal.

                        When this property is enabled, if the :py:attr:`nirfsg.Session.lo_source` property is set to :py:data:`~nirfsg.LoSource.LO_IN` and you do not set the :py:attr:`nirfsg.Session.lo_frequency` or :py:attr:`nirfsg.Session.upconverter_center_frequency` properties, NI-RFSG rounds the LO frequency to approximately an LO step size as if the source was :py:data:`~nirfsg.NIRFSG_VAL_ONBOARD_CLOCK_STR`. This ensures that when you configure NI-RFSA and NI-RFSG with compatible settings that result in the same LO frequency, the rounding also is compatible.

                        **Default Value:** :py:data:`~nirfsg.RFInLoExportEnabled.UNSPECIFIED`

                        **Supported Devices**: PXIe-5840/5841/5842

                    **Defined Values**:

        +----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | Value                                              | Description                                                                                                                             |
        +====================================================+=========================================================================================================================================+
        | :py:data:`~nirfsg.RFInLoExportEnabled.DISABLE`     | The RF In local oscillator signal is not present at the front panel LO OUT connector.                                                   |
        +----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.RFInLoExportEnabled.ENABLE`      | The RF In local oscillator signal is present at the front panel LO OUT connector.                                                       |
        +----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.RFInLoExportEnabled.UNSPECIFIED` | The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it. |
        +----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | enums.RFInLoExportEnabled |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | None                      |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:RF In LO Export Enabled**
                - C Attribute: **NIRFSG_ATTR_RF_IN_LO_EXPORT_ENABLED**

script_trigger_terminal_name
----------------------------

    .. py:attribute:: script_trigger_terminal_name

        Returns the name of the fully qualified signal name as a string.

                        **Default Values**:

                        PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/ScriptTrigger *X*, where *AWGName* is the name of your associated AWG module in MAX and *X* is Script Trigger 0 through 3.

                        PXIe-5830/5831/5832: /*BasebandModule*/ao/0/ScriptTrigger *X*, where *BasebandModule* is the name of the baseband module of your device in MAX and *X* is Script Trigger 0 through 3.

                        PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/ScriptTrigger *X*, where *ModuleName* is the name of your device in MAX and *X* is Script Trigger 0 through 3.

                        PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/ScriptTrigger *X*, where *ModuleName* is the name of your device in MAX, *ChannelNumber* is the channel number (0 or 1), and *X* is Script Trigger 0 through 3.

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

                        `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.GetTerminalName`




        .. tip:: This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

            Example: :py:attr:`my_session.script_triggers[ ... ].script_trigger_terminal_name`

            To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.script_trigger_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------+
            | Characteristic        | Value           |
            +=======================+=================+
            | Datatype              | str             |
            +-----------------------+-----------------+
            | Permissions           | read only       |
            +-----------------------+-----------------+
            | Repeated Capabilities | script_triggers |
            +-----------------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Terminal Name**
                - C Attribute: **NIRFSG_ATTR_SCRIPT_TRIGGER_TERMINAL_NAME**

script_trigger_type
-------------------

    .. py:attribute:: script_trigger_type

        Specifies the Script Trigger type. Depending upon the value of this property, more properties may be needed to fully configure the trigger. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.ScriptTrigType.NONE`

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

                        `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_digital_edge_script_trigger`

                    **Defined Values**:

        +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Value                                           | Description                                                                                                                                                                                                                                                                                                               |
        +=================================================+===========================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsg.ScriptTrigType.NONE`          | No trigger is configured. Signal generation starts immediately.                                                                                                                                                                                                                                                           |
        +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigType.DIGITAL_EDGE`  | The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the :py:attr:`nirfsg.Session.digital_edge_start_trigger_source` property, and the active edge is specified with the :py:attr:`nirfsg.Session.digital_edge_start_trigger_edge` property.              |
        +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigType.DIGITAL_LEVEL` | The data operation does not start until the digital level is detected. The source of the digital level is specified in the :py:attr:`nirfsg.Session.digital_level_script_trigger_source` property, and the active level is specified in the :py:attr:`nirfsg.Session.digital_level_script_trigger_active_level` property. |
        +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.ScriptTrigType.SOFTWARE`      | The data operation does not start until a software trigger occurs. You can create a software event by calling the :py:meth:`nirfsg.Session.send_software_edge_trigger` method.                                                                                                                                            |
        +-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific script_triggers within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

            Example: :py:attr:`my_session.script_triggers[ ... ].script_trigger_type`

            To set/get on all script_triggers, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.script_trigger_type`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.ScriptTrigType |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | script_triggers      |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Type**
                - C Attribute: **NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE**

selected_path
-------------

    .. py:attribute:: selected_path

        Specifies which path to configure to generate a signal.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Selected Path**
                - C Attribute: **NIRFSG_ATTR_SELECTED_PATH**

selected_ports
--------------

    .. py:attribute:: selected_ports

        Specifies the port to configure.

                        **Valid Values**:

                        PXIe-5644/5645/5646, PXIe-5820/5840/5841: "" (empty string)

                        PXIe-5830: if0, if1

                        PXIe-5831/5832: if0, if1, rf*0-1*/port*x*, where *0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and *x* is the port number on the mmRH-5582 front panel.

                        **Default Value:**

                        PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: "" (empty string)

                        PXIe-5830/5831/5832: if0

                        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        :py:attr:`nirfsg.Session.available_ports`



        .. note:: When using RF list mode, ports cannot be shared with NI-RFSA.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:Selected Ports**
                - C Attribute: **NIRFSG_ATTR_SELECTED_PORTS**

selected_script
---------------

    .. py:attribute:: selected_script

        Specifies the script in onboard memory to generate upon calling the :py:meth:`nirfsg.Session._initiate` method when the :py:attr:`nirfsg.Session.generation_mode` property is set to :py:data:`~nirfsg.GenerationMode.SCRIPT`.

                        The :py:attr:`nirfsg.Session.selected_script` property is ignored when the :py:attr:`nirfsg.Session.generation_mode` property is set to :py:data:`~nirfsg.GenerationMode.ARB_WAVEFORM` or :py:data:`~nirfsg.GenerationMode.CW`. To set the :py:attr:`nirfsg.Session.selected_script` property, the NI-RFSG device must be in the Configuration state.

                        **Supported Devices:** PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

                        `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Selected Script**
                - C Attribute: **NIRFSG_ATTR_SELECTED_SCRIPT**

self_calibration_temperature
----------------------------

    .. py:attribute:: self_calibration_temperature

        Indicates, in degrees Celsius, the temperature of the device at the time of the last self calibration.

                        **Supported Devices:** PXIe-5644/5645/5646

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Self Calibration:Last Self Calibration Temperature**
                - C Attribute: **NIRFSG_ATTR_SELF_CALIBRATION_TEMPERATURE**

serial_number
-------------

    .. py:attribute:: serial_number

        Returns the serial number of the RF module. If the NI-RFSG session is controlling multiple modules, this property returns the serial number of the primary RF module.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Serial Number**
                - C Attribute: **NIRFSG_ATTR_SERIAL_NUMBER**

signal_bandwidth
----------------

    .. py:attribute:: signal_bandwidth

        Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8× :py:attr:`nirfsg.Session.iq_rate`).

                        NI-RFSG defines *signal bandwidth* as twice the maximum baseband signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the signal bandwidth is simply the baseband signal's minimum frequency subtracted from its maximum frequency, or *f*\ :sub:`max`\ - *f*\ :sub:`min`\ .

                        This property applies only when the :py:attr:`nirfsg.Session.generation_mode` property is set to :py:data:`~nirfsg.GenerationMode.ARB_WAVEFORM` or :py:data:`~nirfsg.GenerationMode.SCRIPT`, except for when using the PXIe-5830/5831/5832/5840/5841, which supports setting this property in all supported generation modes. To set the :py:attr:`nirfsg.Session.signal_bandwidth` property, the NI-RFSG device must be in the Configuration state.

                        PXI-5670/5671, PXIe-5672: Based on your signal bandwidth, NI-RFSG determines whether to configure the upconverter center frequency in increments of 1MHz or 5MHz. Failure to configure this property may result in the signal being placed outside the upconverter passband.

                        PXIe-5644/5645/5646, PXIe-5673/5673E: This property is used only for error-checking purposes. Otherwise, this property is ignored.

                        PXIe-5820/5830/5831/5832/5840/5841/5842/5860: Based on your signal bandwidth, NI-RFSG decides the equalized bandwidth. If this property is not set, NI-RFSG uses the maximum available signal bandwidth. For the PXIe-5840/5841, the maximum allowed signal bandwidth depends on the upconverter center frequency. Refer to the specifications document for your device for more information about signal bandwidth. The device specifications depend on the signal bandwidth.

                        **Units**: hertz (Hz)

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Phase-Locked Loop Bandwidth <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/phased_lock_loop_bandwidth.html>`_

                        `Frequency Tuning Times <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_tuning_times.html>`_

                        `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

                        `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

                        `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Signal Bandwidth (Hz)**
                - C Attribute: **NIRFSG_ATTR_SIGNAL_BANDWIDTH**

simulate
--------

    .. py:attribute:: simulate

        Returns whether NI-RFSG simulates I/O operations. This property is useful for debugging applications without using hardware. After a session is opened, you cannot change the simulation state. Use the :py:meth:`nirfsg.Session.__init__` method to enable simulation.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +-------+-------------------------+
        | Value | Description             |
        +=======+=========================+
        | True  | Simulation is enabled.  |
        +-------+-------------------------+
        | False | Simulation is disabled. |
        +-------+-------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NIRFSG_ATTR_SIMULATE**

specific_driver_class_spec_major_version
----------------------------------------

    .. py:attribute:: specific_driver_class_spec_major_version

        Returns the major version number of the class specification with which NI-RFSG is compliant.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Class Specification Major Version**
                - C Attribute: **NIRFSG_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION**

specific_driver_class_spec_minor_version
----------------------------------------

    .. py:attribute:: specific_driver_class_spec_minor_version

        Returns the minor version number of the class specification with which NI-RFSG is compliant.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Class Specification Minor Version**
                - C Attribute: **NIRFSG_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        Returns a string that contains a brief description of NI-RFSG. This property returns

                        National Instruments RF Signal Generator Instrument Driver.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Description**
                - C Attribute: **NIRFSG_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_prefix
----------------------

    .. py:attribute:: specific_driver_prefix

        Returns a string that contains the prefix for NI-RFSG. The name of each user-callable method in NI-RFSG starts with this prefix. This property returns

                        niRFSG.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Prefix**
                - C Attribute: **NIRFSG_ATTR_SPECIFIC_DRIVER_PREFIX**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        Returns a string that contains additional version information about NI-RFSG. For example, NI-RFSG can return

                        Driver: NI-RFSG14.5.0, Compiler: MSVC9.00, Components: IVI Engine4.00, VISA-Spec4.00 as the value of this property.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Revision**
                - C Attribute: **NIRFSG_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        Returns a string that contains the name of the vendor that supplies NI-RFSG. This property returns

                        National Instruments.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Vendor**
                - C Attribute: **NIRFSG_ATTR_SPECIFIC_DRIVER_VENDOR**

started_event_terminal_name
---------------------------

    .. py:attribute:: started_event_terminal_name

        Returns the name of the fully qualified signal name as a string.

                        **Default Values**:

                        PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/StartedEvent, where *AWGName* is the name of your associated AWG module in MAX.

                        PXIe-5830/5831/5832: /*BasebandModule*/ao/0/StartedEvent, where *BasebandModule* is the name of the baseband module of your device in MAX.

                        PXIe-5820/5840/5841: /*ModuleName*/ao/0/StartedEvent, where *ModuleName* is the name of your device in MAX.

                        PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/StartedEvent, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

                        **Supported Devices:** PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

                        `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.GetTerminalName`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Started Event Terminal Name**
                - C Attribute: **NIRFSG_ATTR_STARTED_EVENT_TERMINAL_NAME**

start_trigger_terminal_name
---------------------------

    .. py:attribute:: start_trigger_terminal_name

        Returns the name of the fully qualified signal name as a string.

                        **Default Values**:

                        PXIe-5654/5654 with PXIe-5696: /*ModuleName*/StartTrigger, where *ModuleName* is the name of your device in MAX.

                        PXI-5670/5671, PXIe-5672/5673/5673E: /*AWGName*/StartTrigger, where *ModuleName* is the name of your associated AWG module in MAX.

                        PXIe-5830/5831/5832: /*BasebandModule*/ao/0/StartTrigger, where *BasebandModule* is the name of the baseband module of your device in MAX.

                        PXIe-5820/5840/5841/5842: /*ModuleName*/ao/0/StartTrigger, where *ModuleName* is the name of your device in MAX.

                        PXIe-5860: /*ModuleName*/ao/*ChannelNumber*/StartTrigger, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

                        **Supported Devices:** PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

                        `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.GetTerminalName`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Terminal Name**
                - C Attribute: **NIRFSG_ATTR_START_TRIGGER_TERMINAL_NAME**

start_trigger_type
------------------

    .. py:attribute:: start_trigger_type

        Specifies the Start Trigger type. Depending upon the value of this property, more properties may be needed to fully configure the trigger. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** :py:data:`~nirfsg.StartTrigType.NONE`

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

                        `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_

                        **High-Level Methods**:

                        - :py:meth:`nirfsg.Session.configure_digital_edge_start_trigger`
                        - :py:meth:`nirfsg.Session.configure_software_start_trigger`
                        - :py:meth:`nirfsg.Session.disable_start_trigger`

                    **Defined Values**:

        +--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Value                                                  | Description                                                                                                                                                                                                                                                                                                |
        +========================================================+============================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsg.StartTrigType.NONE`                  | No trigger is configured.                                                                                                                                                                                                                                                                                  |
        +--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigType.DIGITAL_EDGE`          | The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the :py:attr:`nirfsg.Session.digital_edge_start_trigger_source` property, and the active edge is specified in the :py:attr:`nirfsg.Session.digital_edge_start_trigger_edge` property. |
        +--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigType.SOFTWARE`              | The data operation does not start until a software event occurs. You may create a software trigger by calling the :py:meth:`nirfsg.Session.send_software_edge_trigger` method.                                                                                                                             |
        +--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.StartTrigType.P2P_ENDPOINT_FULLNESS` | The data operation does not start until the endpoint reaches the threshold specified in the :py:attr:`nirfsg.Session.p2p_endpoint_fullness_start_trigger_level` property.                                                                                                                                  |
        +--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.StartTrigType |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | None                |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Type**
                - C Attribute: **NIRFSG_ATTR_START_TRIGGER_TYPE**

streaming_enabled
-----------------

    .. py:attribute:: streaming_enabled

        Enables and disables continuous streaming of waveform data.

                        **Default Value:** False

                        **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

                    **Defined Values**:

        +-------+------------------------+
        | Value | Description            |
        +=======+========================+
        | True  | Streaming is enabled.  |
        +-------+------------------------+
        | False | Streaming is disabled. |
        +-------+------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Data Transfer:Streaming:Streaming Enabled**
                - C Attribute: **NIRFSG_ATTR_STREAMING_ENABLED**

streaming_space_available_in_waveform
-------------------------------------

    .. py:attribute:: streaming_space_available_in_waveform

        Indicates the space available, in samples, in the streaming waveform for writing new data. For optimal performance, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform. This waveform size ensures that writes do not have to wrap around from the end to the beginning of the waveform buffer.

                        To read this property, the NI-RFSG device must be in the Committed state.

                        **Units**: samples

                        **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Data Transfer:Streaming:Space Available In Streaming Waveform (Samples)**
                - C Attribute: **NIRFSG_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM**

streaming_waveform_name
-----------------------

    .. py:attribute:: streaming_waveform_name

        Specifies the name of the waveform used to continually stream data during generation.

                        **Default Value:** "" (empty string)

                        **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

                        `Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Data Transfer:Streaming:Streaming Waveform Name**
                - C Attribute: **NIRFSG_ATTR_STREAMING_WAVEFORM_NAME**

streaming_write_timeout
-----------------------

    .. py:attribute:: streaming_write_timeout

        Indicates the maximum amount of time allowed to complete a streaming write operation.

                        **Default Value:** 10.0seconds

                        **Supported Devices:** PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

                        `Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Data Transfer:Streaming:Streaming Write Timeout**
                - C Attribute: **NIRFSG_ATTR_STREAMING_WRITE_TIMEOUT**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        Returns a string that contains a model code of the NI-RFSG device. For drivers that support more than one device, this property contains a comma-separated list of supported devices.

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NIRFSG_ATTR_SUPPORTED_INSTRUMENT_MODELS**

sync_sample_clock_dist_line
---------------------------

    .. py:attribute:: sync_sample_clock_dist_line

        Specifies which external trigger line distributes the Sample Clock sync signal. When synchronizing the Sample Clock between multiple devices, configure all devices to use the same Sample Clock sync distribution line.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

                        **Default Value:** "" (empty string)

                        **Supported Devices:** PXIe-5646

                        **Related Topics**

                        `Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/synchronization_rfsa_g.html>`_—Refer to this topic for more information about PXIe-5646 device synchronization.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Sync Sample Clock Dist Line**
                - C Attribute: **NIRFSG_ATTR_SYNC_SAMPLE_CLOCK_DIST_LINE**

sync_sample_clock_master
------------------------

    .. py:attribute:: sync_sample_clock_master

        Specifies whether the device is the master device when synchronizing the Sample Clock between multiple devices. The master device distributes the Sample Clock sync signal to all devices in the system through the Sample Clock sync distribution line.

                        When synchronizing the Sample Clock, one device must always be designated as the master. The master device actively drives the Sample Clock sync distribution line.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** False

                        **Supported Devices:** PXIe-5646

                        **Related Topics**

                        `Synchronization Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/synchronization_rfsa_g.html>`_—Refer to this topic for more information about PXIe-5646 device synchronization.

                    **Defined Values**:

        +-------+---------------------------------------------------------------------+
        | Value | Description                                                         |
        +=======+=====================================================================+
        | True  | The device is the master device for synchronizing the Sample Clock. |
        +-------+---------------------------------------------------------------------+
        | False | The device is not the master for synchronizing the Sample Clock.    |
        +-------+---------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Sync Sample Clock Master**
                - C Attribute: **NIRFSG_ATTR_SYNC_SAMPLE_CLOCK_MASTER**

sync_script_trigger_dist_line
-----------------------------

    .. py:attribute:: sync_script_trigger_dist_line

        Specifies which external trigger line distributes the synchronized Script Trigger signal. When synchronizing the Script Trigger, configure all devices to use the same Script Trigger distribution line.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

                        **Default Value:** "" (empty string)

                        **Supported Devices:** PXIe-5644/5645/5646

                        **Related Topics**

                        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

                        `Synchronizing Sample Clock and Sampled Reference Clock Signals <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sample_clock_sync.html>`_

                        Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Dist Line**
                - C Attribute: **NIRFSG_ATTR_SYNC_SCRIPT_TRIGGER_DIST_LINE**

sync_script_trigger_master
--------------------------

    .. py:attribute:: sync_script_trigger_master

        Specifies whether the device is the master device when synchronizing the Script Trigger.

                        The master device distributes the synchronized Script Trigger to all devices in the system through the Script Trigger distribution line.

                        When synchronizing the Script trigger, one device must always be designated as the master. The master device actively drives the Script Trigger distribution line. For slave devices, set the :py:attr:`nirfsg.Session.script_trigger_type` property to digital edge, and set the :py:attr:`nirfsg.Session.digital_edge_script_trigger_source` property to sync_script.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** False

                        **Supported Devices:** PXIe-5644/5645/5646

                        **Related Topics**

                        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

                        `Synchronizing Sample Clock and Sampled Reference Clock Signals <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/sample_clock_sync.html>`_

                        Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.

                    **Defined Values**:

        +-------+-----------------------------------------------------------------------+
        | Value | Description                                                           |
        +=======+=======================================================================+
        | True  | The device is the master device for synchronizing the Script Trigger. |
        +-------+-----------------------------------------------------------------------+
        | False | The device is not the master for synchronizing the Script Trigger.    |
        +-------+-----------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Sync Script Trigger Master**
                - C Attribute: **NIRFSG_ATTR_SYNC_SCRIPT_TRIGGER_MASTER**

sync_start_trigger_dist_line
----------------------------

    .. py:attribute:: sync_start_trigger_dist_line

        Specifies which external trigger line distributes the synchronized Start Trigger signal. When synchronizing the Start Trigger, configure all devices to use the same Start Trigger distribution line.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Valid Values:** PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, PFI0

                        **Default Value:** "" (empty string)

                        **Supported Devices:** PXIe-5644/5645/5646

                        **Related Topics**

                        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

                        Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Sync Start Trigger Dist Line**
                - C Attribute: **NIRFSG_ATTR_SYNC_START_TRIGGER_DIST_LINE**

sync_start_trigger_master
-------------------------

    .. py:attribute:: sync_start_trigger_master

        Specifies whether the device is the master device when synchronizing the Start Trigger. The master device distributes the synchronized Start Trigger to all devices in the system through the Start Trigger distribution line.

                        When synchronizing the Start Trigger, one device must always be designated as the master. The master device actively drives the Start Trigger distribution line. For slave devices, set the :py:attr:`nirfsg.Session.start_trigger_type` property to digital edge, and set the :py:attr:`nirfsg.Session.digital_edge_start_trigger_source` property to sync_script.

                        To set this property, the NI-RFSG device must be in the Configuration state.

                        **Default Value:** False

                        **Supported Devices:** PXIe-5644/5645/5646

                        **Related Topics**

                        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

                        Refer to the Synchronization Using NI-RFSA and NI-RFSG topic appropriate to your device for more information about device synchronization for vector signal transceivers.

                    **Defined Values**:

        +-------+----------------------------------------------------------------------+
        | Value | Description                                                          |
        +=======+======================================================================+
        | True  | The device is the master device for synchronizing the Start Trigger. |
        +-------+----------------------------------------------------------------------+
        | False | The device is not the master for synchronizing the Start Trigger.    |
        +-------+----------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Triggers:Sync Start Trigger Master**
                - C Attribute: **NIRFSG_ATTR_SYNC_START_TRIGGER_MASTER**

temperature_read_interval
-------------------------

    .. py:attribute:: temperature_read_interval

        Specifies the minimum time between temperature sensor readings.

                        **Units:** Seconds

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Temperature Read Interval**
                - C Attribute: **NIRFSG_ATTR_TEMPERATURE_READ_INTERVAL**

thermal_correction_headroom_range
---------------------------------

    .. py:attribute:: thermal_correction_headroom_range

        Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the :py:attr:`nirfsg.Session.device_temperature` property.

                        For example, if this property is set to 5.0, and the device is self-calibrated at 35°C, then you can expect to run the device from 30°C to 40°C with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance or DSP overflows.

                        **Units:** degrees Celsius (°C)

                        **Default Value**:

                        **PXIe-5830/5831/5832/5842/5860**: 5

                        **PXIe-5840/5841**: 10

                        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Advanced:Thermal Correction Headroom Range (Degrees C)**
                - C Attribute: **NIRFSG_ATTR_THERMAL_CORRECTION_HEADROOM_RANGE**

thermal_correction_temperature_resolution
-----------------------------------------

    .. py:attribute:: thermal_correction_temperature_resolution

        Specifies the temperature change, in degrees Celsius, that is required before NI-RFSG recalculates the thermal correction settings when entering the Generation state.

                        **Units:** degrees Celsius (°C)

                        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Default Values:**

                        PXIe-5830/5831/5832/5842/5860: 0.2

                        PXIe-5840/5841: 1.0

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Advanced:Thermal Correction Temperature Resolution (Degrees C)**
                - C Attribute: **NIRFSG_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION**

timer_event_interval
--------------------

    .. py:attribute:: timer_event_interval

        Specifies the time before the timer emits an event after the task is started and specifies the time interval between Timer events after the first event.

                        **Units**: seconds (s)

                        **Default Value:** 0

                        **Supported Devices:** PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_



        .. note:: For the PXIe-5820/5840/5841/5842/5860, this property must be set for the timer to start. If you do not set this property, the timer is disabled.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Timer:Interval**
                - C Attribute: **NIRFSG_ATTR_TIMER_EVENT_INTERVAL**

upconverter_center_frequency
----------------------------

    .. py:attribute:: upconverter_center_frequency

        Indicates the center frequency of the passband containing the upconverted RF signal. Writing a value to this property while using the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, or PXIe-5820/5840/5841 device enables in-band retuning. In-band retuning increases the speed of frequency sweeps by reducing the amount of upconverter retunes.

                        **Units**: hertz (Hz)

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842



        .. note:: - This property is read/write on the PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842, and is read-only on the PXI-5670/5671.

             - Resetting this property disables in-band retuning, however, for the PXIe-5820, in-band retuning is always enabled.

             - For the PXIe-5820, the only valid value for this property is 0.

             - Setting this property while the PXIe-5644/5645/5646, PXIe-5673/5673E, or PXIe-5820/5830/5831/5832/5840/5841/5842 device is generating has no effect until a dynamic property is set.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Upconverter:Center Frequency (Hz)**
                - C Attribute: **NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY**

upconverter_frequency_offset
----------------------------

    .. py:attribute:: upconverter_frequency_offset

        This property offsets the :py:attr:`nirfsg.Session.upconverter_center_frequency` from the RF frequency. Use this property to keep the local oscillator (LO) leakage at a determined offset from the RF signal.

                        **Valid Values:**

                        PXIe-5644/5645: -42MHz to +42MHz

                        PXIe-5646: -100MHz to +100MHz

                        PXIe-5830/5831/5832/5840/5841: -500MHz to +500MHz

                        PXI-5842 (500 MHz bandwidth option): -250MHz to +250MHz

                        PXI-5842 (1 GHz bandwidth option): -500MHz to +500MHz

                        PXI-5842 (2 GHz bandwidth option): -1GHz to +1GHz

                        PXIe-5842 (4 GHz bandwidth option) using the Standard personality: -1GHz to +1GHz

                        PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality: -2GHz to +2GHz

                        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

                        `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_

                        `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/frequency_and_bandwidth_selection.html>`_



        .. note:: - You cannot set the :py:attr:`nirfsg.Session.upconverter_center_frequency` property or the :py:attr:`nirfsg.Session.arb_carrier_frequency` property at the same time as the :py:attr:`nirfsg.Session.upconverter_frequency_offset` property.

             - Resetting this property disables the upconverter frequency offset.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Upconverter:Frequency Offset (Hz)**
                - C Attribute: **NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET**

upconverter_frequency_offset_mode
---------------------------------

    .. py:attribute:: upconverter_frequency_offset_mode

        Specifies whether to allow NI-RFSG to select the upconverter frequency offset. You can either set an offset yourself or let NI-RFSG select one for you.

                        Placing the upconverter center frequency outside the bandwidth of your waveform can help avoid issues such as LO leakage.

                        To set an offset yourself, set this property to :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.AUTO` or :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.USER_DEFINED`, and set either the :py:attr:`nirfsg.Session.upconverter_center_frequency` or the :py:attr:`nirfsg.Session.upconverter_frequency_offset` property.

                        To allow NI-RFSG to automatically select the upconverter frequency offset, set this property to :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.AUTO` or :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.ENABLE` and set the :py:attr:`nirfsg.Session.signal_bandwidth` to describe the bandwidth of your waveform. The signal bandwidth must be no greater than half the value of the :py:attr:`nirfsg.Session.device_instantaneous_bandwidth` property, minus a device-specific guard band. Do not set the :py:attr:`nirfsg.Session.upconverter_center_frequency` or :py:attr:`nirfsg.Session.upconverter_frequency_offset` properties. If all conditions are met, NI-RFSG places the upconverter center frequency outside the signal bandwidth. Set this property to :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.ENABLE` if you want to receive an error any time NI-RFSG is unable to apply automatic offset.

                        When you set an offset yourself or do not use an offset, the reference frequency for gain is near the upconverter center frequency, and :py:attr:`nirfsg.Session.upconverter_frequency_offset_mode` returns :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.USER_DEFINED`. When NI-RFSG automatically sets an offset, the reference frequency for gain is near the :py:attr:`nirfsg.Session.frequency` and :py:attr:`nirfsg.Session.upconverter_frequency_offset_mode` returns :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.ENABLE`.

                        **Default Value:** :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.AUTO`

                        **Supported Devices**: PXIe-5830/5831/5832/5841/5842

                        **Related Topics**

                        `PXIe-5830 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_

                        `PXIe-5831/5832 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_

                        `PXIe-5841 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/automatic_frequency_offset.html>`_

                    **Defined Values**:

        +----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Value                                                          | Description                                                                                                                                                                                                                                                                                                                |
        +================================================================+============================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.ENABLE`       | NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the :py:attr:`nirfsg.Session.signal_bandwidth` property has been set and can be avoided. NI-RFSG returns an error if the :py:attr:`nirfsg.Session.signal_bandwidth` property has not been set, or if the signal bandwidth is too large. |
        +----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.AUTO`         | NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the :py:attr:`nirfsg.Session.signal_bandwidth` property has been set and can be avoided.                                                                                                                                                |
        +----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.USER_DEFINED` | NI-RFSG uses the offset that you specified with the :py:attr:`nirfsg.Session.upconverter_frequency_offset` or :py:attr:`nirfsg.Session.upconverter_center_frequency` properties.                                                                                                                                           |
        +----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: Below 120 MHz, the PXIe-5841 does not use an LO and :py:data:`~nirfsg.UpconverterFrequencyOffsetMode.ENABLE` is unavailable. Refer to the *PXIe-5841 Automatic Frequency Offset* topic for more information about using an automatic offset with an external LO.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------------------+
            | Characteristic        | Value                                |
            +=======================+======================================+
            | Datatype              | enums.UpconverterFrequencyOffsetMode |
            +-----------------------+--------------------------------------+
            | Permissions           | read-write                           |
            +-----------------------+--------------------------------------+
            | Repeated Capabilities | None                                 |
            +-----------------------+--------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Upconverter:Frequency Offset Mode**
                - C Attribute: **NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE**

upconverter_gain
----------------

    .. py:attribute:: upconverter_gain

        Specifies the gain the upconverter applies to the signal.

                        **Units**: dB

                        **Supported Devices:** PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860



        .. note:: This property is read/write on the PXI-5610 and PXIe-5611 and is read-only on the PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Upconverter:Gain (dB)**
                - C Attribute: **NIRFSG_ATTR_UPCONVERTER_GAIN**

waveform_iq_rate
----------------

    .. py:attribute:: waveform_iq_rate

        Specifies the I/Q rate of the waveform. To set this property, the NI-RFSG device must be in the Configuration state.

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                        **Related Topics**

                        `Streaming <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming.html>`_

                        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_—Refer to this topic for more information about using this property to associate an I/Q rate with a waveform.

                        `Digital Upconverter <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/duc.html>`_




        .. tip:: This property can be set/get on specific waveform within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container waveform to specify a subset.

            Example: :py:attr:`my_session.waveform[ ... ].waveform_iq_rate`

            To set/get on all waveform, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.waveform_iq_rate`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | waveform   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Attributes:Waveform IQ Rate (S/s)**
                - C Attribute: **NIRFSG_ATTR_WAVEFORM_IQ_RATE**

waveform_papr
-------------

    .. py:attribute:: waveform_papr

        Specifies the peak-to-average power ratio (PAPR).

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860




        .. tip:: This property can be set/get on specific waveform within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container waveform to specify a subset.

            Example: :py:attr:`my_session.waveform[ ... ].waveform_papr`

            To set/get on all waveform, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.waveform_papr`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | waveform   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Attributes:Waveform PAPR (dB)**
                - C Attribute: **NIRFSG_ATTR_WAVEFORM_PAPR**

waveform_rf_blanking
--------------------

    .. py:attribute:: waveform_rf_blanking

        **Defined Values**:

        Name (Value): Description

        :py:data:`~nirfsg.RFBlanking.DISABLE` (0):	RF blanking is disabled.

        :py:data:`~nirfsg.RFBlanking.ENABLE` (1):	RF blanking is enabled.

                        **Default Value:** :py:data:`~nirfsg.RFBlanking.DISABLE`

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842

                        **Related Topics**

                        `Marker Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/marker_events.html>`_

                    Enables or disables RF blanking.

        +---------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
        | :py:attr:`nirfsg.Session.rf_blanking_source`                                                                                                                  | :py:attr:`nirfsg.Session.waveform_rf_blanking` | Behaviour                                                                                                 |
        +===============================================================================================================================================================+================================================+===========================================================================================================+
        | "" (empty string)                                                                                                                                             | :py:data:`~nirfsg.RFBlanking.DISABLE`          | No blanking performed.                                                                                    |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
        | "" (empty string)                                                                                                                                             | :py:data:`~nirfsg.RFBlanking.ENABLE`           | Blanking performed based on burst start and stop values and blanking source set to private marker.        |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.NIRFSG_VAL_MARKER0`, :py:data:`~nirfsg.NIRFSG_VAL_MARKER1`, :py:data:`~nirfsg.NIRFSG_VAL_MARKER2`, or :py:data:`~nirfsg.NIRFSG_VAL_MARKER3` | :py:data:`~nirfsg.RFBlanking.DISABLE`          | Blanking performed based on the marker locations for the marker that the user set in the blanking source. |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.NIRFSG_VAL_MARKER0`, :py:data:`~nirfsg.NIRFSG_VAL_MARKER1`, :py:data:`~nirfsg.NIRFSG_VAL_MARKER2`, or :py:data:`~nirfsg.NIRFSG_VAL_MARKER3` | :py:data:`~nirfsg.RFBlanking.ENABLE`           | Error is shown.                                                                                           |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

        .. note:: For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any :py:meth:`nirfsg.Session.reset` or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking properties. Alternatively, you can call :py:meth:`nirfsg.Session.ResetWithOptions` or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific waveform within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container waveform to specify a subset.

            Example: :py:attr:`my_session.waveform[ ... ].waveform_rf_blanking`

            To set/get on all waveform, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.waveform_rf_blanking`

        The following table lists the characteristics of this property.

            +-----------------------+------------------+
            | Characteristic        | Value            |
            +=======================+==================+
            | Datatype              | enums.RFBlanking |
            +-----------------------+------------------+
            | Permissions           | read-write       |
            +-----------------------+------------------+
            | Repeated Capabilities | waveform         |
            +-----------------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Attributes:Waveform RF Blanking**
                - C Attribute: **NIRFSG_ATTR_WAVEFORM_RF_BLANKING**

waveform_runtime_scaling
------------------------

    .. py:attribute:: waveform_runtime_scaling

        Specifies the waveform runtime scaling. The waveform runtime scaling is applied to the waveform data before any other signal processing.

                        **Units**: dB

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860, PXIe-5841 with PXIe-5655




        .. tip:: This property can be set/get on specific waveform within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container waveform to specify a subset.

            Example: :py:attr:`my_session.waveform[ ... ].waveform_runtime_scaling`

            To set/get on all waveform, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.waveform_runtime_scaling`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | waveform   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Attributes:Waveform Runtime Scaling**
                - C Attribute: **NIRFSG_ATTR_WAVEFORM_RUNTIME_SCALING**

waveform_signal_bandwidth
-------------------------

    .. py:attribute:: waveform_signal_bandwidth

        Specifies the bandwidth of the arbitrary signal. This value must be less than or equal to (0.8× :py:attr:`nirfsg.Session.iq_rate`).

                        **Units**: hertz (Hz)

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860




        .. tip:: This property can be set/get on specific waveform within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container waveform to specify a subset.

            Example: :py:attr:`my_session.waveform[ ... ].waveform_signal_bandwidth`

            To set/get on all waveform, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.waveform_signal_bandwidth`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | waveform   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Attributes:Waveform Signal Bandwidth (Hz)**
                - C Attribute: **NIRFSG_ATTR_WAVEFORM_SIGNAL_BANDWIDTH**

waveform_waveform_size
----------------------

    .. py:attribute:: waveform_waveform_size

        Specifies the size of the waveform specified by an active channel.

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5841 with PXIe-5655/5842/5860




        .. tip:: This property can be set/get on specific waveform within your :py:class:`nirfsg.Session` instance.
            Use Python index notation on the repeated capabilities container waveform to specify a subset.

            Example: :py:attr:`my_session.waveform[ ... ].waveform_waveform_size`

            To set/get on all waveform, you can call the property directly on the :py:class:`nirfsg.Session`.

            Example: :py:attr:`my_session.waveform_waveform_size`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | waveform  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Waveform Attributes:Waveform Size**
                - C Attribute: **NIRFSG_ATTR_WAVEFORM_WAVEFORM_SIZE**

write_waveform_burst_detection
------------------------------

    .. py:attribute:: write_waveform_burst_detection

        Enables the detection of burst start and burst stop locations in the waveform. You can read the detected burst start and burst stop locations using :py:meth:`nirfsg.Session._get_waveform_burst_start_locations` and :py:meth:`nirfsg.Session._get_waveform_burst_stop_locations` methods respectively.

                        **Default Value:** :py:data:`~nirfsg.WriteWaveformBurstDetection.DISABLE`

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +--------------------------------------------------------+------------------------------+
        | Value                                                  | Description                  |
        +========================================================+==============================+
        | :py:data:`~nirfsg.WriteWaveformBurstDetection.ENABLE`  | Burst detection is enabled.  |
        +--------------------------------------------------------+------------------------------+
        | :py:data:`~nirfsg.WriteWaveformBurstDetection.DISABLE` | Burst detection is disabled. |
        +--------------------------------------------------------+------------------------------+

        .. note:: - When you download a waveform using :py:meth:`nirfsg.Session.ReadAndDownloadWaveformFromFileTdms` method and if :py:attr:`nirfsg.Session.waveform_rf_blanking` property is enabled, you must set the :py:attr:`nirfsg.Session.write_waveform_burst_detection` property to :py:data:`~nirfsg.WriteWaveformBurstDetection.DISABLE`.

             - For PXIe-5830/5831/5832: The RF Blanking reserves a PXI trigger line. If you are calling any :py:meth:`nirfsg.Session.reset` or `niRFSA_reset <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_reset.html>`_ on the same device, NI recommends calling it before committing blanking properties. Alternatively, you can call :py:meth:`nirfsg.Session.ResetWithOptions` or `niRFSA_ResetWithOptions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/cvinirfsa_resetwithoptions.html>`_. Select **Routes** in the **steps to omit** parameter.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------------+
            | Characteristic        | Value                             |
            +=======================+===================================+
            | Datatype              | enums.WriteWaveformBurstDetection |
            +-----------------------+-----------------------------------+
            | Permissions           | read-write                        |
            +-----------------------+-----------------------------------+
            | Repeated Capabilities | None                              |
            +-----------------------+-----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Write Waveform Burst Detection:Enabled**
                - C Attribute: **NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION**

write_waveform_burst_detection_mode
-----------------------------------

    .. py:attribute:: write_waveform_burst_detection_mode

        Specifies the algorithm that NI-RFSG uses to detect the burst start and burst stop locations in the waveform when burst detection is enabled using the :py:attr:`nirfsg.Session.write_waveform_burst_detection` property. When you set :py:attr:`nirfsg.Session.write_waveform_burst_detection_mode` to :py:data:`~nirfsg.WriteWaveformBurstDetectionMode.AUTO`, NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform. To fine-tune the burst detection process parameters yourself, you can set this property to :py:data:`~nirfsg.WriteWaveformBurstDetectionMode.MANUAL` and specify the burst detection parameters using the write waveform burst detection minimum quiet time, :py:attr:`nirfsg.Session.write_waveform_burst_detection_power_threshold`, write waveform burst detection minimum burst time properties.

                        **Default Value:** :py:data:`~nirfsg.WriteWaveformBurstDetectionMode.AUTO`

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+
        | Value                                                     | Description                                                                                       |
        +===========================================================+===================================================================================================+
        | :py:data:`~nirfsg.WriteWaveformBurstDetectionMode.AUTO`   | NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform. |
        +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.WriteWaveformBurstDetectionMode.MANUAL` | User sets the burst detection parameters.                                                         |
        +-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------------+
            | Characteristic        | Value                                 |
            +=======================+=======================================+
            | Datatype              | enums.WriteWaveformBurstDetectionMode |
            +-----------------------+---------------------------------------+
            | Permissions           | read-write                            |
            +-----------------------+---------------------------------------+
            | Repeated Capabilities | None                                  |
            +-----------------------+---------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Write Waveform Burst Detection:Mode**
                - C Attribute: **NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE**

write_waveform_burst_detection_power_threshold
----------------------------------------------

    .. py:attribute:: write_waveform_burst_detection_power_threshold

        Specifies the relative power level at which burst start or stop locations are detected. The threshold is relative to the peak power in the waveform. NI-RFSG detects burst start (or burst stop) locations when the signal exceeds (or falls below) the level specified by this property. This property is ignored when you disable the :py:attr:`nirfsg.Session.write_waveform_burst_detection` property or when you set the :py:attr:`nirfsg.Session.write_waveform_burst_detection_mode` property to :py:data:`~nirfsg.NIRFSG_VAL_AUTO`.

                        **Units:** dB

                        **Default Value:** 0

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Write Waveform Burst Detection:Power Threshold**
                - C Attribute: **NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD**

write_waveform_normalization
----------------------------

    .. py:attribute:: write_waveform_normalization

        Specifies whether to perform the normalization on a waveform.

                        **Default Value:** :py:data:`~nirfsg.WriteWaveformNormalization.DISABLE`

                        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

                    **Defined Values**:

        +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
        | Value                                                 | Description                                                                                                             |
        +=======================================================+=========================================================================================================================+
        | :py:data:`~nirfsg.WriteWaveformNormalization.ENABLE`  | Enables normalization on a waveform to transform the waveform data so that its maximum is 1.00 and its minimum is -1.00 |
        +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsg.WriteWaveformNormalization.DISABLE` | Disables normalization on the waveform.                                                                                 |
        +-------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+

        .. note:: You can not set :py:attr:`nirfsg.Session.write_waveform_normalization` and :py:attr:`nirfsg.Session.power_level_type` properties at the same time.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.WriteWaveformNormalization |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | None                             |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Arb:Write Waveform Normalization**
                - C Attribute: **NIRFSG_ATTR_WRITE_WAVEFORM_NORMALIZATION**

yig_main_coil_drive
-------------------

    .. py:attribute:: yig_main_coil_drive

        Adjusts the dynamics of the current driving the YIG main coil.

                        **Default Value:** :py:data:`~nirfsg.YigMainCoilDrive.MANUAL`

                        **Supported Devices:** PXIe-5653

                    **Defined Values**:

        +------------------------------------------+--------------------------------------------------------+
        | Value                                    | Description                                            |
        +==========================================+========================================================+
        | :py:data:`~nirfsg.NIRFSG_VAL_SLOW`       | Adjusts the YIG main coil for an underdamped response. |
        +------------------------------------------+--------------------------------------------------------+
        | :py:data:`~nirfsg.YigMainCoilDrive.FAST` | Adjusts the YIG main coil for an overdamped response.  |
        +------------------------------------------+--------------------------------------------------------+

        .. note:: Setting this property to :py:data:`~nirfsg.YigMainCoilDrive.FAST` on the PXIe-5653 allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.YigMainCoilDrive |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **RF:Advanced:YIG Main Coil Drive**
                - C Attribute: **NIRFSG_ATTR_YIG_MAIN_COIL_DRIVE**


NI-TClk Support
===============

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:class:`nitclk.SessionReference` for a complete list of attributes.


.. contents:: Session
