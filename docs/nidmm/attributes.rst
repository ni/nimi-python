NI-DMM Attributes
=================

.. py:currentmodule:: nidmm

.. py:attribute:: absolute_resolution

   Specifies the measurement resolution in absolute units. Setting this
   property to higher values increases the measurement accuracy. Setting
   this property to lower values increases the measurement speed.

   .. note::
      NI-DMM ignores this property for capacitance and inductance measurements on the NI 4082 and NI 4072. To achieve better resolution for such measurements, use the Number of LC Measurements to Average property.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Absolute Resolution**
        - C Attribute: **NIDMM_ATTR_ABSOLUTE_RESOLUTION**

.. py:attribute:: adc_calibration

   For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
   calibration mode.

   The following table lists the characteristics of this property.

   +----------------+---------------------------+
   | Characteristic | Value                     |
   +================+===========================+
   | Datatype       | :py:data:`ADCCalibration` |
   +----------------+---------------------------+
   | Permissions    | read-write                |
   +----------------+---------------------------+
   | Channel Based  | False                     |
   +----------------+---------------------------+
   | Resettable     | No                        |
   +----------------+---------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:ADC Calibration**
        - C Attribute: **NIDMM_ATTR_ADC_CALIBRATION**

.. py:attribute:: aperture_time

   Specifies the measurement aperture time for the current configuration.
   Aperture time is specified in units set by the Aperture Time Units
   property. To override the default aperture, set this property to the
   desired aperture time after calling niDMM Config Measurement . To return
   to the default, set this property to Aperture Time Auto (-1).

   Any number of powerline cycles (PLCs) within the minimum and maximum
   ranges is allowed on the NI 4080/4081/4082 and NI 4070/4071/4072.

   On the NI 4065 the minimum aperture time is 333 micro s and the maximum
   aperture time is 78.2 s. If setting the number of averages directly, the
   total measurement time is aperture time X the number of averages, which
   must be less than 72.8 s. The aperture times allowed are 333 micro s,
   667 micro s, or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33
   ms, and so on. If you set an aperture time other than 333 micro s, 667
   micro s, or multiples of 1.11 ms, the value will be coerced up to the
   next supported aperture time.

   On the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed
   are 1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is
   50 Hz, the PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Advanced:Aperture Time**
        - C Attribute: **NIDMM_ATTR_APERTURE_TIME**

.. py:attribute:: aperture_time_units

   Specifies the units of aperture time for the current configuration.

   .. note::
      The NI 4060 does not support an aperture time set in seconds.

   The following table lists the characteristics of this property.

   +----------------+------------------------------+
   | Characteristic | Value                        |
   +================+==============================+
   | Datatype       | :py:data:`ApertureTimeUnits` |
   +----------------+------------------------------+
   | Permissions    | read-write                   |
   +----------------+------------------------------+
   | Channel Based  | False                        |
   +----------------+------------------------------+
   | Resettable     | No                           |
   +----------------+------------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Advanced:Aperture Time Units**
        - C Attribute: **NIDMM_ATTR_APERTURE_TIME_UNITS**

.. py:attribute:: auto_range_value

   Specifies the value of the range. If auto ranging is enabled, shows the
   actual value of the active range. The value of this property is set
   during a read operation.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | float     |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Auto Range Value**
        - C Attribute: **NIDMM_ATTR_AUTO_RANGE_VALUE**

.. py:attribute:: auto_zero

   Specifies the AutoZero mode. This property is not supported for the NI
   4050.

   The following table lists the characteristics of this property.

   +----------------+---------------------+
   | Characteristic | Value               |
   +================+=====================+
   | Datatype       | :py:data:`AutoZero` |
   +----------------+---------------------+
   | Permissions    | read-write          |
   +----------------+---------------------+
   | Channel Based  | False               |
   +----------------+---------------------+
   | Resettable     | No                  |
   +----------------+---------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Auto Zero**
        - C Attribute: **NIDMM_ATTR_AUTO_ZERO**

.. py:attribute:: buffer_size

   Specifies the size in samples of the internal data buffer. Maximum size
   is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
   chooses the buffer size.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Multi Point Acquisition:Advanced:Buffer Size**
        - C Attribute: **NIDMM_ATTR_BUFFER_SIZE**

.. py:attribute:: cable_compensation_type

   For the NI 4081 and NI 4072 only, specifies the type of cable
   compensation that is applied to the current capacitance or inductance
   measurement for the current range.

   .. note::
      Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value.

   The following table lists the characteristics of this property.

   +----------------+----------------------------------+
   | Characteristic | Value                            |
   +================+==================================+
   | Datatype       | :py:data:`CableCompensationType` |
   +----------------+----------------------------------+
   | Permissions    | read-write                       |
   +----------------+----------------------------------+
   | Channel Based  | False                            |
   +----------------+----------------------------------+
   | Resettable     | No                               |
   +----------------+----------------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Cable Compensation Type**
        - C Attribute: **NIDMM_ATTR_CABLE_COMPENSATION_TYPE**

.. py:attribute:: cache

   Specifies whether to cache the value of properties. When caching is
   enabled, the instrument driver keeps track of the current instrument
   settings and avoids sending redundant commands to the instrument. Thus,
   it significantly increases execution speed. The instrument driver can
   choose to always cache or to never cache particular properties
   regardless of the setting of this property. The default value is TRUE
   (1). Use niDMM Initialize With Options to override the default setting.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:User Options:Cache**
        - C Attribute: **NIDMM_ATTR_CACHE**

.. py:attribute:: channel_count

   Indicates the number of channels that the specific instrument driver
   supports. For each property for which the IVI\_VAL\_MULTI\_CHANNEL flag
   property is set, the IVI engine maintains a separate cache value for
   each channel.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | integer   |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Instrument Capabilities:Channel Count**
        - C Attribute: **NIDMM_ATTR_CHANNEL_COUNT**

.. py:attribute:: conductance

   For the NI 4082 and NI 4072 only, specifies the active part
   (conductance) of the open cable compensation. The valid range is any
   real number >0. The default value (-1.0) indicates that compensation has
   not taken place.

   .. note::
      Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Conductance**
        - C Attribute: **NIDMM_ATTR_CONDUCTANCE**

.. py:attribute:: current_source

   Specifies the current source provided during diode measurements.

   The NI 4050 and NI 4060 are not supported.

   The following table lists the characteristics of this property.

   +----------------+--------------------------+
   | Characteristic | Value                    |
   +================+==========================+
   | Datatype       | :py:data:`CurrentSource` |
   +----------------+--------------------------+
   | Permissions    | read-write               |
   +----------------+--------------------------+
   | Channel Based  | False                    |
   +----------------+--------------------------+
   | Resettable     | No                       |
   +----------------+--------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Current Source**
        - C Attribute: **NIDMM_ATTR_CURRENT_SOURCE**

.. py:attribute:: dc_bias

   For the NI 4082 and NI 4072 only, controls the available DC bias for
   capacitance measurements.

   The following table lists the characteristics of this property.

   +----------------+-------------------+
   | Characteristic | Value             |
   +================+===================+
   | Datatype       | :py:data:`DCBias` |
   +----------------+-------------------+
   | Permissions    | read-write        |
   +----------------+-------------------+
   | Channel Based  | False             |
   +----------------+-------------------+
   | Resettable     | No                |
   +----------------+-------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Advanced:DC Bias**
        - C Attribute: **NIDMM_ATTR_DC_BIAS**

.. py:attribute:: dc_noise_rejection

   Specifies the DC noise rejection mode.

   .. note::
      The NI 4050 and NI 4060 are not supported.

   The following table lists the characteristics of this property.

   +----------------+-----------------------------+
   | Characteristic | Value                       |
   +================+=============================+
   | Datatype       | :py:data:`DCNoiseRejection` |
   +----------------+-----------------------------+
   | Permissions    | read-write                  |
   +----------------+-----------------------------+
   | Channel Based  | False                       |
   +----------------+-----------------------------+
   | Resettable     | No                          |
   +----------------+-----------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:DC Noise Rejection**
        - C Attribute: **NIDMM_ATTR_DC_NOISE_REJECTION**

.. py:attribute:: digits_resolution

   Specifies the measurement resolution in digits. Setting this property to
   higher values increases the measurement accuracy. Setting this property
   to lower values increases the measurement speed.

   .. note::
      NI-DMM ignores this property for capacitance and inductance measurements on the NI 4082 and NI 4072. To achieve better resolution for such measurements, use the Number of LC Measurements to Average property.

   The following table lists the characteristics of this property.

   +----------------+-----------------------------+
   | Characteristic | Value                       |
   +================+=============================+
   | Datatype       | :py:data:`DigitsResolution` |
   +----------------+-----------------------------+
   | Permissions    | read-write                  |
   +----------------+-----------------------------+
   | Channel Based  | False                       |
   +----------------+-----------------------------+
   | Resettable     | No                          |
   +----------------+-----------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Digits Resolution**
        - C Attribute: **NIDMM_ATTR_DIGITS_RESOLUTION**

.. py:attribute:: driver_setup

   This property indicates the Driver Setup string that the user specified
   when initializing the driver. Some cases exist where the end-user must
   specify instrument driver options at initialization time. An example of
   this is specifying a particular instrument model from among a family of
   instruments that the driver supports. This is useful when using
   simulation. The end-user can specify driver-specific options through the
   Driver Setup keyword in the Option String parameter in niDMM Initialize
   With Options . If the user does not specify a Driver Setup string, this
   property returns an empty string.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:User Options:Driver Setup**
        - C Attribute: **NIDMM_ATTR_DRIVER_SETUP**

.. py:attribute:: engine_major_version

   The major version number of the IVI engine.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | integer   |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Obsolete:Inherent IVI Attributes:Version Info:Engine Major Version**
        - C Attribute: **NIDMM_ATTR_ENGINE_MAJOR_VERSION**

.. py:attribute:: engine_minor_version

   The minor version number of the IVI engine.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | integer   |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Obsolete:Inherent IVI Attributes:Version Info:Engine Minor Version**
        - C Attribute: **NIDMM_ATTR_ENGINE_MINOR_VERSION**

.. py:attribute:: engine_revision

   A string that contains additional version information about the IVI
   engine.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Obsolete:Inherent IVI Attributes:Version Info:Engine Revision**
        - C Attribute: **NIDMM_ATTR_ENGINE_REVISION**

.. py:attribute:: error_elaboration

   An optional string that contains additional information concerning the
   primary error condition.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | string     |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Obsolete:Inherent IVI Attributes:Error Info:Error Elaboration**
        - C Attribute: **NIDMM_ATTR_ERROR_ELABORATION**

.. py:attribute:: frequency_voltage_auto_range_value

   For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
   the frequency voltage range. If auto ranging is enabled, shows the
   actual value of the active frequency voltage range. If not Auto Ranging,
   the value is the same as that of the Frequency Voltage Range property.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | float     |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Frequency Voltage Auto Range Value**
        - C Attribute: **NIDMM_ATTR_FREQUENCY_VOLTAGE_AUTO_RANGE_VALUE**

.. py:attribute:: frequency_voltage_range

   For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
   amplitude of the input signal for frequency measurements.

   +------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+
   | Auto Range On    | -1.0   | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement.   |
   +------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+
   | Auto Range Off   | -2.0   | Disables Auto Ranging. NI-DMM sets the voltage range to the last calculated voltage range.                                         |
   +------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Frequency Voltage Range**
        - C Attribute: **NIDMM_ATTR_FREQUENCY_VOLTAGE_RANGE**

.. py:attribute:: function

   Specifies the measurement function. If you are setting this property
   directly, you must also set the Operation Mode property, which controls
   whether the DMM takes standard single or multipoint measurements, or
   acquires a waveform. If you are programming properties directly, you
   must set the Operation Mode property before setting other configuration
   properties. If the Operation Mode property is set to Waveform Mode, the
   only valid function types are Waveform Voltage and Waveform Current. Set
   the Operation Mode property to IVIDMM Mode to set all other function
   values.

   The following table lists the characteristics of this property.

   +----------------+---------------------+
   | Characteristic | Value               |
   +================+=====================+
   | Datatype       | :py:data:`Function` |
   +----------------+---------------------+
   | Permissions    | read-write          |
   +----------------+---------------------+
   | Channel Based  | False               |
   +----------------+---------------------+
   | Resettable     | No                  |
   +----------------+---------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Function**
        - C Attribute: **NIDMM_ATTR_FUNCTION**

.. py:attribute:: group_capabilities

   A string containing the capabilities and extension groups supported by
   the specific driver.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Capabilities:Group Capabilities**
        - C Attribute: **NIDMM_ATTR_GROUP_CAPABILITIES**

.. py:attribute:: idquery_response

   A string containing the type of instrument used in the current session.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Obsolete:Misc:IDQuery response**
        - C Attribute: **NIDMM_ATTR_IDQUERY_RESPONSE**

.. py:attribute:: input_resistance

   Specifies the input resistance of the instrument.

   .. note::
      The NI 4050 and NI 4060 are not supported.

   The following table lists the characteristics of this property.

   +----------------+----------------------------+
   | Characteristic | Value                      |
   +================+============================+
   | Datatype       | :py:data:`InputResistance` |
   +----------------+----------------------------+
   | Permissions    | read-write                 |
   +----------------+----------------------------+
   | Channel Based  | False                      |
   +----------------+----------------------------+
   | Resettable     | No                         |
   +----------------+----------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Input Resistance**
        - C Attribute: **NIDMM_ATTR_INPUT_RESISTANCE**

.. py:attribute:: instrument_firmware_revision

   A string containing the instrument firmware revision number.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Firmware Revision**
        - C Attribute: **NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION**

.. py:attribute:: instrument_manufacturer

   A string containing the manufacturer of the instrument.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Manufacturer**
        - C Attribute: **NIDMM_ATTR_INSTRUMENT_MANUFACTURER**

.. py:attribute:: instrument_model

   A string containing the instrument model.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Model**
        - C Attribute: **NIDMM_ATTR_INSTRUMENT_MODEL**

.. py:attribute:: instrument_product_id

   The PCI product ID.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | integer   |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Product ID**
        - C Attribute: **NIDMM_ATTR_INSTRUMENT_PRODUCT_ID**

.. py:attribute:: instrument_serial_number

   A string containing the serial number of the instrument. This property
   corresponds to the serial number label that is attached to most
   products.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Serial Number**
        - C Attribute: **NIDMM_ATTR_INSTRUMENT_SERIAL_NUMBER**

.. py:attribute:: interchange_check

   Specifies whether to perform interchangeability checking and log
   interchangeability warnings when you call niDMM VIs. Interchangeability
   warnings indicate that using your application with a different
   instrument might cause different behavior. Use niDMM Get Next
   Interchange Warning to extract interchange warnings. Use niDMM Clear
   Interchange Warnings to clear the list of interchangeability warnings
   without reading them. Interchangeability checking examines the
   properties in a capability group only if you specify a value for at
   least one property within that group. Interchangeability warnings can
   occur when a property affects the behavior of the instrument and you
   have not set that property, or the property has been invalidated since
   you set it.

   +---------+-----+
   | TRUE    | 1   |
   +---------+-----+
   | FALSE   | 0   |
   +---------+-----+

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:User Options:Interchange Check**
        - C Attribute: **NIDMM_ATTR_INTERCHANGE_CHECK**

.. py:attribute:: io_resource_descriptor

   A string containing the resource descriptor of the instrument.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:I/O Resource Descriptor**
        - C Attribute: **NIDMM_ATTR_IO_RESOURCE_DESCRIPTOR**

.. py:attribute:: latency

   Specifies the number of measurements transferred at a time from the
   instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
   the transfer size.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Multi Point Acquisition:Advanced:Latency**
        - C Attribute: **NIDMM_ATTR_LATENCY**

.. py:attribute:: lc_calculation_model

   For the NI 4082 and NI 4072 only, specifies the type of algorithm that
   the measurement processing uses for capacitance and inductance
   measurements.

   The following table lists the characteristics of this property.

   +----------------+-------------------------------+
   | Characteristic | Value                         |
   +================+===============================+
   | Datatype       | :py:data:`LCCalculationModel` |
   +----------------+-------------------------------+
   | Permissions    | read-write                    |
   +----------------+-------------------------------+
   | Channel Based  | False                         |
   +----------------+-------------------------------+
   | Resettable     | No                            |
   +----------------+-------------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model**
        - C Attribute: **NIDMM_ATTR_LC_CALCULATION_MODEL**

.. py:attribute:: logical_name

   A string containing the logical name of the instrument.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
        - C Attribute: **NIDMM_ATTR_LOGICAL_NAME**

.. py:attribute:: max_frequency

   Specifies the maximum frequency component of the input signal for AC
   measurements. This property is used only for error checking and verifies
   that the value of this parameter is less than the maximum frequency of
   the device. This property affects the DMM only when you set the Function
   property to AC measurements.

   The valid ranges are shown in the following table.

   +----------------------------------------+----------------+
   | NI 4080/4081/4082, NI 4070/4071/4072   | 1 Hz-300 kHz   |
   +----------------------------------------+----------------+
   | NI 4065                                | 10 Hz-100 Hz   |
   +----------------------------------------+----------------+
   | NI 4050/4060                           | 20 Hz-25 kHz   |
   +----------------------------------------+----------------+

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Max Frequency**
        - C Attribute: **NIDMM_ATTR_MAX_FREQUENCY**

.. py:attribute:: measurement_completdest

   Specifies the destination of the measurement complete (MC) signal.

   To determine which values are supported by each device, refer to the
   LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.

   .. note::
      The NI 4050 is not supported.

   The following table lists the characteristics of this property.

   +----------------+------------------------------------+
   | Characteristic | Value                              |
   +================+====================================+
   | Datatype       | :py:data:`MeasurementCompleteDest` |
   +----------------+------------------------------------+
   | Permissions    | read-write                         |
   +----------------+------------------------------------+
   | Channel Based  | False                              |
   +----------------+------------------------------------+
   | Resettable     | No                                 |
   +----------------+------------------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Trigger:Measurement Complete Dest**
        - C Attribute: **NIDMM_ATTR_MEASUREMENT_COMPLETDEST**

.. py:attribute:: measurement_destination_slope

   Specifies the polarity of the generated measurement complete signal.

   The following table lists the characteristics of this property.

   +----------------+----------------------------------------+
   | Characteristic | Value                                  |
   +================+========================================+
   | Datatype       | :py:data:`MeasurementDestinationSlope` |
   +----------------+----------------------------------------+
   | Permissions    | read-write                             |
   +----------------+----------------------------------------+
   | Channel Based  | False                                  |
   +----------------+----------------------------------------+
   | Resettable     | No                                     |
   +----------------+----------------------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Trigger:Measurement Destination Slope**
        - C Attribute: **NIDMM_ATTR_MEASUREMENT_DESTINATION_SLOPE**

.. py:attribute:: min_frequency

   Specifies the minimum frequency component of the input signal for AC
   measurements. This property affects the DMM only when you set the
   Function property to AC measurements. The valid range is 1 Hz-300 kHz
   for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
   4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Min Frequency**
        - C Attribute: **NIDMM_ATTR_MIN_FREQUENCY**

.. py:attribute:: number_of_averages

   Specifies the number of averages to perform in a measurement. For the NI
   4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
   time is not set to Auto and Auto Zero is ON. The Number of Averages
   Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
   otherwise, the default is 1.

   The NI 4050 and NI 4060 are not supported.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Advanced:Number Of Averages**
        - C Attribute: **NIDMM_ATTR_NUMBER_OF_AVERAGES**

.. py:attribute:: number_of_lc_measurements_to_average

   For the NI 4082 and NI 4072 only, specifies the number of LC
   measurements that are averaged to produce one reading.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average**
        - C Attribute: **NIDMM_ATTR_NUMBER_OF_LC_MEASUREMENTS_TO_AVERAGE**

.. py:attribute:: offset_compensated_ohms

   For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
   offset compensated ohms.

   The following table lists the characteristics of this property.

   +----------------+----------------------------------+
   | Characteristic | Value                            |
   +================+==================================+
   | Datatype       | :py:data:`OffsetCompensatedOhms` |
   +----------------+----------------------------------+
   | Permissions    | read-write                       |
   +----------------+----------------------------------+
   | Channel Based  | False                            |
   +----------------+----------------------------------+
   | Resettable     | No                               |
   +----------------+----------------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Offset Compensated Ohms**
        - C Attribute: **NIDMM_ATTR_OFFSET_COMPENSATED_OHMS**

.. py:attribute:: operation_mode

   Specifies how the DMM acquires data.

   .. note::
      The NI 4050 and NI 4060 are not supported.

   When you call niDMM Config Measurement , NI-DMM sets this property to
   IVIDMM Mode. When you call niDMM Configure Waveform Acquisition , NI-DMM
   sets this property to Waveform Mode. If you are programming properties
   directly, you must set this property before setting other configuration
   properties.

   The following table lists the characteristics of this property.

   +----------------+--------------------------+
   | Characteristic | Value                    |
   +================+==========================+
   | Datatype       | :py:data:`OperationMode` |
   +----------------+--------------------------+
   | Permissions    | read-write               |
   +----------------+--------------------------+
   | Channel Based  | False                    |
   +----------------+--------------------------+
   | Resettable     | No                       |
   +----------------+--------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Advanced:Operation Mode**
        - C Attribute: **NIDMM_ATTR_OPERATION_MODE**

.. py:attribute:: powerline_frequency

   Specifies the powerline frequency. The NI 4060 and NI 4050 use this
   value to select an aperture time to reject powerline noise by selecting
   the appropriate internal sample clock and filter. The NI 4065, NI
   4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
   for setting the Aperture Time property in powerline cycles.

   After configuring powerline frequency, set the Aperture Time Units
   property to PLCs. When setting the Aperture Time property, select the
   number of PLCs for the powerline frequency. For example, if powerline
   frequency = 50 Hz (or 20 ms) and aperture time in PLCs = 5, then
   aperture time in seconds = 20 ms \* 5 PLCs = 100 ms. Similarly, if
   powerline frequency = 60 Hz (or 16.667 ms) and aperture time in PLCs =
   6, then aperture time in seconds = 16.667 ms \* 6 PLCs = 100 ms.

   .. note::
      For 400 Hz powerline frequency, use the 50 Hz setting.

   The following table lists the characteristics of this property.

   +----------------+-------------------------------+
   | Characteristic | Value                         |
   +================+===============================+
   | Datatype       | :py:data:`PowerlineFrequency` |
   +----------------+-------------------------------+
   | Permissions    | read-write                    |
   +----------------+-------------------------------+
   | Channel Based  | False                         |
   +----------------+-------------------------------+
   | Resettable     | No                            |
   +----------------+-------------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Powerline Frequency**
        - C Attribute: **NIDMM_ATTR_POWERLINE_FREQUENCY**

.. py:attribute:: primary_error

   A code that describes the first error that occurred since the last call
   to niDMM Get Error for the session. The value follows the VXIplug&play
   conventions. A negative value describes an error condition. A positive
   value describes a warning condition. A zero indicates that no error or
   warning occurred. The error and warning values can be status codes
   defined by IVI, VISA, class drivers, or specific drivers.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Obsolete:Inherent IVI Attributes:Error Info:Primary Error**
        - C Attribute: **NIDMM_ATTR_PRIMARY_ERROR**

.. py:attribute:: query_instrument_status

   Specifies whether the instrument driver queries the instrument status
   after each operation. Querying the instrument status is very useful for
   debugging. After the user program is validated, this property can be set
   to FALSE (0) to disable status checking and maximize performance. The
   instrument driver can choose to ignore status checking for particular
   properties regardless of the setting of this property. The default value
   is TRUE (1). Use niDMM Initialize With Options to override the default
   setting.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:User Options:Query Instrument Status**
        - C Attribute: **NIDMM_ATTR_QUERY_INSTRUMENT_STATUS**

.. py:attribute:: range

   Specifies the measurement range. Use positive values to represent the
   absolute value of the maximum expected measurement. The value is in
   units appropriate for the current value of the Function property. For
   example, if the Function property is set to DC Volts, the units are
   volts.

   .. note::
      The NI 4050, NI 4060, and NI 4065 only support Auto Range when the trigger and sample trigger are set to Immediate.

   +----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | (-1.0)   | Auto Range On     | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                |
   +----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | (-2.0)   | Auto Range Off    | NI-DMM sets the Range to the current Auto Range Value and uses this range for all subsequent measurements until the measurement configuration is changed.                                      |
   +----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | (-3.0)   | Auto Range Once   | NI-DMM performs an Auto Range before acquiring the next measurement. The Auto Range Value is stored and used for all subsequent measurements until the measurement configuration is changed.   |
   +----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Range**
        - C Attribute: **NIDMM_ATTR_RANGE**

.. py:attribute:: range_check

   Specifies whether to validate property values and VI parameters. If
   enabled, the instrument driver validates the parameter values passed to
   driver VIs. Range checking parameters is very useful for debugging.
   After the user program is validated, you can set this property to FALSE
   (0) to disable range checking and maximize performance. The default
   value is TRUE (1). Use niDMM Initialize With Options to override the
   default setting.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:User Options:Range Check**
        - C Attribute: **NIDMM_ATTR_RANGE_CHECK**

.. py:attribute:: reactance

   For the NI 4082 and NI 4072 only, represents the reactive part
   (reactance) of the short cable compensation. The valid range is any real
   number >0. The default value (-1) indicates that compensation has not
   taken place.

   .. note::
      Changing the VI or the range through this property or through niDMM Config Measurement resets this property to the default value.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Reactance**
        - C Attribute: **NIDMM_ATTR_REACTANCE**

.. py:attribute:: record_value_coercions

   Specifies whether the IVI engine keeps a list of the value coercions it
   makes for ViInt32 and ViReal64 properties. The default value is FALSE
   (0). Use niDMM Initialize With Options to override the default setting.
   Use niDMM Get Next Coercion Record to extract and delete the oldest
   coercion record from the list.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:User Options:Record Value Coercions**
        - C Attribute: **NIDMM_ATTR_RECORD_VALUE_COERCIONS**

.. py:attribute:: resistance

   For the NI 4082 and NI 4072 only, represents the active part
   (resistance) of the short cable compensation. The valid range is any
   real number >0. The default value (-1) indicates that compensation has
   not taken place.

   .. note::
      Changing the VI or the range through this property or through niDMM Config Measurement resets this property to the default value.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Resistance**
        - C Attribute: **NIDMM_ATTR_RESISTANCE**

.. py:attribute:: rtd_a

   Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
   **RTD Type property** is set to Custom.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD A**
        - C Attribute: **NIDMM_ATTR_RTD_A**

.. py:attribute:: rtd_b

   Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
   **RTD Type property** is set to Custom.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD B**
        - C Attribute: **NIDMM_ATTR_RTD_B**

.. py:attribute:: rtd_c

   Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
   **RTD Type property** is set to Custom.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD C**
        - C Attribute: **NIDMM_ATTR_RTD_C**

.. py:attribute:: rtd_resistance

   Specifies the RTD resistance at 0 degrees Celsius.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Resistance**
        - C Attribute: **NIDMM_ATTR_RTD_RESISTANCE**

.. py:attribute:: rtd_type

   Specifies the RTD type.

   The following table lists the characteristics of this property.

   +----------------+--------------------+
   | Characteristic | Value              |
   +================+====================+
   | Datatype       | :py:data:`RTDType` |
   +----------------+--------------------+
   | Permissions    | read-write         |
   +----------------+--------------------+
   | Channel Based  | False              |
   +----------------+--------------------+
   | Resettable     | No                 |
   +----------------+--------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Type**
        - C Attribute: **NIDMM_ATTR_RTD_TYPE**

.. py:attribute:: sample_count

   Specifies the number of measurements the DMM takes each time it receives
   a trigger in a multiple point acquisition. Setting Sample Count to 0 on
   the NI 4050 and NI 4060 causes the device to take continuous
   measurements. Otherwise, setting Sample Count to 0 causes the
   conditional statement "Measurements equal to Sample Count" to always
   evaluate to False, and causes the DMM to continue taking measurements in
   the inner loop.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Multi Point Acquisition:Sample Count**
        - C Attribute: **NIDMM_ATTR_SAMPLE_COUNT**

.. py:attribute:: sample_delay_mode

   For the NI 4060 only, specifies a delay interval after a sample trigger.

   +-----+---------------------+-----------------------------------------------------------------------------------------+
   | 0   | IVI compliant       | The Sample Interval property is only used when the Sample Trigger is set to Interval.   |
   +-----+---------------------+-----------------------------------------------------------------------------------------+
   | 1   | Not IVI compliant   | The Sample Interval property is used as a delay after any type of Sample Trigger.       |
   +-----+---------------------+-----------------------------------------------------------------------------------------+

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Multi Point Acquisition:Sample Delay Mode**
        - C Attribute: **NIDMM_ATTR_SAMPLE_DELAY_MODE**

.. py:attribute:: sample_interval

   Specifies the amount of time in seconds the DMM waits between
   measurement cycles. This property only applies when the Sample Trigger
   property is set to INTERVAL. The default value (-1) ensures that the DMM
   settles for a recommended time, which is the same as using an immediate
   trigger.

   The NI 4065 and NI 4070/4071/4072 use the value specified in this
   property as additional delay. On these devices, the onboard timing
   resolution is 34.72 ns and the valid range is 0-149 s.

   On the NI 4060, the value for this property is used as the settling
   time. When this property is set to 0, the NI 4060 does not settle
   between measurement cycles. The onboard timing resolution is 1 micro s
   on the NI 4060.

   Only positive values are valid when setting the sample interval.

   .. note::
      The NI 4080/4081/4082 and NI 4050 are not supported.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Multi Point Acquisition:Sample Interval**
        - C Attribute: **NIDMM_ATTR_SAMPLE_INTERVAL**

.. py:attribute:: sample_trigger

   Specifies the sample trigger source.

   To determine which values are supported by each device, refer to the
   LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.

   The following table lists the characteristics of this property.

   +----------------+--------------------------+
   | Characteristic | Value                    |
   +================+==========================+
   | Datatype       | :py:data:`SampleTrigger` |
   +----------------+--------------------------+
   | Permissions    | read-write               |
   +----------------+--------------------------+
   | Channel Based  | False                    |
   +----------------+--------------------------+
   | Resettable     | No                       |
   +----------------+--------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Multi Point Acquisition:Sample Trigger**
        - C Attribute: **NIDMM_ATTR_SAMPLE_TRIGGER**

.. py:attribute:: sample_trig_slope

   Specifies the edge of the signal from the specified sample trigger
   source on which the DMM is triggered.

   The following table lists the characteristics of this property.

   +----------------+----------------------------+
   | Characteristic | Value                      |
   +================+============================+
   | Datatype       | :py:data:`SampleTrigSlope` |
   +----------------+----------------------------+
   | Permissions    | read-write                 |
   +----------------+----------------------------+
   | Channel Based  | False                      |
   +----------------+----------------------------+
   | Resettable     | No                         |
   +----------------+----------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Multi Point Acquisition:Sample Trig Slope**
        - C Attribute: **NIDMM_ATTR_SAMPLE_TRIG_SLOPE**

.. py:attribute:: secondary_error

   An optional code that provides additional information concerning the
   primary error condition. The error and warning values can be status
   codes defined by IVI, VISA, class drivers, or specific drivers. Zero
   indicates no additional information.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Obsolete:Inherent IVI Attributes:Error Info:Secondary Error**
        - C Attribute: **NIDMM_ATTR_SECONDARY_ERROR**

.. py:attribute:: settle_time

   Specifies the settling time in seconds. Use this property to override
   the default settling time. To return to the default, set this property
   to Auto (-1).

   .. note::
      The NI 4050 and NI 4060 are not supported.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Advanced:Settle Time**
        - C Attribute: **NIDMM_ATTR_SETTLE_TIME**

.. py:attribute:: shunt_value

   For the NI 4050 only, specifies the shunt resistance value.

   .. note::
      The NI 4050 requires an external shunt resistor for current measurements. This property should be set to the value of the shunt resistor.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Shunt Value**
        - C Attribute: **NIDMM_ATTR_SHUNT_VALUE**

.. py:attribute:: simulate

   Specifies whether to simulate instrument driver I/O operations. If
   simulation is enabled, instrument driver functions perform range
   checking and call IVI Get and Set VIs, but they do not perform
   instrument I/O. For output parameters that represent instrument data,
   the instrument driver VIs return calculated values. The default value is
   FALSE (0). Use niDMM Initialize With Options to override the default
   setting.

   .. note::
      Simulate can only be set within the niDMM Initialize With Options VI. The property value cannot be changed outside of the VI.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
        - C Attribute: **NIDMM_ATTR_SIMULATE**

.. py:attribute:: specific_driver_class_spec_major_version

   The major version number of the class specification for the specific
   driver.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | integer   |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Major Version**
        - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION**

.. py:attribute:: specific_driver_class_spec_minor_version

   The minor version number of the class specification for the specific
   driver.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | integer   |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Minor Version**
        - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION**

.. py:attribute:: specific_driver_description

   A string containing a description of the specific driver.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Description**
        - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

.. py:attribute:: specific_driver_major_version

   Returns the major version number of this instrument driver.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | integer   |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Version Info:Specific Driver Major Version**
        - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION**

.. py:attribute:: specific_driver_minor_version

   Returns the minor version number of this instrument driver.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | integer   |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Version Info:Specific Driver Minor Version**
        - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_MINOR_VERSION**

.. py:attribute:: specific_driver_prefix

   The prefix for the specific instrument driver. The name of each
   user-callable VI in this driver starts with this prefix. The prefix can
   be up to a maximum of eight characters.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Instrument Capabilities:Specific Driver Prefix**
        - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_PREFIX**

.. py:attribute:: specific_driver_revision

   A string that contains additional version information about this
   instrument driver.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Version Info:Specific Driver Revision**
        - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_REVISION**

.. py:attribute:: specific_driver_vendor

   A string containing the vendor of the specific driver.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Vendor**
        - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_VENDOR**

.. py:attribute:: supported_instrument_models

   A string containing the instrument models supported by the specific
   driver.

   The following table lists the characteristics of this property.

   +----------------+-----------+
   | Characteristic | Value     |
   +================+===========+
   | Datatype       | string    |
   +----------------+-----------+
   | Permissions    | read only |
   +----------------+-----------+
   | Channel Based  | False     |
   +----------------+-----------+
   | Resettable     | No        |
   +----------------+-----------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Capabilities:Supported Instrument Models**
        - C Attribute: **NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS**

.. py:attribute:: susceptance

   For the NI 4082 and NI 4072 only, specifies the reactive part
   (susceptance) of the open cable compensation. The valid range is any
   real number >0. The default value (-1.0) indicates that compensation has
   not taken place.

   .. note::
      Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Susceptance**
        - C Attribute: **NIDMM_ATTR_SUSCEPTANCE**

.. py:attribute:: tc_fixed_ref_junction

   Specifies the value of the fixed reference junction temperature for a
   thermocouple in degrees Celsius.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Fixed Reference Junction**
        - C Attribute: **NIDMM_ATTR_TC_FIXED_REF_JUNCTION**

.. py:attribute:: tc_ref_junction_type

   Specifies the thermocouple reference junction type.

   The following table lists the characteristics of this property.

   +----------------+----------------------------------------------+
   | Characteristic | Value                                        |
   +================+==============================================+
   | Datatype       | :py:data:`ThermocoupleReferenceJunctionType` |
   +----------------+----------------------------------------------+
   | Permissions    | read-write                                   |
   +----------------+----------------------------------------------+
   | Channel Based  | False                                        |
   +----------------+----------------------------------------------+
   | Resettable     | No                                           |
   +----------------+----------------------------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Reference Junction Type**
        - C Attribute: **NIDMM_ATTR_TC_REF_JUNCTION_TYPE**

.. py:attribute:: thermistor_a

   Specifies the Steinhart-Hart A coefficient for thermistor scaling when
   the **Thermistor Type property** is set to Custom.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor A**
        - C Attribute: **NIDMM_ATTR_THERMISTOR_A**

.. py:attribute:: thermistor_b

   Specifies the Steinhart-Hart B coefficient for thermistor scaling when
   the **Thermistor Type property** is set to Custom.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor B**
        - C Attribute: **NIDMM_ATTR_THERMISTOR_B**

.. py:attribute:: thermistor_c

   Specifies the Steinhart-Hart C coefficient for thermistor scaling when
   the **Thermistor Type property** is set to Custom.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor C**
        - C Attribute: **NIDMM_ATTR_THERMISTOR_C**

.. py:attribute:: thermistor_type

   Specifies the thermistor type.

   The following table lists the characteristics of this property.

   +----------------+---------------------------+
   | Characteristic | Value                     |
   +================+===========================+
   | Datatype       | :py:data:`ThermistorType` |
   +----------------+---------------------------+
   | Permissions    | read-write                |
   +----------------+---------------------------+
   | Channel Based  | False                     |
   +----------------+---------------------------+
   | Resettable     | No                        |
   +----------------+---------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type**
        - C Attribute: **NIDMM_ATTR_THERMISTOR_TYPE**

.. py:attribute:: thermocouple_type

   Specifies the thermocouple type.

   The following table lists the characteristics of this property.

   +----------------+-----------------------------+
   | Characteristic | Value                       |
   +================+=============================+
   | Datatype       | :py:data:`ThermocoupleType` |
   +----------------+-----------------------------+
   | Permissions    | read-write                  |
   +----------------+-----------------------------+
   | Channel Based  | False                       |
   +----------------+-----------------------------+
   | Resettable     | No                          |
   +----------------+-----------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type**
        - C Attribute: **NIDMM_ATTR_THERMOCOUPLE_TYPE**

.. py:attribute:: transducer_type

   Specifies the transducer type.

   The following table lists the characteristics of this property.

   +----------------+---------------------------+
   | Characteristic | Value                     |
   +================+===========================+
   | Datatype       | :py:data:`TransducerType` |
   +----------------+---------------------------+
   | Permissions    | read-write                |
   +----------------+---------------------------+
   | Channel Based  | False                     |
   +----------------+---------------------------+
   | Resettable     | No                        |
   +----------------+---------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Configuration:Measurement Options:Temperature:Transducer Type**
        - C Attribute: **NIDMM_ATTR_TRANSDUCER_TYPE**

.. py:attribute:: trigger_count

   Specifies the number of triggers the DMM receives before returning to
   the Idle state. This property can be set to any positive ViInt32 value
   for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

   The NI 4050/4060 only support this property being set to 1.

   Refer to Multiple Point Acquisitions in the *NI Digital Multimeters
   Help* for more information.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Multi Point Acquisition:Trigger Count**
        - C Attribute: **NIDMM_ATTR_TRIGGER_COUNT**

.. py:attribute:: trigger_delay

   Specifies the time (in seconds) that the DMM waits after it has received
   a trigger before taking a measurement. The default value is Auto Delay
   (-1), which means that the DMM waits an appropriate settling time before
   taking the measurement.

   The NI 4080/4081/4082 uses the value specified in this property as
   additional settling time. The valid range for Trigger Delay is Auto
   Delay (-1) or 0.0 - 150.0 seconds, and the onboard timing resolution is
   10.0 ns.

   The NI 4065 and NI 4070/4071/4072 use the value specified in this
   property as additional settling time. For these devices, the valid range
   for Trigger Delay is Auto Delay (-1) or 0.0 - 149.0 seconds and the
   onboard timing resolution is 34.72 ns.

   On the NI 4060, if this property is set to 0, the DMM does not settle
   before taking the measurement. On the NI 4060, the valid range for
   Trigger Delay (-1) is 0.0-12.0 seconds and the onboard timing resolution
   is 100 ms.

   When using the NI 4050, this property must be set to Auto Delay (-1).

   Use positive values to set the trigger delay in seconds.

   Valid Range: Auto Delay (-1.0), 0.0-12.0 seconds (NI 4060 only),
   0.0-149.0 seconds (NI 4065 and NI 4070/4071/4072)

   Default Value: Auto Delay

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Trigger:Trigger Delay**
        - C Attribute: **NIDMM_ATTR_TRIGGER_DELAY**

.. py:attribute:: trigger_slope

   Specifies the edge of the signal from the specified trigger source on
   which the DMM is triggered.

   The following table lists the characteristics of this property.

   +----------------+-------------------------+
   | Characteristic | Value                   |
   +================+=========================+
   | Datatype       | :py:data:`TriggerSlope` |
   +----------------+-------------------------+
   | Permissions    | read-write              |
   +----------------+-------------------------+
   | Channel Based  | False                   |
   +----------------+-------------------------+
   | Resettable     | No                      |
   +----------------+-------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Trigger:Trigger Slope**
        - C Attribute: **NIDMM_ATTR_TRIGGER_SLOPE**

.. py:attribute:: trigger_source

   Specifies the trigger source. When niDMM Initiate is called, the DMM
   waits for the trigger specified with this property. After it receives
   the trigger, the DMM waits the length of time specified with the Trigger
   Delay property. The DMM then takes a measurement.

   To determine which values are supported by each device, refer to the
   LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.

   The following table lists the characteristics of this property.

   +----------------+--------------------------+
   | Characteristic | Value                    |
   +================+==========================+
   | Datatype       | :py:data:`TriggerSource` |
   +----------------+--------------------------+
   | Permissions    | read-write               |
   +----------------+--------------------------+
   | Channel Based  | False                    |
   +----------------+--------------------------+
   | Resettable     | No                       |
   +----------------+--------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Trigger:Trigger Source**
        - C Attribute: **NIDMM_ATTR_TRIGGER_SOURCE**

.. py:attribute:: waveform_coupling

   For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
   coupling during a waveform acquisition.

   The following table lists the characteristics of this property.

   +----------------+-----------------------------+
   | Characteristic | Value                       |
   +================+=============================+
   | Datatype       | :py:data:`WaveformCoupling` |
   +----------------+-----------------------------+
   | Permissions    | read-write                  |
   +----------------+-----------------------------+
   | Channel Based  | False                       |
   +----------------+-----------------------------+
   | Resettable     | No                          |
   +----------------+-----------------------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Waveform Acquisition:Waveform Coupling**
        - C Attribute: **NIDMM_ATTR_WAVEFORM_COUPLING**

.. py:attribute:: waveform_points

   For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
   points to acquire in a waveform acquisition.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | integer    |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Waveform Acquisition:Waveform Points**
        - C Attribute: **NIDMM_ATTR_WAVEFORM_POINTS**

.. py:attribute:: waveform_rate

   Specifies the rate of the waveform acquisition in samples per second
   (S/s). The valid rate is calculated by dividing 1,800,000 by an integer
   divisor, and the rate falls between 10 and 1,800,000 samples per second.
   The waveform rate is coerced upwards to the next valid rate. The default
   value is 1,800,000 samples per second. Not supported by NI 4065.

   The following table lists the characteristics of this property.

   +----------------+------------+
   | Characteristic | Value      |
   +================+============+
   | Datatype       | float      |
   +----------------+------------+
   | Permissions    | read-write |
   +----------------+------------+
   | Channel Based  | False      |
   +----------------+------------+
   | Resettable     | No         |
   +----------------+------------+

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

        - LabVIEW Property: **Waveform Acquisition:Waveform Rate**
        - C Attribute: **NIDMM_ATTR_WAVEFORM_RATE**


