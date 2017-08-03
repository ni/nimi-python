functions_codegen_method = {
    'InitWithOptions':  { 'codegen_method': 'private',  },
    'Initiate':         { 'codegen_method': 'private',  },
    'close':            { 'codegen_method': 'private',  },
    'Abort':            { 'codegen_method': 'private',  },
    'CheckAttribute.+': { 'codegen_method': 'no',       },
    'SetAttribute.+':   { 'codegen_method': 'private',  },
    'GetAttribute.+':   { 'codegen_method': 'private',  },
    'init':             { 'codegen_method': 'no',       },
    'GetError':         { 'codegen_method': 'private',  },
    'GetErrorMessage':  { 'codegen_method': 'private',  },
    'ClearError':       { 'codegen_method': 'private',  },
    'Control':          { 'codegen_method': 'no',       },
    'LockSession':      { 'codegen_method': 'private',  },
    'UnlockSession':    { 'codegen_method': 'private',  },
    '.+ExtCal':         { 'codegen_method': 'no',       },
    'CalAdjust.+':      { 'codegen_method': 'no',       },
    '.+UserDefined.+':  { 'codegen_method': 'no',       },
    'SetCalPassword':   { 'codegen_method': 'no',       },
}

functions_enums = {
    'ConfigureTrigger':             { 'parameters': { 1: { 'enum': 'Terminal',                  }, }, },
    'ConfigureMeasCompleteDest':    { 'parameters': { 1: { 'enum': 'Terminal',                  }, }, },
    'ConfigureMultiPoint':          { 'parameters': { 3: { 'enum': 'Terminal',                  }, }, },
    'ConfigureTriggerSlope':        { 'parameters': { 1: { 'enum': 'Slope',                     }, }, },
    'GetApertureTimeInfo':          { 'parameters': { 2: { 'enum': 'ApertureTimeUnits',         }, }, },
    'ConfigureAutoZeroMode':        { 'parameters': { 1: { 'enum': 'EnabledSetting',            }, }, },
    'ConfigureMeasurementDigits':   { 'parameters': { 1: { 'enum': 'Function',                  }, }, },
    'ConfigureMeasurementAbsolute': { 'parameters': { 1: { 'enum': 'Function',                  }, }, },
    'ConfigureMeasCompleteSlope':   { 'parameters': { 1: { 'enum': 'Slope',                     }, }, },
    'ConfigureSampleTriggerSlope':  { 'parameters': { 1: { 'enum': 'Slope',                     }, }, },
    'ReadStatus':                   { 'parameters': { 2: { 'enum': 'AcquisitionStatus',         }, }, },
    'ConfigureADCCalibration':      { 'parameters': { 1: { 'enum': 'EnabledSetting',            }, }, },
    'ConfigureOffsetCompOhms':      { 'parameters': { 1: { 'enum': 'EnabledSetting',            }, }, },
    'ConfigureCurrentSource':       { 'parameters': { 1: { 'enum': 'CurrentSource',             }, }, },
    'ConfigureCableCompType':       { 'parameters': { 1: { 'enum': 'CableCompensationType',     }, }, },
    'ConfigureWaveformAcquisition': { 'parameters': { 1: { 'enum': 'Function',                  }, }, },
    'ConfigureWaveformCoupling':    { 'parameters': { 1: { 'enum': 'WaveformCouplingMode',      }, }, },
    'ConfigureTransducerType':      { 'parameters': { 1: { 'enum': 'TemperatureTransducerType', }, }, },
    'ConfigureThermistorType':      { 'parameters': { 1: { 'enum': 'TemperatureThermistorType', }, }, },

}

functions_params_types = {
    'GetAttributeViString':         { 'parameters': { 4: { 'type': 'ViString',                  }, }, },
    'SetAttributeViString':         { 'parameters': { 3: { 'type': 'ViString',                  }, }, },
}

