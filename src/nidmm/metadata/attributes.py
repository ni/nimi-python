# -*- coding: utf-8 -*-
# This file is generated from NI-DMM API metadata version 23.0.0d85
attributes = {
    1050005: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether or not to simulate instrument driver I/O operations. If  simulation is enabled, instrument driver functions perform range checking and  call IVI Get and Set functions, but they do not perform  instrument I/O. For output parameters that represent instrument data, the  instrument driver functions return calculated values.\nThe default value is VI_FALSE (0). Use the niDMM_InitWithOptions function to  override this setting.\nSimulate can only be set within the InitWithOptions function.  The attribute value cannot be changed outside of the function.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute indicates the Driver Setup string that the user specified when  initializing the driver.\nSome cases exist where the end-user must specify instrument driver options  at initialization time.  An example of this is specifying a particular  instrument model from among a family of instruments that the driver supports.   This is useful when using simulation.  The end-user can specify  driver-specific options through the DriverSetup keyword in the optionsString  parameter to the niDMM Init With Options.vi.\nIf the user does not specify a Driver Setup string, this attribute returns  an empty string.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Driver Setup',
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050203: {
        'access': 'read only',
        'documentation': {
            'description': 'Indicates the number of channels that the specific instrument driver  supports. For each attribute for which the IVI_VAL_MULTI_CHANNEL flag  attribute is set, the IVI engine maintains a separate cache value for each  channel.'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Capabilities:Channel Count',
        'name': 'CHANNEL_COUNT',
        'type': 'ViInt32'
    },
    1050304: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the resource descriptor of the instrument.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:I/O Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the logical name of the instrument.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the instrument models supported by the specific driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Specific Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050503: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the major version number of this instrument driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Version Info:Specific Driver Major Version',
        'name': 'SPECIFIC_DRIVER_MAJOR_VERSION',
        'type': 'ViInt32'
    },
    1050504: {
        'access': 'read only',
        'documentation': {
            'description': '\nThe minor version number of this instrument driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Version Info:Specific Driver Minor Version',
        'name': 'SPECIFIC_DRIVER_MINOR_VERSION',
        'type': 'ViInt32'
    },
    1050510: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the instrument firmware revision number.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Instrument Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the manufacturer of the instrument.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Instrument Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the instrument model.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Instrument Model',
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the vendor of the specific driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Specific Driver Identification:Specific Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing a description of the specific driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Specific Driver Identification:Specific Driver Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050551: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains additional version information about this specific  instrument driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Version Info:Specific Driver Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150014: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies how the NI 4065 and NI 4070/4071/4072 acquire data. When you call  niDMM_ConfigureMeasurementDigits, NI-DMM sets this attribute to NIDMM_VAL_IVIDMM_MODE.  When you call niDMM_ConfigureWaveformAcquisition, NI-DMM sets this attribute to NIDMM_VAL_WAVEFORM_MODE.  If you are programming attributes directly, you must set this attribute before  setting other configuration attributes.\n'
        },
        'enum': 'OperationMode',
        'lv_property': 'Configuration:Advanced:Operation Mode',
        'name': 'OPERATION_MODE',
        'type': 'ViInt32'
    },
    1150018: {
        'access': 'read-write',
        'documentation': {
            'description': 'For the NI 4070/4071/4072 only, specifies the rate of the waveform acquisition in Samples per second (S/s).  The valid Range is 10.0-1,800,000 S/s. Values are coerced to the  closest integer divisor of 1,800,000. The default value is 1,800,000.'
        },
        'lv_property': 'Waveform Acquisition:Waveform Rate',
        'name': 'WAVEFORM_RATE',
        'type': 'ViReal64'
    },
    1150019: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4070/4071/4072 only, specifies the number of points to acquire in a waveform acquisition.\n'
        },
        'lv_property': 'Waveform Acquisition:Waveform Points',
        'name': 'WAVEFORM_POINTS',
        'type': 'ViInt32'
    },
    1150022: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4070/4071/4072 only, specifies the ADC calibration mode.\n'
        },
        'enum': 'ADCCalibration',
        'lv_property': 'Configuration:Measurement Options:ADC Calibration',
        'name': 'ADC_CALIBRATION',
        'type': 'ViInt32'
    },
    1150023: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4070/4071/4072 only, enables or disables offset compensated ohms.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Offset Compensated Ohms',
        'name': 'OFFSET_COMP_OHMS',
        'type': 'ViInt32'
    },
    1150025: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the current source provided during diode measurements.\nThe NI 4050 and NI 4060 are not supported.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Current Source',
        'name': 'CURRENT_SOURCE',
        'type': 'ViReal64'
    },
    1150026: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the DC noise rejection mode.\nThe NI 4050 and NI 4060 are not supported.\n'
        },
        'enum': 'DCNoiseRejection',
        'lv_property': 'Configuration:Measurement Options:DC Noise Rejection',
        'name': 'DC_NOISE_REJECTION',
        'type': 'ViInt32'
    },
    1150027: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4070/4071/4072 only, specifies the coupling during a waveform acquisition.\n'
        },
        'enum': 'WaveformCoupling',
        'lv_property': 'Waveform Acquisition:Waveform Coupling',
        'name': 'WAVEFORM_COUPLING',
        'type': 'ViInt32'
    },
    1150028: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the settling time in seconds. To override the default settling time,  set this attribute. To return to the default, set this attribute to  NIDMM_VAL_SETTLE_TIME_AUTO (-1).\nThe NI 4050 and NI 4060 are not supported.\n'
        },
        'grpc_enum': 'SettleTime',
        'lv_property': 'Configuration:Advanced:Settle Time',
        'name': 'SETTLE_TIME',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150029: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the input resistance of the instrument.\nThe NI 4050 and NI 4060 are not supported.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Input Resistance',
        'name': 'INPUT_RESISTANCE',
        'type': 'ViReal64'
    },
    1150032: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the number of averages to perform in a measurement. For the NI 4070/4071/4072,  applies only when the aperture time is not set to AUTO and Auto Zero is ON.  The default is 1.\nThe NI 4050 and NI 4060 are not supported.\n'
        },
        'lv_property': 'Configuration:Advanced:Number Of Averages',
        'name': 'NUMBER_OF_AVERAGES',
        'type': 'ViInt32'
    },
    1150037: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSize in samples of the internal data buffer. Maximum is 134,217,727 (OX7FFFFFF) samples. When  set to NIDMM_VAL_BUFFER_SIZE_AUTO (-1), NI-DMM chooses the buffer size.\n'
        },
        'grpc_enum': 'BufferSize',
        'lv_property': 'Multi Point Acquisition:Advanced:Buffer Size',
        'name': 'BUFFER_SIZE',
        'type': 'ViInt32'
    },
    1150044: {
        'access': 'read only',
        'documentation': {
            'description': '\nFor the NI 4070/4071/4072 only, specifies the value of the frequency voltage range.  If Auto Ranging, shows the actual value of the active frequency voltage range.  If not Auto Ranging, the value of this attribute is the same as that of  NIDMM_ATTR_FREQ_VOLTAGE_RANGE.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Frequency Voltage Auto Range Value',
        'name': 'FREQ_VOLTAGE_AUTO_RANGE',
        'type': 'ViReal64'
    },
    1150045: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only,  the type of cable compensation that is applied to the current capacitance  or inductance measurement for the current range.\nChanging the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.\n'
        },
        'enum': 'CableCompensationType',
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Cable Compensation Type',
        'name': 'CABLE_COMP_TYPE',
        'type': 'ViInt32'
    },
    1150046: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, represents the reactive part (reactance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.\nChanging the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Reactance',
        'name': 'SHORT_CABLE_COMP_REACTANCE',
        'type': 'ViReal64'
    },
    1150047: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, represents the active part (resistance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.\nChanging the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Resistance',
        'name': 'SHORT_CABLE_COMP_RESISTANCE',
        'type': 'ViReal64'
    },
    1150048: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.\nChanging the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Susceptance',
        'name': 'OPEN_CABLE_COMP_SUSCEPTANCE',
        'type': 'ViReal64'
    },
    1150049: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, specifies the active part (conductance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.\nChanging the function or the range through this attribute or through niDMM_ConfigureMeasurementDigits  resets the value of this attribute to the default value.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Conductance',
        'name': 'OPEN_CABLE_COMP_CONDUCTANCE',
        'type': 'ViReal64'
    },
    1150052: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, specifies the type of algorithm that the measurement processing uses for  capacitance and inductance measurements.\n'
        },
        'enum': 'LCCalculationModel',
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model',
        'name': 'LC_CALCULATION_MODEL',
        'type': 'ViInt32'
    },
    1150053: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, controls the available DC bias for capacitance measurements.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Advanced:DC Bias',
        'name': 'DC_BIAS',
        'type': 'ViInt32'
    },
    1150054: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the serial number of the instrument. This attribute corresponds  to the serial number label that is attached to most products.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Instrument Serial Number',
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150055: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor the NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average',
        'name': 'LC_NUMBER_MEAS_TO_AVERAGE',
        'type': 'ViInt32'
    },
    1150061: {
        'access': 'read only',
        'documentation': {
            'description': 'The PCI product ID.'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Instrument Product ID',
        'name': 'INSTRUMENT_PRODUCT_ID',
        'type': 'ViInt32'
    },
    1150120: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of RTD used to measure temperature. The default value is NIDMM_VAL_TEMP_RTD_PT3851.\nRefer to the NIDMM_ATTR_TEMP_RTD_TYPE topic in the NI Digital Multimeters Help for additional information about defined values.\n'
        },
        'enum': 'RTDType',
        'lv_property': 'Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Type',
        'name': 'TEMP_RTD_TYPE',
        'type': 'ViInt32'
    },
    1150121: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property   is set to Custom. The default value is 3.9083e-3 (Pt3851).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD A',
        'name': 'TEMP_RTD_A',
        'type': 'ViReal64'
    },
    1150122: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Callendar-Van Dusen B coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -5.775e-7(Pt3851).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD B',
        'name': 'TEMP_RTD_B',
        'type': 'ViReal64'
    },
    1150123: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Callendar-Van Dusen C coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -4.183e-12(Pt3851).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD C',
        'name': 'TEMP_RTD_C',
        'type': 'ViReal64'
    },
    1150124: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of thermistor used to measure the temperature. The default value is  NIDMM_VAL_TEMP_THERMISTOR_44006.\nRefer to the NIDMM_ATTR_TEMP_THERMISTOR_TYPE topic in the NI Digital Multimeters Help for additional information about defined values.\n'
        },
        'enum': 'ThermistorType',
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type',
        'name': 'TEMP_THERMISTOR_TYPE',
        'type': 'ViInt32'
    },
    1150125: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 0.0010295 (44006).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermistor:Thermistor A',
        'name': 'TEMP_THERMISTOR_A',
        'type': 'ViReal64'
    },
    1150126: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type  proerty is set to Custom. The default value is 0.0002391 (44006).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermistor:Thermistor B',
        'name': 'TEMP_THERMISTOR_B',
        'type': 'ViReal64'
    },
    1150127: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 1.568e-7 (44006).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermistor:Thermistor C',
        'name': 'TEMP_THERMISTOR_C',
        'type': 'ViReal64'
    },
    1250001: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement function.\nRefer to the NIDMM_ATTR_FUNCTION topic in  the NI Digital Multimeters Help for device-specific information.\nIf you are setting this attribute directly, you must also set the NIDMM_ATTR_OPERATION_MODE attribute,  which controls whether the DMM takes standard single or multipoint measurements, or acquires a waveform.  If you are programming attributes directly, you must set the NIDMM_ATTR_OPERATION_MODE attribute before  setting other configuration attributes. If the NIDMM_ATTR_OPERATION_MODE attribute is set to NIDMM_VAL_WAVEFORM_MODE,  the only valid function types are NIDMM_VAL_WAVEFORM_VOLTAGE and NIDMM_VAL_WAVEFORM_CURRENT. Set the  NIDMM_ATTR_OPERATION_MODE attribute to NIDMM_VAL_IVIDMM_MODE to set all other function values.\n'
        },
        'enum': 'Function',
        'lv_property': 'Configuration:Function',
        'name': 'FUNCTION',
        'type': 'ViInt32'
    },
    1250002: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement range. Use positive values to represent the  absolute value of the maximum expected measurement. The value is in units  appropriate for the current value of the NIDMM_ATTR_FUNCTION attribute. For  example, if NIDMM_ATTR_FUNCTION is set to NIDMM_VAL_VOLTS, the units are  volts.\nThe NI 4050 and NI 4060 only support Auto Range when the trigger and  sample trigger is set to IMMEDIATE.\nNIDMM_VAL_AUTO_RANGE_ON -1.0\nNI-DMM performs an Auto Range before acquiring the measurement.\nNIDMM_VAL_AUTO_RANGE_OFF -2.0\nNI-DMM sets the Range to the current NIDMM_ATTR_AUTO_RANGE_VALUE and uses this range  for all subsequent measurements until the measurement configuration is changed.\nNIDMM_VAL_AUTO_RANGE_ONCE -3.0\nNI-DMM performs an Auto Range before acquiring the next measurement. The NIDMM_ATTR_AUTO_RANGE_VALUE  is stored and used for all subsequent measurements until the measurement configuration is changed.\n'
        },
        'grpc_enum': 'Range',
        'lv_property': 'Configuration:Range',
        'name': 'RANGE',
        'type': 'ViReal64'
    },
    1250003: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement resolution in digits. Setting this  attribute to higher values increases the measurement accuracy. Setting this  attribute to lower values increases the measurement speed.\nNI-DMM ignores this attribute for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE attribute.\n'
        },
        'lv_property': 'Configuration:Digits Resolution',
        'name': 'RESOLUTION_DIGITS',
        'type': 'ViReal64'
    },
    1250004: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the trigger source. When niDMM_Initiate is called, the DMM waits  for the trigger specified with this attribute. After it receives the trigger,  the DMM waits the length of time specified with the NIDMM_ATTR_TRIGGER_DELAY  attribute. The DMM then takes a measurement.\nThis attribute is not supported on the NI 4050.\nTo determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.\n'
        },
        'enum': 'TriggerSource',
        'lv_property': 'Trigger:Trigger Source',
        'name': 'TRIGGER_SOURCE',
        'type': 'ViInt32'
    },
    1250005: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement.  The default value is AUTO DELAY (-1), which means that the DMM waits an appropriate settling time before taking  the measurement. (-1) signifies that AUTO DELAY is on, and (-2) signifies that AUTO DELAY is off.\nThe NI 4065 and NI 4070/4071/4072 use the value specified in this attribute as additional settling time.  For the The NI 4065 and NI 4070/4071/4072, the valid range for Trigger Delay is AUTO DELAY (-1) or 0.0-149.0  seconds and the onboard timing resolution is 34.72 ns.\nOn the NI 4060, if this attribute is set to 0, the DMM does not settle before taking the measurement.  On the NI 4060, the valid range for AUTO DELAY (-1) is 0.0-12.0 seconds and the onboard timing resolution  is 100 ms.\nWhen using the NI 4050, this attribute must be set to AUTO DELAY (-1).\nUse positive values to set the trigger delay in seconds.\nValid Range: NIDMM_VAL_AUTO_DELAY (-1.0), 0.0-12.0 seconds (NI 4060 only)\nDefault Value: NIDMM_VAL_AUTO_DELAY\n'
        },
        'grpc_enum': 'TriggerDelays',
        'lv_property': 'Trigger:Trigger Delay',
        'name': 'TRIGGER_DELAY',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250006: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the minimum frequency component of the input signal for AC  measurements. This attribute affects the DMM only when you set the  NIDMM_ATTR_FUNCTION attribute to AC measurements.\nThe valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Min Frequency',
        'name': 'AC_MIN_FREQ',
        'type': 'ViReal64'
    },
    1250007: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum frequency component of the input signal for AC  measurements. This attribute is used only for error checking and verifies  that the value of this parameter is less than the maximum frequency  of the device. This attribute affects the DMM only when you set the   NIDMM_ATTR_FUNCTION attribute to AC measurements.\nThe valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Max Frequency',
        'name': 'AC_MAX_FREQ',
        'type': 'ViReal64'
    },
    1250008: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement resolution in absolute units. Setting this  attribute to higher values increases the measurement accuracy. Setting this  attribute to lower values increases the measurement speed.\nNI-DMM ignores this attribute for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE attribute.\n'
        },
        'lv_property': 'Configuration:Absolute Resolution',
        'name': 'RESOLUTION_ABSOLUTE',
        'type': 'ViReal64'
    },
    1250101: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum amplitude of the input signal for frequency  measurements.\n'
        },
        'grpc_enum': 'FrequencyVoltageRange',
        'lv_property': 'Configuration:Measurement Options:Frequency Voltage Range',
        'name': 'FREQ_VOLTAGE_RANGE',
        'type': 'ViReal64'
    },
    1250201: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of device used to measure the temperature. The default value is NIDMM_VAL_4_THERMOCOUPLE.\n'
        },
        'enum': 'TransducerType',
        'lv_property': 'Configuration:Measurement Options:Temperature:Transducer Type',
        'name': 'TEMP_TRANSDUCER_TYPE',
        'type': 'ViInt32'
    },
    1250231: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of thermocouple used to measure the temperature. The default value is NIDMM_VAL_TEMP_TC_J.\n'
        },
        'enum': 'ThermocoupleType',
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type',
        'name': 'TEMP_TC_TYPE',
        'type': 'ViInt32'
    },
    1250232: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of reference junction to be used in the reference junction compensation  of a thermocouple. The only supported value, NIDMM_VAL_TEMP_REF_JUNC_FIXED, is fixed.\n'
        },
        'enum': 'ThermocoupleReferenceJunctionType',
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermocouple:Reference Junction Type',
        'name': 'TEMP_TC_REF_JUNC_TYPE',
        'type': 'ViInt32'
    },
    1250233: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the reference junction temperature when a fixed reference junction is used to take  a thermocouple measurement. The default value is 25.0 (°C).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Thermocouple:Fixed Reference Junction',
        'name': 'TEMP_TC_FIXED_REF_JUNC',
        'type': 'ViReal64'
    },
    1250242: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the RTD resistance at 0 degrees Celsius. This applies to all supported RTDs,  including custom RTDs. The default value is 100 (?).\n'
        },
        'lv_property': 'Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Resistance',
        'name': 'TEMP_RTD_RES',
        'type': 'ViReal64'
    },
    1250301: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the number of measurements the DMM takes each time it receives a  trigger in a multiple point acquisition.\n'
        },
        'grpc_enum': 'SampleCount',
        'lv_property': 'Multi Point Acquisition:Sample Count',
        'name': 'SAMPLE_COUNT',
        'type': 'ViInt32'
    },
    1250302: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the sample trigger source.\nTo determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.\n'
        },
        'enum': 'SampleTrigger',
        'lv_property': 'Multi Point Acquisition:Sample Trigger',
        'name': 'SAMPLE_TRIGGER',
        'type': 'ViInt32'
    },
    1250303: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the amount of time in seconds the DMM waits between measurement cycles.  This attribute only applies when the NIDMM_ATTR_SAMPLE_TRIGGER attribute is set to INTERVAL.\nOn the NI 4060, the value for this attribute is used as the settling time.  When this attribute is set to 0, the NI 4060 does not settle between  measurement cycles. The onboard timing resolution is 1 µs on the NI 4060.\nThe NI 4065 and NI 4070/4071/4072 use the value specified in this attribute as additional  delay. On the NI 4065 and NI 4070/4071/4072, the onboard timing resolution is 34.72 ns and  the valid range is 0-149 s.\nOnly positive values are valid when setting the sample interval.\nThe NI 4050 is not supported.\n'
        },
        'grpc_enum': 'SampleInterval',
        'lv_property': 'Multi Point Acquisition:Sample Interval',
        'name': 'SAMPLE_INTERVAL',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250304: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the number of triggers the DMM receives before returning to the  Idle state.\nThis attribute can be set to any positive ViInt32 value for the NI 4065 and NI 4070/4071/4072.\nThe NI 4050 and NI 4060 support this attribute being set to 1.\nRefer to the Multiple Point Acquisitions section of the NI Digital Multimeters Help for more information.\n'
        },
        'grpc_enum': 'TriggerCount',
        'lv_property': 'Multi Point Acquisition:Trigger Count',
        'name': 'TRIGGER_COUNT',
        'type': 'ViInt32'
    },
    1250305: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the destination of the measurement complete (MC) signal.\nThe NI 4050 is not supported.\nTo determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.\n'
        },
        'enum': 'MeasurementCompleteDest',
        'lv_property': 'Trigger:Measurement Complete Dest',
        'name': 'MEAS_COMPLETE_DEST',
        'type': 'ViInt32'
    },
    1250321: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement aperture time for the current configuration.  Aperture time is specified in units set by NIDMM_ATTR_APERTURE_TIME_UNITS. To  override the default aperture, set this attribute to the desired  aperture time after calling niDMM_ConfigureMeasurement. To return to the  default, set this attribute to NIDMM_VAL_APERTURE_TIME_AUTO (-1).\nOn the NI 4070/4071/4072, the minimum aperture time is 8.89 usec,  and the maximum aperture time is 149 sec. Any number of powerline cycles (PLCs)  within the minimum and maximum ranges is allowed on the NI 4070/4071/4072.\nOn the NI 4065 the minimum aperture time is 333 µs, and the maximum aperture time  is 78.2 s. If setting the number of averages directly, the total measurement time is  aperture time X the number of averages, which must be less than 72.8 s. The aperture  times allowed are 333 µs, 667 µs, or multiples of 1.11 ms-for example 1.11 ms, 2.22 ms,  3.33 ms, and so on. If you set an aperture time other than 333 µs, 667 µs, or multiples  of 1.11 ms, the value will be coerced up to the next supported aperture time.\nOn the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed are  1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50 Hz, the  PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.\n'
        },
        'grpc_enum': 'ApertureTime',
        'lv_property': 'Configuration:Advanced:Aperture Time',
        'name': 'APERTURE_TIME',
        'type': 'ViReal64'
    },
    1250322: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the units of aperture time for the current configuration.\nThe NI 4060 does not support an aperture time set in seconds.\n'
        },
        'enum': 'ApertureTimeUnits',
        'lv_property': 'Configuration:Advanced:Aperture Time Units',
        'name': 'APERTURE_TIME_UNITS',
        'type': 'ViInt32'
    },
    1250331: {
        'access': 'read only',
        'documentation': {
            'description': '\nSpecifies the value of the range. If auto ranging, shows the actual value of  the active range. The value of this attribute is set during a read operation.\n'
        },
        'lv_property': 'Configuration:Auto Range Value',
        'name': 'AUTO_RANGE_VALUE',
        'type': 'ViReal64'
    },
    1250332: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the AutoZero mode.\nThe NI 4050 is not supported.\n'
        },
        'enum': 'AutoZero',
        'lv_property': 'Configuration:Measurement Options:Auto Zero',
        'name': 'AUTO_ZERO',
        'type': 'ViInt32'
    },
    1250333: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the powerline frequency. The NI 4050 and NI 4060 use this value to select an aperture time to reject  powerline noise by selecting the appropriate internal sample clock and filter. The NI 4065 and  NI 4070/4071/4072 use this value to select a timebase for setting the NIDMM_ATTR_APERTURE_TIME  attribute in powerline cycles (PLCs).\nAfter configuring powerline frequency, set the NIDMM_ATTR_APERTURE_TIME_UNITS attribute to PLCs.  When setting the NIDMM_ATTR_APERTURE_TIME attribute, select the number of PLCs for the powerline frequency.  For example, if powerline frequency = 50 Hz (or 20ms) and aperture time in PLCs = 5, then aperture time in  Seconds = 20ms * 5 PLCs = 100 ms. Similarly, if powerline frequency = 60 Hz (or 16.667 ms) and aperture time  in PLCs = 6, then aperture time in Seconds = 16.667 ms * 6 PLCs = 100 ms.\n'
        },
        'lv_property': 'Configuration:Measurement Options:Powerline Frequency',
        'name': 'POWERLINE_FREQ',
        'type': 'ViReal64'
    }
}
