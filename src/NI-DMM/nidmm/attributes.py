class AttributeInfo:
    '''Information about NI-DMM attributes'''
    data = {
       'RANGE_CHECK'                                : {'id':1050002, 'type':'bool'       ,      'enum':None                                              ,   'access':'read-write'     },
       'QUERY_INSTRUMENT_STATUS'                    : {'id':1050003, 'type':'bool'       ,      'enum':None                                              ,   'access':'read-write'     },
       'CACHE'                                      : {'id':1050004, 'type':'bool'       ,      'enum':None                                              ,   'access':'read-write'     },
       'SIMULATE'                                   : {'id':1050005, 'type':'bool'       ,      'enum':None                                              ,   'access':'read-write'     },
       'RECORD_COERCIONS'                           : {'id':1050006, 'type':'bool'       ,      'enum':None                                              ,   'access':'read-write'     },
       'INTERCHANGE_CHECK'                          : {'id':1050021, 'type':'bool'       ,      'enum':None                                              ,   'access':'read-write'     },
       'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION'   : {'id':1050515, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read only'      },
       'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION'   : {'id':1050516, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read only'      },
       'SPECIFIC_DRIVER_DESCRIPTION'                : {'id':1050514, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'SPECIFIC_DRIVER_PREFIX'                     : {'id':1050302, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'SPECIFIC_DRIVER_VENDOR'                     : {'id':1050513, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'SPECIFIC_DRIVER_REVISION'                   : {'id':1050551, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION'      : {'id':1050519, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read only'      },
       'CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION'      : {'id':1050520, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read only'      },
       'CHANNEL_COUNT'                              : {'id':1050203, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read only'      },
       'SUPPORTED_INSTRUMENT_MODELS'                : {'id':1050327, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'GROUP_CAPABILITIES'                         : {'id':1050401, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'INSTRUMENT_MANUFACTURER'                    : {'id':1050511, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'INSTRUMENT_MODEL'                           : {'id':1050512, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'INSTRUMENT_FIRMWARE_REVISION'               : {'id':1050510, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'LOGICAL_NAME'                               : {'id':1050305, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'IO_RESOURCE_DESCRIPTOR'                     : {'id':1050304, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'DRIVER_SETUP'                               : {'id':1050007, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'IO_SESSION'                                 : {'id':1050322, 'type':'N/A'        ,      'enum':None                                              ,   'access':'read only'      },
       'FUNCTION'                                   : {'id':1250001, 'type':'int32_t'    ,      'enum':'Function'                                        ,   'access':'read-write'     },
       'RANGE'                                      : {'id':1250002, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'RESOLUTION_ABSOLUTE'                        : {'id':1250008, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'RESOLUTION_DIGITS'                          : {'id':1250003, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'TRIGGER_DELAY'                              : {'id':1250005, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'TRIGGER_SOURCE'                             : {'id':1250004, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read-write'     },
       'AC_MAX_FREQ'                                : {'id':1250007, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'AC_MIN_FREQ'                                : {'id':1250006, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'FREQ_VOLTAGE_RANGE'                         : {'id':1250101, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'MEAS_COMPLETE_DEST'                         : {'id':1250305, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read-write'     },
       'SAMPLE_COUNT'                               : {'id':1250301, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read-write'     },
       'SAMPLE_INTERVAL'                            : {'id':1250303, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'SAMPLE_TRIGGER'                             : {'id':1250302, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read-write'     },
       'TRIGGER_COUNT'                              : {'id':1250304, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read-write'     },
       'APERTURE_TIME'                              : {'id':1250321, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'APERTURE_TIME_UNITS'                        : {'id':1250322, 'type':'int32_t'    ,      'enum':'ApertureTimeUnit'                                ,   'access':'read-write'     },
       'AUTO_RANGE_VALUE'                           : {'id':1250331, 'type':'double'     ,      'enum':None                                              ,   'access':'read only'      },
       'AUTO_ZERO'                                  : {'id':1250332, 'type':'int32_t'    ,      'enum':'EnabledSetting'                                  ,   'access':'read-write'     },
       'POWERLINE_FREQ'                             : {'id':1250333, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'TRIGGER_SLOPE'                              : {'id':1250334, 'type':'int32_t'    ,      'enum':'Slope'                                           ,   'access':'read-write'     },
       'SAMPLE_TRIGGER_SLOPE'                       : {'id':1150010, 'type':'int32_t'    ,      'enum':'Slope'                                           ,   'access':'read-write'     },
       'MEAS_DEST_SLOPE'                            : {'id':1150002, 'type':'int32_t'    ,      'enum':'Slope'                                           ,   'access':'read-write'     },
       'ADC_CALIBRATION'                            : {'id':1150022, 'type':'int32_t'    ,      'enum':'EnabledSetting'                                  ,   'access':'read-write'     },
       'OFFSET_COMP_OHMS'                           : {'id':1150023, 'type':'int32_t'    ,      'enum':'EnabledSetting'                                  ,   'access':'read-write'     },
       'NUMBER_OF_AVERAGES'                         : {'id':1150032, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read-write'     },
       'CURRENT_SOURCE'                             : {'id':1150025, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'DC_NOISE_REJECTION'                         : {'id':1150026, 'type':'int32_t'    ,      'enum':'DCNoiseRejectionMode'                            ,   'access':'read-write'     },
       'SETTLE_TIME'                                : {'id':1150028, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'INPUT_RESISTANCE'                           : {'id':1150029, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'LATENCY'                                    : {'id':1150034, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read-write'     },
       'BUFFER_SIZE'                                : {'id':1150037, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read-write'     },
       'SHUNT_VALUE'                                : {'id':1150003, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'OPERATION_MODE'                             : {'id':1150014, 'type':'int32_t'    ,      'enum':'OperationMode'                                   ,   'access':'read-write'     },
       'WAVEFORM_RATE'                              : {'id':1150018, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'WAVEFORM_POINTS'                            : {'id':1150019, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read-write'     },
       'WAVEFORM_COUPLING'                          : {'id':1150027, 'type':'int32_t'    ,      'enum':'WaveformCouplingMode'                            ,   'access':'read-write'     },
       'FREQ_VOLTAGE_AUTO_RANGE_VALUE'              : {'id':1150044, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'CABLE_COMP_TYPE'                            : {'id':1150045, 'type':'int32_t'    ,      'enum':'CableCompensationType'                           ,   'access':'read-write'     },
       'SHORT_CABLE_COMP_REACTANCE'                 : {'id':1150046, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'SHORT_CABLE_COMP_RESISTANCE'                : {'id':1150047, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'OPEN_CABLE_COMP_SUSCEPTANCE'                : {'id':1150048, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'OPEN_CABLE_COMP_CONDUCTANCE'                : {'id':1150049, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'LC_CALCULATION_MODEL'                       : {'id':1150052, 'type':'int32_t'    ,      'enum':'LCCalculationModel'                              ,   'access':'read-write'     },
       'DC_BIAS'                                    : {'id':1150053, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read-write'     },
       'LC_NUMBER_MEAS_TO_AVERAGE'                  : {'id':1150055, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read-write'     },
       'SERIAL_NUMBER'                              : {'id':1150054, 'type':'std::string',      'enum':None                                              ,   'access':'read only'      },
       'CONFIG_PRODUCT_NUMBER'                      : {'id':1150061, 'type':'int32_t'    ,      'enum':None                                              ,   'access':'read only'      },
       'TEMP_TRANSDUCER_TYPE'                       : {'id':1250201, 'type':'int32_t'    ,      'enum':'TemperatureTransducerType'                       ,   'access':'read-write'     },
       'TEMP_TC_REF_JUNC_TYPE'                      : {'id':1250232, 'type':'int32_t'    ,      'enum':'TemperatureThermocoupleReferenceJunctionType'    ,   'access':'read-write'     },
       'TEMP_TC_TYPE'                               : {'id':1250231, 'type':'int32_t'    ,      'enum':'TemperatureThermocoupleType'                     ,   'access':'read-write'     },
       'TEMP_TC_FIXED_REF_JUNC'                     : {'id':1250233, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'TEMP_RTD_TYPE'                              : {'id':1150120, 'type':'int32_t'    ,      'enum':'TemperatureRTDType'                              ,   'access':'read-write'     },
       'TEMP_RTD_RES'                               : {'id':1250242, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'TEMP_RTD_A'                                 : {'id':1150121, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'TEMP_RTD_B'                                 : {'id':1150122, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'TEMP_RTD_C'                                 : {'id':1150123, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'TEMP_THERMISTOR_TYPE'                       : {'id':1150124, 'type':'int32_t'    ,      'enum':'TemperatureThermistorType'                       ,   'access':'read-write'     },
       'TEMP_THERMISTOR_A'                          : {'id':1150125, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'TEMP_THERMISTOR_B'                          : {'id':1150126, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     },
       'TEMP_THERMISTOR_C'                          : {'id':1150127, 'type':'double'     ,      'enum':None                                              ,   'access':'read-write'     }
    }

    def getInfo(self, name):
        info = data[name]
        if info is None:
            raise Exception("Attribute " + name + " not found")
        else:
            return info

    def getID(self, name):
        return self.getInfo(name)['id']

    def getType(self, name):
        return {
            'bool': c_ushort,
            'int32_t': c_long,
            'std::string': c_char_p,
            'double': c_double
        }[self.getInfo(name)['type']]


