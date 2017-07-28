NI-ModInst Attributes
=====================

.. py:currentmodule:: nimodinst

.. py:attribute:: bus_number

   The bus on which the device has been enumerated.

   The following table lists the characteristics of this property.

   +----------------+---------+
   | Characteristic | Value   |
   +================+=========+
   | Datatype       | integer |
   +----------------+---------+
   | Permissions    | read    |
   +----------------+---------+
   | Channel Based  | False   |
   +----------------+---------+
   | Resettable     | No      |
   +----------------+---------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - C Attribute: **NIMODINST_ATTR_BUS_NUMBER**

.. py:attribute:: chassis_number

   The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

   The following table lists the characteristics of this property.

   +----------------+---------+
   | Characteristic | Value   |
   +================+=========+
   | Datatype       | integer |
   +----------------+---------+
   | Permissions    | read    |
   +----------------+---------+
   | Channel Based  | False   |
   +----------------+---------+
   | Resettable     | No      |
   +----------------+---------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - C Attribute: **NIMODINST_ATTR_CHASSIS_NUMBER**

.. py:attribute:: device_model

   The model of the device (for example, NI PXI-5122)

   The following table lists the characteristics of this property.

   +----------------+--------+
   | Characteristic | Value  |
   +================+========+
   | Datatype       | string |
   +----------------+--------+
   | Permissions    | read   |
   +----------------+--------+
   | Channel Based  | False  |
   +----------------+--------+
   | Resettable     | No     |
   +----------------+--------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - C Attribute: **NIMODINST_ATTR_DEVICE_MODEL**

.. py:attribute:: device_name

   The name of the device, which can be used to open an instrument driver session for that device

   The following table lists the characteristics of this property.

   +----------------+--------+
   | Characteristic | Value  |
   +================+========+
   | Datatype       | string |
   +----------------+--------+
   | Permissions    | read   |
   +----------------+--------+
   | Channel Based  | False  |
   +----------------+--------+
   | Resettable     | No     |
   +----------------+--------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - C Attribute: **NIMODINST_ATTR_DEVICE_NAME**

.. py:attribute:: max_pciexpress_link_width

   **MAX_PCIEXPRESS_LINK_WIDTH**

   The following table lists the characteristics of this property.

   +----------------+---------+
   | Characteristic | Value   |
   +================+=========+
   | Datatype       | integer |
   +----------------+---------+
   | Permissions    | read    |
   +----------------+---------+
   | Channel Based  | False   |
   +----------------+---------+
   | Resettable     | No      |
   +----------------+---------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - C Attribute: **NIMODINST_ATTR_MAX_PCIEXPRESS_LINK_WIDTH**

.. py:attribute:: pciexpress_link_width

   **PCIEXPRESS_LINK_WIDTH**

   The following table lists the characteristics of this property.

   +----------------+---------+
   | Characteristic | Value   |
   +================+=========+
   | Datatype       | integer |
   +----------------+---------+
   | Permissions    | read    |
   +----------------+---------+
   | Channel Based  | False   |
   +----------------+---------+
   | Resettable     | No      |
   +----------------+---------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - C Attribute: **NIMODINST_ATTR_PCIEXPRESS_LINK_WIDTH**

.. py:attribute:: serial_number

   The serial number of the device

   The following table lists the characteristics of this property.

   +----------------+--------+
   | Characteristic | Value  |
   +================+========+
   | Datatype       | string |
   +----------------+--------+
   | Permissions    | read   |
   +----------------+--------+
   | Channel Based  | False  |
   +----------------+--------+
   | Resettable     | No     |
   +----------------+--------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - C Attribute: **NIMODINST_ATTR_SERIAL_NUMBER**

.. py:attribute:: slot_number

   The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

   The following table lists the characteristics of this property.

   +----------------+---------+
   | Characteristic | Value   |
   +================+=========+
   | Datatype       | integer |
   +----------------+---------+
   | Permissions    | read    |
   +----------------+---------+
   | Channel Based  | False   |
   +----------------+---------+
   | Resettable     | No      |
   +----------------+---------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - C Attribute: **NIMODINST_ATTR_SLOT_NUMBER**

.. py:attribute:: socket_number

   The socket number on which the device has been enumerated

   The following table lists the characteristics of this property.

   +----------------+---------+
   | Characteristic | Value   |
   +================+=========+
   | Datatype       | integer |
   +----------------+---------+
   | Permissions    | read    |
   +----------------+---------+
   | Channel Based  | False   |
   +----------------+---------+
   | Resettable     | No      |
   +----------------+---------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - C Attribute: **NIMODINST_ATTR_SOCKET_NUMBER**


