.. py:module:: nidmm

Session
=======

.. py:class:: Session(self, resource_name, id_query=False, reset_device=False, options={})

    

    This method completes the following tasks:

    -  Creates a new IVI instrument driver session and, optionally, sets the
       initial state of the following session properties:
       :py:attr:`nidmm.Session.range_check`, :py:attr:`nidmm.Session.QUERY_INSTR_STATUS`,
       :py:attr:`nidmm.Session.cache`, :py:attr:`nidmm.Session.simulate`,
       :py:attr:`nidmm.Session.record_coercions`.
    -  Opens a session to the device you specify for the **Resource_Name**
       parameter. If the **ID_Query** parameter is set to True, this
       method queries the instrument ID and checks that it is valid for
       this instrument driver.
    -  If the **Reset_Device** parameter is set to True, this method
       resets the instrument to a known state. Sends initialization commands
       to set the instrument to the state necessary for the operation of the
       instrument driver.
    -  Returns a ViSession handle that you use to identify the instrument in
       all subsequent instrument driver method calls.

    

    .. note:: One or more of the referenced properties are not in the Python API for this driver.



    :param resource_name:
        

        .. caution:: All IVI names for the **Resource_Name**, such as logical names or
            virtual names, are case-sensitive. If you use logical names, driver
            session names, or virtual names in your program, you must make sure that
            the name you use matches the name in the IVI Configuration Store file
            exactly, without any variations in the case of the characters in the
            name.

        | Contains the **resource_name** of the device to initialize. The
          **resource_name** is assigned in Measurement & Automation Explorer
          (MAX). Refer to `Related
          Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__
          for the *NI Digital Multimeters Getting Started Guide* for more
          information about configuring and testing the DMM in MAX.
        | Valid Syntax:

        -  NI-DAQmx name
        -  DAQ::NI-DAQmx name[::INSTR]
        -  DAQ::Traditional NI-DAQ device number[::INSTR]
        -  IVI logical name

        


    :type resource_name: str

    :param id_query:
        

        Verifies that the device you initialize is one that the driver supports.
        NI-DMM automatically performs this query, so setting this parameter is
        not necessary.
        Defined Values:

        +----------------+---+------------------+
        | True (default) | 1 | Perform ID Query |
        +----------------+---+------------------+
        | False          | 0 | Skip ID Query    |
        +----------------+---+------------------+


    :type id_query: bool

    :param reset_device:
        

        Specifies whether to reset the instrument during the initialization
        procedure.
        Defined Values:

        +----------------+---+--------------+
        | True (default) | 1 | Reset Device |
        +----------------+---+--------------+
        | False          | 0 | Don't Reset  |
        +----------------+---+--------------+


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

    .. py:currentmodule:: nidmm.Session

    .. py:method:: abort()

            Aborts a previously initiated measurement and returns the DMM to the
            Idle state.

            



close
-----

    .. py:currentmodule:: nidmm.Session

    .. py:method:: close()

            Closes the specified session and deallocates resources that it reserved.

            

            .. note:: This method is not needed when using the session context manager



configure_measurement_absolute
------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_measurement_absolute(measurement_function, range, resolution_absolute)

            Configures the common properties of the measurement. These properties
            include :py:attr:`nidmm.Session.method`, :py:attr:`nidmm.Session.range`, and
            :py:attr:`nidmm.Session.resolution_absolute`.

            



            :param measurement_function:


                Specifies the **measurement_function** used to acquire the measurement.
                The driver sets :py:attr:`nidmm.Session.method` to this value.

                


            :type measurement_function: :py:data:`nidmm.Function`
            :param range:


                Specifies the **range** for the method specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other methods, you must supply a **range** that exceeds the
                value that you are measuring. For example, you must type in 10 V if you
                are measuring 9 V. **range** values are coerced up to the closest input
                **range**. Refer to the `Devices
                Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
                ranges. The driver sets :py:attr:`nidmm.Session.range` to this value. The default is
                0.02 V.

                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON`   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                                  |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_OFF`  | -2.0 | NI-DMM sets the Range to the current :py:attr:`nidmm.Session.auto_range_value` and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE` | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The :py:attr:`nidmm.Session.auto_range_value` is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                .. note:: The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                    trigger and sample trigger are set to IMMEDIATE.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type range: float
            :param resolution_absolute:


                Specifies the absolute resolution for the measurement. NI-DMM sets
                :py:attr:`nidmm.Session.resolution_absolute` to this value. The PXIe-4080/4081/4082
                uses the resolution you specify. The NI 4065 and NI 4070/4071/4072
                ignore this parameter when the **Range** parameter is set to
                :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON` (-1.0) or :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE`
                (-3.0). The default is 0.001 V.

                

                .. note:: NI-DMM ignores this parameter for capacitance and inductance
                    measurements on the NI 4072. To achieve better resolution for such
                    measurements, use the :py:attr:`nidmm.Session.lc_number_meas_to_average`
                    property.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type resolution_absolute: float

configure_measurement_digits
----------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_measurement_digits(measurement_function, range, resolution_digits)

            Configures the common properties of the measurement. These properties
            include :py:attr:`nidmm.Session.method`, :py:attr:`nidmm.Session.range`, and
            :py:attr:`nidmm.Session.resolution_digits`.

            



            :param measurement_function:


                Specifies the **measurement_function** used to acquire the measurement.
                The driver sets :py:attr:`nidmm.Session.method` to this value.

                


            :type measurement_function: :py:data:`nidmm.Function`
            :param range:


                Specifies the range for the method specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other methods, you must supply a range that exceeds the value
                that you are measuring. For example, you must type in 10 V if you are
                measuring 9 V. range values are coerced up to the closest input range.
                Refer to the `Devices
                Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
                ranges. The driver sets :py:attr:`nidmm.Session.range` to this value. The default is
                0.02 V.

                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON`   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                                  |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_OFF`  | -2.0 | NI-DMM sets the Range to the current :py:attr:`nidmm.Session.auto_range_value` and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE` | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The :py:attr:`nidmm.Session.auto_range_value` is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                .. note:: The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                    trigger and sample trigger are set to IMMEDIATE.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type range: float
            :param resolution_digits:


                Specifies the resolution of the measurement in digits. The driver sets
                the `Devices Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a
                list of valid ranges. The driver sets :py:attr:`nidmm.Session.resolution_digits`
                property to this value. The PXIe-4080/4081/4082 uses the resolution you
                specify. The NI 4065 and NI 4070/4071/4072 ignore this parameter when
                the **Range** parameter is set to :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON` (-1.0) or
                :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE` (-3.0). The default is 5½.

                

                .. note:: NI-DMM ignores this parameter for capacitance and inductance
                    measurements on the NI 4072. To achieve better resolution for such
                    measurements, use the :py:attr:`nidmm.Session.lc_number_meas_to_average`
                    property.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type resolution_digits: float

configure_multi_point
---------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_multi_point(trigger_count, sample_count, sample_trigger=nidmm.SampleTrigger.IMMEDIATE, sample_interval=datetime.timedelta(seconds=-1))

            Configures the properties for multipoint measurements. These properties
            include :py:attr:`nidmm.Session.trigger_count`, :py:attr:`nidmm.Session.sample_count`,
            :py:attr:`nidmm.Session.sample_trigger`, and :py:attr:`nidmm.Session.sample_interval`.

            For continuous acquisitions, set :py:attr:`nidmm.Session.trigger_count` or
            :py:attr:`nidmm.Session.sample_count` to zero. For more information, refer to
            `Multiple Point
            Acquisitions <REPLACE_DRIVER_SPECIFIC_URL_1(multi_point)>`__,
            `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__, and `Using
            Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__.

            



            :param trigger_count:


                Sets the number of triggers you want the DMM to receive before returning
                to the Idle state. The driver sets :py:attr:`nidmm.Session.trigger_count` to this
                value. The default value is 1.

                


            :type trigger_count: int
            :param sample_count:


                Sets the number of measurements the DMM makes in each measurement
                sequence initiated by a trigger. The driver sets
                :py:attr:`nidmm.Session.sample_count` to this value. The default value is 1.

                


            :type sample_count: int
            :param sample_trigger:


                Specifies the **sample_trigger** source you want to use. The driver
                sets :py:attr:`nidmm.Session.sample_trigger` to this value. The default is
                Immediate.

                

                .. note:: To determine which values are supported by each device, refer to the
                    `LabWindows/CVI Trigger
                    Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.


            :type sample_trigger: :py:data:`nidmm.SampleTrigger`
            :param sample_interval:


                Sets the amount of time in seconds the DMM waits between measurement
                cycles. The driver sets :py:attr:`nidmm.Session.sample_interval` to this value.
                Specify a sample interval to add settling time between measurement
                cycles or to decrease the measurement rate. **sample_interval** only
                applies when the **Sample_Trigger** is set to INTERVAL.

                On the NI 4060, the **sample_interval** value is used as the settling
                time. When sample interval is set to 0, the DMM does not settle between
                measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
                specified in **sample_interval** as additional delay. The default value
                (-1) ensures that the DMM settles for a recommended time. This is the
                same as using an Immediate trigger.

                

                .. note:: This property is not used on the NI 4080/4081/4082 and the NI 4050.


            :type sample_interval: float in seconds or datetime.timedelta

configure_rtd_custom
--------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_rtd_custom(rtd_a, rtd_b, rtd_c)

            Configures the A, B, and C parameters for a custom RTD.

            



            :param rtd_a:


                Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the :py:meth:`nidmm.Session.configure_rtd_type` method.
                The default is 3.9083e-3 (Pt3851)

                


            :type rtd_a: float
            :param rtd_b:


                Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the :py:meth:`nidmm.Session.configure_rtd_type` method.
                The default is -5.775e-7 (Pt3851).

                


            :type rtd_b: float
            :param rtd_c:


                Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the :py:meth:`nidmm.Session.configure_rtd_type` method.
                The default is -4.183e-12 (Pt3851).

                


            :type rtd_c: float

configure_rtd_type
------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_rtd_type(rtd_type, rtd_resistance)

            Configures the RTD Type and RTD Resistance parameters for an RTD.

            



            :param rtd_type:


                Specifies the type of RTD used to measure the temperature resistance.
                NI-DMM uses this value to set the RTD Type property. The default is
                :py:data:`~nidmm.RTDType.PT3851`.

                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | Enum                             | Standards                                     | Material | TCR (α) | Typical R\ :sub:`0` (Ω) | Notes                                                                         |                               |
                +==================================+===============================================+==========+=========+=========================+===============================================================================+===============================+
                | Callendar-Van Dusen Coefficient  |                                               |          |         |                         |                                                                               |                               |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3851` | IEC-751 DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω            | A = 3.9083 × 10\ :sup:`–3` B = –5.775×10:sup:`–7` C = –4.183×10:sup:`–12`     | Most common RTDs              |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3750` | Low-cost vendor compliant RTD\*               | Platinum | .003750 | 1000 Ω                  | A = 3.81 × 10\ :sup:`–3` B = –6.02×10:sup:`–7` C = –6.0×10:sup:`–12`          | Low-cost RTD                  |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3916` | JISC 1604                                     | Platinum | .003916 | 100 Ω                   | A = 3.9739 × 10\ :sup:`–3` B = –5.870×10:sup:`–7` C = –4.4 ×10\ :sup:`–12`    | Used in primarily in Japan    |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3920` | US Industrial Standard D-100 American         | Platinum | .003920 | 100 Ω                   | A = 3.9787 × 10\ :sup:`–3` B = –5.8686×10:sup:`–7` C = –4.167 ×10\ :sup:`–12` | Low-cost RTD                  |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3911` | US Industrial Standard American               | Platinum | .003911 | 100 Ω                   | A = 3.9692 × 10\ :sup:`–3` B = –5.8495×10:sup:`–7` C = –4.233 ×10\ :sup:`–12` | Low-cost RTD                  |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3928` | ITS-90                                        | Platinum | .003928 | 100 Ω                   | A = 3.9888 × 10\ :sup:`–3` B = –5.915×10:sup:`–7` C = –3.85 ×10\ :sup:`–12`   | The definition of temperature |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | \*No standard. Check the TCR.    |                                               |          |         |                         |                                                                               |                               |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+


            :type rtd_type: :py:data:`nidmm.RTDType`
            :param rtd_resistance:


                Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
                set the RTD Resistance property. The default is 100 (Ω).

                


            :type rtd_resistance: float

configure_thermistor_custom
---------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_thermistor_custom(thermistor_a, thermistor_b, thermistor_c)

            Configures the A, B, and C parameters for a custom thermistor.

            



            :param thermistor_a:


                Specifies the Steinhart-Hart A coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the :py:meth:`nidmm.Session.configure_thermistor_type`
                method. The default is 1.0295e-3 (44006).

                


            :type thermistor_a: float
            :param thermistor_b:


                Specifies the Steinhart-Hart B coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the :py:meth:`nidmm.Session.configure_thermistor_type`
                method. The default is 2.391e-4 (44006).

                


            :type thermistor_b: float
            :param thermistor_c:


                Specifies the Steinhart-Hart C coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the :py:meth:`nidmm.Session.configure_thermistor_type`
                method. The default is 1.568e-7 (44006).

                


            :type thermistor_c: float

configure_thermocouple
----------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_thermocouple(thermocouple_type, reference_junction_type=nidmm.ThermocoupleReferenceJunctionType.FIXED)

            Configures the thermocouple type and reference junction type for a
            chosen thermocouple.

            



            :param thermocouple_type:


                Specifies the type of thermocouple used to measure the temperature.
                NI-DMM uses this value to set the Thermocouple Type property. The
                default is :py:data:`~nidmm.ThermocoupleType.J`.

                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.B` | Thermocouple type B |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.E` | Thermocouple type E |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.J` | Thermocouple type J |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.K` | Thermocouple type K |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.N` | Thermocouple type N |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.R` | Thermocouple type R |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.S` | Thermocouple type S |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.T` | Thermocouple type T |
                +--------------------------------------+---------------------+


            :type thermocouple_type: :py:data:`nidmm.ThermocoupleType`
            :param reference_junction_type:


                Specifies the type of reference junction to be used in the reference
                junction compensation of a thermocouple measurement. NI-DMM uses this
                value to set the Reference Junction Type property. The only supported
                value is :py:data:`~nidmm.NIDMM_VAL_TEMP_REF_JUNC_FIXED`.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type reference_junction_type: :py:data:`nidmm.ThermocoupleReferenceJunctionType`

configure_trigger
-----------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_trigger(trigger_source, trigger_delay=datetime.timedelta(seconds=-1))

            Configures the DMM **Trigger_Source** and **Trigger_Delay**. Refer to
            `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__ and `Using
            Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__ for more
            information.

            



            :param trigger_source:


                Specifies the **trigger_source** that initiates the acquisition. The
                driver sets :py:attr:`nidmm.Session.trigger_source` to this value. Software
                configures the DMM to wait until :py:meth:`nidmm.Session.send_software_trigger` is called
                before triggering the DMM.

                

                .. note:: To determine which values are supported by each device, refer to the
                    `LabWindows/CVI Trigger
                    Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.


            :type trigger_source: :py:data:`nidmm.TriggerSource`
            :param trigger_delay:


                Specifies the time that the DMM waits after it has received a trigger
                before taking a measurement. The driver sets the
                :py:attr:`nidmm.Session.trigger_delay` property to this value. By default,
                **trigger_delay** is :py:data:`~nidmm.NIDMM_VAL_AUTO_DELAY` (-1), which means the DMM
                waits an appropriate settling time before taking the measurement. On the
                NI 4060, if you set **trigger_delay** to 0, the DMM does not settle
                before taking the measurement. The NI 4065 and NI 4070/4071/4072 use the
                value specified in **trigger_delay** as additional settling time.

                

                .. note:: When using the NI 4050, **Trigger_Delay** must be set to
                    :py:data:`~nidmm.NIDMM_VAL_AUTO_DELAY` (-1).

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger_delay: float in seconds or datetime.timedelta

configure_waveform_acquisition
------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_waveform_acquisition(measurement_function, range, rate, waveform_points)

            Configures the DMM for waveform acquisitions. This feature is supported
            on the NI 4080/4081/4082 and the NI 4070/4071/4072.

            



            :param measurement_function:


                Specifies the **measurement_function** used in a waveform acquisition.
                The driver sets :py:attr:`nidmm.Session.method` to this value.

                +-----------------------------------------------------+------+------------------+
                | :py:data:`~nidmm.Method.WAVEFORM_VOLTAGE` (default) | 1003 | Voltage Waveform |
                +-----------------------------------------------------+------+------------------+
                | :py:data:`~nidmm.Method.WAVEFORM_CURRENT`           | 1004 | Current Waveform |
                +-----------------------------------------------------+------+------------------+


            :type measurement_function: :py:data:`nidmm.Function`
            :param range:


                Specifies the expected maximum amplitude of the input signal and sets
                the **range** for the **Measurement_Function**. NI-DMM sets
                :py:attr:`nidmm.Session.range` to this value. **range** values are coerced up to the
                closest input **range**. The default is 10.0.

                For valid ranges refer to the topics in
                `Devices <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__.

                Auto-ranging is not supported during waveform acquisitions.

                


            :type range: float
            :param rate:


                Specifies the **rate** of the acquisition in samples per second. NI-DMM
                sets :py:attr:`nidmm.Session.waveform_rate` to this value.

                The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
                to the closest integer divisor of 1,800,000. The default value is
                1,800,000.

                


            :type rate: float
            :param waveform_points:


                Specifies the number of points to acquire before the waveform
                acquisition completes. NI-DMM sets :py:attr:`nidmm.Session.waveform_points` to this
                value.

                To calculate the maximum and minimum number of waveform points that you
                can acquire in one acquisition, refer to the `Waveform Acquisition
                Measurement Cycle <REPLACE_DRIVER_SPECIFIC_URL_1(waveform_cycle)>`__.

                The default value is 500.

                


            :type waveform_points: int

disable
-------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: disable()

            Places the instrument in a quiescent state where it has minimal or no
            impact on the system to which it is connected. If a measurement is in
            progress when this method is called, the measurement is aborted.

            



export_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: export_attribute_configuration_buffer()

            Exports the property configuration of the session to the specified
            configuration buffer.

            You can export and import session property configurations only between
            devices with identical model numbers.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑DMM returns an
            error.

            **Coercion Behavior for Certain Devices**

            Imported and exported property configurations contain coerced values
            for the following NI‑DMM devices:

            -  PXI/PCI/PCIe/USB‑4065
            -  PXI/PCI‑4070
            -  PXI‑4071
            -  PXI‑4072

            NI‑DMM coerces property values when the value you set is within the
            allowed range for the property but is not one of the discrete valid
            values the property supports. For example, for a property that
            coerces values up, if you choose a value of 4 when the adjacent valid
            values are 1 and 10, the property coerces the value to 10.

            **Related Topics:**

            `Using Properties and Properties with
            NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

            `Setting Properties Before Reading
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            

            .. note:: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.



            :rtype: list of int
            :return:


                    Specifies the byte array buffer to be populated with the exported
                    property configuration.

                    



export_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: export_attribute_configuration_file(file_path)

            Exports the property configuration of the session to the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑DMM returns an
            error.

            **Coercion Behavior for Certain Devices**

            Imported and exported property configurations contain coerced values
            for the following NI‑DMM devices:

            -  PXI/PCI/PCIe/USB‑4065
            -  PXI/PCI‑4070
            -  PXI‑4071
            -  PXI‑4072

            NI‑DMM coerces property values when the value you set is within the
            allowed range for the property but is not one of the discrete valid
            values the property supports. For example, for a property that
            coerces values up, if you choose a value of 4 when the adjacent valid
            values are 1 and 10, the property coerces the value to 10.

            **Related Topics:**

            `Using Properties and Properties with
            NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

            `Setting Properties Before Reading
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            

            .. note:: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.



            :param file_path:


                Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:**\  .nidmmconfig

                


            :type file_path: str

fetch
-----

    .. py:currentmodule:: nidmm.Session

    .. py:method:: fetch(maximum_time=datetime.timedelta(milliseconds=-1))

            Returns the value from a previously initiated measurement. You must call
            :py:meth:`nidmm.Session._initiate` before calling this method.

            



            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: float in seconds or datetime.timedelta

            :rtype: float
            :return:


                    The measured value returned from the DMM.

                    



fetch_multi_point
-----------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: fetch_multi_point(array_size, maximum_time=datetime.timedelta(milliseconds=-1))

            Returns an array of values from a previously initiated multipoint
            measurement. The number of measurements the DMM makes is determined by
            the values you specify for the **Trigger_Count** and **Sample_Count**
            parameters of :py:meth:`nidmm.Session.configure_multi_point`. You must first call
            :py:meth:`nidmm.Session._initiate` to initiate a measurement before calling this method.

            



            :param array_size:


                Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in :py:meth:`nidmm.Session.configure_multi_point`.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

                


            :type array_size: int
            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: float in seconds or datetime.timedelta

            :rtype: tuple (reading_array, actual_number_of_points)

                WHERE

                reading_array (array.array("d")): 


                    An array of measurement values.

                    

                    .. note:: The size of the **Reading_Array** must be at least the size that you
                        specify for the **Array_Size** parameter.


                actual_number_of_points (int): 


                    Indicates the number of measured values actually retrieved from the DMM.

                    



fetch_waveform
--------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: fetch_waveform(array_size, maximum_time=datetime.timedelta(milliseconds=-1))

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
            values from a previously initiated waveform acquisition. You must call
            :py:meth:`nidmm.Session._initiate` before calling this method.

            



            :param array_size:


                Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of :py:meth:`nidmm.Session.configure_waveform_acquisition`. The default value is
                1.

                


            :type array_size: int
            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: float in seconds or datetime.timedelta

            :rtype: tuple (waveform_array, actual_number_of_points)

                WHERE

                waveform_array (array.array("d")): 


                    **Waveform Array** is an array of measurement values stored in waveform
                    data type.

                    


                actual_number_of_points (int): 


                    Indicates the number of measured values actually retrieved from the DMM.

                    



fetch_waveform_into
-------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: fetch_waveform_into(array_size, maximum_time=datetime.timedelta(milliseconds=-1))

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
            values from a previously initiated waveform acquisition. You must call
            :py:meth:`nidmm.Session._initiate` before calling this method.

            



            :param waveform_array:


                **Waveform Array** is an array of measurement values stored in waveform
                data type.

                


            :type waveform_array: numpy.array(dtype=numpy.float64)
            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: float in seconds or datetime.timedelta

            :rtype: tuple (waveform_array, actual_number_of_points)

                WHERE

                waveform_array (numpy.array(dtype=numpy.float64)): 


                    **Waveform Array** is an array of measurement values stored in waveform
                    data type.

                    


                actual_number_of_points (int): 


                    Indicates the number of measured values actually retrieved from the DMM.

                    



get_cal_date_and_time
---------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: get_cal_date_and_time(cal_type)

            Returns the date and time of the last calibration performed.

            

            .. note:: The NI 4050 and NI 4060 are not supported.



            :param cal_type:


                Specifies the type of calibration performed (external or self-calibration).

                +-----------------------------------------------------+---+----------------------+
                | :py:data:`~nidmm.NIDMM_VAL_INTERNAL_AREA` (default) | 0 | Self-Calibration     |
                +-----------------------------------------------------+---+----------------------+
                | :py:data:`~nidmm.NIDMM_VAL_EXTERNAL_AREA`           | 1 | External Calibration |
                +-----------------------------------------------------+---+----------------------+

                .. note:: The NI 4065 does not support self-calibration.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type cal_type: int

            :rtype: datetime.datetime
            :return:


                    Indicates date and time of the last calibration.

                    



get_dev_temp
------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: get_dev_temp(options="")

            Returns the current **Temperature** of the device.

            

            .. note:: The NI 4050 and NI 4060 are not supported.



            :param options:


                Reserved.

                


            :type options: str

            :rtype: float
            :return:


                    Returns the current **temperature** of the device.

                    



get_ext_cal_recommended_interval
--------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: get_ext_cal_recommended_interval()

            Returns the recommended interval between external recalibration in
            **Months**.

            

            .. note:: The NI 4050 and NI 4060 are not supported.



            :rtype: datetime.timedelta
            :return:


                    Returns the recommended number of **months** between external
                    calibrations.

                    



get_last_cal_temp
-----------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: get_last_cal_temp(cal_type)

            Returns the **Temperature** during the last calibration procedure.

            

            .. note:: The NI 4050 and NI 4060 are not supported.



            :param cal_type:


                Specifies the type of calibration performed (external or
                self-calibration).

                +-----------------------------------------------------+---+----------------------+
                | :py:data:`~nidmm.NIDMM_VAL_INTERNAL_AREA` (default) | 0 | Self-Calibration     |
                +-----------------------------------------------------+---+----------------------+
                | :py:data:`~nidmm.NIDMM_VAL_EXTERNAL_AREA`           | 1 | External Calibration |
                +-----------------------------------------------------+---+----------------------+

                .. note:: The NI 4065 does not support self-calibration.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type cal_type: int

            :rtype: float
            :return:


                    Returns the **temperature** during the last calibration.

                    



get_self_cal_supported
----------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: get_self_cal_supported()

            Returns a Boolean value that expresses whether or not the DMM that you
            are using can perform self-calibration.

            



            :rtype: bool
            :return:


                    Returns whether Self Cal is supported for the device specified by the
                    given session.

                    +-------+---+-------------------------------------------------------------+
                    | True  | 1 | The DMM that you are using can perform self-calibration.    |
                    +-------+---+-------------------------------------------------------------+
                    | False | 0 | The DMM that you are using cannot perform self-calibration. |
                    +-------+---+-------------------------------------------------------------+



import_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: import_attribute_configuration_buffer(configuration)

            Imports a property configuration to the session from the specified
            configuration buffer.

            You can export and import session property configurations only between
            devices with identical model numbers.

            **Coercion Behavior for Certain Devices**

            Imported and exported property configurations contain coerced values
            for the following NI‑DMM devices:

            -  PXI/PCI/PCIe/USB‑4065
            -  PXI/PCI‑4070
            -  PXI‑4071
            -  PXI‑4072

            NI‑DMM coerces property values when the value you set is within the
            allowed range for the property but is not one of the discrete valid
            values the property supports. For example, for a property that
            coerces values up, if you choose a value of 4 when the adjacent valid
            values are 1 and 10, the property coerces the value to 10.

            **Related Topics:**

            `Using Properties and Properties with
            NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

            `Setting Properties Before Reading
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            

            .. note:: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.



            :param configuration:


                Specifies the byte array buffer that contains the property
                configuration to import.

                


            :type configuration: list of int

import_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: import_attribute_configuration_file(file_path)

            Imports a property configuration to the session from the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers.

            **Coercion Behavior for Certain Devices**

            Imported and exported property configurations contain coerced values
            for the following NI‑DMM devices:

            -  PXI/PCI/PCIe/USB‑4065
            -  PXI/PCI‑4070
            -  PXI‑4071
            -  PXI‑4072

            NI‑DMM coerces property values when the value you set is within the
            allowed range for the property but is not one of the discrete valid
            values the property supports. For example, for a property that
            coerces values up, if you choose a value of 4 when the adjacent valid
            values are 1 and 10, the property coerces the value to 10.

            **Related Topics:**

            `Using Properties and Properties with
            NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

            `Setting Properties Before Reading
            Properties <javascript:LaunchHelp('DMM.chm::/setting_before_reading_attributes')>`__

            

            .. note:: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.



            :param file_path:


                Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:**\  .nidmmconfig

                


            :type file_path: str

initiate
--------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: initiate()

            Initiates an acquisition. After you call this method, the DMM leaves
            the Idle state and enters the Wait-for-Trigger state. If trigger is set
            to Immediate mode, the DMM begins acquiring measurement data. Use
            :py:meth:`nidmm.Session.fetch`, :py:meth:`nidmm.Session.fetch_multi_point`, or :py:meth:`nidmm.Session.fetch_waveform` to
            retrieve the measurement data.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



lock
----

    .. py:currentmodule:: nidmm.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`nidmm.Session.lock` method.
        -  A call to NI-DMM locked the session.
        -  After a call to the :py:meth:`nidmm.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`nidmm.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`nidmm.Session.lock` method and the
           :py:meth:`nidmm.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nidmm.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nidmm.Session.lock` method with a call to
    the :py:meth:`nidmm.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with nidmm.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`nidmm.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited


perform_open_cable_comp
-----------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: perform_open_cable_comp()

            For the NI 4082 and NI 4072 only, performs the open cable compensation
            measurements for the current capacitance/inductance range, and returns
            open cable compensation **Conductance** and **Susceptance** values. You
            can use the return values of this method as inputs to
            :py:meth:`nidmm.Session.configure_open_cable_comp_values`.

            This method returns an error if the value of the :py:attr:`nidmm.Session.method`
            property is not set to :py:data:`~nidmm.Method.CAPACITANCE` (1005) or
            :py:data:`~nidmm.Method.INDUCTANCE` (1006).

            



            :rtype: tuple (conductance, susceptance)

                WHERE

                conductance (float): 


                    **conductance** is the measured value of open cable compensation
                    **conductance**.

                    


                susceptance (float): 


                    **susceptance** is the measured value of open cable compensation
                    **susceptance**.

                    



perform_short_cable_comp
------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: perform_short_cable_comp()

            Performs the short cable compensation measurements for the current
            capacitance/inductance range, and returns short cable compensation
            **Resistance** and **Reactance** values. You can use the return values
            of this method as inputs to :py:meth:`nidmm.Session.configure_short_cable_comp_values`.

            This method returns an error if the value of the :py:attr:`nidmm.Session.method`
            property is not set to :py:data:`~nidmm.Method.CAPACITANCE` (1005) or
            :py:data:`~nidmm.Method.INDUCTANCE` (1006).

            



            :rtype: tuple (resistance, reactance)

                WHERE

                resistance (float): 


                    **resistance** is the measured value of short cable compensation
                    **resistance**.

                    


                reactance (float): 


                    **reactance** is the measured value of short cable compensation
                    **reactance**.

                    



read
----

    .. py:currentmodule:: nidmm.Session

    .. py:method:: read(maximum_time=datetime.timedelta(milliseconds=-1))

            Acquires a single measurement and returns the measured value.

            



            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: float in seconds or datetime.timedelta

            :rtype: float
            :return:


                    The measured value returned from the DMM.

                    



read_multi_point
----------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: read_multi_point(array_size, maximum_time=datetime.timedelta(milliseconds=-1))

            Acquires multiple measurements and returns an array of measured values.
            The number of measurements the DMM makes is determined by the values you
            specify for the **Trigger_Count** and **Sample_Count** parameters in
            :py:meth:`nidmm.Session.configure_multi_point`.

            



            :param array_size:


                Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in :py:meth:`nidmm.Session.configure_multi_point`.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

                


            :type array_size: int
            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: float in seconds or datetime.timedelta

            :rtype: tuple (reading_array, actual_number_of_points)

                WHERE

                reading_array (array.array("d")): 


                    An array of measurement values.

                    

                    .. note:: The size of the **Reading_Array** must be at least the size that you
                        specify for the **Array_Size** parameter.


                actual_number_of_points (int): 


                    Indicates the number of measured values actually retrieved from the DMM.

                    



read_status
-----------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: read_status()

            Returns measurement backlog and acquisition status. Use this method to
            determine how many measurements are available before calling
            :py:meth:`nidmm.Session.fetch`, :py:meth:`nidmm.Session.fetch_multi_point`, or :py:meth:`nidmm.Session.fetch_waveform`.

            

            .. note:: The NI 4050 is not supported.



            :rtype: tuple (acquisition_backlog, acquisition_status)

                WHERE

                acquisition_backlog (int): 


                    The number of measurements available to be read. If the backlog
                    continues to increase, data is eventually overwritten, resulting in an
                    error.

                    

                    .. note:: On the NI 4060, the **Backlog** does not increase when autoranging. On
                        the NI 4065, the **Backlog** does not increase when Range is set to AUTO
                        RANGE ON (-1), or before the first point is fetched when Range is set to
                        AUTO RANGE ONCE (-3). These behaviors are due to the autorange model of
                        the devices.


                acquisition_status (:py:data:`nidmm.AcquisitionStatus`): 


                    Indicates status of the acquisition. The following table shows the
                    acquisition states:

                    +---+----------------------------+
                    | 0 | Running                    |
                    +---+----------------------------+
                    | 1 | Finished with backlog      |
                    +---+----------------------------+
                    | 2 | Finished with no backlog   |
                    +---+----------------------------+
                    | 3 | Paused                     |
                    +---+----------------------------+
                    | 4 | No acquisition in progress |
                    +---+----------------------------+



read_waveform
-------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: read_waveform(array_size, maximum_time=datetime.timedelta(milliseconds=-1))

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
            and returns data as an array of values or as a waveform data type. The
            number of elements in the **Waveform_Array** is determined by the
            values you specify for the **Waveform_Points** parameter in
            :py:meth:`nidmm.Session.configure_waveform_acquisition`.

            



            :param array_size:


                Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of :py:meth:`nidmm.Session.configure_waveform_acquisition`. The default value is
                1.

                


            :type array_size: int
            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: float in seconds or datetime.timedelta

            :rtype: tuple (waveform_array, actual_number_of_points)

                WHERE

                waveform_array (array.array("d")): 


                    An array of measurement values.

                    

                    .. note:: The size of the **Waveform_Array** must be at least the size that you
                        specify for the **Array_Size** parameter.


                actual_number_of_points (int): 


                    Indicates the number of measured values actually retrieved from the DMM.

                    



reset
-----

    .. py:currentmodule:: nidmm.Session

    .. py:method:: reset()

            Resets the instrument to a known state and sends initialization commands
            to the instrument. The initialization commands set instrument settings
            to the state necessary for the operation of the instrument driver.

            



reset_with_defaults
-------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: reset_with_defaults()

            Resets the instrument to a known state and sends initialization commands
            to the DMM. The initialization commands set the DMM settings to the
            state necessary for the operation of NI-DMM. All user-defined default
            values associated with a logical name are applied after setting the DMM.

            



self_cal
--------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: self_cal()

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
            self-calibration routine to maintain measurement accuracy.

            

            .. note:: This method calls :py:meth:`nidmm.Session.reset`, and any configurations previous to
                the call will be lost. All properties will be set to their default
                values after the call returns.



self_test
---------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: self_test()

            Performs a self-test on the DMM to ensure that the DMM is functioning
            properly. Self-test does not calibrate the DMM. Zero
            indicates success.

            On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
            you should check the fuse and replace it, if necessary.

            Raises `SelfTestError` on self test failure. Properties on exception object:

            - code - failure code from driver
            - message - status message from driver

            

            .. note:: Self-test does not check the fuse on the NI 4065, NI 4071, and NI 4081. Hence, even if the fuse is blown on the device, self-test does not return error code 1013.

            .. note:: This method calls :py:meth:`nidmm.Session.reset`, and any configurations previous to the call will be lost. All properties will be set to their default values after the call returns.



send_software_trigger
---------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: send_software_trigger()

            Sends a command to trigger the DMM. Call this method if you have
            configured either the :py:attr:`nidmm.Session.trigger_source` or
            :py:attr:`nidmm.Session.sample_trigger` properties. If the
            :py:attr:`nidmm.Session.trigger_source` and/or :py:attr:`nidmm.Session.sample_trigger`
            properties are set to :py:data:`~nidmm.NIDMM_VAL_EXTERNAL` or :py:data:`~nidmm.NIDMM_VAL_TTL`\ *n*, you
            can use this method to override the trigger source that you configured
            and trigger the device. The NI 4050 and NI 4060 are not supported.

            

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



unlock
------

    .. py:currentmodule:: nidmm.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`nidmm.Session.lock`. Refer to :py:meth:`nidmm.Session.unlock` for additional
    information on session locks.





Properties
==========

ac_max_freq
-----------

    .. py:attribute:: ac_max_freq

        Specifies the maximum frequency component of the input signal for AC  measurements. This property is used only for error checking and verifies  that the value of this parameter is less than the maximum frequency  of the device. This property affects the DMM only when you set the   :py:attr:`nidmm.Session.method` property to AC measurements.
        The valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.

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

                - LabVIEW Property: **Configuration:Measurement Options:Max Frequency**
                - C Attribute: **NIDMM_ATTR_AC_MAX_FREQ**

ac_min_freq
-----------

    .. py:attribute:: ac_min_freq

        Specifies the minimum frequency component of the input signal for AC  measurements. This property affects the DMM only when you set the  :py:attr:`nidmm.Session.method` property to AC measurements.
        The valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.

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

                - LabVIEW Property: **Configuration:Measurement Options:Min Frequency**
                - C Attribute: **NIDMM_ATTR_AC_MIN_FREQ**

adc_calibration
---------------

    .. py:attribute:: adc_calibration

        For the NI 4070/4071/4072 only, specifies the ADC calibration mode.

        The following table lists the characteristics of this property.

            +----------------+----------------------+
            | Characteristic | Value                |
            +================+======================+
            | Datatype       | enums.ADCCalibration |
            +----------------+----------------------+
            | Permissions    | read-write           |
            +----------------+----------------------+
            | Channel Based  | No                   |
            +----------------+----------------------+
            | Resettable     | No                   |
            +----------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:ADC Calibration**
                - C Attribute: **NIDMM_ATTR_ADC_CALIBRATION**

aperture_time
-------------

    .. py:attribute:: aperture_time

        Specifies the measurement aperture time for the current configuration.  Aperture time is specified in units set by :py:attr:`nidmm.Session.aperture_time_units`. To  override the default aperture, set this property to the desired  aperture time after calling :py:meth:`nidmm.Session.ConfigureMeasurement`. To return to the  default, set this property to :py:data:`~nidmm.NIDMM_VAL_APERTURE_TIME_AUTO` (-1).
        On the NI 4070/4071/4072, the minimum aperture time is 8.89 usec,  and the maximum aperture time is 149 sec. Any number of powerline cycles (PLCs)  within the minimum and maximum ranges is allowed on the NI 4070/4071/4072.
        On the NI 4065 the minimum aperture time is 333 µs, and the maximum aperture time  is 78.2 s. If setting the number of averages directly, the total measurement time is  aperture time X the number of averages, which must be less than 72.8 s. The aperture  times allowed are 333 µs, 667 µs, or multiples of 1.11 ms-for example 1.11 ms, 2.22 ms,  3.33 ms, and so on. If you set an aperture time other than 333 µs, 667 µs, or multiples  of 1.11 ms, the value will be coerced up to the next supported aperture time.
        On the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed are  1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50 Hz, the  PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Advanced:Aperture Time**
                - C Attribute: **NIDMM_ATTR_APERTURE_TIME**

aperture_time_units
-------------------

    .. py:attribute:: aperture_time_units

        Specifies the units of aperture time for the current configuration.
        The NI 4060 does not support an aperture time set in seconds.

        The following table lists the characteristics of this property.

            +----------------+-------------------------+
            | Characteristic | Value                   |
            +================+=========================+
            | Datatype       | enums.ApertureTimeUnits |
            +----------------+-------------------------+
            | Permissions    | read-write              |
            +----------------+-------------------------+
            | Channel Based  | No                      |
            +----------------+-------------------------+
            | Resettable     | No                      |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Advanced:Aperture Time Units**
                - C Attribute: **NIDMM_ATTR_APERTURE_TIME_UNITS**

auto_range_value
----------------

    .. py:attribute:: auto_range_value

        Specifies the value of the range. If auto ranging, shows the actual value of  the active range. The value of this property is set during a read operation.

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

                - LabVIEW Property: **Configuration:Auto Range Value**
                - C Attribute: **NIDMM_ATTR_AUTO_RANGE_VALUE**

auto_zero
---------

    .. py:attribute:: auto_zero

        Specifies the AutoZero mode.
        The NI 4050 is not supported.

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.AutoZero |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+
            | Channel Based  | No             |
            +----------------+----------------+
            | Resettable     | No             |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Auto Zero**
                - C Attribute: **NIDMM_ATTR_AUTO_ZERO**

buffer_size
-----------

    .. py:attribute:: buffer_size

        Size in samples of the internal data buffer. Maximum is 134,217,727 (OX7FFFFFF) samples. When  set to :py:data:`~nidmm.NIDMM_VAL_BUFFER_SIZE_AUTO` (-1), NI-DMM chooses the buffer size.



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

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

                - LabVIEW Property: **Multi Point Acquisition:Advanced:Buffer Size**
                - C Attribute: **NIDMM_ATTR_BUFFER_SIZE**

cable_comp_type
---------------

    .. py:attribute:: cable_comp_type

        For the NI 4072 only,  the type of cable compensation that is applied to the current capacitance  or inductance measurement for the current range.
        Changing the method or the range through this property or through :py:meth:`nidmm.Session.configure_measurement_digits`  resets the value of this property to the default value.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------+
            | Characteristic | Value                       |
            +================+=============================+
            | Datatype       | enums.CableCompensationType |
            +----------------+-----------------------------+
            | Permissions    | read-write                  |
            +----------------+-----------------------------+
            | Channel Based  | No                          |
            +----------------+-----------------------------+
            | Resettable     | No                          |
            +----------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Cable Compensation Type**
                - C Attribute: **NIDMM_ATTR_CABLE_COMP_TYPE**

channel_count
-------------

    .. py:attribute:: channel_count

        Indicates the number of channels that the specific instrument driver  supports. For each property for which the IVI_VAL_MULTI_CHANNEL flag  property is set, the IVI engine maintains a separate cache value for each  channel.

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

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Capabilities:Channel Count**
                - C Attribute: **NIDMM_ATTR_CHANNEL_COUNT**

current_source
--------------

    .. py:attribute:: current_source

        Specifies the current source provided during diode measurements.
        The NI 4050 and NI 4060 are not supported.

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

                - LabVIEW Property: **Configuration:Measurement Options:Current Source**
                - C Attribute: **NIDMM_ATTR_CURRENT_SOURCE**

dc_bias
-------

    .. py:attribute:: dc_bias

        For the NI 4072 only, controls the available DC bias for capacitance measurements.

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

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Advanced:DC Bias**
                - C Attribute: **NIDMM_ATTR_DC_BIAS**

dc_noise_rejection
------------------

    .. py:attribute:: dc_noise_rejection

        Specifies the DC noise rejection mode.
        The NI 4050 and NI 4060 are not supported.

        The following table lists the characteristics of this property.

            +----------------+------------------------+
            | Characteristic | Value                  |
            +================+========================+
            | Datatype       | enums.DCNoiseRejection |
            +----------------+------------------------+
            | Permissions    | read-write             |
            +----------------+------------------------+
            | Channel Based  | No                     |
            +----------------+------------------------+
            | Resettable     | No                     |
            +----------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:DC Noise Rejection**
                - C Attribute: **NIDMM_ATTR_DC_NOISE_REJECTION**

driver_setup
------------

    .. py:attribute:: driver_setup

        This property indicates the Driver Setup string that the user specified when  initializing the driver.
        Some cases exist where the end-user must specify instrument driver options  at initialization time.  An example of this is specifying a particular  instrument model from among a family of instruments that the driver supports.   This is useful when using simulation.  The end-user can specify  driver-specific options through the DriverSetup keyword in the optionsString  parameter to the niDMM Init With Options.vi.
        If the user does not specify a Driver Setup string, this property returns  an empty string.

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

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Driver Setup**
                - C Attribute: **NIDMM_ATTR_DRIVER_SETUP**

freq_voltage_auto_range
-----------------------

    .. py:attribute:: freq_voltage_auto_range

        For the NI 4070/4071/4072 only, specifies the value of the frequency voltage range.  If Auto Ranging, shows the actual value of the active frequency voltage range.  If not Auto Ranging, the value of this property is the same as that of  :py:attr:`nidmm.Session.freq_voltage_range`.

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

                - LabVIEW Property: **Configuration:Measurement Options:Frequency Voltage Auto Range Value**
                - C Attribute: **NIDMM_ATTR_FREQ_VOLTAGE_AUTO_RANGE**

freq_voltage_range
------------------

    .. py:attribute:: freq_voltage_range

        Specifies the maximum amplitude of the input signal for frequency  measurements.

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

                - LabVIEW Property: **Configuration:Measurement Options:Frequency Voltage Range**
                - C Attribute: **NIDMM_ATTR_FREQ_VOLTAGE_RANGE**

function
--------

    .. py:attribute:: function

        Specifies the measurement method.
        Refer to the :py:attr:`nidmm.Session.method` topic in  the NI Digital Multimeters Help for device-specific information.
        If you are setting this property directly, you must also set the :py:attr:`nidmm.Session.operation_mode` property,  which controls whether the DMM takes standard single or multipoint measurements, or acquires a waveform.  If you are programming properties directly, you must set the :py:attr:`nidmm.Session.operation_mode` property before  setting other configuration properties. If the :py:attr:`nidmm.Session.operation_mode` property is set to :py:data:`~nidmm.OperationMode.WAVEFORM`,  the only valid method types are :py:data:`~nidmm.Method.WAVEFORM_VOLTAGE` and :py:data:`~nidmm.Method.WAVEFORM_CURRENT`. Set the  :py:attr:`nidmm.Session.operation_mode` property to :py:data:`~nidmm.OperationMode.IVIDMM` to set all other method values.

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.Function |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+
            | Channel Based  | No             |
            +----------------+----------------+
            | Resettable     | No             |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Function**
                - C Attribute: **NIDMM_ATTR_FUNCTION**

input_resistance
----------------

    .. py:attribute:: input_resistance

        Specifies the input resistance of the instrument.
        The NI 4050 and NI 4060 are not supported.

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

                - LabVIEW Property: **Configuration:Measurement Options:Input Resistance**
                - C Attribute: **NIDMM_ATTR_INPUT_RESISTANCE**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        A string containing the instrument firmware revision number.

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

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Firmware Revision**
                - C Attribute: **NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        A string containing the manufacturer of the instrument.

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

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Manufacturer**
                - C Attribute: **NIDMM_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        A string containing the instrument model.

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

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Model**
                - C Attribute: **NIDMM_ATTR_INSTRUMENT_MODEL**

instrument_product_id
---------------------

    .. py:attribute:: instrument_product_id

        The PCI product ID.

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

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Product ID**
                - C Attribute: **NIDMM_ATTR_INSTRUMENT_PRODUCT_ID**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        A string containing the resource descriptor of the instrument.

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

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:I/O Resource Descriptor**
                - C Attribute: **NIDMM_ATTR_IO_RESOURCE_DESCRIPTOR**

lc_calculation_model
--------------------

    .. py:attribute:: lc_calculation_model

        For the NI 4072 only, specifies the type of algorithm that the measurement processing uses for  capacitance and inductance measurements.

        The following table lists the characteristics of this property.

            +----------------+--------------------------+
            | Characteristic | Value                    |
            +================+==========================+
            | Datatype       | enums.LCCalculationModel |
            +----------------+--------------------------+
            | Permissions    | read-write               |
            +----------------+--------------------------+
            | Channel Based  | No                       |
            +----------------+--------------------------+
            | Resettable     | No                       |
            +----------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model**
                - C Attribute: **NIDMM_ATTR_LC_CALCULATION_MODEL**

lc_number_meas_to_average
-------------------------

    .. py:attribute:: lc_number_meas_to_average

        For the NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading.

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

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average**
                - C Attribute: **NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE**

logical_name
------------

    .. py:attribute:: logical_name

        A string containing the logical name of the instrument.

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

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NIDMM_ATTR_LOGICAL_NAME**

meas_complete_dest
------------------

    .. py:attribute:: meas_complete_dest

        Specifies the destination of the measurement complete (MC) signal.
        The NI 4050 is not supported.
        To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.

        The following table lists the characteristics of this property.

            +----------------+-------------------------------+
            | Characteristic | Value                         |
            +================+===============================+
            | Datatype       | enums.MeasurementCompleteDest |
            +----------------+-------------------------------+
            | Permissions    | read-write                    |
            +----------------+-------------------------------+
            | Channel Based  | No                            |
            +----------------+-------------------------------+
            | Resettable     | No                            |
            +----------------+-------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Trigger:Measurement Complete Dest**
                - C Attribute: **NIDMM_ATTR_MEAS_COMPLETE_DEST**

number_of_averages
------------------

    .. py:attribute:: number_of_averages

        Specifies the number of averages to perform in a measurement. For the NI 4070/4071/4072,  applies only when the aperture time is not set to AUTO and Auto Zero is ON.  The default is 1.
        The NI 4050 and NI 4060 are not supported.

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

                - LabVIEW Property: **Configuration:Advanced:Number Of Averages**
                - C Attribute: **NIDMM_ATTR_NUMBER_OF_AVERAGES**

offset_comp_ohms
----------------

    .. py:attribute:: offset_comp_ohms

        For the NI 4070/4071/4072 only, enables or disables offset compensated ohms.

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

                - LabVIEW Property: **Configuration:Measurement Options:Offset Compensated Ohms**
                - C Attribute: **NIDMM_ATTR_OFFSET_COMP_OHMS**

open_cable_comp_conductance
---------------------------

    .. py:attribute:: open_cable_comp_conductance

        For the NI 4072 only, specifies the active part (conductance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.
        Changing the method or the range through this property or through :py:meth:`nidmm.Session.configure_measurement_digits`  resets the value of this property to the default value.

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

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Conductance**
                - C Attribute: **NIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCE**

open_cable_comp_susceptance
---------------------------

    .. py:attribute:: open_cable_comp_susceptance

        For the NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.
        Changing the method or the range through this property or through :py:meth:`nidmm.Session.configure_measurement_digits`  resets the value of this property to the default value.

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

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Susceptance**
                - C Attribute: **NIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCE**

operation_mode
--------------

    .. py:attribute:: operation_mode

        Specifies how the NI 4065 and NI 4070/4071/4072 acquire data. When you call  :py:meth:`nidmm.Session.configure_measurement_digits`, NI-DMM sets this property to :py:data:`~nidmm.OperationMode.IVIDMM`.  When you call :py:meth:`nidmm.Session.configure_waveform_acquisition`, NI-DMM sets this property to :py:data:`~nidmm.OperationMode.WAVEFORM`.  If you are programming properties directly, you must set this property before  setting other configuration properties.

        The following table lists the characteristics of this property.

            +----------------+---------------------+
            | Characteristic | Value               |
            +================+=====================+
            | Datatype       | enums.OperationMode |
            +----------------+---------------------+
            | Permissions    | read-write          |
            +----------------+---------------------+
            | Channel Based  | No                  |
            +----------------+---------------------+
            | Resettable     | No                  |
            +----------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Advanced:Operation Mode**
                - C Attribute: **NIDMM_ATTR_OPERATION_MODE**

powerline_freq
--------------

    .. py:attribute:: powerline_freq

        Specifies the powerline frequency. The NI 4050 and NI 4060 use this value to select an aperture time to reject  powerline noise by selecting the appropriate internal sample clock and filter. The NI 4065 and  NI 4070/4071/4072 use this value to select a timebase for setting the :py:attr:`nidmm.Session.aperture_time`  property in powerline cycles (PLCs).
        After configuring powerline frequency, set the :py:attr:`nidmm.Session.aperture_time_units` property to PLCs.  When setting the :py:attr:`nidmm.Session.aperture_time` property, select the number of PLCs for the powerline frequency.  For example, if powerline frequency = 50 Hz (or 20ms) and aperture time in PLCs = 5, then aperture time in  Seconds = 20ms * 5 PLCs = 100 ms. Similarly, if powerline frequency = 60 Hz (or 16.667 ms) and aperture time  in PLCs = 6, then aperture time in Seconds = 16.667 ms * 6 PLCs = 100 ms.

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

                - LabVIEW Property: **Configuration:Measurement Options:Powerline Frequency**
                - C Attribute: **NIDMM_ATTR_POWERLINE_FREQ**

range
-----

    .. py:attribute:: range

        Specifies the measurement range. Use positive values to represent the  absolute value of the maximum expected measurement. The value is in units  appropriate for the current value of the :py:attr:`nidmm.Session.method` property. For  example, if :py:attr:`nidmm.Session.method` is set to :py:data:`~nidmm.NIDMM_VAL_VOLTS`, the units are  volts.
        The NI 4050 and NI 4060 only support Auto Range when the trigger and  sample trigger is set to IMMEDIATE.
        :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON` -1.0
        NI-DMM performs an Auto Range before acquiring the measurement.
        :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_OFF` -2.0
        NI-DMM sets the Range to the current :py:attr:`nidmm.Session.auto_range_value` and uses this range  for all subsequent measurements until the measurement configuration is changed.
        :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE` -3.0
        NI-DMM performs an Auto Range before acquiring the next measurement. The :py:attr:`nidmm.Session.auto_range_value`  is stored and used for all subsequent measurements until the measurement configuration is changed.



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
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Range**
                - C Attribute: **NIDMM_ATTR_RANGE**

resolution_absolute
-------------------

    .. py:attribute:: resolution_absolute

        Specifies the measurement resolution in absolute units. Setting this  property to higher values increases the measurement accuracy. Setting this  property to lower values increases the measurement speed.
        NI-DMM ignores this property for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the :py:attr:`nidmm.Session.lc_number_meas_to_average` property.

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

                - LabVIEW Property: **Configuration:Absolute Resolution**
                - C Attribute: **NIDMM_ATTR_RESOLUTION_ABSOLUTE**

resolution_digits
-----------------

    .. py:attribute:: resolution_digits

        Specifies the measurement resolution in digits. Setting this  property to higher values increases the measurement accuracy. Setting this  property to lower values increases the measurement speed.
        NI-DMM ignores this property for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the :py:attr:`nidmm.Session.lc_number_meas_to_average` property.

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

                - LabVIEW Property: **Configuration:Digits Resolution**
                - C Attribute: **NIDMM_ATTR_RESOLUTION_DIGITS**

sample_count
------------

    .. py:attribute:: sample_count

        Specifies the number of measurements the DMM takes each time it receives a  trigger in a multiple point acquisition.

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

                - LabVIEW Property: **Multi Point Acquisition:Sample Count**
                - C Attribute: **NIDMM_ATTR_SAMPLE_COUNT**

sample_interval
---------------

    .. py:attribute:: sample_interval

        Specifies the amount of time in seconds the DMM waits between measurement cycles.  This property only applies when the :py:attr:`nidmm.Session.sample_trigger` property is set to INTERVAL.
        On the NI 4060, the value for this property is used as the settling time.  When this property is set to 0, the NI 4060 does not settle between  measurement cycles. The onboard timing resolution is 1 µs on the NI 4060.
        The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional  delay. On the NI 4065 and NI 4070/4071/4072, the onboard timing resolution is 34.72 ns and  the valid range is 0-149 s.
        Only positive values are valid when setting the sample interval.
        The NI 4050 is not supported.

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
            | Resettable     | No                                     |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Multi Point Acquisition:Sample Interval**
                - C Attribute: **NIDMM_ATTR_SAMPLE_INTERVAL**

sample_trigger
--------------

    .. py:attribute:: sample_trigger

        Specifies the sample trigger source.
        To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.

        The following table lists the characteristics of this property.

            +----------------+---------------------+
            | Characteristic | Value               |
            +================+=====================+
            | Datatype       | enums.SampleTrigger |
            +----------------+---------------------+
            | Permissions    | read-write          |
            +----------------+---------------------+
            | Channel Based  | No                  |
            +----------------+---------------------+
            | Resettable     | No                  |
            +----------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Multi Point Acquisition:Sample Trigger**
                - C Attribute: **NIDMM_ATTR_SAMPLE_TRIGGER**

serial_number
-------------

    .. py:attribute:: serial_number

        A string containing the serial number of the instrument. This property corresponds  to the serial number label that is attached to most products.

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

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Serial Number**
                - C Attribute: **NIDMM_ATTR_SERIAL_NUMBER**

settle_time
-----------

    .. py:attribute:: settle_time

        Specifies the settling time in seconds. To override the default settling time,  set this property. To return to the default, set this property to  :py:data:`~nidmm.NIDMM_VAL_SETTLE_TIME_AUTO` (-1).
        The NI 4050 and NI 4060 are not supported.



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

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
            | Resettable     | No                                     |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Advanced:Settle Time**
                - C Attribute: **NIDMM_ATTR_SETTLE_TIME**

short_cable_comp_reactance
--------------------------

    .. py:attribute:: short_cable_comp_reactance

        For the NI 4072 only, represents the reactive part (reactance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.
        Changing the method or the range through this property or through :py:meth:`nidmm.Session.configure_measurement_digits`  resets the value of this property to the default value.

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

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Reactance**
                - C Attribute: **NIDMM_ATTR_SHORT_CABLE_COMP_REACTANCE**

short_cable_comp_resistance
---------------------------

    .. py:attribute:: short_cable_comp_resistance

        For the NI 4072 only, represents the active part (resistance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.
        Changing the method or the range through this property or through :py:meth:`nidmm.Session.configure_measurement_digits`  resets the value of this property to the default value.

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

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Resistance**
                - C Attribute: **NIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCE**

simulate
--------

    .. py:attribute:: simulate

        Specifies whether or not to simulate instrument driver I/O operations. If  simulation is enabled, instrument driver methods perform range checking and  call IVI Get and Set methods, but they do not perform  instrument I/O. For output parameters that represent instrument data, the  instrument driver methods return calculated values.
        The default value is False (0). Use the :py:meth:`nidmm.Session.__init__` method to  override this setting.
        Simulate can only be set within the InitWithOptions method.  The property value cannot be changed outside of the method.

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

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NIDMM_ATTR_SIMULATE**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        A string containing a description of the specific driver.

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

                - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Description**
                - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_major_version
-----------------------------

    .. py:attribute:: specific_driver_major_version

        Returns the major version number of this instrument driver.

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

                - LabVIEW Property: **Inherent IVI Attributes:Version Info:Specific Driver Major Version**
                - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION**

specific_driver_minor_version
-----------------------------

    .. py:attribute:: specific_driver_minor_version

        The minor version number of this instrument driver.

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

                - LabVIEW Property: **Inherent IVI Attributes:Version Info:Specific Driver Minor Version**
                - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_MINOR_VERSION**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        A string that contains additional version information about this specific  instrument driver.

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

                - LabVIEW Property: **Inherent IVI Attributes:Version Info:Specific Driver Revision**
                - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        A string containing the vendor of the specific driver.

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

                - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Vendor**
                - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_VENDOR**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        A string containing the instrument models supported by the specific driver.

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

                - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS**

temp_rtd_a
----------

    .. py:attribute:: temp_rtd_a

        Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property   is set to Custom. The default value is 3.9083e-3 (Pt3851).

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

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD A**
                - C Attribute: **NIDMM_ATTR_TEMP_RTD_A**

temp_rtd_b
----------

    .. py:attribute:: temp_rtd_b

        Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -5.775e-7(Pt3851).

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

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD B**
                - C Attribute: **NIDMM_ATTR_TEMP_RTD_B**

temp_rtd_c
----------

    .. py:attribute:: temp_rtd_c

        Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -4.183e-12(Pt3851).

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

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD C**
                - C Attribute: **NIDMM_ATTR_TEMP_RTD_C**

temp_rtd_res
------------

    .. py:attribute:: temp_rtd_res

        Specifies the RTD resistance at 0 degrees Celsius. This applies to all supported RTDs,  including custom RTDs. The default value is 100 (?).

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

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Resistance**
                - C Attribute: **NIDMM_ATTR_TEMP_RTD_RES**

temp_rtd_type
-------------

    .. py:attribute:: temp_rtd_type

        Specifies the type of RTD used to measure temperature. The default value is :py:data:`~nidmm.RTDType.PT3851`.
        Refer to the :py:attr:`nidmm.Session.temp_rtd_type` topic in the NI Digital Multimeters Help for additional information about defined values.

        The following table lists the characteristics of this property.

            +----------------+---------------+
            | Characteristic | Value         |
            +================+===============+
            | Datatype       | enums.RTDType |
            +----------------+---------------+
            | Permissions    | read-write    |
            +----------------+---------------+
            | Channel Based  | No            |
            +----------------+---------------+
            | Resettable     | No            |
            +----------------+---------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Type**
                - C Attribute: **NIDMM_ATTR_TEMP_RTD_TYPE**

temp_tc_fixed_ref_junc
----------------------

    .. py:attribute:: temp_tc_fixed_ref_junc

        Specifies the reference junction temperature when a fixed reference junction is used to take  a thermocouple measurement. The default value is 25.0 (°C).

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

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Fixed Reference Junction**
                - C Attribute: **NIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC**

temp_tc_ref_junc_type
---------------------

    .. py:attribute:: temp_tc_ref_junc_type

        Specifies the type of reference junction to be used in the reference junction compensation  of a thermocouple. The only supported value, :py:data:`~nidmm.NIDMM_VAL_TEMP_REF_JUNC_FIXED`, is fixed.



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------------------+
            | Characteristic | Value                                   |
            +================+=========================================+
            | Datatype       | enums.ThermocoupleReferenceJunctionType |
            +----------------+-----------------------------------------+
            | Permissions    | read-write                              |
            +----------------+-----------------------------------------+
            | Channel Based  | No                                      |
            +----------------+-----------------------------------------+
            | Resettable     | No                                      |
            +----------------+-----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Reference Junction Type**
                - C Attribute: **NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE**

temp_tc_type
------------

    .. py:attribute:: temp_tc_type

        Specifies the type of thermocouple used to measure the temperature. The default value is :py:data:`~nidmm.ThermocoupleType.J`.

        The following table lists the characteristics of this property.

            +----------------+------------------------+
            | Characteristic | Value                  |
            +================+========================+
            | Datatype       | enums.ThermocoupleType |
            +----------------+------------------------+
            | Permissions    | read-write             |
            +----------------+------------------------+
            | Channel Based  | No                     |
            +----------------+------------------------+
            | Resettable     | No                     |
            +----------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type**
                - C Attribute: **NIDMM_ATTR_TEMP_TC_TYPE**

temp_thermistor_a
-----------------

    .. py:attribute:: temp_thermistor_a

        Specifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 0.0010295 (44006).

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

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor A**
                - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_A**

temp_thermistor_b
-----------------

    .. py:attribute:: temp_thermistor_b

        Specifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type  proerty is set to Custom. The default value is 0.0002391 (44006).

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

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor B**
                - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_B**

temp_thermistor_c
-----------------

    .. py:attribute:: temp_thermistor_c

        Specifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 1.568e-7 (44006).

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

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor C**
                - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_C**

temp_thermistor_type
--------------------

    .. py:attribute:: temp_thermistor_type

        Specifies the type of thermistor used to measure the temperature. The default value is  :py:data:`~nidmm.ThermistorType.THERMISTOR_44006`.
        Refer to the :py:attr:`nidmm.Session.temp_thermistor_type` topic in the NI Digital Multimeters Help for additional information about defined values.

        The following table lists the characteristics of this property.

            +----------------+----------------------+
            | Characteristic | Value                |
            +================+======================+
            | Datatype       | enums.ThermistorType |
            +----------------+----------------------+
            | Permissions    | read-write           |
            +----------------+----------------------+
            | Channel Based  | No                   |
            +----------------+----------------------+
            | Resettable     | No                   |
            +----------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type**
                - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_TYPE**

temp_transducer_type
--------------------

    .. py:attribute:: temp_transducer_type

        Specifies the type of device used to measure the temperature. The default value is :py:data:`~nidmm.NIDMM_VAL_4_THERMOCOUPLE`.



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +----------------+----------------------+
            | Characteristic | Value                |
            +================+======================+
            | Datatype       | enums.TransducerType |
            +----------------+----------------------+
            | Permissions    | read-write           |
            +----------------+----------------------+
            | Channel Based  | No                   |
            +----------------+----------------------+
            | Resettable     | No                   |
            +----------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Transducer Type**
                - C Attribute: **NIDMM_ATTR_TEMP_TRANSDUCER_TYPE**

trigger_count
-------------

    .. py:attribute:: trigger_count

        Specifies the number of triggers the DMM receives before returning to the  Idle state.
        This property can be set to any positive ViInt32 value for the NI 4065 and NI 4070/4071/4072.
        The NI 4050 and NI 4060 support this property being set to 1.
        Refer to the Multiple Point Acquisitions section of the NI Digital Multimeters Help for more information.

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

                - LabVIEW Property: **Multi Point Acquisition:Trigger Count**
                - C Attribute: **NIDMM_ATTR_TRIGGER_COUNT**

trigger_delay
-------------

    .. py:attribute:: trigger_delay

        Specifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement.  The default value is AUTO DELAY (-1), which means that the DMM waits an appropriate settling time before taking  the measurement. (-1) signifies that AUTO DELAY is on, and (-2) signifies that AUTO DELAY is off.
        The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional settling time.  For the The NI 4065 and NI 4070/4071/4072, the valid range for Trigger Delay is AUTO DELAY (-1) or 0.0-149.0  seconds and the onboard timing resolution is 34.72 ns.
        On the NI 4060, if this property is set to 0, the DMM does not settle before taking the measurement.  On the NI 4060, the valid range for AUTO DELAY (-1) is 0.0-12.0 seconds and the onboard timing resolution  is 100 ms.
        When using the NI 4050, this property must be set to AUTO DELAY (-1).
        Use positive values to set the trigger delay in seconds.
        Valid Range: :py:data:`~nidmm.NIDMM_VAL_AUTO_DELAY` (-1.0), 0.0-12.0 seconds (NI 4060 only)
        Default Value: :py:data:`~nidmm.NIDMM_VAL_AUTO_DELAY`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

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
            | Resettable     | No                                     |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Trigger:Trigger Delay**
                - C Attribute: **NIDMM_ATTR_TRIGGER_DELAY**

trigger_source
--------------

    .. py:attribute:: trigger_source

        Specifies the trigger source. When :py:meth:`nidmm.Session._initiate` is called, the DMM waits  for the trigger specified with this property. After it receives the trigger,  the DMM waits the length of time specified with the :py:attr:`nidmm.Session.trigger_delay`  property. The DMM then takes a measurement.
        This property is not supported on the NI 4050.
        To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.

        The following table lists the characteristics of this property.

            +----------------+---------------------+
            | Characteristic | Value               |
            +================+=====================+
            | Datatype       | enums.TriggerSource |
            +----------------+---------------------+
            | Permissions    | read-write          |
            +----------------+---------------------+
            | Channel Based  | No                  |
            +----------------+---------------------+
            | Resettable     | No                  |
            +----------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Trigger:Trigger Source**
                - C Attribute: **NIDMM_ATTR_TRIGGER_SOURCE**

waveform_coupling
-----------------

    .. py:attribute:: waveform_coupling

        For the NI 4070/4071/4072 only, specifies the coupling during a waveform acquisition.

        The following table lists the characteristics of this property.

            +----------------+------------------------+
            | Characteristic | Value                  |
            +================+========================+
            | Datatype       | enums.WaveformCoupling |
            +----------------+------------------------+
            | Permissions    | read-write             |
            +----------------+------------------------+
            | Channel Based  | No                     |
            +----------------+------------------------+
            | Resettable     | No                     |
            +----------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Acquisition:Waveform Coupling**
                - C Attribute: **NIDMM_ATTR_WAVEFORM_COUPLING**

waveform_points
---------------

    .. py:attribute:: waveform_points

        For the NI 4070/4071/4072 only, specifies the number of points to acquire in a waveform acquisition.

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

                - LabVIEW Property: **Waveform Acquisition:Waveform Points**
                - C Attribute: **NIDMM_ATTR_WAVEFORM_POINTS**

waveform_rate
-------------

    .. py:attribute:: waveform_rate

        For the NI 4070/4071/4072 only, specifies the rate of the waveform acquisition in Samples per second (S/s).  The valid Range is 10.0-1,800,000 S/s. Values are coerced to the  closest integer divisor of 1,800,000. The default value is 1,800,000.

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

                - LabVIEW Property: **Waveform Acquisition:Waveform Rate**
                - C Attribute: **NIDMM_ATTR_WAVEFORM_RATE**


.. contents:: Session


