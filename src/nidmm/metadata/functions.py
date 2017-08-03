<<<<<<< HEAD
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here
#  If the generated information is not correct for python
#  changes can be made in functions_addon.py and they will be 
#  applied at build time
=======
functions = [   {   'name': 'init',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'resourceName',
                                       'is_buffer': True,
                                       'type': 'ViRsrc'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'IDQuery',
                                       'type': 'ViBoolean'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'reset', 'type': 'ViBoolean'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'newVi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'InitWithOptions',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'resourceName',
                                       'is_buffer': True,
                                       'type': 'ViRsrc'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'IDQuery',
                                       'type': 'ViBoolean'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'resetDevice',
                                       'type': 'ViBoolean'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'optionsString',
                                       'is_buffer': True,
                                       'type': 'ViString'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'newVi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'close',
                    'codegen_method': 'private',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetError',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'errorCode',
                                       'type': 'ViStatus'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'bufferSize',
                                       'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'description',
                                       'is_buffer': True,
                                       'type': 'ViChar'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetErrorMessage',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'errorCode',
                                       'type': 'ViStatus'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'bufferSize',
                                       'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'errMessage',
                                       'is_buffer': True,
                                       'type': 'ViChar'}],
                    'returns': 'ViStatus'},
                {   'name': 'ClearError',
                    'codegen_method': 'private',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'reset',
                    'codegen_method': 'public',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'self_test',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'selfTestResult',
                                       'type': 'ViInt16'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'selfTestMessage',
                                       'is_buffer': True,
                                       'type': 'ViChar'}],
                    'returns': 'ViStatus'},
                {   'name': 'SelfCal',
                    'codegen_method': 'public',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'revision_query',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'driverRev',
                                       'is_buffer': True,
                                       'type': 'ViChar'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'instrRev',
                                       'is_buffer': True,
                                       'type': 'ViChar'}],
                    'returns': 'ViStatus'},
                {   'name': 'InvalidateAllAttributes',
                    'codegen_method': 'public',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'ResetWithDefaults',
                    'codegen_method': 'public',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'Disable',
                    'codegen_method': 'public',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetMeasurementPeriod',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'period', 'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureTrigger',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'TriggerSource',
                                       'name': 'trigSource',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'triggerDelay',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'Read',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'maxTime', 'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'reading',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'Fetch',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'maxTime', 'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'reading',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'Abort',
                    'codegen_method': 'private',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'Initiate',
                    'codegen_method': 'private',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'IsOverRange',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'measurementValue',
                                       'type': 'ViReal64'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'isOverRange',
                                       'type': 'ViBoolean'}],
                    'returns': 'ViStatus'},
                {   'name': 'IsUnderRange',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'measurementValue',
                                       'type': 'ViReal64'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'isUnderRange',
                                       'type': 'ViBoolean'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureACBandwidth',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'minFreq', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'maxFreq',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureFrequencyVoltageRange',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'frequencyVoltageRange',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureMeasCompleteDest',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'MeasurementCompleteDest',
                                       'name': 'destination',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureMultiPoint',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'triggerCount',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'sampleCount',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': 'SampleTrigger',
                                       'name': 'sampleTrigger',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'sampleInterval',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ReadMultiPoint',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'maxTime', 'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'arraySize',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'readingArray',
                                       'type': 'ViReal64'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'actualPts',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'FetchMultiPoint',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'maxTime', 'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'arraySize',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'readingArray',
                                       'type': 'ViReal64'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'actualPts',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureTriggerSlope',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'Slope',
                                       'name': 'polarity',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'SendSoftwareTrigger',
                    'codegen_method': 'public',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetApertureTimeInfo',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'apertureTime',
                                       'type': 'ViReal64'},
                                      {'direction': 'out',
                                       'enum': 'ApertureTimeUnits',
                                       'name': 'apertureTimeUnits',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetAutoRangeValue',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'autoRangeValue',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureAutoZeroMode',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'EnabledSetting',
                                       'name': 'autoZeroMode',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigurePowerLineFrequency',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'frequency',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureMeasurementDigits',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'Function',
                                       'name': 'measFunction',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'range', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'resolutionDigits',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureMeasurementAbsolute',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'Function',
                                       'name': 'measFunction',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'range', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'resolutionAbsolute',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureMeasCompleteSlope',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'Slope',
                                       'name': 'polarity',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureSampleTriggerSlope',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'Slope',
                                       'name': 'polarity',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ReadStatus',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'acqBacklog',
                                       'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': 'AcquisitionStatus',
                                       'name': 'acqDone', 'type': 'ViInt16'}],
                    'returns': 'ViStatus'},
                {   'name': 'Control',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None, # TODO(marcoskirsch): About to be obsoleted and replaced with commit.
                                       'name': 'action', 'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureADCCalibration',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'EnabledSetting',
                                       'name': 'adcGainComp', # TODO(marcoskirsch): bad param name?
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureOffsetCompOhms',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'EnabledSetting',
                                       'name': 'offsetCompOhms',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureCurrentSource',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'CurrentSource',
                                       'name': 'diodeCurrentSrc',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureCableCompType',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'CableCompensationType',
                                       'name': 'typeOfCompensation',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'PerformOpenCableComp',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'conductance',
                                       'type': 'ViReal64'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'susceptance',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'PerformShortCableComp',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'resistance',
                                       'type': 'ViReal64'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'reactance',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureOpenCableCompValues',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'conductance',
                                       'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'susceptance',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureShortCableCompValues',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'resistance',
                                       'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'reactance',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'LockSession',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'callerHasLock',
                                       'type': 'ViBoolean'}],
                    'returns': 'ViStatus'},
                {   'name': 'UnlockSession',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'callerHasLock',
                                       'type': 'ViBoolean'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureWaveformAcquisition',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'Function',
                                       'name': 'function', 'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'range', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'rate', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'waveformPoints',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureWaveformCoupling',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'WaveformCouplingMode',
                                       'name': 'coupling',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'FetchWaveform',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'maxTime', 'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'arraySize',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'waveformArray',
                                       'type': 'ViReal64'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'actualPoints',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ReadWaveform',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'maxTime', 'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'arraySize',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'waveformArray',
                                       'type': 'ViReal64'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'actualPoints',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetAttributeViInt32',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'value', 'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'SetAttributeViInt32',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'value', 'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'CheckAttributeViInt32',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'value', 'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetAttributeViReal64',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'value', 'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'SetAttributeViReal64',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'value', 'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'CheckAttributeViReal64',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'value', 'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetAttributeViString',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'bufSize', 'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'value',
                                       'is_buffer': True,
                                       'type': 'ViString'}],
                    'returns': 'ViStatus'},
                {   'name': 'SetAttributeViString',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'value',
                                       'is_buffer': True,
                                       'type': 'ViString'}],
                    'returns': 'ViStatus'},
                {   'name': 'CheckAttributeViString',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'value',
                                       'is_buffer': True,
                                       'type': 'ViChar'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetAttributeViSession',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'value', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'SetAttributeViSession',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'value', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'CheckAttributeViSession',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'value', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetAttributeViBoolean',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'value', 'type': 'ViBoolean'}],
                    'returns': 'ViStatus'},
                {   'name': 'SetAttributeViBoolean',
                    'codegen_method': 'private',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'value', 'type': 'ViBoolean'}],
                    'returns': 'ViStatus'},
                {   'name': 'CheckAttributeViBoolean',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'channelName',
                                       'is_buffer': True,
                                       'type': 'ViConstString'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'attributeId',
                                       'type': 'ViAttr'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'value', 'type': 'ViBoolean'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetNextCoercionRecord',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'bufferSize',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'record',
                                       'is_buffer': True,
                                       'type': 'ViChar'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetNextInterchangeWarning',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'bufferSize',
                                       'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'warnString',
                                       'is_buffer': True,
                                       'type': 'ViChar'}],
                    'returns': 'ViStatus'},
                {   'name': 'ResetInterchangeCheck',
                    'codegen_method': 'public',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'ClearInterchangeWarnings',
                    'codegen_method': 'public',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': '4022Control',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'resourceName',
                                       'is_buffer': True,
                                       'type': 'ViRsrc'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'configuration',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetChannelName',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'index', 'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'bufferSize',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'name',
                                       'is_buffer': True,
                                       'type': 'ViChar'}],
                    'returns': 'ViStatus'},
                {   'name': 'InitExtCal',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'resourceName',
                                       'is_buffer': True,
                                       'type': 'ViRsrc'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'password',
                                       'is_buffer': True,
                                       'type': 'ViChar'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'newVi',
                                       'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'CloseExtCal',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'action', 'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'CalAdjustLinearization',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'mode', 'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'range', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'inputR', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'expectedValue',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'CalAdjustGain',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'mode', 'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'range', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'inputR', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'expectedValue',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'CalAdjustOffset',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'mode', 'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'range', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'inputR', 'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'CalAdjustMisc',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'type', 'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'CalAdjustLC',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'type', 'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'CalAdjustACFilter',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'mode', 'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'range', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'frequency',
                                       'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'expectedValue',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'RestoreLastExtCalConstants',
                    'codegen_method': 'no',
                    'parameters': [{'direction': 'in', 'enum': None,
                                    'name': 'vi', 'type': 'ViSession'}],
                    'returns': 'ViStatus'},
                {   'name': 'SetCalPassword',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'oldPassword',
                                       'is_buffer': True,
                                       'type': 'ViChar'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'newPassword',
                                       'is_buffer': True,
                                       'type': 'ViChar'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetExtCalRecommendedInterval',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'months', 'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'SetCalUserDefinedInfo',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'info',
                                       'is_buffer': True,
                                       'type': 'ViChar'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetCalUserDefinedInfoMaxSize',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'infoSize',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetCalUserDefinedInfo',
                    'codegen_method': 'no',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'bufferSize',
                                       'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'info',
                                       'is_buffer': True,
                                       'type': 'ViChar'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetSelfCalSupported',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'selfCalSupported',
                                       'type': 'ViBoolean'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetCalDateAndTime',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'calType', 'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'month', 'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'day', 'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'year', 'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'hour', 'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'minute', 'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetCalCount',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'calType', 'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'count', 'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetLastCalTemp',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'calType', 'type': 'ViInt32'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'temperature',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'GetDevTemp',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'reserved',
                                       'is_buffer': True,
                                       'type': 'ViString'},
                                      {'direction': 'out', 'enum': None,
                                       'name': 'temperature',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureTransducerType',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'TemperatureTransducerType',
                                       'name': 'transducerType',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureThermocouple',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'thermocoupleType',
                                       'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'refJunctionType',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureFixedRefJunction',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'fixedRefJunction',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureRTDType',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'rtdType', 'type': 'ViInt32'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'resistance',
                                       'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureRTDCustom',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'a', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'b', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'c', 'type': 'ViReal64'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureThermistorType',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': 'TemperatureThermistorType',
                                       'name': 'thermistorType',
                                       'type': 'ViInt32'}],
                    'returns': 'ViStatus'},
                {   'name': 'ConfigureThermistorCustom',
                    'codegen_method': 'public',
                    'parameters': [   {'direction': 'in', 'enum': None,
                                       'name': 'vi', 'type': 'ViSession'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'a', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'b', 'type': 'ViReal64'},
                                      {'direction': 'in', 'enum': None,
                                       'name': 'c', 'type': 'ViReal64'}],
                    'returns': 'ViStatus'}]
>>>>>>> master

functions = {
    'Abort': {
        'purpose': '''
Aborts a previously initiated measurement and returns the DMM to the
Idle state.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'CalAdjustACFilter': {
        'long_description': '''
+------------+--------------------------------------------------------------------------------------------+
| |image0|   | **Note**  Refer to the calibration procedure for your device before using this function.   |
+------------+--------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
        'purpose': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072, calibrates the
filter coefficients used for AC measurements of the supplied **Mode**
and **Range**.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
The session handle that you obtain from `
niDMM\_InitExtCal <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitExtCal.html')>`__.
The handle identifies a particular instrument calibration session.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the calibration **mode** used to acquire the measurement.

For valid modes, refer to the calibration procedure for your device.
''',
                'name': 'mode',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **range** to calibrate.

For valid ranges, refer to the calibration procedure for your device.
Auto-ranging is not supported for calibration operations.
''',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **frequency** of the input signal.
''',
                'name': 'frequency',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **expectedValue** of the measurement.
''',
                'name': 'expectedValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'CalAdjustGain': {
        'long_description': '''
+------------+----------------------------------------------------------------------------------+
| |image0|   | **Notes**  The NI 4050 and NI 4060 are not supported.                            |
|            | Refer to the calibration procedure for your device before using this function.   |
+------------+----------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
        'purpose': '''
Calibrates the gain coefficient for the supplied **Mode**, **Range**,
and **Input\_Resistance**.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
The session handle that you obtain from `
niDMM\_InitExtCal <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitExtCal.html')>`__.
The handle identifies a particular instrument calibration session.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the calibration **mode** used to acquire the measurement.

For valid modes, refer to the calibration procedure for your device.
''',
                'name': 'mode',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **range** to calibrate.

For valid ranges, refer to the calibration procedure for your device.
Auto-ranging is not supported for calibration operations.
''',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **inputResistance** that the device should use.
**inputResistance** values are coerced up to the closest
**inputResistance**.
''',
                'name': 'inputResistance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **expectedValue** of the measurement.
''',
                'name': 'expectedValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'CalAdjustLC': {
        'long_description': '''
+------------+--------------------------------------------------------------------------------------------+
| |image0|   | **Note**  Refer to the calibration procedure for your device before using this function.   |
+------------+--------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
        'purpose': '''
For the NI 4082 and NI 4072 only, performs a specialized LC calibration
step depending on the specified **Type**.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
The session handle that you obtain from `
niDMM\_InitExtCal <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitExtCal.html')>`__.
The handle identifies a particular instrument calibration session.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies which of the LC calibration steps to perform.
+------------------------+--------------------------------------+
| L & C Open (default)   | Calibrates the open compensation.    |
+------------------------+--------------------------------------+
| L & C Short            | Calibrates the short compensation.   |
+------------------------+--------------------------------------+
| L & C 25 Ω             | Calibrates the 25 Ω resistance.      |
+------------------------+--------------------------------------+
| L & C 1 kΩ             | Calibrates the 1 kΩ resistance.      |
+------------------------+--------------------------------------+
| L & C 5 kΩ             | Calibrates the 5 kΩ resistance.      |
+------------------------+--------------------------------------+
| L & C 100 kΩ           | Calibrates the 100 kΩ resistance.    |
+------------------------+--------------------------------------+
''',
                'name': 'type',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'CalAdjustLinearization': {
        'purpose': '''
For the NI 4065 only, compensates for any non-linearities.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
The session handle that you obtain from `
niDMM\_InitExtCal <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitExtCal.html')>`__.
The handle identifies a particular instrument calibration session.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the calibration **function** used to acquire the measurement.

For valid modes, refer to the *NI 4065 6½ Digit DMM Calibration
Procedure*.
''',
                'name': 'function',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **range** to calibrate. **range** values are coerced up to
the closest **range**.

For valid ranges, refer to the *NI 4065 6½ Digit DMM Calibration
Procedure*. Auto-ranging is not supported for calibration operations.
''',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **inputResistance** that the device should use.
**inputResistance** values are coerced up to the closest
**inputResistance**.
''',
                'name': 'inputResistance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **expectedValue** of the measurement.
''',
                'name': 'expectedValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'CalAdjustMisc': {
        'long_description': '''
+------------+----------------------------------------------------------------------------------+
| |image0|   | **Note**  The NI 4050 and NI 4060 are not supported.                             |
|            | Refer to the calibration procedure for your device before using this function.   |
+------------+----------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
        'purpose': '''
Performs a specialized calibration step depending on the specified
**Type**.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
The session handle that you obtain from `
niDMM\_InitExtCal <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitExtCal.html')>`__.
The handle identifies a particular instrument calibration session.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies which of the miscellaneous calibration steps to perform.
+------------------------------------------+-----------------------------------------------------------------------+
| NIDMM\_EXTCAL\_MISCCAL\_VREF (default)   | Calibrate the Voltage Reference.                                      |
+------------------------------------------+-----------------------------------------------------------------------+
| NIDMM\_EXTCAL\_MISCCAL\_RREF             | Calibrate the Resistance Reference.                                   |
+------------------------------------------+-----------------------------------------------------------------------+
| NIDMM\_EXTCAL\_MISCCAL\_ZINT             | Calibrate the Internal Impedance.                                     |
+------------------------------------------+-----------------------------------------------------------------------+
| NIDMM\_EXTCAL\_MISCCAL\_2WIRELEAKAGE     | Calibrate the 2-wire Leakage resistance.                              |
+------------------------------------------+-----------------------------------------------------------------------+
| NIDMM\_EXTCAL\_MISCCAL\_4WIRELEAKAGE     | Calibrate the 4-wire Leakage resistance.                              |
+------------------------------------------+-----------------------------------------------------------------------+
| NIDMM\_EXTCAL\_MISCCAL\_SECTION          | Update calibration information and verify calibration completeness.   |
+------------------------------------------+-----------------------------------------------------------------------+
''',
                'name': 'type',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'CalAdjustOffset': {
        'long_description': '''
+------------+----------------------------------------------------------------------------------+
| |image0|   | **Note**  The NI 4050 and NI 4060 are not supported.                             |
|            | Refer to the calibration procedure for your device before using this function.   |
+------------+----------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
        'purpose': '''
Calibrates the offset and Auto Zero offset for the supplied **Mode**,
**Range**, and **Input\_Resistance**.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
The session handle that you obtain from `
niDMM\_InitExtCal <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitExtCal.html')>`__.
The handle identifies a particular instrument calibration session.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the calibration **mode** used to acquire the measurement.

For valid modes, refer to the calibration procedure for your device.
''',
                'name': 'mode',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **range** to calibrate.

For valid ranges, refer to the calibration procedure for your device.
Auto-ranging is not supported for calibration operations.
''',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **inputResistance** that the device should use.
**inputResistance** values are coerced up to the closest
**inputResistance**.
''',
                'name': 'inputResistance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'CheckAttributeViBoolean': {
        'long_description': '''
ViStatus = niDMM\_CheckAttributeViBoolean(ViSession Instrument\_Handle,
ViConstString Channel\_Name, ViAttr Attribute\_ID, ViBoolean
Attribute\_Value)
''',
        'purpose': '''
This function checks the validity of a value you specify for a ViBoolean
attribute.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the value that you want to set the attribute to.
''',
                'name': 'attributeValue',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'CheckAttributeViInt32': {
        'long_description': '''
ViStatus = niDMM\_CheckAttributeViInt32(ViSession Instrument\_Handle,
ViConstString Channel\_Name, ViAttr Attribute\_ID, ViInt32
Attribute\_Value)
''',
        'purpose': '''
This function checks the validity of a value you specify for a ViInt32
attribute.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the value that you want to set the attribute to.
''',
                'name': 'attributeValue',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'CheckAttributeViReal64': {
        'long_description': '''
ViStatus = niDMM\_CheckAttributeViReal64(ViSession Instrument\_Handle,
ViConstString Channel\_Name, ViAttr Attribute\_ID, ViReal64
Attribute\_Value)
''',
        'purpose': '''
This function checks the validity of a value you specify for a ViReal64
attribute.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the value that you want to set the attribute to.
''',
                'name': 'attributeValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'CheckAttributeViSession': {
        'long_description': '''
ViStatus = niDMM\_CheckAttributeViSession(ViSession Instrument\_Handle,
ViConstString Channel\_Name, ViAttr Attribute\_ID, ViSession
Attribute\_Value)
''',
        'purpose': '''
This function checks the validity of a value you specify for a ViSession
attribute.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the value that you want to set the attribute to.
''',
                'name': 'attributeValue',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'CheckAttributeViString': {
        'long_description': '''
ViStatus = niDMM\_CheckAttributeViString(ViSession Instrument\_Handle,
ViConstString Channel\_Name, ViAttr Attribute\_ID, ViChar
Attribute\_Value[])
''',
        'purpose': '''
This function checks the validity of a value you specify for a ViString
attribute.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'long_description': '''
Pass the value that you want to set the attribute to.
''',
                'name': 'attributeValue',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'ClearError': {
        'purpose': '''
Clears the error information for the current execution thread and the
IVI session you specify. If you pass VI\_NULL for the
**Instrument\_Handle** parameter, this function clears the error
information only for the current execution thread.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'ClearInterchangeWarnings': {
        'purpose': '''
Clears the list of current interchange warnings.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'CloseExtCal': {
        'long_description': '''
Purpose
-------

Performs the specified **Action**, closes the specified external
calibration session obtained from `
niDMM\_InitExtCal <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitExtCal.html')>`__,
and deallocates resources that it reserved.

+------------+----------------------------------------------------------------------------------+
| |image0|   | **Note**  The NI 4050 and NI 4060 are not supported.                             |
|            | Refer to the calibration procedure for your device before using this function.   |
+------------+----------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
The session handle that you obtain from `
niDMM\_InitExtCal <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitExtCal.html')>`__.
The handle identifies a particular instrument calibration session.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies whether the driver saves the updated calibration constants.
+------------------------------------------+------------------------------------------------------------------------------------------------------------+
| NIDMM\_EXTCAL\_ACTION\_ABORT (default)   | Restores the calibration constants to what they were before starting the external calibration procedure.   |
+------------------------------------------+------------------------------------------------------------------------------------------------------------+
| NIDMM\_EXTCAL\_ACTION\_SAVE              | Saves the new calibration constants to the device.                                                         |
+------------------------------------------+------------------------------------------------------------------------------------------------------------+
''',
                'name': 'action',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureACBandwidth': {
        'long_description': '''
Purpose
-------

Configures the `
NIDMM\_ATTR\_AC\_MIN\_FREQ <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AC_MIN_FREQ.html')>`__
and `
NIDMM\_ATTR\_AC\_MAX\_FREQ <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_AC_MAX_FREQ.html')>`__
attributes, which the DMM uses for AC measurements.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the minimum expected frequency component of the input signal
in hertz. This parameter affects the DMM only when you set the `
NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__
attribute to AC measurements. NI-DMM uses this parameter to calculate
the proper aperture for the measurement.
The driver sets the `
NIDMM\_ATTR\_AC\_MIN\_FREQ <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_AC_MIN_FREQ.html')>`__
attribute to this value. The valid range is 1 Hz–300 kHz for the NI
4080/4081/4082 and the NI 4070/4071/4072, 10 Hz–100 Hz for the NI 4065,
and 20 Hz–25 kHz for the NI 4050 and NI 4060.
''',
                'name': 'acMinimumFrequencyHz',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the maximum expected frequency component of the input signal
in hertz within the device limits. This parameter is used only for error
checking and verifies that the value of this parameter is less than the
maximum frequency of the device.

This parameter affects the DMM only when you set the `
NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_FUNCTION.html')>`__
attribute to AC measurements. The driver sets the `
NIDMM\_ATTR\_AC\_MAX\_FREQ <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AC_MAX_FREQ.html')>`__
attribute to this value. The valid range is 1 Hz–300 kHz for the NI
4080/4081/4082 and the NI 4070/4071/4072, 10 Hz–100 Hz for the NI 4065,
and 20 Hz–25 kHz for the NI 4050 and NI 4060.
''',
                'name': 'acMaximumFrequencyHz',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureADCCalibration': {
        'purpose': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
compensate for gain drift since the last external calibration or
self-calibration. When **ADC\_Calibration** is ON, the DMM measures an
internal reference to calculate the correct gain for the measurement.
When **ADC\_Calibration** is OFF, the DMM does not compensate for
changes to the gain.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **ADC\_Calibration** setting. The driver sets `
NIDMM\_ATTR\_ADC\_CALIBRATION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_ADC_CALIBRATION.html')>`__
to this value.
NIDMM\_VAL\_ADC\_CALIBRATION\_ON enables **ADC\_Calibration**.
NIDMM\_VAL\_ADC\_CALIBRATION\_OFF disables **ADC\_Calibration**. If you
set the value to NIDMM\_VAL\_ADC\_CALIBRATION\_AUTO, the driver
determines whether to enable **ADC\_Calibration** based on the
measurement function and resolution that you configure. If you configure
the NI 4080/4081/4082 or NI 4070/4071/4072 for a 6½–digit and greater
resolution DC measurement, the driver enables ADC Calibration. For all
other measurement configurations, the driver disables
**ADC\_Calibration**.
+------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+
| Name                                           | Value   | Description                                                                                         |
+================================================+=========+=====================================================================================================+
| NIDMM\_VAL\_ADC\_CALIBRATION\_AUTO (default)   | -1.0    | The DMM enables or disables **ADC\_Calibration** based on the configured function and resolution.   |
+------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+
| NIDMM\_VAL\_ADC\_CALIBRATION\_OFF              |  0      | The DMM does not compensate for changes to the gain.                                                |
+------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+
| NIDMM\_VAL\_ADC\_CALIBRATION\_ON               |  1      | The DMM measures an internal reference to calculate the correct gain for the measurement.           |
+------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+
''',
                'name': 'adcCalibration',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureAutoZeroMode': {
        'purpose': '''
Configures the DMM for **Auto\_Zero\_Mode**. When **Auto\_Zero\_Mode**
is ON, the DMM internally disconnects the input signal and takes a zero
reading. It then subtracts the zero reading from the measurement. This
prevents offset voltages present on the input circuitry of the DMM from
affecting measurement accuracy. When **Auto\_Zero\_Mode** is OFF, the
DMM does not compensate for zero reading offset.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **autoZeroMode**. NI-DMM sets the `
NIDMM\_ATTR\_AUTO\_ZERO <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_ZERO.html')>`__
attribute to this value.

ON enables **autoZeroMode** for each measurement. ONCE enables
**autoZeroMode** before the next measurement. The **autoZeroMode** value
is stored and used in subsequent measurements until the device is
reconfigured.

OFF disables **autoZeroMode**. If you set this parameter to AUTO, NI-DMM
determines whether to enable Auto Zero based on the measurement function
that you configure. If you configure the NI 4080/4081/4082 or the
NI 4070/4071/4072 for a 6½–digit and greater resolution DC measurement,
NI-DMM sets **autoZeroMode** to ON.

For all other DC measurement configurations on the NI 4080/4081/4082 or
the NI 4070/4071/4072, NI-DMM sets **autoZeroMode** to ONCE. For all AC
measurements or waveform acquisitions on the NI 4080/4081/4082 or the
NI 4070/4071/4072, NI-DMM sets **autoZeroMode** to OFF. For NI 4060,
**autoZeroMode** is set to OFF when AUTO is selected.

For NI 4065 devices, **autoZeroMode** is always ON. **autoZeroMode** is
an integral part of the signal measurement phase and adds no extra time
to the overall measurement.

+--------------------------+--------------------------+--------------------------+
| NIDMM\_VAL\_AUTO\_ZERO\_ | -1                       | NI-DMM chooses the Auto  |
| AUTO (default)           |                          | Zero setting based on    |
|                          |                          | the configured function  |
|                          |                          | and resolution.          |
+--------------------------+--------------------------+--------------------------+
| NIDMM\_VAL\_AUTO\_ZERO\_ |  0                       | Disables Auto Zero.      |
| OFF                      |                          | +------------+---------- |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | +                        |
|                          |                          | | |image0|   | **Note**  |
|                          |                          |  The NI 4065 does *not*  |
|                          |                          | support this setting.    |
|                          |                          | |                        |
|                          |                          | +------------+---------- |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | +                        |
+--------------------------+--------------------------+--------------------------+
| NIDMM\_VAL\_AUTO\_ZERO\_ |  1                       | The DMM internally       |
| ON                       |                          | disconnects the input    |
|                          |                          | signal following each    |
|                          |                          | measurement and takes a  |
|                          |                          | zero reading. It then    |
|                          |                          | subtracts the zero       |
|                          |                          | reading from the         |
|                          |                          | preceding reading.       |
|                          |                          | +------------+---------- |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | -------+                 |
|                          |                          | | |image1|   | **Note**  |
|                          |                          |  For NI 4065 devices, ** |
|                          |                          | autoZeroMode** is always |
|                          |                          |  ON. **autoZeroMode** is |
|                          |                          |  an integral part of the |
|                          |                          |  signal measurement phas |
|                          |                          | e and adds no extra time |
|                          |                          |  to the overall measurem |
|                          |                          | ent.   |                 |
|                          |                          | +------------+---------- |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | -------+                 |
+--------------------------+--------------------------+--------------------------+
| NIDMM\_VAL\_AUTO\_ZERO\_ |  2                       | The DMM internally       |
| ONCE                     |                          | disconnects the input    |
|                          |                          | signal following the     |
|                          |                          | first measurement and    |
|                          |                          | takes a zero reading. It |
|                          |                          | then subtracts the zero  |
|                          |                          | reading from the         |
|                          |                          | preceding reading and    |
|                          |                          | each measurement that    |
|                          |                          | follows.                 |
|                          |                          | +------------+---------- |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | -----+                   |
|                          |                          | | |image2|   | **Note**  |
|                          |                          |  The NI 4060/4065 does * |
|                          |                          | not* support this settin |
|                          |                          | g.   |                   |
|                          |                          | +------------+---------- |
|                          |                          | ------------------------ |
|                          |                          | ------------------------ |
|                          |                          | -----+                   |
+--------------------------+--------------------------+--------------------------+

.. |image0| image:: note.gif
.. |image1| image:: note.gif
.. |image2| image:: note.gif
''',
                'name': 'autoZeroMode',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureCableCompType': {
        'long_description': '''
Purpose
-------

For the NI 4082 and NI 4072 only, sets the `
NIDMM\_ATTR\_CABLE\_COMPENSATION\_TYPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_CABLE_COMP_TYPE.html')>`__
attribute for the current capacitance/inductance mode range.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the type of cable compensation that is used for the current
range.
''',
                'name': 'cableCompType',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureCurrentSource': {
        'purpose': '''
The NI 4050 and NI 4060 are not supported. Configures the
**Current\_Source** for diode measurements.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **currentSource** provided during diode measurements. For
valid ranges, refer to the device sections for your device. The driver
sets `
NIDMM\_ATTR\_CURRENT\_SOURCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_CURRENT_SOURCE.html')>`__
to this value.
+-------------------------------------+----------+-----------------------------------------------------+
| NIDMM\_VAL\_1\_MICROAMP             | 1 µA     | NI 4080/4081/4082 and NI 4070/4071/4072             |
+-------------------------------------+----------+-----------------------------------------------------+
| NIDMM\_VAL\_10\_MICROAMP            | 10 µA    | NI 4080/4081/4082 and NI 4070/4071/4072 only        |
+-------------------------------------+----------+-----------------------------------------------------+
| NIDMM\_VAL\_100\_MICROAMP           | 100 µA   | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065   |
+-------------------------------------+----------+-----------------------------------------------------+
| NIDMM\_VAL\_1\_MILLIAMP (default)   | 1 mA     | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065   |
+-------------------------------------+----------+-----------------------------------------------------+
''',
                'name': 'currentSource',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureFixedRefJunction': {
        'purpose': '''
Configures the fixed reference junction temperature for a thermocouple
with a fixed reference junction type.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the reference junction temperature when a fixed reference
junction is used to take a thermocouple measurement. The units are
degrees Celsius. NI-DMM uses this value to set the Fixed Reference
Junction property. The default is 25.00 (°C).
''',
                'name': 'fixedReferenceJunction',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureFrequencyVoltageRange': {
        'purpose': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072 only, specifies the
expected maximum amplitude of the input signal for frequency and period
measurements.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Sets the expected maximum amplitude of the input signal. Refer to the
`NI 4080 <javascript:LaunchHelp('dmm.chm::/4080_functional_overview.html')>`__,
`NI 4081 <javascript:LaunchHelp('dmm.chm::/4081_functional_overview.html')>`__,
`NI 4072 <javascript:LaunchHelp('dmm.chm::/4082.html')>`__,
`NI 4070 <javascript:LaunchHelp('dmm.chm::/4070_functional_overview.html')>`__,
`NI 4071 <javascript:LaunchHelp('dmm.chm::/4071_functional_overview.html')>`__,
and `NI 4072 <javascript:LaunchHelp('dmm.chm::/4072.html')>`__ sections
for a list of valid values. NI-DMM sets `
NIDMM\_ATTR\_FREQ\_VOLTAGE\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_FREQ_VOLTAGE_RANGE.html')>`__
to this value. The minimum peak-to-peak signal amplitude that can be
detected is 10% of the specified **voltageRange**.
+-----------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------+
| Name                                    | Value   | Description                                                                                                                        |
+=========================================+=========+====================================================================================================================================+
| NIDMM\_VAL\_AUTO\_RANGE\_ON (default)   | -1.0    | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement.   |
+-----------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------+
| NIDMM\_VAL\_AUTO\_RANGE\_OFF            | -2.0    | Disables Auto Ranging. The driver sets the voltage range to the last calculated voltage range.                                     |
+-----------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------+
''',
                'name': 'voltageRange',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureMeasCompleteDest': {
        'purpose': '''
Specifies the destination of the DMM Measurement Complete (MC) signal.
Refer to
`Triggering <javascript:LaunchHelp('dmm.chm::/trigger.html')>`__ for
more information.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the destination of the Measurement Complete signal. This
signal is issued when the DMM completes a single measurement. The driver
sets the `
NIDMM\_ATTR\_MEAS\_COMPLETE\_DEST <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_MEAS_COMPLETE_DEST.html')>`__
attribute to this value. This signal is commonly referred to as
Voltmeter Complete.
+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**  To determine which values are supported by each device, refer to the `LabWindows/CVI Trigger Routing <javascript:LaunchHelp('dmm.chm::/CVItrigger_routing.html')>`__ section.   |
+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'measCompleteDestination',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureMeasCompleteSlope': {
        'purpose': '''
Sets the Measurement Complete signal to either rising edge (positive) or
falling edge (negative) polarity.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the polarity of the signal that is generated. The driver sets
`
NIDMM\_ATTR\_MEAS\_DEST\_SLOPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_MEAS_DEST_SLOPE.html')>`__
to this value.
+--------------------------+-----+------------------------+------------------------------------------------------------------+
| Rising Edge              | 0   | NIDMM\_VAL\_POSITIVE   | The driver triggers on the rising edge of the trigger signal.    |
+--------------------------+-----+------------------------+------------------------------------------------------------------+
| Falling Edge (default)   | 1   | NIDMM\_VAL\_NEGATIVE   | The driver triggers on the falling edge of the trigger signal.   |
+--------------------------+-----+------------------------+------------------------------------------------------------------+
''',
                'name': 'measCompleteSlope',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureMeasurementAbsolute': {
        'long_description': '''
ViStatus = niDMM\_ConfigureMeasurementAbsolute(ViSession
Instrument\_Handle, ViInt32 Measurement\_Function, ViReal64 Range,
ViReal64 Resolution\_Absolute)

Purpose
-------

Configures the common attributes of the measurement. These attributes
include `
NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__,
`
NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__,
and `
NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_ABSOLUTE.html')>`__.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **measurementFunction** used to acquire the measurement.
The driver sets `
NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__
to this value.
''',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **range** for the function specified in the
**Measurement\_Function** parameter. When frequency is specified in the
**Measurement\_Function** parameter, you must supply the minimum
frequency expected in the **range** parameter. For example, you must
type in 100 Hz if you are measuring 101 Hz or higher.
For all other functions, you must supply a **range** that exceeds the
value that you are measuring. For example, you must type in 10 V if you
are measuring 9 V. **range** values are coerced up to the closest input
**range**. Refer to the `Devices
Overview <javascript:LaunchHelp('dmm.chm::/devices.html')>`__ for a list
of valid ranges. The driver sets `
NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__
to this value. The default is 0.02 V.
+------------+---------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**  The NI 4050, NI 4060, and NI 4065 only support Auto range when the trigger and sample trigger are set to IMMEDIATE.   |
+------------+---------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NIDMM\_VAL\_AUTO\_RANGE\_ON     | -1.0   | NI-DMM performs an Auto range before acquiring the measurement.                                                                                                                                                                                                                                                 |
+---------------------------------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NIDMM\_VAL\_AUTO\_RANGE\_OFF    | -2.0   | NI-DMM sets the range to the current ` NIDMM\_ATTR\_AUTO\_RANGE\_VALUE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_RANGE_VALUE.html')>`__ and uses this range                                                                                                                 |
|                                 |        | for all subsequent measurements until the measurement configuration is changed.                                                                                                                                                                                                                                 |
+---------------------------------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NIDMM\_VAL\_AUTO\_RANGE\_ONCE   | -3.0   | NI-DMM performs an Auto range before acquiring the measurement. The ` NIDMM\_ATTR\_AUTO\_RANGE\_VALUE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_RANGE_VALUE.html')>`__ is stored and used for all subsequent measurements until the measurement configuration is changed.   |
+---------------------------------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the absolute resolution for the measurement. NI-DMM sets `
NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_ABSOLUTE.html')>`__
to this value. This parameter is ignored when the **Range** parameter is
set to NIDMM\_VAL\_AUTO\_RANGE\_ON (-1.0) or
NIDMM\_VAL\_AUTO\_RANGE\_ONCE (-3.0). The default is 0.001 V.
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**  NI-DMM ignores this parameter for capacitance and inductance measurements on the NI 4072. To achieve better resolution for such measurements, use the ` NIDMM\_ATTR\_LC\_NUMBER\_MEAS\_TO\_AVERAGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE.html')>`__ attribute.   |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'resolutionAbsolute',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureMeasurementDigits': {
        'long_description': '''
ViStatus = niDMM\_ConfigureMeasurementDigits(ViSession
Instrument\_Handle, ViInt32 Measurement\_Function, ViReal64 Range,
ViReal64 Resolution\_Digits)

Purpose
-------

Configures the common attributes of the measurement. These attributes
include `
NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__,
`
NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__,
and `
NIDMM\_ATTR\_RESOLUTION\_DIGITS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_DIGITS.html')>`__.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **measurementFunction** used to acquire the measurement.
The driver sets `
NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__
to this value.
''',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the range for the function specified in the
**Measurement\_Function** parameter. When frequency is specified in the
**Measurement\_Function** parameter, you must supply the minimum
frequency expected in the **range** parameter. For example, you must
type in 100 Hz if you are measuring 101 Hz or higher.
For all other functions, you must supply a range that exceeds the value
that you are measuring. For example, you must type in 10 V if you are
measuring 9 V. range values are coerced up to the closest input range.
Refer to the `Devices
Overview <javascript:LaunchHelp('dmm.chm::/devices.html')>`__ for a list
of valid ranges. The driver sets `
NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__
to this value. The default is 0.02 V.
+------------+---------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**  The NI 4050, NI 4060, and NI 4065 only support Auto range when the trigger and sample trigger are set to IMMEDIATE.   |
+------------+---------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NIDMM\_VAL\_AUTO\_RANGE\_ON     | -1.0   | NI-DMM performs an Auto range before acquiring the measurement.                                                                                                                                                                                                                                                 |
+---------------------------------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NIDMM\_VAL\_AUTO\_RANGE\_OFF    | -2.0   | NI-DMM sets the range to the current ` NIDMM\_ATTR\_AUTO\_RANGE\_VALUE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_RANGE_VALUE.html')>`__ and uses this range                                                                                                                 |
|                                 |        | for all subsequent measurements until the measurement configuration is changed.                                                                                                                                                                                                                                 |
+---------------------------------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NIDMM\_VAL\_AUTO\_RANGE\_ONCE   | -3.0   | NI-DMM performs an Auto range before acquiring the measurement. The ` NIDMM\_ATTR\_AUTO\_RANGE\_VALUE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_RANGE_VALUE.html')>`__ is stored and used for all subsequent measurements until the measurement configuration is changed.   |
+---------------------------------+--------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the resolution of the measurement in digits. The driver sets
the `Devices
Overview <javascript:LaunchHelp('dmm.chm::/devices.html')>`__ for a list
of valid ranges. The driver sets `
NIDMM\_ATTR\_RESOLUTION\_DIGITS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_DIGITS.html')>`__
attribute to this value. This parameter is ignored when the **Range**
parameter is set to NIDMM\_VAL\_AUTO\_RANGE\_ON (-1.0) or
NIDMM\_VAL\_AUTO\_RANGE\_ONCE (-3.0). The default is 5½.
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**  NI-DMM ignores this parameter for capacitance and inductance measurements on the NI 4072. To achieve better resolution for such measurements, use the ` NIDMM\_ATTR\_LC\_NUMBER\_MEAS\_TO\_AVERAGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE.html')>`__ attribute.   |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'resolutionDigits',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureMultiPoint': {
        'long_description': '''
Purpose
-------

Configures the attributes for multipoint measurements. These attributes
include `
NIDMM\_ATTR\_TRIGGER\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_TRIGGER_COUNT.html')>`__,
`
NIDMM\_ATTR\_SAMPLE\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_COUNT.html')>`__,
`
NIDMM\_ATTR\_SAMPLE\_TRIGGER <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_TRIGGER.html')>`__,
and `
NIDMM\_ATTR\_SAMPLE\_INTERVAL <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_INTERVAL.html')>`__.

For continuous acquisitions, set `
NIDMM\_ATTR\_TRIGGER\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_TRIGGER_COUNT.html')>`__
or `
NIDMM\_ATTR\_SAMPLE\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_COUNT.html')>`__
to zero. For more information, refer to `Multiple Point
Acquisitions <javascript:LaunchHelp('dmm.chm::/multi_point.html')>`__,
`Triggering <javascript:LaunchHelp('dmm.chm::/trigger.html')>`__, and
`Using
Switches <javascript:LaunchHelp('dmm.chm::/switch_selection.html')>`__.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Sets the number of triggers you want the DMM to receive before returning
to the Idle state. The driver sets `
NIDMM\_ATTR\_TRIGGER\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_TRIGGER_COUNT.html')>`__
to this value. The default value is 1.
''',
                'name': 'triggerCount',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Sets the number of measurements the DMM makes in each measurement
sequence initiated by a trigger. The driver sets `
NIDMM\_ATTR\_SAMPLE\_COUNT <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_COUNT.html')>`__
to this value. The default value is 1.
''',
                'name': 'sampleCount',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **sampleTrigger** source you want to use. The driver sets
`
NIDMM\_ATTR\_SAMPLE\_TRIGGER <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_SAMPLE_TRIGGER.html')>`__
to this value. The default is Immediate.
+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**  To determine which values are supported by each device, refer to the `LabWindows/CVI Trigger Routing <javascript:LaunchHelp('dmm.chm::/CVItrigger_routing.html')>`__ section.   |
+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'sampleTrigger',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Sets the amount of time in seconds the DMM waits between measurement
cycles. The driver sets `
NIDMM\_ATTR\_SAMPLE\_INTERVAL <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_SAMPLE_INTERVAL.html')>`__
to this value. Specify a sample interval to add settling time between
measurement cycles or to decrease the measurement rate.
**sampleInterval** only applies when the **Sample\_Trigger** is set to
INTERVAL.

On the NI 4060, the **sampleInterval** value is used as the settling
time. When sample interval is set to 0, the DMM does not settle between
measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
specified in **sampleInterval** as additional delay. The default value
(-1) ensures that the DMM settles for a recommended time. This is the
same as using an Immediate trigger.

+------------+----------------------------------------------------------------------------------+
| |image0|   | **Note**  This attribute is not used on the NI 4080/4081/4082 and the NI 4050.   |
+------------+----------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'sampleInterval',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureOffsetCompOhms': {
        'purpose': '''
For NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
compensate for voltage offsets in resistance measurements. When
**Offset\_Comp\_Ohms** is enabled, the DMM measures the resistance twice
(once with the current source on and again with it turned off). Any
voltage offset present in both measurements is cancelled out.
**Offset\_Comp\_Ohms** is useful when measuring resistance values less
than 10 KΩ.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Enables or disables **offsetCompOhms**. The driver sets `
NIDMM\_ATTR\_OFFSET\_COMP\_OHMS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_OFFSET_COMP_OHMS.html')>`__
to this value.
+-------------------------------------------------+---------+--------------------------------------+
| Name                                            | Value   | Description                          |
+=================================================+=========+======================================+
| NIDMM\_VAL\_OFFSET\_COMP\_OHMS\_OFF (default)   | 0       | Off disables \ **offsetCompOhms**.   |
+-------------------------------------------------+---------+--------------------------------------+
| NIDMM\_VAL\_OFFSET\_COMP\_OHMS\_ON              | 1       | On enables **offsetCompOhms**.       |
+-------------------------------------------------+---------+--------------------------------------+
''',
                'name': 'offsetCompOhms',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureOpenCableCompValues': {
        'long_description': '''
Purpose
-------

For the NI 4082 and NI 4072 only, configures the `
NIDMM\_ATTR\_OPEN\_CABLE\_COMP\_CONDUCTANCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCE.html')>`__
and `
NIDMM\_ATTR\_OPEN\_CABLE\_COMP\_SUSCEPTANCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCE.html')>`__
attributes.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the open cable compensation **conductance**.
''',
                'name': 'conductance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the open cable compensation **susceptance**.
''',
                'name': 'susceptance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigurePowerLineFrequency': {
        'purpose': '''
Specifies the powerline frequency.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
**Powerline Frequency** specifies the powerline frequency in hertz.
NI-DMM sets the Powerline Frequency property to this value.
''',
                'name': 'powerLineFrequencyHz',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureRTDCustom': {
        'purpose': '''
Configures the A, B, and C parameters for a custom RTD.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
Type parameter is set to Custom in the `
niDMM\_ConfigureRTDType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureRTDType.html')>`__
function. The default is 3.9083e-3 (Pt3851)
''',
                'name': 'rtdA',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
Type parameter is set to Custom in the `
niDMM\_ConfigureRTDType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureRTDType.html')>`__
function. The default is -5.775e-7 (Pt3851).
''',
                'name': 'rtdB',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
Type parameter is set to Custom in the `
niDMM\_ConfigureRTDType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureRTDType.html')>`__
function. The default is -4.183e-12 (Pt3851).
''',
                'name': 'rtdC',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureRTDType': {
        'purpose': '''
Configures the RTD Type and RTD Resistance parameters for an RTD.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the type of RTD used to measure the temperature resistance.
NI-DMM uses this value to set the RTD Type property. The default is
NIDMM\_VAL\_TEMP\_RTD\_PT3851.
Enum
Standards
Material
TCR (α)
Typical R\ :sub:`0` (Ω)
Callendar-Van Dusen Coefficient
Notes
NIDMM\_VAL\_TEMP\_RTD\_PT3851
IEC-751
DIN 43760
BS 1904
ASTM-E1137
EN-60751
Platinum
.003851
100 Ω
1000 Ω
A = 3.9083 × 10\ :sup:`–3`
B = –5.775×10:sup:`–7`
C = –4.183×10:sup:`–12`
Most common RTDs
NIDMM\_VAL\_TEMP\_RTD\_PT3750
Low-cost vendor compliant RTD\*
Platinum
.003750
1000 Ω
A = 3.81 × 10\ :sup:`–3`
B = –6.02×10:sup:`–7`
C = –6.0×10:sup:`–12`
Low-cost RTD
NIDMM\_VAL\_TEMP\_RTD\_PT3916
JISC 1604
Platinum
.003916
100 Ω
A = 3.9739 × 10\ :sup:`–3`
B = –5.870×10:sup:`–7`
C = –4.4 ×10\ :sup:`–12`
Used in primarily in Japan
NIDMM\_VAL\_TEMP\_RTD\_PT3920
US Industrial Standard D-100
American
Platinum
.003920
100 Ω
A = 3.9787 × 10\ :sup:`–3`
B = –5.8686×10:sup:`–7`
C = –4.167 ×10\ :sup:`–12`
Low-cost RTD
NIDMM\_VAL\_TEMP\_RTD\_PT3911
US Industrial Standard
American
Platinum
.003911
100 Ω
A = 3.9692 × 10\ :sup:`–3`
B = –5.8495×10:sup:`–7`
C = –4.233 ×10\ :sup:`–12`
Low-cost RTD
NIDMM\_VAL\_TEMP\_RTD\_PT3928
ITS-90
Platinum
.003928
100 Ω
A = 3.9888 × 10\ :sup:`–3`
B = –5.915×10:sup:`–7`
C = –3.85 ×10\ :sup:`–12`
The definition of temperature
\*No standard. Check the TCR.
''',
                'name': 'rtdType',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
set the RTD Resistance property. The default is 100 (Ω).
''',
                'name': 'rtdResistance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureSampleTriggerSlope': {
        'purpose': '''
Sets the `
NIDMM\_ATTR\_SAMPLE\_TRIGGER\_SLOPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_TRIGGER_SLOPE.html')>`__
to either rising edge (positive) or falling edge (negative) polarity.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the polarity of the Trigger signal on which the measurement is
triggered for values of either NIDMM\_VAL\_POSITIVE or
NIDMM\_VAL\_NEGATIVE. The driver sets `
NIDMM\_ATTR\_SAMPLE\_TRIGGER\_SLOPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SAMPLE_TRIGGER_SLOPE.html')>`__
to this value.
+--------------------------+-----+------------------------+------------------------------------------------------------------+
| Rising Edge              | 0   | NIDMM\_VAL\_POSITIVE   | The driver triggers on the rising edge of the trigger signal.    |
+--------------------------+-----+------------------------+------------------------------------------------------------------+
| Falling Edge (default)   | 1   | NIDMM\_VAL\_NEGATIVE   | The driver triggers on the falling edge of the trigger signal.   |
+--------------------------+-----+------------------------+------------------------------------------------------------------+
''',
                'name': 'sampleTriggerSlope',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureShortCableCompValues': {
        'long_description': '''
Purpose
-------

For the NI 4082 and NI 4072 only, configures the
`NIDMM\_ATTR\_SHORT\_CABLE\_COMP\_RESISTANCE <javascript:LaunchHelp('dmmcref.chm::/caNIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCE.html')>`__
and
`NIDMM\_ATTR\_SHORT\_CABLE\_COMP\_REACTANCE <javascript:LaunchHelp('dmmcref.chm::/caNIDMM_ATTR_SHORT_CABLE_COMP_REACTANCE.html')>`__
attributes.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the short cable compensation **resistance**.
''',
                'name': 'resistance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the short cable compensation **reactance**.
''',
                'name': 'reactance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureThermistorCustom': {
        'purpose': '''
Configures the A, B, and C parameters for a custom thermistor.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the Steinhart-Hart A coefficient for thermistor scaling when
Thermistor Type is set to Custom in the `
niDMM\_ConfigureThermistorType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureThermistorType.html')>`__
function. The default is 1.0295e-3 (44006).
''',
                'name': 'thermistorA',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the Steinhart-Hart B coefficient for thermistor scaling when
Thermistor Type is set to Custom in the `
niDMM\_ConfigureThermistorType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureThermistorType.html')>`__
function. The default is 2.391e-4 (44006).
''',
                'name': 'thermistorB',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the Steinhart-Hart C coefficient for thermistor scaling when
Thermistor Type is set to Custom in the `
niDMM\_ConfigureThermistorType <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureThermistorType.html')>`__
function. The default is 1.568e-7 (44006).
''',
                'name': 'thermistorC',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureThermistorType': {
        'purpose': '''
Configures the thermistor type.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the type of thermistor used to measure the temperature. NI-DMM
uses this value to set the Thermistor Type property. The default is
NIDMM\_VAL\_TEMP\_THERMISTOR\_44006.

+--------------------+--------------------+--------------------+--------------------+
| **Defined Values** | **Thermistor       | **Value**          | **25 °C            |
|                    | Type**             |                    | Resistance**       |
+--------------------+--------------------+--------------------+--------------------+
| NIDMM\_VAL\_TEMP\_ | Custom             | 0                  | —                  |
| THERMISTOR\_CUSTOM |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NIDMM\_VAL\_TEMP\_ | 44004              | 1                  | 2.25 kΩ            |
| THERMISTOR\_44004  |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NIDMM\_VAL\_TEMP\_ | 44006              | 2                  | 10 kΩ              |
| THERMISTOR\_44006  |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| NIDMM\_VAL\_TEMP\_ | 44007              | 3                  | 5 kΩ               |
| THERMISTOR\_44007  |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
''',
                'name': 'thermistorType',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureThermocouple': {
        'purpose': '''
Configures the thermocouple type and reference junction type for a
chosen thermocouple.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the type of thermocouple used to measure the temperature.
NI-DMM uses this value to set the Thermocouple Type property. The
default is NIDMM\_VAL\_TEMP\_TC\_J.
+---------------------------+-----------------------+
| NIDMM\_VAL\_TEMP\_TC\_B   | Thermocouple type B   |
+---------------------------+-----------------------+
| NIDMM\_VAL\_TEMP\_TC\_E   | Thermocouple type E   |
+---------------------------+-----------------------+
| NIDMM\_VAL\_TEMP\_TC\_J   | Thermocouple type J   |
+---------------------------+-----------------------+
| NIDMM\_VAL\_TEMP\_TC\_K   | Thermocouple type K   |
+---------------------------+-----------------------+
| NIDMM\_VAL\_TEMP\_TC\_N   | Thermocouple type N   |
+---------------------------+-----------------------+
| NIDMM\_VAL\_TEMP\_TC\_R   | Thermocouple type R   |
+---------------------------+-----------------------+
| NIDMM\_VAL\_TEMP\_TC\_S   | Thermocouple type S   |
+---------------------------+-----------------------+
| NIDMM\_VAL\_TEMP\_TC\_T   | Thermocouple type T   |
+---------------------------+-----------------------+
''',
                'name': 'thermocoupleType',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the type of reference junction to be used in the reference
junction compensation of a thermocouple measurement. NI-DMM uses this
value to set the Reference Junction Type property. The only supported
value is NIDMM\_VAL\_TEMP\_REF\_JUNC\_FIXED.
''',
                'name': 'referenceJunctionType',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureTransducerType': {
        'purpose': '''
Configures the transducer type.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the type of device used to measure the temperature. NI-DMM
uses this value to set the Transducer Type property. The default is
NIDMM\_VAL\_THERMOCOUPLE.
+----------------------------+----------------+
| NIDMM\_VAL\_2\_WIRE\_RTD   | 2-wire RTD     |
+----------------------------+----------------+
| NIDMM\_VAL\_4\_WIRE\_RTD   | 4-wire RTD     |
+----------------------------+----------------+
| NIDMM\_VAL\_THERMISTOR     | Thermistor     |
+----------------------------+----------------+
| NIDMM\_VAL\_THERMOCOUPLE   | Thermocouple   |
+----------------------------+----------------+
''',
                'name': 'transducerType',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureTrigger': {
        'long_description': '''
Purpose
-------

Configures the DMM **Trigger\_Source** and **Trigger\_Delay**. Refer to
`Triggering <javascript:LaunchHelp('dmm.chm::/trigger.html')>`__ and
`Using
Switches <javascript:LaunchHelp('dmm.chm::/switch_selection.html')>`__
for more information.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **triggerSource** that initiates the acquisition. The
driver sets `
NIDMM\_ATTR\_TRIGGER\_SOURCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_TRIGGER_SOURCE.html')>`__
to this value. Software configures the DMM to wait until `
niDMM\_SendSoftwareTrigger <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_SendSoftwareTrigger.html')>`__
is called before triggering the DMM.
+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**  To determine which values are supported by each device, refer to the `LabWindows/CVI Trigger Routing <javascript:LaunchHelp('dmm.chm::/CVItrigger_routing.html')>`__ section.   |
+------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'triggerSource',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the time that the DMM waits after it has received a trigger
before taking a measurement. The driver sets the
`NIDMM\_ATTR\_TRIGGER\_DELAY <javascript:LaunchHelp('dmmcref.chm::/caNIDMM_ATTR_TRIGGER_DELAY.html')>`__
attribute to this value. By default, **triggerDelay** is
NIDMM\_VAL\_AUTO\_DELAY (-1), which means the DMM waits an appropriate
settling time before taking the measurement. On the NI 4060, if you set
**triggerDelay** to 0, the DMM does not settle before taking the
measurement. The NI 4065 and NI 4070/4071/4072 use the value specified
in **triggerDelay** as additional settling time.
+------------+---------------------------------------------------------------------------------------------------+
| |image0|   | **Note**  When using the NI 4050, **triggerDelay** must be set to NIDMM\_VAL\_AUTO\_DELAY (-1).   |
+------------+---------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'triggerDelay',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ConfigureTriggerSlope': {
        'purpose': '''
Sets the `
NIDMM\_ATTR\_TRIGGER\_SLOPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_TRIGGER_SLOPE.html')>`__
attribute to either rising edge (positive) or falling edge (negative)
polarity.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the polarity of the trigger signal on which the measurement is
triggered for values of either NIDMM\_VAL\_POSITIVE or
NIDMM\_VAL\_NEGATIVE. The driver sets the `
NIDMM\_ATTR\_TRIGGER\_SLOPE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_TRIGGER_SLOPE.html')>`__
attribute to this value.
+----------------------------------+-----+------------------------------------------------------------------+
| NIDMM\_VAL\_POSITIVE             | 0   | The driver triggers on the rising edge of the trigger signal.    |
+----------------------------------+-----+------------------------------------------------------------------+
| NIDMM\_VAL\_NEGATIVE (default)   | 1   | The driver triggers on the falling edge of the trigger signal.   |
+----------------------------------+-----+------------------------------------------------------------------+
''',
                'name': 'triggerSlope',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureWaveformAcquisition': {
        'purpose': '''
Configures the DMM for waveform acquisitions. This feature is supported
on the NI 4080/4081/4082 and the NI 4070/4071/4072.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **measurementFunction** used in a waveform acquisition.
The driver sets `
NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_FUNCTION.html')>`__
to this value.
+-------------------------------------------+--------+--------------------+
| NIDMM\_VAL\_WAVEFORM\_VOLTAGE (default)   | 1003   | Voltage Waveform   |
+-------------------------------------------+--------+--------------------+
| NIDMM\_VAL\_WAVEFORM\_CURRENT             | 1004   | Current Waveform   |
+-------------------------------------------+--------+--------------------+
''',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the expected maximum amplitude of the input signal and sets
the **range** for the **Measurement\_Function**. NI-DMM sets `
NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_RANGE.html')>`__
to this value. **range** values are coerced up to the closest input
**range**. The default is 10.0.

For valid ranges refer to the topics in
`Devices <javascript:LaunchHelp('dmm.chm::/Devices.html')>`__.

Auto-ranging is not supported during waveform acquisitions.
''',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **rate** of the acquisition in samples per second. NI-DMM
sets `
NIDMM\_ATTR\_WAVEFORM\_RATE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_WAVEFORM_RATE.html')>`__
to this value.

The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
to the closest integer divisor of 1,800,000. The default value is
1,800,000.
''',
                'name': 'rate',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the number of points to acquire before the waveform
acquisition completes. NI-DMM sets `
NIDMM\_ATTR\_WAVEFORM\_POINTS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_WAVEFORM_POINTS.html')>`__
to this value.

To calculate the maximum and minimum number of waveform points that you
can acquire in one acquisition, refer to the `Waveform Acquisition
Measurement
Cycle <javascript:LaunchHelp('dmm.chm::/waveform_cycle.html')>`__.

The default value is 500.
''',
                'name': 'waveformPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ConfigureWaveformCoupling': {
        'purpose': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072, configures
instrument coupling for voltage waveforms.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Selects DC or AC coupling. The driver sets `
NIDMM\_ATTR\_WAVEFORM\_COUPLING <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_WAVEFORM_COUPLING.html')>`__
to this value.
+------------------------------------------------+---------+---------------+
| Name                                           | Value   | Description   |
+================================================+=========+===============+
| NIDMM\_VAL\_WAVEFORM\_COUPLING\_AC             | 0       | AC coupling   |
+------------------------------------------------+---------+---------------+
| NIDMM\_VAL\_WAVEFORM\_COUPLING\_DC (default)   | 1       | DC coupling   |
+------------------------------------------------+---------+---------------+
''',
                'name': 'waveformCoupling',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'Control': {
        'long_description': '''
Purpose
-------

Controls the DMM. Use this function if you want a parameter change to be
immediately reflected in the hardware. Use this function before calling
`
niDMM\_Initiate <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cvinidMM_Initiate.html')>`__
to make the initiate call as quickly as possible.

+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Notes**  The NI 4050 and NI 4060 are not supported.                                                                                                                                                   |
|            | Calling this function while the DMM is taking measurements results in an error. After the DMM is finished taking measurements, calling this function will make any unfetched data points unavailable.   |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
The action you want the driver to perform. Only
NIDMM\_VAL\_CONTROL\_COMMIT (0) is supported, which commits to hardware
all of the configured attributes associated with the session.
''',
                'name': 'controlAction',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'Disable': {
        'purpose': '''
Places the instrument in a quiescent state where it has minimal or no
impact on the system to which it is connected. If a measurement is in
progress when this function is called, the measurement is aborted.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'Fetch': {
        'long_description': '''
Purpose
-------

Returns the value from a previously initiated measurement. You must call
`
niDMM\_Initiate <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_Initiate.html')>`__
before calling this function.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **maximumTime** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
The measured value returned from the DMM.
''',
                'name': 'reading',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'FetchMultiPoint': {
        'long_description': '''
Purpose
-------

Returns an array of values from a previously initiated multipoint
measurement. The number of measurements the DMM makes is determined by
the values you specify for the **Trigger\_Count** and **Sample\_Count**
parameters of `
niDMM\_ConfigureMultiPoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_ConfigureMultiPoint.html')>`__.
You must first call `
niDMM\_Initiate <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_Initiate.html')>`__
to initiate a measurement before calling this function.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **maximumTime** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the number of measurements to acquire. The maximum number of
measurements for a finite acquisition is the (**Trigger Count** x
**Sample Count**) parameters in `
niDMM\_ConfigureMultiPoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureMultiPoint.html')>`__.

For continuous acquisitions, up to 100,000 points can be returned at
once. The number of measurements can be a subset. The valid range is any
positive ViInt32. The default value is 1.
''',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
An array of measurement values.
+------------+-----------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**   The size of the **readingArray** must be at least the size that you specify for the **Array\_Size** parameter.   |
+------------+-----------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'readingArray',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates the number of measured values actually retrieved from the DMM.
''',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'FetchWaveform': {
        'purpose': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
values from a previously initiated waveform acquisition. You must call `
niDMM\_Initiate <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_Initiate.html')>`__
before calling this function.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **maximumTime** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the number of waveform points to return. You specify the total
number of points that the DMM acquires in the **Waveform Points**
parameter of `
niDMM\_ConfigureWaveformAcquisition <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureWaveformAcquisition.htm')>`__.
The default value is 1.
''',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
**Waveform Array** is an array of measurement values stored in waveform
data type.
''',
                'name': 'waveformArray',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates the number of measured values actually retrieved from the DMM.
''',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'FormatMeasAbsolute': {
        'purpose': '''
Formats the **Measurement** to the proper number of displayed digits
according to the **Measurement\_Function**, **Range**, and
**Resolution**. Returns the formatted data, range, and mode strings.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Specifies the **measurementFunction** used to acquire the measurement.
The driver sets `
NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__
to this value.
''',
                'name': 'measurementFunction',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the `
NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__
used to acquire the **Measurement**.
''',
                'name': 'range',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the `
NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_ABSOLUTE.html')>`__
of the **Measurement**.
''',
                'name': 'resolution',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the measured value returned from the DMM.
''',
                'name': 'measurement',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Returns a string containing the units of the **Measurement** mode.
''',
                'name': 'modeString',
                'type': 'ViChar',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Returns the `
NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__
of the **Measurement**, formatted into a string with the correct number
of display digits.
''',
                'name': 'rangeString',
                'type': 'ViChar',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Returns the **Measurement**, formatted according to the `
NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_FUNCTION.html')>`__,
`
NIDMM\_ATTR\_RANGE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE.html')>`__,
and `
NIDMM\_ATTR\_RESOLUTION\_ABSOLUTE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RESOLUTION_ABSOLUTE.html')>`__.
''',
                'name': 'dataString',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetApertureTimeInfo': {
        'purpose': '''
Returns the DMM **Aperture\_Time** and **Aperture\_Time\_Units**.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Specifies the amount of time the DMM digitizes the input signal for a
single measurement. This parameter does not include settling time.
Returns the value of the `
NIDMM\_ATTR\_APERTURE\_TIME <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_APERTURE_TIME.html')>`__
attribute. The units of this attribute depend on the value of the `
NIDMM\_ATTR\_APERTURE\_TIME\_UNITS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_APERTURE_TIME_UNITS.html')>`__
attribute.
On the NI 4070/4071/4072, the minimum aperture time is 8.89 µs, and the
maximum aperture time is 149 s. Any number of powerline cycles (PLCs)
within the minimum and maximum ranges is allowed on the
NI 4070/4071/4072.
On the NI 4065 the minimum aperture time is 333 µs, and the maximum
aperture time is 78.2 s. If setting the number of averages directly, the
total measurement time is aperture time X the number of averages, which
must be less than 72.8 s. The aperture times allowed are 333 µs, 667 µs,
or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33 ms, and so
on. If you set an aperture time other than 333 µs, 667 µs, or multiples
of 1.11 ms, the value will be coerced up to the next supported aperture
time.
On the NI 4060, when the powerline frequency is 60, the PLCs allowed are
1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50,
the PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.
''',
                'name': 'apertureTime',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates the units of aperture time as powerline cycles (PLCs) or
seconds. Returns the value of the `
NIDMM\_ATTR\_APERTURE\_TIME\_UNITS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_APERTURE_TIME_UNITS.html')>`__
attribute.
+-----------------------------------+-----+--------------------+
| NIDMM\_VAL\_SECONDS               | 0   | Seconds            |
+-----------------------------------+-----+--------------------+
| NIDMM\_VAL\_POWER\_LINE\_CYCLES   | 1   | Powerline Cycles   |
+-----------------------------------+-----+--------------------+
''',
                'name': 'apertureTimeUnits',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetAttributeViBoolean': {
        'long_description': '''
If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid.
''',
        'purpose': '''
Queries the value of a ViBoolean attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns the current value of the attribute. Pass the address of a
ViBoolean variable.
''',
                'name': 'attributeValue',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'GetAttributeViInt32': {
        'long_description': '''
If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid.
''',
        'purpose': '''
Queries the value of a ViInt32 attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns the current value of the attribute. Pass the address of a
ViInt32 variable.
''',
                'name': 'attributeValue',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetAttributeViReal64': {
        'long_description': '''
Purpose
-------

Queries the value of a ViReal64 attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns the current value of the attribute. Pass the address of a
ViReal64 variable.
''',
                'name': 'attributeValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'GetAttributeViSession': {
        'long_description': '''
Purpose
-------

Queries the value of a ViSession attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns the current value of the attribute. Pass the address of a
ViSession variable.
''',
                'name': 'attributeValue',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'GetAttributeViString': {
        'long_description': '''
If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid.
   You must provide a ViChar array to serve as a buffer for the value.
   You pass the number of bytes in the buffer as the Array Size
   parameter.
''',
        'purpose': '''
Queries the value of a ViString attribute. You can use this function to
get the values of instrument-specific attributes and inherent IVI
attributes.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the number of bytes in the ViChar array you specify for the
**Attribute\_Value** parameter.

If the current value of the attribute, including the terminating NULL
byte, contains more bytes that you indicate in this parameter, the
function copies **bufferSize**—1 bytes into the buffer, places an ASCII
NUL byte at the end of the buffer, and returns the buffer size you must
pass to get the entire value. For example, if the value is "123456" and
the **bufferSize** is 4, the function places "123" into the buffer and
returns 7.

If you pass a negative number, the function copies the value to the
buffer regardless of the number of bytes in the value. If you pass 0,
you can pass VI\_NULL for the **Attribute\_Value** buffer parameter.
''',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
The buffer in which the function returns the current value of the
attribute. The buffer must be of type ViChar and have at least as many
bytes as indicated in the **Buffer\_Size** parameter.

If you specify 0 for the **Buffer\_Size** parameter, you can pass
VI\_NULL for this parameter.
''',
                'name': 'attributeValue',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetAutoRangeValue': {
        'purpose': '''
Returns the **Actual\_Range** that the DMM is using, even when Auto
Range is off.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates the **actualRange** the DMM is using. Returns the value of the
`
NIDMM\_ATTR\_AUTO\_RANGE\_VALUE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_RANGE_VALUE.html')>`__
attribute. The units of the returned value depend on the function.
''',
                'name': 'actualRange',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'GetCalCount': {
        'long_description': '''
+----------+----------------------------------------------------------------------------+
| |Note|   | **Note**  The NI 4050, NI 4060, and NI 4080/4081/4082 are not supported.   |
+----------+----------------------------------------------------------------------------+

.. |Note| image:: note.gif
''',
        'purpose': '''
Returns the calibration **Count** for the specified type of calibration.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the type of calibration performed (external or
self-calibration).
+--------------------------+--------------------------+--------------------------+
| NIDMM\_VAL\_INTERNAL\_AR | 0                        | Self-Calibration         |
| EA (default)             |                          |                          |
| +----------+------------ |                          |                          |
| ------------------------ |                          |                          |
| ------------------------ |                          |                          |
| +                        |                          |                          |
| | |Note|   | **Note**  T |                          |                          |
| he NI 4065 does not supp |                          |                          |
| ort self-calibration.    |                          |                          |
| |                        |                          |                          |
| +----------+------------ |                          |                          |
| ------------------------ |                          |                          |
| ------------------------ |                          |                          |
| +                        |                          |                          |
+--------------------------+--------------------------+--------------------------+
| NIDMM\_VAL\_EXTERNAL\_AR | 1                        | External Calibration     |
| EA                       |                          |                          |
+--------------------------+--------------------------+--------------------------+

.. |Note| image:: note.gif
''',
                'name': 'calType',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
The number of times calibration has been performed.
''',
                'name': 'count',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetCalDateAndTime': {
        'long_description': '''
+----------+--------------------------------------------------------+
| |Note|   | **Note**  The NI 4050 and NI 4060 are not supported.   |
+----------+--------------------------------------------------------+

.. |Note| image:: note.gif
''',
        'purpose': '''
Returns the date and time of the last calibration performed.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the type of calibration performed (external or
self-calibration).
+--------------------------+--------------------------+--------------------------+
| NIDMM\_VAL\_INTERNAL\_AR | 0                        | Self-Calibration         |
| EA (default)             |                          |                          |
| +----------+------------ |                          |                          |
| ------------------------ |                          |                          |
| ------------------------ |                          |                          |
| +                        |                          |                          |
| | |Note|   | **Note**  T |                          |                          |
| he NI 4065 does not supp |                          |                          |
| ort self-calibration.    |                          |                          |
| |                        |                          |                          |
| +----------+------------ |                          |                          |
| ------------------------ |                          |                          |
| ------------------------ |                          |                          |
| +                        |                          |                          |
+--------------------------+--------------------------+--------------------------+
| NIDMM\_VAL\_EXTERNAL\_AR | 1                        | External Calibration     |
| EA                       |                          |                          |
+--------------------------+--------------------------+--------------------------+

.. |Note| image:: note.gif
''',
                'name': 'calType',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates the **month** of the last calibration.
''',
                'name': 'month',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates the **day** of the last calibration.
''',
                'name': 'day',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates the **year** of the last calibration.
''',
                'name': 'year',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates the **hour** of the last calibration.
''',
                'name': 'hour',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates the **minute** of the last calibration.
''',
                'name': 'minute',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetCalUserDefinedInfo': {
        'long_description': '''
+----------+--------------------------------------------------------+
| |Note|   | **Note**  The NI 4050 and NI 4060 are not supported.   |
+----------+--------------------------------------------------------+

.. |Note| image:: note.gif
''',
        'purpose': '''
Returns the user-defined calibration information stored in the EEPROM.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Passes the number of bytes in the ViString you specify for the **Info**
parameter.

If zero is passed for this parameter, the **bufferSize** needed to store
the information is returned. If the Info parameter, including the
terminating NULL byte, contains more bytes than you indicate in this
parameter, the function copies **bufferSize** - 1 bytes into the buffer,
places an ASCII NULL byte at the end of the buffer, and returns the
**bufferSize** you must pass to get the entire value.

For example, if the value is "123456" and the **bufferSize** is 4, the
function places "123" into the buffer and returns 7. If you pass a
negative number, the function copies the value to the buffer regardless
of the number of bytes in the value.
''',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Returns the user-defined calibration information stored in the EEPROM.
If this is NULL, the **Buffer\_Size** needed to store the information is
returned.
''',
                'name': 'info',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetCalUserDefinedInfoMaxSize': {
        'long_description': '''
Purpose
-------

Returns the maximum string length that can be stored in the EEPROM. Use
`
niDMM\_SetCalUserDefinedInfo <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_SetCalUserDefinedInfo.html')>`__
to store user-defined information.

+----------+--------------------------------------------------------+
| |Note|   | **Note**  The NI 4050 and NI 4060 are not supported.   |
+----------+--------------------------------------------------------+

.. |Note| image:: note.gif
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns the value of maximum string length that can be stored in the
EEPROM using `
niDMM\_SetCalUserDefinedInfo <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_SetCalUserDefinedInfo.htm')>`__.
The **infoSize** value is given in characters, but it does not include
the termination character.
''',
                'name': 'infoSize',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetChannelName': {
        'purpose': '''
Returns the **Channel\_String** that is in the channel table at an
**Index** you specify. Not applicable to National Instruments DMMs.
Included for compliance with the *IviDmm Class Specification*.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
A 1–based **index** into the channel table.
''',
                'name': 'index',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Passes the number of bytes in the ViChar array you specify for the
**Channel\_String** parameter. If the next **Channel\_String**,
including the terminating NULL byte, contains more bytes than you
indicate in this parameter, the function copies **bufferSize** –1 bytes
into the buffer, places an ASCII NULL byte at the end of the buffer, and
returns the buffer size you must pass to get the entire value.

For example, if the value is "123456" and the **bufferSize** is 4, the
function places "123" into the buffer and returns 7. If you pass a
negative number, the function copies the value to the buffer regardless
of the number of bytes in the value. If you pass 0, you can pass
VI\_NULL for the **Channel\_String** buffer parameter. The default value
is None.
''',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Returns the **channelString** that is in the channel table at the
**Index** you specify. Do not modify the contents of the
**channelString**.
''',
                'name': 'channelString',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetDevTemp': {
        'long_description': '''
+----------+--------------------------------------------------------+
| |Note|   | **Note**  The NI 4050 and NI 4060 are not supported.   |
+----------+--------------------------------------------------------+

.. |Note| image:: note.gif
''',
        'purpose': '''
Returns the current **Temperature** of the device.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Reserved.
''',
                'name': 'options',
                'type': 'ViString',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns the current **temperature** of the device.
''',
                'name': 'temperature',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'GetError': {
        'purpose': '''
Returns the error information associated with the
**Instrument\_Handle**. This function retrieves and then clears the
error information for the session. If you leave the
**Instrument\_Handle** unwired, this function retrieves and then clears
the error information for the process.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns the **errorCode** for the session or execution thread. If you
pass 0 for the **Buffer\_Size**, you can pass VI\_NULL for this
parameter.
''',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Passes the number of bytes in the ViChar array you specify for the
**Description** parameter. If the error description, including the
terminating NULL byte, contains more bytes than you indicate in this
parameter, the function copies **bufferSize** –1 bytes into the buffer,
places an ASCII NULL byte at the end of the buffer, and returns the
**bufferSize** you must pass to get the entire value.

For example, if the value is "123456" and the **bufferSize** is 4, the
function places "123" into the buffer and returns 7. If you pass a
negative number, the function copies the value to the buffer regardless
of the number of bytes in the value. If you pass 0, you can pass
VI\_NULL for the **Description** buffer parameter. The default value is
None.
''',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Returns the error **description** for the IVI session or execution
thread. If there is no **description**, the function returns an empty
string. The buffer must contain at least as many elements as the value
you specify with the **Buffer\_Size** parameter. If you pass 0 for the
**Buffer\_Size**, you can pass VI\_NULL for this parameter.
''',
                'name': 'description',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetErrorMessage': {
        'long_description': '''
Purpose
-------

Returns the **Error\_Message** as a user-readable string for the
provided **Error\_Code**. Calling this function with a **Buffer\_Size**
of 0 returns the size needed for the **Error\_Message**.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
You can also use VI\_NULL if you do not have a valid **vi**.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
The error code returned from the instrument for which you want to get a
user-readable string.
''',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the number of bytes allocated for the **Error\_Message**
ViChar array. If the error description that this function returns
(including terminating NULL byte) is larger than you indicated in
**buffer\_size**, the error description will be truncated to fit. If you
pass 0 for **buffer\_size**, the function returns the buffer size needed
for **Error\_Message**.
''',
                'name': 'buffer_size',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Contains the error information formatted into a user-readable string.
The buffer must contain at least as many elements as the value you
specify with the **Buffer\_Size** parameter. If you pass 0 for
**Buffer\_Size**, you can pass VI\_NULL for this parameter.
''',
                'name': 'errorMessage',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetExtCalRecommendedInterval': {
        'long_description': '''
+----------+--------------------------------------------------------+
| |Note|   | **Note**  The NI 4050 and NI 4060 are not supported.   |
+----------+--------------------------------------------------------+

.. |Note| image:: note.gif
''',
        'purpose': '''
Returns the recommended interval between external recalibration in
**Months**.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns the recommended number of **months** between external
calibrations.
''',
                'name': 'months',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'GetLastCalTemp': {
        'long_description': '''
+----------+--------------------------------------------------------+
| |Note|   | **Note**  The NI 4050 and NI 4060 are not supported.   |
+----------+--------------------------------------------------------+

.. |Note| image:: note.gif
''',
        'purpose': '''
Returns the **Temperature** during the last calibration procedure.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the type of calibration performed (external or
self-calibration).
+--------------------------+--------------------------+--------------------------+
| NIDMM\_VAL\_INTERNAL\_AR | 0                        | Self-Calibration         |
| EA (default)             |                          |                          |
| +----------+------------ |                          |                          |
| ------------------------ |                          |                          |
| ------------------------ |                          |                          |
| +                        |                          |                          |
| | |Note|   | **Note**  T |                          |                          |
| he NI 4065 does not supp |                          |                          |
| ort self-calibration.    |                          |                          |
| |                        |                          |                          |
| +----------+------------ |                          |                          |
| ------------------------ |                          |                          |
| ------------------------ |                          |                          |
| +                        |                          |                          |
+--------------------------+--------------------------+--------------------------+
| NIDMM\_VAL\_EXTERNAL\_AR | 1                        | External Calibration     |
| EA                       |                          |                          |
+--------------------------+--------------------------+--------------------------+

.. |Note| image:: note.gif
''',
                'name': 'calType',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns the **temperature** during the last calibration.
''',
                'name': 'temperature',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'GetMeasurementPeriod': {
        'purpose': '''
Returns the measurement **Period**, which is the amount of time it takes
to complete one measurement with the current configuration. Use this
function right before you begin acquiring data—after you have completely
configured the measurement and after all configuration functions have
been called.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns the number of seconds it takes to make one measurement.

The first measurement in a multipoint acquisition requires additional
settling time. This function does not include this additional time or
any `
NIDMM\_ATTR\_TRIGGER\_DELAY <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_TRIGGER_DELAY.html')>`__
associated with the first measurement. Time required for internal
measurements, such as `
NIDMM\_ATTR\_AUTO\_ZERO <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_AUTO_ZERO.html')>`__,
is included.
''',
                'name': 'period',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'GetNextCoercionRecord': {
        'long_description': '''
If you set `
NIDMM\_ATTR\_RECORD\_COERCIONS <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RECORD_COERCIONS.html')>`__
to VI\_TRUE (1), NI-DMM keeps a list of all coercions it makes on
ViInt32 or ViReal64 values that you pass to NI-DMM functions. Use this
function to retrieve information from that list.
''',
        'purpose': '''
This function returns the coercion information associated with the IVI
session, and it retrieves and clears the oldest instance in which NI-DMM
coerced a value you specified to another value.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Passes the number of bytes in the ViChar array you specify for the
**Coercion\_Record** parameter. If the next coercion record string,
including the terminating NULL byte, contains more bytes than you
indicate in this parameter, the function copies **bufferSize** – 1 bytes
into the buffer, places an ASCII NULL byte at the end of the buffer, and
returns the buffer size you must pass to get the entire value.

For example, if the value is "123456" and the **bufferSize** is 4, the
function places "123" into the buffer and returns 7. If you pass a
negative number, the function copies the value to the buffer regardless
of the number of bytes in the value.

If you pass 0, you can pass VI\_NULL for the **Coercion\_Record** buffer
parameter.

The default value is None.
''',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Returns the next **coercionRecord** for the IVI session.

If there are no coercions records, the function returns an empty string.
The buffer must contain at least as many elements as the value you
specify with the **Buffer\_Size** parameter.
''',
                'name': 'coercionRecord',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetNextInterchangeWarning': {
        'long_description': '''
The driver performs interchangeability checking when `
NIDMM\_ATTR\_INTERCHANGE\_CHECK <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_INTERCHANGE_CHECK.html')>`__
is set to VI\_TRUE (1). The function returns an empty string in the
**Interchange\_Warning** parameter if no interchangeability warnings
remain for the session. In general, the instrument driver generates
interchangeability warnings when an attribute that affects the behavior
of the instrument is in a state that you did not specify.
''',
        'purpose': '''
This function returns the interchangeability warnings associated with
the IVI session. It retrieves and clears the oldest instance in which
the class driver recorded an interchangeability warning.
Interchangeability warnings indicate that using your application with a
different instrument might cause different behavior.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Passes the number of bytes in the ViChar array you specify for the
**Interchange\_Warning** parameter. If the next interchangeability
warning string, including the terminating NULL byte, contains more bytes
than you indicate in this parameter, the function copies
**bufferSize** –1 bytes into the buffer, places an ASCII NULL byte at
the end of the buffer, and returns the buffer size you must pass to get
the entire value.

For example, if the value is "123456" and the **bufferSize** is 4, the
function places "123" into the buffer and returns 7. If you pass a
negative number, the function copies the value to the buffer regardless
of the number of bytes in the value. If you pass 0, you can pass
VI\_NULL for the **Interchange\_Warning** buffer parameter. The default
value is None.
''',
                'name': 'bufferSize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Returns the next interchange warning for the IVI session. If there are
no interchange warnings, the function returns an empty string. The
buffer must contain at least as many elements as the value you specify
with the **Buffer\_Size** parameter.
''',
                'name': 'interchangeWarning',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'GetSelfCalSupported': {
        'purpose': '''
Returns a Boolean value that expresses whether or not the DMM that you
are using can perform self-calibration.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns whether Self Cal is supported for the device specified by the
given session.
+-------------+-----+---------------------------------------------------------------+
| VI\_TRUE    | 1   | The DMM that you are using can perform self-calibration.      |
+-------------+-----+---------------------------------------------------------------+
| VI\_FALSE   | 0   | The DMM that you are using cannot perform self-calibration.   |
+-------------+-----+---------------------------------------------------------------+
''',
                'name': 'selfCalSupported',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'InitExtCal': {
        'long_description': '''
-  Creates a new session for external calibration to the device you
   specify for the **Resource\_Name** parameter.
-  Resets the device and prepares the EEPROM for new calibration
   coefficients.
-  Returns a ViSession handle that you use to identify the instrument in
   all calibration adjustments and post-adjustment verification steps.

+------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Notes**   | The NI 4050 and NI 4060 are not supported.                                                                                                                                                                                                                                                                                              |
|            |             | Refer to the *NI 4065 6½ Digit DMM Calibration Procedure*, the *NI 4070/4072 6½ Digit FlexDMM Calibration Procedure*, or the *NI 4071 7½–Digit FlexDMM Calibration Procedure* before using this function.                                                                                                                               |
|            |             | This function creates a new session the first time you invoke it for a device. If you call this function on the same resource, an error is returned. You should use ` niDMM\_CloseExtCal <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_CloseExtCal.html')>`__ to close a session obtained using this function.   |
+------------+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

After opening a calibration session, the device cannot take valid
measurements using this session until the device has been properly
adjusted. Once the adjustment phase is complete, you can use this
session to verify the new calibration constants. After verification, you
have the option of saving the new calibration constants or reverting to
the previous calibration constants by specifying the **Action**
parameter in `
niDMM\_CloseExtCal <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_CloseExtCal.html')>`__.

If you encounter a fatal error such as a power failure or system crash
while performing an external calibration, you can call `
niDMM\_RestoreLastExtCalConstants <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_RestoreLastExtCalConstants.html')>`__
to return the device to a usable state.

.. |image0| image:: note.gif
''',
        'purpose': '''
The following operations are performed if the **Calibration\_Password**
is valid:
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
| Contains the **resourceName** of the device to initialize. The
  **resourceName** is assigned in Measurement & Automation Explorer
  (MAX). Refer to `Related
  Documentation <javascript:LaunchHelp('dmm.chm::/related_documentation.html')>`__
  for the *NI Digital Multimeters Getting Started Guide* for more
  information about configuring and testing the DMM in MAX.
| Valid Syntax:

-  NI-DAQmx name
-  DAQ::NI-DAQmx name[::INSTR]
-  DAQ::Traditional NI-DAQ device number[::INSTR]
-  IVI logical name

.. caution::   All IVI names for the **resourceName**, such as logical
names or virtual names, are case-sensitive. If you use logical names,
driver session names, or virtual names in your program, you must make
sure that the name you use matches the name in the IVI Configuration
Store file exactly, without any variations in the case of the characters
in the name.
''',
                'name': 'resourceName',
                'type': 'ViString',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'long_description': '''
Specifies the password required to enable external calibration
functionality.

The maximum password string length is eight characters, excluding the
termination character. "NI" is the factory-default password.
''',
                'name': 'calibrationPassword',
                'type': 'ViChar',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
The session handle that you obtain from niDMM\_InitExtCal. The handle
identifies a particular instrument calibration session.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'InitWithOptions': {
        'long_description': '''
-  Creates a new IVI instrument driver session and, optionally, sets the
   initial state of the following session attributes: `
   RangeCheck <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RANGE_CHECK.html')>`__,
   `
   QueryInstrStatus <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_QUERY_INSTR_STATUS.html')>`__,
   `
   Cache <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_CACHE.html')>`__,
   `
   Simulate <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_SIMULATE.html')>`__,
   `
   Recordcoercions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'caNIDMM_ATTR_RECORD_COERCIONS.html')>`__.
-  Opens a session to the device you specify for the **Resource\_Name**
   parameter. If the **ID\_Query** parameter is set to VI\_TRUE, this
   function queries the instrument ID and checks that it is valid for
   this instrument driver.
-  If the **Reset\_Device** parameter is set to VI\_TRUE, this function
   resets the instrument to a known state. Sends initialization commands
   to set the instrument to the state necessary for the operation of the
   instrument driver.
-  Returns a ViSession handle that you use to identify the instrument in
   all subsequent instrument driver function calls.
''',
        'purpose': '''
This function completes the following tasks:
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
| Contains the **resourceName** of the device to initialize. The
  **resourceName** is assigned in Measurement & Automation Explorer
  (MAX). Refer to `Related
  Documentation <javascript:LaunchHelp('dmm.chm::/related_documentation.html')>`__
  for the *NI Digital Multimeters Getting Started Guide* for more
  information about configuring and testing the DMM in MAX.
| Valid Syntax:

-  NI-DAQmx name
-  DAQ::NI-DAQmx name[::INSTR]
-  DAQ::Traditional NI-DAQ device number[::INSTR]
-  IVI logical name

.. caution::   All IVI names for the **resourceName**, such as logical
names or virtual names, are case-sensitive. If you use logical names,
driver session names, or virtual names in your program, you must make
sure that the name you use matches the name in the IVI Configuration
Store file exactly, without any variations in the case of the characters
in the name.
''',
                'name': 'resourceName',
                'type': 'ViString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Verifies that the device you initialize is one that the driver supports.
NI-DMM automatically performs this query, so setting this parameter is
not necessary.
Defined Values:
+----------------------+-----+--------------------+
| VI\_TRUE (default)   | 1   | Perform ID Query   |
+----------------------+-----+--------------------+
| VI\_FALSE            | 0   | Skip ID Query      |
+----------------------+-----+--------------------+
''',
                'name': 'idQuery',
                'type': 'ViBoolean',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies whether to reset the instrument during the initialization
procedure.
Defined Values:
+----------------------+-----+----------------+
| VI\_TRUE (default)   | 1   | Reset Device   |
+----------------------+-----+----------------+
| VI\_FALSE            | 0   | Don't Reset    |
+----------------------+-----+----------------+
''',
                'name': 'resetDevice',
                'type': 'ViBoolean',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
| Sets the initial value of certain attributes for the session. The
  following table specifies the attribute name, attribute constant, and
  default value for each attribute that you can use in this parameter:

+--------------------+-------------------------------------+---------------------+------+
| Check              | NIDMM\_ATTR\_RANGE\_CHECK           | VI\_TRUE            | 1    |
+--------------------+-------------------------------------+---------------------+------+
| QueryInstrStatus   | NIDMM\_ATTR\_QUERY\_INSTR\_STATUS   | VI\_FALSE           | 0    |
+--------------------+-------------------------------------+---------------------+------+
| Cache              | NIDMM\_ATTR\_CACHE                  | VI\_TRUE            | 1    |
+--------------------+-------------------------------------+---------------------+------+
| Simulate           | NIDMM\_ATTR\_SIMULATE               | VI\_FALSE           | 0    |
+--------------------+-------------------------------------+---------------------+------+
| RecordCoercions    | NIDMM\_ATTR\_RECORD\_COERCIONS      | VI\_FALSE           | 0    |
+--------------------+-------------------------------------+---------------------+------+
| DriverSetup        | NIDMM\_ATTR\_DRIVER\_SETUP          | "" (empty string)   | ""   |
+--------------------+-------------------------------------+---------------------+------+

The format of this string is, "AttributeName=Value." To set multiple
attributes, separate their assignments with a comma.

If you pass NULL or an empty string for this parameter, the session uses
the default values for the attributes. You can override the default
values by assigning a value explicitly in an **optionString** parameter.
You do not have to specify all of the attributes and may leave any of
them out (those left out use the default value).

Refer to `Simulating NI Digital
Multimeters <javascript:LaunchHelp('dmm.chm::/simulation.html')>`__ for
more information.
''',
                'name': 'optionString',
                'type': 'ViString',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns a ViSession handle that you use to identify the instrument in
all subsequent instrument driver function calls.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'Initiate': {
        'long_description': '''
Purpose
-------

Initiates an acquisition. After you call this function, the DMM leaves
the Idle state and enters the Wait-for-Trigger state. If trigger is set
to Immediate mode, the DMM begins acquiring measurement data. Use `
niDMM\_Fetch <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_Fetch.html')>`__,
`
niDMM\_FetchMultiPoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_FetchMultiPoint.html')>`__,
or `
niDMM\_FetchWaveform <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_FetchWaveform.html')>`__
to retrieve the measurement data.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'IsOverRange': {
        'purpose': '''
Takes a **Measurement\_Value** and determines if the value is a valid
measurement or a value indicating that an overrange condition occurred.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
The measured value returned from the DMM.
+------------+----------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**   If an overrange condition occurs, the **measurementValue** contains an IEEE-defined NaN (Not a Number) value.   |
+------------+----------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'measurementValue',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns whether the measurement value is a valid measurement or an
overrange condition.
+-------------+-----+-------------------------------------------------------------+
| VI\_TRUE    | 1   | The value indicates that an overrange condition occurred.   |
+-------------+-----+-------------------------------------------------------------+
| VI\_FALSE   | 0   | The value is a valid measurement.                           |
+-------------+-----+-------------------------------------------------------------+
''',
                'name': 'isOverRange',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'IsUnderRange': {
        'purpose': '''
Takes a **Measurement\_Value** and determines if the value is a valid
measurement or a value indicating that an underrange condition occurred.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
The measured value returned from the DMM.
+------------+----------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**   If an overrange condition occurs, the **measurementValue** contains an IEEE-defined NaN (Not a Number) value.   |
+------------+----------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'measurementValue',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns whether the **Measurement\_Value** is a valid measurement or an
underrange condition.
+-------------+-----+--------------------------------------------------------------+
| VI\_TRUE    | 1   | The value indicates that an underrange condition occurred.   |
+-------------+-----+--------------------------------------------------------------+
| VI\_FALSE   | 0   | The value is a valid measurement.                            |
+-------------+-----+--------------------------------------------------------------+
''',
                'name': 'isUnderRange',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'LockSession': {
        'long_description': '''
Other threads might have obtained a lock on this session in the
following ways:

-  The user application called this function.
-  A call to the instrument driver locked the session.
-  A call to the IVI Library locked the session.

After your call to this function returns successfully, no other threads
can access the instrument session until you call `
niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__.

Use this function and `
niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__
around a sequence of calls to instrument driver functions if you require
that the instrument retain its settings through the end of the sequence.
You can safely make nested calls to this function within the same
thread.

To completely unlock the session, you must balance each call to this
function with a call to `
niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__.
If, however, you use the **Caller\_Has\_Lock** parameter in all calls to
this function and `
niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__
within a function, the IVI Library locks the session only once within
the function regardless of the number of calls you make to this
function. This feature allows you to call `
niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__
just once at the end of the function.
''',
        'purpose': '''
This function obtains a multithread lock on the instrument session.
Before it does so, it waits until all other execution threads have
released their locks on the instrument session.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
This parameter serves as a convenience. If you do not want to use this
parameter, pass VI\_NULL. Use this parameter in complex functions to
keep track of whether you obtain a lock and, therefore, need to unlock
the session. To use this parameter, complete the following steps:

#. Pass the address of a local ViBoolean variable.
#. In the declaration of the local variable, initialize it to VI\_FALSE
   (0).
#. Pass the address of the same local variable to any other calls you
   make to this function or `
   niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__
   in the same function.

The parameter is an input/output parameter. This function and `
niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__
each inspect the current value and take the following actions:

If the value is VI\_TRUE (1), this function does not lock the session
again. If the value is VI\_FALSE, this function obtains the lock and
sets the value of the parameter to VI\_TRUE.

If the value is VI\_FALSE, `
niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__
does not attempt to unlock the session. If the value is VI\_TRUE, `
niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__
releases the lock and sets the value of the parameter to VI\_FALSE.
Thus, you can, call `
niDMM\_UnlockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_UnlockSession.html')>`__
at the end of your function without worrying about whether you actually
have the lock.

**Example**

ViStatus TestFunc (ViSession vi, ViInt32 flags)

{

| ViStatus error = VI\_SUCCESS;
| ViBoolean haveLock = VI\_FALSE;
| if (flags & BIT\_1)

| {
| viCheckErr( NIDMM\_LockSession(vi, &haveLock;));
| viCheckErr( TakeAction1(vi));
| if (flags & BIT\_2)

{

viCheckErr( NIDMM\_UnlockSession(vi, &haveLock;));

viCheckErr( TakeAction2(vi));

viCheckErr( NIDMM\_LockSession(vi, &haveLock;);

}

if (flags & BIT\_3)

viCheckErr( TakeAction3(vi));

}

Error:

/\*

At this point, you cannot really be sure that you have the lock.
Fortunately, the haveLock variable takes care of that for you.

\*/

niDMM\_UnlockSession(vi, &haveLock;);

return error;

}
''',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'PerformOpenCableComp': {
        'long_description': '''
Purpose
-------

For the NI 4082 and NI 4072 only, performs the open cable compensation
measurements for the current capacitance/inductance range, and returns
open cable compensation **Conductance** and **Susceptance** values. You
can use the return values of this function as inputs to `
niDMM\_ConfigureOpenCableCompValues <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_ConfigureOpenCableCompValues.html')>`__.

This function returns an error if the value of the `
NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_FUNCTION.html')>`__
attribute is not set to NIDMM\_VAL\_CAPACITANCE (1005) or
NIDMM\_VAL\_INDUCTANCE (1006).
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
**conductance** is the measured value of open cable compensation
**conductance**.
''',
                'name': 'conductance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
**susceptance** is the measured value of open cable compensation
**susceptance**.
''',
                'name': 'susceptance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'PerformShortCableComp': {
        'long_description': '''
Purpose
-------

Performs the short cable compensation measurements for the current
capacitance/inductance range, and returns short cable compensation
**Resistance** and **Reactance** values. You can use the return values
of this function as inputs to `
niDMM\_ConfigureShortCableCompValues <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'cviniDMM_ConfigureShortCableCompValues.html')>`__.

This function returns an error if the value of the `
NIDMM\_ATTR\_FUNCTION <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_FUNCTION.html')>`__
attribute is not set to NIDMM\_VAL\_CAPACITANCE (1005) or
NIDMM\_VAL\_INDUCTANCE (1006).
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
**resistance** is the measured value of short cable compensation
**resistance**.
''',
                'name': 'resistance',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
**reactance** is the measured value of short cable compensation
**reactance**.
''',
                'name': 'reactance',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'Read': {
        'purpose': '''
Acquires a single measurement and returns the measured value.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **maximumTime** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
The measured value returned from the DMM.
''',
                'name': 'reading',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'ReadMultiPoint': {
        'purpose': '''
Acquires multiple measurements and returns an array of measured values.
The number of measurements the DMM makes is determined by the values you
specify for the **Trigger\_Count** and **Sample\_Count** parameters in `
niDMM\_ConfigureMultiPoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureMultiPoint.html')>`__.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **maximumTime** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the number of measurements to acquire. The maximum number of
measurements for a finite acquisition is the (**Trigger Count** x
**Sample Count**) parameters in `
niDMM\_ConfigureMultiPoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureMultiPoint.html')>`__.

For continuous acquisitions, up to 100,000 points can be returned at
once. The number of measurements can be a subset. The valid range is any
positive ViInt32. The default value is 1.
''',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
An array of measurement values.
+------------+-----------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**   The size of the **readingArray** must be at least the size that you specify for the **Array\_Size** parameter.   |
+------------+-----------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'readingArray',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates the number of measured values actually retrieved from the DMM.
''',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ReadStatus': {
        'long_description': '''
+----------+-------------------------------------------+
| |Note|   | **Note**  The NI 4050 is not supported.   |
+----------+-------------------------------------------+

.. |Note| image:: note.gif
''',
        'purpose': '''
Returns measurement backlog and acquisition status. Use this function to
determine how many measurements are available before calling `
niDMM\_Fetch <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_Fetch.html')>`__,
`
niDMM\_FetchMultipoint <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_FetchMultiPoint.html')>`__,
or `
niDMM\_FetchWaveform <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_FetchWaveform.html')>`__.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
The number of measurements available to be read. If the backlog
continues to increase, data is eventually overwritten, resulting in an
error.
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |Note|   | **Note**  On the NI 4060, the **Backlog** does not increase when autoranging. On the NI 4065, the **Backlog** does not increase when Range is set to AUTO RANGE ON (-1), or before the first point is fetched when Range is set to AUTO RANGE ONCE (-3). These behaviors are due to the autorange model of the devices.   |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |Note| image:: note.gif
''',
                'name': 'acquisitionBacklog',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates status of the acquisition. The following table shows the
acquisition states:
+-----+------------------------------+
| 0   | Running                      |
+-----+------------------------------+
| 1   | Finished with backlog        |
+-----+------------------------------+
| 2   | Finished with no backlog     |
+-----+------------------------------+
| 3   | Paused                       |
+-----+------------------------------+
| 4   | No acquisition in progress   |
+-----+------------------------------+
''',
                'name': 'acquisitionStatus',
                'type': 'ViInt16',
                'enum': None,
            },
        ],
    },
    'ReadWaveform': {
        'purpose': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
and returns data as an array of values or as a waveform data type. The
number of elements in the **Waveform\_Array** is determined by the
values you specify for the **Waveform\_Points** parameter in `
niDMM\_ConfigureWaveformAcquisition <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureWaveformAcquisition.html')>`__.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the **maximumTime** allowed for this function to complete in
milliseconds. If the function does not complete within this time
interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
error code. This may happen if an external trigger has not been
received, or if the specified timeout is not long enough for the
acquisition to complete.

The valid range is 0–86400000. The default value is
NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
automatically.
''',
                'name': 'maximumTime',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies the number of waveform points to return. You specify the total
number of points that the DMM acquires in the **Waveform Points**
parameter of `
niDMM\_ConfigureWaveformAcquisition <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ConfigureWaveformAcquisition.html')>`__.
The default value is 1.
''',
                'name': 'arraySize',
                'type': 'ViInt32',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
An array of measurement values.
+------------+------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**   The size of the **waveformArray** must be at least the size that you specify for the **Array\_Size** parameter.   |
+------------+------------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'waveformArray',
                'type': 'ViReal64',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Indicates the number of measured values actually retrieved from the DMM.
''',
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'ResetInterchangeCheck': {
        'long_description': '''
If a particular test module does not completely configure the state of
an instrument, the state of the instrument depends on the configuration
from a previously executed test module. If you execute the test modules
in a different order, the behavior of the instrument and therefore the
entire test module is likely to change. This change in behavior is
generally instrument specific and represents an interchangeability
problem. You can use this function to test for such cases. After you
call this function, the interchangeability checking algorithms in NI-DMM
ignore all previous configuration operations. By calling this function
at the beginning of a test module, you can determine whether the test
module has dependencies on the operation of previously executed test
modules.

This function does not clear the interchangeability warnings from the
list of previously recorded interchangeability warnings. If you want to
guarantee that `
niDMM\_GetNextInterchangeWarning <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_GetNextInterchangeWarning.html')>`__
only returns those interchangeability warnings that are generated after
calling this function, you must clear the list of interchangeability
warnings. You can clear the interchangeability warnings list by
repeatedly calling `
niDMM\_GetNextInterchangeWarning <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_GetNextInterchangeWarning.html')>`__
until no more interchangeability warnings are returned. If you are not
interested in the content of those warnings, you can call `
niDMM\_ClearInterchangeWarnings <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_ClearInterchangeWarnings.html')>`__.
''',
        'purpose': '''
When developing a complex test system that consists of multiple test
modules, it is generally a good idea to design the test modules so that
they can run in any order. To do so requires ensuring that each test
module completely configures the state of each instrument it uses.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'ResetWithDefaults': {
        'purpose': '''
Resets the instrument to a known state and sends initialization commands
to the DMM. The initialization commands set the DMM settings to the
state necessary for the operation of NI-DMM. All user-defined default
values associated with a logical name are applied after setting the DMM.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'RestoreLastExtCalConstants': {
        'long_description': '''
After calling this function, you should call `
niDMM\_SelfCal <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_SelfCal.html')>`__
before taking measurements with the device to adjust the device for any
temperature drifts since the last external calibration.

+----------+----------------------------------------------------------------------------+
| |Note|   | **Note**  The NI 4050, NI 4060, and NI 4080/4081/4082 are not supported.   |
+----------+----------------------------------------------------------------------------+

.. |Note| image:: note.gif
''',
        'purpose': '''
Reverts the device to the calibration constants from the last complete
external calibration. This function recovers the hardware if a fatal
system error should occur during an external or self-calibration
procedure.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'SelfCal': {
        'long_description': '''
+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**  This function calls ` niDMM\_reset <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_reset.html')>`__, and any configurations previous to the call will be lost. All attributes will be set to their default values after the call returns.   |
+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
        'purpose': '''
For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
self-calibration routine to maintain measurement accuracy.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'SendSoftwareTrigger': {
        'long_description': '''
Purpose
-------

Sends a command to trigger the DMM. Call this function if you have
configured either the `
NIDMM\_ATTR\_TRIGGER\_SOURCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_TRIGGER_SOURCE.html')>`__
or `
NIDMM\_ATTR\_SAMPLE\_TRIGGER <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_SAMPLE_TRIGGER.html')>`__
attributes. If the `
NIDMM\_ATTR\_TRIGGER\_SOURCE <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_TRIGGER_SOURCE.html')>`__
and/or `
NIDMM\_ATTR\_SAMPLE\_TRIGGER <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20%0A'caNIDMM_ATTR_SAMPLE_TRIGGER.html')>`__
attributes are set to NIDMM\_VAL\_EXTERNAL or NIDMM\_VAL\_TTL\ *n*, you
can use this function to override the trigger source that you configured
and trigger the device. The NI 4050 and NI 4060 are not supported.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'SetAttributeViBoolean': {
        'long_description': '''
This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid
   or is different than the value you specify.

This instrument driver contains high-level functions that set most of
the instrument attributes. It is best to use the high-level driver
functions as much as possible. They handle order dependencies and
multithread locking for you. In addition, they perform status checking
only after setting all of the attributes.

In contrast, when you set multiple attributes using the SetAttribute
functions, the functions check the instrument status after each call.
Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
''',
        'purpose': '''
This function sets the value of a ViBoolean attribute.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the value that you want to set the attribute to.
''',
                'name': 'attributeValue',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'SetAttributeViInt32': {
        'long_description': '''
This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid
   or is different than the value you specify.

This instrument driver contains high-level functions that set most of
the instrument attributes. It is best to use the high-level driver
functions as much as possible. They handle order dependencies and
multithread locking for you. In addition, they perform status checking
only after setting all of the attributes.

In contrast, when you set multiple attributes using the SetAttribute
functions, the functions check the instrument status after each call.
Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
''',
        'purpose': '''
This function sets the value of a ViInt32 attribute.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the value that you want to set the attribute to.
''',
                'name': 'attributeValue',
                'type': 'ViInt32',
                'enum': None,
            },
        ],
    },
    'SetAttributeViReal64': {
        'long_description': '''
This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid
   or is different than the value you specify.

This instrument driver contains high-level functions that set most of
the instrument attributes. It is best to use the high-level driver
functions as much as possible. They handle order dependencies and
multithread locking for you. In addition, they perform status checking
only after setting all of the attributes.

In contrast, when you set multiple attributes using the SetAttribute
functions, the functions check the instrument status after each call.
Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
''',
        'purpose': '''
This function sets the value of a ViReal64 attribute.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the value that you want to set the attribute to.
''',
                'name': 'attributeValue',
                'type': 'ViReal64',
                'enum': None,
            },
        ],
    },
    'SetAttributeViSession': {
        'long_description': '''
Purpose
-------

This function sets the value of a ViSession attribute.

This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid
   or is different than the value you specify.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the value that you want to set the attribute to.
''',
                'name': 'attributeValue',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'SetAttributeViString': {
        'long_description': '''
This is a low-level function that you can use to set the values of
instrument-specific attributes and inherent IVI attributes.

If the attribute represents an instrument state, this function performs
instrument I/O in the following cases:

-  State caching is disabled for the entire session or for the
   particular attribute.
-  State caching is enabled, and the currently cached value is invalid
   or is different than the value you specify.

This instrument driver contains high-level functions that set most of
the instrument attributes. It is best to use the high-level driver
functions as much as possible. They handle order dependencies and
multithread locking for you. In addition, they perform status checking
only after setting all of the attributes.

In contrast, when you set multiple attributes using the SetAttribute
functions, the functions check the instrument status after each call.
Also, when state caching is enabled, the high-level functions that
configure multiple attributes perform instrument I/O only for the
attributes whose value you change. Thus, you can safely call the
high-level functions without the penalty of redundant instrument I/O.
''',
        'purpose': '''
This function sets the value of a ViString attribute.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
This parameter is ignored. National Instruments DMMs do not support
channel names since they only have a single channel. This parameter is
included in order to support interchangeability and upgradability to
multiple channel DMMs.

The default value is " " (an empty string).
''',
                'name': 'channelName',
                'type': 'ViConstString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Pass the ID of an attribute.
''',
                'name': 'attributeId',
                'type': 'ViAttr',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'long_description': '''
Pass the value that you want to set the attribute to.
''',
                'name': 'attributeValue',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'SetCalPassword': {
        'long_description': '''
+------------+---------------+---------------------------------------------------------------------------------------------------------+
| |image0|   | **Notes**     | The NI 4050 and NI 4060 are not supported.                                                              |
|            |               | A password is required for external calibration. Be sure to record the password in a secure location.   |
+------------+---------------+---------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
        'purpose': '''
Changes the password required to enable external calibration
functionality for the specified instrument. The maximum password string
length is eight characters, excluding the termination character. "NI" is
the default password.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'long_description': '''
Specifies the current password required to enable external calibration
functionality. The maximum password string length is eight characters,
excluding the termination character.
''',
                'name': 'oldPassword',
                'type': 'ViChar',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'long_description': '''
Specifies the **newPassword** required to enable external calibration
functionality. The maximum password string length is eight characters,
excluding the termination character.
''',
                'name': 'newPassword',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'SetCalUserDefinedInfo': {
        'long_description': '''
Purpose
-------

Stores the user-defined information in the EEPROM. Use `
niDMM\_GetCalUserDefinedInfoMaxSize <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_GetCalUserDefinedInfoMaxSize.html')>`__
to learn the maximum string size that is allowed. If the **Info** string
size is larger than the maximum string size, NI-DMM stores as much of
the information as possible, truncates the remainder, and returns a
warning.

+----------+--------------------------------------------------------+
| |Note|   | **Note**  The NI 4050 and NI 4060 are not supported.   |
+----------+--------------------------------------------------------+

.. |Note| image:: note.gif
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'is_buffer': True,
                'long_description': '''
Specifies the user-defined information to be stored in the EEPROM such
as the operator who performed the calibration operation or system
information. Use `
niDMM\_GetCalUserDefinedinfoMaxSize <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_GetCalUserDefinedinfoMaxSize.html')>`__
to learn the maximum string size that is allowed. If the **info** string
size is larger than the maximum string size, NI-DMM stores as much of
the information as possible, truncates the remainder, and return a
warning.
''',
                'name': 'info',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'UnlockSession': {
        'purpose': '''
This function releases a lock that you acquired on an instrument session
using niDMM\_LockSession. Refer to `
niDMM\_LockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_LockSession.html')>`__
for additional information on session locks.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
This parameter serves as a convenience. If you do not want to use this
parameter, pass VI\_NULL.

Use this parameter in complex functions to keep track of whether you
obtain a lock and, therefore, need to unlock the session.

To use this parameter, complete the following steps:

#. Pass the address of a local ViBoolean variable.
#. In the declaration of the local variable, initialize it to VI\_FALSE
   (0).
#. Pass the address of the same local variable to any other calls you
   make to `
   niDMM\_LockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_LockSession.html')>`__
   or this function in the same function.

The parameter is an input/output parameter. `
niDMM\_LockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_LockSession.html')>`__
and this function each inspect the current value and take the following
actions:

If the value is VI\_TRUE (1), `
niDMM\_LockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_LockSession.html')>`__
does not lock the session again. If the value is VI\_FALSE, `
niDMM\_LockSession <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_LockSession.html')>`__
obtains the lock and sets the value of the parameter to VI\_TRUE.

If the value is VI\_FALSE, this function does not attempt to unlock the
session. If the value is VI\_TRUE, this function releases the lock and
sets the value of the parameter to VI\_FALSE. Thus, you can, call this
function at the end of your function without worrying about whether you
actually have the lock.

**Example**

ViStatus TestFunc (ViSession vi, ViInt32 flags)

{

ViStatus error = VI\_SUCCESS;

ViBoolean haveLock = VI\_FALSE;

if (flags & BIT\_1)

{

viCheckErr( NIDMM\_LockSession(vi, &haveLock;));

viCheckErr( TakeAction1(vi));

if (flags & BIT\_2)

{

viCheckErr( NIDMM\_UnlockSession(vi, &haveLock;));

viCheckErr( TakeAction2(vi));

viCheckErr( NIDMM\_LockSession(vi, &haveLock;);

}

if (flags & BIT\_3)

viCheckErr( TakeAction3(vi));

}

Error:

/\*

At this point, you cannot really be sure that you have the lock.
Fortunately, the haveLock variable takes care of that for you.

\*/

niDMM\_UnlockSession(vi, &haveLock;);

return error;

}
''',
                'name': 'callerHasLock',
                'type': 'ViBoolean',
                'enum': None,
            },
        ],
    },
    'close': {
        'long_description': '''
Purpose
-------

Closes the specified session and deallocates resources that it reserved.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'error_message': {
        'purpose': '''
Takes the **Error\_Code** returned by the instrument driver functions,
interprets it, and returns it as a user-readable string.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
The **errorCode** returned from the instrument. The default is 0,
indicating VI\_SUCCESS.
''',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
The error information formatted into a string.
''',
                'name': 'errorMessage',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'error_query': {
        'purpose': '''
Reads an **Error\_Code** and message from the DMM error queue. National
Instruments DMMs do not contain an error queue. Errors are reported as
they occur. Therefore, this function does not detect errors; it is
included for compliance with the *IviDmm Class Specification*.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
The **errorCode** returned from the instrument.

The default value is VI\_SUCCESS (0).
''',
                'name': 'errorCode',
                'type': 'ViStatus',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Formats the **Error\_Code** into a user-readable message string.
+------------+------------------------------------------------------------------------+
| |image0|   | **Note**   The array must contain at least 256 elements ViChar[256].   |
+------------+------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'errorMessage',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'init': {
        'long_description': '''
-  Creates a new IVI instrument driver session.
-  Opens a session to the device you specify for the **Resource\_Name**
   parameter.

-  If the **ID\_Query** parameter is set to VI\_TRUE (1), this function
   queries the instrument ID and checks that it is valid for this
   instrument driver.

-  If the **Reset\_Device** parameter is set to VI\_TRUE (1), this
   function resets the instrument to a known state. Sends initialization
   commands to set the instrument to the state necessary for the
   operation of the instrument driver.

-  Returns a ViSession handle that you use to identify the instrument in
   all subsequent instrument driver function calls.
''',
        'purpose': '''
This function completes the following tasks:
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
| Contains the **resourceName** of the device to initialize. The
  **resourceName** is assigned in Measurement & Automation Explorer
  (MAX). Refer to `Related
  Documentation <javascript:LaunchHelp('dmm.chm::/related_documentation.html')>`__
  for the *NI Digital Multimeters Getting Started Guide* for more
  information about configuring and testing the DMM in MAX.
| Valid Syntax:

-  NI-DAQmx name
-  DAQ::NI-DAQmx name[::INSTR]
-  DAQ::Traditional NI-DAQ device number[::INSTR]
-  IVI logical name

.. caution::   All IVI names for the **resourceName**, such as logical
names or virtual names, are case-sensitive. If you use logical names,
driver session names, or virtual names in your program, you must make
sure that the name you use matches the name in the IVI Configuration
Store file exactly, without any variations in the case of the characters
in the name.
''',
                'name': 'resourceName',
                'type': 'ViString',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Verifies that the device you initialize is one that the driver supports.
NI-DMM automatically performs this query, so setting this parameter is
not necessary.
Defined Values:
+----------------------+-----+--------------------+
| VI\_TRUE (default)   | 1   | Perform ID Query   |
+----------------------+-----+--------------------+
| VI\_FALSE            | 0   | Skip ID Query      |
+----------------------+-----+--------------------+
''',
                'name': 'idQuery',
                'type': 'ViBoolean',
                'enum': None,
            },
            {
                'direction': 'in',
                'long_description': '''
Specifies whether to reset the instrument during the initialization
procedure.
Defined Values:
+----------------------+-----+----------------+
| VI\_TRUE (default)   | 1   | Reset Device   |
+----------------------+-----+----------------+
| VI\_FALSE            | 0   | Don't Reset    |
+----------------------+-----+----------------+
''',
                'name': 'resetDevice',
                'type': 'ViBoolean',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Returns a ViSession handle that you use to identify the instrument in
all subsequent instrument driver function calls.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'reset': {
        'purpose': '''
Resets the instrument to a known state and sends initialization commands
to the instrument. The initialization commands set instrument settings
to the state necessary for the operation of the instrument driver.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
        ],
    },
    'revision_query': {
        'purpose': '''
Returns the revision numbers of the instrument driver and instrument
firmware.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Returns a string containing the instrument driver software revision
numbers.
+------------+------------------------------------------------------------------------+
| |image0|   | **Note**   The array must contain at least 256 elements ViChar[256].   |
+------------+------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'instrumentDriverRevision',
                'type': 'ViChar',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
Returns a string containing the instrument **firmwareRevision** numbers.
+------------+------------------------------------------------------------------------+
| |image0|   | **Note**   The array must contain at least 256 elements ViChar[256].   |
+------------+------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
                'name': 'firmwareRevision',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
    'self_test': {
        'long_description': '''
+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image0|   | **Note**  This function calls ` niDMM\_reset <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_reset.html')>`__, and any configurations previous to the call will be lost. All attributes will be set to their default values after the call returns.   |
+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image0| image:: note.gif
''',
        'purpose': '''
Performs a self-test on the DMM to ensure that the DMM is functioning
properly. Self-test does not calibrate the DMM.
''',
        'returns': 'ViStatus',
        'codegen_method': 'public',
        'parameters': [
            {
                'direction': 'in',
                'long_description': '''
Identifies a particular instrument session. You obtain the **vi**
parameter from `
niDMM\_init <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_init.html')>`__
or `
niDMM\_InitWithOptions <javascript:LaunchMergedHelp('dmm.chm',%20'dmmcref.chm',%20'cviniDMM_InitWithOptions.html')>`__.
The default is None.
''',
                'name': 'vi',
                'type': 'ViSession',
                'enum': None,
            },
            {
                'direction': 'out',
                'long_description': '''
Contains the value returned from the instrument self-test. Zero
indicates success.

On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
you should check the fuse and replace it, if necessary.

+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |Note|   | **Note**  Self-test does not check the fuse on the NI 4065, NI 4071, and NI 4081. Hence, even if the fuse is blown on the device, self-test does not return error code 1013.   |
+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |Note| image:: note.gif
''',
                'name': 'selfTestResult',
                'type': 'ViInt16',
                'enum': None,
            },
            {
                'direction': 'out',
                'is_buffer': True,
                'long_description': '''
This parameter contains the string returned from the instrument
self-test. The array must contain at least 256 elements.

For the NI 4050 and NI 4060, the error codes returned for self-test
failures include the following:

-  NIDMM\_ERROR\_AC\_TEST\_FAILURE
-  NIDMM\_ERROR\_DC\_TEST\_FAILURE
-  NIDMM\_ERROR\_RESISTANCE\_TEST\_FAILURE

These error codes indicate that the DMM should be repaired.

For the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code
returned for a self-test failure is NIDMM\_ERROR\_SELF\_TEST\_FAILURE.
This error code indicates that the DMM should be repaired.
''',
                'name': 'selfTestMessage',
                'type': 'ViChar',
                'enum': None,
            },
        ],
    },
}
