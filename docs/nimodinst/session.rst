NI-ModInst Session
==================

.. py:module:: nimodinst

.. py:class:: Session

   A NI-ModInst session to get device information


   :ivar ViInt32 bus_number: 
      The bus on which the device has been enumerated.
   :ivar ViInt32 chassis_number: 
      The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
   :ivar ViString device_model: 
      The model of the device (for example, NI PXI-5122)
   :ivar ViString device_name: 
      The name of the device, which can be used to open an instrument driver session for that device
   :ivar ViInt32 max_pciexpress_link_width: 
      **MAX_PCIEXPRESS_LINK_WIDTH**
   :ivar ViInt32 pciexpress_link_width: 
      **PCIEXPRESS_LINK_WIDTH**
   :ivar ViString serial_number: 
      The serial number of the device
   :ivar ViInt32 slot_number: 
      The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
   :ivar ViInt32 socket_number: 
      The socket number on which the device has been enumerated


