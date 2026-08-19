.. py:module:: nirfsa

Session
=======

.. py:class:: Session(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None)

    

    Creates a new session for the device.

    This method sets the initial value of certain properties and sends initialization commands to reset all hardware modules to a known state necessary for NI-RFSA operation.

    To create a new session, pass the downconverter resource name for the RF vector signal analyzer to the **resource name** parameter.

    You can access the device session this VI creates using the NI-RFSA Soft Front Panel (SFP). Accessing the device session with the SFP can help you debug your code. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about accessing your session with the SFP.

    ----
    **Note**
    Before initializing your device, you must first associate the modules that comprise your device in MAX. After associating the modules, pass the resource name of the device to this method to initialize all the modules. Refer to `Associating NI-RFSA Modules <https://www.ni.com/docs/en-US/bundle/ni-rfsa-max/page/maxrfsa/mi_rf_associating.html>`_ for information about MAX association.

    ----

    ----
    **Note**
    For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending *ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

    ----

    **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

    **Related Topics**

    `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_

    



    :param resource_name:
        

        Specifies the resource name of the device to initialize.

        For NI-RFSA devices, the syntax is the device name specified in MAX. The typical default name for your device in MAX is PXI1Slot2. You can rename your device by right-clicking the name in MAX, selecting **Rename** from the drop-down menu, and entering a new name. You can also pass in the name of an IVI logical name configured with the IVI Configuration utility. For additional information, refer to the **Installed Devices IVI** topic of the *Measurement & Automation Explorer Help*.

        Device names are not case-sensitive. However, IVI logical names are case-sensitive. If you use an IVI logical name, verify the name is identical to the name shown in the IVI Configuration Utility.

        


    :type resource_name: str

    :param id_query:
        

        Specifies whether you want NI-RFSA to perform an ID query.

        **Defined Values** :

        +--------------------------+
        | Description              |
        +==========================+
        | Perform ID query.        |
        +--------------------------+
        | Do not perform ID query. |
        +--------------------------+


    :type id_query: bool

    :param reset_device:
        

        Specifies whether the NI-RFSA device is reset during the initialization procedure.

        **Defined Values** :

        +----------------------+
        | Description          |
        +======================+
        | Reset the device.    |
        +----------------------+
        | Do not reset device. |
        +----------------------+


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

    :param grpc_options:
        

        MeasurementLink gRPC session options

        


    :type grpc_options: nirfsa.GrpcSessionOptions


Methods
=======

abort
-----

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: abort()

            Stops an acquisition previously started with the :py:meth:`nirfsa.Session._initiate` method or the :py:meth:`nirfsa.Session.read_power_spectrum` method.

            You can also use the :py:meth:`nirfsa.Session.abort` method to stop a self-calibration. Calling this method is optional, unless you want to stop an acquisition before it is complete or you are continuously acquiring data.

            You can stop the following kinds of acquisitions:

            - Triggered spectrum acquisitions that have not yet been triggered
            - Multispan acquisitions in progress
            - Average spectrum acquisitions in progress
            - Single-record spectrum acquisitions in progress
            - Streaming in progress

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



change_external_calibration_password
------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: change_external_calibration_password(old_password, new_password)

            Changes the password that is required to initialize an external calibration session.

            **Supported Devices**: PXIe-5601/5603/5605/5606, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



            :param old_password:


                Specifies the old (current) external calibration password.

                The maximum length of the password varies by device.

                


            :type old_password: str
            :param new_password:


                Specifies the new (desired) external calibration password.

                The maximum length of the password varies by device.

                


            :type new_password: str

check_acquisition_status
------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: check_acquisition_status()

            Checks the status of the acquisition.

            Use this method to check for any errors that may occur during signal acquisition or to check whether the device has completed the acquisition operation.

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/hardware-state-diagram.html>`_

            



            :rtype: bool
            :return:


                    Returns signal acquisition status.

                    |Value          |Description                                     |
                    |:---------|:------------------------------------|
                    | True  | Signal acquisition is complete.     |
                    | False | Signal acquisition is not complete. |

                    



clear_self_calibrate_range
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: clear_self_calibrate_range()

            Clears the data obtained from the :py:meth:`nirfsa.Session.self_calibrate_range` method.

            **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

            



close
-----

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: close()

            Closes the session to the device.

            If you close a session that has Soft Front Panel (SFP) session access enabled, any application connected to the shared device session is no longer usable. Refer to `Debugging Your Application Using SFP Session Access <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/using_session_access_sfp_top.html>`_ for more information about using SFP session access.

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: commit()

            Commits settings to hardware.

            Calling this method is optional. Settings are automatically committed to hardware when you call the :py:meth:`nirfsa.Session._initiate` method, the read IQ single record complex F64 method, or the :py:meth:`nirfsa.Session.read_power_spectrum` method.

            ----
            **Note**
            This method does not wait for settling time, unlike the :py:meth:`nirfsa.Session._initiate` method.

            ----

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/hardware-state-diagram.html>`_

            



configure_deembedding_table_interpolation_linear
------------------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_deembedding_table_interpolation_linear(port, table_name, format)

            Selects the linear interpolation method.

            If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str
            :param format:


                Specifies the format of parameters to interpolate. **Defined Values** :

                +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | Name                                                                | Description                                                                                                                             |
                +=====================================================================+=========================================================================================================================================+
                | :py:data:`~nirfsa.LinearInterpolationFormat.REAL_AND_IMAGINARY`     | Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion. |
                +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nirfsa.LinearInterpolationFormat.MAGNITUDE_AND_PHASE`    | Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.                                    |
                +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nirfsa.LinearInterpolationFormat.MAGNITUDE_DB_AND_PHASE` | Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.                      |
                +---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+


            :type format: :py:data:`nirfsa.LinearInterpolationFormat`

configure_deembedding_table_interpolation_nearest
-------------------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_deembedding_table_interpolation_nearest(port, table_name)

            Selects the nearest interpolation method.

            NI-RFSA uses the parameters of the table nearest to the carrier frequency for de-embedding.

            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str

configure_deembedding_table_interpolation_spline
------------------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_deembedding_table_interpolation_spline(port, table_name)

            Selects the spline interpolation method.

            If the carrier frequency does not match a row in the de-embedding table, NI-RFSA performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str

configure_digital_edge_advance_trigger
--------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_digital_edge_advance_trigger(source, edge)

            Configures the device to wait for a digital edge Advance Trigger.

            The Advance Trigger indicates where a new record begins.

            ----
            **Note**
             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.ConfigureAcquisitionType` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

            ----

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param source:


                Specifies the source of the digital edge for the Advance Trigger.

                | Value                                           | Description                                                                                                                                                                                                                |
                |:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                | :py:data:`~nirfsa.NIRFSA_VAL_PFI0` ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                            |
                | :py:data:`~nirfsa.NIRFSA_VAL_PFI1` ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                              |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG0` ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG1` ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG2` ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG3` ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG4` ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG5` ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG6` ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG7` ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_STAR` ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                             |
                | :py:data:`~nirfsa.OutputTerm.PXIE_DSTARB` ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |
                | :py:data:`~nirfsa.OutputTerm.TIMER_EVENT` ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI0` ('PFI0')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI1`('PFI1')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI2` ('PFI2')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI3` ('PFI3')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI4` ('PFI4')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI5` ('PFI5')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI6` ('PFI6')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI7` ('PFI7')               | The trigger is received on PFI 7 of the DIO Terminal. |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source: str
            :param edge:


                Specifies the trigger edge to detect. The default value is :py:data:`~nirfsa.AdvanceTriggerDigitalEdgeEdge.RISING`.

                | Value                              | Description                                |
                |:------------------------------|:--------------------------------|
                | :py:data:`~nirfsa.AdvanceTriggerDigitalEdgeEdge.RISING` (900)  | NI-RFSA detects a rising edge.  |
                | :py:data:`~nirfsa.AdvanceTriggerDigitalEdgeEdge.FALLING` (901) | NI-RFSA detects a falling edge. |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type edge: :py:data:`nirfsa.AdvanceTriggerDigitalEdgeEdge`

configure_digital_edge_ref_trigger
----------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_digital_edge_ref_trigger(source, edge, pretrigger_samples=0)

            Configures the device to wait for a digital edge Reference Trigger to mark a reference point within the record.

            You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

            ----
            **Note**
             The PXIe-5644/5645/5646 does not support the NI-TClk API.

            ----

            ----
            **Note**
             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.ConfigureAcquisitionType` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

            ----

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param source:


                Specifies the source of the digital edge for the Reference trigger.

                |Value                                            |Description                                                                                                                                                                                                                               |
                |:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                | :py:data:`~nirfsa.NIRFSA_VAL_PFI0` ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                                           |
                | :py:data:`~nirfsa.NIRFSA_VAL_PFI1` ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                                             |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG0` ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                                |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG1` ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                                |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG2` ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                                |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG3` ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                                |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG4` ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                                |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG5` ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                                |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG6` ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                                |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG7` ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                                |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_STAR` ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                                            |
                | :py:data:`~nirfsa.OutputTerm.PXIE_DSTARB` ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |
                | :py:data:`~nirfsa.OutputTerm.TIMER_EVENT` ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI0` ('PFI0')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI1`('PFI1')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI2` ('PFI2')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI3` ('PFI3')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI4` ('PFI4')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI5` ('PFI5')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI6` ('PFI6')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI7` ('PFI7')               | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                          |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source: str
            :param edge:


                Specifies the trigger edge to detect. The default value is :py:data:`~nirfsa.ReferenceTriggerDigitalEdgeEdge.RISING`.

                |Value                               |Description                                 |
                |:------------------------------|:--------------------------------|
                | :py:data:`~nirfsa.ReferenceTriggerDigitalEdgeEdge.RISING` (900)  | NI-RFSA detects a rising edge.  |
                | :py:data:`~nirfsa.ReferenceTriggerDigitalEdgeEdge.FALLING` (901) | NI-RFSA detects a falling edge. |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type edge: :py:data:`nirfsa.ReferenceTriggerDigitalEdgeEdge`
            :param pretrigger_samples:


                Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.

                


            :type pretrigger_samples: int

configure_digital_edge_start_trigger
------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_digital_edge_start_trigger(source, edge)

            Configures the device to wait for a digital edge Start Trigger at the beginning of the acquisition.

            You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

            ----
            **Note**
             The PXIe-5644/5645/5646 does not support the NI-TClk API.

            ----

            ----
            **Note**
             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.ConfigureAcquisitionType` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

            ----

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param source:


                Specifies the source of the digital edge for the Start Trigger.

                | Value                                           | Description                                                                                                                                                                                                               |
                |:-------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                | :py:data:`~nirfsa.NIRFSA_VAL_PFI0` ('PFI0')               | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                            |
                | :py:data:`~nirfsa.NIRFSA_VAL_PFI1` ('PFI1')               | The trigger is received on PFI 1.                                                                                                                                                                              |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG0` ('PXI_Trig0')     | The trigger is received on PXI trigger line 0.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG1` ('PXI_Trig1')     | The trigger is received on PXI trigger line 1.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG2` ('PXI_Trig2')     | The trigger is received on PXI trigger line 2.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG3` ('PXI_Trig3')     | The trigger is received on PXI trigger line 3.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG4` ('PXI_Trig4')     | The trigger is received on PXI trigger line 4.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG5` ('PXI_Trig5')     | The trigger is received on PXI trigger line 5.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG6` ('PXI_Trig6')     | The trigger is received on PXI trigger line 6.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG7` ('PXI_Trig7')     | The trigger is received on PXI trigger line 7.                                                                                                                                                                 |
                | :py:data:`~nirfsa.NIRFSA_VAL_PXI_STAR` ('PXI_STAR')       | The trigger is received on the PXI star trigger line. This value is not supported for PXIe-5644/5645/5646 devices.                                                                                             |
                | :py:data:`~nirfsa.OutputTerm.PXIE_DSTARB` ('PXIE_DSTARB') | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.                                                                        |
                | :py:data:`~nirfsa.OutputTerm.TIMER_EVENT` ('TimerEvent')  | The trigger is received from Timer Event on the digitizer. This value is valid on only the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5644/5645/5646 and PXIe-5663E/5665. |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI0` ('PFI1')               | The trigger is received on PFI 0 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI1`('PFI2')               | The trigger is received on PFI 1 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI2` ('PFI3')               | The trigger is received on PFI 2 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI3` ('PFI4')               | The trigger is received on PFI 3 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI4` ('PFI5')               | The trigger is received on PFI 4 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI5` ('PFI6')               | The trigger is received on PFI 5 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI6` ('PFI7')               | The trigger is received on PFI 6 of the DIO Terminal.                                                                                                                                                          |
                | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI7` ('PFI8')               | The trigger is received on PFI 7 of the DIO Terminal.                                                                                                                                                          |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source: str
            :param edge:


                Specifies the trigger edge to detect. The default value is :py:data:`~nirfsa.StartTriggerDigitalEdgeEdge.RISING`.

                | Value                              | Description                                |
                |:------------------------------|:--------------------------------|
                | :py:data:`~nirfsa.StartTriggerDigitalEdgeEdge.RISING` (900)  | NI-RFSA detects a rising edge.  |
                | :py:data:`~nirfsa.StartTriggerDigitalEdgeEdge.FALLING` (901) | NI-RFSA detects a falling edge. |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type edge: :py:data:`nirfsa.StartTriggerDigitalEdgeEdge`

configure_iq_power_edge_ref_trigger
-----------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_iq_power_edge_ref_trigger(source, level, slope, pretrigger_samples=0)

            Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

            To trigger on burst signals, add a minimum quiet time, configured with the :py:attr:`nirfsa.Session.ref_trigger_minimum_quiet_time` property, to ensure the trigger does not occur in the middle of a burst if the acquisition starts while a burst is being generated. The quiet time should be set to a value smaller than the time between bursts, but large enough to ignore power changes within a burst.

            You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

            ----
            **Note**
             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.ConfigureAcquisitionType` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

            ----

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param source:


                Specifies the source of the RF signal for the power edge Reference trigger. The only supported value is "0".

                


            :type source: str
            :param level:


                Specifies the threshold, in dBm, above or below which the device triggers.

                


            :type level: float
            :param slope:


                Specifies whether the device detects a positive or negative slope on the trigger signal. The default value is :py:data:`~nirfsa.ReferenceTriggerIqPowerEdgeSlope.RISING`.

                | Value                                | Description                                                |
                |:--------------------------------|:-------------------------------------------------|
                | :py:data:`~nirfsa.ReferenceTriggerIqPowerEdgeSlope.RISING` (1000)  | NI-RFSA detects a rising edge (positive slope).  |
                | :py:data:`~nirfsa.ReferenceTriggerIqPowerEdgeSlope.FALLING` (1001) | NI-RFSA detects a falling edge (negative slope). |

                


            :type slope: :py:data:`nirfsa.ReferenceTriggerIqPowerEdgeSlope`
            :param pretrigger_samples:


                Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.

                


            :type pretrigger_samples: int

configure_ref_clock
-------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_ref_clock(clock_source, ref_clock_rate)

            Configures the NI-RFSA device Reference Clock.

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `PXI-5661 Reference Clock <https://www.ni.com/docs/en-US/bundle/pxi-5661-feature/page/reference-clock.html>`_

            `PXIe-5663 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/timing-configurations.html>`_

            `PXIe-5665 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/timing-configurations.html>`_

            `PXIe-5667 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/timing-configurations.html>`_

            `PXIe-5668 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/timing-configurations.html>`_

            `PXIe-5830 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/timing-configurations.html>`_

            `PXIe-5831 Timing Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/timing-configurations.html>`_

            



            :param clock_source:


                specifies the source of the Reference Clock signal.
                | Clock Source          | Description |
                |-----------------------|-------------|
                | **Onboard Clock (default)** | Uses the onboard Reference Clock as the clock source. <br/>**PXIe-5830/5831/5832**-<br>- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT. <br>- PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br/>**PXIe-5831 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. <br/>**PXIe-5841 with PXIe-5655**-<br>- Lock to PXIe-5655 onboard clock. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. <br/>**PXIe-5842**-<br>- Lock to PXIe-5655 onboard clock. Use cables as shown in the Getting Started Guide. |
                | **RefIn** | Uses the signal at the front panel REF IN connector. <br/>**PXIe-5830/5831/5832**-<br>- PXIe-5830: Connect PXIe-5820 REF IN to PXIe-3621 REF OUT; lock external signal to PXIe-3621 REF IN. <br>- PXIe-5831: Connect PXIe-5820 REF IN to PXIe-3622 REF OUT; lock external signal to PXIe-3622 REF IN. <br>- PXIe-5832: Connect PXIe-5820 REF IN to PXIe-3623 REF OUT; lock external signal to PXIe-3623 REF IN. <br/>**PXIe-5831 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3622 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3622 REF IN. <br>- Lock external signal to PXIe-5653 REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- Connect PXIe-5820 REF IN to PXIe-3623 REF OUT. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXIe-3623 REF IN. <br>- Lock external signal to PXIe-5653 REF IN. <br/>**PXIe-5841 with PXIe-5655**-<br>- Lock to signal at REF IN on PXIe-5655. Connect REF OUT on PXIe-5655 to PXIe-5841 REF IN. <br/>**PXIe-5842**-<br>- Lock to signal at REF IN on PXIe-5655. Use cables as shown in the Getting Started Guide. |
                | **PXI Clock** | Uses the PXI_CLK signal present on the PXI backplane. |
                | **PXI_ClkMaster** | Valid only for PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. <br/>**PXIe-5831 with PXIe-5653**-<br>- NI-RFSG configures PXIe-5653 to export Reference Clock. <br>- Configures PXIe-5820 and PXIe-3622 to use PXI_Clk. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. <br/>**PXIe-5832 with PXIe-5653**-<br>- NI-RFSG configures PXIe-5653 to export Reference Clock. <br>- Configures PXIe-5820 and PXIe-3623 to use PXI_Clk. <br>- Connect PXIe-5653 REF OUT (10 MHz) to PXI chassis REF IN. |

                


            :type clock_source: :py:data:`nirfsa.ReferenceClockSource`
            :param ref_clock_rate:


                specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. This parameter is only valid when the **ref clock source** parameter is set to **RefIn**. The default value is Auto (-1.0), which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. Refer to the Reference Clock Rate property for possible values.

                


            :type ref_clock_rate: float

configure_software_edge_advance_trigger
---------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_software_edge_advance_trigger()

            Configures the device to wait for a software Advance Trigger.

            The Advance Trigger indicates where a new record begins. The device waits until you call the :py:meth:`nirfsa.Session.send_software_edge_trigger` method to assert the trigger.

            ----
            **Note**
             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.ConfigureAcquisitionType` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

            ----

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



configure_software_edge_ref_trigger
-----------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_software_edge_ref_trigger(pretrigger_samples=0)

            Configures the device to wait for a software Reference Trigger to mark a reference point within the record.

            The device waits until you call the :py:meth:`nirfsa.Session.send_software_edge_trigger` method to assert the trigger.

            You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

            ----
            **Note**
             The PXIe-5644/5645/5646 does not support the NI-TClk API.

            ----

            ----
            **Note**
             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.ConfigureAcquisitionType` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

            ----

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param pretrigger_samples:


                Specifies the number of samples to store for each record that was acquired in the time period immediately before the trigger occurred.

                


            :type pretrigger_samples: int

configure_software_edge_start_trigger
-------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_software_edge_start_trigger()

            Configures the device to wait for a software Start Trigger at the beginning of the acquisition.

            The device waits until you call the :py:meth:`nirfsa.Session.send_software_edge_trigger` method to assert the trigger.

            You can use this trigger with the `NI-TClk API <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/user-manual-welcome.html>`_.

            ----
            **Note**
             The PXIe-5644/5645/5646 does not support the NI-TClk API.

            ----

            ----
            **Note**
             This method is not supported if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.ConfigureAcquisitionType` method or if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM`.

            ----

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



configure_spectrum_frequency
----------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: configure_spectrum_frequency(center_frequency=None, span=None, start_frequency=None, stop_frequency=None)

            Configures the frequency range of a spectrum acquisition.

            You can specify the frequency range using either center frequency and span, or start and stop frequencies.

            ----
            **Note**
            If you configure the spectrum span to a value larger than the instantaneous bandwidth of the device, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you requested.

            ----

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_spectrum_frequency`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.configure_spectrum_frequency`


            :param center_frequency:


                Specifies the center frequency in a spectrum acquisition. The value is expressed in hertz (Hz). Must be used together with **span**.

                


            :type center_frequency: float
            :param span:


                Specifies the span of a spectrum acquisition. The value is expressed in hertz (Hz). Must be used together with **center_frequency**.

                


            :type span: float
            :param start_frequency:


                Specifies the lower limit of a span of frequencies. The value is expressed in hertz (Hz). Must be used together with **stop_frequency**.

                


            :type start_frequency: float
            :param stop_frequency:


                Specifies the upper limit of a span of frequencies. The value is expressed in hertz (Hz). Must be used together with **start_frequency**.

                


            :type stop_frequency: float

create_deembedding_sparameter_table_array
-----------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: create_deembedding_sparameter_table_array(port, table_name, frequencies, sparameter_table, sparameter_orientation)

            Creates an s-parameter de-embedding table for the port from the input data.

            If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.

            **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `De-embedding Overview<https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

                


            :type table_name: str
            :param frequencies:


                Specifies the frequencies for the :py:attr:`nirfsa.Session.SPARAMETER_TABLE` rows. Frequencies must be unique and in ascending order.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type frequencies: numpy.array(dtype=numpy.float64)
            :param sparameter_table:


                Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.

                


            :type sparameter_table: numpy.array(dtype=numpy.complex128)
            :param sparameter_orientation:


                Specifies the orientation of the input data relative to the port on the DUT port.

                **Defined Values** :

                +------------------------------------------------------------+-----------------------------------------------------+
                | Name                                                       | Description                                         |
                +============================================================+=====================================================+
                | :py:data:`~nirfsa.SparameterOrientation.PORT1_TOWARDS_DUT` | Port 1 of the S2P is oriented towards the DUT port. |
                +------------------------------------------------------------+-----------------------------------------------------+
                | :py:data:`~nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT` | Port 2 of the S2P is oriented towards the DUT port. |
                +------------------------------------------------------------+-----------------------------------------------------+


            :type sparameter_orientation: :py:data:`nirfsa.SparameterOrientation`

create_deembedding_sparameter_table_s2p_file
--------------------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: create_deembedding_sparameter_table_s2p_file(port, table_name, s2p_file_path, sparameter_orientation)

            Creates an S-parameter de-embedding table for the port based on the specified S2P file.

            If you only create one table for a port, NI-RFSA automatically selects that table to de-embed the measurement.

            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_

            `S-parameters <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html#GUID-0AD828DE-398A-45C6-ABBA-4208DEB7DE1B__GUID-67A69775-E4DB-4FA2-84FE-C05977ED4184>`_

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

                


            :type table_name: str
            :param s2p_file_path:


                Specifies the path to the S2P file that contains de-embedding information for the specified port.

                


            :type s2p_file_path: str
            :param sparameter_orientation:


                Specifies the orientation of the data in the S2P file relative to the port on the DUT port. **Defined Values** :

                +------------------------------------------------------------+-----------------------------------------------------+
                | Name                                                       | Description                                         |
                +============================================================+=====================================================+
                | :py:data:`~nirfsa.SparameterOrientation.PORT1_TOWARDS_DUT` | Port 1 of the S2P is oriented towards the DUT port. |
                +------------------------------------------------------------+-----------------------------------------------------+
                | :py:data:`~nirfsa.SparameterOrientation.PORT2_TOWARDS_DUT` | Port 2 of the S2P is oriented towards the DUT port. |
                +------------------------------------------------------------+-----------------------------------------------------+


            :type sparameter_orientation: :py:data:`nirfsa.SparameterOrientation`

delete_all_deembedding_tables
-----------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: delete_all_deembedding_tables()

            Deletes all configured de-embedding tables for the session.

            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            



delete_deembedding_table
------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: delete_deembedding_table(port, table_name)

            Deletes the selected de-embedding table for a given port.

            **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

            



            :param port:


                Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

                


            :type port: str
            :param table_name:


                Specifies the name of the table.

                


            :type table_name: str

disable_advance_trigger
-----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: disable_advance_trigger()

            Configures the device to not use an Advance Trigger.

            This method is necessary only if you configured an Advance Trigger in the past and now want to disable it.

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



disable_ref_trigger
-------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: disable_ref_trigger()

            Configures the device to not wait for a Reference Trigger to mark a reference point within a record.

            This method is necessary only if you previously configured a Reference trigger in the past and now want to disable it.

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



disable_start_trigger
---------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: disable_start_trigger()

            Configures the device to not wait for a Start Trigger at the beginning of the acquisition.

            This method is necessary only if you previously configured a Start Trigger in the past and now want to disable it.

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



enable_session_access
---------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: enable_session_access(enable)

            Enables or disables SFP session access for the specified instrument.

            SFP session access allows the NI-RFSA Soft Front Panel (SFP) to access a device with an existing open session and can help you debug your code. To enable session access, pass True to the **enabled** parameter. To disable session access, pass False to the **enabled** parameter.

            Refer to `Configuring SFP Session Access using LabWindows/CVI or C <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/configuring_session_access_labwindows.html>`_ for more information about SFP session access.

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860

            ----
            **Note**
            NI-RFSA does not support NI-TClk when driver session debugging is enabled.

            ----

            



            :param enable:


                Enables or disables SFP session access for the specified device.

                | Value         | Description                         |
                |:---------|:-------------------------|
                | True  | Enables session access.  |
                | False | Disables session access. |

                


            :type enable: bool

error_message
-------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: error_message(error_code)

            Converts an error code returned by an NI-RFSA method into a user-readable string.

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5840

            



            :param error_code:


                Passes the **errorCode** parameter that is returned from any NI-RFSA method.

                


            :type error_code: int

            :rtype: str
            :return:


                    Returns the user-readable message string that corresponds to the error code you specify.

                    You must pass a ViChar array with 1024 bytes or more to this parameter. Only the first 1024 bytes of the array are used.

                    



fetch_iq_multi_record_into
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: fetch_iq_multi_record_into(iq_data_arrays, starting_record=0, number_of_records=None, number_of_samples=None, timeout=hightime.timedelta(seconds=10.0))

            Fetches I/Q data from multiple records in an acquisition.

            A fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.

            This method accepts a data_type parameter to specify the desired data format: numpy.complex64, numpy.complex128, or numpy.int16.

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].fetch_iq_multi_record`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.fetch_iq_multi_record`


            :param iq_data_arrays:


                Specifies a pre-allocated 2D numpy array of shape (number_of_records, number_of_samples) to be filled with the acquired I/Q data. Each row corresponds to one record. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

                


            :type iq_data_arrays: 2D numpy.array of numpy.complex64, 2D numpy.array of numpy.complex128 or interleaved complex data in the form of 2D numpy.array of numpy.int16
            :param starting_record:


                Specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.

                


            :type starting_record: int
            :param number_of_records:


                Specifies the number of records to fetch.

                


            :type number_of_records: int
            :param number_of_samples:


                Specifies the number of samples per record.

                


            :type number_of_samples: int
            :param timeout:


                **PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the method to complete before returning a timeout error.

                **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.

                ----

                For all supported devices, a value of  specifies the method waits until all data is available. A value of 0 specifies the method immediately returns available data.

                ----

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

fetch_iq_single_record_into
---------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: fetch_iq_single_record_into(iq_data_array, record_number=0, number_of_samples=None, timeout=hightime.timedelta(seconds=10.0))

            Fetches I/Q data from a single record in an acquisition.

            The fetch transfers acquired waveform data from device memory to computer memory. The data was acquired to onboard memory previously by the hardware after the acquisition was initiated.

            This method accepts a data_type parameter to specify the desired data format: numpy.complex64, numpy.complex128, or numpy.int16.

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].fetch_iq_single_record`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.fetch_iq_single_record`


            :param iq_data_array:


                Specifies the pre-allocated numpy array to be filled with the acquired I/Q data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively.

                


            :type iq_data_array: numpy array of numpy.complex64, numpy array of numpy.complex128 or interleaved complex data in the form of numpy array of numpy.int16
            :param record_number:


                Specifies the record to retrieve. Record numbers are zero-based.

                


            :type record_number: int
            :param number_of_samples:


                Specifies the number of samples to fetch. The value must specify the array size of the :py:attr:`nirfsa.Session.DATA` parameter.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type number_of_samples: int
            :param timeout:


                **PXI-5661, PXIe-5663/5665/5667** Specifies the time, in seconds, allotted for the method to complete before returning a timeout error.

                **PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860** Specifies the time, in seconds, allotted to receive the reference trigger.

                ----

                For all supported devices, a value of  specifies the method waits until all data is available. A value of 0 specifies the method immediately returns available data.

                ----

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

get_deembedding_sparameters
---------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_deembedding_sparameters()

            Returns the S-parameters used for de-embedding a measurement on the selected port.

            This includes interpolation of the parameters based on the configured carrier frequency. This method returns an empty array if no de-embedding is done.

            If you want to call this method just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.

            **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

            

            .. note:: The port orientation for the returned S-parameters is normalized to :py:data:`~nirfsa.SparameterOrientation.PORT1_TOWARDS_DUT`.



            :rtype: numpy.array(dtype=numpy.complex128)
            :return:


                    Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.

                    



get_ext_cal_last_date_and_time
------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_ext_cal_last_date_and_time()

            Returns the date and time of the last successful external calibration.

            The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this method returns

            14 for the hours parameter and

            30 for the minutes parameter.

            **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



            :rtype: hightime.datetime
            :return:


                    



get_ext_cal_recommended_interval
--------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_ext_cal_recommended_interval()

            Returns the recommended interval between external calibrations, in months.

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



            :rtype: hightime.timedelta, datetime.timedelta, or int in months
            :return:


                    Returns the recommended maximum interval between external calibrations, in months.

                    



get_fetch_backlog
-----------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_fetch_backlog(record_number)

            Returns the number of points acquired that have not yet been fetched.

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_fetch_backlog`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_fetch_backlog`


            :param record_number:


                Specifies the record from which to read the backlog. Record numbers are zero-based.

                


            :type record_number: int

            :rtype: int
            :return:


                    Returns the number of samples available to read for the requested record.

                    



get_frequency_response
----------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_frequency_response()

            Returns the requested device response type, based on current NI-RFSA settings. The PXI-5661 and PXIe-5663/5663E/5665/5667/5668 automatically corrects the IF and RF response when you set the Digital IF Equalization Enabled property to TRUE. If you are using external digitizer mode, you can use information returned from this VI to correct your measurement.

            Refer to the *Factory Calibration* topic for your device for more information about frequency-response calibration.

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_frequency_response`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_frequency_response`


            :rtype: tuple (frequencies, magnitude_response, phase_response)

                WHERE

                frequencies (list of float): 


                    Returns an array containing the frequencies, in hertz (Hz), that correspond to the response data.

                    Pass VI_NULL if you do not want to use this parameter.

                    


                magnitude_response (list of float): 


                    Returns an array containing the magnitude of the requested response, in decibels (dB). The magnitude response is normalized to the center frequency at each frequency in the :py:attr:`nirfsa.Session.FREQUENCIES` array.

                    Pass VI_NULL if you do not want to use this parameter.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.


                phase_response (list of float): 


                    Returns an array containing the phase of the requested response, in radians. The phase response is normalized to the center frequency at each frequency entry in the :py:attr:`nirfsa.Session.FREQUENCIES` array.

                    Pass VI_NULL if you do not want to use this parameter. This array may contain zeros if the device does not contain a stored phase response in its calibration data.

                    

                    .. note:: One or more of the referenced properties are not in the Python API for this driver.



get_scaling_coefficients
------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_scaling_coefficients()

            Returns coefficients you can use to convert unscaled data to scaled I/Q data.

            Acquired data may be unscaled when sent by a peer-to-peer stream or fetched as unscaled data. Use this method to obtain :py:meth:`nirfsa.Session.get_scaling_coefficients` structures in the **:py:attr:`nirfsa.Session.COEFFICIENT_INFO`** array that provide gain and offset values you can use to scale this data into the actual I/Q values. The **:py:attr:`nirfsa.Session.COEFFICIENT_INFO`** array returns one element for each channel specified in the **:py:attr:`nirfsa.Session.CHANNEL_LIST`** parameter. The element order matches the order specified by the **:py:attr:`nirfsa.Session.CHANNEL_LIST`** parameter. To get the actual I/Q values, scale the unscaled data from an acquisition by multiplying it by the gain value of the appropriate **:py:attr:`nirfsa.Session.COEFFICIENT_INFO`** element then adding the offset from the same element.

            ----
            **Note**
            The coefficients are calculated by NI-RFSA for the current configuration of the device, so they are only valid for acquisitions obtained with the same device configuration.

            ----

            To get the required size of the array, call this method with **:py:attr:`nirfsa.Session.ARRAY_SIZE`** set to 0 and NULL for the **:py:attr:`nirfsa.Session.COEFFICIENT_INFO`** array. This method returns the required size in the **:py:attr:`nirfsa.Session.NUMBER_OF_COEFFICIENT_SETS`** parameter.

            **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_scaling_coefficients`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.get_scaling_coefficients`


            :rtype: list of CoefficientInfo
            :return:


                    Specifies the array for storing the coefficient info.

                    - **offset** is the number that should be added to the data from a peer-to-peer stream after the gain has been applied if you want to scale unscaled data.
                    - **gain** returns the multiplier that you should use to scale data obtained from a peer-to-peer stream.

                    



get_self_cal_last_date_and_time
-------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_self_cal_last_date_and_time(self_calibration_step)

            Returns the date and time of the last successful self-calibration.

            The time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this method returns

            14 for the hours parameter and

            30 for the minutes parameter.

            **Supported Devices** : PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            



            :param self_calibration_step:


                Specifies the self-calibration step to query for the last successful self-calibration date and time data.

                


            :type self_calibration_step: :py:data:`nirfsa.SelfCalibrationStep`

            :rtype: hightime.datetime
            :return:


                    



get_self_calibration_temperature
--------------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_self_calibration_temperature(self_calibration_step)

            Returns the temperature, in degrees Celsius, at the last successful self-calibration.

            ----
            **Note**
            For the PXIe-5644/5645/5646, you must select :py:data:`~nirfsa.NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION` for the **selfCalibrationStep** parameter.

            ----

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860

            

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



            :param self_calibration_step:


                Specifies the self-calibration step to query for the last successful self-calibration date and time data.

                +-------------------------------------------+-------------------------------------------------------------------------------------------------+
                | Name                                      | Description                                                                                     |
                +===========================================+=================================================================================================+
                | SelfCalibrationStep.PRESELECTOR_ALIGNMENT | Calls for preselector alignment.                                                                |
                +-------------------------------------------+-------------------------------------------------------------------------------------------------+
                | SelfCalibrationStep.GAIN_REFERENCE        | Measures the changes in gain since the last external calibration was run.                       |
                +-------------------------------------------+-------------------------------------------------------------------------------------------------+
                | SelfCalibrationStep.IF_FLATNESS           | Measures the IF response of the entire system for each of the supported IF filters              |
                +-------------------------------------------+-------------------------------------------------------------------------------------------------+
                | SelfCalibrationStep.DIGITIZER_SELF_CAL    | Calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter. |
                +-------------------------------------------+-------------------------------------------------------------------------------------------------+
                | SelfCalibrationStep.LO_SELF_CAL           | Calls for LO self-calibration, if the LO source module is associated with the RF downconverter. |
                +-------------------------------------------+-------------------------------------------------------------------------------------------------+
                | SelfCalibrationStep.AMPLITUDE_ACCURACY    | Selects the Amplitude Accuracy self-calibration step.                                           |
                +-------------------------------------------+-------------------------------------------------------------------------------------------------+
                | SelfCalibrationStep.RESIDUAL_LO_POWER     | Selects the Residual LO Power self-calibration step.                                            |
                +-------------------------------------------+-------------------------------------------------------------------------------------------------+
                | SelfCalibrationStep.IMAGE_SUPPRESSION     | Selects the Image Suppression self-calibration step.                                            |
                +-------------------------------------------+-------------------------------------------------------------------------------------------------+
                | SelfCalibrationStep.SYNTHESIZER_ALIGNMENT | Selects the Synthesizer Alignment self-calibration step.                                        |
                +-------------------------------------------+-------------------------------------------------------------------------------------------------+
                | SelfCalibrationStep.DC_OFFSET             | Selects the DC Offset self-calibration step.                                                    |
                +-------------------------------------------+-------------------------------------------------------------------------------------------------+


            :type self_calibration_step: :py:data:`nirfsa.SelfCalibrationStep`

            :rtype: float
            :return:


                    Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

                    



get_terminal_name
-----------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: get_terminal_name(signal, signal_identifier="")

            Returns the fully qualified name of the signal being queried.

            Signals can be triggers, clocks, or events.

            You can pass the **:py:attr:`nirfsa.Session.TERMINAL_NAME`** parameter that is returned to the **source** parameter of a configure trigger method.

            **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :param signal:


                Specifies the signal for which you want to query the terminal.

                +------------------------------+----------------------------------------------+
                | Name                         | Description                                  |
                +==============================+==============================================+
                | Signal.START_TRIGGER         | NI-RFSA routes a Start Trigger.              |
                +------------------------------+----------------------------------------------+
                | Signal.REF_TRIGGER           | NI-RFSA routes a Reference                   |
                +------------------------------+----------------------------------------------+
                | Signal.ADVANCE_TRIGGER       | NI-RFSA routes an Advance                    |
                +------------------------------+----------------------------------------------+
                | Signal.READY_FOR_START_EVENT | NI-RFSA routes a Ready for Start Event.      |
                +------------------------------+----------------------------------------------+
                | Signal.READY_FOR_REF_EVENT   | NI-RFSA routes a Ready for Reference Event.. |
                +------------------------------+----------------------------------------------+
                | Signal.END_OF_RECORD_EVENT   | NI-RFSA routes a End of Record Event.        |
                +------------------------------+----------------------------------------------+
                | Signal.DONE_EVENT            | NI-RFSA routes a Done Event.                 |
                +------------------------------+----------------------------------------------+
                | Signal.REF_CLOCK             | NI-RFSA routes a Reference Clock.            |
                +------------------------------+----------------------------------------------+
                | Signal.USER                  | NI-RFSA routes a User Defined Signal.        |
                +------------------------------+----------------------------------------------+


            :type signal: :py:data:`nirfsa.Signal`
            :param signal_identifier:


                Specifies a particular instance of a trigger. NI-RFSA does not support this parameter.

                


            :type signal_identifier: str

            :rtype: str
            :return:


                    Returns the fully qualified name of the signal being queried.

                    



initiate
--------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: initiate()

            Commits settings to hardware, waits for hardware settling, and starts an acquisition.

            You can use this method in conjunction with one of the niRFSA fetch I/Q methods to retrieve acquired I/Q data, or you can use the read IQ single record complex F64 method to both initiate the acquisition and retrieve I/Q data at one time.

            ----
            **Note**
            If you are using external digitizer mode, this method commits settings and waits for settling, but it does not start an acquisition. Notice that using the :py:meth:`nirfsa.Session.commit` method on its own commits settings to hardware, but the device does not wait for hardware settling.

            ----

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

            `RF List Mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_

            `NI RF Vector Signal Analyzer State Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/hardware-state-diagram.html>`_

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



is_self_cal_valid
-----------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: is_self_cal_valid()

            Indicates which calibration steps contain valid calibration data.

            To omit steps with valid calibration data from self-calibration, you can pass the **:py:attr:`nirfsa.Session.VALID_STEPS`** parameter to the **stepsToOmit** parameter of the :py:meth:`nirfsa.Session.SelfCalibrate` method.

            **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.



            :rtype: tuple (self_cal_valid, valid_steps)

                WHERE

                self_cal_valid (bool): 


                    Returns True if all the calibration data is valid and False if any of the calibration data is invalid.

                    


                valid_steps (:py:data:`nirfsa.SelfCalSteps`): 


                    Returns valid steps.

                    ----
                    If two or more calibration steps are valid, this parameter returns a bitwise-OR combination of the calibration steps. For example, if both :py:data:`~nirfsa.SelfCalSteps.IF_FLATNESS` and :py:data:`~nirfsa.SelfCalSteps.LO_SELF_CAL` steps are valid, NI-RFSA returns the following string:

                    :py:data:`~nirfsa.SelfCalSteps.IF_FLATNESS` |

                    :py:data:`~nirfsa.SelfCalSteps.LO_SELF_CAL`

                    ----

                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+
                    | Name                               | Description                                                                                                         |
                    +====================================+=====================================================================================================================+
                    | SelfCalSteps.DIGITIZER_SELF_CAL    | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.   |
                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+
                    | SelfCalSteps.PRESELECTOR_ALIGNMENT | Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.                       |
                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+
                    | SelfCalSteps.OMIT_NONE             | No calibration steps are omitted.                                                                                   |
                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+
                    | SelfCalSteps.GAIN_REFERENCE        | Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted. |
                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+
                    | SelfCalSteps.IF_FLATNESS           | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.         |
                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+
                    | SelfCalSteps.LO_SELF_CAL           | Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.    |
                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+
                    | SelfCalSteps.AMPLITUDE_ACCURACY    | Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.    |
                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+
                    | SelfCalSteps.RESIDUAL_LO_POWER     | Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.    |
                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+
                    | SelfCalSteps.IMAGE_SUPPRESSION     | Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.    |
                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+
                    | SelfCalSteps.SYNTHESIZER_ALIGNMENT | Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.    |
                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+
                    | SelfCalSteps.DC_OFFSET             | Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.    |
                    +------------------------------------+---------------------------------------------------------------------------------------------------------------------+

                    .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



load_configurations_from_file
-----------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: load_configurations_from_file(file_path)

            Loads the configurations from the specified file to the NI-RFSA driver session.

            The VI does an implicit reset before loading the configurations from the file.

            **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].load_configurations_from_file`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.load_configurations_from_file`


            :param file_path:


                Specifies the absolute path of the file from which the NI-RFSA loads the configurations.

                


            :type file_path: str

lock
----

    .. py:currentmodule:: nirfsa.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`nirfsa.Session.lock` method.
        -  A call to NI-RFSA locked the session.
        -  After a call to the :py:meth:`nirfsa.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`nirfsa.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`nirfsa.Session.lock` method and the
           :py:meth:`nirfsa.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nirfsa.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nirfsa.Session.lock` method with a call to
    the :py:meth:`nirfsa.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with nirfsa.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`nirfsa.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited

perform_thermal_correction
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: perform_thermal_correction()

            Corrects for temperature variations while acquiring the same signal for an extended period of time in a continuous acquisition.

            NI-RFSA internally acquires the temperature every time you initiate an acquisition. If you are performing a continuous acquisition, National Instruments recommends calling this method once every 10 minutes in a stable temperature environment to periodically update temperature calibration. If the ambient temperature varies, call this method more frequently.

            ----
            **Note**
            You cannot call this method if your device is operating in `RF list mode <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/rf-list-mode.html>`_.

            ----

            Refer to the *Thermal Management* section for your device for more information about typical operating temperatures.

            **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842

            



read_iq_single_record_into
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: read_iq_single_record_into(iq_data_array, data_array_size, timeout=hightime.timedelta(seconds=10.0))

            Initiates an acquisition and fetches a single I/Q data record.

            Do not use this method if you have configured the device to continuously acquire data samples or to acquire multiple records.

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `None (Trigger Type) <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/no-trigger.html>`_

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].read_iq_single_record`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.read_iq_single_record`


            :param iq_data_array:


                Returns the acquired waveform. Allocate an NIComplexNumber array at least as large as the number of samples configured in the :py:meth:`nirfsa.Session.ConfigureNumberOfSamples` method.

                


            :type iq_data_array: numpy array of numpy.complex64, numpy array of numpy.complex128 or interleaved complex data in the form of numpy array of numpy.int16
            :param timeout:


                Specifies in seconds the time allotted for the method to complete before returning a timeout error. A value of  specifies the method waits until all data is available.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: WaveformInfo
            :return:


                    Contains the absolute and relative timestamps for the operation, the time interval (dt), and the actual number of samples read.

                    The following list provides more information about each of these properties:

                    - **absolute timestamp** Returns the timestamp, in seconds, of the first fetched sample that is comparable between records and acquisitions.

                    ----

                    The value of the absolute timestamp returned is always 0 for the PXIe-5644/5645/5646, PXIe-5668, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860.

                    ----

                    - **relative timestamp** Returns a timestamp that corresponds to the difference, in seconds, between the first sample returned and the Reference Trigger location. The timestamp is zero if the Reference Trigger has not occurred.

                    ----


                    The value of the relative timestamp returned is always 0 for the PXIe-5644/5645/5646.

                    ----

                    - **dt** Returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value.
                    - **actual samples read** Returns an integer representing the number of samples in the waveform.
                    - **offset** Returns the offset to scale data, (*b*), in *mx* + *b* form.
                    - **gain** Returns the gain to scale data, (*m*), in *mx* + *b* form.

                    



read_power_spectrum_into
------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: read_power_spectrum_into(power_spectrum_data_array, data_array_size=None, timeout=hightime.timedelta(seconds=10.0))

            Initiates a spectrum acquisition and returns power spectrum data.

            ----
            **Note**
             Under certain configurations, negative infinity is returned from this VI. If the Reference Level is very high and if the Signal Bandwidth is comparatively less, the ADC returns zero, which equates to negative infinity in dBm. This is expected behavior.

            ----

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].read_power_spectrum`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.read_power_spectrum`


            :param power_spectrum_data_array:


                Specifies a pre-allocated numpy array to be filled with power spectrum data. The dtype of this array determines the data format: numpy.float64 or numpy.float32. Allocate an array at least as large as the number of spectral lines returned by the get_number_of_spectral_lines method.

                


            :type power_spectrum_data_array: numpy.array of numpy.float64 or numpy.array of numpy.float32
            :param data_array_size:


                Specifies the expected number of spectral lines. If None, falls back to self.number_of_spectral_lines.

                


            :type data_array_size: int
            :param timeout:


                Specifies the time, in seconds, allotted for the method to complete before returning a timeout error. A value of specifies the method waits until all data is available.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

reset
-----

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: reset()

            Resets all properties to default values, deletes all de-embedding tables, and stops the export of all external signals and events.

            For the PXI-5600, this method does not reset the PXI Clock signal that is driven by devices installed in the Trigger Controller Slot, also known as the System Timing Slot.

            This method resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG. To avoid resetting routes on the device that are in use by NI-RFSG sessions, NI recommends using the :py:meth:`nirfsa.Session.reset_with_options` method, with **stepsToOmit** set to :py:data:`~nirfsa.NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES`.

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

            

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



reset_device
------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: reset_device()

            Performs a hard reset on the device.

            A hard reset consists of the following actions:

            - Signal acquisition is stopped.
            - All routes are released.
            - External bidirectional terminals are tristated.
            - FPGAs are reset.
            - Hardware is configured to its default state.
            - All session properties are reset to their default states.

            During a device reset, routes of signals between this and other devices are released, regardless of which device created the route. For example, a trigger signal exported to a PXI trigger line that is used by another device is no longer exported.

            On the PXI-5600, if you are driving the PXI_CLK10 line, you continue to drive the clock even after a device reset. To stop driving the PXI_CLK10 line, use the :py:meth:`nirfsa.Session.ConfigurePxiChassisClk10` method and set the **pxiClk10Source** parameter to :py:data:`~nirfsa.NIRFSA_VAL_NONE` or set the :py:attr:`nirfsa.Session.PXI_CHASSIS_CLK10_SOURCE` property to :py:data:`~nirfsa.NIRFSA_VAL_NONE`.

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



reset_with_options
------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: reset_with_options(steps_to_omit)

            Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes.

            For the PXI-5600, this method does not reset the PXI Clock signal that is driven by devices installed in the Star Trigger Controller Slot, also known as the System Timing Slot.

            By default, this method resets all properties to their default values, deletes all de-embedding tables, aborts generation, clears all routes, and resets session properties to initial values. You can specify steps to omit using the steps to omit parameter. For example, if you specify :py:data:`~nirfsa.NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES` for the **:py:attr:`nirfsa.Session.STEPS_TO_OMIT`** parameter, this method does not release signal routes during the reset process.

            When routes of signals between two devices are released, they are released regardless of which device created the route.

            To avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSG sessions, NI recommends using this method instead of :py:meth:`nirfsa.Session.Reset`, with **:py:attr:`nirfsa.Session.STEPS_TO_OMIT`** set to :py:data:`~nirfsa.NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES`.

            **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

            

            .. note:: One or more of the referenced properties are not in the Python API for this driver.

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



            :param steps_to_omit:


                Specifies a list of steps to skip during the reset process. The default value is :py:data:`~nirfsa.ResetWithOptionsStepsToOmit.NONE`, which specifies that no step is omitted during reset.

                Note::py:data:`~nirfsa.ResetWithOptionsStepsToOmit.ROUTES` is not supported in external calibration or alignment sessions.

                Note::py:data:`~nirfsa.ResetWithOptionsStepsToOmit.ROUTES` is not supported for the PXI-5600/5661.

                +------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Name                                           | Description                                                                                                                                                                                                |
                +================================================+============================================================================================================================================================================================================+
                | ResetWithOptionsStepsToOmit.DEEMBEDDING_TABLES | Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.                                                                                                              |
                +------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.NONE               | No step is omitted during reset.                                                                                                                                                                           |
                +------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.ROUTES             | Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset. |
                +------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type steps_to_omit: :py:data:`nirfsa.ResetWithOptionsStepsToOmit`

save_configurations_to_file
---------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: save_configurations_to_file(file_path)

            Saves the configurations of the session to the specified file.

            **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            


            .. tip:: This method can be called on specific channels within your :py:class:`nirfsa.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].save_configurations_to_file`

                To call the method on all channels, you can call it directly on the :py:class:`nirfsa.Session`.

                Example: :py:meth:`my_session.save_configurations_to_file`


            :param file_path:


                Specifies the absolute path of the file to which the NI-RFSA saves the configurations.

                


            :type file_path: str

self_calibrate_range
--------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: self_calibrate_range(steps_to_omit, minimum_frequency, maximum_frequency, minimum_reference_level, maximum_reference_level)

            Self-calibrates all configurations within the specified frequency and reference level limits.

            Self-calibration range data is valid until you restart the system or call the :py:meth:`nirfsa.Session.clear_self_calibrate_range` method.

            NI recommends that no external signals are present on the RF In port while the calibration is taking place.

            ----
            **Note**
            This method does not update self-calibration date and temperature.

            ----

            For best results, NI recommends that you perform a complete self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit that step for faster execution.

            ----
            **Note**
            If there is an existing NI-RFSG session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this method runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSG Commit or niRFSG Initiate.

            ----

            ----
            **Note**
            If there is an existing NI-RFSG session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this method runs.

            ----

            **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

            



            :param steps_to_omit:


                Specifies which calibration steps to skip as part of the self-calibration process. A value of 0 specifies all supported calibration steps are performed.

                ----

                To omit two or more calibration steps, specify a bitwise-OR combination of the following constants. For example, if you wanted to omit :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.AMPLITUDE_ACCURACY` and :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.LO_SELF_CAL`, you would pass the following string to the :py:meth:`nirfsa.Session.SelfCalibrate` method: :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.AMPLITUDE_ACCURACY` | :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.LO_SELF_CAL`

                ----

                | Value                                          |  Description                                                                                                                                                                                                                     |
                |:------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
                | :py:data:`~nirfsa.NIRFSA_VAL_RESET_WITH_OPTIONS_NONE`             | No step is omitted during self-calibration.                                                                                                                                                                           |
                | :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.PRESELECTOR_ALIGNMENT` | Not used by this method.                                                                                                                                                                                            |
                | :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.GAIN_REFERENCE`        | Not used by this method.                                                                                                                                                                                            |
                | :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.IF_FLATNESS`           | Not used by this method.                                                                                                                                                                                            |
                | :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.DIGITIZER_SELF_CAL`    | Not used by this method.                                                                                                                                                                                            |
                | :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.LO_SELF_CAL`           | Omits the Local Oscillator (LO) Self Cal step. If you omit this step and the :py:meth:`nirfsa.Session.is_self_cal_valid` method indicates the calibration data for this step is invalid, the LO phase-locked loop (PLL) may fail to lock. |
                | :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.AMPLITUDE_ACCURACY`    | Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted.                                                                                                        |
                | :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.RESIDUAL_LO_POWER`     | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.                                                                                                           |
                |:py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.IMAGE_SUPPRESSION`      | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image Performance is not adjusted.                                                                                                     |
                | :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.SYNTHESIZER_ALIGNMENT` | Omits the Synthesizer Alignment step. If you omit this step, the LO PLL is not adjusted. This step is not valid for the PXIe-5820.                                                                                    |
                | :py:data:`~nirfsa.SelfCalibrateRangeStepsToOmit.DC_OFFSET`             | Omits the DC Offset step. This step applies only to the PXIe-5820.                                                                                                                                                    |

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type steps_to_omit: :py:data:`nirfsa.SelfCalibrateRangeStepsToOmit`
            :param minimum_frequency:


                Specifies the minimum RF frequency in Hz.

                


            :type minimum_frequency: float
            :param maximum_frequency:


                Specifies the maximum RF frequency in Hz.

                


            :type maximum_frequency: float
            :param minimum_reference_level:


                Specifies the minimum reference level in dBm.

                


            :type minimum_reference_level: float
            :param maximum_reference_level:


                Specifies the maximum reference level in dBm.

                


            :type maximum_reference_level: float

self_test
---------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: self_test()

            Performs a self-test on the NI-RFSA device and returns the test results.

            This method performs a simple series of tests to ensure that the NI-RFSA device is powered up and responding.

            This method does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this method. The NI-RFSA device must be in the Configuration state before you call this method.

            **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Device Warm-Up <https://www.ni.com/docs/en-US/bundle/rfsa/page/rfsa/warmup.html>`_

            +----------------+------------------+
            | Self-Test Code | Description      |
            +================+==================+
            | 0              | Passed self-test |
            +----------------+------------------+
            | 1              | Self-test failed |
            +----------------+------------------+



send_software_edge_trigger
--------------------------

    .. py:currentmodule:: nirfsa.Session

    .. py:method:: send_software_edge_trigger(trigger, trigger_identifier="")

            Sends a trigger to the device when you use a software version of a supported trigger and the device is waiting for the trigger to be sent.

            You can also use this method to override a hardware trigger.

            This method returns an error in the following situations:

            - You configure an invalid trigger.
            - You set the **acquisitionType** to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.ConfigureAcquisitionType` method.
            - You have not previously called the :py:meth:`nirfsa.Session._initiate` method.

            **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

            **Related Topics**

            `Software Trigger <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/software-edge-trigger.html>`_

            `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

            



            :param trigger:


                Specifies the trigger to send.

                **Default Value:** :py:data:`~nirfsa.SoftwareTriggerType.START`

                **Defined Values:**

                +----------------------------------------------+-------------------------------+
                | Name                                         | Description                   |
                +==============================================+===============================+
                | :py:data:`~nirfsa.SoftwareTriggerType.START` | Specifies the Start Trigger.  |
                +----------------------------------------------+-------------------------------+
                | :py:data:`~nirfsa.NIRFSA_VAL_SCRIPT_TRIGGER` | Specifies the Script Trigger. |
                +----------------------------------------------+-------------------------------+

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger: :py:data:`nirfsa.SoftwareTriggerType`
            :param trigger_identifier:


                Specifies a particular instance of a trigger. NI-RFSA does not currently support this parameter.

                


            :type trigger_identifier: str

unlock
------

    .. py:currentmodule:: nirfsa.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`nirfsa.Session.lock`. Refer to :py:meth:`nirfsa.Session.unlock` for additional
    information on session locks.


Properties
==========

absolute_delay
--------------

    .. py:attribute:: absolute_delay

        Specifies the sub-sample clock delay, in seconds, to apply to the acquired signal.

        Use this property to reduce the trigger jitter when synchronizing multiple devices with NI-TClk.
        This property can also help maintain synchronization repeatability by writing the absolute delay value of a previous measurement to the current session.

        To set this property, the NI-RFSA device must be in the Configuration state.

        ----
        **Note**
        If this property is set, NI-TClk cannot do any sub-sample clock adjustment.

        ----

        **Units:** Seconds

        **Valid Values:** Plus or minus half of one sample clock period

        **Default Value**: 0

        **Supported Devices:** PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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
                - C Attribute: **NIRFSA_ATTR_ABSOLUTE_DELAY**

acquisition_type
----------------

    .. py:attribute:: acquisition_type

        Configures the session to either acquire I/Q data or to compute a power spectrum over the specified frequency range.

        **Default Value**: :py:data:`~nirfsa.AcquisitionType.IQ`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureAcquisitionType`

        **Defined Values**:

        +---------------------------------------------+-----------------------------------------------+
        | Name                                        | Description                                   |
        +=============================================+===============================================+
        | :py:data:`~nirfsa.AcquisitionType.IQ`       | Configures NI-RFSA for I/Q acquisitions.      |
        +---------------------------------------------+-----------------------------------------------+
        | :py:data:`~nirfsa.AcquisitionType.SPECTRUM` | Configures NI-RFSA for spectrum acquisitions. |
        +---------------------------------------------+-----------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.AcquisitionType |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition Type**
                - C Attribute: **NIRFSA_ATTR_ACQUISITION_TYPE**

advance_trigger_terminal_name
-----------------------------

    .. py:attribute:: advance_trigger_terminal_name

        Returns the fully qualified signal name as a string.

        **Default Values**:

        **PXIe-5830/5831/5832**:  /<i>BasebandModule</i>/<i>ai</i>/0/<i>AdvanceTrigger</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

        **PXIe-5820/5840/5841/5842**: /<i>ModuleNameai</i>/0/<i>AdvanceTrigger</i>, where *ModuleName* is the name of your device in MAX.

        **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>AdvanceTrigger</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

        **All other devices**: /<i>DigitizerName</i>/<i>AdvanceTrigger</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.get_terminal_name`

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

                - LabVIEW Property: **Triggers:Advance:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_ADVANCE_TRIGGER_TERMINAL_NAME**

advance_trigger_type
--------------------

    .. py:attribute:: advance_trigger_type

        Specifies whether you want the Advance Trigger to be a digital edge or software trigger.

        ----
        **Note**
        Set this property to :py:data:`~nirfsa.AdvanceTriggerType.NONE` if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` or if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.ConfigureAcquisitionType` method.

        ----

        **Default Value**: :py:data:`~nirfsa.AdvanceTriggerType.NONE`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **Defined Values**:

        +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                | Description                                                                                                                                                                                                                                                                   |
        +=====================================================+===============================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.AdvanceTriggerType.NONE`          | No Advance Trigger is configured.                                                                                                                                                                                                                                             |
        +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.AdvanceTriggerType.DIGITAL_EDGE`  | The Advance Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the :py:attr:`nirfsa.Session.digital_edge_advance_trigger_source` property.                                                                            |
        +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.AdvanceTriggerType.SOFTWARE_EDGE` | The Advance Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the :py:meth:`nirfsa.Session.send_software_edge_trigger` method and selecting :py:data:`~nirfsa.NIRFSA_VAL_ADVANCE_TRIGGER` as the **trigger** parameter. |
        +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.AdvanceTriggerType |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | None                     |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Advance:Type**
                - C Attribute: **NIRFSA_ATTR_ADVANCE_TRIGGER_TYPE**

allow_more_records_than_memory
------------------------------

    .. py:attribute:: allow_more_records_than_memory

        Specifies whether to allow the device to acquire more records than can fit in the device memory of the PXIe-5622/5624.

        ----
        **Note**
        If you set the property to FALSE and attempt to acquire more records than can fit into the PXIe-5622/5624 device memory, NI-RFSA returns an error. If this property is set to TRUE, NI-RFSA returns an error only in the event of an acquisition buffer overflow.

        ----

        ----
        **Note**
        This property is always set to True for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841.

        ----

        **Default Value**: False

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +-------+------------------------------------------------------------------------+
        | Name  | Description                                                            |
        +=======+========================================================================+
        | True  | Allows acquisition of more records than fit in device memory.          |
        +-------+------------------------------------------------------------------------+
        | False | Does not allow acquisitions of more records than fit in device memory. |
        +-------+------------------------------------------------------------------------+

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

                - LabVIEW Property: **Acquisition:IQ:Allow More Records Than Memory**
                - C Attribute: **NIRFSA_ATTR_ALLOW_MORE_RECORDS_THAN_MEMORY**

allow_out_of_specification_user_settings
----------------------------------------

    .. py:attribute:: allow_out_of_specification_user_settings

        Enables or disables warnings and errors when you set frequency, power, or bandwidth values beyond the limits of the NI-RFSA device specifications.

        When you set this property to :py:data:`~nirfsa.AllowOutOfSpecificationUserSettings.ENABLED`, the driver does not report out-of-specification warnings and errors.

        **Default Value**: :py:data:`~nirfsa.AllowOutOfSpecificationUserSettings.DISABLED`

        **Supported Devices:** PXIe-5820/5830/5831/5840/5841/5842/5860

        **Defined Values**:

        +-----------------------------------------------------------------+----------------------------------------------+
        | Name                                                            | Description                                  |
        +=================================================================+==============================================+
        | :py:data:`~nirfsa.AllowOutOfSpecificationUserSettings.DISABLED` | Disables out-of-specification user settings. |
        +-----------------------------------------------------------------+----------------------------------------------+
        | :py:data:`~nirfsa.AllowOutOfSpecificationUserSettings.ENABLED`  | Enables out-of-specification user settings.  |
        +-----------------------------------------------------------------+----------------------------------------------+

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

                - LabVIEW Property: **Acquisition:Advanced:Allow Out Of Specification User Settings**
                - C Attribute: **NIRFSA_ATTR_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS**

amplitude_settling
------------------

    .. py:attribute:: amplitude_settling

        Configures the amplitude settling accuracy in decibels.

        NI-RFSA waits until the RF power settles within the specified accuracy level after calling the :py:meth:`nirfsa.Session._initiate` method.

        Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.

        **Units**: dB

        **Default Value:** 0.5

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

                - LabVIEW Property: **Vertical:Advanced:Amplitude Settling**
                - C Attribute: **NIRFSA_ATTR_AMPLITUDE_SETTLING**

arm_ref_trigger_type
--------------------

    .. py:attribute:: arm_ref_trigger_type

        Specifies whether you want the Arm Reference Trigger to be a digital edge or software trigger.

        ----
        **Note**
        The PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841 only support :py:data:`~nirfsa.ArmReferenceTriggerType.NONE`.

        ----

        ----
        **Note**
        Set this property to :py:data:`~nirfsa.ArmReferenceTriggerType.NONE` if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` or if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the :py:meth:`nirfsa.Session.ConfigureAcquisitionType` method.

        ----

        **Default Value**: :py:data:`~nirfsa.ArmReferenceTriggerType.NONE`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                     | Description                                                                                                                                                                                                                                                                          |
        +==========================================================+======================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ArmReferenceTriggerType.NONE`          | No Arm Reference Trigger is configured.                                                                                                                                                                                                                                              |
        +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ArmReferenceTriggerType.DIGITAL_EDGE`  | The Arm Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the :py:attr:`nirfsa.Session.digital_edge_arm_ref_trigger_source` property.                                                                             |
        +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ArmReferenceTriggerType.SOFTWARE_EDGE` | The Arm Reference Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the :py:meth:`nirfsa.Session.send_software_edge_trigger` method and selecting :py:data:`~nirfsa.SoftwareTriggerType.ARM_REF` as the **trigger** parameter. |
        +----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------+
            | Characteristic        | Value                         |
            +=======================+===============================+
            | Datatype              | enums.ArmReferenceTriggerType |
            +-----------------------+-------------------------------+
            | Permissions           | read-write                    |
            +-----------------------+-------------------------------+
            | Repeated Capabilities | None                          |
            +-----------------------+-------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Arm Ref:Type**
                - C Attribute: **NIRFSA_ATTR_ARM_REF_TRIGGER_TYPE**

attenuation
-----------

    .. py:attribute:: attenuation

        Specifies the nominal attenuation setting, in dB, for all attenuators before the first mixer in the RF signal chain.

        If you do not set this property, NI-RFSA automatically chooses an attenuation setting based on the reference level you configure. The valid values for this property depend on the device configuration.

        **PXI-5600/5661**: You can change the attenuation value to modify the amount of noise and distortion. Higher attenuation levels increase the noise level while decreasing distortion; lower attenuation levels decrease the noise level while increasing distortion.

        **PXIe-5601/5663/5663E**: You can change the attenuation value and the value of the :py:attr:`nirfsa.Session.if_attenuation` property to modify the amount of noise and distortion. Higher attenuation levels increase the noise level while decreasing distortion; lower attenuation levels decrease the noise level while increasing distortion.

        **PXIe-5603/5605/5606/5665/5668**: You can set multiple properties to modify the attenuation values for the device. Refer to `PXIe-5665 RF Attenuation and Signal Levels <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/attenuation-and-signal-levels.html>`_ for more information about configuring attenuation.

        **PXIe-5667**: This property specifies the nominal attenuation setting for all attenuators before the first RF mixer in the input signal path. This property is read-only when the :py:attr:`nirfsa.Session.LOW_FREQUENCY_BYPASS_ENABLED` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`.

        **PXIe-5693**: This property is read-only and returns the nominal RF attenuation of the PXIe-5693.

        **Units**: dB

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693



        .. note:: One or more of the referenced properties are not in the Python API for this driver.

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

                - LabVIEW Property: **Vertical:Advanced:RF Attenuation (dB)**
                - C Attribute: **NIRFSA_ATTR_ATTENUATION**

available_paths
---------------

    .. py:attribute:: available_paths

        Returns a comma separated list of the configurable paths available for use based on your instrument configuration.

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | list of str |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | None        |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Available Paths**
                - C Attribute: **NIRFSA_ATTR_AVAILABLE_PATHS**

available_ports
---------------

    .. py:attribute:: available_ports

        Returns a comma-separated list of the available ports for use based on your instrument configuration.

        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | list of str |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | None        |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Available Ports**
                - C Attribute: **NIRFSA_ATTR_AVAILABLE_PORTS**

center_frequency
----------------

    .. py:attribute:: center_frequency

        Specifies the center frequency in a spectrum acquisition.

        The value is expressed in hertz (Hz). An acquisition consists of a span of data surrounding the center frequency.

        ----
        **Note**
        Use this property to tune the downconverter when using external digitizer mode.

        ----

        **Units**: hertz (Hz)

        **Default Values**:

        **PXIe-5694**: 193.6 MHz

        **PXIe-5820**: 0 Hz

        **PXIe-5830/5831/5832**: 6.5 GHz

        **All other devices**: 1 GHz

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Acquisition:Spectrum:Center Frequency**
                - C Attribute: **NIRFSA_ATTR_CENTER_FREQUENCY**

channel_coupling
----------------

    .. py:attribute:: channel_coupling

        Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter.

        ----
        **Note**
        For the PXIe-5605/5606/5665/5667/5668, this property must be set to :py:data:`~nirfsa.ChannelCoupling.AC` when the DC block is present and set to :py:data:`~nirfsa.ChannelCoupling.DC` when the DC block is not present to ensure device specifications are met and proper calibration data is used. For more information about removing or attaching the DC block, refer to the `PXIe-5665 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/block-diagram.2.html>`_, the `PXIe-5605 Front Panel and LEDs <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/pinout.4.html>`_, the `PXIe-5667 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5667-feature/page/block-diagram.html>`_, or the `PXIe-5668 Block Diagram <https://www.ni.com/docs/en-US/bundle/pxie-5668-feature/page/block-diagram.html>`_ topics in this help file.

        ----

        **Valid Values**:

        **PXIe-5603/5665 (3.6 GHz)**: :py:data:`~nirfsa.ChannelCoupling.AC`, :py:data:`~nirfsa.ChannelCoupling.DC`

        **PXIe-5605/5665 (14 GHz)**: :py:data:`~nirfsa.ChannelCoupling.AC`, :py:data:`~nirfsa.ChannelCoupling.DC`

        **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low-frequency bypass path**: :py:data:`~nirfsa.ChannelCoupling.AC`, :py:data:`~nirfsa.ChannelCoupling.DC`

        **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**: :py:data:`~nirfsa.ChannelCoupling.AC`

        **PXIe-5667 (7 GHz)**: :py:data:`~nirfsa.ChannelCoupling.AC`

        **PXIe-5606/5668**: :py:data:`~nirfsa.ChannelCoupling.AC`, :py:data:`~nirfsa.ChannelCoupling.DC`

        **Default Value**: :py:data:`~nirfsa.ChannelCoupling.AC`

        **Supported Devices**: PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668

        **Defined Values**:

        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                  | Description                                                                                                                                                |
        +=======================================+============================================================================================================================================================+
        | :py:data:`~nirfsa.ChannelCoupling.AC` | Specifies that the RF input channel is AC-coupled. For low frequencies (<10 MHz), accuracy decreases because NI-RFSA does not calibrate the configuration. |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ChannelCoupling.DC` | Specifies that the RF input channel is DC-coupled. NI-RFSA enforces a minimum RF attenuation for device protection.                                        |
        +---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.ChannelCoupling |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:NI 5665/5667/5668R:Channel Coupling**
                - C Attribute: **NIRFSA_ATTR_CHANNEL_COUPLING**

common_mode_level
-----------------

    .. py:attribute:: common_mode_level

        Specifies the common-mode level presented at each differential input terminal.

        Common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT).

        **Units**: volts

        **Default Value**: 0 V

        **Supported Devices**: PXIe-5820

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

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ In Port:Common Mode Level**
                - C Attribute: **NIRFSA_ATTR_COMMON_MODE_LEVEL**

deembedding_compensation_gain
-----------------------------

    .. py:attribute:: deembedding_compensation_gain

        Returns the de-embedding gain applied to compensate for the mismatch on the specified port. Use the Active Channel property to specify the name of the port to configure for de-embedding.

        If de-embedding is enabled, NI-RFSA uses the returned compensation gain to remove the effects of the external network between the instrument and the DUT.

        **Supported Devices**: PXIe-5830/5831/5840/5841/5842/5860

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

                - LabVIEW Property: **De-embedding:Compensation Gain**
                - C Attribute: **NIRFSA_ATTR_DEEMBEDDING_COMPENSATION_GAIN**

deembedding_selected_table
--------------------------

    .. py:attribute:: deembedding_selected_table

        Selects the de-embedding table to apply to the measurements on the specified port.

        To use this property, you must use the channelName parameter of the :py:meth:`nirfsa.Session._set_attribute_vi_string` method to specify the name of the port to configure for de-embedding.

        If de-embedding is enabled, NI-RFSA uses the specified table to remove the effects of the external network between the instrument and the DUT.

        Use the :py:meth:`nirfsa.Session._create_deembedding_sparameter_table_array` method to create tables.

        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860




        .. tip:: This property can be set/get on specific ports within your :py:class:`nirfsa.Session` instance.
            Use Python index notation on the repeated capabilities container ports to specify a subset.

            Example: :py:attr:`my_session.ports[ ... ].deembedding_selected_table`

            To set/get on all ports, you can call the property directly on the :py:class:`nirfsa.Session`.

            Example: :py:attr:`my_session.deembedding_selected_table`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | ports      |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **De-embedding:Selected Table**
                - C Attribute: **NIRFSA_ATTR_DEEMBEDDING_SELECTED_TABLE**

deembedding_type
----------------

    .. py:attribute:: deembedding_type

        Specifies the type of de-embedding to apply to measurements on the specified port.

        To use this property, you must use the channelName parameter of the :py:meth:`nirfsa.Session._set_attribute_vi_int32` method to specify the name of the port to configure for de-embedding.

        If you set this property to any value besides :py:data:`~nirfsa.DeembeddingType.NONE`, NI-RFSA adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT.

        **Default Value**: :py:data:`~nirfsa.DeembeddingType.SCALAR`

        **Valid Values for PXIe-5830/5832/5840/5841** : :py:data:`~nirfsa.DeembeddingType.NONE` or :py:data:`~nirfsa.DeembeddingType.SCALAR`

        **Valid Values for PXIe-5842/5860** : :py:data:`~nirfsa.DeembeddingType.NONE` or :py:data:`~nirfsa.DeembeddingType.SCALAR` or :py:data:`~nirfsa.NIRFSA_VAL_DEEMBEDDING_TYPE_AMPLITUDE_FLATNESS` or :py:data:`~nirfsa.NIRFSA_VAL_DEEMBEDDING_TYPE_AMPLITUDE_AND_PHASE_FLATNESS`

        **Valid Values for PXIe-5831:** :py:data:`~nirfsa.DeembeddingType.NONE`, :py:data:`~nirfsa.DeembeddingType.SCALAR`, or :py:data:`~nirfsa.DeembeddingType.VECTOR`. :py:data:`~nirfsa.DeembeddingType.VECTOR` is only supported for TRX Ports in a Semiconductor Test System (STS).

        **Supported Devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +-------------------------------------------+------------------------------------------------------------------------+
        | Name                                      | Description                                                            |
        +===========================================+========================================================================+
        | :py:data:`~nirfsa.DeembeddingType.NONE`   | De-embedding is not applied to the measurement.                        |
        +-------------------------------------------+------------------------------------------------------------------------+
        | :py:data:`~nirfsa.DeembeddingType.SCALAR` | De-embeds the measurement using only the gain term.                    |
        +-------------------------------------------+------------------------------------------------------------------------+
        | :py:data:`~nirfsa.DeembeddingType.VECTOR` | De-embeds the measurement using the gain term and the reflection term. |
        +-------------------------------------------+------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific ports within your :py:class:`nirfsa.Session` instance.
            Use Python index notation on the repeated capabilities container ports to specify a subset.

            Example: :py:attr:`my_session.ports[ ... ].deembedding_type`

            To set/get on all ports, you can call the property directly on the :py:class:`nirfsa.Session`.

            Example: :py:attr:`my_session.deembedding_type`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.DeembeddingType |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | ports                 |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **De-embedding:Type**
                - C Attribute: **NIRFSA_ATTR_DEEMBEDDING_TYPE**

device_configuration_temperature
--------------------------------

    .. py:attribute:: device_configuration_temperature

        Specifies the temperature, in degrees Celsius, that NI-RFSA uses to calculate the device configuration settings.

        ----
        **Note**
        For most applications, you can choose not to set this property, so NI-RFSA uses the device temperature to calculate best attenuation settings. Set this property only if you want NI-RFSA to maintain the same device configuration settings from acquisition to acquisition, independent of device temperature changes.

        ----

        **PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: This property is read-only.

        **Units**: degrees Celsius

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Vertical:Advanced:Device Configuration Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_DEVICE_CONFIGURATION_TEMPERATURE**

device_instantaneous_bandwidth
------------------------------

    .. py:attribute:: device_instantaneous_bandwidth

        Specifies the instantaneous bandwidth of the device in hertz (Hz).

        The instantaneous bandwidth is the effective real-time bandwidth of the signal path for your configuration.

        Specify the maximum instantaneous bandwidth needed for your measurement. NI-RFSA coerces the actual IF filter to use based on other measurement constraints such as the :py:attr:`nirfsa.Session.if_filter_bandwidth` property and the :py:attr:`nirfsa.Session.digital_if_equalization_enabled` property.

        To change the value that NI-RFSA uses for the maximum size of multispan acquisition subspans, use the :py:attr:`nirfsa.Session.fft_width` property.

        ----
        **Note**
        If your application uses the PXIe-5622 IF digitizer, your maximum device instantaneous bandwidth is constrained to 50 MHz or 25 MHz, depending on the digitizer option you purchased. If your application uses the PXIe-5624 digitizer, your maximum device instantaneous bandwidth is constrained by the hardware option you purchased and your FPGA image.

        ----

        **PXI-5661**: The PXI-5600 RF downconverter instantaneous bandwidth is 20 MHz.

        **PXIe-5663/5663E**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the `PXIe-5601 RF Signal Downconverter Overview <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/overview.3.html>`_ for more information about instantaneous bandwidth.

        ----
        **Note**
        For the PXIe-5663/5663E, NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the instantaneous bandwidth for frequencies above 120 MHz is different than the instantaneous bandwidth for frequencies less than 120 MHz, which are 20 MHz and 10 MHz respectively.

        ----

        **PXIe-5665**: Your maximum allowed instantaneous bandwidth is independent of the downconverter center frequency. Refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth.

        **PXIe-5665 (14 GHz), PXIe-5668**: If you have enabled the preselector for the PXIe-5605/5606, the device instantaneous bandwidth value is only a typical specification. For multispan acquisitions, NI-RFSA uses this typical specification as the maximum size for the acquisition subspans.

        ----
        **Note**
        When used with an external digitizer, the PXIe-5603 and the low band signal path of the PXIe-5605 provide a nominal 80 MHz bandwidth at   dB. At frequencies greater than 3.6 GHz, the PXIe-5605 provides a typical bandwidth of 47 MHz at   dB with the preselector (YIG-tuned filter) enabled.

        ----

        ----
        **Note**
        For PXIe-5606 devices, the 765 MHz IF filter is available only at center frequencies above 3.6 GHz.

        ----

        **PXIe-5693**: This property is read-only for the PXIe-5693. The value for the device instantaneous bandwidth depends on the value for the RF preselector filter.

        **PXIe-5694/PXIe-5667**: If your application uses the PXIe-5694 as part of an PXIe-5667 spectrum monitoring receiver or the PXIe-5694 as a stand-alone device, NI-RFSA determines the appropriate IF filter to use based on the value that you set for this property.

        ----
        **Note**

        ----

        **PXIe-5644/5645/5646**: This property is read-only for the PXIe-5644/5645/5646. Refer to the specifications document for your device for more information about instantaneous bandwidth.

        **PXIe-5840/5841/5860**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use. Refer to the *PXIe-5840/5841/5860 Specifications* for more information about instantaneous bandwidth. Set this property to select different device instantaneous bandwidths for a given downconverter center frequency. The device instantaneous bandwidth that you select is greater than or equal to the requested instantaneous bandwidth. If this property is not set, NI-RFSA uses the maximum allowed instantaneous bandwidth.

        **PXIe-5842**: Your maximum allowed instantaneous bandwidth depends on the device's hardware options, configured device personality, and the downconverter center frequency you use. Refer to the *PXIe-5842 Specifications* for more information about instantaneous bandwidth. Set this property to select different device instantaneous bandwidths for a given downconverter center frequency. The device instantaneous bandwidth that you select is greater than or equal to the requested instantaneous bandwidth. If this property is not set, NI-RFSA uses the maximum allowed instantaneous bandwidth.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-selection.html>`_

        `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-selection.html>`_

        `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-selection.html>`_

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

                - LabVIEW Property: **Acquisition:Device Instantaneous Bandwidth (Hz)**
                - C Attribute: **NIRFSA_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH**

device_temperature
------------------

    .. py:attribute:: device_temperature

        Returns the current temperature, in degrees Celsius, of the module.

        **PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: If you query this property during RF list mode, list steps may take longer to complete during list execution.

        **PXIe-5830/5831/5832**: To use this property, you must first set the channelName parameter of the :py:meth:`nirfsa.Session._set_attribute_vi_real64` method to using the appropriate string for your instrument configuration. Setting the :py:meth:`nirfsa.Session._set_attribute_vi_real64` property is not required for the PXIe-3621/3622. Refer to the following table to determine which strings are valid for your configuration.

        **Units**: degrees Celcius

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        +--------------------------------+---------------------------+---------------------------+
        | Hardware Module                | TRX Port Type             | Active Channel String     |
        +================================+===========================+===========================+
        | PXIe-3621/3622/5842            | -                         | if or "" (empty string)   |
        +--------------------------------+---------------------------+---------------------------+
        | PXIe-5820                      | -                         | fpga                      |
        +--------------------------------+---------------------------+---------------------------+
        | PXIe-5860                      | -                         | 5860 or "" (empty string) |
        +--------------------------------+---------------------------+---------------------------+
        | First connected mmRH-5582      | DIRECT TRX PORTS Only     | rf0                       |
        +--------------------------------+---------------------------+---------------------------+
        | First connected mmRH-5582      | SWITCHED TRX PORTS [0-7]  | rf0switch0                |
        +--------------------------------+---------------------------+---------------------------+
        | First connected mmRH-5582      | SWITCHED TRX PORTS [8-15] | rf0switch1                |
        +--------------------------------+---------------------------+---------------------------+
        | Second connected mmRH-5582     | DIRECT TRX PORTS Only     | rf1                       |
        +--------------------------------+---------------------------+---------------------------+
        | Second connected mmRH-5582     | SWITCHED TRX PORTS [0-7]  | rf1switch0                |
        +--------------------------------+---------------------------+---------------------------+
        | Second connected mmRH-5582     | SWITCHED TRX PORTS [8-15] | rf1switch1                |
        +--------------------------------+---------------------------+---------------------------+
        | First connected RMM-5544/5546  | -                         | rmm0                      |
        +--------------------------------+---------------------------+---------------------------+
        | Second connected RMM-5544/5546 | -                         | rmm1                      |
        +--------------------------------+---------------------------+---------------------------+


        .. tip:: This property can be set/get on specific device_temperatures within your :py:class:`nirfsa.Session` instance.
            Use Python index notation on the repeated capabilities container device_temperatures to specify a subset.

            Example: :py:attr:`my_session.device_temperatures[ ... ].device_temperature`

            To set/get on all device_temperatures, you can call the property directly on the :py:class:`nirfsa.Session`.

            Example: :py:attr:`my_session.device_temperature`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | float               |
            +-----------------------+---------------------+
            | Permissions           | read only           |
            +-----------------------+---------------------+
            | Repeated Capabilities | device_temperatures |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Characteristics:Device Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_DEVICE_TEMPERATURE**

digital_edge_advance_trigger_source
-----------------------------------

    .. py:attribute:: digital_edge_advance_trigger_source

        Specifies the source terminal for the Advance Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.advance_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_digital_edge_ref_trigger`

        **Defined Values**:

        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                        | Description                                                                                                                                                                                                     |
        +=============================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.NIRFSA_VAL_DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PFI1`          | The trigger is received on the PFI 1.                                                                                                                                                                           |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG0`     | The trigger is received on the PXI trigger line 0.                                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG1`     | The trigger is received on the PXI trigger line 1.                                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG2`     | The trigger is received on the PXI trigger line 2.                                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG3`     | The trigger is received on the PXI trigger line 3.                                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG4`     | The trigger is received on the PXI trigger line 4.                                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG5`     | The trigger is received on the PXI trigger line 5.                                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG6`     | The trigger is received on the PXI trigger line 6.                                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG7`     | The trigger is received on the PXI trigger line 7.                                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.OutputTerm.PXIE_DSTARB`   | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.OutputTerm.TIMER_EVENT`   | The trigger is received from the Timer Event. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841, and for digital edge Advance Triggers on the PXIe-5663E/5665.                                 |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

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

                - LabVIEW Property: **Triggers:Advance:Digital Edge:Source**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE**

digital_edge_arm_ref_trigger_source
-----------------------------------

    .. py:attribute:: digital_edge_arm_ref_trigger_source

        Specifies the source terminal for the digital edge Arm Reference Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.arm_ref_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

        **Default Value**: "" (empty string)

        ----
        **Note**
        The PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841 devices only support "" (empty string).

        The trigger is received on PFI0 from the front panel DIO terminal.

        The trigger is received on PFI1 from the front panel DIO terminal.

        The trigger is received on PFI2 from the front panel DIO terminal.

        The trigger is received on PFI3 from the front panel DIO terminal.

        The trigger is received on PFI4 from the front panel DIO terminal.

        The trigger is received on PFI5 from the front panel DIO terminal.

        The trigger is received on PFI6 from the front panel DIO terminal.

        The trigger is received on PFI7 from the front panel DIO terminal.

        ----

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5820/5830/5831/5832/5840/5841

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **Defined Values**:

        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                        | Description                                                                                                                                                                                                     |
        +=============================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.NIRFSA_VAL_DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PFI1`          | The trigger is received on PFI 1.                                                                                                                                                                               |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG0`     | The trigger is received on PXI trigger line 0.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG1`     | The trigger is received on PXI trigger line 1.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG2`     | The trigger is received on PXI trigger line 2.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG3`     | The trigger is received on PXI trigger line 3.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG4`     | The trigger is received on PXI trigger line 4.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG5`     | The trigger is received on PXI trigger line 5.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG6`     | The trigger is received on PXI trigger line 6.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG7`     | The trigger is received on PXI trigger line 7.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.OutputTerm.PXIE_DSTARB`   | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.OutputTerm.TIMER_EVENT`   | The trigger is received from the Timer Event. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841, and for digital edge Advance Triggers on the PXIe-5663E/5665.                                 |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

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

                - LabVIEW Property: **Triggers:Arm Ref:Digital Edge:Source**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_ARM_REF_TRIGGER_SOURCE**

digital_edge_ref_trigger_edge
-----------------------------

    .. py:attribute:: digital_edge_ref_trigger_edge

        Specifies the active edge for the Reference Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.ref_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

        **Default Value**: :py:data:`~nirfsa.ReferenceTriggerDigitalEdgeEdge.RISING`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_digital_edge_ref_trigger`

        **Defined Values**:

        +------------------------------------------------------------+-------------------------------------------------------+
        | Name                                                       | Description                                           |
        +============================================================+=======================================================+
        | :py:data:`~nirfsa.ReferenceTriggerDigitalEdgeEdge.RISING`  | The trigger asserts on the rising edge of the signal. |
        +------------------------------------------------------------+-------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceTriggerDigitalEdgeEdge.FALLING` | The trigger asserts on the falling edge of the signal |
        +------------------------------------------------------------+-------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------------+
            | Characteristic        | Value                                 |
            +=======================+=======================================+
            | Datatype              | enums.ReferenceTriggerDigitalEdgeEdge |
            +-----------------------+---------------------------------------+
            | Permissions           | read-write                            |
            +-----------------------+---------------------------------------+
            | Repeated Capabilities | None                                  |
            +-----------------------+---------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Digital Edge:Edge**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_EDGE**

digital_edge_ref_trigger_source
-------------------------------

    .. py:attribute:: digital_edge_ref_trigger_source

        Specifies the source terminal for the digital edge Reference Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.ref_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **Defined Values**:

        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                        | Description                                                                                                                                                                                                     |
        +=============================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.NIRFSA_VAL_DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PFI1`          | The trigger is received on PFI 1.                                                                                                                                                                               |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG0`     | The trigger is received on PXI trigger line 0.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG1`     | The trigger is received on PXI trigger line 1.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG2`     | The trigger is received on PXI trigger line 2.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG3`     | The trigger is received on PXI trigger line 3.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG4`     | The trigger is received on PXI trigger line 4.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG5`     | The trigger is received on PXI trigger line 5.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG6`     | The trigger is received on PXI trigger line 6.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG7`     | The trigger is received on PXI trigger line 7.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.OutputTerm.PXIE_DSTARB`   | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.OutputTerm.TIMER_EVENT`   | The trigger is received from the Timer Event. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841, and for digital edge Advance Triggers on the PXIe-5663E/5665.                                 |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

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

                - LabVIEW Property: **Triggers:Ref:Digital Edge:Source**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE**

digital_edge_start_trigger_edge
-------------------------------

    .. py:attribute:: digital_edge_start_trigger_edge

        Specifies the active edge for the Start Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.start_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

        **Default Value**: :py:data:`~nirfsa.StartTriggerDigitalEdgeEdge.RISING`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_digital_edge_start_trigger`

        **Defined and Valid Values:**

        +--------------------------------------------------------+-------------------------------------------------------+-------------------------------------+
        | Name                                                   | Description                                           | Valid For                           |
        +========================================================+=======================================================+=====================================+
        | :py:data:`~nirfsa.StartTriggerDigitalEdgeEdge.RISING`  | The trigger asserts on the rising edge of the signal. | PXI-5661, PXIe-5663/5663E/5665/5668 |
        +--------------------------------------------------------+-------------------------------------------------------+-------------------------------------+
        | :py:data:`~nirfsa.StartTriggerDigitalEdgeEdge.FALLING` | The trigger asserts on the falling edge of the signal | PXIe-5668                           |
        +--------------------------------------------------------+-------------------------------------------------------+-------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------------+
            | Characteristic        | Value                             |
            +=======================+===================================+
            | Datatype              | enums.StartTriggerDigitalEdgeEdge |
            +-----------------------+-----------------------------------+
            | Permissions           | read-write                        |
            +-----------------------+-----------------------------------+
            | Repeated Capabilities | None                              |
            +-----------------------+-----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Digital Edge:Edge**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

digital_edge_start_trigger_source
---------------------------------

    .. py:attribute:: digital_edge_start_trigger_source

        Specifies the source terminal for the Start Trigger.

        This property is used only when the :py:attr:`nirfsa.Session.start_trigger_type` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DIGITAL_EDGE`.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_digital_edge_start_trigger`

        **Defined Values**:

        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                        | Description                                                                                                                                                                                                     |
        +=============================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.NIRFSA_VAL_DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PFI1`          | The trigger is received on PFI 1.                                                                                                                                                                               |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG0`     | The trigger is received on PXI trigger line 0.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG1`     | The trigger is received on PXI trigger line 1.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG2`     | The trigger is received on PXI trigger line 2.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG3`     | The trigger is received on PXI trigger line 3.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG4`     | The trigger is received on PXI trigger line 4.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG5`     | The trigger is received on PXI trigger line 5.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG6`     | The trigger is received on PXI trigger line 6.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_TRIG7`     | The trigger is received on PXI trigger line 7.                                                                                                                                                                  |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.OutputTerm.PXIE_DSTARB`   | The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.OutputTerm.TIMER_EVENT`   | The trigger is received from the Timer Event. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841, and for digital edge Advance Triggers on the PXIe-5663E/5665.                                 |
        +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

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

                - LabVIEW Property: **Triggers:Start:Digital Edge:Source**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE**

digital_gain
------------

    .. py:attribute:: digital_gain

        Specifies the scaling factor applied to the time-domain voltage data in the digitizer.

        NI-RFSA does not compensate for the specified digital gain.

        You can use this property to account for external gain changes without changing the analog signal path.

        ----
        **Note**
        The PXIe-5644/5645/5646 applies this gain when the data is scaled. The raw data does not include this scaling on these devices.

        ----

        **Units:** dB

        **Default Value:** 0 dB

        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Vertical:Advanced:Digital Gain (dB)**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_GAIN**

digital_if_equalization_enabled
-------------------------------

    .. py:attribute:: digital_if_equalization_enabled

        Enables use of the digital equalization filter for the RF downconverter.

        **PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: The only valid value for this property is True.

        ----
        **Note**
        For PXIe-5665/5667 devices, digital IF equalization is supported only with a 150 MHz clock. You cannot set this property to True if the :py:attr:`nirfsa.Session.digitizer_sample_clock_timebase_source` property is set to :py:data:`~nirfsa.DigitizerSampleClockTimebaseSource.LO_REF_CLK`.

        ----

        ----
        **Note**
        For the PXIe-5665 (14 GHz)/5667 (7 GHz)/5668, the preselector is not part of the IF filter path, so NI-RFSA does not equalize the preselector distortions.

        ----

        **Default Value**: True, if the device configuration is supported.

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841

        **Defined Values**:

        +-------+-----------------------------------------------------------+
        | Name  | Description                                               |
        +=======+===========================================================+
        | True  | Enables digital IF equalization on the RF downconverter.  |
        +-------+-----------------------------------------------------------+
        | False | Disables digital IF equalization on the RF downconverter. |
        +-------+-----------------------------------------------------------+

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

                - LabVIEW Property: **Signal Path:Digital IF Equalization Enabled**
                - C Attribute: **NIRFSA_ATTR_DIGITAL_IF_EQUALIZATION_ENABLED**

digitizer_dither_enabled
------------------------

    .. py:attribute:: digitizer_dither_enabled

        Specifies whether dithering is enabled on the digitizer.

        Dithering adds band-limited noise in the analog signal path to help reduce the quantization effects of the A/D converter and improve spectral performance. On the PXIe-5622, this out-of-band noise is added at low frequencies up to approximately 12 MHz. On the PXIe-5624, this out-of-band noise is added at low frequencies up to approximately 50 MHz.

        **PXIe-5663/5663E/5665/5667**: When you enable dithering, the maximum signal level is reduced by up to 3 dB. This signal level reduction is accounted for in the nominal input ranges of the PXIe-5622. Therefore, you can overrange the input by up to 3 dB with dither disabled. For example, the +4 dBm input range can handle signal levels up to +7 dBm with dither disabled. For wider bandwidth acquisitions, such as 40 MHz, disable dithering to eliminate residual leakage of the dither signal into the lower frequencies of the IF passband, which starts at 12.5 MHz and ends at 62.5 MHz. This leakage can slightly raise the noise floor in the lower frequencies, thus degrading the performance in high-sensitivity applications. When taking spectral measurements, this leakage can also appear as a wide, low-amplitude signal near 12.5 MHz and 62.5 MHz. The width and amplitude of the signal depends on your resolution bandwidth and the type of time-domain window you apply to your FFT.

        **PXIe-5668**: When you enable dithering, the maximum signal level is reduced by up to 2 dB. For the PXIe-5624, the maximum input power with dither off is 8 dBm and the maximum input power with dither on is 6 dBm. When acquiring an 800 MHz bandwidth signal, the I/Q data contains the dither even if the dither signal is not in the displayed spectrum. The dither can affect actions like power level triggering.

        ----
        **Note**
        For the PXIe-5668, disabling dithering can negatively affect absolute amplitude accuracy.

        ----

        ----
        **Note**
        For the PXIe-5820/5830/5831/5832/5840/5841/5842, only :py:data:`~nirfsa.DigitizerDitherEnabled.ENABLED` is supported.

        ----

        **Default Value**: :py:data:`~nirfsa.DigitizerDitherEnabled.ENABLED`

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        **Defined Values**:

        +----------------------------------------------------+-----------------------------------+
        | Name                                               | Description                       |
        +====================================================+===================================+
        | :py:data:`~nirfsa.DigitizerDitherEnabled.DISABLED` | Disables dither on the digitizer. |
        +----------------------------------------------------+-----------------------------------+
        | :py:data:`~nirfsa.DigitizerDitherEnabled.ENABLED`  | Enables dither on the digitizer.  |
        +----------------------------------------------------+-----------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------+
            | Characteristic        | Value                        |
            +=======================+==============================+
            | Datatype              | enums.DigitizerDitherEnabled |
            +-----------------------+------------------------------+
            | Permissions           | read-write                   |
            +-----------------------+------------------------------+
            | Repeated Capabilities | None                         |
            +-----------------------+------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Digitizer Dither Enabled**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_DITHER_ENABLED**

digitizer_sample_clock_rate
---------------------------

    .. py:attribute:: digitizer_sample_clock_rate

        Returns the actual frequency, in hertz (Hz), of the digitizer Sample Clock.

        **Units**: hertz (Hz)

        **Supported Devices**: PXIe-5668

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

                - LabVIEW Property: **Clocking:Digitizer Sample Clock Rate**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_RATE**

digitizer_sample_clock_timebase_rate
------------------------------------

    .. py:attribute:: digitizer_sample_clock_timebase_rate

        Specifies the frequency, in hertz (Hz), of the external clock used as the timebase source if you set the :py:attr:`nirfsa.Session.digitizer_sample_clock_timebase_source` property to an external source, such as :py:data:`~nirfsa.NIRFSA_VAL_CLK_IN`, :py:data:`~nirfsa.DigitizerSampleClockTimebaseSource.LO_REF_CLK`, or :py:data:`~nirfsa.DigitizerSampleClockTimebaseSource.DOWNCONVERTER_LO2_OUT`

        **PXI-5661**If this property is set to a value less than 60 MHz, signals at frequencies just above the 20 MHz passband of the downconverter may be aliased back into the passband. This aliasing occurs because the IF frequency of the downconverter is 15 MHz, and the upper end of the passband is 25 MHz. At sampling rates below 60 MHz, the Nyquist frequency is close to the end of the passband and creates aliases that are not filtered effectively by the downconverter.

        **Units**: hertz (Hz)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668

        **Valid and Default Values**:

        +---------------------------+----------------------------+---------------+
        | Device                    | Valid Values               | Default Value |
        +===========================+============================+===============+
        | PXI-5661                  | Any frequency 226552.5 MHz | 100 MHz       |
        +---------------------------+----------------------------+---------------+
        | PXIe-5663/5663E/5665/5667 | 150 MHz                    | 150 MHz       |
        +---------------------------+----------------------------+---------------+
        | PXIe-5668                 | 2 GHz                      | 2 GHz         |
        +---------------------------+----------------------------+---------------+

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

                - LabVIEW Property: **Clocking:Digitizer Sample Clock Timebase Rate**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_RATE**

digitizer_sample_clock_timebase_source
--------------------------------------

    .. py:attribute:: digitizer_sample_clock_timebase_source

        Specifies the source of the Sample Clock timebase, which is the timebase used to control waveform sampling.

        **Default Value**: :py:data:`~nirfsa.DigitizerSampleClockTimebaseSource.ONBOARD_CLOCK`

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668

        **Defined Values**:

        +-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                                        | Description                                                                                                                                                            |
        +=============================================================================+========================================================================================================================================================================+
        | :py:data:`~nirfsa.DigitizerSampleClockTimebaseSource.ONBOARD_CLOCK`         | The digitizer uses its onboard clock as the Sample Clock timebase.                                                                                                     |
        +-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.DigitizerSampleClockTimebaseSource.CLK_IN`                | The digitizer uses the signal present on the CLK IN connector as the Sample Clock timebase.                                                                            |
        +-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.DigitizerSampleClockTimebaseSource.LO_REF_CLK`            | The digitizer uses the signal generated on the 100 MHz REF OUT terminal on the PXIe-5653 as the Sample Clock timebase. This value is supported only for the PXIe-5665. |
        +-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.DigitizerSampleClockTimebaseSource.PXI_STAR`              | The digitizer uses the signal present at the PXI star trigger line as the Sample Clock timebase. This value is not supported for the PXIe-5668.                        |
        +-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.DigitizerSampleClockTimebaseSource.DOWNCONVERTER_LO2_OUT` | The digitizer uses the signal present on the LO2 OUT connector on the downconverter as the Sample Clock timebase. This value is supported only for the PXIe-5668.      |
        +-----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------------------+
            | Characteristic        | Value                                    |
            +=======================+==========================================+
            | Datatype              | enums.DigitizerSampleClockTimebaseSource |
            +-----------------------+------------------------------------------+
            | Permissions           | read-write                               |
            +-----------------------+------------------------------------------+
            | Repeated Capabilities | None                                     |
            +-----------------------+------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Digitizer Sample Clock Timebase Source**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_SAMPLE_CLOCK_TIMEBASE_SOURCE**

digitizer_temperature
---------------------

    .. py:attribute:: digitizer_temperature

        Returns the current temperature, in degrees Celsius, of the digitizer module.

        **PXIe-5820/5840/5841/5842**: If you query this property during RF list mode, list steps may take longer to complete during list execution.

        **Default Value**: N/A

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842

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

                - LabVIEW Property: **Device Characteristics:Digitizer Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_TEMPERATURE**

digitizer_vertical_range
------------------------

    .. py:attribute:: digitizer_vertical_range

        Specifies the vertical range of the digitizer.

        The vertical range is defined as the absolute value of the input range for a channel. The default vertical range works for all device configurations, but you can use this property to optimize performance if you know that the signal level at the digitizer input terminal is low.

        ----
        **Note**
        For most applications, NI-RFSA selects an appropriate value for this property.

        ----

        This value is expressed in volts. For example, to acquire a sine wave that spans between 20130.5 V and +0.5 V, set this property to 1.0.

        **PXIe-5840/5841/5842/5860**: This property is read-only.

        **Default Value**: 1.0

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667, PXIe-5840/5841/5842/5860

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

                - LabVIEW Property: **Vertical:Digitizer Vertical Range**
                - C Attribute: **NIRFSA_ATTR_DIGITIZER_VERTICAL_RANGE**

done_event_terminal_name
------------------------

    .. py:attribute:: done_event_terminal_name

        Returns the fully qualified signal name as a string.

        **Default Values**:

        **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>DoneEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

        **PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>DoneEvent</i>, where *ModuleName* is the name of your device in MAX.

        **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>DoneEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

        **All other devices**: /<i>DigitizerName</i>/<i>DoneEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.get_terminal_name`

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

                - LabVIEW Property: **Events:Done:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_DONE_EVENT_TERMINAL_NAME**

downconverter_center_frequency
------------------------------

    .. py:attribute:: downconverter_center_frequency

        Enables in-band retuning and specifies the current frequency, in hertz (Hz), of the RF downconverter.

        If you set this property, any measurements outside the instantaneous bandwidth of the device are invalid. To disable in-band retuning, reset the property or call the :py:meth:`nirfsa.Session.reset_device` method.

        After you set this property, the downconverter is locked to that frequency until the value is changed or the property is reset. Locking the downconverter to a fixed value allows frequencies within the instantaneous bandwidth of the downconverter to be measured with minimal overhead, decreasing tuning time.

        **Valid Values**: Any supported tuning frequency of the device

        **PXIe-5820**: The only valid value for this property is 0 Hz.

        **Default Value**:

        **PXIe-5694**: The default value for the PXIe-5694 is 193.6 MHz unless you set the :py:attr:`nirfsa.Session.signal_conditioning_enabled` property to  :py:data:`~nirfsa.SignalConditioningEnabled.BYPASSED`, in which case the default value is 187.5 MHz.

        **All other devices**: The carrier frequency or spectrum center frequency. NI-RFSA sets this property to the default value based on the value of the :py:attr:`nirfsa.Session.acquisition_type` property.

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842

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

                - LabVIEW Property: **Acquisition:Advanced:Downconverter Center Frequency**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY**

downconverter_frequency_offset
------------------------------

    .. py:attribute:: downconverter_frequency_offset

        Specifies an offset from the I/Q carrier frequency for the downconverter.

        If you set this property, any measurements outside the instantaneous bandwidth of the device are invalid. After you set this property, the RF downconverter is locked to that frequency offset until the value is changed or the property is reset.

        **Valid Values:**

        **PXIe-5646:**: -100 MHz to +100 MHz

        **PXIe-5830/5831/5832/5840/5841:**: -500 MHz to +500 MHz

        **All other devices:**: -42 MHz to +42 MHz

        **Default Values:**: For spectrum acquisition types the driver automatically calculates the default to avoid residual LO power. For I/Q acquisition types the default is 0 Hz. If the center frequency is set to a non-multiple of the :py:attr:`nirfsa.Session.lo_frequency_step_size` property, the :py:attr:`nirfsa.Session.downconverter_frequency_offset` property is set to compensate for the difference.

        **Supported Devices:**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

        **Related Topics**

        `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-selection.html>`_

        `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-selection.html>`_

        `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-selection.html>`_

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

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Acquisition:Advanced:Downconverter Frequency Offset**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET**

downconverter_frequency_offset_mode
-----------------------------------

    .. py:attribute:: downconverter_frequency_offset_mode

        Specifies whether to allow NI-RFSA to select the downconveter frequency offset.

        You can either set an offset yourself or let NI-RFSA select one for you.

        Placing the downconverter center frequency outside the bandwidth of your input signal can help avoid issues such as LO leakage.

        To set an offset yourself, set this property to :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.AUTOMATIC` or :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.USER_DEFINED`, and set either the :py:attr:`nirfsa.Session.downconverter_center_frequency` or the :py:attr:`nirfsa.Session.downconverter_frequency_offset` properties.

        To allow NI-RFSA to automatically select the downconverter frequency offset, set this property to :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.AUTOMATIC` or :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.ENABLED` and configure the :py:attr:`nirfsa.Session.signal_bandwidth` property to describe your expected input signal. The signal bandwidth must be no greater than half the specified value of the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property, minus a device-specific guard band. Do not set the :py:attr:`nirfsa.Session.downconverter_center_frequency` or :py:attr:`nirfsa.Session.downconverter_frequency_offset` properties. If all conditions are met, NI-RFSA places the downconverter center frequency outside the signal bandwidth. Set this property to :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.ENABLED` if you want to receive an error any time NI-RFSA is unable to apply automatic offset.

        When you set an offset yourself or do not use an offset, the reference frequency for gain is near the downconverter center frequency, and :py:attr:`nirfsa.Session.downconverter_frequency_offset_mode` returns :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.USER_DEFINED`. When NI-RFSA automatically sets an offset, the reference frequency for gain is the :py:attr:`nirfsa.Session.iq_carrier_frequency`, and :py:attr:`nirfsa.Session.downconverter_frequency_offset_mode` returns :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.ENABLED`. Refer to the specifications document for your device for more information about gain, flatness, and reference frequencies.

        ----
        **Note**
        Below 120 MHz, the PXIe-5841 does not use an LO and :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.ENABLED` is unavailable. Refer to the *PXIe-5841 Automatic Frequency Offset* topic for more information about using an automatic offset with an external LO.

        ----

        **Default Value:** :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.AUTOMATIC`

        **Supported Devices**: PXIe-5830/5831/5832/5841/5842

        **Related Topics**

        `PXIe-5830 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/automatic-frequency-offset.html>`_

        `PXIe-5831/5832 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/automatic-frequency-offset.html>`_

        `PXIe-5841 Automatic Frequency Offset <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/automatic-frequency-offset.html>`_

        **Defined Values**:

        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                             | Description                                                                                                                                                                                                                                                                                                                  |
        +==================================================================+==============================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.AUTOMATIC`    | NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the :py:attr:`nirfsa.Session.signal_bandwidth` property has been set and can be avoided.                                                                                                                                                |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.ENABLED`      | NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the :py:attr:`nirfsa.Session.signal_bandwidth` property has been set and can be avoided. NI-RFSA returns an error if the :py:attr:`nirfsa.Session.signal_bandwidth` property has not been set, or if the signal bandwidth is too large. |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.DownconverterFrequencyOffsetMode.USER_DEFINED` | NI-RFSA uses the offset that you specified with the :py:attr:`nirfsa.Session.downconverter_frequency_offset` or :py:attr:`nirfsa.Session.downconverter_center_frequency` properties.                                                                                                                                         |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------------+
            | Characteristic        | Value                                  |
            +=======================+========================================+
            | Datatype              | enums.DownconverterFrequencyOffsetMode |
            +-----------------------+----------------------------------------+
            | Permissions           | read-write                             |
            +-----------------------+----------------------------------------+
            | Repeated Capabilities | None                                   |
            +-----------------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Advanced:Downconverter Frequency Offset Mode**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET_MODE**

downconverter_gain
------------------

    .. py:attribute:: downconverter_gain

        Returns the net signal gain for the NI-RFSA device at the current NI-RFSA settings and temperature.

        NI-RFSA scales the acquired I/Q and spectrum data from the digitizer using the value of this property.

        For a vector signal analyzer (VSA), the system is defined as the RF downconverter and all interfaces between the RF IN connector on the RF downconverter front panel and the IF IN connector on the digitizer front panel. For a spectrum monitoring receiver, the system is defined as the RF preselector, RF downconverter, and IF conditioning modules including all interfaces between the RF IN connector on the RF preselector module front panel and the IF IN connector on the digitizer front panel.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Vertical:Downconverter Gain (dB)**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_GAIN**

downconverter_loop_bandwidth
----------------------------

    .. py:attribute:: downconverter_loop_bandwidth

        Configures the loop bandwidth of the RF downconverter tuning PLLs.

        To set this property, the NI-RFSA device must be in the Configuration state.

        **PXI-5600/5661** : For signal bandwidths greater than 10 MHz, :py:data:`~nirfsa.DownconverterLoopBandwidth.WIDE` is the only value supported for this property.

        **PXIe-5601/5663/5663E** : The PXIe-5601 does not support the :py:data:`~nirfsa.DownconverterLoopBandwidth.MEDIUM` value. This property is not supported if you are using an external LO.

        **PXIe-5830/5831/5832/5840/5841/5842** : The PXIe-5840/5841/5842 supports only :py:data:`~nirfsa.DownconverterLoopBandwidth.MEDIUM` for this property. This property is not supported if you are using an external LO.

        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session._set_attribute_vi_int32` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

        **Default Values**:

        **PXI-5600** : :py:data:`~nirfsa.DownconverterLoopBandwidth.WIDE`

        **PXIe-5601** : :py:data:`~nirfsa.DownconverterLoopBandwidth.NARROW`

        **PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842** : :py:data:`~nirfsa.DownconverterLoopBandwidth.MEDIUM`

        **Supported Devices**: PXI-5600, PXIe-5601 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E, PXIe-5830/5831/5832/5840/5841/5842

        **Defined Values**:

        +------------------------------------------------------+-----------------------------------------------------------------------+
        | Name                                                 | Description                                                           |
        +======================================================+=======================================================================+
        | :py:data:`~nirfsa.DownconverterLoopBandwidth.NARROW` | Specifies that the downconverter module uses a narrow loop bandwidth. |
        +------------------------------------------------------+-----------------------------------------------------------------------+
        | :py:data:`~nirfsa.DownconverterLoopBandwidth.MEDIUM` | Specifies that the downconverter module uses a medium loop bandwidth. |
        +------------------------------------------------------+-----------------------------------------------------------------------+
        | :py:data:`~nirfsa.DownconverterLoopBandwidth.WIDE`   | Specifies that the downconverter module uses a wide loop bandwidth.   |
        +------------------------------------------------------+-----------------------------------------------------------------------+


        .. tip:: This property can be set/get on specific los within your :py:class:`nirfsa.Session` instance.
            Use Python index notation on the repeated capabilities container los to specify a subset.

            Example: :py:attr:`my_session.los[ ... ].downconverter_loop_bandwidth`

            To set/get on all los, you can call the property directly on the :py:class:`nirfsa.Session`.

            Example: :py:attr:`my_session.downconverter_loop_bandwidth`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.DownconverterLoopBandwidth |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | los                              |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Downconverter Loop Bandwidth**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_LOOP_BANDWIDTH**

downconverter_preselector_enabled
---------------------------------

    .. py:attribute:: downconverter_preselector_enabled

        Specifies whether the tunable preselector is enabled on the downconverter.

        ----
        **Note**
        All devices support setting this property to :py:data:`~nirfsa.DownconverterPreselectorEnabled.DISABLED` or :py:data:`~nirfsa.DownconverterPreselectorEnabled.ENABLED_WHEN_IN_SIGNAL_PATH`. Only devices with a preselector support setting this property to :py:data:`~nirfsa.DownconverterPreselectorEnabled.ENABLED`.

        ----

        **Default Value**: :py:data:`~nirfsa.DownconverterPreselectorEnabled.DISABLED` if the device has no preselector. :py:data:`~nirfsa.DownconverterPreselectorEnabled.ENABLED_WHEN_IN_SIGNAL_PATH` if the device has a preselector.

        **Supported Devices:** PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +--------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                                           | Description                                                                                                                                                                                                                                                                       |
        +================================================================================+===================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.DownconverterPreselectorEnabled.DISABLED`                    | Disables the preselector.                                                                                                                                                                                                                                                         |
        +--------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.DownconverterPreselectorEnabled.ENABLED_WHEN_IN_SIGNAL_PATH` | The preselector is automatically enabled when it is in the signal path and is automatically disabled when it is not in the signal path. Use the :py:attr:`nirfsa.Session.preselector_present` property to determine if the downconverter has an preselector.                      |
        +--------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.DownconverterPreselectorEnabled.ENABLED`                     | Enables the preselector. If the preselector is not in the signal path or if the preselector is not supported on the device, NI-RFSA returns an error. Select the :py:data:`~nirfsa.DownconverterPreselectorEnabled.ENABLED_WHEN_IN_SIGNAL_PATH` whenever possible avoid an error. |
        +--------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------------+
            | Characteristic        | Value                                 |
            +=======================+=======================================+
            | Datatype              | enums.DownconverterPreselectorEnabled |
            +-----------------------+---------------------------------------+
            | Permissions           | read-write                            |
            +-----------------------+---------------------------------------+
            | Repeated Capabilities | None                                  |
            +-----------------------+---------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Downconverter Preselector Enabled**
                - C Attribute: **NIRFSA_ATTR_DOWNCONVERTER_PRESELECTOR_ENABLED**

driver_setup
------------

    .. py:attribute:: driver_setup

        The Driver Setup string returns the initial values for properties that are specific to NI-RFSA.

        The Driver Setup string uses the following format:

        DriverSetup= <i>Tag</i>:<i>Value</i>

        *Tag* is the name of the Driver Setup string property. *Value* is the value set to the property. If multiple properties are set, their assignments are separated with a semicolon.

        This property only returns the Driver Setup string that has already been defined. Refer to `Driver Setup Options <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/driver-setup-options.html>`_ for more information about configuring the Driver Setup string. Refer to the :py:meth:`nirfsa.Session.__init__` method for additional information about using the **option string** parameter.

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Driver Setup**
                - C Attribute: **NIRFSA_ATTR_DRIVER_SETUP**

enable_fractional_resampling
----------------------------

    .. py:attribute:: enable_fractional_resampling

        Specifies whether fractional resampling is enabled on the digitizer.

        Fractional resampling allows the digitizer to achieve very fine resolution on the I/Q rate value. Setting this property to False improves spectral performance.

        **PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: The only valid value for this property is True.

        **PXIe-5668**: When using a 400 MHz FPGA image, the only valid value for this property is True. When using a 800 MHz FPGA image, the only valid value for this property is False. Refer to `NI-RFSA Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/ni-rf-vst/page/rfsa-rfsg-instrument-driver-fpga-extensions.html>`_ for more information about FPGA images.

        **Default Value**: True

        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +-------+---------------------------------+
        | Value | Description                     |
        +=======+=================================+
        | True  | Enables fractional resampling.  |
        +-------+---------------------------------+
        | False | Disables fractional resampling. |
        +-------+---------------------------------+

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

                - LabVIEW Property: **Signal Path:Fractional Resample Enabled**
                - C Attribute: **NIRFSA_ATTR_ENABLE_FRACTIONAL_RESAMPLING**

end_of_record_event_terminal_name
---------------------------------

    .. py:attribute:: end_of_record_event_terminal_name

        Returns the fully qualified signal name as a string.

        **Default Values**:

        **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>EndOfRecordEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

        **PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>EndOfRecordEvent</i>, where *ModuleName* is the name of your device in MAX.

        **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>EndOfRecordEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

        **All other devices**: /<i>DigitizerName</i>/<i>EndOfRecordEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.get_terminal_name`

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

                - LabVIEW Property: **Events:End Of Record:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAME**

exported_advance_trigger_output_terminal
----------------------------------------

    .. py:attribute:: exported_advance_trigger_output_terminal

        Specifies the destination terminal for the exported Advance Trigger.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ExportSignal`

        **Defined Values**:

        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                  | Description                                                                                                                                                                                                     |
        +=======================================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ExportOutputTerminal.DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI1`          | The trigger is received on PFI 1.                                                                                                                                                                               |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG0`     | The trigger is received on PXI trigger line 0.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG1`     | The trigger is received on PXI trigger line 1.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG2`     | The trigger is received on PXI trigger line 2.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG3`     | The trigger is received on PXI trigger line 3.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG4`     | The trigger is received on PXI trigger line 4.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG5`     | The trigger is received on PXI trigger line 5.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG6`     | The trigger is received on PXI trigger line 6.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG7`     | The trigger is received on PXI trigger line 7.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXIE_DSTARC`   | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ExportOutputTerminal |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Advance:Export:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL**

exported_digitizer_sample_clock_output_terminal
-----------------------------------------------

    .. py:attribute:: exported_digitizer_sample_clock_output_terminal

        Specifies the terminal at which to export the Digitizer Sample Clock.

        **Valid Values**:

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5668

        **Defined Values**:

        +-----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                            | Description                                                                                                                                              |
        +=================================================================+==========================================================================================================================================================+
        | :py:data:`~nirfsa.DigitizerSampleClockExportedTerminal.NONE`    | The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646.                                                                |
        +-----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.DigitizerSampleClockExportedTerminal.CLK_OUT` | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841. |
        +-----------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------------------------+
            | Characteristic        | Value                                      |
            +=======================+============================================+
            | Datatype              | enums.DigitizerSampleClockExportedTerminal |
            +-----------------------+--------------------------------------------+
            | Permissions           | read-write                                 |
            +-----------------------+--------------------------------------------+
            | Repeated Capabilities | None                                       |
            +-----------------------+--------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Digitizer Sample Clock Exported Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_DIGITIZER_SAMPLE_CLOCK_OUTPUT_TERMINAL**

exported_done_event_output_terminal
-----------------------------------

    .. py:attribute:: exported_done_event_output_terminal

        Specifies the destination terminal for the Done Event.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ExportSignal`

        **Defined Values**:

        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                  | Description                                                                                                                                                                                                     |
        +=======================================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ExportOutputTerminal.DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI1`          | The trigger is received on PFI 1.                                                                                                                                                                               |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG0`     | The trigger is received on PXI trigger line 0.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG1`     | The trigger is received on PXI trigger line 1.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG2`     | The trigger is received on PXI trigger line 2.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG3`     | The trigger is received on PXI trigger line 3.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG4`     | The trigger is received on PXI trigger line 4.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG5`     | The trigger is received on PXI trigger line 5.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG6`     | The trigger is received on PXI trigger line 6.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG7`     | The trigger is received on PXI trigger line 7.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXIE_DSTARC`   | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ExportOutputTerminal |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Done:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL**

exported_end_of_record_event_output_terminal
--------------------------------------------

    .. py:attribute:: exported_end_of_record_event_output_terminal

        Specifies the destination terminal for the End of Record Event.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

        `Signal Routing <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/signal-routing.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ExportSignal`

        **Defined Values**:

        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                  | Description                                                                                                                                                                                                     |
        +=======================================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ExportOutputTerminal.DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI1`          | The trigger is received on PFI 1.                                                                                                                                                                               |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG0`     | The trigger is received on PXI trigger line 0.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG1`     | The trigger is received on PXI trigger line 1.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG2`     | The trigger is received on PXI trigger line 2.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG3`     | The trigger is received on PXI trigger line 3.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG4`     | The trigger is received on PXI trigger line 4.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG5`     | The trigger is received on PXI trigger line 5.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG6`     | The trigger is received on PXI trigger line 6.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG7`     | The trigger is received on PXI trigger line 7.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXIE_DSTARC`   | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ExportOutputTerminal |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:End Of Record:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_END_OF_RECORD_EVENT_OUTPUT_TERMINAL**

exported_ready_for_advance_event_output_terminal
------------------------------------------------

    .. py:attribute:: exported_ready_for_advance_event_output_terminal

        Specifies the destination terminal for the Ready for Advance Event.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ExportSignal`

        **Defined Values**:

        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                  | Description                                                                                                                                                                                                     |
        +=======================================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ExportOutputTerminal.DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI1`          | The trigger is received on PFI 1.                                                                                                                                                                               |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG0`     | The trigger is received on the PXI trigger line 0.                                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG1`     | The trigger is received on the PXI trigger line 1.                                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG2`     | The trigger is received on the PXI trigger line 2.                                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG3`     | The trigger is received on the PXI trigger line 3.                                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG4`     | The trigger is received on the PXI trigger line 4.                                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG5`     | The trigger is received on the PXI trigger line 5.                                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG6`     | The trigger is received on the PXI trigger line 6.                                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG7`     | The trigger is received on the PXI trigger line 7.                                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXIE_DSTARC`   | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ExportOutputTerminal |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Advance:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL**

exported_ready_for_ref_event_output_terminal
--------------------------------------------

    .. py:attribute:: exported_ready_for_ref_event_output_terminal

        Specifies the destination terminal for the Ready for Reference Event.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ExportSignal`

        **Defined Values**:

        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                  | Description                                                                                                                                                                                                     |
        +=======================================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ExportOutputTerminal.DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI1`          | The trigger is received on PFI 1.                                                                                                                                                                               |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG0`     | The trigger is received on PXI trigger line 0.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG1`     | The trigger is received on PXI trigger line 1.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG2`     | The trigger is received on PXI trigger line 2.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG3`     | The trigger is received on PXI trigger line 3.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG4`     | The trigger is received on PXI trigger line 4.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG5`     | The trigger is received on PXI trigger line 5.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG6`     | The trigger is received on PXI trigger line 6.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG7`     | The trigger is received on PXI trigger line 7.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXIE_DSTARC`   | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ExportOutputTerminal |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Ref:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_READY_FOR_REF_EVENT_OUTPUT_TERMINAL**

exported_ready_for_start_event_output_terminal
----------------------------------------------

    .. py:attribute:: exported_ready_for_start_event_output_terminal

        Specifies the destination terminal for the Ready for Start Event.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ExportSignal`

        **Defined Values**:

        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                  | Description                                                                                                                                                                                                     |
        +=======================================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ExportOutputTerminal.DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI1`          | The trigger is received on PFI 1.                                                                                                                                                                               |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG0`     | The trigger is received on PXI trigger line 0.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG1`     | The trigger is received on PXI trigger line 1.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG2`     | The trigger is received on PXI trigger line 2.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG3`     | The trigger is received on PXI trigger line 3.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG4`     | The trigger is received on PXI trigger line 4.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG5`     | The trigger is received on PXI trigger line 5.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG6`     | The trigger is received on PXI trigger line 6.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG7`     | The trigger is received on PXI trigger line 7.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXIE_DSTARC`   | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ExportOutputTerminal |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Ready For Start:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_READY_FOR_START_EVENT_OUTPUT_TERMINAL**

exported_ref_clock_output_terminal
----------------------------------

    .. py:attribute:: exported_ref_clock_output_terminal

        Specifies a comma-separated list of the terminals at which to export the Reference Clock.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ExportSignal`

        **Defined Values**:

        +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                              | Description                                                                                                                                                                                                     |
        +===================================================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ReferenceClockExportedTerminal.NONE`            | The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646.                                                                                                                       |
        +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceClockExportedTerminal.REF_OUT`         | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceClockExportedTerminal.REF_OUT2`        | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceClockExportedTerminal.CLK_OUT`         | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceClockExportedTerminal.IF_COND_REF_OUT` | Export the clock on the REF OUT terminal on the PXIe-5694. This value is valid only for the PXIe-5667.                                                                                                          |
        +-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------------------+
            | Characteristic        | Value                                |
            +=======================+======================================+
            | Datatype              | enums.ReferenceClockExportedTerminal |
            +-----------------------+--------------------------------------+
            | Permissions           | read-write                           |
            +-----------------------+--------------------------------------+
            | Repeated Capabilities | None                                 |
            +-----------------------+--------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Ref Clock Exported Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL**

exported_ref_clock_rate
-----------------------

    .. py:attribute:: exported_ref_clock_rate

        Specifies the Reference Clock Rate, in Hz, of the signal sent to the Ref Clock Exported Terminal.

        **Default Value**: 10 MHz

        **Valid Values**:

        PXIe-5820/5830/5831/5832/5840/5841: 10 MHz

        PXIe-5842: 10 MHz, 100 MHz, 1 GHz

        PXIe-5860: 10 MHz, 100 MHz

        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Clocking:Ref Clock Exported Rate:Ref Clock Exported Rate**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_REF_CLOCK_RATE**

exported_ref_trigger_output_terminal
------------------------------------

    .. py:attribute:: exported_ref_trigger_output_terminal

        Specifies the destination terminal for the exported Reference Trigger.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ExportSignal`

        **Defined Values**:

        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                  | Description                                                                                                                                                                                                     |
        +=======================================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ExportOutputTerminal.DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI1`          | The trigger is received on PFI 1.                                                                                                                                                                               |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG0`     | The trigger is received on PXI trigger line 0.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG1`     | The trigger is received on PXI trigger line 1.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG2`     | The trigger is received on PXI trigger line 2.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG3`     | The trigger is received on PXI trigger line 3.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG4`     | The trigger is received on PXI trigger line 4.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG5`     | The trigger is received on PXI trigger line 5.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG6`     | The trigger is received on PXI trigger line 6.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG7`     | The trigger is received on PXI trigger line 7.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXIE_DSTARC`   | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ExportOutputTerminal |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Export:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_start_trigger_output_terminal

        Specifies the destination terminal for the exported Start Trigger.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ExportSignal`

        **Defined Values**:

        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                  | Description                                                                                                                                                                                                     |
        +=======================================================+=================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ExportOutputTerminal.DO_NOT_EXPORT` | The signal is not exported.                                                                                                                                                                                     |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.CLK_OUT`       | Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT`       | Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841. |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.REF_OUT2`      | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.                                                                                                        |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI0`          | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.                                                                                             |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PFI1`          | The trigger is received on PFI 1.                                                                                                                                                                               |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG0`     | The trigger is received on PXI trigger line 0.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG1`     | The trigger is received on PXI trigger line 1.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG2`     | The trigger is received on PXI trigger line 2.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG3`     | The trigger is received on PXI trigger line 3.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG4`     | The trigger is received on PXI trigger line 4.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG5`     | The trigger is received on PXI trigger line 5.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG6`     | The trigger is received on PXI trigger line 6.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_TRIG7`     | The trigger is received on PXI trigger line 7.                                                                                                                                                                  |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXI_STAR`      | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.                                                                                                      |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.PXIE_DSTARC`   | The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.                                                                                   |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI0`      | The trigger is received on PFI0 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI1`      | The trigger is received on PFI1 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI2`      | The trigger is received on PFI2 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI3`      | The trigger is received on PFI3 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI4`      | The trigger is received on PFI4 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI5`      | The trigger is received on PFI5 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI6`      | The trigger is received on PFI6 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ExportOutputTerminal.DIO_PFI7`      | The trigger is received on PFI7 from the front panel DIO terminal.                                                                                                                                              |
        +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ExportOutputTerminal |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Export:Output Terminal**
                - C Attribute: **NIRFSA_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

external_gain
-------------

    .. py:attribute:: external_gain

        Specifies the gain, in dB, of a switch (or cable) connected before the RF IN connector of an NI-RFSA system.

        When you set this property, NI-RFSA calculates appropriate attenuator settings based on the value of this property and the value of the :py:attr:`nirfsa.Session.reference_level` property. In this case, NI-RFSA interprets the reference level as the maximum expected power level of the signal at the input of the external gain device. For more information about attenuation, refer to the *Attenuation and Signal Levels* topic for your device in the *NI RF Vector Signal Analyzers Help*.

        ----
        **Note**
        For the PXIe-5820, this property specifies the gain, in dB, of a switch (or cable) connected before the IQ IN connector.

        ----

        ----
        **Note**
        For the PXIe-5645, this property is ignored if you are using the I/Q ports.

        ----

        With this property set, NI-RFSA reads the :py:attr:`nirfsa.Session.iq_power_edge_ref_trigger_level` property value as the power level at the input of the external gain device at which the NI-RFSA device should trigger.

        Negative values indicate attenuation.

        **Valid Values**: INF to +INF

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Vertical:Advanced:External Gain (dB)**
                - C Attribute: **NIRFSA_ATTR_EXTERNAL_GAIN**

fetch_offset
------------

    .. py:attribute:: fetch_offset

        Specifies the offset relative to the position specified by the :py:attr:`nirfsa.Session.fetch_relative_to` property from which to start fetching data.

        Offset can be a positive or negative value.

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Acquisition:Fetch:Fetch Offset**
                - C Attribute: **NIRFSA_ATTR_FETCH_OFFSET**

fetch_relative_to
-----------------

    .. py:attribute:: fetch_relative_to

        Specifies the reference location within the acquired record from which to begin fetching.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                       | Description                                                                                                                                                                                                                 |
        +============================================================+=============================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.FetchRelativeTo.MOST_RECENT_SAMPLE`      | Fetching occurs relative to the most recently acquired data. The value of the :py:attr:`nirfsa.Session.fetch_offset` property must be negative.                                                                             |
        +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.FetchRelativeTo.FIRST_SAMPLE`            | Fetching occurs at the first sample acquired by the device. If the device wraps its buffer, the first sample is no longer available. In this case, NI-RFSA returns an error if the fetch offset is in the overwritten data. |
        +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.FetchRelativeTo.REFERENCE_TRIGGER`       | Fetching occurs relative to the Reference Trigger. This value behaves like :py:data:`~nirfsa.FetchRelativeTo.FIRST_SAMPLE` if no Reference Trigger is configured.                                                           |
        +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.FetchRelativeTo.FIRST_PRETRIGGER_SAMPLE` | Fetching occurs relative to the first pretrigger sample acquired.                                                                                                                                                           |
        +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.FetchRelativeTo.CURRENT_READ_POSITION`   | Fetching occurs after the last fetched sample.                                                                                                                                                                              |
        +------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.FetchRelativeTo |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Fetch:Fetch Relative To**
                - C Attribute: **NIRFSA_ATTR_FETCH_RELATIVE_TO**

fft_size
--------

    .. py:attribute:: fft_size

        Returns the size of the fast Fourier transform (FFT).

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Acquisition:Spectrum:FFT Size**
                - C Attribute: **NIRFSA_ATTR_FFT_SIZE**

fft_width
---------

    .. py:attribute:: fft_width

        Specifies the FFT width of the device.

        The FFT width is the effective bandwidth of the signal path during each signal acquisition.

        ----
        **Note**
        The maximum FFT width when using the PXIe-5622 is constrained to 50 MHz or 25 MHz, depending on the digitizer option you purchased. The maximum FFT width when using thing PXIe-5624 is constrained to 400 MHz or 765 MHz, depending on the digitizer configuration.

        ----

        ----
        **Note**
        You can use the :py:attr:`nirfsa.Session.fft_width` property with in-band retuning. For more information about in-band retuning, refer to the :py:attr:`nirfsa.Session.downconverter_center_frequency` property.

        ----

        NI-RFSA treats the *device instantaneous bandwidth* as the effective real-time bandwidth of the signal path. The *span* specifies the frequency range of the computed spectrum. An RF vector signal analyzer can acquire a bandwidth only within the device instantaneous bandwidth frequency. If the span you choose is greater than the device instantaneous bandwidth, NI-RFSA obtains multiple acquisitions and combines them into a single spectrum. By specifying the FFT width, you can control the specific bandwidth obtained in each signal acquisition. If you read the :py:attr:`nirfsa.Session.fft_width` property without setting it, NI-RFSA returns the value of the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property.

        **Valid Values**:

        The lower limit for all FFT width supported devices using the PXIe-5622 IF digitizer is 7.325 kHz. The lower limit for all FFT width supported devices using the PXIe-5624 IF digitizer is 400 MHz or 800 MHz, depending on the FPGA image that is downloaded upon opening the session to the PXIe-5624 IF digitizer.

        **PXIe-5663/5663E**: The FFT width upper limit for the PXIe-5663/5663E depends on the downconverter center frequency and on the module revision of the PXIe-5601 as illustrated in the following table. Refer to the `Identifying Module Revision <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/identifying-module-revision.html>`_ topic for more information about determining which revision of the PXIe-5601 RF downconverter you have installed.

        **PXIe-5665/5667/5668**: The upper limit of the FFT width is the maximum device instantaneous bandwidth.

        ----
        **Note**

        ----

        ----
        **Note**
        At frequencies greater than 3.6 GHz, the PXIe-5605 provides a typical bandwidth of 47 MHz at   dB with the preselector enabled. The :py:attr:`nirfsa.Session.fft_width` property can override the typical bandwidth of the PXIe-5605 up to 57 MHz using an external digitizer and up to 50 MHz or 25 MHz depending on the PXIe-5622 digitizer option you purchased. The increase in bandwidth results in faster signal acquisitions, but amplitude accuracy is decreased for spectrum acquisitions, and magnitude and phase accuracy is decreased for I/Q acquisitions. National Instruments does not guarantee device specifications if you set the :py:attr:`nirfsa.Session.fft_width` property greater than the warranted instantaneous bandwidth specification.

        ----

        ----
        **Note**
        When using the PXIe-5606, the 765 MHz IF filter is only available at center frequencies of 3.6 GHz and above.

        ----

        **Default Value**: N/A

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668

        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+--------------------------------------------------------------------+
        | Downconverter Center Frequency                                                                                                                                                                                | PXIe-5601 Instantaneous Bandwidth | FFT Width Upper Limit                                              |
        +===============================================================================================================================================================================================================+===================================+====================================================================+
        | 10 MHz to <120 MHz                                                                                                                                                                                            | 10 MHz                            | 10 MHz (Revision E), 20 MHz< sup >* < /sup> (Revision G or later)  |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+--------------------------------------------------------------------+
        | 120 MHz to <330 MHz                                                                                                                                                                                           | 20 MHz                            | 20 MHz (Revision E), 30 MHz< sup > * < /sup> (Revision G or later) |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+--------------------------------------------------------------------+
        | 330 MHz to <6.6 GHz                                                                                                                                                                                           | 50 MHz                            | 50 MHz                                                             |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+--------------------------------------------------------------------+
        | <sup > * < / sup >National Instruments does not guarantee device specifications if you set the :py:attr:`nirfsa.Session.fft_width` property greater than the warranted instantaneous bandwidth specification. |                                   |                                                                    |
        +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+--------------------------------------------------------------------+

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

                - LabVIEW Property: **Acquisition:Spectrum:FFT Width**
                - C Attribute: **NIRFSA_ATTR_FFT_WIDTH**

fft_window_shape_factor
-----------------------

    .. py:attribute:: fft_window_shape_factor

        Returns the shape factor of the window used in the fast Fourier transform (FFT).

        The window shape factor is defined as the ratio of the 60 dB to 6 dB bandwidths.

        The following table shows the shape factor for each NI-RFSA FFT window type.

        | Window Type            | Shape Factor |
        |:-----------------------|:-------------|
        | Uniform                | 1.57:1       |
        | Hanning                | 1.94:1       |
        | Hamming                | 2.13:1       |
        | Exact Blackman         | 2.52:1       |
        | Flat Top               | 2.0:1        |
        | 4-term Blackman-Harris | 2.5:1        |
        | 7-term Blackman-Harris | 4.1:1        |
        | Low Side Lobe          | 2.78:1       |
        | Gaussian               | 2.3:1        |
        | Kaiser Bessel          | 2.55:1       |

        **Default Value**: N/A

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

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

                - LabVIEW Property: **Acquisition:Spectrum:FFT Window Shape Factor**
                - C Attribute: **NIRFSA_ATTR_FFT_WINDOW_SHAPE_FACTOR**

fft_window_size
---------------

    .. py:attribute:: fft_window_size

        Returns the size of the window used in the fast Fourier transform (FFT), in terms of the number of samples in the window.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Acquisition:Spectrum:FFT Window Size**
                - C Attribute: **NIRFSA_ATTR_FFT_WINDOW_SIZE**

fft_window_type
---------------

    .. py:attribute:: fft_window_type

        Specifies the time-domain window type.

        **Default Values**:

        **PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: :py:data:`~nirfsa.SpectrumFftWindowType._7_TERM_BLACKMAN_HARRIS`

        **PXIe-5667**: :py:data:`~nirfsa.SpectrumFftWindowType._4_TERM_BLACKMAN_HARRIS`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Resolution Bandwidth <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/resolution-bandwidth.html>`_

        **Defined Values**:

        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
        +==================================================================+======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.SpectrumFftWindowType.UNIFORM`                 | No window is applied.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumFftWindowType.HANNING`                 | The Hanning window is useful for analyzing transients longer than the time duration of the window, and also for general-purpose applications.                                                                                                                                                                                                                                                                                                                                                                                                        |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumFftWindowType.HAMMING`                 | A Hamming window is applied to the waveform using the following equation: y[i] = x[i] * (0.54 - 0.46cos(w)) where w = (2)i/n and n = the waveform size. Note: Hanning and Hamming windows are somewhat similar. However, in the time domain, the Hamming window does not get as close to zero near the edges as does the Hanning window.                                                                                                                                                                                                             |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumFftWindowType.BLACKMAN_HARRIS`         | A Blackman-Harris window is applied to the waveform using the following equation: y[i] = x[i] * (0.42323 - 0.49755*cos(w) + 0.07922*cos(2w))                                                                                                                                                                                                                                                                                                                                                                                                         |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumFftWindowType.EXACT_BLACKMAN`          | An Exact Blackman window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w))                                                                                                                                                                                                                                                                                                                                                                                                                        |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumFftWindowType.BLACKMAN`                | A Blackman window is useful for analyzing transient signals, and provides similar windowing to Hanning and Hamming windows but adds one additional cosine term to reduce ripple. A Blackman window is applied to the waveform using the following equation: y[i] = x[i] * (0.42 - 0.50*cos(w) + 0.08*cos(2w))                                                                                                                                                                                                                                        |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumFftWindowType.FLAT_TOP`                | The fifth-order Flat Top window has the best amplitude accuracy of all the window methods. The increased amplitude accuracy (0.02 dB for signals exactly between integral cycles) is at the expense of frequency selectivity. The Flat Top window is most useful in accurately measuring the amplitude of single frequency components with little nearby spectral energy in the signal. A fifth-order Flat Top window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w) + a4*cos(4w)) |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumFftWindowType._4_TERM_BLACKMAN_HARRIS` | A 4-term Blackman-Harris window is a general purpose window; it has side-lobe rejection in the upper 90 dB, with moderately wide side lobe. A 4-term Blackman Harris window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w))                                                                                                                                                                                                                                                        |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumFftWindowType._7_TERM_BLACKMAN_HARRIS` | A 7-term Blackman-Harris window has the highest dynamic range; it is ideal for signal-to-noise ratio applications. A 7-term Blackman Harris window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w) + a4*cos(4w) - a5*cos(5w) + a6*cos(6w))                                                                                                                                                                                                                                          |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumFftWindowType.LOW_SIDE_LOBE`           | The Low Side Lobe window further reduces the size of the main lobe. The following equation defines the Low Side Lobe window. where   *N* is the length of window                                                                                                                                                                                                                                                                                                                                                                                     |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumFftWindowType.GAUSSIAN`                | A Gaussian window is applied to the waveform using the following equation: y[i] = x[i] * exp(-0.5*(i - (N-1)/2)^2 / ((N-1)/2)^2) where N is the length of the window                                                                                                                                                                                                                                                                                                                                                                                 |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumFftWindowType.KAISER_BESSEL`           | A Kaiser-Bessel window is applied to the waveform using the following equation: y[i] = x[i] * I0(β*sqrt(1 - (2i/(N-1) - 1)^2))/I0(β) where i is between 0 and N-1, N is the length of the window, β determines the shape of the window, and I0 is the zeroth order Modified Bessel method of the first kind                                                                                                                                                                                                                                          |
        +------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.SpectrumFftWindowType |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:FFT Window Type**
                - C Attribute: **NIRFSA_ATTR_FFT_WINDOW_TYPE**

fixed_group_delay_across_ports
------------------------------

    .. py:attribute:: fixed_group_delay_across_ports

        Specifies a comma-separated list of ports for which to fix the group delay.

        **Valid Values**:

        PXIe-5831/5832: rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel.

        **Default Value**:

        PXIe-5831/5832: (empty string), which specifies that the group delay will not be fixed for any port.

        **Supported Devices**: PXIe-5831/5832

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | list of str |
            +-----------------------+-------------+
            | Permissions           | read-write  |
            +-----------------------+-------------+
            | Repeated Capabilities | None        |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Fixed Group Delay Across Ports**
                - C Attribute: **NIRFSA_ATTR_FIXED_GROUP_DELAY_ACROSS_PORTS**

fpga_bitfile_path
-----------------

    .. py:attribute:: fpga_bitfile_path

        Returns a string containing the path to the location of the current NI-RFSA instrument driver FPGA extensions bitfile, a .lvbitx file, that is programmed on the device.

        You can specify the bitfile location using the Driver Setup string in the **optionString** parameter of the :py:meth:`nirfsa.Session.__init__` method.

        NI-RFSA instrument driver FPGA extensions enable you to use pre-compiled FPGA bitfiles to customize the behavior of the device FPGA while maintaining the functionality of the NI-RFSA instrument driver.

        Refer to `NI-RFSA Instrument Driver FPGA Extensions <https://www.ni.com/docs/en-US/bundle/ni-rf-vst/page/rfsa-rfsg-instrument-driver-fpga-extensions.html>`_ for more information about using NI-RFSA instrument driver FPGA extensions for NI devices.

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Device Characteristics:FPGA Bitfile Path**
                - C Attribute: **NIRFSA_ATTR_FPGA_BITFILE_PATH**

fpga_target_name
----------------

    .. py:attribute:: fpga_target_name

        Returns a string containing the name of the FPGA target being used.

        This name can be used with the RIO open session to open a reference to the FPGA.

        This property is channel dependent if multiple targets are supported.

        **Supported Devices:** PXIe-5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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
                - C Attribute: **NIRFSA_ATTR_FPGA_TARGET_NAME**

fpga_temperature
----------------

    .. py:attribute:: fpga_temperature

        Returns the current temperature, in degrees Celsius, of the FPGA.

        ----
        **Note**
        If you query this property during RF list mode, list steps may take longer to complete during list execution.

        ----

        **Units**: degrees Celcius

        **Default Value**: N/A

        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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
                - C Attribute: **NIRFSA_ATTR_FPGA_TEMPERATURE**

frequency_settling
------------------

    .. py:attribute:: frequency_settling

        Specifies the value used for local oscillator (LO) frequency settling.

        The units and interpretation for this scalar value are specified using the :py:attr:`nirfsa.Session.frequency_settling_units` property. This property is not supported if you are using an external LO.

        The valid values for this property depend on the :py:attr:`nirfsa.Session.frequency_settling_units` property.

        **Notes:**
        1. If the frequency settling units property is set to :py:data:`~nirfsa.FrequencySettlingUnits.SECONDS_AFTER_LOCK` and the downconverter loop bandwidth property is set to narrow, NI recommends a minimum settling time of 128 microseconds to ensure that the phase-locked loop (PLL) lock stabilizes. If the downconverter loop bandwidth is set to wide, NI recommends a minimum settling time of 16 microseconds.
        2. When in RF list mode, the valid values for :py:data:`~nirfsa.FrequencySettlingUnits.SECONDS_AFTER_IO` are 0 microseconds to 50 milliseconds.
        3. The valid values for this configuration depend on the module used as the LO source. Refer to the lo source property for more information.

        **Default Value**: 0.1

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842

        +----------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------------------------------------------+
        | Device                                                         | :py:data:`~nirfsa.FrequencySettlingUnits.SECONDS_AFTER_LOCK`                              | :py:data:`~nirfsa.FrequencySettlingUnits.SECONDS_AFTER_IO`                 | %enum_value{frequency settling units.fsu ppm} |
        +================================================================+===========================================================================================+============================================================================+===============================================+
        | PXIe-5663/5663E                                                | 2 microseconds<sup>1</sup> to 80 milliseconds, resolution of approximately 2 microseconds | 0 microseconds to 80 milliseconds<sup>2</sup>, resolution of 1 microsecond | 1.0, 0.1, 0.01                                |
        +----------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------------------------------------------+
        | PXIe-5665/5667/5668                                            | 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds             | 0 microseconds to 80 milliseconds<sup>2</sup>, resolution of 1 microsecond | 1.0, 0.1, 0.01, 0.001                         |
        +----------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------------------------------------------+
        | PXIe-5644/5645/5646                                            | 1 microsecond<sup>1</sup> to 65 milliseconds, resolution of 1 microsecond                 | 1 microsecond<sup>1</sup> to 65 milliseconds, resolution of 1 microsecond  | 1.0, 0.1, 0.01                                |
        +----------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------------------------------------------+
        | PXIe-5830/5831/5832/5840/5841/5842                             | 1 microsecond<sup>1</sup> to 10 seconds, resolution of 1 microsecond                      | 0 microseconds to 10 seconds, resolution of 1 microsecond                  | 1.0 to 0.01                                   |
        +----------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------------------------------------------+
        | PXIe-5831/5832 with PXIe-5653 (using PXIe-3622 LO)<sup>3</sup> | 1 microsecond<sup>1</sup> to 10 seconds, resolution of 1 microsecond                      | 0 microseconds to 10 seconds, resolution of 1 microsecond                  | 1.0 to 0.01                                   |
        +----------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------------------------------------------+
        | PXIe-5831/5832 with PXIe-5653 (using PXIe-5653 LO)<sup>3</sup> | 4 microseconds to 80 milliseconds, resolution of approximately 4 microseconds             | 0 microseconds to 80 milliseconds, resolution of 1 microsecond             | 1.0 to 0.01                                   |
        +----------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+-----------------------------------------------+

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

                - LabVIEW Property: **Signal Path:Advanced:Frequency Settling**
                - C Attribute: **NIRFSA_ATTR_FREQUENCY_SETTLING**

frequency_settling_units
------------------------

    .. py:attribute:: frequency_settling_units

        Specifies the delay duration units and interpretation for LO settling.

        Specify the actual settling value using the :py:attr:`nirfsa.Session.frequency_settling` property. This property is not supported if you are using an external LO.

        **Default Value**: :py:data:`~nirfsa.FrequencySettlingUnits.PPM`

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5830/5831/5832/5840/5841/5842

        **Defined Values**:

        +--------------------------------------------------------------+-------------------------------------------------------------------+
        | Name                                                         | Description                                                       |
        +==============================================================+===================================================================+
        | :py:data:`~nirfsa.FrequencySettlingUnits.PPM`                | Specifies the frequency settling time in parts per million (PPM). |
        +--------------------------------------------------------------+-------------------------------------------------------------------+
        | :py:data:`~nirfsa.FrequencySettlingUnits.SECONDS_AFTER_LOCK` | Specifies the frequency settling in time after lock (seconds).    |
        +--------------------------------------------------------------+-------------------------------------------------------------------+
        | :py:data:`~nirfsa.FrequencySettlingUnits.SECONDS_AFTER_IO`   | Specifies the frequency settling time after I/O (seconds).        |
        +--------------------------------------------------------------+-------------------------------------------------------------------+

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

                - LabVIEW Property: **Signal Path:Advanced:Frequency Settling Units**
                - C Attribute: **NIRFSA_ATTR_FREQUENCY_SETTLING_UNITS**

group_capabilities
------------------

    .. py:attribute:: group_capabilities

        Returns a list of class-extension groups that NI-RFSA implements.

        **Supported Devices:** PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | list of str |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | None        |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities**
                - C Attribute: **NIRFSA_ATTR_GROUP_CAPABILITIES**

host_dma_buffer_size
--------------------

    .. py:attribute:: host_dma_buffer_size

        Specifies the size of the DMA buffer in computer memory, in bytes.

        To set this property, the NI-RFSA device must be in the Configuration state.

        A sufficiently large host DMA buffer improves performance by allowing large fetches to be transferred more efficiently.

        **Default Value:** 8 MB

        **Supported Devices**: PXI-5820/5830/5831/5840/5841/5842/5860

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

                - LabVIEW Property: **Acquisition:Fetch:Data Transfer:Host DMA Buffer Size**
                - C Attribute: **NIRFSA_ATTR_HOST_DMA_BUFFER_SIZE**

if_attenuation
--------------

    .. py:attribute:: if_attenuation

        Configures the device attenuation to a value that has the actual calibrated IF attenuation closest to the desired value.

        **Valid Values**: 0 to 30

        **Default Value**: N/A

        **Supported Devices**: PXIe-5601/5603/5605 (external digitizer mode), PXIe-5663/5663E/5665/5667, PXIe-5693

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

                - LabVIEW Property: **Signal Path:Advanced:NI 5663:IF Attenuation (dB)**
                - C Attribute: **NIRFSA_ATTR_IF_ATTENUATION**

if_filter_bandwidth
-------------------

    .. py:attribute:: if_filter_bandwidth

        Specifies the IF filter path bandwidth for your device configuration.

        ----
        **Note**
        For composite devices, such as the PXIe-5665/5667/5668, the IF filter path bandwidth includes all IF filters across the component modules of a composite device.

        ----

        NI-RFSA uses this property in conjunction with the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property and the :py:attr:`nirfsa.Session.digital_if_equalization_enabled` property to determine the settings for your measurement. NI-RFSA selects the next highest available filter based on the value you specify. The following table lists the IF filters available for NI devices. You may specify a higher value than your device instantaneous bandwidth if your measurement requires it, but specifying a lower value returns an error.

        **Valid Values**:

        **PXIe-5603/5605**: 0 to 80 MHz

        **PXIe-5665/5667**: 0 to 50 MHz

        **PXIe-5668**: 0 to 765 MHz

        **PXIe-5694**: 0 to 50 MHz

        ----
        **Note**
        To set this property to values greater than 20 MHz, you must set the :py:attr:`nirfsa.Session.signal_conditioning_enabled` property to :py:data:`~nirfsa.SignalConditioningEnabled.BYPASSED`

        ----

        **Default Values:** For spectrum acquisition types the default is greater than or equal to the :py:attr:`nirfsa.Session.spectrum_span` property. NI-RFSA chooses the default value of the :py:attr:`nirfsa.Session.if_filter_bandwidth` property to correspond to the appropriate IF filter. For I/Q acquisition types NI-RFSA chooses the default value corresponding to the widest IF filter possible for your equipment setup.

        **Supported Devices**: PXIe-5603/5605/5606, PXIe-5665/5667/5668, PXIe-5694

        +--------------------------+---------------------------+-------------------+
        | Device                   | IF Filter Bandwidth Range | IF Filter         |
        +==========================+===========================+===================+
        | PXIe-5603/5665 (3.6 GHz) | 2264300 kHz               | 300 kHz IF filter |
        +--------------------------+---------------------------+-------------------+
        | PXIe-5603/5665 (3.6 GHz) | >300 kHz and 22645 MHz    | Through IF filter |
        +--------------------------+---------------------------+-------------------+
        | PXIe-5603/5665 (3.6 GHz) | >5 MHz                    | Through IF filter |
        +--------------------------+---------------------------+-------------------+
        | PXIe-5605/5665 (14 GHz)  | 2264300 kHz               | 300 kHz IF filter |
        +--------------------------+---------------------------+-------------------+
        | PXIe-5603/5665 (14 GHz)  | >300 kHz and 22645 MHz    | 5 MHz IF filter   |
        +--------------------------+---------------------------+-------------------+
        | PXIe-5603/5665 (14 GHz)  | >5 MHz                    | Through IF filter |
        +--------------------------+---------------------------+-------------------+
        | PXIe-5668                | 2264300 kHz               | 300 kHz IF filter |
        +--------------------------+---------------------------+-------------------+
        | PXIe-5668                | >300 kHz and 22645 MHz    | 5 MHz IF filter   |
        +--------------------------+---------------------------+-------------------+
        | PXIe-5668                | >5 MHz and 2264100 MHz    | 100 MHz IF filter |
        +--------------------------+---------------------------+-------------------+
        | PXIe-5668                | >100 MHz and 2264320 MHz  | 320 MHz IF filter |
        +--------------------------+---------------------------+-------------------+
        | PXIe-5668                | >320 MHz                  | 765 MHz IF filter |
        +--------------------------+---------------------------+-------------------+

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

                - LabVIEW Property: **Signal Path:IF Filter Bandwidth**
                - C Attribute: **NIRFSA_ATTR_IF_FILTER_BANDWIDTH**

if_output_frequency
-------------------

    .. py:attribute:: if_output_frequency

        Returns the center frequency of the IF output signal that corresponds to the configured RF center frequency.

        The downconverter translates the RF input frequency to the IF output frequency by mixing it with the LO signal. The nominal values for the IF output frequency are shown in the following table.

        The coarse nature of the LO settings can cause the downconverter to be unable to tune to the exact LO frequency that would produce the nominal IF output frequency. Any coercion in the actual LO frequency results in the IF output frequency being slightly off from the nominal value.

        Additionally, if you use the :py:attr:`nirfsa.Session.downconverter_center_frequency` and :py:attr:`nirfsa.Session.lo_frequency` properties to program the downconverter, the IF output frequency could vary from the nominal value. NI-RFSA adjusts the acquired spectrum or I/Q data for the difference between nominal and actual IF output frequency. If you use an external digitizer with a RF downconverter, use this property to specify the actual IF output frequency.

        **Default Value**: N/A

        **Supported Devices**:PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694

        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Downconverter | Nominal IF Output Frequency                                                                                                                                                                                                                                                                                |
        +===============+============================================================================================================================================================================================================================================================================================================+
        | PXI-5600      | 15 MHz                                                                                                                                                                                                                                                                                                     |
        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXIe-5601     | 53 MHz or 187.5 MHz                                                                                                                                                                                                                                                                                        |
        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXIe-5603     | 187.5 MHz or 199 MHz                                                                                                                                                                                                                                                                                       |
        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXIe-5605     | 187.5 MHz, 190 MHz, or 199 MHz                                                                                                                                                                                                                                                                             |
        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXIe-5606     | 187.5 MHz, 190 MHz, 199 MHz, 507.5 MHz, or 730 MHz                                                                                                                                                                                                                                                         |
        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | PXIe-5694     | - signal_conditioning_enabled set to SIGNAL_CONDITIONING_ENABLED and if_conditioning_down_conversion_enabled set to disabled: 193.6 MHz<br>- if_conditioning_down_conversion_enabled set to enabled: 21.4 MHz<br>- signal_conditioning_enabled set to SIGNAL_CONDITIONING_BYPASSED: 162.5 MHz to 212.5 MHz |
        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

                - LabVIEW Property: **Acquisition:Advanced:IF Output Frequency**
                - C Attribute: **NIRFSA_ATTR_IF_OUTPUT_FREQUENCY**

if_output_power_level
---------------------

    .. py:attribute:: if_output_power_level

        Specifies the level of the IF signal leaving the system, in dBm.

        Use this property to increase or decrease the nominal IF signal output level to achieve better measurement results.

        If you set the :py:attr:`nirfsa.Session.if_output_power_level` and :py:attr:`nirfsa.Session.if_output_power_level_offset` properties at the same time, NI-RFSA returns an error.

        ----
        **Note**
        If you set the :py:attr:`nirfsa.Session.if_output_power_level` property to a value less than 201310 dBm, the IF output power level may be higher than the value you request. Read the value of this property to determine the configured IF output power level.

        ----

        ----
        **Note**
        The value of this property is limited by the amount of IF attenuation that the downconverter can apply, the :py:attr:`nirfsa.Session.reference_level` property, the :py:attr:`nirfsa.Session.downconverter_center_frequency` property, and the :py:attr:`nirfsa.Session.center_frequency` property or :py:attr:`nirfsa.Session.iq_carrier_frequency` property, depending on your acquisition type.

        ----

        **Units**: dBm

        **Default Value**:

        **PXIe-5667**: -2 dBm

        **PXIe-5668**: -1 dBm

        **All other devices**:   dBm

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694

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

                - LabVIEW Property: **Vertical:IF Output Power Level (dBm)**
                - C Attribute: **NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL**

if_output_power_level_offset
----------------------------

    .. py:attribute:: if_output_power_level_offset

        Specifies the number of dB by which to adjust the default IF output power level.

        This property does not depend on absolute IF output power levels, so you can use it to adjust the IF output power level on all NI-RFSA devices without knowing the exact default value. Use this property to increase or decrease the nominal output level to achieve better measurement results. The default value for the offset is 0 dB.

        If you set the :py:attr:`nirfsa.Session.if_output_power_level` and :py:attr:`nirfsa.Session.if_output_power_level_offset` properties at the same time, NI-RFSA returns an error.

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668

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

                - LabVIEW Property: **Vertical:IF Output Power Level Offset (dB)**
                - C Attribute: **NIRFSA_ATTR_IF_OUTPUT_POWER_LEVEL_OFFSET**

input_isolation_enabled
-----------------------

    .. py:attribute:: input_isolation_enabled

        Specifies whether input isolation is enabled.

        Enabling this property isolates the input signal at the RF IN connector on the RF downconverter from the rest of the RF downconverter signal path. Disabling this property reintegrates the input signal into the RF downconverter signal path.

        ----
        **Note**
        If you enable input isolation for your device, the device impedance is changed from the characteristic 50  impedance. A change in the device impedance may also cause a VSWR value higher than the device specifications.

        ----

        For the PXIe-5830/5831/5832, input isolation is supported for all available ports for your hardware configuration.

        **Default Value**: :py:data:`~nirfsa.InputIsolationEnabled.DISABLED`, if the device configuration is supported.

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5693, PXIe-5820/5830/5831/5832/5840/5841

        **Defined Values**:

        +---------------------------------------------------+---------------------------+
        | Name                                              | Description               |
        +===================================================+===========================+
        | :py:data:`~nirfsa.InputIsolationEnabled.DISABLED` | Disables input isolation. |
        +---------------------------------------------------+---------------------------+
        | :py:data:`~nirfsa.InputIsolationEnabled.ENABLED`  | Enables input isolation.  |
        +---------------------------------------------------+---------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.InputIsolationEnabled |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:Input Isolation Enabled**
                - C Attribute: **NIRFSA_ATTR_INPUT_ISOLATION_ENABLED**

input_port
----------

    .. py:attribute:: input_port

        Specifies the connector(s) to use to acquire the signal.

        To set this property, the NI-RFSA device must be in the Configuration state.

        **Default Values**:

        **PXIe-5820**: :py:data:`~nirfsa.InputPort.IQ_IN`

        **All other devices**: :py:data:`~nirfsa.InputPort.RF_IN`

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +-------------------------------------+---------------------------------------------------------------------------------+
        | Name                                | Description                                                                     |
        +=====================================+=================================================================================+
        | :py:data:`~nirfsa.InputPort.RF_IN`  | Enables the RF IN port.                                                         |
        +-------------------------------------+---------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.InputPort.IQ_IN`  | Enables the I/Q IN port.                                                        |
        +-------------------------------------+---------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.InputPort.CAL_IN` | Enables the CAL IN port.                                                        |
        +-------------------------------------+---------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.InputPort.I_ONLY` | Enables the I terminals of the I/Q IN port. It is supported only for PXIe-5645. |
        +-------------------------------------+---------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-----------------+
            | Characteristic        | Value           |
            +=======================+=================+
            | Datatype              | enums.InputPort |
            +-----------------------+-----------------+
            | Permissions           | read-write      |
            +-----------------------+-----------------+
            | Repeated Capabilities | None            |
            +-----------------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:Input Port**
                - C Attribute: **NIRFSA_ATTR_INPUT_PORT**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        Returns a string that contains the firmware revision information for the NI-RFSA downconverter for the composite device you are currently using.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        ----
        **Note**
        PXIe-5820/5830/5831/5832/5840/5841/5842/5860 devices will return "No revision information available." To retrieve the firmware revision, use MAX, Hardware Configuration Utility, or NI System Configuration API.

        ----

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
                - C Attribute: **NIRFSA_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        Returns a string that contains the name of the manufacturer for the NI-RFSA device you are currently using.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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
                - C Attribute: **NIRFSA_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        Returns a string that contains the model number or name of the NI-RFSA device that you are currently using.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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
                - C Attribute: **NIRFSA_ATTR_INSTRUMENT_MODEL**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Indicates the resource name NI-RFSA uses to identify the physical device.

        If you initialize NI-RFSA with a logical name, this property contains the resource name that corresponds to the entry in the IVI Configuration Utility.

        If you initialize NI-RFSA with the resource name, this property contains that value.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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
                - C Attribute: **NIRFSA_ATTR_IO_RESOURCE_DESCRIPTOR**

iq_carrier_frequency
--------------------

    .. py:attribute:: iq_carrier_frequency

        Specifies the expected carrier frequency of the incoming signal for demodulation.

        The NI-RFSA device tunes to this frequency. NI-RFSA may coerce this value based on hardware settings and the RF downconverter specifications.

        ----
        **Note**
        For the PXIe-5645, this property is ignored if you are using the I/Q ports.

        ----

        **Units**: hertz (Hz)

        **Default Values**:

        **PXIe-5644/5645/5646, PXIe-5840/5841/5860, PXIe-5842 (500 MHz, 1 GHz, and 2 GHz bandwidth options)**: 1 GHz

        **PXIe-5842 (4 GHz bandwidth option) using the Standard personality**: 1 GHz

        **PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality**: 6.5 GHz

        **PXIe-5820**: 0 Hz

        **PXIe-5830/5831/5832**: 6.5 GHz

        **All other devices**: 100 MHz

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Carrier Wave <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/fund-carrierwave.html>`_

        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureIqCarrierFrequency`

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

                - LabVIEW Property: **Acquisition:IQ:IQ Carrier Frequency**
                - C Attribute: **NIRFSA_ATTR_IQ_CARRIER_FREQUENCY**

iq_in_port_carrier_frequency
----------------------------

    .. py:attribute:: iq_in_port_carrier_frequency

        Configures the frequency of the signal.

        The onboard signal processing (OSP) frequency shifts the signal at this frequency to baseband prior to acquiring it.

        ----
        **Note**
        For the PXIe-5645, this property is ignored if you are using the RF ports.

        ----

        **Valid Values**:

        **PXIe-5645**: -60 MHz to +60 MHz

        **PXIe-5820**: -500 MHz to +500 MHz

        **Default Value**: 0

        **Supported Devices**: PXIe-5645, PXIe-5820

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

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ In Port:Carrier Frequency**
                - C Attribute: **NIRFSA_ATTR_IQ_IN_PORT_CARRIER_FREQUENCY**

iq_in_port_temperature
----------------------

    .. py:attribute:: iq_in_port_temperature

        Returns the temperature of the I/Q IN circuitry on the device.

        **Units:** degrees C

        **Supported Devices:** PXIe-5645, PXIe-5820

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

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ In Port:Temperature (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_IQ_IN_PORT_TEMPERATURE**

iq_in_port_terminal_configuration
---------------------------------

    .. py:attribute:: iq_in_port_terminal_configuration

        Configures the terminal configuration of the I/Q port.

        To use this property, you must use the channelName parameter of the :py:meth:`nirfsa.Session._set_attribute_vi_int32` method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

        ----
        **Note**
        For the PXIe-5645, this property is ignored if you are using the RF ports.

        ----

        **PXIe-5820**: The only valid value for this property is :py:data:`~nirfsa.IqInPortTerminalConfiguration.DIFFERENTIAL`.

        **Default Value**: :py:data:`~nirfsa.IqInPortTerminalConfiguration.DIFFERENTIAL`

        **Supported Devices:** PXIe-5645, PXIe-5820

        **Defined Values**:

        +---------------------------------------------------------------+--------------------------------------------------+
        | Name                                                          | Description                                      |
        +===============================================================+==================================================+
        | :py:data:`~nirfsa.IqInPortTerminalConfiguration.DIFFERENTIAL` | Sets the terminal configuration to differential. |
        +---------------------------------------------------------------+--------------------------------------------------+
        | :py:data:`~nirfsa.IqInPortTerminalConfiguration.SINGLE_ENDED` | Sets the terminal configuration to single-ended. |
        +---------------------------------------------------------------+--------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------+
            | Characteristic        | Value                               |
            +=======================+=====================================+
            | Datatype              | enums.IqInPortTerminalConfiguration |
            +-----------------------+-------------------------------------+
            | Permissions           | read-write                          |
            +-----------------------+-------------------------------------+
            | Repeated Capabilities | None                                |
            +-----------------------+-------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ In Port:Terminal Configuration**
                - C Attribute: **NIRFSA_ATTR_IQ_IN_PORT_TERMINAL_CONFIGURATION**

iq_in_port_vertical_range
-------------------------

    .. py:attribute:: iq_in_port_vertical_range

        Specifies the voltage range for the I/Q terminals.

        To use this property, you must use the channelName parameter of the :py:meth:`nirfsa.Session._set_attribute_vi_real64` method to specify the name of the channel you are configuring. For the PXIe-5645, you can configure the I and Q channels by using I or Q as the channel string, or set the channel string to "" (empty string) to configure both channels. For the PXIe-5820, the only valid value for the channel string is "" (empty string).

        The voltage range in differential terminal configuration is configurable from 2 V<sub>pk-pk</sub> to 0.032 V<sub>pk-pk</sub> in 1 dB steps. In single-ended terminal configuration, valid ranges are half those for differential. Values are always coerced up to the next valid range.

        ----
        **Note**
        For the PXIe-5645, this property is ignored if you are using the RF ports.

        ----

        **Valid Values:**

        **PXIe-5645**: 0 V<sub>pk-pk</sub> to 2 V<sub>pk-pk</sub> for differential terminal configuration, 0 V<sub>pk-pk</sub> to 1 V<sub>pk-pk</sub> for single-ended terminal configuration.

        **PXIe-5820**: 0 V<sub>pk-pk</sub> to 4 V<sub>pk-pk</sub> for differential terminal configuration.

        **Default Value**: 2 V<sub>pk-pk</sub>

        **Supported Devices:** PXIe-5645, PXIe-5820

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

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:IQ In Port:Vertical Range**
                - C Attribute: **NIRFSA_ATTR_IQ_IN_PORT_VERTICAL_RANGE**

iq_power_edge_ref_trigger_level
-------------------------------

    .. py:attribute:: iq_power_edge_ref_trigger_level

        Specifies the power level, in dBm, at which the device triggers.

        The device asserts the trigger when the signal crosses the level specified by the value of this property, taking into consideration the specified slope. If you are using external gain, refer to the :py:attr:`nirfsa.Session.external_gain` property for more information about how this property affects the I/Q power edge trigger level.

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureIqPowerEdgeRefTrigger`

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

                - LabVIEW Property: **Triggers:Ref:IQ Power Edge:Level**
                - C Attribute: **NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_LEVEL**

iq_power_edge_ref_trigger_slope
-------------------------------

    .. py:attribute:: iq_power_edge_ref_trigger_slope

        Specifies whether the device asserts the trigger when the signal power is rising or falling.

        When you set the :py:attr:`nirfsa.Session.ref_trigger_type` property to :py:data:`~nirfsa.ReferenceTriggerType.IQ_POWER_EDGE`, the device asserts the trigger when the signal power exceeds the specified level with the slope you specify.

        **Default Value**: :py:data:`~nirfsa.ReferenceTriggerIqPowerEdgeSlope.RISING`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureIqPowerEdgeRefTrigger`

        **Defined Values**:

        +-------------------------------------------------------------+-------------------------------------------------------+
        | Name                                                        | Description                                           |
        +=============================================================+=======================================================+
        | :py:data:`~nirfsa.ReferenceTriggerIqPowerEdgeSlope.RISING`  | The trigger asserts when the signal power is rising.  |
        +-------------------------------------------------------------+-------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceTriggerIqPowerEdgeSlope.FALLING` | The trigger asserts when the signal power is falling. |
        +-------------------------------------------------------------+-------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------------+
            | Characteristic        | Value                                  |
            +=======================+========================================+
            | Datatype              | enums.ReferenceTriggerIqPowerEdgeSlope |
            +-----------------------+----------------------------------------+
            | Permissions           | read-write                             |
            +-----------------------+----------------------------------------+
            | Repeated Capabilities | None                                   |
            +-----------------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:IQ Power Edge:Slope**
                - C Attribute: **NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_SLOPE**

iq_power_edge_ref_trigger_source
--------------------------------

    .. py:attribute:: iq_power_edge_ref_trigger_source

        Specifies the channel from which the device monitors the trigger.

        NI-RFSA currently supports only 0 as the value of this property.

        **Default Value**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureIqPowerEdgeRefTrigger`

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

                - LabVIEW Property: **Triggers:Ref:IQ Power Edge:Source**
                - C Attribute: **NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_SOURCE**

iq_rate
-------

    .. py:attribute:: iq_rate

        Specifies the I/Q rate for the acquisition.

        The value is expressed in samples per second (S/s).

        Refer to the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property for more information about device specific instantaneous bandwidth limits. You can also refer to the *NI PXIe-5665 Specifications* for more information about instantaneous bandwidth device specifications.

        ----
        **Note**
        For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. At I/Q rates above 50 MS/s, the dither noise can affect phase coherency performance and leak into the lower frequencies and the upper frequencies of the IF passband. Refer to the :py:attr:`nirfsa.Session.digitizer_dither_enabled` property for more information about dithering.

        For the PXIe-5663/5663E/5665/5667, when you set the :py:attr:`nirfsa.Session.digitizer_sample_clock_timebase_source` property to :py:data:`~nirfsa.NIRFSA_VAL_ONBOARD_CLOCK`, the downconverter instantaneous bandwidth is greater than or equal to the coerced I/Q rate times 0.8. For the PXIe-5665, the actual signal bandwidth is further limited by the combination of the chosen IF filter and anti-aliasing filter.

        ----

        **PXI-5661**: You should not need to configure an I/Q rate higher than 25 megasamples per second (MS/s) because the PXI-5600 RF downconverter bandwidth is 20 MHz. If you configure a higher I/Q rate, you may see aliasing effects at negative frequencies because the IF frequency of the PXI-5600 is 15 MHz.

        **PXIe-5663/5663E**: Your maximum allowed instantaneous bandwidth depends on the I/Q carrier frequency you use. Refer to the `PXIe-5601 RF downconverter overview <https://www.ni.com/docs/en-US/bundle/pxie-5663-5663e-feature/page/overview.3.html>`_ for more information about instantaneous bandwidth.

        **PXIe-5665**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency if you have enabled the preselector (YIG-tuned filter).

        **PXIe-5667**: Your maximum allowed instantaneous bandwidth depends on the selected [RF preselector filter](:py:attr:`nirfsa.Session.RF_PRESELECTOR_FILTER`.html) and whether the preselector on the [RF downconverter](:py:attr:`nirfsa.Session.PRESELECTOR_ENABLED`.html) is enabled.

        **PXIe-5668**: Your maximum allowed instantaneous bandwidth depends on the downconverter center frequency you use and whether or not you enable the highpass filter or preselector (YIG-tuned filter).

        **Units**: S/s

        **Default Values:**

        **PXIe-5842 (4 GHz bandwidth option) using the 4 GHz Bandwidth personality**: 5 GS/s only.

        **All Other Devices**: 1 MS/s

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureIqRate`



        .. note:: One or more of the referenced properties are not in the Python API for this driver.

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

                - LabVIEW Property: **Acquisition:IQ:IQ Rate (S/s)**
                - C Attribute: **NIRFSA_ATTR_IQ_RATE**

lo2_export_enabled
------------------

    .. py:attribute:: lo2_export_enabled

        Specifies whether to enable the LO2 OUT terminal on the installed devices.

        Set this property to TRUE to export the 4 GHz LO signal from the device LO2 IN terminal to the LO2 OUT terminal.

        You can also export the LO2 signal by setting the :py:attr:`nirfsa.Session.lo_export_enabled` property and the :py:attr:`nirfsa.Session.digitizer_sample_clock_timebase_source` property.

        | Value | Description                    |
        |:------|:-------------------------------|
        | True  | Enables the LO2 OUT terminal.  |
        | False | Disables the LO2 OUT terminal. |

        **Default Value:** False

        **Supported Devices:** PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5668

        **Defined Values**:

        +----------------------------------------------+----------------------+
        | Name                                         | Description          |
        +==============================================+======================+
        | :py:data:`~nirfsa.Lo2ExportEnabled.DISABLED` | Disables LO2 export. |
        +----------------------------------------------+----------------------+
        | :py:data:`~nirfsa.Lo2ExportEnabled.ENABLED`  | Enables LO2 export.  |
        +----------------------------------------------+----------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.Lo2ExportEnabled |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:LO2 Export Enabled**
                - C Attribute: **NIRFSA_ATTR_LO2_EXPORT_ENABLED**

load_configurations_from_file_reset_options
-------------------------------------------

    .. py:attribute:: load_configurations_from_file_reset_options

        Specifies the configurations to skip to reset while loading configurations from a file.

        **Default Value:**  :py:data:`~nirfsa.NIRFSA_VAL_SKIP_NONE`
        **Supported Devices:** PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +---------------------------------------------------------------------+--------------------------------------------------+
        | Name                                                                | Description                                      |
        +=====================================================================+==================================================+
        | :py:data:`~nirfsa.LoadConfigurationResetOptions.NONE`               | NI-RFSA resets all configurations.               |
        +---------------------------------------------------------------------+--------------------------------------------------+
        | :py:data:`~nirfsa.LoadConfigurationResetOptions.DEEMBEDDING_TABLES` | NI-RFSA skips resetting the de-embedding tables. |
        +---------------------------------------------------------------------+--------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------+
            | Characteristic        | Value                               |
            +=======================+=====================================+
            | Datatype              | enums.LoadConfigurationResetOptions |
            +-----------------------+-------------------------------------+
            | Permissions           | read-write                          |
            +-----------------------+-------------------------------------+
            | Repeated Capabilities | None                                |
            +-----------------------+-------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Load Configurations:Reset Options**
                - C Attribute: **NIRFSA_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS**

logical_name
------------

    .. py:attribute:: logical_name

        Contains the logical name you specified when opening the current IVI session.

        You may pass a logical name to the :py:meth:`nirfsa.Session.Init` method or the :py:meth:`nirfsa.Session.__init__` method. The IVI Configuration Utility must contain an entry for the logical name. The logical name entry refers to a driver session section in the IVI Configuration file. The driver session section specifies a physical device and initial user options.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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
                - C Attribute: **NIRFSA_ATTR_LOGICAL_NAME**

lo_export_enabled
-----------------

    .. py:attribute:: lo_export_enabled

        Specifies whether to enable the LO OUT terminals on the installed devices.

        **PXIe-5601**: The only valid value for this property is True.

        **PXIe-5603/5605/5606**: If you want to daisy-chain multiple devices together using the same LO source, set this property to TRUE to export the LO input signals on the LO1 IN, LO2 IN, and LO3 IN terminals to LO1 OUT, LO2 OUT, and LO3 OUT, respectively.

        **PXIe-5694**: You can enable this property only if you set the :py:attr:`nirfsa.Session.lo_source` property to :py:data:`~nirfsa.LoSource.LO_IN`, or if you set the :py:attr:`nirfsa.Session.lo_source` property to :py:data:`~nirfsa.LoSource.ONBOARD` and the :py:attr:`nirfsa.Session.IF_CONDITIONING_DOWN_CONVERSION_ENABLED` property to :py:data:`~nirfsa.NIRFSA_VAL_ENABLED`.

        **PXIe-5830/5831**: To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session._set_attribute_vi_boolean` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

        ----
        **Note**
        If you are sharing an LO for the PXIe-5830/5831/5832 between an NI-RFSA and NI-RFSG session, ensure both sessions use the same shared setting.

        ----

        **Defined Values:**

        | Value    | Description                    |
        |:---------|:-------------------------------|
        | True  | Enables the LO OUT terminals.  |
        | False | Disables the LO OUT terminals. |

        **Default Values**:

        **PXIe-5601, PXIe-5663/5663E**: True

        **PXIe-5603/5605/5606, PXIe-5644/5645/5646, PXIe-5665/5667/5668, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842**: False

        **Supported Devices**: PXIe-5601/5603/5605 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842



        .. note:: One or more of the referenced properties are not in the Python API for this driver.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific los within your :py:class:`nirfsa.Session` instance.
            Use Python index notation on the repeated capabilities container los to specify a subset.

            Example: :py:attr:`my_session.los[ ... ].lo_export_enabled`

            To set/get on all los, you can call the property directly on the :py:class:`nirfsa.Session`.

            Example: :py:attr:`my_session.lo_export_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | los        |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:LO Export Enabled**
                - C Attribute: **NIRFSA_ATTR_LO_EXPORT_ENABLED**

lo_frequency
------------

    .. py:attribute:: lo_frequency

        Specifies the LO signal frequency for the configured center frequency.

        If you are using the NI RF vector signal analyzer with an external LO, use this property to specify the LO frequency that the external LO source passes into the LO IN or LO1 IN connector on the RF downconverter front panel. If you are using an external LO, reading the value of this property after configuring the rest of the parameters returns the LO frequency needed by the device.

        Set this property to the actual LO frequency because NI-RFSA corrects for any difference between expected and actual LO frequencies.

        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session._set_attribute_vi_real64` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

        **Default Values**:

        **PXIe-5694**: 215 MHz

        **All other devices**: 0

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842

        **Related Topics**

        `PXIe-5830 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-configuration.html>`_

        `PXIe-5831/5832 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-configuration.html>`_

        `PXIe-5841 Frequency and Bandwidth Configuration <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-configuration.html>`_




        .. tip:: This property can be set/get on specific los within your :py:class:`nirfsa.Session` instance.
            Use Python index notation on the repeated capabilities container los to specify a subset.

            Example: :py:attr:`my_session.los[ ... ].lo_frequency`

            To set/get on all los, you can call the property directly on the :py:class:`nirfsa.Session`.

            Example: :py:attr:`my_session.lo_frequency`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | los        |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:LO Frequency**
                - C Attribute: **NIRFSA_ATTR_LO_FREQUENCY**

lo_frequency_step_size
----------------------

    .. py:attribute:: lo_frequency_step_size

        Specifies the step size for tuning the local oscillator (LO) phase-locked loop (PLL).

        You can only tune the LO frequency by multiples of the :py:attr:`nirfsa.Session.lo_frequency_step_size` property. For the PXIe-5644/5645/5646 and PXIe-5840/5841, the LO frequency can therefore be offset from the requested center frequency by as much as half of the :py:attr:`nirfsa.Session.lo_frequency_step_size` property. This offset is corrected by digitally frequency shifting the :py:attr:`nirfsa.Session.lo_frequency` property to the value requested in either the :py:attr:`nirfsa.Session.iq_carrier_frequency` property or the :py:attr:`nirfsa.Session.center_frequency` property.

        ----
        **Note**
        For the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653, this property is ignored if the PXIe-5653 is used as the LO source.

        ----

        The valid values for this property depend on the :py:attr:`nirfsa.Session.lo_pll_fractional_mode_enabled` property.

        **PXIe-5644/5645/5646**: If the :py:attr:`nirfsa.Session.lo_pll_fractional_mode_enabled` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`, the specified value is coerced to the closest valid value.

        **PXIe-5840/5841/5842**: If the :py:attr:`nirfsa.Session.lo_pll_fractional_mode_enabled` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.

        * Values up to 100 MHz are coerced to 50 MHz.

        ----
        **Note**
        The default value for the PXIe-5831 depends on the frequency range of the selected port for your instrument configuration. Refer to the `Instrument Configurations <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/instrument-configurations.html>`_ topic for more information about available ports for your hardware configuration.

        ----

        **Default Values:**

        **PXIe-5644/5645/5646:** 200 kHz

        **PXIe-5830:** 2 MHz

        **PXIe-5831/5832 (RF port):** 8 MHz

        **PXIe-5831/5832 (IF port):** 2 MHz, 4 MHz

        **PXIe-5840/5841:**

        - Fractional mode: 500 kHz
        - Integer mode: 10 MHz for frequencies less than or equal to 4 GHz. 20 MHz for frequencies greater than 4 GHz.

        **PXIe-5841 with PXIe-5655:** 500 kHz

        **PXIe-5842:** 1 Hz

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

        +----------------------------------------+-------------------------------------+------------------------------+-----------------------------------------------+--------------------------------------------+-----------------------+
        | lo_pll_fractional_mode_enabled         | PXIe-5644/5645                      | PXIe-5646                    | PXIe-5840/5841                                | PXIe-5830/5831/5832                        | PXIe-5841 w/PXIe-5655 |
        +========================================+=====================================+==============================+===============================================+============================================+=======================+
        | :py:data:`~nirfsa.NIRFSA_VAL_ENABLED`  | 50 kHz to 24 MHz                    | 50 kHz to 25 MHz             | 50 kHz to 100 MHz                             | LO1: 8 Hz to 400 MHz
        LO2: 4 kHz to 400 MHz | 1 nHz to 50 MHz       |
        +----------------------------------------+-------------------------------------+------------------------------+-----------------------------------------------+--------------------------------------------+-----------------------+
        | :py:data:`~nirfsa.NIRFSA_VAL_DISABLED` | 4 MHz, 5 MHz, 6 MHz, 12 MHz, 24 MHz | 2 MHz, 5 MHz, 10 MHz, 25 MHz | 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, 100 MHz | LO1: --
        LO2: --                            | 1 nHz to 50 MHz       |
        +----------------------------------------+-------------------------------------+------------------------------+-----------------------------------------------+--------------------------------------------+-----------------------+

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

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO Frequency Step Size (Hz)**
                - C Attribute: **NIRFSA_ATTR_LO_FREQUENCY_STEP_SIZE**

lo_injection_side
-----------------

    .. py:attribute:: lo_injection_side

        Specifies the LO injection side.

        **PXIe-5601/5663/5663E**: For frequencies below 517.5 MHz or above 6.4125 GHz, the LO injection side is fixed and NI-RFSA returns an error if you specify the incorrect value. If you do not configure this property, NI-RFSA selects the default LO injection side based on the downconverter center frequency. Reset this property to return to automatic behavior.

        **PXIe-5603/5605/5665 (3.6 GHz)/5667 (3.6 GHz)**: Setting this property to :py:data:`~nirfsa.LoInjection.LOW` is not supported for this device.

        **PXIe-5605/5665 (14 GHz)/5667 (7 GHz)**: Setting this property to :py:data:`~nirfsa.LoInjection.LOW` is supported for this device for frequencies greater than 4 GHz, but this configuration is not calibrated, and device specifications are not guaranteed.

        **PXIe-5606/5668**: Setting this property to :py:data:`~nirfsa.LoInjection.LOW` is supported for certain frequencies in high band, varying by final IF frequency. This configuration is not calibrated and device specifications are not guaranteed.

        **Default Values**:

        **PXIe-5601 (external digitizer mode), PXIe-5663/5663E (frequencies < 3.0 GHz)**: :py:data:`~nirfsa.LoInjection.HIGH`

        **PXIe-5601 (external digitizer mode), PXIe-5663/5663E (frequencies  3.0 GHz)**: :py:data:`~nirfsa.LoInjection.LOW`

        **PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668**: :py:data:`~nirfsa.LoInjection.HIGH`

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668

        **Defined Values**:

        +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                | Description                                                                                                                                                                                         |
        +=====================================+=====================================================================================================================================================================================================+
        | :py:data:`~nirfsa.LoInjection.HIGH` | Configures the LO signal that the NI-RFSA device generates at a frequency higher than the RF frequency. This LO frequency is given by the formula f<sub>LO</sub> = f<sub>RF</sub> + f<sub>IF</sub>. |
        +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.LoInjection.LOW`  | Configures the LO signal that the NI-RFSA device generates at a frequency lower than the RF frequency. This LO frequency is given by the formula f<sub>LO</sub> = f<sub>RF</sub> - f<sub>IF</sub>.  |
        +-------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.LoInjection |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:LO Injection Side**
                - C Attribute: **NIRFSA_ATTR_LO_INJECTION_SIDE**

lo_in_power
-----------

    .. py:attribute:: lo_in_power

        Returns the power level, in dBm, expected at the LO IN terminal when the :py:attr:`nirfsa.Session.lo_source` property is set to :py:data:`~nirfsa.LoSource.LO_IN`.

        ----
        **Note**
        For the PXIe-5644/5645/5646, this property is always read-only.

        ----

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

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

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO In Power (dBm)**
                - C Attribute: **NIRFSA_ATTR_LO_IN_POWER**

lo_out_export_configure_from_rfsg
---------------------------------

    .. py:attribute:: lo_out_export_configure_from_rfsg

        Specifies whether to allow NI-RFSG to control the NI-RFSA LO out export.

        Set this property to :py:data:`~nirfsa.LoOutExportConfigureFromRfsg.ENABLED` to allow NI-RFSG to control the LO out export. Use the NIRFSG ATTR RF IN LO EXPORT ENABLED property to control the NI-RFSA LO out export from NI-RFSG.

        **Default Value:** :py:data:`~nirfsa.LoOutExportConfigureFromRfsg.DISABLED`

        **Supported Devices**: PXIe-5840/5841/5842

        **Defined Values**:

        +----------------------------------------------------------+----------------------------------------------------------------------+
        | Name                                                     | Description                                                          |
        +==========================================================+======================================================================+
        | :py:data:`~nirfsa.LoOutExportConfigureFromRfsg.DISABLED` | Do not allow NI-RFSG to control the NI-RFSA local oscillator export. |
        +----------------------------------------------------------+----------------------------------------------------------------------+
        | :py:data:`~nirfsa.LoOutExportConfigureFromRfsg.ENABLED`  | Allow NI-RFSG to control the NI-RFSA local oscillator export.        |
        +----------------------------------------------------------+----------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------------+
            | Characteristic        | Value                              |
            +=======================+====================================+
            | Datatype              | enums.LoOutExportConfigureFromRfsg |
            +-----------------------+------------------------------------+
            | Permissions           | read-write                         |
            +-----------------------+------------------------------------+
            | Repeated Capabilities | None                               |
            +-----------------------+------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:LO Out Export Configure From RFSG**
                - C Attribute: **NIRFSA_ATTR_LO_OUT_EXPORT_CONFIGURE_FROM_RFSG**

lo_out_power
------------

    .. py:attribute:: lo_out_power

        Specifies the power level, in dBm, of the signal at the LO OUT terminal when the :py:attr:`nirfsa.Session.lo_export_enabled` property is set to True.

        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session._set_attribute_vi_real64` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

        **Units:** dBm

        **Supported Devices:** PXIe-5830/5831/5832/5840/5841/5842




        .. tip:: This property can be set/get on specific los within your :py:class:`nirfsa.Session` instance.
            Use Python index notation on the repeated capabilities container los to specify a subset.

            Example: :py:attr:`my_session.los[ ... ].lo_out_power`

            To set/get on all los, you can call the property directly on the :py:class:`nirfsa.Session`.

            Example: :py:attr:`my_session.lo_out_power`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | los        |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO Out Power (dBm)**
                - C Attribute: **NIRFSA_ATTR_LO_OUT_POWER**

lo_pll_fractional_mode_enabled
------------------------------

    .. py:attribute:: lo_pll_fractional_mode_enabled

        Specifies whether to use fractional mode for the local oscillator (LO) phase-locked loop (PLL).

        Fractional mode gives a finer frequency step resolution, but it may result in non harmonic spurs. Refer to the device specifications for your device for more information about fractional mode and non harmonic spurs.

        ----
        **Note**
        The :py:attr:`nirfsa.Session.lo_pll_fractional_mode_enabled` property is applicable only when using the internal LO.

        ----

        ----
        **Note**
        For the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653, this property is ignored if the PXIe-5653 is used as the LO source. For the PXIe-5841 with PXIe-5655, this property is ignored if the PXIe-5655 is used as the LO source.

        ----

        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session._set_attribute_vi_int32` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the the only valid value for the channel string is "" (empty string).

        **Default Value**: :py:data:`~nirfsa.LoPllFractionalModeEnabled.ENABLED`

        **Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

        **Defined Values**:

        +--------------------------------------------------------+------------------------------------------+
        | Name                                                   | Description                              |
        +========================================================+==========================================+
        | :py:data:`~nirfsa.LoPllFractionalModeEnabled.DISABLED` | Disables fractional mode for the LO PLL. |
        +--------------------------------------------------------+------------------------------------------+
        | :py:data:`~nirfsa.LoPllFractionalModeEnabled.ENABLED`  | Enables fractional mode for the LO PLL.  |
        +--------------------------------------------------------+------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific los within your :py:class:`nirfsa.Session` instance.
            Use Python index notation on the repeated capabilities container los to specify a subset.

            Example: :py:attr:`my_session.los[ ... ].lo_pll_fractional_mode_enabled`

            To set/get on all los, you can call the property directly on the :py:class:`nirfsa.Session`.

            Example: :py:attr:`my_session.lo_pll_fractional_mode_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.LoPllFractionalModeEnabled |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | los                              |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:Vector Signal Transceiver:Signal Path:LO PLL Fractional Mode Enabled**
                - C Attribute: **NIRFSA_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED**

lo_source
---------

    .. py:attribute:: lo_source

        Specifies the LO signal source used to downconvert the RF input signal.

                        If no signal downconversion is required, this property is ignored. If this property is set to "" (empty string), NI-RFSA uses the internal LO source.

                        To use this property for the PXIe-5830/5831/5832, you must use the channelName parameter of the :py:meth:`nirfsa.Session._set_attribute_vi_string` method to specify the name of the channel you are configuring. You can configure the LO1 and LO2 channels by using lo1 or lo2 as the channel string, or set the channel string to lo1,lo2 to configure both channels. For all other devices, the only valid value for the channel string is "" (empty string).

                        ----
                        **Note**
                        For the PXIe-5841 with PXIe-5655, RF list mode is not supported when this property is set to :py:data:`~nirfsa.LoSource.LO_SOURCE_SG_SA_SHARED`.

                        ----




                        **Default Value**: :py:data:`~nirfsa.LoSource.ONBOARD` ("Onboard")

                        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5694, PXIe-5830/5831/5832/5840/5841/5842

                        **Related Topics**
                        `PXIe-5830 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/lo-sharing-using-rfsa-rfsg.html>`_
                        `PXIe-5831/5832 LO Sharing Using NI-RFSA and NI-RFSG <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/lo-sharing-using-rfsa-rfsg.html>`_

        **Defined Values**:

        +----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
        +====================================================+===================================================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.LoSource.NONE`                   | Specifies that no LO source is required to downconvert the RF input signal.                                                                                                                                                                                                                                                                                                                                                       |
        +----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.LoSource.ONBOARD`                | Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal.**PXIe-5831/5832** This configuration uses the onboard LO of the PXIe-3622, using the LO2 stage.**PXIe-5831/5832 with PXIe-5653** This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3622.**PXIe-5841 with PXIe-5655** This configuration uses the onboard LO of the PXIe-5655. |
        +----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.LoSource.LO_IN`                  | Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel.                                                                                                                                                                                                                                                                                                      |
        +----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.LoSource.LO_SOURCE_SECONDARY`    | Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid on only the PXIe-5831 with PXIe-5653 (LO1 stage only) or PXIe-5832 with PCIe-5653 (LO1 stage only).                                                                                                                                                                                                                                                     |
        +----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.LoSource.LO_SOURCE_SG_SA_SHARED` | Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSA selects an internal synthesizer and the synthesizer signal is switched to both the RF Out and RF In mixers. This value is valid on only the PXIe-5830/5831/5832/5841 with PXIe-5655.                                                                                                                                                                       |
        +----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific los within your :py:class:`nirfsa.Session` instance.
            Use Python index notation on the repeated capabilities container los to specify a subset.

            Example: :py:attr:`my_session.los[ ... ].lo_source`

            To set/get on all los, you can call the property directly on the :py:class:`nirfsa.Session`.

            Example: :py:attr:`my_session.lo_source`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.LoSource |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | los            |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:LO Source**
                - C Attribute: **NIRFSA_ATTR_LO_SOURCE**

lo_temperature
--------------

    .. py:attribute:: lo_temperature

        Returns the current temperature, in degrees Celsius, of the LO module.

        **PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode) PXI-5661, PXIe-5663/5663E/5665/5667/5668** This property is not supported if you are using an external LO.

        **PXIe-5840/5841/5842**: If you query this property during RF list mode, list steps may take longer to complete during list execution.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode) PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5840/5841/5842

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
                - C Attribute: **NIRFSA_ATTR_LO_TEMPERATURE**

lo_vco_frequency_step_size
--------------------------

    .. py:attribute:: lo_vco_frequency_step_size

        Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal.

        ----
        **Note**
        Do not set this property with the :py:attr:`nirfsa.Session.lo_frequency_step_size` property.

        ----

        **Valid Values**:

        LO1: 1 Hz to 50 MHz

        LO2: 1 Hz to 100 MHz

        **Default Values**: 1 MHz

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
                - C Attribute: **NIRFSA_ATTR_LO_VCO_FREQUENCY_STEP_SIZE**

lo_yig_main_coil_drive
----------------------

    .. py:attribute:: lo_yig_main_coil_drive

        Adjusts the dynamics of the current driving the YIG main coil.

        ----
        **Note**
        Setting this property to :py:data:`~nirfsa.LoYigMainCoilDrive.FAST` allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise. This property is not supported if you are using an external LO.

        ----

        **Default Value**: :py:data:`~nirfsa.LoYigMainCoilDrive.NORMAL`

        **Supported Devices:** PXIe-5603/5605/5606 (external digitizer mode), PXIe-5665/5667/5668

        **Defined Values**:

        +----------------------------------------------+------------------------------------------------------------------+
        | Name                                         | Description                                                      |
        +==============================================+==================================================================+
        | :py:data:`~nirfsa.LoYigMainCoilDrive.NORMAL` | Adjusts the YIG main coil on the LO for an underdamped response. |
        +----------------------------------------------+------------------------------------------------------------------+
        | :py:data:`~nirfsa.LoYigMainCoilDrive.FAST`   | Adjusts the YIG main coil on the LO for an overdamped response.  |
        +----------------------------------------------+------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.LoYigMainCoilDrive |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | None                     |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:LO YIG Main Coil Drive**
                - C Attribute: **NIRFSA_ATTR_LO_YIG_MAIN_COIL_DRIVE**

max_device_instantaneous_bandwidth
----------------------------------

    .. py:attribute:: max_device_instantaneous_bandwidth

        Returns the maximum instantaneous bandwidth of the device.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Device Characteristics:Max Device Instantaneous Bandwidth**
                - C Attribute: **NIRFSA_ATTR_MAX_DEVICE_INSTANTANEOUS_BANDWIDTH**

max_iq_rate
-----------

    .. py:attribute:: max_iq_rate

        Returns the maximum I/Q rate.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Device Characteristics:Max IQ Rate**
                - C Attribute: **NIRFSA_ATTR_MAX_IQ_RATE**

mechanical_attenuation
----------------------

    .. py:attribute:: mechanical_attenuation

        Specifies the level of mechanical attenuation for the RF path, in dB.

        **PXIe-5667**: This property is read-only when the :py:attr:`nirfsa.Session.LOW_FREQUENCY_BYPASS_ENABLED` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`.

        **PXIe-5668with PXIe-5698**: This property is read-only when the :py:attr:`nirfsa.Session.rf_preamp_enabled` property is set to :py:data:`~nirfsa.EnableRfPreamp.ENABLED`.

        **Units**: dB

        **Valid Values:**

        **PXIe-5601/5663/5663E**: 0, 16

        **PXIe-5603/5665 (3.6 GHz)**: 0, 10, 20, 30

        **PXIe-5605/5665 (14 GHz), PXIe-5606/5668**: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75

        **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 0, 10, 20, 30

        **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**: 0

        **PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75

        **PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector filter path**: 0

        **PXIe-5668 with PXIe-5698 with the** :py:attr:`nirfsa.Session.rf_preamp_enabled` property set to :py:data:`~nirfsa.EnableRfPreamp.ENABLED`: 5

        **Default Value**: N/A

        **Supported Devices**: PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5663/5663E/5665/5667/5668



        .. note:: One or more of the referenced properties are not in the Python API for this driver.

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

                - LabVIEW Property: **Vertical:Advanced:Mechanical Attenuation (dB)**
                - C Attribute: **NIRFSA_ATTR_MECHANICAL_ATTENUATION**

memory_size
-----------

    .. py:attribute:: memory_size

        Returns the digitizer onboard memory size, in bytes.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Device Characteristics:Memory Size**
                - C Attribute: **NIRFSA_ATTR_MEMORY_SIZE**

minimum_acpr
------------

    .. py:attribute:: minimum_acpr

        Specifies the minimum adjacent channel power ratio (ACPR), in dB, relative to the main channel reference level.

        This property configures NI-RFSA to optimize downconverter gain to measure a lower-power adjacent channel, adding gain only after filtering the main channel. The gain NI-RFSA applies is always less than or equal to the ACPR value you specify.

        ----
        **Note**
        For the PXIe-5665 (3.6 GHz), this property is supported only if you set the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth`, :py:attr:`nirfsa.Session.spectrum_span`, or :py:attr:`nirfsa.Session.if_filter_bandwidth` property to a value less than 300 kHz. For the PXIe-5665 (14 GHz), this property is supported for :py:attr:`nirfsa.Session.device_instantaneous_bandwidth`, :py:attr:`nirfsa.Session.spectrum_span`, or :py:attr:`nirfsa.Session.if_filter_bandwidth` property values less than 300 kHz by using the 300 kHz IF filter, and it is supported for values between 300 kHz and 5 MHz by using the 5 MHz IF filter.

        ----

        ----
        **Note**
        NI-RFSA coerces this property to zero for the PXI-5600, PXIe-5601 and the PXIe-5667. For all other devices, read the coerced value of this property to determine the actual amount of gain applied.

        ----

        ----
        **Note**
        For the PXIe-5668, this property alters the :py:attr:`nirfsa.Session.if_output_power_level` property. This property will not affect the :py:attr:`nirfsa.Session.reference_level` property.

        ----

        **Default Value**: 0

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668

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

                - LabVIEW Property: **Vertical:Advanced:Minimum Adjacent Channel Power Ratio (dB)**
                - C Attribute: **NIRFSA_ATTR_MINIMUM_ACPR**

mixer_level
-----------

    .. py:attribute:: mixer_level

        Specifies the mixer level, in dBm.

        The mixer level represents the attenuation value to apply to the input RF signal as it reaches the first mixer in the signal chain. If you do not set this property, NI-RFSA automatically selects an optimal mixer level value based on the reference level. The valid values for this property depend on your device configuration.

        If you set the :py:attr:`nirfsa.Session.mixer_level` and :py:attr:`nirfsa.Session.mixer_level_offset` properties at the same time, NI-RFSA returns an error.

        **PXIe-5601/5663/5663E**: This property is read-only.

        **PXIe-5667**: This property is read-only when the :py:attr:`nirfsa.Session.LOW_FREQUENCY_BYPASS_ENABLED` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`.

        **Units**: dBm

        **Default Values**:

        **PXI-5600/5661**: -30

        **PXIe-5603/5605/5665/5667/5668**: -10

        **All other devices**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668



        .. note:: One or more of the referenced properties are not in the Python API for this driver.

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

                - LabVIEW Property: **Vertical:Mixer Level (dBm)**
                - C Attribute: **NIRFSA_ATTR_MIXER_LEVEL**

mixer_level_offset
------------------

    .. py:attribute:: mixer_level_offset

        Specifies the number of dB by which to adjust the device mixer level.

        The default value is 0, which specifies device settings that are the best compromise between distortion and noise. Specifying a positive value for this property configures the device for moderate distortion and low noise, and specifying a negative value results in low distortion and higher noise.

        You cannot set the :py:attr:`nirfsa.Session.mixer_level` and :py:attr:`nirfsa.Session.mixer_level_offset` properties at the same time.

        **PXIe-5667**: This property is read-only when the :py:attr:`nirfsa.Session.LOW_FREQUENCY_BYPASS_ENABLED` property is set to :py:data:`~nirfsa.NIRFSA_VAL_DISABLED`.

        **Units**: dB

        **Default Value**: 0

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668



        .. note:: One or more of the referenced properties are not in the Python API for this driver.

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

                - LabVIEW Property: **Vertical:Mixer Level Offset (dB)**
                - C Attribute: **NIRFSA_ATTR_MIXER_LEVEL_OFFSET**

module_power_consumption
------------------------

    .. py:attribute:: module_power_consumption

        Returns the module power consumption.

        ----
        **Note**
        If you query this property during RF list mode, list steps may take longer to complete during list execution.

        ----

        **Units**: watts

        **Default Value**: N/A

        **Supported Devices:**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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
                - C Attribute: **NIRFSA_ATTR_MODULE_POWER_CONSUMPTION**

module_revision
---------------

    .. py:attribute:: module_revision

        Returns the revision of the RF downconverter module.

        ----
        **Note**
        For the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5840/5841, this property returns the revision of the VST module. For the PXIe-5830/5831/5832, this property returns the revision of the PXIe-3621/3622

        ----

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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
                - C Attribute: **NIRFSA_ATTR_MODULE_REVISION**

noise_source_power_enabled
--------------------------

    .. py:attribute:: noise_source_power_enabled

        Enables the 28 V DC source on the device front panel.

        **PXIe-5668 with PXIe-5698**: When this property is set to :py:data:`~nirfsa.NoiseSourcePowerEnabled.ENABLED`, the PXIe-5698 noise source is used instead of the PXIe-5668 noise source.

        **Units**: dB

        **Default Value**: :py:data:`~nirfsa.NoiseSourcePowerEnabled.DISABLED`

        **Supported Devices**: PXIe-5606, PXIe-5668, PXIe-5698

        **Defined Values**:

        +-----------------------------------------------------+----------------------------------+
        | Name                                                | Description                      |
        +=====================================================+==================================+
        | :py:data:`~nirfsa.NoiseSourcePowerEnabled.DISABLED` | Disables the noise source power. |
        +-----------------------------------------------------+----------------------------------+
        | :py:data:`~nirfsa.NoiseSourcePowerEnabled.ENABLED`  | Enables the noise source power.  |
        +-----------------------------------------------------+----------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------+
            | Characteristic        | Value                         |
            +=======================+===============================+
            | Datatype              | enums.NoiseSourcePowerEnabled |
            +-----------------------+-------------------------------+
            | Permissions           | read-write                    |
            +-----------------------+-------------------------------+
            | Repeated Capabilities | None                          |
            +-----------------------+-------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device Specific:5606:Noise Source Power Enabled**
                - C Attribute: **NIRFSA_ATTR_NOISE_SOURCE_POWER_ENABLED**

number_of_records
-----------------

    .. py:attribute:: number_of_records

        Specifies the number of records to acquire if the :py:attr:`nirfsa.Session.number_of_records_is_finite` property is set to True.

        **Default Value**: 1

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureNumberOfRecords`

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

                - LabVIEW Property: **Acquisition:IQ:Number Of Records**
                - C Attribute: **NIRFSA_ATTR_NUMBER_OF_RECORDS**

number_of_records_is_finite
---------------------------

    .. py:attribute:: number_of_records_is_finite

        Specifies whether the device stops after acquiring the specified number of records or acquires records continuously.

        **Defined Values**:

        | Value    | Description                                                  |
        |:---------|:--------------------------------------------------------------|
        | True  | Acquire a finite number of records.                           |
        | False | Acquire records continuously until you abort the acquisition. |

        **Default Value**: True

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureNumberOfRecords`

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

                - LabVIEW Property: **Acquisition:IQ:Number Of Records Is Finite**
                - C Attribute: **NIRFSA_ATTR_NUMBER_OF_RECORDS_IS_FINITE**

number_of_samples
-----------------

    .. py:attribute:: number_of_samples

        Specifies the number of samples to acquire.

        This property is valid only if the :py:attr:`nirfsa.Session.number_of_samples_is_finite` property is set to True.

        **Default Value**: 1,000

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureNumberOfSamples`

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

                - LabVIEW Property: **Acquisition:IQ:Number Of Samples**
                - C Attribute: **NIRFSA_ATTR_NUMBER_OF_SAMPLES**

number_of_samples_is_finite
---------------------------

    .. py:attribute:: number_of_samples_is_finite

        Specifies whether the device acquires a finite number of samples or acquires continuously.

        **Defined Values**:

        | Value    | Description                                          |
        |:---------|:------------------------------------------------------|
        | True  | Acquire a finite number of samples.                   |
        | False | Acquire continuously until you abort the acquisition. |

        **Default Value**: True

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `I/Q Modulation <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/iq-modulation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureNumberOfSamples`

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

                - LabVIEW Property: **Acquisition:IQ:Number Of Samples Is Finite**
                - C Attribute: **NIRFSA_ATTR_NUMBER_OF_SAMPLES_IS_FINITE**

number_of_spectral_lines
------------------------

    .. py:attribute:: number_of_spectral_lines

        Specifies the number of spectral lines expected with the current power spectrum configuration.

        If you do not configure this property, NI-RFSA selects an appropriate value based on the :py:attr:`nirfsa.Session.resolution_bandwidth` property. If you configure this property, NI-RFSA coerces the :py:attr:`nirfsa.Session.resolution_bandwidth` value based on the number of spectral lines requested and the value of the :py:attr:`nirfsa.Session.spectrum_span` property.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Acquisition:Spectrum:Number Of Spectral Lines**
                - C Attribute: **NIRFSA_ATTR_NUMBER_OF_SPECTRAL_LINES**

osp_data_scaling_factor
-----------------------

    .. py:attribute:: osp_data_scaling_factor

        Specifies the scaling factor applied to the time-domain voltage data in the IF digitizer.

        Use this property to maximize the dynamic range of the digitizer by increasing the maximum IF power the digitizer can measure without creating OSP overflows.

        Because of the device amplitude response, some wide-band signals normally attenuated by the downconverter go through the IF digitizer without causing an ADC overflow. During IF equalization, these wide-band digitizer input signals may become amplified. These amplified input signal values overflow the available numeric range used in the signal processing algorithm.

        You can use this property when OSP calculations would generate an overflow while applying digital filters to the data. The OSP module in the digitizer multiplies the time-domain signal amplitude, in volts, by the specified property value before further onboard processing. Set this property to a value less than 1 to avoid OSP overflow for near full-scale IF signals and to use the maximum dynamic range of the digitizer. NI-RFSA compensates for the specified OSP data scaling factor to ensure that the correct scaled data, in absolute levels, is always returned regardless of the value of this property.

        **Valid Values:**: 0.25 to 1.0

        **Default Values:**

        **PXI-5661, PXIe-5663/5663E/5665 (3.6 GHz)/5667 (3.6 GHz)/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860**: 1.0

        **PXIe-5665 (14 GHz)/5667 (7 GHz)**: 0.8

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Vertical:Advanced:OSP Data Scaling Factor**
                - C Attribute: **NIRFSA_ATTR_OSP_DATA_SCALING_FACTOR**

overflow_error_reporting
------------------------

    .. py:attribute:: overflow_error_reporting

        Configures error reporting for ADC and onboard signal processing overflows.

        Overflows lead to clipping of the waveform.

        **Default Value**: :py:data:`~nirfsa.OverflowErrorReporting.WARNING`

        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +----------------------------------------------------+--------------------------------------------------------------------------------------------------------+
        | Name                                               | Description                                                                                            |
        +====================================================+========================================================================================================+
        | :py:data:`~nirfsa.OverflowErrorReporting.WARNING`  | Configures NI-RFSA to return a warning when an ADC or onboard signal processing (OSP) overflow occurs. |
        +----------------------------------------------------+--------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.OverflowErrorReporting.DISABLED` | Configures NI-RFSA to not return an error or a warning when an ADC or OSP overflow occurs.             |
        +----------------------------------------------------+--------------------------------------------------------------------------------------------------------+

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

                - LabVIEW Property: **Vertical:Advanced:Overflow Error Reporting**
                - C Attribute: **NIRFSA_ATTR_OVERFLOW_ERROR_REPORTING**

phase_offset
------------

    .. py:attribute:: phase_offset

        Specifies the offset to apply to the initial I and Q phases.

        **Valid Values**: 0 to 180

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

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

                - LabVIEW Property: **Acquisition:IQ:Phase Offset**
                - C Attribute: **NIRFSA_ATTR_PHASE_OFFSET**

power_spectrum_units
--------------------

    .. py:attribute:: power_spectrum_units

        Specifies the units of the power spectrum.

        **Default Value**: :py:data:`~nirfsa.PowerSpectrumUnits.DBM`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +-----------------------------------------------------+---------------------------------------------+
        | Name                                                | Description                                 |
        +=====================================================+=============================================+
        | :py:data:`~nirfsa.PowerSpectrumUnits.DBM`           | Units are dB with reference to 1 milliwatt. |
        +-----------------------------------------------------+---------------------------------------------+
        | :py:data:`~nirfsa.PowerSpectrumUnits.VOLTS_SQUARED` | Units are in volts squared.                 |
        +-----------------------------------------------------+---------------------------------------------+
        | :py:data:`~nirfsa.PowerSpectrumUnits.DBMV`          | Units are dB with reference to 1 millivolt. |
        +-----------------------------------------------------+---------------------------------------------+
        | :py:data:`~nirfsa.PowerSpectrumUnits.DBUV`          | Units are dB with reference to 1 microvolt. |
        +-----------------------------------------------------+---------------------------------------------+
        | :py:data:`~nirfsa.PowerSpectrumUnits.VOLTS`         | Units are in volts.                         |
        +-----------------------------------------------------+---------------------------------------------+
        | :py:data:`~nirfsa.PowerSpectrumUnits.WATTS`         | Units are in watts.                         |
        +-----------------------------------------------------+---------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.PowerSpectrumUnits |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | None                     |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Power Spectrum Units**
                - C Attribute: **NIRFSA_ATTR_POWER_SPECTRUM_UNITS**

preselector_present
-------------------

    .. py:attribute:: preselector_present

        Returns whether a preselector is available on the RF downconverter module.

        **Defined Values**:

        | Value    | Description                                      |
        |:---------|:--------------------------------------------------|
        | True  | A preselector is available on the downconverter.  |
        | False | No preselector is available on the downconverter. |

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842

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

                - LabVIEW Property: **Device Characteristics:Preselector Present**
                - C Attribute: **NIRFSA_ATTR_PRESELECTOR_PRESENT**

ready_for_advance_event_terminal_name
-------------------------------------

    .. py:attribute:: ready_for_advance_event_terminal_name

        Returns the fully qualified signal name as a string.

        **Default Values**:

        **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>ReadyForAdvanceEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

        **PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>ReadyForAdvanceEvent</i>, where *ModuleName* is the name of your device in MAX.

        **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>ReadyForAdvanceEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

        **All other devices**: /<i>DigitizerName</i>ReadyForAdvanceEvent, where *DigitizerName* is the name associated with your digitizer module in MAX.

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.get_terminal_name`

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

                - LabVIEW Property: **Events:Ready For Advance:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME**

ready_for_ref_event_terminal_name
---------------------------------

    .. py:attribute:: ready_for_ref_event_terminal_name

        Returns the fully qualified signal name as a string.

        **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>ReadyForReferenceEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

        **PXIe-5820/5840/5841/5842**: /<i>ModuleName/<i>ai/0/<i>ReadyForReferenceEvent</i>, where *ModuleName* is the name of your device in MAX.

        **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>ReadyForReferenceEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

        **All other devices**: /<i>DigitizerName</i>/<i>ReadyForReferenceEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.get_terminal_name`

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

                - LabVIEW Property: **Events:Ready For Ref:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_READY_FOR_REF_EVENT_TERMINAL_NAME**

ready_for_start_event_terminal_name
-----------------------------------

    .. py:attribute:: ready_for_start_event_terminal_name

        Returns the fully qualified signal name as a string.

        **Default Values**:

        **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>ReadyForStartEvent</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

        **PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>ReadyForStartEvent</i>, where *ModuleName* is the name of your device in MAX.

        **PXIe-5860**: /<i>ModuleName/<i>ai</i>/<i>ChannelNumber</i>/<i>ReadyForStartEvent</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

        **All other devices**: /<i>DigitizerName</i>/<i>ReadyForStartEvent</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.get_terminal_name`

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

                - LabVIEW Property: **Events:Ready For Start:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_READY_FOR_START_EVENT_TERMINAL_NAME**

records_done
------------

    .. py:attribute:: records_done

        Returns the number of records the RF vector signal analyzer has acquired.

        **Default Value**: N/A

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Acquisition:Fetch:Records Done**
                - C Attribute: **NIRFSA_ATTR_RECORDS_DONE**

reference_level
---------------

    .. py:attribute:: reference_level

        Specifies the reference level, in dBm.

        The reference level represents the maximum expected power of an RF input signal.

        ----
        **Note**
        For the PXIe-5645, this property is ignored if you are using the I/Q ports.

        ----

        Refer to the :py:attr:`nirfsa.Session.external_gain` property for more information about how configuring an external gain and a reference level affect attenuation.

        **Default Value**: 0

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694, PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Improving Your Measurements <https://www.ni.com/docs/en-US/bundle/ni-rfsa-sfp/page/rfsasfp/measurement_guidelines.html>`_

        `Programming Attenuation-Related Properties and Properties Using NI-RFSA <https://www.ni.com/docs/en-US/bundle/pxie-5665-feature/page/programming-attenuation.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureReferenceLevel`

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

                - LabVIEW Property: **Vertical:Reference Level (dBm)**
                - C Attribute: **NIRFSA_ATTR_REFERENCE_LEVEL**

reference_level_headroom
------------------------

    .. py:attribute:: reference_level_headroom

        Specifies the margin NI-RFSA adds to the :py:attr:`nirfsa.Session.reference_level` property.

        The margin helps to avoid clipping and overflow warnings if the input signal exceeds the configured reference level.

        NI-RFSA configures the input gain to avoid clipping and associated overflow warnings as long as the instantaneous power of the input signal remains within the reference level plus the reference level headroom. If you know the input power of the signal precisely or have already included margin in the reference level, you may be able to improve the signal-to-noise ratio by reducing the reference level headroom.

        **Units**: dB

        **Default Value**:

        **PXIe-5830/5831/5832/5841/5842/5860**: 1 dB

        **PXIe-5840**: 0 dB

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

                - LabVIEW Property: **Vertical:Advanced:Reference Level Headroom (dB)**
                - C Attribute: **NIRFSA_ATTR_REFERENCE_LEVEL_HEADROOM**

ref_clock_rate
--------------

    .. py:attribute:: ref_clock_rate

        Specifies the Reference Clock rate, in Hz, of the signal present at the REF IN or CLK IN connector.

        This property is only valid when the :py:attr:`nirfsa.Session.ref_clock_source` property is set to :py:data:`~nirfsa.NIRFSA_VAL_CLK_IN`, :py:data:`~nirfsa.NIRFSA_VAL_REF_IN`, or :py:data:`~nirfsa.ReferenceClockSource.REF_IN_2`.

        **Valid Values**:

        **PXIe-5644/5645/5646, PXIe-5601/5663/5663E, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841**: 10 MHz

        **PXIe-5603/5605/5665/5667/5668**: 5 MHz to 100 MHz, in increments of 1 MHz

        **PXIe-5841 with PXIe-5655, PXIe-5842**: 10 MHz, 100 MHz, 270 MHz, and 3.84 MHz  *y*, where *y* is 4, 8, 16, 24, 25, or 32.

        **PXIe-5860**: 10 MHz, 100 MHz

        **Default Value**: 10 MHz

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_ref_clock`



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

                - LabVIEW Property: **Clocking:Ref Clock Rate**
                - C Attribute: **NIRFSA_ATTR_REF_CLOCK_RATE**

ref_clock_source
----------------

    .. py:attribute:: ref_clock_source

        Specifies the Reference Clock source.

        ----
        **Note**
        For the PXIe-5694, if your application requires an external LO source, set this property to :py:data:`~nirfsa.ReferenceClockSource.NONE`.

        ----

        **Default Values**:

        **PXIe-5694**: :py:data:`~nirfsa.ReferenceClockSource.REF_IN`

        **All other devices**: :py:data:`~nirfsa.ReferenceClockSource.ONBOARD_CLOCK`

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5694, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_ref_clock`

        **Defined Values**:

        +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
        +========================================================+===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ReferenceClockSource.NONE`           | No Reference Clock is required for the current device configuration. This value is valid only for the PXIe-5694 or the PXIe-5668.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
        +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceClockSource.ONBOARD_CLOCK`  | **PXI-5661 **NI-RFSA locks the NI-RFSA device to the PXI-5600 RF downconverter onboard clock.**PXIe-5663/5663E **NI-RFSA locks the PXIe-5663/5663E to the PXI/PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, connect the REF IN/OUT connector on the PXI/PXIe-5652 to the CLK IN terminal on the PXI5622.**PXIe-5665 **NI-RFSA locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622.**PXIe-5667 **NI-RFSA locks the PXIe-5667 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694.**PXIe-5668 **Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624.**PXIe-5830/5831 **For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector.**PXIe-5831/5832 with PXIe-5653 **Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector.**PXIe-5644/5645/5646, PXIe-5820/5840/5841 **Lock the NI-RFSA device to its onboard clock.**PXIe-5841 with PXIe-5655 **Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector.**PXIe-5842 **Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the User Manual for the instrument.**PXIe-5860 **Lock to the PXIe-5860 onboard clock.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
        +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceClockSource.REF_IN`         | **PXI-5661 **NI-RFSA locks the NI-RFSA device to the signal at the external FREQ REF IN connector on the PXI-5600**PXIe-5663/5663E **Connect the external signal to the PXI/PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, this configuration can only be used in external digitizer mode.**PXIe-5665 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the :py:attr:`nirfsa.Session.ref_clock_rate` property according to the frequency of your external clock signal.**PXIe-5667 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. If your external clock signal frequency is set to a frequency other than 10 MHz, set the :py:attr:`nirfsa.Session.ref_clock_rate` property according to the frequency of your external clock signal.**PXIe-5668 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the **clock rate** parameter according to the frequency of your external clock signal.**PXIe-5694 **Connect the Reference Clock signal to the REF/LO IN connector on the PXIe-5694 front panel.**PXIe-5644/5645/5646, PXIe-5820/5840/5841 **Lock the NI-RFSA device to the signal at the external REF IN connector.**PXIe-5830/5831 **For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831/5832, lock the external signal to the PXIe-3622 REF IN connector.**PXIe-5831/5832 with PXIe-5653 **Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector.**PXIe-5841 with PXIe-5655 **Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. **PXIe-5842 **Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the User Manual for the instrument. PXIe-5860 Lock to the signal at the REF IN connector on the PXIe-5860. |
        +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceClockSource.PXI_CLK`        | **PXI-5661 **NI-RFSA locks the NI-RFSA device to the PXI backplane clock using the PXI-5600. You must connect the PXI 10 MHz connector to the REF IN connector on the PXI-5600 front panel to use this option. **PXIe-5668 **Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624.**PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655/5842/5860 **Lock the device to the PXI backplane clock.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
        +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceClockSource.CLK_IN`         | **PXI-5661 **This configuration does not apply to the PXI-5661.**PXIe-5663/5663E **NI-RFSA locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXI/PXIe-5652.**PXIe-5665 **NI-RFSA locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the :py:attr:`nirfsa.Session.ref_clock_rate` property to 100 MHz.**PXIe-5667 **NI-RFSA locks the PXIe-5667 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. Set the :py:attr:`nirfsa.Session.ref_clock_rate` property to 100 MHz.**PXIe-5668 **Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the **clock rate** parameter to 100 MHz.**PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655/5842/5860 **This configuration does not apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
        +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceClockSource.PXI_CLK_MASTER` | **PXIe-5831/5832 with PXIe-5653 **NI-RFSA configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.**PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5644/5645/5646, PXIe-5820/5840/5841/5841 with PXIe-5655 /5842/5860**This configuration does not apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
        +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceClockSource.REF_IN_2`       | **PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655 **This configuration does not apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
        +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

                - LabVIEW Property: **Clocking:Ref Clock Source**
                - C Attribute: **NIRFSA_ATTR_REF_CLOCK_SOURCE**

ref_to_ref_trigger_holdoff
--------------------------

    .. py:attribute:: ref_to_ref_trigger_holdoff

        Specifies the minimum time, in seconds, that must elapse between Reference Triggers of two records.

        The device does not recognize the Reference Trigger of the next record before this minimum time elapses.

        **Units:**: seconds

        **Default Value**: 0

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Triggers:Ref:Advanced:Ref To Ref Trigger Holdoff (s)**
                - C Attribute: **NIRFSA_ATTR_REF_TO_REF_TRIGGER_HOLDOFF**

ref_trigger_delay
-----------------

    .. py:attribute:: ref_trigger_delay

        Specifies the trigger delay time, in seconds.

        The trigger delay time is the length of time the IF digitizer waits after it receives the trigger before it asserts the Reference Event.

        **Units:**: seconds

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Triggers:Ref:Advanced:Ref Trigger Delay (s)**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_DELAY**

ref_trigger_minimum_quiet_time
------------------------------

    .. py:attribute:: ref_trigger_minimum_quiet_time

        Specifies a time duration, in seconds, for which the signal must be quiet before the device arms the trigger.

        The signal is quiet when it is below the trigger level if the trigger slope, specified by the :py:attr:`nirfsa.Session.iq_power_edge_ref_trigger_slope` property, is set to :py:data:`~nirfsa.ReferenceTriggerIqPowerEdgeSlope.RISING` or when it is above the trigger level if the trigger slope is set to :py:data:`~nirfsa.ReferenceTriggerIqPowerEdgeSlope.FALLING`.

        By default, this value is set to 0, which means the device does not wait for a quiet time before arming the trigger. This property is useful to trigger the acquisition on signals containing repeated bursts, but for which each burst may have large changes in signal power within itself. By configuring the minimum quiet time to the time between bursts, you can ensure that the trigger occurs at the beginning of a burst rather than at the signal power change within a burst.

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Triggers:Ref:Minimum Quiet Time**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME**

ref_trigger_osp_delay_enabled
-----------------------------

    .. py:attribute:: ref_trigger_osp_delay_enabled

        Specifies whether the digitizer OSP block delays Reference Triggers, along with the data samples, moving through the OSP block or if the Reference Triggers bypass the OSP block and are processed immediately.

        Enabling this property requires the following equipment configurations:

        - All digitizers being used must be the same model and hardware revision.
        - All digitizers must use the same firmware.
        - All digitizers must be configured with the same I/Q rate.
        - All devices must use the same signal path.

        **PXIe-5663/5663E**: Read the value of the :py:attr:`nirfsa.Session.IF_FILTER` property to determine the IF filters used by the PXIe-5663/5663E.

        **PXIe-5665/5667/5668**:Refer to the device-specific information in the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property to determine the IF filters used by the PXIe-5665/5667/5668. If you set the :py:attr:`nirfsa.Session.fft_width` property, refer to the device-specific information for this property and the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property to determine the IF filters used. For frequencies less than 3.6 GHz, set the :py:attr:`nirfsa.Session.rf_preamp_enabled` to the same value for all devices.

        **PXIe-5665 14 GHz**: Set the :py:attr:`nirfsa.Session.downconverter_preselector_enabled` to the same value for all devices.

        If the I/Q rate is set programmatically for I/Q acquisitions, the following properties should be identical for the best device synchronization:

        - :py:attr:`nirfsa.Session.digital_if_equalization_enabled`
        - :py:attr:`nirfsa.Session.spectrum_osp_sampling_ratio`

        For spectrum acquisitions, the following properties should be identical for the best device synchronization:

        - :py:attr:`nirfsa.Session.spectrum_span`
        - :py:attr:`nirfsa.Session.resolution_bandwidth_type`
        - :py:attr:`nirfsa.Session.digital_if_equalization_enabled`
        - :py:attr:`nirfsa.Session.spectrum_osp_sampling_ratio`

        For more information about the digitizer OSP block and Reference Triggers, refer to the following topics in the *NI High-Speed Digitizers Help*:

        - NI 5622 Onboard Signal Processing (OSP)
        - NI 5142 Onboard Signal Processing (OSP)
        - NI PXIe-5622 Trigger Sources
        - NI PXI-5142 Trigger Sources
        - NI PXIe-5622 Block Diagram
        - NI PXI-5142 Trigger Sources

        **Default Value**: :py:data:`~nirfsa.ReferenceTriggerOspDelayEnabled.ENABLED`

        **Supported Devices**:PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841

        **Defined Values**:

        +-------------------------------------------------------------+-----------------------------------------------+
        | Name                                                        | Description                                   |
        +=============================================================+===============================================+
        | :py:data:`~nirfsa.ReferenceTriggerOspDelayEnabled.DISABLED` | Disables OSP delay for the Reference Trigger. |
        +-------------------------------------------------------------+-----------------------------------------------+
        | :py:data:`~nirfsa.ReferenceTriggerOspDelayEnabled.ENABLED`  | Enables OSP delay for the Reference Trigger.  |
        +-------------------------------------------------------------+-----------------------------------------------+

        .. note:: One or more of the referenced properties are not in the Python API for this driver.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------------+
            | Characteristic        | Value                                 |
            +=======================+=======================================+
            | Datatype              | enums.ReferenceTriggerOspDelayEnabled |
            +-----------------------+---------------------------------------+
            | Permissions           | read-write                            |
            +-----------------------+---------------------------------------+
            | Repeated Capabilities | None                                  |
            +-----------------------+---------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Advanced:OSP Delay Enabled**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_OSP_DELAY_ENABLED**

ref_trigger_pretrigger_samples
------------------------------

    .. py:attribute:: ref_trigger_pretrigger_samples

        Specifies the number of pretrigger samples the samples acquired before the Reference Trigger is received to be acquired per record.

        **Default Value**: 0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_digital_edge_ref_trigger`
        - :py:meth:`nirfsa.Session.configure_software_edge_ref_trigger`
        - :py:meth:`nirfsa.Session.ConfigureIqPowerEdgeRefTrigger`

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

                - LabVIEW Property: **Triggers:Ref:Pretrigger Samples**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_PRETRIGGER_SAMPLES**

ref_trigger_terminal_name
-------------------------

    .. py:attribute:: ref_trigger_terminal_name

        Returns the fully qualified signal name as a string.

        **Default Values**:

        **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>RefTrigger</i>, where *BasebandModule* is the name of your baseband module of your device in MAX.

        **PXIe-5820/5840/5841/5842**: /<i>ModuleName/<i>ai</i>/0/<i>RefTrigger</i>, where *ModuleName* is the name of your device in MAX.

        **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>RefTrigger</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

        **All other devices**: /<i>DigitizerName</i>/<i>RefTrigger</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.get_terminal_name`

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

                - LabVIEW Property: **Triggers:Ref:Terminal Name**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_TERMINAL_NAME**

ref_trigger_type
----------------

    .. py:attribute:: ref_trigger_type

        Specifies whether you want the Reference Trigger to be a digital edge, I/Q power edge, or software trigger.

        **Default Value**: :py:data:`~nirfsa.ReferenceTriggerType.NONE`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **Defined Values**:

        +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                   | Description                                                                                                                                                                                                                                                                 |
        +========================================================+=============================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.ReferenceTriggerType.NONE`           | No Reference Trigger is configured.                                                                                                                                                                                                                                         |
        +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceTriggerType.DIGITAL_EDGE`   | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the :py:attr:`nirfsa.Session.digital_edge_ref_trigger_source` property.                                                                            |
        +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceTriggerType.IQ_POWER_EDGE`  | The Reference Trigger is asserted when the signal is changing past the level specified with the slope (rising or falling) configured with the :py:attr:`nirfsa.Session.iq_power_edge_ref_trigger_slope` property.                                                           |
        +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceTriggerType.SOFTWARE_EDGE`  | The Reference Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the :py:meth:`nirfsa.Session.send_software_edge_trigger` method and selecting :py:data:`~nirfsa.NIRFSA_VAL_REF_TRIGGER` as the **trigger** parameter. |
        +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.ReferenceTriggerType.IQ_ANALOG_EDGE` | The Reference Trigger is asserted when the I or Q signal is changed past the level specified with the slope configured with the :py:attr:`nirfsa.Session.IQ_ANALOG_EDGE_REF_TRIGGER_SLOPE` property. This value is valid only for PXIe-5644/5645 devices.                   |
        +--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced properties are not in the Python API for this driver.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ReferenceTriggerType |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Ref:Type**
                - C Attribute: **NIRFSA_ATTR_REF_TRIGGER_TYPE**

resolution_bandwidth
--------------------

    .. py:attribute:: resolution_bandwidth

        Specifies the resolution along the x-axis of the spectrum.

        NI-RFSA uses the resolution bandwidth value to determine the acquisition size. If specified, the :py:attr:`nirfsa.Session.number_of_spectral_lines` property value overrides this value.

        **Units**: hertz (Hz)

        **Default Value**: 100 kHz

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.ConfigureResolutionBandwidth`

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

                - LabVIEW Property: **Acquisition:Spectrum:Resolution Bandwidth (Hz)**
                - C Attribute: **NIRFSA_ATTR_RESOLUTION_BANDWIDTH**

resolution_bandwidth_type
-------------------------

    .. py:attribute:: resolution_bandwidth_type

        Specifies how the :py:attr:`nirfsa.Session.resolution_bandwidth` property is expressed.

        **Default Value**: :py:data:`~nirfsa.SpectrumResolutionBandwidthType.THREE_DECIBELS`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                                          | Description                                                                                                                                              |
        +===============================================================================+==========================================================================================================================================================+
        | :py:data:`~nirfsa.SpectrumResolutionBandwidthType.THREE_DECIBELS`             | Defines the resolution bandwidth (RBW) in terms of the 3 dB bandwidth of the window specified by the :py:attr:`nirfsa.Session.fft_window_type` property. |
        +-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumResolutionBandwidthType.SIX_DECIBELS`               | Defines the RBW in terms of the 6 dB bandwidth of the window specified by the :py:attr:`nirfsa.Session.fft_window_type` property.                        |
        +-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumResolutionBandwidthType.BIN_WIDTH`                  | Defines the RBW in terms of the display resolution, which is the ratio of the sampling frequency to the number of samples that you acquire.              |
        +-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumResolutionBandwidthType.EQUIVALENT_NOISE_BANDWIDTH` | Defines the RBW in terms of the equivalent noise bandwidth (ENBW) of the window specified by the :py:attr:`nirfsa.Session.fft_window_type` property.     |
        +-------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------------+
            | Characteristic        | Value                                 |
            +=======================+=======================================+
            | Datatype              | enums.SpectrumResolutionBandwidthType |
            +-----------------------+---------------------------------------+
            | Permissions           | read-write                            |
            +-----------------------+---------------------------------------+
            | Repeated Capabilities | None                                  |
            +-----------------------+---------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Resolution Bandwidth Type**
                - C Attribute: **NIRFSA_ATTR_RESOLUTION_BANDWIDTH_TYPE**

rf_attenuation_step_size
------------------------

    .. py:attribute:: rf_attenuation_step_size

        Specifies the step size for the RF attenuation level.

        The actual RF attenuation is coerced up to the next highest multiple of this step size. You can also set this value to change the step size for the device within the supported device precision and configuration.

        **PXI-5600**: The device configuration supports only the following attenuation step size values: 10, 20, 30, 40, and 50.

        **PXIe-5601**: The attenuation is calculated based on the actual calibrated value closest to the desired value, so the step size varies as the actual gain values vary between consecutive attenuation settings.

        **PXIe-5603**: The device configuration supports attenuation changes in 1 dB steps.

        **PXIe-5605**: The available attenuation step size depends on the specified center frequency. In the high band signal path (input frequencies greater than 3.6 GHz), the only available attenuation is the step attenuator that you can change in 5 dB steps. In the low band signal path (input frequencies less than or equal to 3.6 GHz), an additional 31 dB of solid-state attenuation is available in 1 dB steps. The 5 dB default value indicates that, even when in the low band signal path, NI-RFSA changes the attenuation in 5 dB steps using only the mechanical attenuator. You can use this property to affect when the device changes the attenuation settings. To use the solid-state attenuation in the low band signal path, change the step size to a value other than a multiple of 5 (for example, a step size of 1 dB). If you use a value other than a multiple of 5 while in the high band of the PXIe-5605, NI-RFSA returns an error.

        **Units**: dB

        **Valid Values:**

        **PXI-5600/5661**: 10, 20, 30, 40, and 50

        **PXIe-5601/5663/5663E**: 0.0 to 93.0, continuous

        **PXIe-5603/5665 (3.6 GHz)**: 1.0 to 74.0, in 1 dB steps

        **PXIe-5605/5665 (14 GHz) (low band), PXIe-5606/5668 (low band)**: 1.0 to 106.0, in 1 dB steps

        **PXIe-5605/5665 (14 GHz) (high band), PXIe-5606/5668 (high band)**: 5.0 to 75.0, in 5 dB steps

        **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector low frequency bypass path**: 1.0 to 74.0, in 1 dB steps

        **PXIe-5667 (3.6 GHz) using the PXIe-5693 RF preselector filter path**:  1.0

        **PXIe-5667 (7 GHz) using the PXIe-5693 preselector low frequency bypass path**:  1.0 to 106.0 in 1 dB steps

        **PXIe-5667 (7 GHz) using the PXIe-5693 RF preselector filter path**:  1.0

        **Default Value:**

        **PXI-5600/5661**: 10.0

        **PXIe-5601/5663/5663E**: 0.0

        **PXIe-5603/5665 (3.6 GHz)**: 1.0

        **PXIe-5605/5665 (14 GHz), PXIe-5606/5668**: 5.0

        **PXIe-5667**: 1.0

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668

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

                - LabVIEW Property: **Vertical:Advanced:RF Attenuation Step Size (dB)**
                - C Attribute: **NIRFSA_ATTR_RF_ATTENUATION_STEP_SIZE**

rf_high_pass_filtering
----------------------

    .. py:attribute:: rf_high_pass_filtering

        Specifies the maximum corner frequency of the highpass filter in the RF signal path.

        The device uses the highest frequency highpass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables highpass filtering.

        For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this property returns the value you specified rather than a coerced value if multiple highpass filters are used during the acquisition.

        The PXIe-5606 features highpass filters at 1.35 GHz and 2.2 GHz.

        **Valid Values**: 0 to 26.5

        **Default Value**: 0

        **Supported Devices**: PXIe-5606, PXIe-5668

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

                - LabVIEW Property: **Signal Path:Advanced:RF Highpass Filtering**
                - C Attribute: **NIRFSA_ATTR_RF_HIGH_PASS_FILTERING**

rf_out_lo_export_enabled
------------------------

    .. py:attribute:: rf_out_lo_export_enabled

        Specifies whether to enable the RF OUT LO OUT terminal on the PXIe-5840/5841.

        When this property is enabled, if the :py:attr:`nirfsa.Session.lo_source` property is set to :py:data:`~nirfsa.LoSource.LO_IN` and you do not set the :py:attr:`nirfsa.Session.lo_frequency` or :py:attr:`nirfsa.Session.downconverter_center_frequency` properties, NI-RFSA rounds the LO frequency to approximately an LO step size as if the source was :py:data:`~nirfsa.LoSource.ONBOARD`. This ensures that when you configure NI-RFSA and NI-RFSG with compatible settings that result in the same LO frequency, the rounding also is compatible.

        **Default Value:**: :py:data:`~nirfsa.RfOutLoExport.UNSPECIFIED`

        **Supported Devices**: PXIe-5840/5841/5842

        **Defined Values**:

        +----------------------------------------------+----------------------------------------------------------------------------------------------------------------+
        | Name                                         | Description                                                                                                    |
        +==============================================+================================================================================================================+
        | :py:data:`~nirfsa.RfOutLoExport.DISABLED`    | The LO signal is not exported from the RF OUT LO OUT terminal.                                                 |
        +----------------------------------------------+----------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.RfOutLoExport.ENABLED`     | The LO signal is exported from the RF OUT LO OUT terminal.                                                     |
        +----------------------------------------------+----------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.RfOutLoExport.UNSPECIFIED` | The LO signal may or may not be exported to the RF OUT LO OUT terminal, because NI-RFSG may be controlling it. |
        +----------------------------------------------+----------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.RfOutLoExport |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | None                |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:RF Out LO Export Enabled**
                - C Attribute: **NIRFSA_ATTR_RF_OUT_LO_EXPORT_ENABLED**

rf_preamp_enabled
-----------------

    .. py:attribute:: rf_preamp_enabled

        Specifies whether the RF preamplifier is enabled in the system.

        **PXIe-5667, PXIe-5644/5645/5646, PXIe-5830/5831/5840/5841/5842**: The  :py:data:`~nirfsa.EnableRfPreamp.AUTOMATIC` value enables the RF preamplifier based on the value of the :py:attr:`nirfsa.Session.reference_level` property and the center frequency. Except on the PXIe-5830/5831/5832, NI-RFSA coerces this property from :py:data:`~nirfsa.EnableRfPreamp.AUTOMATIC` to the selected value.

        ----
        **Note**
        For the PXIe-5840/5841, the automatically selected value may not be optimal for all measurements. At some reference levels, :py:data:`~nirfsa.EnableRfPreamp.ENABLED` may improve the noise floor while :py:data:`~nirfsa.EnableRfPreamp.DISABLED` may improve distortion.

        ----

        **PXIe-5667**: The :py:data:`~nirfsa.EnableRfPreamp.AUTOMATIC` value is supported only when the :py:attr:`nirfsa.Session.LOW_FREQUENCY_BYPASS_ENABLED` property is set to :py:data:`~nirfsa.EnableRfPreamp.DISABLED`. If the reference level is greater than -25 dBm, NI-RFSA disables the preamplifier. If the reference level is less than or equal to -25 dBm, NI-RFSA sets the :py:attr:`nirfsa.Session.rf_preamp_enabled` property to :py:data:`~nirfsa.EnableRfPreamp.ENABLED_WHEN_IN_SIGNAL_PATH`.

        **PXIe-5668 with PXIe-5698**: If you set this property to :py:attr:`nirfsa.Session.rf_preamp_enabled`, only the preamplifier on the PXIe-5698 is used, and the preamplifier on the PXIe-5668 remains disabled.

        **Default Value**:

        **PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842**: :py:data:`~nirfsa.EnableRfPreamp.AUTOMATIC`

        **All other devices**: :py:data:`~nirfsa.EnableRfPreamp.DISABLED`

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5698, PXIe-5830/5831/5832/5840/5841/5842

        **Defined Values**:

        +---------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                                          | Description                                                                                                                                                                                                                                                                                                                                                                      |
        +===============================================================+==================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.EnableRfPreamp.DISABLED`                    | Disables the RF preamplifier.                                                                                                                                                                                                                                                                                                                                                    |
        +---------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.EnableRfPreamp.ENABLED_WHEN_IN_SIGNAL_PATH` | Enables the RF preamplifier when the RF preamplifier is present in the signal path and disables the preamplifier when it is not in the signal path. Only devices with an RF preamplifier on the downconverter and an RF preselector support this option. Use the :py:attr:`nirfsa.Session.rf_preamp_present` property to determine whether the downconverter has a preamplifier. |
        +---------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.EnableRfPreamp.ENABLED`                     | Enables the RF preamplifier. If the RF preamplifier is not in a signal path, NI-RFSA returns an error. Select the :py:data:`~nirfsa.EnableRfPreamp.ENABLED_WHEN_IN_SIGNAL_PATH` value whenever possible to avoid an error.                                                                                                                                                       |
        +---------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.EnableRfPreamp.AUTOMATIC`                   | Automatically enables the RF preamplifier based on the value of the :py:attr:`nirfsa.Session.reference_level` property. This value is valid only for the PXIe-5644/5645/5646, PXIe-5667, and PXIe-5830/5831/5832/5840/5841.                                                                                                                                                      |
        +---------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced properties are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.EnableRfPreamp |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Preamp Enabled**
                - C Attribute: **NIRFSA_ATTR_RF_PREAMP_ENABLED**

rf_preamp_present
-----------------

    .. py:attribute:: rf_preamp_present

        Returns whether an RF preamplifier is available on the RF downconverter module.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

        **Defined Values**:

        +-------+------------------------------------------------------+
        | Name  | Description                                          |
        +=======+======================================================+
        | True  | The device has an enabled RF preamplifier available. |
        +-------+------------------------------------------------------+
        | False | The device has no RF preamplifier available.         |
        +-------+------------------------------------------------------+

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

                - LabVIEW Property: **Device Characteristics:RF Preamp Present**
                - C Attribute: **NIRFSA_ATTR_RF_PREAMP_PRESENT**

selected_path
-------------

    .. py:attribute:: selected_path

        Specifies which path to configure to acquire a signal.

        **Default Value**: "" (empty string)

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
                - C Attribute: **NIRFSA_ATTR_SELECTED_PATH**

selected_ports
--------------

    .. py:attribute:: selected_ports

        Specifies the port to configure.

        ----
        **Note**
        When using RF list mode, ports cannot be shared with NI-RFSA.

        ----

        **Valid Values**:

        **PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: "" (empty string)

        **PXIe-5830**: if0, if1

        **PXIe-5831/5832**: if0, if1, rf <0-1> port <x>, where

        *0-1* indicates one (*0*) or two (*1*) mmRH-5582 connections and

        *x* is the port number on the mmRH-5582 front panel.

        **Default Value:**

        **PXIe-5830/5831/5832:**: if1

        **PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860**: "" (empty string)

        **Supported Devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        :py:attr:`nirfsa.Session.available_ports`

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

                - LabVIEW Property: **Signal Path:Advanced:Selected Ports**
                - C Attribute: **NIRFSA_ATTR_SELECTED_PORTS**

serial_number
-------------

    .. py:attribute:: serial_number

        Returns the serial number of the RF downconverter module.

        ----
        **Note**
        For the PXIe-5644/5645/5646 and PXIe-5820/5840/5841, this property returns the serial number of the VST module. For the PXIe-5830/5831/5832, this property returns the serial number of the PXIe-3621/3622.

        ----

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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
                - C Attribute: **NIRFSA_ATTR_SERIAL_NUMBER**

signal_bandwidth
----------------

    .. py:attribute:: signal_bandwidth

        Specifies the bandwidth of the input signal around the :py:attr:`nirfsa.Session.iq_carrier_frequency`.

        This value must be less than or equal to (0.8 7 [I/Q rate](:py:attr:`nirfsa.Session.iq_rate`.html)).

        NI-RFSA defines *signal bandwidth* as twice the maximum I/Q signal deviation from 0 Hz. Usually, the baseband signal center frequency is 0 Hz. In such cases, the signal bandwidth is simply the baseband signal's minimum frequency subtracted from its maximum frequency, or *f* < sub>max</sub> - *f*< sub>min</sub>.

        If you do not set this property, NI-RFSA uses the maximum available signal bandwidth. Depending on your device settings, setting this property enables certain optimizations. Based on the specified signal bandwidth, NI-RFSA decides the minimum equalized bandwidth and equalizer gain.

        ----
        **Note**
        You must set this property to enable the :py:attr:`nirfsa.Session.downconverter_frequency_offset_mode` property.

        ----

        Ensure you set the signal bandwidth wide enough to encompass all significant anticipated input power. In cases where NI-RFSA optimizes the input gain based on the signal bandwidth, significant input power outside the signal bandwidth can lead to clipping and associated overflow warnings if you do not have enough margin in your [reference level.](:py:attr:`nirfsa.Session.reference_level`.html)

        **Units**: Hz

        **Default Value**: 0 Hz

        **Supported Devices:**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `PXIe-5830 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5830-feature/page/frequency-and-bandwidth-selection.html>`_

        `PXIe-5831/5832 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5831/page/frequency-and-bandwidth-selection.html>`_

        `PXIe-5841 Frequency and Bandwidth Selection <https://www.ni.com/docs/en-US/bundle/pxie-5841/page/frequency-and-bandwidth-selection.html>`_

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

                - LabVIEW Property: **Acquisition:IQ:Signal Bandwidth (Hz)**
                - C Attribute: **NIRFSA_ATTR_SIGNAL_BANDWIDTH**

signal_conditioning_enabled
---------------------------

    .. py:attribute:: signal_conditioning_enabled

        Specifies whether all signal conditioning is enabled on the PXIe-5694.

        ----
        **Note**
        If you set this property to :py:data:`~nirfsa.SignalConditioningEnabled.BYPASSED`, NI-RFSA bypasses all signal conditioning, prevents any signal downconversion, and fixes the values for :py:attr:`nirfsa.Session.downconverter_gain` property, the :py:attr:`nirfsa.Session.device_instantaneous_bandwidth` property, and the :py:attr:`nirfsa.Session.if_filter_bandwidth` property.

        ----

        **Default Value**: :py:data:`~nirfsa.SignalConditioningEnabled.ENABLED`

        **Supported Devices**: PXIe-5694

        **Defined Values**:

        +-------------------------------------------------------+-----------------------------------+
        | Name                                                  | Description                       |
        +=======================================================+===================================+
        | :py:data:`~nirfsa.SignalConditioningEnabled.ENABLED`  | Enables signal conditioning.      |
        +-------------------------------------------------------+-----------------------------------+
        | :py:data:`~nirfsa.SignalConditioningEnabled.BYPASSED` | Bypasses all signal conditioning. |
        +-------------------------------------------------------+-----------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.SignalConditioningEnabled |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Signal Path:Advanced:NI 5694:Signal Conditioning Enabled**
                - C Attribute: **NIRFSA_ATTR_SIGNAL_CONDITIONING_ENABLED**

smooth_spectrum_enabled
-----------------------

    .. py:attribute:: smooth_spectrum_enabled

        Specifies that an optimized IF filtering selection is made at different spectrum frequency ranges during spectrum acquisition.

        The IF filter used depends on the configured RF center frequency, as shown in the following table.

        | Center Frequency    | IF Filter |
        |:--------------------|:----------|
        | 0 Hz and <80 MHz | 300 kHz   |
        | 0 MHz             | 50 MHz    |

        ----
        **Note**
        Setting this property to **Enabled** prevents you from setting :py:attr:`nirfsa.Session.if_filter_bandwidth` or :py:attr:`nirfsa.Session.device_instantaneous_bandwidth`.

        ----

        **Default Value**: :py:data:`~nirfsa.SmoothSpectrumEnabled.DISABLED`

        **Supported Devices**: PXIe-5665/5668

        **Defined Values**:

        +---------------------------------------------------+------------------------------+
        | Name                                              | Description                  |
        +===================================================+==============================+
        | :py:data:`~nirfsa.SmoothSpectrumEnabled.DISABLED` | Disables spectrum smoothing. |
        +---------------------------------------------------+------------------------------+
        | :py:data:`~nirfsa.SmoothSpectrumEnabled.ENABLED`  | Enables spectrum smoothing.  |
        +---------------------------------------------------+------------------------------+

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.SmoothSpectrumEnabled |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Smooth Spectrum Enabled**
                - C Attribute: **NIRFSA_ATTR_SMOOTH_SPECTRUM_ENABLED**

spectrum_averaging_mode
-----------------------

    .. py:attribute:: spectrum_averaging_mode

        Specifies the averaging mode for the spectrum acquisition.

        **Default Value**: :py:data:`~nirfsa.SpectrumAveragingMode.NO`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                               | Description                                                                                                                                                                                                                                                                                                                                                                                           |
        +====================================================+=======================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.SpectrumAveragingMode.NO`        | Configures NI-RFSA to perform no averaging on acquisitions.                                                                                                                                                                                                                                                                                                                                           |
        +----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumAveragingMode.RMS`       | Configures NI-RFSA for root-mean-square (RMS) averaging. RMS averaging reduces signal fluctuations but not the noise floor. RMS averaging averages the energy, or power, of the signal. This averaging prevents noise floor reduction and gives averaged RMS quantities of single-channel measurements zero phase. RMS averaging for dual-channel measurements preserves important phase information. |
        +----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumAveragingMode.VECTOR`    | Configures NI-RFSA for vector averaging. Vector averaging reduces noise from synchronous signals. Vector averaging computes the average of complex quantities directly, which means that it allows separate averaging for real and imaginary parts. Complex averaging such as vector averaging reduces noise and usually requires a trigger to improve block-to-block phase coherence.                |
        +----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumAveragingMode.PEAK_HOLD` | Configures NI-RFSA for peak-hold averaging. Peak-hold averaging retains the RMS peak levels of the averaged quantities. The peak-hold averaging process performs peak-hold at each frequency bin separately to retain peak RMS levels from one FFT record to the next.                                                                                                                                |
        +----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumAveragingMode.MIN_HOLD`  | Configures NI-RFSA to perform no averaging on acquisitions.                                                                                                                                                                                                                                                                                                                                           |
        +----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumAveragingMode.SCALAR`    | Configures NI-RFSA to perform no averaging on acquisitions.                                                                                                                                                                                                                                                                                                                                           |
        +----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.SpectrumAveragingMode.LOG`       | Configures NI-RFSA to perform no averaging on acquisitions.                                                                                                                                                                                                                                                                                                                                           |
        +----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.SpectrumAveragingMode |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Spectrum:Averaging Mode**
                - C Attribute: **NIRFSA_ATTR_SPECTRUM_AVERAGING_MODE**

spectrum_number_of_averages
---------------------------

    .. py:attribute:: spectrum_number_of_averages

        Specifies the number of acquisitions to average.

        The averaging process returns the final result after the number of averages is complete.

        **Default Value**: 10

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Acquisition:Spectrum:Number Of Averages**
                - C Attribute: **NIRFSA_ATTR_SPECTRUM_NUMBER_OF_AVERAGES**

spectrum_osp_sampling_ratio
---------------------------

    .. py:attribute:: spectrum_osp_sampling_ratio

        Specifies the oversampling ratio used by the digitizer onboard signal processing (OSP) when you are in spectrum acquisition mode. This property allows you to acquire a larger bandwidth in hardware and reduce that bandwidth in software, decreasing the possibility of hardware data path overflows.

        **PXIe-5644/5645/5646**: The only valid value for this property is 1.

        **Default Value**: 1.0

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Acquisition:Spectrum:Spectrum OSP Sampling Ratio**
                - C Attribute: **NIRFSA_ATTR_SPECTRUM_OSP_SAMPLING_RATIO**

spectrum_span
-------------

    .. py:attribute:: spectrum_span

        Specifies the frequency range of the computed spectrum in hertz (Hz).

        For example, if you specify a center frequency of 1 GHz and a span of 100 MHz, the spectrum ranges from 950 MHz to 1,050 MHz after zoom processing. This value may be coerced based on hardware settings and RF downconverter specifications.

        NI-RFSA performs multispan acquisitions by dividing the total requested span into equally sized subspans based on the device instantaneous bandwidth at the range of frequencies you specify. NI-RFSA combines these subspans to yield a multispan acquisition. You can use the :py:attr:`nirfsa.Session.fft_width` property to improve amplitude accuracy and avoid unwanted effects such as filter roll-off and spurs across the span you select.

        ----
        **Note**
        If you configure the spectrum span to a value larger than the hardware instantaneous bandwidth, NI-RFSA performs multiple acquisitions and combines them into a spectrum of the size you requested.

        ----

        ----
        **Note**
        For the PXIe-5663/5663E/5665/5667/5668, NI-RFSA enables dithering by default. The dither noise can appear in your passband and affect measurements. Refer to the :py:attr:`nirfsa.Session.digitizer_dither_enabled` property for more information about dithering.

        ----

        **PXIe-5663/5663E**: NI-RFSA does not support multispan acquisitions from frequency ranges that correspond with different instantaneous bandwidths. For example, you cannot configure a multispan acquisition that acquires one span from 110 MHz to 120 MHz and a second from 120 MHz to 130 MHz because the instantaneous bandwidth for frequencies above 120 MHz is different than instantaneous bandwidth for frequencies less than 120 MHz, which are 20 MHz and 10 MHz respectively.

        **PXIe-5665 (14 GHz)/5667 (7 GHz)**: If you enable the downconverter preselector filter, the device instantaneous bandwidth is only a typical specification.

        **Default Value**: 10 MHz

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5840/5841/5842/5860

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.configure_spectrum_frequency`

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

                - LabVIEW Property: **Acquisition:Spectrum:Span**
                - C Attribute: **NIRFSA_ATTR_SPECTRUM_SPAN**

start_to_ref_trigger_holdoff
----------------------------

    .. py:attribute:: start_to_ref_trigger_holdoff

        Specifies the minimum time, in seconds, that must elapse after the Start Trigger is received before the device recognizes a Reference Trigger.

        **Units:** seconds

        **Default Value**: 0

        **Supported Devices**: PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Triggers:Ref:Advanced:Start To Ref Trigger Holdoff (s)**
                - C Attribute: **NIRFSA_ATTR_START_TO_REF_TRIGGER_HOLDOFF**

start_trigger_terminal_name
---------------------------

    .. py:attribute:: start_trigger_terminal_name

        Returns the fully qualified signal name as a string.

        **Default Values**:

        **PXIe-5830/5831/5832**: /<i>BasebandModule</i>/<i>ai</i>/0/<i>StartTrigger</i>, where *BasebandModule* is the name of the baseband module of your device in MAX.

        **PXIe-5820/5840/5841/5842**: /<i>ModuleName</i>/<i>ai</i>/0/<i>StartTrigger</i>, where *ModuleName* is the name of your device in MAX.

        **PXIe-5860**: /<i>ModuleName</i>/<i>ai</i>/<i>ChannelNumber</i>/<i>StartTrigger</i>, where *ModuleName* is the name of your device in MAX and *ChannelNumber* is the channel number (0 or 1).

        **All other devices**: /<i>DigitizerName</i>/StartTrigger</i>, where *DigitizerName* is the name associated with your digitizer module in MAX.

        **Supported Devices**: PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Events <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/events.html>`_

        **High-Level Methods**:

        - :py:meth:`nirfsa.Session.get_terminal_name`

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
                - C Attribute: **NIRFSA_ATTR_START_TRIGGER_TERMINAL_NAME**

start_trigger_type
------------------

    .. py:attribute:: start_trigger_type

        Specifies whether you want the Start Trigger to be a digital edge or software trigger.

        ----
        **Note**
        Set this property to :py:data:`~nirfsa.StartTriggerType.NONE` if you set the :py:attr:`nirfsa.Session.acquisition_type` property to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` or if you set the **acquisitionType** parameter to :py:data:`~nirfsa.AcquisitionType.SPECTRUM` using the [cvi:py:meth:`nirfsa.Session.ConfigureAcquisitionType`](cvi:py:meth:`nirfsa.Session.ConfigureAcquisitionType`.html) method.

        ----

        **Default Value**: :py:data:`~nirfsa.StartTriggerType.NONE`

        **Supported Devices**: PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/ni-rfsa/page/ni-rfsa-triggers-vst.html>`_

        **Defined Values**:

        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                              | Description                                                                                                                                                                                                                                                                            |
        +===================================================+========================================================================================================================================================================================================================================================================================+
        | :py:data:`~nirfsa.StartTriggerType.NONE`          | No Start Trigger is configured.                                                                                                                                                                                                                                                        |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.StartTriggerType.DIGITAL_EDGE`  | The Start Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the :py:attr:`nirfsa.Session.digital_edge_start_trigger_source` property.                                                                                         |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nirfsa.StartTriggerType.SOFTWARE_EDGE` | The Start Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the :py:meth:`nirfsa.Session.send_software_edge_trigger` method and selecting :py:data:`~nirfsa.NIRFSA_VAL_START_TRIGGER` as the value of the **trigger** parameter. |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.StartTriggerType |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Type**
                - C Attribute: **NIRFSA_ATTR_START_TRIGGER_TYPE**

subspan_overlap
---------------

    .. py:attribute:: subspan_overlap

        Use subspan overlap process to eliminate or reduce analyzer spurs.

        To enable this feature, specify a non-zero percentage overlap between consecutive subspans in a spectrum acquisition.

        If a value greater than 0 is specified, then for each spectral line in the resulting spectrum, the driver acquires data twice with slightly different hardware settings, so that the analyzer spurs, if any, are present at different frequencies in the two acquisitions. Typically, LO frequency is shifted between the acquisitions causing analyzer spurs that are relative to the LO frequency, to move from one frequency to another. Those spurs, which are present in only one of the acquisitions for each spectral line, get removed.

        The subspan overlap feature will not remove any spurs from the Device Under Test or modify the signal being measured; unlike the analyzer spurs, the spurs in the signal being measured stay at a constant frequency in the two acquisitions.

        ----
        **Note**
        Subspan overlap process effectively is performing minimum averaging, which might reduce the measured noise floor level. NI-RFSA Spectrum Averaging can be enabled to minimize the effect of subspan overlap on the noise floor.

        ----

        ----
        **Note**
        NI-RFSA may apply further shifts to the specified value to accommodate fixed-frequency edges of components such as preselectors.

        ----

        **Valid Values**:

        **PXIe-5665/5668**: 0 to < 100

        **PXIe-5820/5830/5831/5832/5840/5841/5860**: 0

        **PXIe-5842**: 0, 50

        **Default Value**: 0

        **Supported Devices**: PXIe-5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        ----
        **Note**
        Subspan overlap will not be supported by PXIe-5842, if RMM-5585 (54GHz Frequency Extension) is connected.

        ----

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

                - LabVIEW Property: **Acquisition:Spectrum:Subspan Overlap**
                - C Attribute: **NIRFSA_ATTR_SUBSPAN_OVERLAP**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        Returns a comma-separated list of supported devices.

        **Default Value**: N/A

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXIe-5644/5645/5646, PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | list of str |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | None        |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NIRFSA_ATTR_SUPPORTED_INSTRUMENT_MODELS**

temperature_read_interval
-------------------------

    .. py:attribute:: temperature_read_interval

        Indicates the minimum time between temperature sensor readings in seconds.

        When you call the :py:meth:`nirfsa.Session.read_power_spectrum` method, the :py:meth:`nirfsa.Session.ReadIqSingleRecordComplexF64` method, or the :py:meth:`nirfsa.Session._initiate` method, NI-RFSA checks whether at least the amount of time specified by this property has elapsed before reading the hardware temperature.

        ----
        **Note**
        NI-RFSA ignores this property if you call the :py:meth:`nirfsa.Session.perform_thermal_correction` method or read the :py:attr:`nirfsa.Session.downconverter_gain` property.

        ----

        **Default Value**: 30 seconds

        **Supported Devices**: PXI-5600, PXIe-5601/5603/5605/5606 (external digitizer mode), PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5693/5694/5698, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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
                - C Attribute: **NIRFSA_ATTR_TEMPERATURE_READ_INTERVAL**

thermal_correction_headroom_range
---------------------------------

    .. py:attribute:: thermal_correction_headroom_range

        Specifies the expected thermal operating range of the instrument from the self-calibration temperature, in degrees Celsius, returned from the :py:attr:`nirfsa.Session.device_temperature` property.

        For example, if this property is set to 5.0, and the device is self-calibrated at 35 C, then you can expect to run the device from 30 C to 40 C with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance and ADC or DSP overflows.

        **Units:** degrees Celsius (C)

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

                - LabVIEW Property: **Vertical:Advanced:Thermal Correction Headroom Range (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_THERMAL_CORRECTION_HEADROOM_RANGE**

thermal_correction_temperature_resolution
-----------------------------------------

    .. py:attribute:: thermal_correction_temperature_resolution

        Specifies the temperature change required before NI-RFSA recalculates the thermal correction settings when entering the Running state.

        **Units:** degrees Celsius (C)

        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Default Values**:

        **PXIe-5830/5831/5832/5842/5860**: 0.2

        **PXIe-5840/5841**: 1.0

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

                - LabVIEW Property: **Vertical:Advanced:Thermal Correction Temperature Resolution (Degrees C)**
                - C Attribute: **NIRFSA_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION**

user_source_pulse_width
-----------------------

    .. py:attribute:: user_source_pulse_width

        Specifies the pulse width for the User Source.

        Use the :py:attr:`nirfsa.Session.user_source_pulse_width_units` property to set the units for the pulse width.

        **Default Value**: 200E(-9)

        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

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

                - LabVIEW Property: **Events:User Source:Pulse Width**
                - C Attribute: **NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH**

user_source_pulse_width_units
-----------------------------

    .. py:attribute:: user_source_pulse_width_units

        Specifies the pulse width units for the User Source.

        When the value is :py:data:`~nirfsa.UserSourcePulseWidthUnits.SECONDS`, it is assumed that the clock rate of the signal is the data clock. Use :py:data:`~nirfsa.UserSourcePulseWidthUnits.CLOCK_PERIODS` if the user source clock rate is anything else.

        **Default Value**: :py:data:`~nirfsa.UserSourcePulseWidthUnits.SECONDS`

        **Supported Devices**: PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Defined Values**:

        +------------------------------------------------------------+--------------------------+
        | Name                                                       | Description              |
        +============================================================+==========================+
        | :py:data:`~nirfsa.UserSourcePulseWidthUnits.SECONDS`       | Units are seconds.       |
        +------------------------------------------------------------+--------------------------+
        | :py:data:`~nirfsa.UserSourcePulseWidthUnits.CLOCK_PERIODS` | Units are clock periods. |
        +------------------------------------------------------------+--------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.UserSourcePulseWidthUnits |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:User Source:Pulse Width Units**
                - C Attribute: **NIRFSA_ATTR_USER_SOURCE_PULSE_WIDTH_UNITS**


NI-TClk Support
===============

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:class:`nitclk.SessionReference` for a complete list of attributes.


.. contents:: Session
