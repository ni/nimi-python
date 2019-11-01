.. py:module:: nisync

Session
=======

.. py:class:: Session(self, resource_name, id_query, reset_device)

    

    This method performs the following initialization actions: - Creates a
    new NI-Sync instrument driver session. - Opens a session to the
    specified device using the interface and address you specify for the
    Resource Name parameter. - If the ID Query parameter is set to True,
    this method queries the instrument ID and checks that it is valid for
    this instrument driver. - If the Reset parameter is set to True,
    this method resets the module to a known state. Returns a ViSession
    handle that you use to identify the instrument in all subsequent
    instrument driver method calls. - Returns an instrument handle that
    you use to identify the instrument in all subsequent instrument driver
    method calls.

    



    :param resource_name:
        

        Resource name of the switch module to initialize. The resource name is
        assigned in Measurement & Automation Explorer (MAX). Syntax PXI[bus
        number]::device number NI-DAQmx name Optional fields are shown in square
        brackets ([]).

        

        .. note:: VISA aliases are also valid for the resource name.
            Example resource names: Resource Name Description Dev1 DAQmx name
            PXI1Slot5 DAQmx name PXI0::15::INSTR PXI bus 0, device number 15
            PXI::15::INSTR PXI bus 0, device number 15 PXI4::9::INSTR PXI bus 4,
            device number 9


    :type resource_name: str

    :param id_query:
        

        This parameter is ignored. Because NI-Sync supports multiple timing and
        synchronization modules, it always queries the device to determine which
        device is installed. Valid Values: True - Query the device (Default
        Value) False - Do not query the device

        


    :type id_query: bool

    :param reset_device:
        

        Specify whether you want the to reset the timing and synchronization
        module during the initialization procedure. Valid Range: True (1) -
        Reset Device False (0) - Don't Reset (Default Value)

        


    :type reset_device: bool


Methods
=======

clear_clock
-----------

    .. py:currentmodule:: nisync.Session

    .. py:method:: clear_clock(terminal)

            This method clears a clock created by the :py:meth:`nisync.Session.create_clock`
            method. Once the clock is cleared, the associated terminal may be used
            for other operations. When this method is called, the specified line
            is tri-stated.

            



            :param terminal:


                An input string enumeration that specifies the terminal containing the
                digital signal that is the specified clock. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_PFI0` :py:data:`~nisync.NISYNC_VAL_PFI1` :py:data:`~nisync.NISYNC_VAL_PFI2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1` :py:data:`~nisync.NISYNC_VAL_PXITRIG2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`
                :py:data:`~nisync.NISYNC_VAL_ALL_CONNECTED` If :py:data:`~nisync.NISYNC_VAL_ALL_CONNECTED` is specified,
                all clocks created within the context of this session are cleared.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type terminal: str

clear_future_time_events
------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: clear_future_time_events(terminal)

            This method clears future time events created by the
            :py:meth:`nisync.Session.create_future_time_event` method that have not yet occurred. Once
            the future time events are cleared, the associated terminal can be used
            for other operations. When this method is called, the specified line
            is tri-stated.

            



            :param terminal:


                An input string enumeration that specifies the terminal that will no
                longer generate future time events. Valid Values: :py:data:`~nisync.NISYNC_VAL_PFI0`
                :py:data:`~nisync.NISYNC_VAL_PFI1` :py:data:`~nisync.NISYNC_VAL_PFI2` :py:data:`~nisync.NISYNC_VAL_PXITRIG0`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG1` :py:data:`~nisync.NISYNC_VAL_PXITRIG2` :py:data:`~nisync.NISYNC_VAL_PXITRIG3`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5` :py:data:`~nisync.NISYNC_VAL_PXITRIG6`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0` :py:data:`~nisync.NISYNC_VAL_PXISTAR1`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3` :py:data:`~nisync.NISYNC_VAL_PXISTAR4`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6` :py:data:`~nisync.NISYNC_VAL_PXISTAR7`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9` :py:data:`~nisync.NISYNC_VAL_PXISTAR10`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`
                :py:data:`~nisync.NISYNC_VAL_ALL_CONNECTED` If :py:data:`~nisync.NISYNC_VAL_ALL_CONNECTED` is specified,
                all future time events created within the context of this session are
                cleared.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type terminal: str

close
-----

    .. py:currentmodule:: nisync.Session

    .. py:method:: close()

            This method performs the following operations: - Closes the NI-Sync
            I/O session. - Destroys the NI-Sync session and all of its properties. -
            Deallocates any memory resources the NI-Sync driver uses. Note: If the
            session is locked, you must unlock the session before calling
            :py:meth:`nisync.Session._close`. Note: After calling :py:meth:`nisync.Session._close`, you cannot use the
            instrument driver again until you call :py:meth:`nisync.Session.init`. Note: If any clocks
            have been created with the :py:meth:`nisync.Session.create_clock` method in the context
            of this session and have not been cleared, this method clears them. If
            any future time events have been created with the
            :py:meth:`nisync.Session.create_future_time_event` method in the context of this session
            and have not occurred or been cleared, this method clears them. If any
            time stamp triggers have been enabled with the
            :py:meth:`nisync.Session.enable_time_stamp_trigger` method in the context of this session
            and have not been disabled, this method clears them.

            

            .. note:: This method is not needed when using the session context manager



configure_fpga
--------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: configure_fpga(fpga_program_path)

            This method programs the FPGA on the module with an alternate
            bitstream file. The bitstream is specified using an absolute path to a
            location on disk. NOTE: This method is an advanced operation and
            should be used with caution.

            



            :param fpga_program_path:


                This input specifies the full path to an FPGA bitstream file on disk.

                


            :type fpga_program_path: str

connect_clk_terminals
---------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: connect_clk_terminals(source_terminal, destination_terminal)

            This method connects a source clock terminal to a destination clock
            terminal. A clock terminal connection is characterized by its source
            terminal and destination terminal.

            



            :param source_terminal:


                This input specifies the source clock terminal to connect to the
                destination terminal. Valid Values: :py:data:`~nisync.NISYNC_VAL_CLKIN` (Default Value)
                :py:data:`~nisync.NISYNC_VAL_CLK10` :py:data:`~nisync.NISYNC_VAL_OSCILLATOR` :py:data:`~nisync.NISYNC_VAL_DDS`
                :py:data:`~nisync.NISYNC_VAL_PFILVDS0` :py:data:`~nisync.NISYNC_VAL_PFILVDS1` :py:data:`~nisync.NISYNC_VAL_PFILVDS2`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC0` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC1`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC3`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC4` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC5`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC6` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC7`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC8` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC9`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC10` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC11`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC12` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC13`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC14` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC15`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC16` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA`

                

                .. note:: Each
                    PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor
                    specific. Your chassis documentation may describe this mapping in
                    addition to the chassis.ini and pxisys.ini system description files the
                    PXI Specification requires.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source_terminal: str
            :param destination_terminal:


                This input specifies the destination clock terminal that the source
                terminal will connect to. Valid Values: :py:data:`~nisync.NISYNC_VAL_CLK10_IN` (Default
                Value) :py:data:`~nisync.NISYNC_VAL_CLKOUT` :py:data:`~nisync.NISYNC_VAL_BOARD_CLK` :py:data:`~nisync.NISYNC_VAL_PFILVDS0`
                :py:data:`~nisync.NISYNC_VAL_PFILVDS1` :py:data:`~nisync.NISYNC_VAL_PFILVDS2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA0`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA1` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA2`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA3` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA4`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA5` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA6`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA7` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA8`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA9` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA10`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA11` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA12`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA13` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA14`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA15` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA16`

                

                .. note:: Each
                    PXIe_DStarA trigger is mapped to a single slot. This mapping is vendor
                    specific. Your chassis documentation may describe this mapping in
                    addition to the chassis.ini and pxisys.ini system description files the
                    PXI Specification requires.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type destination_terminal: str

connect_sw_trig_to_terminal
---------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: connect_sw_trig_to_terminal(source_terminal, destination_terminal, synchronization_clock, invert, update_edge, delay)

            This method connects the global software trigger terminal to a
            destination trigger terminal. A software trigger terminal connection is
            characterized by its source terminal, destination terminal, and a
            synchronization clock. The signal at the destination terminal can be
            inverted, synchronized to the rising or falling edge of the
            synchronization clock, and delayed by up to 15 synchronization clock
            cycles.

            



            :param source_terminal:


                This input specifies the source software trigger terminal to connect to
                the destination terminal. Valid Values: :py:data:`~nisync.NISYNC_VAL_SWTRIG_GLOBAL`
                (Default Value)

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source_terminal: str
            :param destination_terminal:


                This input specifies the destination trigger terminal that the global
                software trigger terminal will connect to. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_PXITRIG0` (Default Value) :py:data:`~nisync.NISYNC_VAL_PXITRIG1`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG2` :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG5` :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR0` :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR3` :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR6` :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR9` :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR12` :py:data:`~nisync.NISYNC_VAL_PXISTAR13` :py:data:`~nisync.NISYNC_VAL_PXISTAR14`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR15` :py:data:`~nisync.NISYNC_VAL_PXISTAR16` :py:data:`~nisync.NISYNC_VAL_PXISTAR`
                :py:data:`~nisync.NISYNC_VAL_PFI0` :py:data:`~nisync.NISYNC_VAL_PFI1` :py:data:`~nisync.NISYNC_VAL_PFI2` :py:data:`~nisync.NISYNC_VAL_PFI3`
                :py:data:`~nisync.NISYNC_VAL_PFI4` :py:data:`~nisync.NISYNC_VAL_PFI5` :py:data:`~nisync.NISYNC_VAL_PFILVDS0`
                :py:data:`~nisync.NISYNC_VAL_PFILVDS1` :py:data:`~nisync.NISYNC_VAL_PFILVDS2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB0`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB1` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB2`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB3` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB4`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB5` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB6`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB7` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB8`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB9` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB10`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB11` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB12`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB13` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB14`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB15` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB16`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC`

                

                .. note:: Each PXI_Star and PXIe_DStarB trigger is
                    mapped to a single slot. This mapping is vendor specific. Your chassis
                    documentation may describe this mapping in addition to the chassis.ini
                    and pxisys.ini system description files the PXI Specification requires.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type destination_terminal: str
            :param synchronization_clock:


                This input specifies the synchronization clock to use to synchronize the
                destination terminal with the global software trigger terminal.

                

                .. note:: Asynchronous connections are not valid for software trigger terminal
                    connections.

                .. note:: The source of the synchronization clock for software trigger connections
                    is determined by the destination terminal trigger "zone" ("front" for
                    the PFI lines, and "rear" for the PXI\_Trig and PXI\_Star terminals).
                    The source of the synchronization clock for a given trigger zone can be
                    selected using the NISYNC\_ATTR\_FRONT\_SYNC\_CLK\_SRC (PFI zone) and
                    NISYNC\_ATTR\_REAR\_SYNC\_CLK\_SRC (PXI backplane zone) properties.
                    Valid Values: NISYNC\_VAL\_SYNC\_CLK\_FULLSPEED (Default Value)
                    NISYNC\_VAL\_SYNC\_CLK\_DIV1 NISYNC\_VAL\_SYNC\_CLK\_DIV2


            :type synchronization_clock: str
            :param invert:


                This input specifies whether or not the global software trigger terminal
                should be inverted at the destination terminal. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_DONT_INVERT` (Default Value) :py:data:`~nisync.NISYNC_VAL_INVERT`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type invert: int
            :param update_edge:


                This input specifies the synchronization clock update edge that the
                global software trigger should be propagated on. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_UPDATE_EDGE_RISING` (Default Value)
                :py:data:`~nisync.NISYNC_VAL_UPDATE_EDGE_FALLING`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type update_edge: int
            :param delay:


                This input specifies the number of seconds to delay the global software
                trigger pulse. The delay must be a multiple of the synchronization clock
                period. The global software trigger can be delayed up to 15 clock cycles
                for each route. Default Value: 0.00 seconds

                

                .. note:: This input is not
                    supported on the PXIe-6674.


            :type delay: float

connect_trig_terminals
----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: connect_trig_terminals(source_terminal, destination_terminal, synchronization_clock, invert, update_edge)

            This method connects a source trigger terminal to a destination
            trigger terminal. A trigger terminal connection is characterized by its
            source terminal, destination terminal, and a synchronization clock. The
            signal at the destination terminal can be inverted and synchronized to
            the rising or falling edge of the synchronization clock.

            



            :param source_terminal:


                This input specifies the source trigger terminal to connect to the
                destination terminal.

                

                .. note:: Each PXI\_Star and PXIe\_DStarC trigger is
                    mapped to a single slot. This mapping is vendor specific. Your chassis
                    documentation may describe this mapping in addition to the chassis.ini
                    and pxisys.ini system description files the PXI Specification requires.

                .. note:: The source of the synchronization clock for
                    trigger connections is determined by the destination terminal (either
                    the PFI sync clock zone or the backplane sync clock zone). Also, the two
                    divided versions of the synchronization clock are shared between the PFI
                    sync clock zone and the backplane sync clock zone. Valid Values:
                    NISYNC\_VAL\_PXITRIG0 (Default Value) NISYNC\_VAL\_PXITRIG1
                    NISYNC\_VAL\_PXITRIG2 NISYNC\_VAL\_PXITRIG3 NISYNC\_VAL\_PXITRIG4
                    NISYNC\_VAL\_PXITRIG5 NISYNC\_VAL\_PXITRIG6 NISYNC\_VAL\_PXITRIG7
                    NISYNC\_VAL\_PXISTAR0 NISYNC\_VAL\_PXISTAR1 NISYNC\_VAL\_PXISTAR2
                    NISYNC\_VAL\_PXISTAR3 NISYNC\_VAL\_PXISTAR4 NISYNC\_VAL\_PXISTAR5
                    NISYNC\_VAL\_PXISTAR6 NISYNC\_VAL\_PXISTAR7 NISYNC\_VAL\_PXISTAR8
                    NISYNC\_VAL\_PXISTAR9 NISYNC\_VAL\_PXISTAR10 NISYNC\_VAL\_PXISTAR11
                    NISYNC\_VAL\_PXISTAR12 NISYNC\_VAL\_PXISTAR13 NISYNC\_VAL\_PXISTAR14
                    NISYNC\_VAL\_PXISTAR15 NISYNC\_VAL\_PXISTAR16 NISYNC\_VAL\_PXISTAR
                    NISYNC\_VAL\_PFI0 NISYNC\_VAL\_PFI1 NISYNC\_VAL\_PFI2 NISYNC\_VAL\_PFI3
                    NISYNC\_VAL\_PFI4 NISYNC\_VAL\_PFI5 NISYNC\_VAL\_PFILVDS0
                    NISYNC\_VAL\_PFILVDS1 NISYNC\_VAL\_PFILVDS2 NISYNC\_VAL\_GND
                    NISYNC\_VAL\_SYNC\_CLK\_FULLSPEED NISYNC\_VAL\_SYNC\_CLK\_DIV1
                    NISYNC\_VAL\_SYNC\_CLK\_DIV2 NISYNC\_VAL\_CLKIN NISYNC\_VAL\_PXIEDSTARC0
                    NISYNC\_VAL\_PXIEDSTARC1 NISYNC\_VAL\_PXIEDSTARC2
                    NISYNC\_VAL\_PXIEDSTARC3 NISYNC\_VAL\_PXIEDSTARC4
                    NISYNC\_VAL\_PXIEDSTARC5 NISYNC\_VAL\_PXIEDSTARC6
                    NISYNC\_VAL\_PXIEDSTARC7 NISYNC\_VAL\_PXIEDSTARC8
                    NISYNC\_VAL\_PXIEDSTARC9 NISYNC\_VAL\_PXIEDSTARC10
                    NISYNC\_VAL\_PXIEDSTARC11 NISYNC\_VAL\_PXIEDSTARC12
                    NISYNC\_VAL\_PXIEDSTARC13 NISYNC\_VAL\_PXIEDSTARC14
                    NISYNC\_VAL\_PXIEDSTARC15 NISYNC\_VAL\_PXIEDSTARC16
                    NISYNC\_VAL\_PXIEDSTARB


            :type source_terminal: str
            :param destination_terminal:


                This input specifies the destination trigger terminal that the source
                terminal will connect to. Valid Values: :py:data:`~nisync.NISYNC_VAL_PXITRIG0`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG1` (Default Value) :py:data:`~nisync.NISYNC_VAL_PXITRIG2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR13` :py:data:`~nisync.NISYNC_VAL_PXISTAR14` :py:data:`~nisync.NISYNC_VAL_PXISTAR15`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR16` :py:data:`~nisync.NISYNC_VAL_PXISTAR` :py:data:`~nisync.NISYNC_VAL_PFI0`
                :py:data:`~nisync.NISYNC_VAL_PFI1` :py:data:`~nisync.NISYNC_VAL_PFI2` :py:data:`~nisync.NISYNC_VAL_PFI3` :py:data:`~nisync.NISYNC_VAL_PFI4`
                :py:data:`~nisync.NISYNC_VAL_PFI5` :py:data:`~nisync.NISYNC_VAL_PFILVDS0` :py:data:`~nisync.NISYNC_VAL_PFILVDS1`
                :py:data:`~nisync.NISYNC_VAL_PFILVDS2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB0` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB1`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB3`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB4` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB5`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB6` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB7`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB8` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB9`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB10` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB11`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB12` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB13`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB14` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB15`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB16` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC`

                

                .. note:: Each PXI_Star
                    and PXIe_DStarB trigger is mapped to a single slot. This mapping is
                    vendor specific. Your chassis documentation may describe this mapping in
                    addition to the chassis.ini and pxisys.ini system description files the
                    PXI Specification requires.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type destination_terminal: str
            :param synchronization_clock:


                This input specifies the synchronization clock to use to synchronize the
                destination terminal with the source terminal for this connection.

                

                .. note:: The source of the synchronization clock for trigger connections is
                    determined by the destination terminal trigger "zone" ("front" for the
                    PFI lines, and "rear" for the PXI_Trig and PXI_Star terminals). The
                    source of the synchronization clock for a given trigger zone can be
                    selected using the :py:attr:`nisync.Session.front_sync_clk_src` (PFI zone) and
                    :py:attr:`nisync.Session.rear_sync_clk_src` (PXI backplane zone) properties.
                    Valid Values: :py:data:`~nisync.NISYNC_VAL_SYNC_CLK_ASYNC`
                    :py:data:`~nisync.NISYNC_VAL_SYNC_CLK_FULLSPEED` :py:data:`~nisync.NISYNC_VAL_SYNC_CLK_DIV1`
                    :py:data:`~nisync.NISYNC_VAL_SYNC_CLK_DIV2`

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type synchronization_clock: str
            :param invert:


                This input specifies whether or not the signal at the source terminal
                should be inverted at the destination terminal.

                

                .. note:: The source and
                    destination must be connected synchronously for the signal to be
                    inverted. Valid Values: :py:data:`~nisync.NISYNC_VAL_DONT_INVERT` (Default Value)
                    :py:data:`~nisync.NISYNC_VAL_INVERT`

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type invert: int
            :param update_edge:


                This input specifies the synhronization clock update edge that a
                connected signal should be propagated on. Note that the source and
                destination terminals must be connected synchronously for this parameter
                to apply. Valid Values: :py:data:`~nisync.NISYNC_VAL_UPDATE_EDGE_RISING` (Default
                Value) :py:data:`~nisync.NISYNC_VAL_UPDATE_EDGE_FALLING`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type update_edge: int

create_clock
------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: create_clock(terminal, high_ticks, low_ticks, start_time_seconds, start_time_nanoseconds, start_time_fractional_nsecs, stop_time_seconds, stop_time_nanoseconds, stop_time_fractional_nsecs)

            This method creates a clock synchronized to the board time associated
            with the specified instrument handle. The terminal associated with this
            clock cannot be used for other operations until the clock is cleared
            with the :py:meth:`nisync.Session.clear_clock` method or the session is closed with the
            :py:meth:`nisync.Session.Close` method. When this method is called, the digital signal
            on the specified terminal is driven low until the clock starts.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :param terminal:


                An input string enumeration that specifies the terminal containing the
                digital signal that is the specified clock. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1` :py:data:`~nisync.NISYNC_VAL_PXITRIG2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type terminal: str
            :param high_ticks:


                An input integer that specifies the high ticks of the clock generated on
                the specified terminal. The clock resolution, which can be queried using
                the :py:attr:`nisync.Session.1588_CLK_RESOLUTION` property, determines the length
                of a tick.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type high_ticks: int
            :param low_ticks:


                An input integer that specifies the low ticks of the clock generated on
                the specified terminal. The clock resolution, which can be queried using
                the :py:attr:`nisync.Session.1588_CLK_RESOLUTION` property, determines the length
                of a tick.

                

                .. note:: One or more of the referenced properties are not in the Python API for this driver.


            :type low_ticks: int
            :param start_time_seconds:


                An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will start. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of seconds is assumed to be within the
                supported time range. Specify 0 to start the clock immediately.

                


            :type start_time_seconds: int
            :param start_time_nanoseconds:


                An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will start. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of nanoseconds is assumed to be within
                the supported time range. Specify 0 to start the clock immediately.

                


            :type start_time_nanoseconds: int
            :param start_time_fractional_nsecs:


                An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will start. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of fractional nanoseconds is assumed to
                be within the supported time range. Specify 0 to start the clock
                immediately.

                


            :type start_time_fractional_nsecs: int
            :param stop_time_seconds:


                An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will stop. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of seconds is assumed to be within the
                supported time range. Specify 0 to never stop the clock.

                


            :type stop_time_seconds: int
            :param stop_time_nanoseconds:


                An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will stop. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of nanoseconds is assumed to be within
                the supported time range. Specify 0 to never stop the clock.

                


            :type stop_time_nanoseconds: int
            :param stop_time_fractional_nsecs:


                An input integer that specifies a portion of the board time when the
                clock generated on the specified terminal will stop. Note that NI-Sync
                supports only the time range between 1 January 1970 and 1 January 2100.
                Therefore, the specified number of fractional nanoseconds is assumed to
                be within the supported time range. Specify 0 to never stop the clock.

                


            :type stop_time_fractional_nsecs: int

create_future_time_event
------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: create_future_time_event(terminal, output_level, time_seconds, time_nanoseconds, time_fractional_nanoseconds)

            This method creates a future time event that is synchronized to the
            board time associated with the specified session handle. To create
            multiple future time events, invoke this method multiple times. The
            terminal associated with this future time event cannot be used for
            operations other than generating future time events until the future
            time events are cleared with the :py:meth:`nisync.Session.clear_future_time_events` method
            or the session is closed with the :py:meth:`nisync.Session._close` method. When this
            method is invoked, the digital signal on the specified terminal is
            driven low until the first future time event occurs. Note: The NI-Sync
            family of devices uses the TAI timescale.

            



            :param terminal:


                An input string that specifies the terminal generating the digital
                signal whose state is set to the specified value. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_PFI0` :py:data:`~nisync.NISYNC_VAL_PFI1` :py:data:`~nisync.NISYNC_VAL_PFI2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1` :py:data:`~nisync.NISYNC_VAL_PXITRIG2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type terminal: str
            :param output_level:


                An input integer enumeration that specifies the level to set the digital
                signal to at the specified time. Valid Values: :py:data:`~nisync.NISYNC_VAL_LEVEL_LOW`
                :py:data:`~nisync.NISYNC_VAL_LEVEL_HIGH`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type output_level: int
            :param time_seconds:


                An input integer that specifies a portion of the board time that
                specifies when to change to the specified state of the digital signal on
                the specified terminal. Note that NI-Sync supports only the time range
                between 1 January 1970 and 1 January 2100. Therefore, the specified
                number of seconds is assumed to be within the supported time range.
                Specify 0 to generate the future time event immediately.

                


            :type time_seconds: int
            :param time_nanoseconds:


                An input integer that specifies a portion of the board time that
                specifies when to change to the specified state of the digital signal on
                the specified terminal. Note that NI-Sync supports only the time range
                between 1 January 1970 and 1 January 2100. Therefore, the specified
                number of nanoseconds is assumed to be within the supported time range.
                Specify 0 to generate the future time event immediately.

                


            :type time_nanoseconds: int
            :param time_fractional_nanoseconds:


                An input integer that specifies a portion of the board time that
                specifies when to change to the specified state of the digital signal on
                the specified terminal. Note that NI-Sync supports only the time range
                between 1 January 1970 and 1 January 2100. Therefore, the specified
                number of fractional nanoseconds is assumed to be within the supported
                time range. Specify 0 to generate the future time event immediately.

                


            :type time_fractional_nanoseconds: int

disable_gps_timestamping
------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: disable_gps_timestamping()

            This method disables timestamping enabled by
            :py:meth:`nisync.Session.EnableGPSTimestamping`.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



disable_irig_timestamping
-------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: disable_irig_timestamping(terminal_name)

            This method disables timestamping enabled by
            :py:meth:`nisync.Session.EnableIRIGTimestamping`. The associated terminal may be used for
            other operations once timestamping has been disabled.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :param terminal_name:


                An input string that specifies the terminal to which the IRIG input is
                connected.

                


            :type terminal_name: str

disable_time_stamp_trigger
--------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: disable_time_stamp_trigger(terminal)

            This method disables a time stamp trigger enabled by the
            :py:meth:`nisync.Session.enable_time_stamp_trigger` method. Once the time stamp trigger is
            disabled, the associated terminal may be used for other operations.

            



            :param terminal:


                An input string enumeration that specifies the terminal containing the
                digital signal that is the trigger to stop time stamping. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_PFI0` :py:data:`~nisync.NISYNC_VAL_PFI1` :py:data:`~nisync.NISYNC_VAL_PFI2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1` :py:data:`~nisync.NISYNC_VAL_PXITRIG2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`
                :py:data:`~nisync.NISYNC_VAL_ALL_CONNECTED` If :py:data:`~nisync.NISYNC_VAL_ALL_CONNECTED` is specified,
                all time stamp triggers enabled within the context of this session are
                disabled.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type terminal: str

disconnect_clk_terminals
------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: disconnect_clk_terminals(source_terminal, destination_terminal)

            This method disconnects a source clock terminal from a destination
            clock terminal.

            



            :param source_terminal:


                This input specifies the source clock terminal to disconnect from the
                destination terminal. The source and destination terminals must be
                connected for this operation to succeed. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_CLKIN` :py:data:`~nisync.NISYNC_VAL_CLK10` :py:data:`~nisync.NISYNC_VAL_OSCILLATOR`
                :py:data:`~nisync.NISYNC_VAL_DDS` :py:data:`~nisync.NISYNC_VAL_PFILVDS0` :py:data:`~nisync.NISYNC_VAL_PFILVDS1`
                :py:data:`~nisync.NISYNC_VAL_PFILVDS2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC0` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC1`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC3`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC4` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC5`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC6` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC7`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC8` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC9`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC10` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC11`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC12` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC13`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC14` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC15`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC16` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA`
                :py:data:`~nisync.NISYNC_VAL_ALL_CONNECTED` (Default Value)

                

                .. note:: Each PXIe_DStarC
                    trigger is mapped to a single slot. This mapping is vendor specific.
                    Your chassis documentation may describe this mapping in addition to the
                    chassis.ini and pxisys.ini system description files the PXI
                    Specification requires.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source_terminal: str
            :param destination_terminal:


                This input specifies the destination clock terminal that the source
                terminal will disconnect from. The source and destination must be
                connected for this operation to succeed. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_CLKIN` :py:data:`~nisync.NISYNC_VAL_CLK10_IN` :py:data:`~nisync.NISYNC_VAL_CLKOUT`
                :py:data:`~nisync.NISYNC_VAL_BOARD_CLK` :py:data:`~nisync.NISYNC_VAL_PFILVDS0` :py:data:`~nisync.NISYNC_VAL_PFILVDS1`
                :py:data:`~nisync.NISYNC_VAL_PFILVDS2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA0` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA1`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA3`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA4` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA5`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA6` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA7`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA8` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA9`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA10` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA11`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA12` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA13`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA14` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA15`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARA16` :py:data:`~nisync.NISYNC_VAL_ALL_CONNECTED` (Default Value)

                

                .. note:: Each PXIe_DStarA trigger is mapped to a single slot. This mapping
                    is vendor specific. Your chassis documentation may describe this mapping
                    in addition to the chassis.ini and pxisys.ini system description files
                    the PXI Specification requires.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type destination_terminal: str

disconnect_sw_trig_from_terminal
--------------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: disconnect_sw_trig_from_terminal(source_terminal, destination_terminal)

            This method disconnects the global software trigger terminal from a
            destination trigger terminal.

            



            :param source_terminal:


                This input specifies the source software trigger terminal to disconnect
                from the destination terminal. The global software trigger must be
                connected to the destination terminal for this operation to succeed.
                Valid Values: :py:data:`~nisync.NISYNC_VAL_SWTRIG_GLOBAL` (Default Value)

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source_terminal: str
            :param destination_terminal:


                This input specifies the destination trigger terminal that the global
                software trigger terminal will disconnect from. The global software
                trigger must be connected to the destination terminal for this operation
                to succeed. Valid Values: :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG2` :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG5` :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR0` :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR3` :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR6` :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR9` :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR12` :py:data:`~nisync.NISYNC_VAL_PXISTAR13` :py:data:`~nisync.NISYNC_VAL_PXISTAR14`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR15` :py:data:`~nisync.NISYNC_VAL_PXISTAR16` :py:data:`~nisync.NISYNC_VAL_PXISTAR`
                :py:data:`~nisync.NISYNC_VAL_PFI0` :py:data:`~nisync.NISYNC_VAL_PFI1` :py:data:`~nisync.NISYNC_VAL_PFI2` :py:data:`~nisync.NISYNC_VAL_PFI3`
                :py:data:`~nisync.NISYNC_VAL_PFI4` :py:data:`~nisync.NISYNC_VAL_PFI5` :py:data:`~nisync.NISYNC_VAL_PFILVDS0`
                :py:data:`~nisync.NISYNC_VAL_PFILVDS1` :py:data:`~nisync.NISYNC_VAL_PFILVDS2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB0`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB1` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB2`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB3` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB4`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB5` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB6`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB7` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB8`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB9` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB10`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB11` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB12`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB13` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB14`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB15` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB16`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC` :py:data:`~nisync.NISYNC_VAL_ALL_CONNECTED` (Default Value)

                

                .. note:: Each PXI_Star and PXIe_DStarB trigger is mapped to a single
                    slot. This mapping is vendor specific. Your chassis documentation may
                    describe this mapping in addition to the chassis.ini and pxisys.ini
                    system description files the PXI Specification requires.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type destination_terminal: str

disconnect_trig_terminals
-------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: disconnect_trig_terminals(source_terminal, destination_terminal)

            This method disconnects a source trigger terminal from a destination
            trigger terminal.

            



            :param source_terminal:


                This input specifies the source trigger terminal to disconnect from the
                destination terminal. The source and destination terminals must be
                connected for this operation to succeed. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1` :py:data:`~nisync.NISYNC_VAL_PXITRIG2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR13` :py:data:`~nisync.NISYNC_VAL_PXISTAR14` :py:data:`~nisync.NISYNC_VAL_PXISTAR15`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR16` :py:data:`~nisync.NISYNC_VAL_PXISTAR` :py:data:`~nisync.NISYNC_VAL_PFI0`
                :py:data:`~nisync.NISYNC_VAL_PFI1` :py:data:`~nisync.NISYNC_VAL_PFI2` :py:data:`~nisync.NISYNC_VAL_PFI3` :py:data:`~nisync.NISYNC_VAL_PFI4`
                :py:data:`~nisync.NISYNC_VAL_PFI5` :py:data:`~nisync.NISYNC_VAL_PFILVDS0` :py:data:`~nisync.NISYNC_VAL_PFILVDS1`
                :py:data:`~nisync.NISYNC_VAL_PFILVDS2` :py:data:`~nisync.NISYNC_VAL_GND` :py:data:`~nisync.NISYNC_VAL_SYNC_CLK_FULLSPEED`
                :py:data:`~nisync.NISYNC_VAL_SYNC_CLK_DIV1` :py:data:`~nisync.NISYNC_VAL_SYNC_CLK_DIV2`
                :py:data:`~nisync.NISYNC_VAL_CLKIN` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC0` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC1`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC3`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC4` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC5`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC6` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC7`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC8` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC9`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC10` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC11`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC12` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC13`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC14` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC15`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC16` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB`
                :py:data:`~nisync.NISYNC_VAL_ALL_CONNECTED` (Default Value)

                

                .. note:: Each PXI_Star and
                    PXIe_DStarC trigger is mapped to a single slot. This mapping is vendor
                    specific. Your chassis documentation may describe this mapping in
                    addition to the chassis.ini and pxisys.ini system description files the
                    PXI Specification requires.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source_terminal: str
            :param destination_terminal:


                This input specifies the destination trigger terminal that the source
                terminal disconnect from. The source and destination terminals must be
                connected for this operation to succeed. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1` :py:data:`~nisync.NISYNC_VAL_PXITRIG2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR13` :py:data:`~nisync.NISYNC_VAL_PXISTAR14` :py:data:`~nisync.NISYNC_VAL_PXISTAR15`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR16` :py:data:`~nisync.NISYNC_VAL_PXISTAR` :py:data:`~nisync.NISYNC_VAL_PFI0`
                :py:data:`~nisync.NISYNC_VAL_PFI1` :py:data:`~nisync.NISYNC_VAL_PFI2` :py:data:`~nisync.NISYNC_VAL_PFI3` :py:data:`~nisync.NISYNC_VAL_PFI4`
                :py:data:`~nisync.NISYNC_VAL_PFI5` :py:data:`~nisync.NISYNC_VAL_PFILVDS0` :py:data:`~nisync.NISYNC_VAL_PFILVDS1`
                :py:data:`~nisync.NISYNC_VAL_PFILVDS2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB0` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB1`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB2` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB3`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB4` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB5`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB6` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB7`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB8` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB9`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB10` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB11`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB12` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB13`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB14` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB15`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB16` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC`
                :py:data:`~nisync.NISYNC_VAL_ALL_CONNECTED` (Default Value)

                

                .. note:: Each PXI_Star and
                    PXIe_DStarB trigger is mapped to a single slot. This mapping is vendor
                    specific. Your chassis documentation may describe this mapping in
                    addition to the chassis.ini and pxisys.ini system description files the
                    PXI Specification requires.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type destination_terminal: str

enable_gps_timestamping
-----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: enable_gps_timestamping()

            This method enables timestamping of the GPS pulse per second
            synchronized to the board time associated with the specified instrument
            handle.

            



enable_irig_timestamping
------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: enable_irig_timestamping(irig_type, terminal_name)

            This method enables timestamping IRIG decodes synchronized to the
            board time associated with the specified instrument handle. The terminal
            associated with this timestamp cannot be used for other operations until
            timestamping is disabled with :py:meth:`nisync.Session.DisableIRIGTimestamping` or the
            session is closed with :py:meth:`nisync.Session._close`.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :param irig_type:


                An input integer enumeration of the IRIG input being supplied. Valid
                Values: :py:data:`~nisync.NISYNC_VAL_IRIG_TYPE_IRIGB_DC`
                :py:data:`~nisync.NISYNC_VAL_IRIG_TYPE_IRIGB_AM` (Default)

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type irig_type: int
            :param terminal_name:


                An input string that specifies the terminal to which the IRIG input is
                connected.

                


            :type terminal_name: str

enable_time_stamp_trigger
-------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: enable_time_stamp_trigger(terminal, active_edge)

            This method enables time stamping of a specified trigger synchronized
            to the board time associated with the specified session handle. The
            terminal associated with this time stamp trigger cannot be used for
            other operations until the time stamp trigger is disabled with the
            :py:meth:`nisync.Session.disable_time_stamp_trigger` method or the session is closed with
            the :py:meth:`nisync.Session.Close` method.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :param terminal:


                An input string enumeration that specifies the terminal containing the
                digital signal that is the trigger to start time stamping. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_PFI0` :py:data:`~nisync.NISYNC_VAL_PFI1` :py:data:`~nisync.NISYNC_VAL_PFI2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1` :py:data:`~nisync.NISYNC_VAL_PXITRIG2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type terminal: str
            :param active_edge:


                An input integer enumeration that specifies the trigger conditions.
                Valid Values: :py:data:`~nisync.NISYNC_VAL_EDGE_RISING` :py:data:`~nisync.NISYNC_VAL_EDGE_FALLING`
                :py:data:`~nisync.NISYNC_VAL_EDGE_ANY`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type active_edge: int

enable_time_stamp_trigger_with_decimation
-----------------------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: enable_time_stamp_trigger_with_decimation(terminal, active_edge, decimation_count)

            This method enables time stamping of a specified trigger synchronized
            to the board time associated with the specified session handle. The
            terminal associated with this time stamp trigger cannot be used for
            other operations until the time stamp trigger is disabled with the
            :py:meth:`nisync.Session.disable_time_stamp_trigger` method or the session is closed with
            the :py:meth:`nisync.Session.Close` method.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :param terminal:


                An input string enumeration that specifies the terminal containing the
                digital signal that is the trigger to start time stamping. Valid Values:
                :py:data:`~nisync.NISYNC_VAL_PFI0` :py:data:`~nisync.NISYNC_VAL_PFI1` :py:data:`~nisync.NISYNC_VAL_PFI2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1` :py:data:`~nisync.NISYNC_VAL_PXITRIG2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type terminal: str
            :param active_edge:


                An input integer enumeration that specifies the trigger conditions.
                Valid Values: :py:data:`~nisync.NISYNC_VAL_EDGE_RISING` :py:data:`~nisync.NISYNC_VAL_EDGE_FALLING`
                :py:data:`~nisync.NISYNC_VAL_EDGE_ANY`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type active_edge: int
            :param decimation_count:


                An input specifying how frequently to timestamp incoming trigger events.
                For example, if you pass in a value of 4, every fourth event is
                timestamped. The default is 1. This value must be greater than or equal
                to 1.

                


            :type decimation_count: int

error_message
-------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: error_message(error_code)

            This method converts a status code returned by an NI-Sync driver
            method into a user-readable string.

            



            :param error_code:


                Pass the Status parameter that is returned from any of the instrument
                driver methods. Default Value: 0 (VI_SUCCESS)

                


            :type error_code: int

            :rtype: str
            :return:


                    Returns the user-readable message string that corresponds to the status
                    code you specify. You must pass a ViChar array at least 256 bytes in
                    size.

                    



get_attribute_vi_boolean
------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: get_attribute_vi_boolean(active_item, attribute_id)

            This method sets the value of a ViBoolean property.

            



            :param active_item:


                Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

                


            :type active_item: str
            :param attribute_id:


                This parameter specifies the ID of the property you wish to get.

                


            :type attribute_id: int

            :rtype: bool
            :return:


                    Pass the value to which you want to set the property. From the method
                    panel window, you can use this control as follows. - If the property
                    currently showing in the Property ID ring control has constants as
                    valid values, you can view a list of the constants by pressing on this
                    control. Select a value by double-clicking on it or by selecting it and
                    then pressing .

                    

                    .. note:: Some of the values might not be valid depending on
                        the current settings of the instrument session. Default Value: none



get_attribute_vi_int32
----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: get_attribute_vi_int32(active_item, attribute_id)

            This method queries the value of a ViInt32 property.

            



            :param active_item:


                Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

                


            :type active_item: str
            :param attribute_id:


                This parameter specifies the ID of the property you wish to get.

                


            :type attribute_id: int

            :rtype: int
            :return:


                    Returns the current value of the property. Pass the address of a
                    ViInt32 variable. From the method panel window, you can use this
                    control as follows. - If the property currently showing in the
                    Property ID ring control has named constants as valid values, you can
                    view a list of the constants by pressing on this control. Select a value
                    by double-clicking on it or by selecting it and then pressing .

                    



get_attribute_vi_real64
-----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: get_attribute_vi_real64(active_item, attribute_id)

            This method queries the value of a ViReal64 property.

            



            :param active_item:


                Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

                


            :type active_item: str
            :param attribute_id:


                This parameter specifies the ID of the property you wish to get.

                


            :type attribute_id: int

            :rtype: float
            :return:


                    Returns the current value of the property. Pass the address of a
                    ViReal64 variable. From the method panel window, you can use this
                    control as follows. - If the property currently showing in the
                    Property ID ring control has named constants as valid values, you can
                    view a list of the constants by pressing on this control. Select a value
                    by double-clicking on it or by selecting it and then pressing .

                    



get_attribute_vi_string
-----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: get_attribute_vi_string(active_item, attribute_id)

            This method queries the value of a ViString property. You can use
            this method to get the values of instrument- specific properties and
            inherent IVI properties. If the property represents an instrument
            state, this method performs instrument I/O in the following cases: -
            State caching is disabled for the entire session or for the particular
            property. - State caching is enabled and the currently cached value is
            invalid. You must provide a ViChar array to serve as a buffer for the
            value. You pass the number of bytes in the buffer as the Buffer Size
            parameter. If the current value of the property, including the
            terminating NUL byte, is larger than the size you indicate in the Buffer
            Size parameter, the method copies Buffer Size - 1 bytes into the
            buffer, places an ASCII NUL byte at the end of the buffer, and returns
            the buffer size you must pass to get the entire value. For example, if
            the value is "123456" and the Buffer Size is 4, the method places
            "123" into the buffer and returns 7. If you want to call this method
            just to get the required buffer size, you can pass 0 for the Buffer Size
            and VI_NULL for the Property Value buffer. If you want the method to
            fill in the buffer regardless of the number of bytes in the value, pass
            a negative number for the Buffer Size parameter.

            



            :param active_item:


                Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

                


            :type active_item: str
            :param attribute_id:


                This parameter specifies the ID of the property you wish to get.

                


            :type attribute_id: int

            :rtype: str
            :return:


                    The buffer in which the method returns the current value of the
                    property. The buffer must be of type ViChar and have at least as many
                    bytes as indicated in the Buffer Size parameter. If the current value of
                    the property, including the terminating NUL byte, contains more bytes
                    that you indicate in this parameter, the method copies Buffer Size - 1
                    bytes into the buffer, places an ASCII NUL byte at the end of the
                    buffer, and returns the buffer size you must pass to get the entire
                    value. For example, if the value is "123456" and the Buffer Size is 4,
                    the method places "123" into the buffer and returns 7. If you specify
                    0 for the Buffer Size parameter, you can pass VI_NULL for this
                    parameter. From the method panel window, you can use this control as
                    follows. - If the property currently showing in the Property ID ring
                    control has named constants as valid values, you can view a list of the
                    constants by pressing on this control. Select a value by double-clicking
                    on it or by selecting it and then pressing .

                    



get_location
------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: get_location()

            This method returns the last calculated location of the onboard GPS
            receiver. The method returns latitude and longitude in degrees and
            altitude in meters. An external GPS antenna must be connected to receive
            valid data from this method. For best results, allow the GPS receiver
            to complete a self survey before reading location.

            



            :rtype: tuple (latitude, longitude, altitude)

                WHERE

                latitude (float): 


                    An input double pointer. The caller of this method must allocate a
                    ViReal64 and pass the pointer in this argument. The method sets the
                    ViReal64 value to the latitude reported by the onboard GPS receiver.
                    Negative values represent southern latitude. Positive values represent
                    northern latitude.

                    


                longitude (float): 


                    An input double pointer. The caller of this method must allocate a
                    ViReal64 and pass the pointer in this argument. The method sets the
                    ViReal64 value to the longitude reported by the onboard GPS receiver.
                    Negative values represent western longitude. Positive values represent
                    eastern longitude.

                    


                altitude (float): 


                    An input double pointer. The caller of this method must allocate a
                    ViReal64 and pass the pointer in this argument. The method sets the
                    ViReal64 value to the altitude reported by the onboard GPS receiver.
                    Returns current altitude in meters (WGS-84 earth ellipsoid).

                    



get_time
--------

    .. py:currentmodule:: nisync.Session

    .. py:method:: get_time()

            This method gets the board time associated with the specified session
            handle. Note: NI-Sync supports only the time range between 1 January
            1970 and 1 January 2100. Therefore, if the supported time range has
            ended, an error is returned. Note: The NI-Sync family of devices uses
            the TAI timescale

            



            :rtype: tuple (time_seconds, time_nanoseconds, time_fractional_nanoseconds)

                WHERE

                time_seconds (int): 


                    An output integer that specifies a portion of the board time.

                    


                time_nanoseconds (int): 


                    An output integer that specifies a portion of the board time.

                    


                time_fractional_nanoseconds (int): 


                    An output integer that specifies a portion of the board time.

                    



get_time_reference_names
------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: get_time_reference_names()

            TBD

            



            :rtype: str
            :return:


                    The buffer in which the method returns the current value of the
                    property. The buffer must be of type ViChar and have at least as many
                    bytes as indicated in the Buffer Size parameter. If the current value of
                    the property, including the terminating NUL byte, contains more bytes
                    that you indicate in this parameter, the method copies Buffer Size - 1
                    bytes into the buffer, places an ASCII NUL byte at the end of the
                    buffer, and returns the buffer size you must pass to get the entire
                    value. For example, if the value is "123456" and the Buffer Size is 4,
                    the method places "123" into the buffer and returns 7. If you specify
                    0 for the Buffer Size parameter, you can pass VI_NULL for this
                    parameter. From the method panel window, you can use this control as
                    follows. - If the property currently showing in the Property ID ring
                    control has named constants as valid values, you can view a list of the
                    constants by pressing on this control. Select a value by double-clicking
                    on it or by selecting it and then pressing .

                    



get_velocity
------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: get_velocity()

            This method returns the last calculated velocity of the onboard GPS
            receiver. The method returns east velocity, north velocity, and up
            velocity in meters per second. An external GPS antenna must be connected
            to receive valid data from this method, and the GPS receiver must be
            configured for Mobile Mode to receive nonzero velocity values.

            



            :rtype: tuple (east_velocity, north_velocity, up_velocity)

                WHERE

                east_velocity (float): 


                    An input double pointer. The caller of this method must allocate a
                    ViReal64 and pass the pointer in this argument. The method sets the
                    ViReal64 value to the eastVelocity reported by the onboard GPS receiver.
                    Negative values represent west velocity. Positive values represent east
                    velocity.

                    


                north_velocity (float): 


                    An input double pointer. The caller of this method must allocate a
                    ViReal64 and pass the pointer in this argument. The method sets the
                    ViReal64 value to the northVelocity reported by the onboard GPS
                    receiver. Negative values represent south velocity. Positive values
                    represent north velocity.

                    


                up_velocity (float): 


                    An input double pointer. The caller of this method must allocate a
                    ViReal64 and pass the pointer in this argument. The method sets the
                    ViReal64 value to the upVelocity reported by the onboard GPS receiver.
                    Negative values represent down velocity. Positive values represent up
                    velocity.

                    



init
----

    .. py:currentmodule:: nisync.Session

    .. py:method:: init(resource_name, id_query, reset_device)

            This method performs the following initialization actions: - Creates a
            new NI-Sync instrument driver session. - Opens a session to the
            specified device using the interface and address you specify for the
            Resource Name parameter. - If the ID Query parameter is set to True,
            this method queries the instrument ID and checks that it is valid for
            this instrument driver. - If the Reset parameter is set to True,
            this method resets the module to a known state. Returns a ViSession
            handle that you use to identify the instrument in all subsequent
            instrument driver method calls. - Returns an instrument handle that
            you use to identify the instrument in all subsequent instrument driver
            method calls.

            



            :param resource_name:


                Resource name of the switch module to initialize. The resource name is
                assigned in Measurement & Automation Explorer (MAX). Syntax PXI[bus
                number]::device number NI-DAQmx name Optional fields are shown in square
                brackets ([]).

                

                .. note:: VISA aliases are also valid for the resource name.
                    Example resource names: Resource Name Description Dev1 DAQmx name
                    PXI1Slot5 DAQmx name PXI0::15::INSTR PXI bus 0, device number 15
                    PXI::15::INSTR PXI bus 0, device number 15 PXI4::9::INSTR PXI bus 4,
                    device number 9


            :type resource_name: str
            :param id_query:


                This parameter is ignored. Because NI-Sync supports multiple timing and
                synchronization modules, it always queries the device to determine which
                device is installed. Valid Values: True - Query the device (Default
                Value) False - Do not query the device

                


            :type id_query: bool
            :param reset_device:


                Specify whether you want the to reset the timing and synchronization
                module during the initialization procedure. Valid Range: True (1) -
                Reset Device False (0) - Don't Reset (Default Value)

                


            :type reset_device: bool

            :rtype: int
            :return:


                    Returns a ViSession handle that you use to identify the instrument in
                    all subsequent instrument driver method calls.

                    

                    .. note:: Although you can
                        create more than one NI-Sync session for the same resource, it is best
                        not to do so. A better approach is to use the same NI-Sync session in
                        multiple execution threads. You can use VISA methods viLock and
                        viUnlock to protect sections of code that require exclusive access to
                        the resource.



measure_frequency
-----------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: measure_frequency(source_terminal, duration)

            This method measures the frequency of the signal at the specified
            terminal for a specified duration. The method returns the frequency,
            the calculated error, and the actual duration of the frequency
            measurement.

            



            :param source_terminal:


                This input specifies the source terminal of the signal to measure. Valid
                Values: :py:data:`~nisync.NISYNC_VAL_PFI0` (Default Value) :py:data:`~nisync.NISYNC_VAL_PFI1`
                :py:data:`~nisync.NISYNC_VAL_PFI2` :py:data:`~nisync.NISYNC_VAL_PFI3` :py:data:`~nisync.NISYNC_VAL_PFI4` :py:data:`~nisync.NISYNC_VAL_PFI5`
                :py:data:`~nisync.NISYNC_VAL_PFILVDS0` :py:data:`~nisync.NISYNC_VAL_PFILVDS1` :py:data:`~nisync.NISYNC_VAL_PFILVDS2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1` :py:data:`~nisync.NISYNC_VAL_PXITRIG2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR13` :py:data:`~nisync.NISYNC_VAL_PXISTAR14` :py:data:`~nisync.NISYNC_VAL_PXISTAR15`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR16` :py:data:`~nisync.NISYNC_VAL_PXISTAR` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC0`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC1` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC2`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC3` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC4`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC5` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC6`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC7` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC8`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC9` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC10`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC11` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC12`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC13` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC14`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC15` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC16`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB` :py:data:`~nisync.NISYNC_VAL_OSCILLATOR` :py:data:`~nisync.NISYNC_VAL_CLKIN`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source_terminal: str
            :param duration:


                This input specifies the duration of the frequency measurement, in units
                of seconds. The duration should be a multiple of the PXI_Clk10 signal
                period, i.e. it should be specified in multiples of 100 ns. If the
                duration is not a multiple of the PXI_Clk10 period, it will be coerced
                to the closest multiple. Default Value: 0.00000100 seconds

                


            :type duration: float

            :rtype: tuple (actual_duration, measured_frequency, frequency_error)

                WHERE

                actual_duration (float): 


                    This parameter returns the actual duration, in units of seconds, used in
                    the frequency measurement. The measurement duration will be a multiple
                    of the PXI_Clk10 period, i.e. it is a multiple of 100ns.

                    


                measured_frequency (float): 


                    This parameter returns the frequency measured at the PFI0 terminal, in
                    units of Hz. The measurable frequency range is approximately 0.1 Hz to
                    105 MHz.

                    


                frequency_error (float): 


                    This parameter returns the error calculated for the frequency
                    measurement. The formula used to calculate the error is: Measurement
                    Error = 1 / (Actual Duration) where "Actual Duration" is the value
                    returned in the Actual Duration parameter, i.e. the actual duration of
                    the measurement.

                    



measure_frequency_ex
--------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: measure_frequency_ex(source_terminal, duration, decimation_count)

            This method measures the frequency of the signal at the specified
            terminal for a specified duration. The method returns the frequency,
            the calculated error, and the actual duration of the frequency
            measurement.

            



            :param source_terminal:


                This input specifies the source terminal of the signal to measure. Valid
                Values: :py:data:`~nisync.NISYNC_VAL_PFI0` (Default Value) :py:data:`~nisync.NISYNC_VAL_PFI1`
                :py:data:`~nisync.NISYNC_VAL_PFI2` :py:data:`~nisync.NISYNC_VAL_PFI3` :py:data:`~nisync.NISYNC_VAL_PFI4` :py:data:`~nisync.NISYNC_VAL_PFI5`
                :py:data:`~nisync.NISYNC_VAL_PFILVDS0` :py:data:`~nisync.NISYNC_VAL_PFILVDS1` :py:data:`~nisync.NISYNC_VAL_PFILVDS2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1` :py:data:`~nisync.NISYNC_VAL_PXITRIG2`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4` :py:data:`~nisync.NISYNC_VAL_PXITRIG5`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7` :py:data:`~nisync.NISYNC_VAL_PXISTAR0`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2` :py:data:`~nisync.NISYNC_VAL_PXISTAR3`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5` :py:data:`~nisync.NISYNC_VAL_PXISTAR6`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8` :py:data:`~nisync.NISYNC_VAL_PXISTAR9`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11` :py:data:`~nisync.NISYNC_VAL_PXISTAR12`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR13` :py:data:`~nisync.NISYNC_VAL_PXISTAR14` :py:data:`~nisync.NISYNC_VAL_PXISTAR15`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR16` :py:data:`~nisync.NISYNC_VAL_PXISTAR` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC0`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC1` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC2`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC3` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC4`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC5` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC6`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC7` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC8`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC9` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC10`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC11` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC12`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC13` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC14`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC15` :py:data:`~nisync.NISYNC_VAL_PXIEDSTARC16`
                :py:data:`~nisync.NISYNC_VAL_PXIEDSTARB` :py:data:`~nisync.NISYNC_VAL_OSCILLATOR` :py:data:`~nisync.NISYNC_VAL_CLKIN`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source_terminal: str
            :param duration:


                This input specifies the duration of the frequency measurement, in units
                of seconds. The duration should be a multiple of the PXI_Clk10 signal
                period, i.e. it should be specified in multiples of 100 ns. If the
                duration is not a multiple of the PXI_Clk10 period, it will be coerced
                to the closest multiple. Default Value: 0.00000100 seconds

                


            :type duration: float
            :param decimation_count:


                


            :type decimation_count: int

            :rtype: tuple (actual_duration, measured_frequency, frequency_error)

                WHERE

                actual_duration (float): 


                    This parameter returns the actual duration, in units of seconds, used in
                    the frequency measurement. The measurement duration will be a multiple
                    of the PXI_Clk10 period, i.e. it is a multiple of 100ns.

                    


                measured_frequency (float): 


                    This parameter returns the frequency measured at the PFI0 terminal, in
                    units of Hz. The measurable frequency range is approximately 0.1 Hz to
                    105 MHz.

                    


                frequency_error (float): 


                    This parameter returns the error calculated for the frequency
                    measurement. The formula used to calculate the error is: Measurement
                    Error = 1 / (Actual Duration) where "Actual Duration" is the value
                    returned in the Actual Duration parameter, i.e. the actual duration of
                    the measurement.

                    



persist_config
--------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: persist_config()

            This method will copy the sync configuration from volatile storage to
            permanent storage.

            



read_current_temperature
------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: read_current_temperature()

            This method reads the current module temperature, in degrees celcius.
            Note: A calibration password is not required to use this method. It
            can be invoked with an instrument handle created with either
            :py:meth:`nisync.Session.init` or :py:meth:`nisync.Session.InitExtCal`.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :rtype: float
            :return:


                    This parameter returns the temperature, in degrees celcius, of the
                    timing and synchronization module.

                    



read_last_gps_timestamp
-----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: read_last_gps_timestamp()

            This method returns the last timestamp received of the GPS pulse per
            second. The read operation is a single-timestamp, nonblocking read. That
            is, the newest timestamp is returned. If no valid timestamp has ever
            been received, a value of zero is returned for the timestamp and the
            decoded time. A single timestamp can be read multiple times; only the
            reception of a subsequent timestamp updates the values returned. The
            method does not block waiting for a new timestamp to become available.
            Prior to calling :py:meth:`nisync.Session.ReadLastGPSTimestamp`, it is expected that
            timestamping has been enabled by calling :py:meth:`nisync.Session.EnableGPSTimestamping`.
            Note: The NI-Sync family of devices uses the TAI timescale. Note: You
            can combine the values returned in timestampSeconds,
            timestampNanoseconds, and timestampFractionalNanoseconds to get the
            board time the GPS pulse per second was received. You can combine the
            values returned in gpsSeconds, gpsNanoseconds, and
            gpsFractionalNanoseconds to get the time reported by the onboard GPS
            receiver.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :rtype: tuple (time_seconds, time_nanoseconds, time_fractional_nanoseconds, gps_seconds, gps_nanoseconds, gps_fractional_nanoseconds)

                WHERE

                time_seconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt32 and pass the pointer in this argument. The method sets the
                    ViUInt32 value to the seconds field of when the timestamp occurred.

                    


                time_nanoseconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt32 and pass the pointer in this argument. The method sets the
                    ViUInt32 value to the nanoseconds field of when the timestamp occurred.

                    


                time_fractional_nanoseconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt16 and pass the pointer in this argument. The method sets the
                    ViUInt16 value to the fractional nanoseconds field of when the timestamp
                    occurred.

                    


                gps_seconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt32 and pass the pointer in this argument. The method sets the
                    ViUInt32 value to the seconds field of time reported by the onboard GPS
                    receiver.

                    


                gps_nanoseconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt32 and pass the pointer in this argument. The method sets the
                    ViUInt32 value to the nanoseconds field of the time reported by the
                    onboard GPS receiver.

                    


                gps_fractional_nanoseconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt16 and pass the pointer in this argument. The method sets the
                    ViUInt16 value to the fractional nanoseconds field of the time reported
                    by the onboard GPS receiver.

                    



read_last_irig_timestamp
------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: read_last_irig_timestamp()

            This method returns the last IRIG timestamp received. The read
            operation is a single-timestamp, nonblocking read. That is, the newest
            timestamp is returned. If no valid timestamp has ever been received, a
            value of zero is returned for the timestamp and the decoded time. A
            single timestamp can be read multiple times; only the reception of a
            subsequent timestamp will update the values returned. The method does
            not block waiting for a new timestamp to become available. Prior to
            calling :py:meth:`nisync.Session.ReadLastIRIGTimestamp`, it is expected that timestamping
            has been enabled by calling :py:meth:`nisync.Session.EnableIRIGTimestamping`. Note: The
            NI-Sync family of devices uses the TAI timescale. Note: You can combine
            the values returned in timestampSeconds, timestampNanoseconds, and
            timestampFractionalNanoseconds to get the board time the IRIG message
            was received. You can combine the values returned in irigbSeconds,
            irigbNanoseconds, and irigbFractionalNanoseconds to get the time
            reported in the IRIG message.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :rtype: tuple (time_seconds, time_nanoseconds, time_fractional_nanoseconds, irig_seconds, irig_nanoseconds, irig_fractional_nanoseconds)

                WHERE

                time_seconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt32 and pass the pointer in this argument. The method sets the
                    ViUInt32 value to the seconds field of when the timestamp occurred.

                    


                time_nanoseconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt32 and pass the pointer in this argument. The method sets the
                    ViUInt32 value to the nanoseconds field of when the timestamp occurred.

                    


                time_fractional_nanoseconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt16 and pass the pointer in this argument. The method sets the
                    ViUInt16 value to the fractional nanoseconds field of when the timestamp
                    occurred.

                    


                irig_seconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt32 and pass the pointer in this argument. The method sets the
                    ViUInt32 value to the seconds field of time reported in the IRIG
                    message.

                    


                irig_nanoseconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt32 and pass the pointer in this argument. The method sets the
                    ViUInt32 value to the nanoseconds field of the time reported in the IRIG
                    message.

                    


                irig_fractional_nanoseconds (int): 


                    An input integer pointer. The caller of this method must allocate a
                    ViUInt16 and pass the pointer in this argument. The method sets the
                    ViUInt16 value to the fractional nanoseconds field of the time reported
                    in the IRIG message.

                    



read_multiple_trigger_time_stamp
--------------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: read_multiple_trigger_time_stamp(terminal, time_stamps_to_read, timeout)

            This method reads trigger time stamps from the internal software
            buffer for the specified terminal. The read operation is a destructive,
            blocking read. That is, the oldest unread time stamp associated with the
            specified terminal is returned. When a time stamp is read, it is removed
            from the buffer. The method does not return until the time stamps
            requested are available to be read, or the specified timeout elapses. If
            the internal software buffer associated with the specified terminal is
            full, time stamp operations for that terminal are suspended. Also, an
            error specifying that the internal software buffer overflowed is
            returned when the :py:meth:`nisync.Session.ReadMultipleTriggertimestamp` method is
            invoked. If the hardware time stamp buffer is full, all trigger time
            stamp operations are suspended. Also, an error specifying that the
            hardware time stamp buffer overflowed is returned when the
            :py:meth:`nisync.Session.ReadMultipleTriggertimestamp` method is invoked. That is, the
            :py:meth:`nisync.Session.ReadMultipleTriggertimestamp` method continues to return
            previously generated time stamps, despite the overflow condition, until
            no time stamps are available. To clear this error condition, the
            :py:meth:`nisync.Session.DisabletimestampTrigger` method must be invoked. Note that
            NI-Sync supports only the time range between 1 January 1970 and 1
            January 2100. Therefore, if the supported time range ends before a time
            stamp is captured, an error is returned. Note: If timestampsToRead is
            not equal to timestampsRead, the data held in the output arrays from
            index timestampsRead to the end of the arrays is uninitialized, and
            should be considered invalid.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :param terminal:


                An input string that specifies the terminal containing the digital
                signal that is the trigger whose oldest unread time stamp will be read.

                


            :type terminal: str
            :param time_stamps_to_read:


                An input integer specifying the number of time stamps to read. If the
                number of time stamps is not available before the timeout elapses, the
                number read before the timeout occurred is returned.

                


            :type time_stamps_to_read: int
            :param timeout:


                An input floating-point number that specifies the number of seconds to
                wait for a time stamp to be generated before returning a timeout error.

                


            :type timeout: float

            :rtype: tuple (time_seconds, time_nanoseconds, time_fractional_nanoseconds, detected_edge_buffer, time_stamps_read)

                WHERE

                time_seconds (int): 


                    An input pointer to an array of ViUInt32 values. The caller of this
                    method must allocate an array of ViUInt32s of size timestampsToRead
                    and pass the pointer to the array in this argument. The method sets
                    the values of the ViUInt32s to the seconds field of when the time stamp
                    occurred. After the method returns, index 0 holds the earliest
                    occurring seconds value, and the value returned in timestampsRead, minus
                    one, is the index in which the latest occurring seconds value is stored.

                    


                time_nanoseconds (int): 


                    An input pointer to an array of ViUInt32 values. The caller of this
                    method must allocate an array of ViUInt32s of size timestampsToRead
                    and pass the pointer to the array in this argument. The method sets
                    the values of the ViUInt32s to the nanoseconds field of when the time
                    stamp occurred. After the method returns, index 0 holds the earliest
                    occurring nanoseconds value, and the value returned in timestampsRead,
                    minus one, is the index in which the latest occurring nanoseconds value
                    is stored.

                    


                time_fractional_nanoseconds (int): 


                    An input pointer to an array of ViUInt16 values. The caller of this
                    method must allocate an array of ViUInt16s of size timestampsToRead
                    and pass the pointer to the array in this argument. The method sets
                    the values of the ViUInt16s to the fractional nanoseconds field of when
                    the time stamp occurred. After the method returns, index 0 holds the
                    earliest occurring fractional nanoseconds value, and the value returned
                    in timestampsRead, minus one, is the index in which the latest occurring
                    fractional nanoseconds value is stored.

                    


                detected_edge_buffer (int): 


                    An input pointer to an array of ViInt32s. The caller of this method
                    must allocate an array of ViUInt32s of size timestampsToRead and pass
                    the pointer to the array in this argument. After the method returns,
                    index 0 holds the earliest occurring detectedEdge value, and the value
                    returned in timestampsRead, minus one, is the index in which the latest
                    occurring detectedEdge value is stored. Each detectedEdge is an integer
                    enumeration that specifies the detected trigger condition. Valid Values:
                    :py:data:`~nisync.NISYNC_VAL_EDGE_RISING` :py:data:`~nisync.NISYNC_VAL_EDGE_FALLING`

                    

                    .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


                time_stamps_read (int): 


                    An input pointer to a ViUInt32. The caller of this method must
                    allocate a ViUInt32 and pass the pointer to the array in this argument.
                    When the method returns, the value at this pointer is set to the
                    number of actual time stamps read. This value may be different than
                    timestampsToRead if a timeout or other error occurs while reading time
                    stamps.

                    



read_trigger_time_stamp
-----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: read_trigger_time_stamp(terminal, timeout)

            This method reads a trigger time stamp from the internal software
            buffer for the specified terminal. The read operation is a
            single-time-stamp, destructive, blocking read. That is, the oldest
            unread time stamp associated with the specified terminal is returned.
            When a time stamp is read, it is removed from the buffer. The method
            does not return until a time stamp is available to be read or the
            specified timeout elapses. If the internal software buffer associated
            with the specified terminal is full, time stamp operations for that
            terminal are suspended and an error, specifying that the internal
            software buffer overflowed, is returned when the
            :py:meth:`nisync.Session.read_trigger_time_stamp` method is invoked. If the hardware
            time-stamp buffer is full, all trigger time stamp operations are
            suspended and an error, specifying that the hardware time-stamp buffer
            overflowed, is returned when the :py:meth:`nisync.Session.read_trigger_time_stamp` method
            is invoked. That is, the :py:meth:`nisync.Session.read_trigger_time_stamp` method continues
            to return previously generated time stamps, despite the overflow
            condition, until no time stamps are available. To clear this error
            condition, the :py:meth:`nisync.Session.disable_time_stamp_trigger` method must be invoked.
            Note: NI-Sync supports only the time range between 1 January 1970 and 1
            January 2100. Therefore, if the supported time range ends before a time
            stamp is captured, an error is returned. Note: The NI-Sync family of
            devices uses the TAI timescale.

            



            :param terminal:


                An input string enumeration that specifies the terminal containing the
                digital signal that is the trigger whose oldest unread time stamp will
                be read. Valid Values: :py:data:`~nisync.NISYNC_VAL_PFI0` :py:data:`~nisync.NISYNC_VAL_PFI1`
                :py:data:`~nisync.NISYNC_VAL_PFI2` :py:data:`~nisync.NISYNC_VAL_PXITRIG0` :py:data:`~nisync.NISYNC_VAL_PXITRIG1`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG2` :py:data:`~nisync.NISYNC_VAL_PXITRIG3` :py:data:`~nisync.NISYNC_VAL_PXITRIG4`
                :py:data:`~nisync.NISYNC_VAL_PXITRIG5` :py:data:`~nisync.NISYNC_VAL_PXITRIG6` :py:data:`~nisync.NISYNC_VAL_PXITRIG7`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR0` :py:data:`~nisync.NISYNC_VAL_PXISTAR1` :py:data:`~nisync.NISYNC_VAL_PXISTAR2`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR3` :py:data:`~nisync.NISYNC_VAL_PXISTAR4` :py:data:`~nisync.NISYNC_VAL_PXISTAR5`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR6` :py:data:`~nisync.NISYNC_VAL_PXISTAR7` :py:data:`~nisync.NISYNC_VAL_PXISTAR8`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR9` :py:data:`~nisync.NISYNC_VAL_PXISTAR10` :py:data:`~nisync.NISYNC_VAL_PXISTAR11`
                :py:data:`~nisync.NISYNC_VAL_PXISTAR12`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type terminal: str
            :param timeout:


                An input floating-point number that specifies the number of seconds to
                wait for a time stamp to be generated before returning a timeout error.
                Default Value: 10 seconds

                


            :type timeout: float

            :rtype: tuple (time_seconds, time_nanoseconds, time_fractional_nanoseconds, detected_edge)

                WHERE

                time_seconds (int): 


                    An output integer that specifies a portion of the board time when the
                    trigger associated with the specified terminal was detected.

                    


                time_nanoseconds (int): 


                    An output integer that specifies a portion of the board time when the
                    trigger associated with the specified terminal was detected.

                    


                time_fractional_nanoseconds (int): 


                    An output integer that specifies a portion of the board time when the
                    trigger associated with the specified terminal was detected.

                    


                detected_edge (int): 


                    An output integer enumeration that specifies the detected trigger
                    condition. Valid Values: :py:data:`~nisync.NISYNC_VAL_EDGE_RISING`
                    :py:data:`~nisync.NISYNC_VAL_EDGE_FALLING`

                    

                    .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



reset
-----

    .. py:currentmodule:: nisync.Session

    .. py:method:: reset()

            This method resets the module to a known state. Resetting the module
            performs the following operations: - All terminal connections are
            disconnected. - The DDS frequency is set to 0 Hz if DDS is supported. -
            All PFI front panel terminals are set to 50 input impedance. - The front
            (PFI) and rear (PXI backplane) zone synchronization clock sources are
            set to PXI_Clk10. Resetting the module performs the following
            operations on a timing and synchronization module capable of 1588. - Any
            participation in PTP is stopped. - The 1588 clock is reset to the
            current system time. - All clocks and future time events are cleared. -
            All time stamp triggers are disabled.

            



reset_frequency
---------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: reset_frequency()

            This method resets the internal frequency at which the board time
            increments to the default value.

            



revision_query
--------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: revision_query()

            This method returns the revision numbers of the NI-Sync driver and the
            firmware of the module.

            



            :rtype: tuple (instrument_driver_revision, firmware_revision)

                WHERE

                instrument_driver_revision (str): 


                    Returns the NI-Sync software revision numbers in the form of a string.

                    

                    .. note:: You must pass a ViChar array at least 256 bytes in size.


                firmware_revision (str): 


                    Returns the module firmware revision numbers in the form of a string.

                    

                    .. note:: You must pass a ViChar array at least 256 bytes in size.



self_test
---------

    .. py:currentmodule:: nisync.Session

    .. py:method:: self_test()

            This method runs the module's self test routine and returns the test
            result(s). Note: Currently, this operation does nothing.

            



            :rtype: tuple (self_test_result, self_test_message)

                WHERE

                self_test_result (int): 


                    This control contains the value returned from the instrument self test.
                    Zero means success. For any other code, see the device's operator's
                    manual. Self-Test Code Description
                    --------------------------------------- 0 Passed self test 1 Self test
                    failed

                    


                self_test_message (str): 


                    Returns the self-test response string from the instrument. See the
                    device's operation manual for an explanation of the string's contents.

                    

                    .. note:: You must pass a ViChar array at least 256 bytes in size.



send_software_trigger
---------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: send_software_trigger(source_terminal)

            This method sends a pulse on the global software trigger terminal. The
            global software trigger terminal must be connected to a destination
            terminal for this operation to have any effect.

            



            :param source_terminal:


                This input specifies the source software trigger terminal to send. When
                this method is invoked, the global software trigger will be sent
                simultaneously to all destination terminals that it is connected to.
                Valid Values: :py:data:`~nisync.NISYNC_VAL_SWTRIG_GLOBAL` (Default Value)

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type source_terminal: str

set_attribute_vi_boolean
------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: set_attribute_vi_boolean(active_item, attribute_id, attribute_value)

            This method sets the value of a ViBoolean property.

            



            :param active_item:


                Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

                


            :type active_item: str
            :param attribute_id:


                This parameter specifies the ID of the property you wish to set.

                


            :type attribute_id: int
            :param attribute_value:


                Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing .

                

                .. note:: Some of the values might not be valid depending on
                    the current settings of the instrument session. Default Value: none


            :type attribute_value: bool

set_attribute_vi_int32
----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: set_attribute_vi_int32(active_item, attribute_id, attribute_value)

            This method sets the value of a ViInt32 property.

            



            :param active_item:


                Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

                


            :type active_item: str
            :param attribute_id:


                This parameter specifies the ID of the property you wish to set.

                


            :type attribute_id: int
            :param attribute_value:


                Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing .

                

                .. note:: Some of the values might not be valid depending on
                    the current settings of the instrument session. Default Value: none


            :type attribute_value: int

set_attribute_vi_real64
-----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: set_attribute_vi_real64(active_item, attribute_id, attribute_value)

            This method sets the value of a ViReal64 property.

            



            :param active_item:


                Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

                


            :type active_item: str
            :param attribute_id:


                This parameter specifies the ID of the property you wish to set.

                


            :type attribute_id: int
            :param attribute_value:


                Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing .

                

                .. note:: Some of the values might not be valid depending on
                    the current settings of the instrument session. Default Value: none


            :type attribute_value: float

set_attribute_vi_string
-----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: set_attribute_vi_string(active_item, attribute_id, attribute_value)

            This method sets the value of a ViString property. This is a
            low-level method that you can use to set the values of
            instrument-specific properties and inherent IVI properties. If the
            property represents an instrument state, this method performs
            instrument I/O in the following cases: - State caching is disabled for
            the entire session or for the particular property. - State caching is
            enabled and the currently cached value is invalid or is different than
            the value you specify. This instrument driver contains high-level
            methods that set most of the instrument properties. It is best to use
            the high-level driver methods as much as possible. They handle order
            dependencies and multithread locking for you. In addition, they perform
            status checking only after setting all of the properties. In contrast,
            when you set multiple properties using the SetAttribute methods, the
            methods check the instrument status after each call. Also, when state
            caching is enabled, the high-level methods that configure multiple
            properties perform instrument I/O only for the properties whose value
            you change. Thus, you can safely call the high-level methods without
            the penalty of redundant instrument I/O.

            



            :param active_item:


                Since NI-Sync does not include any channel-based properties, this
                parameter is ignored. Default Value: ""

                


            :type active_item: str
            :param attribute_id:


                This parameter specifies the ID of the property you wish to set.

                


            :type attribute_id: int
            :param attribute_value:


                Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing .

                

                .. note:: Some of the values might not be valid depending on
                    the current settings of the instrument session. Default Value: none


            :type attribute_value: str

set_time
--------

    .. py:currentmodule:: nisync.Session

    .. py:method:: set_time(time_source, time_seconds, time_nanoseconds, time_fractional_nanoseconds)

            This method sets the absolute board time to the time specified. This
            method leaves the internal frequency at which the board time
            increments unchanged. Note: The NI-Sync family of devices uses the TAI
            timescale.

            



            :param time_source:


                An input integer enumeration that specifies the time source for the
                board time. Valid Values: :py:data:`~nisync.NISYNC_VAL_INIT_TIME_SRC_SYSTEM_CLK`
                (Default) :py:data:`~nisync.NISYNC_VAL_INIT_TIME_SRC_MANUAL`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type time_source: int
            :param time_seconds:


                An integer that specifies the seconds portion of the time to which the
                board time will be set. Note that NI-Sync supports setting the initial
                time between 0 hours on 1 January 1970 and 0 hours on 1 January 2100.
                This parameter is ignored unless the timeSource parameter is set to
                :py:data:`~nisync.NISYNC_VAL_INIT_TIME_SRC_MANUAL`.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type time_seconds: int
            :param time_nanoseconds:


                An integer that specifies the nanoseconds portion of the time to which
                the board time will be set. Note that NI-Sync supports setting the
                initial time between 0 hours on 1 January 1970 and 0 hours on 1 January
                2100. This parameter is ignored unless the timeSource parameter is set
                to :py:data:`~nisync.NISYNC_VAL_INIT_TIME_SRC_MANUAL`.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type time_nanoseconds: int
            :param time_fractional_nanoseconds:


                An integer that specifies the fractional nanoseconds portion of the time
                to which the board time will be set. Note that NI-Sync supports setting
                the initial time between 0 hours on 1 January 1970 and 0 hours on 1
                January 2100. This parameter is ignored unless the timeSource parameter
                is set to :py:data:`~nisync.NISYNC_VAL_INIT_TIME_SRC_MANUAL`.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type time_fractional_nanoseconds: int

set_time_reference1588_ordinary_clock
-------------------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: set_time_reference1588_ordinary_clock()

            This method sets the time reference of the device associated with the
            specified instrument handle. The time reference set is used to update
            the value and frequency of the board time such that the board time
            reflects the time reference's time as closely as possible. The board
            time is then used for tasks such as creating future time events, clocks,
            and timestamping triggers. This method is a nonblocking call that
            returns immediately regardless of the state of the time reference set.
            Setting the time reference is a systemwide (per device) configuration
            that persists after the session exits. The time reference is not
            reservable; the last call to set the time reference takes precedence. If
            the time reference set is not providing valid time information, the
            board time free runs from the last known time at the last frequency that
            was applied. Note: When a device's board time and the configured time
            reference's time vary by more than 1 ms, a macro phase adjustment may be
            necessary. A macro phase adjustment is when the board time is adjusted
            by a significant amount and, therefore, the board time no longer
            atomically increments. This should not occur on a well designed and
            stable time reference. If this occurs, future time events, clocks, and
            time stamps may be affected. If the board time is set forward, future
            time events and clock transitions that were missed occur immediately. If
            the board time is set backward, future time events and clock transitions
            are delayed. Note: An alternative to calling this method is to
            configure the default configured Time Reference through Measurement &
            Automation Explorer. The state configured is then reapplied at every
            restart. Note: Closing the session that calls this VI does not alter the
            value of the configured Time Reference. Note: The NI-Sync family of
            devices uses the TAI timescale. This method sets the Time Reference of
            the device to 1588.

            



set_time_reference_free_running
-------------------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: set_time_reference_free_running()

            This method sets the time reference of the device associated with the
            specified instrument handle. The time reference set is used to update
            the value and frequency of the board time such that the board time
            reflects the time reference's time as closely as possible. The board
            time is then used for tasks such as creating future time events, clocks,
            and timestamping triggers. This method is a nonblocking call that
            returns immediately regardless of the state of the time reference set.
            Setting the time reference is a systemwide (per device) configuration
            that persists after the session exits. The time reference is not
            reservable; the last call to set the time reference takes precedence. If
            the time reference set is not providing valid time information, the
            board time free runs from the last known time at the last frequency that
            was applied. Note: When a device's board time and the configured time
            reference's time vary by more than 1 ms, a macro phase adjustment may be
            necessary. A macro phase adjustment is when the board time is adjusted
            by a significant amount and, therefore, the board time no longer
            atomically increments. This should not occur on a well designed and
            stable time reference. If this occurs, future time events, clocks, and
            time stamps may be affected. If the board time is set forward, future
            time events and clock transitions that were missed occur immediately. If
            the board time is set backward, future time events and clock transitions
            are delayed. Note: An alternative to calling this method is to
            configure the default configured Time Reference through Measurement &
            Automation Explorer. The state configured is then reapplied at every
            restart. Note: Closing the session that calls this VI does not alter the
            value of the configured Time Reference. Note: The NI-Sync family of
            devices uses the TAI timescale. This method sets the Time Reference of
            the device to free running. The board time is guaranteed to atomically
            increment at the last calculated frequency. No external stimuli will
            alter the board time or frequency.

            



set_time_reference_gps
----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: set_time_reference_gps()

            This method sets the time reference of the device associated with the
            specified instrument handle. The time reference set is used to update
            the value and frequency of the board time such that the board time
            reflects the time reference's time as closely as possible. The board
            time is then used for tasks such as creating future time events, clocks,
            and timestamping triggers. This method is a nonblocking call that
            returns immediately regardless of the state of the time reference set.
            Setting the time reference is a systemwide (per device) configuration
            that persists after the session exits. The time reference is not
            reservable; the last call to set the time reference takes precedence. If
            the time reference set is not providing valid time information, the
            board time free runs from the last known time at the last frequency that
            was applied. Note: When a device's board time and the configured time
            reference's time vary by more than 1 ms, a macro phase adjustment may be
            necessary. A macro phase adjustment is when the board time is adjusted
            by a significant amount and, therefore, the board time no longer
            atomically increments. This should not occur on a well designed and
            stable time reference. If this occurs, future time events, clocks, and
            time stamps may be affected. If the board time is set forward, future
            time events and clock transitions that were missed occur immediately. If
            the board time is set backward, future time events and clock transitions
            are delayed. Note: An alternative to calling this method is to
            configure the default configured Time Reference through Measurement &
            Automation Explorer. The state configured is then reapplied at every
            restart. Note: Closing the session that calls this VI does not alter the
            value of the configured Time Reference. Note: The NI-Sync family of
            devices uses the TAI timescale. This method sets the Time Reference of
            the device to GPS.

            



set_time_reference_irig
-----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: set_time_reference_irig(irig_type, terminal_name)

            This method sets the time reference of the device associated with the
            specified instrument handle. The time reference set is used to update
            the value and frequency of the board time such that the board time
            reflects the time reference's time as closely as possible. The board
            time is then used for tasks such as creating future time events, clocks,
            and timestamping triggers. This method is a nonblocking call that
            returns immediately regardless of the state of the time reference set.
            Setting the time reference is a systemwide (per device) configuration
            that persists after the session exits. The time reference is not
            reservable; the last call to set the time reference takes precedence. If
            the time reference set is not providing valid time information, the
            board time free runs from the last known time at the last frequency that
            was applied. Note: When a device's board time and the configured time
            reference's time vary by more than 1 ms, a macro phase adjustment may be
            necessary. A macro phase adjustment is when the board time is adjusted
            by a significant amount and, therefore, the board time no longer
            atomically increments. This should not occur on a well designed and
            stable time reference. If this occurs, future time events, clocks, and
            time stamps may be affected. If the board time is set forward, future
            time events and clock transitions that were missed occur immediately. If
            the board time is set backward, future time events and clock transitions
            are delayed. Note: An alternative to calling this method is to
            configure the default configured Time Reference through Measurement &
            Automation Explorer. The state configured is then reapplied every
            restart. Note: Closing the session that calls this VI does not alter the
            value of the configured Time Reference. Note: The NI-Sync family of
            devices uses the TAI timescale. This method sets the Time Reference of
            the device to IRIG.

            



            :param irig_type:


                An input integer enumeration of the IRIG input being supplied. Valid
                Values: :py:data:`~nisync.NISYNC_VAL_IRIG_TYPE_IRIGB_DC`
                :py:data:`~nisync.NISYNC_VAL_IRIG_TYPE_IRIGB_AM` (Default)

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type irig_type: int
            :param terminal_name:


                An input string that specifies the terminal to which the IRIG input is
                connected.

                


            :type terminal_name: str

set_time_reference_pps
----------------------

    .. py:currentmodule:: nisync.Session

    .. py:method:: set_time_reference_pps(terminal_name, use_manual_time, initial_time_seconds, initial_nanoseconds, initial_fractional_nanoseconds)

            This method sets the time reference of the device associated with the
            specified instrument handle. The time reference set is used to update
            the value and frequency of the board time such that the board time
            reflects the time reference's time as closely as possible. The board
            time is then used for tasks such as creating future time events, clocks,
            and timestamping triggers. This method is a nonblocking call that
            returns immediately regardless of the state of the time reference set.
            Setting the time reference is a systemwide (per device) configuration
            that persists after the session exits. The time reference is not
            reservable; the last call to set the time reference takes precedence. If
            the time reference set is not providing valid time information, the
            board time free runs from the last known time at the last frequency that
            was applied. Note: When a device's board time and the configured time
            reference's time vary by more than 1 ms, a macro phase adjustment may be
            necessary. A macro phase adjustment is when the board time is adjusted
            by a significant amount and, therefore, the board time no longer
            atomically increments. This should not occur on a well designed and
            stable time reference. If this occurs, future time events, clocks, and
            time stamps may be affected. If the board time is set forward, future
            time events and clock transitions that were missed occur immediately. If
            the board time is set backward, future time events and clock transitions
            are delayed. Note: An alternative to calling this method is to
            configure the default configured Time Reference through Measurement &
            Automation Explorer. The state configured is then reapplied at every
            restart. Note: Closing the session that calls this VI does not alter the
            value of the configured Time Reference. Note: The NI-Sync family of
            devices uses the TAI timescale. This method sets the Time Reference of
            the device to PPS (pulse per second).

            



            :param terminal_name:


                An input string that specifies the terminal to which the PPS is
                supplied.

                


            :type terminal_name: str
            :param use_manual_time:


                An input Boolean that specifies whether to use the user-supplied time or
                the OS system time to represent the time at which the first pulse is
                received. If false, the OS system time is read at the time the first
                pulse is received, and it is used to set the board time. If true, the
                user-specified initial time is used to set the board time when the first
                pulse is recevied. Every subsequent pulse is interpreted to be received
                one second later, and the board time adjusted accordingly.

                


            :type use_manual_time: bool
            :param initial_time_seconds:


                An input integer that specifies the seconds field of the time to apply
                as the board time when the first pulse is received if useManualTime was
                set to True.

                


            :type initial_time_seconds: int
            :param initial_nanoseconds:


                An input integer that specifies the nanoseconds field of the time to
                apply as the board time when the first pulse is received if
                useManualTime was set to True.

                


            :type initial_nanoseconds: int
            :param initial_fractional_nanoseconds:


                An input integer that specifies the fractional nanoseconds field of the
                time to apply as the board time when the first pulse is received if
                useManualTime was set to True.

                


            :type initial_fractional_nanoseconds: int

start1588
---------

    .. py:currentmodule:: nisync.Session

    .. py:method:: start1588()

            This method starts participation in 1588. Note that this method
            returns as soon as participation begins and does not wait until the 1588
            clock has reached a steady state. For clocks, future time events, and
            triggered time stamps to be synchronized with respect to other devices
            participating in 1588, this method should be invoked, 1588 should be
            set as the Time Reference, and the 1588 clock should reach a steady
            state before any of these operations are invoked. Note that you do not
            need to invoke this method in the same session as these other
            operations, but rather you can invoke it in a separate session
            associated with the same device. Note: An alternative to calling this
            method is to configure the 1588 default state through Measurement &
            Automation Explorer. The state configured is then reapplied at every
            restart. Note: Closing the session that calls this method does not
            stop 1588. Stop 1588 must be called explicitly from any session to stop
            1588 participation. Note: If the clock participating in 1588 enters the
            faulty state, and 1588 is configured as the Time Reference, future time
            events, clocks, and time stamps are no longer synchronized with other
            1588 devices participating in PTP. This should not occur on a well
            designed and stable network. You can check for this condition by
            monitoring the 1588 clock state property.

            



stop1588
--------

    .. py:currentmodule:: nisync.Session

    .. py:method:: stop1588()

            This method stops participation in 1588.

            





Properties
==========

clk10_phase_adjust
------------------

    .. py:attribute:: clk10_phase_adjust

        Specifies the PXI_Clk10 Phase Adjust Voltage.  When using the PLL to lock PXI_CLK10 to an external reference clock, the phase between the clocks can be adjusted.  The time between rising edges of PXI_CLK10 and the input clock is minimized using this constant.

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

                - C Attribute: **NISYNC_ATTR_CLK10_PHASE_ADJUST**

clkin_attenuation_disable
-------------------------

    .. py:attribute:: clkin_attenuation_disable

        Setting this property to True disables the ClkIn attenuation.

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

                - C Attribute: **NISYNC_ATTR_CLKIN_ATTENUATION_DISABLE**

clkin_pll_freq
--------------

    .. py:attribute:: clkin_pll_freq

        Specifies the frequency that the PLL should lock to.  The PLL can be used to lock to frequencies between 1 MHz and 100 MHz, in multiples of 1 MHz.

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

                - C Attribute: **NISYNC_ATTR_CLKIN_PLL_FREQ**

clkin_pll_locked
----------------

    .. py:attribute:: clkin_pll_locked

        Returns whether or not the PXI_Clk10 PLL is currently locked to a signal at the ClkIn terminal.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_CLKIN_PLL_LOCKED**

clkin_use_pll
-------------

    .. py:attribute:: clkin_use_pll

        Specifies whether or not the connection between ClkIn and PXI_Clk10 should use the PLL circuit.  If this Boolean value is set to True, the PLL will be used to lock to the frequency at ClkIn when connecting to PXI_Clk10.  You must set this property before connecting the clock to PXI_Clk10_In.

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

                - C Attribute: **NISYNC_ATTR_CLKIN_USE_PLL**

clkout_gain_enable
------------------

    .. py:attribute:: clkout_gain_enable

        Setting this property to True increases the ClkOut amplitude.

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

                - C Attribute: **NISYNC_ATTR_CLKOUT_GAIN_ENABLE**

dds_freq
--------

    .. py:attribute:: dds_freq

        Specifies the frequency (in Hertz) that the DDS should generate.

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

                - C Attribute: **NISYNC_ATTR_DDS_FREQ**

dds_initial_delay
-----------------

    .. py:attribute:: dds_initial_delay

        Specifies the initial delay (in seconds) that the DDS should wait before it begins generating a specified frequency.  This property must be set prior to setting the DDS frequency, and it must be set using the same NI-Sync instrument driver session that sets the DDS frequency.

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

                - C Attribute: **NISYNC_ATTR_DDS_INITIAL_DELAY**

dds_phase_adjust
----------------

    .. py:attribute:: dds_phase_adjust

        Specifies the DDS Phase Adjust Voltage.

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

                - C Attribute: **NISYNC_ATTR_DDS_PHASE_ADJUST**

dds_update_source
-----------------

    .. py:attribute:: dds_update_source

        Specifies the signal source to be used when updating the DDS frequency.  The default is to update the frequency immediately, i.e. as soon as the frequency is set.  Alternatively, the DDS frequency can be committed to the DDS with an update pulse that arrives on a PXI_Trig terminal.

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

                - C Attribute: **NISYNC_ATTR_DDS_UPDATE_SOURCE**

dds_vcxo_voltage
----------------

    .. py:attribute:: dds_vcxo_voltage

        Specifies the DDS VCXO Voltage.

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

                - C Attribute: **NISYNC_ATTR_DDS_VCXO_VOLTAGE**

front_sync_clk_src
------------------

    .. py:attribute:: front_sync_clk_src

        Specifies the synchronization clock source for the front zone (PFI and PFI_LVDS) terminals.

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

                - C Attribute: **NISYNC_ATTR_FRONT_SYNC_CLK_SRC**

gps_antenna_connected
---------------------

    .. py:attribute:: gps_antenna_connected

        A Boolean that specifies whether the GPS antenna is properly connected.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_GPS_ANTENNA_CONNECTED**

gps_mobile_mode
---------------

    .. py:attribute:: gps_mobile_mode

        A Boolean that specifies whether GPS is using mobile mode.  Enabling mobile mode allows the user to move the GPS  antenna and continuously calculate the current position and velocity.  If mobile mode is disabled, the antenna  must remain in a fixed position while the computer is on.  Timing accuracy is significantly improved with mobile  mode disabled.

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

                - C Attribute: **NISYNC_ATTR_GPS_MOBILE_MODE**

gps_recalculate_position
------------------------

    .. py:attribute:: gps_recalculate_position

        A Boolean that specifies whether GPS attempts to recalculate the current position at every system reboot. If not  configured to recalculate position, GPS permanently stores the current location. GPS never performs a self survey  until this flag is set.

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

                - C Attribute: **NISYNC_ATTR_GPS_RECALCULATE_POSITION**

gps_satellites_available
------------------------

    .. py:attribute:: gps_satellites_available

        An integer that specifies the number of GPS satellites currently being tracked. A minimum of four satellites must be  visible for the onboard GPS receiver to perform a self survey. If using GPS as a Time Reference, four or more  satellites must be visible throughout timing measurements for the most accurate results.

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_GPS_SATELLITES_AVAILABLE**

gps_self_survey
---------------

    .. py:attribute:: gps_self_survey

        An integer that specifies the percentage of the GPS self survey that has been completed. The onboard GPS receiver  performs position fixes during the self survey. The individual position fixes are accumulated and averaged over  the course of the self survey. The GPS Time Reference and location information are most accurate after the self  survey has completed and least accurate at the beginning of a self survey. If using GPS as a Time Reference, wait  until the self survey is complete prior to beginning timing measurements for the most accurate results. The onboard  GPS receiver requires at least four visible satellites to perform a self survey.

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_GPS_SELF_SURVEY**

gps_status
----------

    .. py:attribute:: gps_status

        An integer enumeration that specifies the status of GPS.  This property can be queried to determine if GPS is in a  valid state before the application continues with other operations dependent on GPS. This property can also be used  to troubleshoot various GPS errors.

        The following table lists the characteristics of this property.

            +----------------+-----------------+
            | Characteristic | Value           |
            +================+=================+
            | Datatype       | enums.GpsStatus |
            +----------------+-----------------+
            | Permissions    | read only       |
            +----------------+-----------------+
            | Channel Based  | No              |
            +----------------+-----------------+
            | Resettable     | Yes             |
            +----------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_GPS_STATUS**

intf_num
--------

    .. py:attribute:: intf_num

        Returns the interface (board) number of this NI PXI-665x.  If there are multiple instances of the NI PXI-665x, each will have a unique interface number.

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_INTF_NUM**

oscillator_voltage
------------------

    .. py:attribute:: oscillator_voltage

        Specifies the tuning voltage for the OCXO/TCXO.  The OCXO/TCXO frequency can be varied over a small range.  The output frequency is adjusted using this tuning voltage.

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

                - C Attribute: **NISYNC_ATTR_OSCILLATOR_VOLTAGE**

pfi0_10kohm_enable
------------------

    .. py:attribute:: pfi0_10kohm_enable

        Specifies whether or not the PFI0 terminal should be terminated with 10kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI0_10KOHM_ENABLE**

pfi0_1kohm_enable
-----------------

    .. py:attribute:: pfi0_1kohm_enable

        Specifies whether or not the PFI0 terminal should be terminated with 1kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI0_1KOHM_ENABLE**

pfi0_threshold
--------------

    .. py:attribute:: pfi0_threshold

        Specifies the voltage threshold for PFI0 terminal.

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

                - C Attribute: **NISYNC_ATTR_PFI0_THRESHOLD**

pfi1_10kohm_enable
------------------

    .. py:attribute:: pfi1_10kohm_enable

        Specifies whether or not the PFI1 terminal should be terminated with 10kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI1_10KOHM_ENABLE**

pfi1_1kohm_enable
-----------------

    .. py:attribute:: pfi1_1kohm_enable

        Specifies whether or not the PFI1 terminal should be terminated with 1kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI1_1KOHM_ENABLE**

pfi1_threshold
--------------

    .. py:attribute:: pfi1_threshold

        Specifies the voltage threshold for PFI1 terminal.

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

                - C Attribute: **NISYNC_ATTR_PFI1_THRESHOLD**

pfi2_10kohm_enable
------------------

    .. py:attribute:: pfi2_10kohm_enable

        Specifies whether or not the PFI2 terminal should be terminated with 10kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI2_10KOHM_ENABLE**

pfi2_1kohm_enable
-----------------

    .. py:attribute:: pfi2_1kohm_enable

        Specifies whether or not the PFI2 terminal should be terminated with 1kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI2_1KOHM_ENABLE**

pfi2_threshold
--------------

    .. py:attribute:: pfi2_threshold

        Specifies the voltage threshold for PFI2 terminal.

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

                - C Attribute: **NISYNC_ATTR_PFI2_THRESHOLD**

pfi3_10kohm_enable
------------------

    .. py:attribute:: pfi3_10kohm_enable

        Specifies whether or not the PFI3 terminal should be terminated with 10kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI3_10KOHM_ENABLE**

pfi3_1kohm_enable
-----------------

    .. py:attribute:: pfi3_1kohm_enable

        Specifies whether or not the PFI3 terminal should be terminated with 1kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI3_1KOHM_ENABLE**

pfi3_threshold
--------------

    .. py:attribute:: pfi3_threshold

        Specifies the voltage threshold for PFI3 terminal.

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

                - C Attribute: **NISYNC_ATTR_PFI3_THRESHOLD**

pfi4_10kohm_enable
------------------

    .. py:attribute:: pfi4_10kohm_enable

        Specifies whether or not the PFI4 terminal should be terminated with 10kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI4_10KOHM_ENABLE**

pfi4_1kohm_enable
-----------------

    .. py:attribute:: pfi4_1kohm_enable

        Specifies whether or not the PFI4 terminal should be terminated with 1kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI4_1KOHM_ENABLE**

pfi4_threshold
--------------

    .. py:attribute:: pfi4_threshold

        Specifies the voltage threshold for PFI4 terminal.

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

                - C Attribute: **NISYNC_ATTR_PFI4_THRESHOLD**

pfi5_10kohm_enable
------------------

    .. py:attribute:: pfi5_10kohm_enable

        Specifies whether or not the PFI5 terminal should be terminated with 10kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI5_10KOHM_ENABLE**

pfi5_1kohm_enable
-----------------

    .. py:attribute:: pfi5_1kohm_enable

        Specifies whether or not the PFI5 terminal should be terminated with 1kOhm impedance.

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

                - C Attribute: **NISYNC_ATTR_PFI5_1KOHM_ENABLE**

pfi5_threshold
--------------

    .. py:attribute:: pfi5_threshold

        Specifies the voltage threshold for PFI5 terminal.

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

                - C Attribute: **NISYNC_ATTR_PFI5_THRESHOLD**

pxiclk10_present
----------------

    .. py:attribute:: pxiclk10_present

        Returns whether or not the PXI_Clk10 signal is present on the PXI backplane.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_PXICLK10_PRESENT**

rear_sync_clk_src
-----------------

    .. py:attribute:: rear_sync_clk_src

        Specifies the synchronization clock source for the rear zone (PXI_Trig, PXI_Star, and PXIe_DStarB) terminals.

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

                - C Attribute: **NISYNC_ATTR_REAR_SYNC_CLK_SRC**

serial_num
----------

    .. py:attribute:: serial_num

        Returns the serial number of this NI PXI-665x interface.

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_SERIAL_NUM**

sync_clk_div1
-------------

    .. py:attribute:: sync_clk_div1

        Specifies the value for the first clock divisor

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

                - C Attribute: **NISYNC_ATTR_SYNC_CLK_DIV1**

sync_clk_div2
-------------

    .. py:attribute:: sync_clk_div2

        Specifies the value for the second clock divisor

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

                - C Attribute: **NISYNC_ATTR_SYNC_CLK_DIV2**

sync_clk_pfi0_freq
------------------

    .. py:attribute:: sync_clk_pfi0_freq

        Specifies the frequency reference (in MHz) for PFI0

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

                - C Attribute: **NISYNC_ATTR_SYNC_CLK_PFI0_FREQ**

sync_clk_rst_clk10_cntr_on_pxitrig
----------------------------------

    .. py:attribute:: sync_clk_rst_clk10_cntr_on_pxitrig

        Specifies whether or not the PXI_Clk10 clock divider counters should reset on a PXI_Trig line pulse.  The PXI_Trig line used to reset the divided clock counters is specified with the 'Reset Synchronization Clock PXI_Trig Line' property.

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

                - C Attribute: **NISYNC_ATTR_SYNC_CLK_RST_CLK10_CNTR_ON_PXITRIG**

sync_clk_rst_dds_cntr_on_pxitrig
--------------------------------

    .. py:attribute:: sync_clk_rst_dds_cntr_on_pxitrig

        Specifies whether or not the DDS clock dividers should reset on a PXI_Trig line pulse.  The PXI_Trig line used to reset the divided clock counters is specified with the 'Reset Synchronization Clock PXI_Trig Line' property.

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

                - C Attribute: **NISYNC_ATTR_SYNC_CLK_RST_DDS_CNTR_ON_PXITRIG**

sync_clk_rst_pfi0_cntr_on_pxitrig
---------------------------------

    .. py:attribute:: sync_clk_rst_pfi0_cntr_on_pxitrig

        Specifies whether or not the PFI0 clock divider counters should reset on a PXI_Trig line pulse.  The PXI_Trig line used to reset the divided clock counters is specified with the 'Reset Synchronization Clock PXI_Trig Line' property.

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

                - C Attribute: **NISYNC_ATTR_SYNC_CLK_RST_PFI0_CNTR_ON_PXITRIG**

sync_clk_rst_pxitrig_num
------------------------

    .. py:attribute:: sync_clk_rst_pxitrig_num

        Specifies the PXI_Trig terminal to use to reset the synchronization clock dividers.

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

                - C Attribute: **NISYNC_ATTR_SYNC_CLK_RST_PXITRIG_NUM**

terminal_state_pfi
------------------

    .. py:attribute:: terminal_state_pfi

        Returns a bitmap containing the current PFI terminal states.  Each bit represents the state of a PFI terminal.  Bit 0 corresponds to PFI0, but 1 corresponds to PFI1, etc.  Bits 6 and above are not defined.

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TERMINAL_STATE_PFI**

terminal_state_pfilvds
----------------------

    .. py:attribute:: terminal_state_pfilvds

        A bitmap containing the current PFI_LVDS terminal states. Each bit represents the state of a PFI_LVDS terminal. Bit 0 corresponds to PFI_LVDS0, bit 1 corresponds to PFI_LVDS1, and bit 2 corresponds to PFI_LVDS2.

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TERMINAL_STATE_PFILVDS**

terminal_state_pxiedstarbperipheral
-----------------------------------

    .. py:attribute:: terminal_state_pxiedstarbperipheral

        Returns the logical state of the PXIe_DStarB peripheral terminal.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TERMINAL_STATE_PXIEDSTARBPERIPHERAL**

terminal_state_pxiedstarc
-------------------------

    .. py:attribute:: terminal_state_pxiedstarc

        A bitmap containing the current PXIe_DStarC terminal states. Each bit represents the state of a PXIe_DStarC terminal. Bit 0 corresponds to PXIe_DStarC0, bit 1 corresponds to PXIe_DStarC1, etc.

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TERMINAL_STATE_PXIEDSTARC**

terminal_state_pxistar
----------------------

    .. py:attribute:: terminal_state_pxistar

        Returns a bitmap containing the PXI_Star terminal states.  Each bit represents the state of a PXI_STAR terminal.  Bit 0 corresponds to PXI_STAR0, bit 1 corresponds to PXI_STAR1, etc.  Bits 13 and above are not defined.

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TERMINAL_STATE_PXISTAR**

terminal_state_pxistarperipheral
--------------------------------

    .. py:attribute:: terminal_state_pxistarperipheral

        Returns the logical state of the PXI_Star peripheral terminal.  This value is only valid when the board is in a peripheral slot.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TERMINAL_STATE_PXISTARPERIPHERAL**

terminal_state_pxitrig
----------------------

    .. py:attribute:: terminal_state_pxitrig

        Returns a bitmap containing the PXI_Trig terminal states.  Each bit represents the state of a PXI_TRIG terminal.  Bit 0 corresponds to PXI_TRIG0, bit 1 corresponds to PXI_TRIG1, etc.  Bits 8 and above are not defined.

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TERMINAL_STATE_PXITRIG**

timeref_correction
------------------

    .. py:attribute:: timeref_correction

        A double that specifies a manual correction, in seconds, to apply to the time reference. Use this property to  calibrate the time reference manually to achieve better synchronization with the configured time reference.

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

                - C Attribute: **NISYNC_ATTR_TIMEREF_CORRECTION**

timeref_enabled
---------------

    .. py:attribute:: timeref_enabled

        A boolean that specifies whether the time reference associated with this session is enabled.

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

                - C Attribute: **NISYNC_ATTR_TIMEREF_ENABLED**

timeref_is_selected
-------------------

    .. py:attribute:: timeref_is_selected

        A boolean that represents whether the time reference associated with this session is the selected time reference.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TIMEREF_IS_SELECTED**

timeref_last_sync_id
--------------------

    .. py:attribute:: timeref_last_sync_id

        An integer that is incremented when a synchronization message is received from the current time reference.   and the 1588 clock is a master.



        .. note:: that synchronization messages are not received if the time reference is set to free running or if set to 1588

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TIMEREF_LAST_SYNC_ID**

timeref_offset
--------------

    .. py:attribute:: timeref_offset

        A double that specifies the calculated offset, in seconds, from the configured time reference. This property can be  used to determine when the local clock is sufficiently synchronized with the selected time reference to continue  operations.

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TIMEREF_OFFSET**

timeref_offset_ns
-----------------

    .. py:attribute:: timeref_offset_ns

        A double that specifies the calculated offset, in nanoseconds, from the configured time reference. This property can be  used to determine when the local clock is sufficiently synchronized with the selected time reference to continue  operations.

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
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TIMEREF_OFFSET_NS**

timeref_present
---------------

    .. py:attribute:: timeref_present

        A Boolean that specifies whether the configured time reference is currently providing a valid time signal.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | Yes       |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISYNC_ATTR_TIMEREF_PRESENT**

timeref_selected_name
---------------------

    .. py:attribute:: timeref_selected_name

        A string that represents the name of the selected time reference.

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

                - C Attribute: **NISYNC_ATTR_TIMEREF_SELECTED_NAME**

timeref_selected_type
---------------------

    .. py:attribute:: timeref_selected_type

        A string that represents the synchronization protocol being used by the selected time reference.

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

                - C Attribute: **NISYNC_ATTR_TIMEREF_SELECTED_TYPE**

timeref_type
------------

    .. py:attribute:: timeref_type

        A string that represents the synchronization protocol being used by the time reference associated with this session.

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

                - C Attribute: **NISYNC_ATTR_TIMEREF_TYPE**

timeref_utc_offset
------------------

    .. py:attribute:: timeref_utc_offset

        An integer that specifies the offset, in seconds, of the UTC timescale from the current time reference.

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

                - C Attribute: **NISYNC_ATTR_TIMEREF_UTC_OFFSET**

timeref_utc_offset_valid
------------------------

    .. py:attribute:: timeref_utc_offset_valid

        A boolean that specifies whether the UTC offset of the current time reference is valid.

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

                - C Attribute: **NISYNC_ATTR_TIMEREF_UTC_OFFSET_VALID**

user_led_state
--------------

    .. py:attribute:: user_led_state

        Specifies the state of the User LED.  Setting this Boolean value to True will turn on the User LED, and setting it to False will turn off the User LED.

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

                - C Attribute: **NISYNC_ATTR_USER_LED_STATE**


.. contents:: Session


