NI-ModInst Session
==================

.. py:module:: nimodinst

.. py:class:: Session

   A NI-ModInst session to get device information


   :var bus_number: 
      The bus on which the device has been enumerated.
   :vartype bus_number: ViInt32
   :var chassis_number: 
      The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
   :vartype chassis_number: ViInt32
   :var device_model: 
      The model of the device (for example, NI PXI-5122)
   :vartype device_model: ViString
   :var device_name: 
      The name of the device, which can be used to open an instrument driver session for that device
   :vartype device_name: ViString
   :var max_pciexpress_link_width: 
      **MAX_PCIEXPRESS_LINK_WIDTH**
   :vartype max_pciexpress_link_width: ViInt32
   :var pciexpress_link_width: 
      **PCIEXPRESS_LINK_WIDTH**
   :vartype pciexpress_link_width: ViInt32
   :var serial_number: 
      The serial number of the device
   :vartype serial_number: ViString
   :var slot_number: 
      The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
   :vartype slot_number: ViInt32
   :var socket_number: 
      The socket number on which the device has been enumerated
   :vartype socket_number: ViInt32


