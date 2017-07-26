NI-ModInst Session
==================

.. py:module:: nimodinst

.. py:class:: Session

   A NI-ModInst session to get device information


   :ivar ViString device_name: 
      The name of the device, which can be used to open an instrument driver session for that device
   :ivar ViString device_model: 
      The model of the device (for example, NI PXI-5122)
   :ivar ViString serial_number: 
      The serial number of the device
   :ivar ViInt32 slot_number: 
      The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
   :ivar ViInt32 chassis_number: 
      The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
   :ivar ViInt32 bus_number: 
      The bus on which the device has been enumerated.
   :ivar ViInt32 socket_number: 
      The socket number on which the device has been enumerated
   :ivar ViInt32 pciexpress_link_width: 
      **PCIEXPRESS_LINK_WIDTH**
   :ivar ViInt32 max_pciexpress_link_width: 
      **MAX_PCIEXPRESS_LINK_WIDTH**

   .. py:attribute:: device_name

      The name of the device, which can be used to open an instrument driver session for that device

      The following table lists the characteristics of this property.

      +------------------+-------------+
      | Characteristic   | Value       |
      +------------------+-------------+
      | Datatype         | string      |
      +------------------+-------------+
      | Permissions      | Read Only   |
      +------------------+-------------+
      | Channel Based    | False       |
      +------------------+-------------+
      | Resettable       | No          |
      +------------------+-------------+

      .. tip:: 
         This attribute corresponds to:

           - C Attribute: **NIMODINST_ATTR_DEVICE_NAME**

   .. py:attribute:: device_model

      The model of the device (for example, NI PXI-5122)

      The following table lists the characteristics of this property.

      +------------------+-------------+
      | Characteristic   | Value       |
      +------------------+-------------+
      | Datatype         | string      |
      +------------------+-------------+
      | Permissions      | Read Only   |
      +------------------+-------------+
      | Channel Based    | False       |
      +------------------+-------------+
      | Resettable       | No          |
      +------------------+-------------+

      .. tip:: 
         This attribute corresponds to:

           - C Attribute: **NIMODINST_ATTR_DEVICE_MODEL**

   .. py:attribute:: serial_number

      The serial number of the device

      The following table lists the characteristics of this property.

      +------------------+-------------+
      | Characteristic   | Value       |
      +------------------+-------------+
      | Datatype         | string      |
      +------------------+-------------+
      | Permissions      | Read Only   |
      +------------------+-------------+
      | Channel Based    | False       |
      +------------------+-------------+
      | Resettable       | No          |
      +------------------+-------------+

      .. tip:: 
         This attribute corresponds to:

           - C Attribute: **NIMODINST_ATTR_SERIAL_NUMBER**

   .. py:attribute:: slot_number

      The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

      The following table lists the characteristics of this property.

      +------------------+-------------------------+
      | Characteristic   | Value                   |
      +------------------+-------------------------+
      | Datatype         | 32-bit signed integer   |
      +------------------+-------------------------+
      | Permissions      | Read/Write              |
      +------------------+-------------------------+
      | Channel Based    | False                   |
      +------------------+-------------------------+
      | Resettable       | No                      |
      +------------------+-------------------------+

      .. tip:: 
         This attribute corresponds to:

           - C Attribute: **NIMODINST_ATTR_SLOT_NUMBER**

   .. py:attribute:: chassis_number

      The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

      The following table lists the characteristics of this property.

      +------------------+-------------------------+
      | Characteristic   | Value                   |
      +------------------+-------------------------+
      | Datatype         | 32-bit signed integer   |
      +------------------+-------------------------+
      | Permissions      | Read/Write              |
      +------------------+-------------------------+
      | Channel Based    | False                   |
      +------------------+-------------------------+
      | Resettable       | No                      |
      +------------------+-------------------------+

      .. tip:: 
         This attribute corresponds to:

           - C Attribute: **NIMODINST_ATTR_CHASSIS_NUMBER**

   .. py:attribute:: bus_number

      The bus on which the device has been enumerated.

      The following table lists the characteristics of this property.

      +------------------+-------------------------+
      | Characteristic   | Value                   |
      +------------------+-------------------------+
      | Datatype         | 32-bit signed integer   |
      +------------------+-------------------------+
      | Permissions      | Read/Write              |
      +------------------+-------------------------+
      | Channel Based    | False                   |
      +------------------+-------------------------+
      | Resettable       | No                      |
      +------------------+-------------------------+

      .. tip:: 
         This attribute corresponds to:

           - C Attribute: **NIMODINST_ATTR_BUS_NUMBER**

   .. py:attribute:: socket_number

      The socket number on which the device has been enumerated

      The following table lists the characteristics of this property.

      +------------------+-------------------------+
      | Characteristic   | Value                   |
      +------------------+-------------------------+
      | Datatype         | 32-bit signed integer   |
      +------------------+-------------------------+
      | Permissions      | Read/Write              |
      +------------------+-------------------------+
      | Channel Based    | False                   |
      +------------------+-------------------------+
      | Resettable       | No                      |
      +------------------+-------------------------+

      .. tip:: 
         This attribute corresponds to:

           - C Attribute: **NIMODINST_ATTR_SOCKET_NUMBER**

   .. py:attribute:: pciexpress_link_width

      The following table lists the characteristics of this property.

      +------------------+-------------------------+
      | Characteristic   | Value                   |
      +------------------+-------------------------+
      | Datatype         | 32-bit signed integer   |
      +------------------+-------------------------+
      | Permissions      | Read/Write              |
      +------------------+-------------------------+
      | Channel Based    | False                   |
      +------------------+-------------------------+
      | Resettable       | No                      |
      +------------------+-------------------------+

      .. tip:: 
         This attribute corresponds to:

           - C Attribute: **NIMODINST_ATTR_PCIEXPRESS_LINK_WIDTH**

   .. py:attribute:: max_pciexpress_link_width

      The following table lists the characteristics of this property.

      +------------------+-------------------------+
      | Characteristic   | Value                   |
      +------------------+-------------------------+
      | Datatype         | 32-bit signed integer   |
      +------------------+-------------------------+
      | Permissions      | Read/Write              |
      +------------------+-------------------------+
      | Channel Based    | False                   |
      +------------------+-------------------------+
      | Resettable       | No                      |
      +------------------+-------------------------+

      .. tip:: 
         This attribute corresponds to:

           - C Attribute: **NIMODINST_ATTR_MAX_PCIEXPRESS_LINK_WIDTH**

