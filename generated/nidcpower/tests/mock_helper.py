# This file was generated


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['Abort'] = {}
        self._defaults['Abort']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureApertureTime'] = {}
        self._defaults['ConfigureApertureTime']['return'] = 0
        self._defaults['ConfigureDigitalEdgeMeasureTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgePulseTrigger'] = {}
        self._defaults['ConfigureDigitalEdgePulseTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeSourceTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeSourceTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeStartTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] = 0
        self._defaults['CreateAdvancedSequence'] = {}
        self._defaults['CreateAdvancedSequence']['return'] = 0
        self._defaults['CreateAdvancedSequenceStep'] = {}
        self._defaults['CreateAdvancedSequenceStep']['return'] = 0
        self._defaults['DeleteAdvancedSequence'] = {}
        self._defaults['DeleteAdvancedSequence']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['ExportSignal'] = {}
        self._defaults['ExportSignal']['return'] = 0
        self._defaults['FetchMultiple'] = {}
        self._defaults['FetchMultiple']['return'] = 0
        self._defaults['FetchMultiple']['voltageMeasurements'] = None
        self._defaults['FetchMultiple']['currentMeasurements'] = None
        self._defaults['FetchMultiple']['inCompliance'] = None
        self._defaults['FetchMultiple']['actualCount'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViInt64'] = {}
        self._defaults['GetAttributeViInt64']['return'] = 0
        self._defaults['GetAttributeViInt64']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetChannelName']['channelName'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['Code'] = None
        self._defaults['GetError']['Description'] = None
        self._defaults['GetSelfCalLastDateAndTime'] = {}
        self._defaults['GetSelfCalLastDateAndTime']['return'] = 0
        self._defaults['GetSelfCalLastDateAndTime']['Year'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Month'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Day'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Hour'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Minute'] = None
        self._defaults['GetSelfCalLastTemp'] = {}
        self._defaults['GetSelfCalLastTemp']['return'] = 0
        self._defaults['GetSelfCalLastTemp']['Temperature'] = None
        self._defaults['InitializeWithChannels'] = {}
        self._defaults['InitializeWithChannels']['return'] = 0
        self._defaults['InitializeWithChannels']['vi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['Measure'] = {}
        self._defaults['Measure']['return'] = 0
        self._defaults['Measure']['Measurement'] = None
        self._defaults['QueryInCompliance'] = {}
        self._defaults['QueryInCompliance']['return'] = 0
        self._defaults['QueryInCompliance']['inCompliance'] = None
        self._defaults['QueryMaxCurrentLimit'] = {}
        self._defaults['QueryMaxCurrentLimit']['return'] = 0
        self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit'] = None
        self._defaults['QueryMaxVoltageLevel'] = {}
        self._defaults['QueryMaxVoltageLevel']['return'] = 0
        self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel'] = None
        self._defaults['QueryMinCurrentLimit'] = {}
        self._defaults['QueryMinCurrentLimit']['return'] = 0
        self._defaults['QueryMinCurrentLimit']['minCurrentLimit'] = None
        self._defaults['QueryOutputState'] = {}
        self._defaults['QueryOutputState']['return'] = 0
        self._defaults['QueryOutputState']['inState'] = None
        self._defaults['ReadCurrentTemperature'] = {}
        self._defaults['ReadCurrentTemperature']['return'] = 0
        self._defaults['ReadCurrentTemperature']['Temperature'] = None
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['SendSoftwareEdgeTrigger'] = {}
        self._defaults['SendSoftwareEdgeTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViInt64'] = {}
        self._defaults['SetAttributeViInt64']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetSequence'] = {}
        self._defaults['SetSequence']['return'] = 0
        self._defaults['WaitForEvent'] = {}
        self._defaults['WaitForEvent']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['selfTestResult'] = None
        self._defaults['self_test']['selfTestMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niDCPower_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niDCPower_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niDCPower_ConfigureApertureTime(self, vi, channel_name, aperture_time, units):  # noqa: N802
        if self._defaults['ConfigureApertureTime']['return'] != 0:
            return self._defaults['ConfigureApertureTime']['return']
        return self._defaults['ConfigureApertureTime']['return']

    def niDCPower_ConfigureDigitalEdgeMeasureTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return']

    def niDCPower_ConfigureDigitalEdgePulseTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgePulseTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgePulseTrigger']['return']
        return self._defaults['ConfigureDigitalEdgePulseTrigger']['return']

    def niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return']

    def niDCPower_ConfigureDigitalEdgeSourceTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeSourceTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeSourceTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeSourceTrigger']['return']

    def niDCPower_ConfigureDigitalEdgeStartTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']

    def niDCPower_CreateAdvancedSequence(self, vi, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence):  # noqa: N802
        if self._defaults['CreateAdvancedSequence']['return'] != 0:
            return self._defaults['CreateAdvancedSequence']['return']
        return self._defaults['CreateAdvancedSequence']['return']

    def niDCPower_CreateAdvancedSequenceStep(self, vi, set_as_active_step):  # noqa: N802
        if self._defaults['CreateAdvancedSequenceStep']['return'] != 0:
            return self._defaults['CreateAdvancedSequenceStep']['return']
        return self._defaults['CreateAdvancedSequenceStep']['return']

    def niDCPower_DeleteAdvancedSequence(self, vi, sequence_name):  # noqa: N802
        if self._defaults['DeleteAdvancedSequence']['return'] != 0:
            return self._defaults['DeleteAdvancedSequence']['return']
        return self._defaults['DeleteAdvancedSequence']['return']

    def niDCPower_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niDCPower_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        if self._defaults['ExportSignal']['return'] != 0:
            return self._defaults['ExportSignal']['return']
        return self._defaults['ExportSignal']['return']

    def niDCPower_FetchMultiple(self, vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count):  # noqa: N802
        if self._defaults['FetchMultiple']['return'] != 0:
            return self._defaults['FetchMultiple']['return']
        if self._defaults['FetchMultiple']['voltageMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='voltageMeasurements')
        a = self._defaults['FetchMultiple']['voltageMeasurements']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(voltage_measurements), len(a))):
            voltage_measurements[i] = a[i]
        if self._defaults['FetchMultiple']['currentMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='currentMeasurements')
        a = self._defaults['FetchMultiple']['currentMeasurements']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(current_measurements), len(a))):
            current_measurements[i] = a[i]
        if self._defaults['FetchMultiple']['inCompliance'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='inCompliance')
        a = self._defaults['FetchMultiple']['inCompliance']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(in_compliance), len(a))):
            in_compliance[i] = a[i]
        if self._defaults['FetchMultiple']['actualCount'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='actualCount')
        actual_count.contents.value = self._defaults['FetchMultiple']['actualCount']
        return self._defaults['FetchMultiple']['return']

    def niDCPower_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViBoolean", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niDCPower_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViInt32", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niDCPower_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        if self._defaults['GetAttributeViInt64']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViInt64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt64']['attributeValue']
        return self._defaults['GetAttributeViInt64']['return']

    def niDCPower_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViReal64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niDCPower_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViString", param='attributeValue')
        if buffer_size == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niDCPower_GetChannelName(self, vi, index, buffer_size, channel_name):  # noqa: N802
        if self._defaults['GetChannelName']['return'] != 0:
            return self._defaults['GetChannelName']['return']
        if self._defaults['GetChannelName']['channelName'] is None:
            raise MockFunctionCallError("niDCPower_GetChannelName", param='channelName')
        if buffer_size == 0:
            return len(self._defaults['GetChannelName']['channelName'])
        channel_name.value = self._defaults['GetChannelName']['channelName'].encode('ascii')
        return self._defaults['GetChannelName']['return']

    def niDCPower_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        if self._defaults['GetError']['Code'] is None:
            raise MockFunctionCallError("niDCPower_GetError", param='Code')
        code.contents.value = self._defaults['GetError']['Code']
        if self._defaults['GetError']['Description'] is None:
            raise MockFunctionCallError("niDCPower_GetError", param='Description')
        if buffer_size == 0:
            return len(self._defaults['GetError']['Description'])
        description.value = self._defaults['GetError']['Description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niDCPower_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalLastDateAndTime']['return']
        if self._defaults['GetSelfCalLastDateAndTime']['Year'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Year')
        year.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Year']
        if self._defaults['GetSelfCalLastDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Month')
        month.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Month']
        if self._defaults['GetSelfCalLastDateAndTime']['Day'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Day')
        day.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Day']
        if self._defaults['GetSelfCalLastDateAndTime']['Hour'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Hour')
        hour.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Hour']
        if self._defaults['GetSelfCalLastDateAndTime']['Minute'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Minute')
        minute.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Minute']
        return self._defaults['GetSelfCalLastDateAndTime']['return']

    def niDCPower_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetSelfCalLastTemp']['return'] != 0:
            return self._defaults['GetSelfCalLastTemp']['return']
        if self._defaults['GetSelfCalLastTemp']['Temperature'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastTemp", param='Temperature')
        temperature.contents.value = self._defaults['GetSelfCalLastTemp']['Temperature']
        return self._defaults['GetSelfCalLastTemp']['return']

    def niDCPower_InitializeWithChannels(self, resource_name, channels, reset, option_string, vi):  # noqa: N802
        if self._defaults['InitializeWithChannels']['return'] != 0:
            return self._defaults['InitializeWithChannels']['return']
        if self._defaults['InitializeWithChannels']['vi'] is None:
            raise MockFunctionCallError("niDCPower_InitializeWithChannels", param='vi')
        vi.contents.value = self._defaults['InitializeWithChannels']['vi']
        return self._defaults['InitializeWithChannels']['return']

    def niDCPower_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niDCPower_Measure(self, vi, channel_name, measurement_type, measurement):  # noqa: N802
        if self._defaults['Measure']['return'] != 0:
            return self._defaults['Measure']['return']
        if self._defaults['Measure']['Measurement'] is None:
            raise MockFunctionCallError("niDCPower_Measure", param='Measurement')
        measurement.contents.value = self._defaults['Measure']['Measurement']
        return self._defaults['Measure']['return']

    def niDCPower_QueryInCompliance(self, vi, channel_name, in_compliance):  # noqa: N802
        if self._defaults['QueryInCompliance']['return'] != 0:
            return self._defaults['QueryInCompliance']['return']
        if self._defaults['QueryInCompliance']['inCompliance'] is None:
            raise MockFunctionCallError("niDCPower_QueryInCompliance", param='inCompliance')
        in_compliance.contents.value = self._defaults['QueryInCompliance']['inCompliance']
        return self._defaults['QueryInCompliance']['return']

    def niDCPower_QueryMaxCurrentLimit(self, vi, channel_name, voltage_level, max_current_limit):  # noqa: N802
        if self._defaults['QueryMaxCurrentLimit']['return'] != 0:
            return self._defaults['QueryMaxCurrentLimit']['return']
        if self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit'] is None:
            raise MockFunctionCallError("niDCPower_QueryMaxCurrentLimit", param='maxCurrentLimit')
        max_current_limit.contents.value = self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit']
        return self._defaults['QueryMaxCurrentLimit']['return']

    def niDCPower_QueryMaxVoltageLevel(self, vi, channel_name, current_limit, max_voltage_level):  # noqa: N802
        if self._defaults['QueryMaxVoltageLevel']['return'] != 0:
            return self._defaults['QueryMaxVoltageLevel']['return']
        if self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel'] is None:
            raise MockFunctionCallError("niDCPower_QueryMaxVoltageLevel", param='maxVoltageLevel')
        max_voltage_level.contents.value = self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel']
        return self._defaults['QueryMaxVoltageLevel']['return']

    def niDCPower_QueryMinCurrentLimit(self, vi, channel_name, voltage_level, min_current_limit):  # noqa: N802
        if self._defaults['QueryMinCurrentLimit']['return'] != 0:
            return self._defaults['QueryMinCurrentLimit']['return']
        if self._defaults['QueryMinCurrentLimit']['minCurrentLimit'] is None:
            raise MockFunctionCallError("niDCPower_QueryMinCurrentLimit", param='minCurrentLimit')
        min_current_limit.contents.value = self._defaults['QueryMinCurrentLimit']['minCurrentLimit']
        return self._defaults['QueryMinCurrentLimit']['return']

    def niDCPower_QueryOutputState(self, vi, channel_name, output_state, in_state):  # noqa: N802
        if self._defaults['QueryOutputState']['return'] != 0:
            return self._defaults['QueryOutputState']['return']
        if self._defaults['QueryOutputState']['inState'] is None:
            raise MockFunctionCallError("niDCPower_QueryOutputState", param='inState')
        in_state.contents.value = self._defaults['QueryOutputState']['inState']
        return self._defaults['QueryOutputState']['return']

    def niDCPower_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        if self._defaults['ReadCurrentTemperature']['return'] != 0:
            return self._defaults['ReadCurrentTemperature']['return']
        if self._defaults['ReadCurrentTemperature']['Temperature'] is None:
            raise MockFunctionCallError("niDCPower_ReadCurrentTemperature", param='Temperature')
        temperature.contents.value = self._defaults['ReadCurrentTemperature']['Temperature']
        return self._defaults['ReadCurrentTemperature']['return']

    def niDCPower_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niDCPower_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niDCPower_SendSoftwareEdgeTrigger(self, vi, trigger):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niDCPower_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niDCPower_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niDCPower_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niDCPower_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niDCPower_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niDCPower_SetSequence(self, vi, channel_name, values, source_delays, size):  # noqa: N802
        if self._defaults['SetSequence']['return'] != 0:
            return self._defaults['SetSequence']['return']
        return self._defaults['SetSequence']['return']

    def niDCPower_WaitForEvent(self, vi, event_id, timeout):  # noqa: N802
        if self._defaults['WaitForEvent']['return'] != 0:
            return self._defaults['WaitForEvent']['return']
        return self._defaults['WaitForEvent']['return']

    def niDCPower_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niDCPower_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niDCPower_error_message", param='errorMessage')
        a = self._defaults['error_message']['errorMessage']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(error_message), len(a))):
            error_message[i] = a[i]
        return self._defaults['error_message']['return']

    def niDCPower_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niDCPower_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niDCPower_self_test", param='selfTestResult')
        self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niDCPower_self_test", param='selfTestMessage')
        a = self._defaults['self_test']['selfTestMessage']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(self_test_message), len(a))):
            self_test_message[i] = a[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niDCPower_Abort.side_effect = MockFunctionCallError("niDCPower_Abort")
        mock_library.niDCPower_Abort.return_value = 0
        mock_library.niDCPower_Commit.side_effect = MockFunctionCallError("niDCPower_Commit")
        mock_library.niDCPower_Commit.return_value = 0
        mock_library.niDCPower_ConfigureApertureTime.side_effect = MockFunctionCallError("niDCPower_ConfigureApertureTime")
        mock_library.niDCPower_ConfigureApertureTime.return_value = 0
        mock_library.niDCPower_ConfigureDigitalEdgeMeasureTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeMeasureTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeMeasureTrigger.return_value = 0
        mock_library.niDCPower_ConfigureDigitalEdgePulseTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgePulseTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgePulseTrigger.return_value = 0
        mock_library.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger.return_value = 0
        mock_library.niDCPower_ConfigureDigitalEdgeSourceTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeSourceTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeSourceTrigger.return_value = 0
        mock_library.niDCPower_ConfigureDigitalEdgeStartTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeStartTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeStartTrigger.return_value = 0
        mock_library.niDCPower_CreateAdvancedSequence.side_effect = MockFunctionCallError("niDCPower_CreateAdvancedSequence")
        mock_library.niDCPower_CreateAdvancedSequence.return_value = 0
        mock_library.niDCPower_CreateAdvancedSequenceStep.side_effect = MockFunctionCallError("niDCPower_CreateAdvancedSequenceStep")
        mock_library.niDCPower_CreateAdvancedSequenceStep.return_value = 0
        mock_library.niDCPower_DeleteAdvancedSequence.side_effect = MockFunctionCallError("niDCPower_DeleteAdvancedSequence")
        mock_library.niDCPower_DeleteAdvancedSequence.return_value = 0
        mock_library.niDCPower_Disable.side_effect = MockFunctionCallError("niDCPower_Disable")
        mock_library.niDCPower_Disable.return_value = 0
        mock_library.niDCPower_ExportSignal.side_effect = MockFunctionCallError("niDCPower_ExportSignal")
        mock_library.niDCPower_ExportSignal.return_value = 0
        mock_library.niDCPower_FetchMultiple.side_effect = MockFunctionCallError("niDCPower_FetchMultiple")
        mock_library.niDCPower_FetchMultiple.return_value = 0
        mock_library.niDCPower_GetAttributeViBoolean.side_effect = MockFunctionCallError("niDCPower_GetAttributeViBoolean")
        mock_library.niDCPower_GetAttributeViBoolean.return_value = 0
        mock_library.niDCPower_GetAttributeViInt32.side_effect = MockFunctionCallError("niDCPower_GetAttributeViInt32")
        mock_library.niDCPower_GetAttributeViInt32.return_value = 0
        mock_library.niDCPower_GetAttributeViInt64.side_effect = MockFunctionCallError("niDCPower_GetAttributeViInt64")
        mock_library.niDCPower_GetAttributeViInt64.return_value = 0
        mock_library.niDCPower_GetAttributeViReal64.side_effect = MockFunctionCallError("niDCPower_GetAttributeViReal64")
        mock_library.niDCPower_GetAttributeViReal64.return_value = 0
        mock_library.niDCPower_GetAttributeViString.side_effect = MockFunctionCallError("niDCPower_GetAttributeViString")
        mock_library.niDCPower_GetAttributeViString.return_value = 0
        mock_library.niDCPower_GetChannelName.side_effect = MockFunctionCallError("niDCPower_GetChannelName")
        mock_library.niDCPower_GetChannelName.return_value = 0
        mock_library.niDCPower_GetError.side_effect = MockFunctionCallError("niDCPower_GetError")
        mock_library.niDCPower_GetError.return_value = 0
        mock_library.niDCPower_GetSelfCalLastDateAndTime.side_effect = MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime")
        mock_library.niDCPower_GetSelfCalLastDateAndTime.return_value = 0
        mock_library.niDCPower_GetSelfCalLastTemp.side_effect = MockFunctionCallError("niDCPower_GetSelfCalLastTemp")
        mock_library.niDCPower_GetSelfCalLastTemp.return_value = 0
        mock_library.niDCPower_InitializeWithChannels.side_effect = MockFunctionCallError("niDCPower_InitializeWithChannels")
        mock_library.niDCPower_InitializeWithChannels.return_value = 0
        mock_library.niDCPower_Initiate.side_effect = MockFunctionCallError("niDCPower_Initiate")
        mock_library.niDCPower_Initiate.return_value = 0
        mock_library.niDCPower_Measure.side_effect = MockFunctionCallError("niDCPower_Measure")
        mock_library.niDCPower_Measure.return_value = 0
        mock_library.niDCPower_QueryInCompliance.side_effect = MockFunctionCallError("niDCPower_QueryInCompliance")
        mock_library.niDCPower_QueryInCompliance.return_value = 0
        mock_library.niDCPower_QueryMaxCurrentLimit.side_effect = MockFunctionCallError("niDCPower_QueryMaxCurrentLimit")
        mock_library.niDCPower_QueryMaxCurrentLimit.return_value = 0
        mock_library.niDCPower_QueryMaxVoltageLevel.side_effect = MockFunctionCallError("niDCPower_QueryMaxVoltageLevel")
        mock_library.niDCPower_QueryMaxVoltageLevel.return_value = 0
        mock_library.niDCPower_QueryMinCurrentLimit.side_effect = MockFunctionCallError("niDCPower_QueryMinCurrentLimit")
        mock_library.niDCPower_QueryMinCurrentLimit.return_value = 0
        mock_library.niDCPower_QueryOutputState.side_effect = MockFunctionCallError("niDCPower_QueryOutputState")
        mock_library.niDCPower_QueryOutputState.return_value = 0
        mock_library.niDCPower_ReadCurrentTemperature.side_effect = MockFunctionCallError("niDCPower_ReadCurrentTemperature")
        mock_library.niDCPower_ReadCurrentTemperature.return_value = 0
        mock_library.niDCPower_ResetDevice.side_effect = MockFunctionCallError("niDCPower_ResetDevice")
        mock_library.niDCPower_ResetDevice.return_value = 0
        mock_library.niDCPower_ResetWithDefaults.side_effect = MockFunctionCallError("niDCPower_ResetWithDefaults")
        mock_library.niDCPower_ResetWithDefaults.return_value = 0
        mock_library.niDCPower_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niDCPower_SendSoftwareEdgeTrigger")
        mock_library.niDCPower_SendSoftwareEdgeTrigger.return_value = 0
        mock_library.niDCPower_SetAttributeViBoolean.side_effect = MockFunctionCallError("niDCPower_SetAttributeViBoolean")
        mock_library.niDCPower_SetAttributeViBoolean.return_value = 0
        mock_library.niDCPower_SetAttributeViInt32.side_effect = MockFunctionCallError("niDCPower_SetAttributeViInt32")
        mock_library.niDCPower_SetAttributeViInt32.return_value = 0
        mock_library.niDCPower_SetAttributeViInt64.side_effect = MockFunctionCallError("niDCPower_SetAttributeViInt64")
        mock_library.niDCPower_SetAttributeViInt64.return_value = 0
        mock_library.niDCPower_SetAttributeViReal64.side_effect = MockFunctionCallError("niDCPower_SetAttributeViReal64")
        mock_library.niDCPower_SetAttributeViReal64.return_value = 0
        mock_library.niDCPower_SetAttributeViString.side_effect = MockFunctionCallError("niDCPower_SetAttributeViString")
        mock_library.niDCPower_SetAttributeViString.return_value = 0
        mock_library.niDCPower_SetSequence.side_effect = MockFunctionCallError("niDCPower_SetSequence")
        mock_library.niDCPower_SetSequence.return_value = 0
        mock_library.niDCPower_WaitForEvent.side_effect = MockFunctionCallError("niDCPower_WaitForEvent")
        mock_library.niDCPower_WaitForEvent.return_value = 0
        mock_library.niDCPower_close.side_effect = MockFunctionCallError("niDCPower_close")
        mock_library.niDCPower_close.return_value = 0
        mock_library.niDCPower_error_message.side_effect = MockFunctionCallError("niDCPower_error_message")
        mock_library.niDCPower_error_message.return_value = 0
        mock_library.niDCPower_reset.side_effect = MockFunctionCallError("niDCPower_reset")
        mock_library.niDCPower_reset.return_value = 0
        mock_library.niDCPower_self_test.side_effect = MockFunctionCallError("niDCPower_self_test")
        mock_library.niDCPower_self_test.return_value = 0
