# -*- coding: utf-8 -*-
# This file was generated
import sys  # noqa: F401   - Not all mock_helpers will need this


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
        self._defaults['AcceptListOfDurationsInSeconds'] = {}
        self._defaults['AcceptListOfDurationsInSeconds']['return'] = 0
        self._defaults['BoolArrayOutputFunction'] = {}
        self._defaults['BoolArrayOutputFunction']['return'] = 0
        self._defaults['BoolArrayOutputFunction']['anArray'] = None
        self._defaults['DoubleAllTheNums'] = {}
        self._defaults['DoubleAllTheNums']['return'] = 0
        self._defaults['EnumArrayOutputFunction'] = {}
        self._defaults['EnumArrayOutputFunction']['return'] = 0
        self._defaults['EnumArrayOutputFunction']['anArray'] = None
        self._defaults['EnumInputFunctionWithDefaults'] = {}
        self._defaults['EnumInputFunctionWithDefaults']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer'] = {}
        self._defaults['ExportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer']['configuration'] = None
        self._defaults['FetchWaveform'] = {}
        self._defaults['FetchWaveform']['return'] = 0
        self._defaults['FetchWaveform']['waveformData'] = None
        self._defaults['FetchWaveform']['actualNumberOfSamples'] = None
        self._defaults['FunctionWithRepeatedCapabilityType'] = {}
        self._defaults['FunctionWithRepeatedCapabilityType']['return'] = 0
        self._defaults['GetABoolean'] = {}
        self._defaults['GetABoolean']['return'] = 0
        self._defaults['GetABoolean']['aBoolean'] = None
        self._defaults['GetANumber'] = {}
        self._defaults['GetANumber']['return'] = 0
        self._defaults['GetANumber']['aNumber'] = None
        self._defaults['GetAStringOfFixedMaximumSize'] = {}
        self._defaults['GetAStringOfFixedMaximumSize']['return'] = 0
        self._defaults['GetAStringOfFixedMaximumSize']['aString'] = None
        self._defaults['GetAStringUsingPythonCode'] = {}
        self._defaults['GetAStringUsingPythonCode']['return'] = 0
        self._defaults['GetAStringUsingPythonCode']['aString'] = None
        self._defaults['GetAnIviDanceString'] = {}
        self._defaults['GetAnIviDanceString']['return'] = 0
        self._defaults['GetAnIviDanceString']['aString'] = None
        self._defaults['GetAnIviDanceWithATwistString'] = {}
        self._defaults['GetAnIviDanceWithATwistString']['return'] = 0
        self._defaults['GetAnIviDanceWithATwistString']['actualSize'] = None
        self._defaults['GetAnIviDanceWithATwistString']['aString'] = None
        self._defaults['GetArrayForPythonCodeCustomType'] = {}
        self._defaults['GetArrayForPythonCodeCustomType']['return'] = 0
        self._defaults['GetArrayForPythonCodeCustomType']['arrayOut'] = None
        self._defaults['GetArrayForPythonCodeDouble'] = {}
        self._defaults['GetArrayForPythonCodeDouble']['return'] = 0
        self._defaults['GetArrayForPythonCodeDouble']['arrayOut'] = None
        self._defaults['GetArraySizeForPythonCode'] = {}
        self._defaults['GetArraySizeForPythonCode']['return'] = 0
        self._defaults['GetArraySizeForPythonCode']['sizeOut'] = None
        self._defaults['GetArrayUsingIviDance'] = {}
        self._defaults['GetArrayUsingIviDance']['return'] = 0
        self._defaults['GetArrayUsingIviDance']['arrayOut'] = None
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
        self._defaults['GetCalDateAndTime'] = {}
        self._defaults['GetCalDateAndTime']['return'] = 0
        self._defaults['GetCalDateAndTime']['month'] = None
        self._defaults['GetCalDateAndTime']['day'] = None
        self._defaults['GetCalDateAndTime']['year'] = None
        self._defaults['GetCalDateAndTime']['hour'] = None
        self._defaults['GetCalDateAndTime']['minute'] = None
        self._defaults['GetCalInterval'] = {}
        self._defaults['GetCalInterval']['return'] = 0
        self._defaults['GetCalInterval']['months'] = None
        self._defaults['GetChannelNames'] = {}
        self._defaults['GetChannelNames']['return'] = 0
        self._defaults['GetChannelNames']['names'] = None
        self._defaults['GetCustomType'] = {}
        self._defaults['GetCustomType']['return'] = 0
        self._defaults['GetCustomType']['cs'] = None
        self._defaults['GetCustomTypeArray'] = {}
        self._defaults['GetCustomTypeArray']['return'] = 0
        self._defaults['GetCustomTypeArray']['cs'] = None
        self._defaults['GetCustomTypeTypedef'] = {}
        self._defaults['GetCustomTypeTypedef']['return'] = 0
        self._defaults['GetCustomTypeTypedef']['cst'] = None
        self._defaults['GetCustomTypeTypedef']['csnt'] = None
        self._defaults['GetEnumValue'] = {}
        self._defaults['GetEnumValue']['return'] = 0
        self._defaults['GetEnumValue']['aQuantity'] = None
        self._defaults['GetEnumValue']['aTurtle'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['description'] = None
        self._defaults['ImportAttributeConfigurationBuffer'] = {}
        self._defaults['ImportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['MultipleArrayTypes'] = {}
        self._defaults['MultipleArrayTypes']['return'] = 0
        self._defaults['MultipleArrayTypes']['outputArray'] = None
        self._defaults['MultipleArrayTypes']['outputArrayOfFixedLength'] = None
        self._defaults['MultipleArraysSameSize'] = {}
        self._defaults['MultipleArraysSameSize']['return'] = 0
        self._defaults['OneInputFunction'] = {}
        self._defaults['OneInputFunction']['return'] = 0
        self._defaults['ParametersAreMultipleTypes'] = {}
        self._defaults['ParametersAreMultipleTypes']['return'] = 0
        self._defaults['PoorlyNamedSimpleFunction'] = {}
        self._defaults['PoorlyNamedSimpleFunction']['return'] = 0
        self._defaults['Read'] = {}
        self._defaults['Read']['return'] = 0
        self._defaults['Read']['reading'] = None
        self._defaults['ReadFromChannel'] = {}
        self._defaults['ReadFromChannel']['return'] = 0
        self._defaults['ReadFromChannel']['reading'] = None
        self._defaults['ReturnANumberAndAString'] = {}
        self._defaults['ReturnANumberAndAString']['return'] = 0
        self._defaults['ReturnANumberAndAString']['aNumber'] = None
        self._defaults['ReturnANumberAndAString']['aString'] = None
        self._defaults['ReturnDurationInSeconds'] = {}
        self._defaults['ReturnDurationInSeconds']['return'] = 0
        self._defaults['ReturnDurationInSeconds']['timedelta'] = None
        self._defaults['ReturnListOfDurationsInSeconds'] = {}
        self._defaults['ReturnListOfDurationsInSeconds']['return'] = 0
        self._defaults['ReturnListOfDurationsInSeconds']['timedeltas'] = None
        self._defaults['ReturnMultipleTypes'] = {}
        self._defaults['ReturnMultipleTypes']['return'] = 0
        self._defaults['ReturnMultipleTypes']['aBoolean'] = None
        self._defaults['ReturnMultipleTypes']['anInt32'] = None
        self._defaults['ReturnMultipleTypes']['anInt64'] = None
        self._defaults['ReturnMultipleTypes']['anIntEnum'] = None
        self._defaults['ReturnMultipleTypes']['aFloat'] = None
        self._defaults['ReturnMultipleTypes']['aFloatEnum'] = None
        self._defaults['ReturnMultipleTypes']['anArray'] = None
        self._defaults['ReturnMultipleTypes']['aString'] = None
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
        self._defaults['SetCustomType'] = {}
        self._defaults['SetCustomType']['return'] = 0
        self._defaults['SetCustomTypeArray'] = {}
        self._defaults['SetCustomTypeArray']['return'] = 0
        self._defaults['StringValuedEnumInputFunctionWithDefaults'] = {}
        self._defaults['StringValuedEnumInputFunctionWithDefaults']['return'] = 0
        self._defaults['TwoInputFunction'] = {}
        self._defaults['TwoInputFunction']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['Use64BitNumber'] = {}
        self._defaults['Use64BitNumber']['return'] = 0
        self._defaults['Use64BitNumber']['output'] = None
        self._defaults['WriteWaveform'] = {}
        self._defaults['WriteWaveform']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['selfTestResult'] = None
        self._defaults['self_test']['selfTestMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niFake_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niFake_AcceptListOfDurationsInSeconds(self, vi, count, delays):  # noqa: N802
        if self._defaults['AcceptListOfDurationsInSeconds']['return'] != 0:
            return self._defaults['AcceptListOfDurationsInSeconds']['return']
        return self._defaults['AcceptListOfDurationsInSeconds']['return']

    def niFake_BoolArrayOutputFunction(self, vi, number_of_elements, an_array):  # noqa: N802
        if self._defaults['BoolArrayOutputFunction']['return'] != 0:
            return self._defaults['BoolArrayOutputFunction']['return']
        # an_array
        if self._defaults['BoolArrayOutputFunction']['anArray'] is None:
            raise MockFunctionCallError("niFake_BoolArrayOutputFunction", param='anArray')
        test_value = self._defaults['BoolArrayOutputFunction']['anArray']
        try:
            an_array_ref = an_array.contents
        except AttributeError:
            an_array_ref = an_array
        assert len(an_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            an_array_ref[i] = test_value[i]
        return self._defaults['BoolArrayOutputFunction']['return']

    def niFake_DoubleAllTheNums(self, vi, number_count, numbers):  # noqa: N802
        if self._defaults['DoubleAllTheNums']['return'] != 0:
            return self._defaults['DoubleAllTheNums']['return']
        return self._defaults['DoubleAllTheNums']['return']

    def niFake_EnumArrayOutputFunction(self, vi, number_of_elements, an_array):  # noqa: N802
        if self._defaults['EnumArrayOutputFunction']['return'] != 0:
            return self._defaults['EnumArrayOutputFunction']['return']
        # an_array
        if self._defaults['EnumArrayOutputFunction']['anArray'] is None:
            raise MockFunctionCallError("niFake_EnumArrayOutputFunction", param='anArray')
        test_value = self._defaults['EnumArrayOutputFunction']['anArray']
        try:
            an_array_ref = an_array.contents
        except AttributeError:
            an_array_ref = an_array
        assert len(an_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            an_array_ref[i] = test_value[i]
        return self._defaults['EnumArrayOutputFunction']['return']

    def niFake_EnumInputFunctionWithDefaults(self, vi, a_turtle):  # noqa: N802
        if self._defaults['EnumInputFunctionWithDefaults']['return'] != 0:
            return self._defaults['EnumInputFunctionWithDefaults']['return']
        return self._defaults['EnumInputFunctionWithDefaults']['return']

    def niFake_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationBuffer']['return']
        if self._defaults['ExportAttributeConfigurationBuffer']['configuration'] is None:
            raise MockFunctionCallError("niFake_ExportAttributeConfigurationBuffer", param='configuration')
        if size_in_bytes.value == 0:
            return len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])
        try:
            configuration_ref = configuration.contents
        except AttributeError:
            configuration_ref = configuration
        for i in range(len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])):
            configuration_ref[i] = self._defaults['ExportAttributeConfigurationBuffer']['configuration'][i]
        return self._defaults['ExportAttributeConfigurationBuffer']['return']

    def niFake_FetchWaveform(self, vi, number_of_samples, waveform_data, actual_number_of_samples):  # noqa: N802
        if self._defaults['FetchWaveform']['return'] != 0:
            return self._defaults['FetchWaveform']['return']
        # waveform_data
        if self._defaults['FetchWaveform']['waveformData'] is None:
            raise MockFunctionCallError("niFake_FetchWaveform", param='waveformData')
        test_value = self._defaults['FetchWaveform']['waveformData']
        try:
            waveform_data_ref = waveform_data.contents
        except AttributeError:
            waveform_data_ref = waveform_data
        assert len(waveform_data_ref) >= len(test_value)
        for i in range(len(test_value)):
            waveform_data_ref[i] = test_value[i]
        # actual_number_of_samples
        if self._defaults['FetchWaveform']['actualNumberOfSamples'] is None:
            raise MockFunctionCallError("niFake_FetchWaveform", param='actualNumberOfSamples')
        if actual_number_of_samples is not None:
            actual_number_of_samples.contents.value = self._defaults['FetchWaveform']['actualNumberOfSamples']
        return self._defaults['FetchWaveform']['return']

    def niFake_FunctionWithRepeatedCapabilityType(self, vi, site_list):  # noqa: N802
        if self._defaults['FunctionWithRepeatedCapabilityType']['return'] != 0:
            return self._defaults['FunctionWithRepeatedCapabilityType']['return']
        return self._defaults['FunctionWithRepeatedCapabilityType']['return']

    def niFake_GetABoolean(self, vi, a_boolean):  # noqa: N802
        if self._defaults['GetABoolean']['return'] != 0:
            return self._defaults['GetABoolean']['return']
        # a_boolean
        if self._defaults['GetABoolean']['aBoolean'] is None:
            raise MockFunctionCallError("niFake_GetABoolean", param='aBoolean')
        if a_boolean is not None:
            a_boolean.contents.value = self._defaults['GetABoolean']['aBoolean']
        return self._defaults['GetABoolean']['return']

    def niFake_GetANumber(self, vi, a_number):  # noqa: N802
        if self._defaults['GetANumber']['return'] != 0:
            return self._defaults['GetANumber']['return']
        # a_number
        if self._defaults['GetANumber']['aNumber'] is None:
            raise MockFunctionCallError("niFake_GetANumber", param='aNumber')
        if a_number is not None:
            a_number.contents.value = self._defaults['GetANumber']['aNumber']
        return self._defaults['GetANumber']['return']

    def niFake_GetAStringOfFixedMaximumSize(self, vi, a_string):  # noqa: N802
        if self._defaults['GetAStringOfFixedMaximumSize']['return'] != 0:
            return self._defaults['GetAStringOfFixedMaximumSize']['return']
        # a_string
        if self._defaults['GetAStringOfFixedMaximumSize']['aString'] is None:
            raise MockFunctionCallError("niFake_GetAStringOfFixedMaximumSize", param='aString')
        test_value = self._defaults['GetAStringOfFixedMaximumSize']['aString']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(a_string) >= len(test_value)
        for i in range(len(test_value)):
            a_string[i] = test_value[i]
        return self._defaults['GetAStringOfFixedMaximumSize']['return']

    def niFake_GetAStringUsingPythonCode(self, vi, a_number, a_string):  # noqa: N802
        if self._defaults['GetAStringUsingPythonCode']['return'] != 0:
            return self._defaults['GetAStringUsingPythonCode']['return']
        # a_string
        if self._defaults['GetAStringUsingPythonCode']['aString'] is None:
            raise MockFunctionCallError("niFake_GetAStringUsingPythonCode", param='aString')
        test_value = self._defaults['GetAStringUsingPythonCode']['aString']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(a_string) >= len(test_value)
        for i in range(len(test_value)):
            a_string[i] = test_value[i]
        return self._defaults['GetAStringUsingPythonCode']['return']

    def niFake_GetAnIviDanceString(self, vi, buffer_size, a_string):  # noqa: N802
        if self._defaults['GetAnIviDanceString']['return'] != 0:
            return self._defaults['GetAnIviDanceString']['return']
        if self._defaults['GetAnIviDanceString']['aString'] is None:
            raise MockFunctionCallError("niFake_GetAnIviDanceString", param='aString')
        if buffer_size.value == 0:
            return len(self._defaults['GetAnIviDanceString']['aString'])
        a_string.value = self._defaults['GetAnIviDanceString']['aString'].encode('ascii')
        return self._defaults['GetAnIviDanceString']['return']

    def niFake_GetAnIviDanceWithATwistString(self, vi, buffer_size, a_string, actual_size):  # noqa: N802
        if self._defaults['GetAnIviDanceWithATwistString']['return'] != 0:
            return self._defaults['GetAnIviDanceWithATwistString']['return']
        # actual_size
        if self._defaults['GetAnIviDanceWithATwistString']['actualSize'] is None:
            raise MockFunctionCallError("niFake_GetAnIviDanceWithATwistString", param='actualSize')
        if actual_size is not None:
            actual_size.contents.value = self._defaults['GetAnIviDanceWithATwistString']['actualSize']
        if self._defaults['GetAnIviDanceWithATwistString']['aString'] is None:
            raise MockFunctionCallError("niFake_GetAnIviDanceWithATwistString", param='aString')
        if buffer_size.value == 0:
            return len(self._defaults['GetAnIviDanceWithATwistString']['aString'])
        a_string.value = self._defaults['GetAnIviDanceWithATwistString']['aString'].encode('ascii')
        return self._defaults['GetAnIviDanceWithATwistString']['return']

    def niFake_GetArrayForPythonCodeCustomType(self, vi, number_of_elements, array_out):  # noqa: N802
        if self._defaults['GetArrayForPythonCodeCustomType']['return'] != 0:
            return self._defaults['GetArrayForPythonCodeCustomType']['return']
        # array_out
        if self._defaults['GetArrayForPythonCodeCustomType']['arrayOut'] is None:
            raise MockFunctionCallError("niFake_GetArrayForPythonCodeCustomType", param='arrayOut')
        test_value = self._defaults['GetArrayForPythonCodeCustomType']['arrayOut']
        try:
            array_out_ref = array_out.contents
        except AttributeError:
            array_out_ref = array_out
        assert len(array_out_ref) >= len(test_value)
        for i in range(len(test_value)):
            array_out_ref[i] = test_value[i]
        return self._defaults['GetArrayForPythonCodeCustomType']['return']

    def niFake_GetArrayForPythonCodeDouble(self, vi, number_of_elements, array_out):  # noqa: N802
        if self._defaults['GetArrayForPythonCodeDouble']['return'] != 0:
            return self._defaults['GetArrayForPythonCodeDouble']['return']
        # array_out
        if self._defaults['GetArrayForPythonCodeDouble']['arrayOut'] is None:
            raise MockFunctionCallError("niFake_GetArrayForPythonCodeDouble", param='arrayOut')
        test_value = self._defaults['GetArrayForPythonCodeDouble']['arrayOut']
        try:
            array_out_ref = array_out.contents
        except AttributeError:
            array_out_ref = array_out
        assert len(array_out_ref) >= len(test_value)
        for i in range(len(test_value)):
            array_out_ref[i] = test_value[i]
        return self._defaults['GetArrayForPythonCodeDouble']['return']

    def niFake_GetArraySizeForPythonCode(self, vi, size_out):  # noqa: N802
        if self._defaults['GetArraySizeForPythonCode']['return'] != 0:
            return self._defaults['GetArraySizeForPythonCode']['return']
        # size_out
        if self._defaults['GetArraySizeForPythonCode']['sizeOut'] is None:
            raise MockFunctionCallError("niFake_GetArraySizeForPythonCode", param='sizeOut')
        if size_out is not None:
            size_out.contents.value = self._defaults['GetArraySizeForPythonCode']['sizeOut']
        return self._defaults['GetArraySizeForPythonCode']['return']

    def niFake_GetArrayUsingIviDance(self, vi, array_size, array_out):  # noqa: N802
        if self._defaults['GetArrayUsingIviDance']['return'] != 0:
            return self._defaults['GetArrayUsingIviDance']['return']
        if self._defaults['GetArrayUsingIviDance']['arrayOut'] is None:
            raise MockFunctionCallError("niFake_GetArrayUsingIviDance", param='arrayOut')
        if array_size.value == 0:
            return len(self._defaults['GetArrayUsingIviDance']['arrayOut'])
        try:
            array_out_ref = array_out.contents
        except AttributeError:
            array_out_ref = array_out
        for i in range(len(self._defaults['GetArrayUsingIviDance']['arrayOut'])):
            array_out_ref[i] = self._defaults['GetArrayUsingIviDance']['arrayOut'][i]
        return self._defaults['GetArrayUsingIviDance']['return']

    def niFake_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViBoolean", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niFake_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViInt32", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niFake_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt64']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViInt64", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt64']['attributeValue']
        return self._defaults['GetAttributeViInt64']['return']

    def niFake_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViReal64", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niFake_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViString", param='attributeValue')
        if buffer_size.value == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niFake_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute):  # noqa: N802
        if self._defaults['GetCalDateAndTime']['return'] != 0:
            return self._defaults['GetCalDateAndTime']['return']
        # month
        if self._defaults['GetCalDateAndTime']['month'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetCalDateAndTime']['month']
        # day
        if self._defaults['GetCalDateAndTime']['day'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetCalDateAndTime']['day']
        # year
        if self._defaults['GetCalDateAndTime']['year'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetCalDateAndTime']['year']
        # hour
        if self._defaults['GetCalDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetCalDateAndTime']['hour']
        # minute
        if self._defaults['GetCalDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetCalDateAndTime']['minute']
        return self._defaults['GetCalDateAndTime']['return']

    def niFake_GetCalInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetCalInterval']['return'] != 0:
            return self._defaults['GetCalInterval']['return']
        # months
        if self._defaults['GetCalInterval']['months'] is None:
            raise MockFunctionCallError("niFake_GetCalInterval", param='months')
        if months is not None:
            months.contents.value = self._defaults['GetCalInterval']['months']
        return self._defaults['GetCalInterval']['return']

    def niFake_GetChannelNames(self, vi, indices, name_size, names):  # noqa: N802
        if self._defaults['GetChannelNames']['return'] != 0:
            return self._defaults['GetChannelNames']['return']
        if self._defaults['GetChannelNames']['names'] is None:
            raise MockFunctionCallError("niFake_GetChannelNames", param='names')
        if name_size.value == 0:
            return len(self._defaults['GetChannelNames']['names'])
        names.value = self._defaults['GetChannelNames']['names'].encode('ascii')
        return self._defaults['GetChannelNames']['return']

    def niFake_GetCustomType(self, vi, cs):  # noqa: N802
        if self._defaults['GetCustomType']['return'] != 0:
            return self._defaults['GetCustomType']['return']
        # cs
        if self._defaults['GetCustomType']['cs'] is None:
            raise MockFunctionCallError("niFake_GetCustomType", param='cs')
        for field in self._defaults['GetCustomType']['cs']._fields_:
            field_name = field[0]
            setattr(cs.contents, field_name, getattr(self._defaults['GetCustomType']['cs'], field_name))
        return self._defaults['GetCustomType']['return']

    def niFake_GetCustomTypeArray(self, vi, number_of_elements, cs):  # noqa: N802
        if self._defaults['GetCustomTypeArray']['return'] != 0:
            return self._defaults['GetCustomTypeArray']['return']
        # cs
        if self._defaults['GetCustomTypeArray']['cs'] is None:
            raise MockFunctionCallError("niFake_GetCustomTypeArray", param='cs')
        test_value = self._defaults['GetCustomTypeArray']['cs']
        try:
            cs_ref = cs.contents
        except AttributeError:
            cs_ref = cs
        assert len(cs_ref) >= len(test_value)
        for i in range(len(test_value)):
            cs_ref[i] = test_value[i]
        return self._defaults['GetCustomTypeArray']['return']

    def niFake_GetCustomTypeTypedef(self, vi, cst, csnt):  # noqa: N802
        if self._defaults['GetCustomTypeTypedef']['return'] != 0:
            return self._defaults['GetCustomTypeTypedef']['return']
        # cst
        if self._defaults['GetCustomTypeTypedef']['cst'] is None:
            raise MockFunctionCallError("niFake_GetCustomTypeTypedef", param='cst')
        for field in self._defaults['GetCustomTypeTypedef']['cst']._fields_:
            field_name = field[0]
            setattr(cst.contents, field_name, getattr(self._defaults['GetCustomTypeTypedef']['cst'], field_name))
        # csnt
        if self._defaults['GetCustomTypeTypedef']['csnt'] is None:
            raise MockFunctionCallError("niFake_GetCustomTypeTypedef", param='csnt')
        for field in self._defaults['GetCustomTypeTypedef']['csnt']._fields_:
            field_name = field[0]
            setattr(csnt.contents, field_name, getattr(self._defaults['GetCustomTypeTypedef']['csnt'], field_name))
        return self._defaults['GetCustomTypeTypedef']['return']

    def niFake_GetEnumValue(self, vi, a_quantity, a_turtle):  # noqa: N802
        if self._defaults['GetEnumValue']['return'] != 0:
            return self._defaults['GetEnumValue']['return']
        # a_quantity
        if self._defaults['GetEnumValue']['aQuantity'] is None:
            raise MockFunctionCallError("niFake_GetEnumValue", param='aQuantity')
        if a_quantity is not None:
            a_quantity.contents.value = self._defaults['GetEnumValue']['aQuantity']
        # a_turtle
        if self._defaults['GetEnumValue']['aTurtle'] is None:
            raise MockFunctionCallError("niFake_GetEnumValue", param='aTurtle')
        if a_turtle is not None:
            a_turtle.contents.value = self._defaults['GetEnumValue']['aTurtle']
        return self._defaults['GetEnumValue']['return']

    def niFake_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niFake_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niFake_GetError", param='description')
        if buffer_size.value == 0:
            return len(self._defaults['GetError']['description'])
        description.value = self._defaults['GetError']['description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niFake_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationBuffer']['return']
        return self._defaults['ImportAttributeConfigurationBuffer']['return']

    def niFake_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # vi
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niFake_InitWithOptions", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niFake_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niFake_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niFake_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niFake_MultipleArrayTypes(self, vi, output_array_size, output_array, output_array_of_fixed_length, input_array_sizes, input_array_of_floats, input_array_of_integers):  # noqa: N802
        if self._defaults['MultipleArrayTypes']['return'] != 0:
            return self._defaults['MultipleArrayTypes']['return']
        # output_array
        if self._defaults['MultipleArrayTypes']['outputArray'] is None:
            raise MockFunctionCallError("niFake_MultipleArrayTypes", param='outputArray')
        test_value = self._defaults['MultipleArrayTypes']['outputArray']
        try:
            output_array_ref = output_array.contents
        except AttributeError:
            output_array_ref = output_array
        assert len(output_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            output_array_ref[i] = test_value[i]
        # output_array_of_fixed_length
        if self._defaults['MultipleArrayTypes']['outputArrayOfFixedLength'] is None:
            raise MockFunctionCallError("niFake_MultipleArrayTypes", param='outputArrayOfFixedLength')
        test_value = self._defaults['MultipleArrayTypes']['outputArrayOfFixedLength']
        try:
            output_array_of_fixed_length_ref = output_array_of_fixed_length.contents
        except AttributeError:
            output_array_of_fixed_length_ref = output_array_of_fixed_length
        assert len(output_array_of_fixed_length_ref) >= len(test_value)
        for i in range(len(test_value)):
            output_array_of_fixed_length_ref[i] = test_value[i]
        return self._defaults['MultipleArrayTypes']['return']

    def niFake_MultipleArraysSameSize(self, vi, values1, values2, values3, values4, size):  # noqa: N802
        if self._defaults['MultipleArraysSameSize']['return'] != 0:
            return self._defaults['MultipleArraysSameSize']['return']
        return self._defaults['MultipleArraysSameSize']['return']

    def niFake_OneInputFunction(self, vi, a_number):  # noqa: N802
        if self._defaults['OneInputFunction']['return'] != 0:
            return self._defaults['OneInputFunction']['return']
        return self._defaults['OneInputFunction']['return']

    def niFake_ParametersAreMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, string_size, a_string):  # noqa: N802
        if self._defaults['ParametersAreMultipleTypes']['return'] != 0:
            return self._defaults['ParametersAreMultipleTypes']['return']
        return self._defaults['ParametersAreMultipleTypes']['return']

    def niFake_PoorlyNamedSimpleFunction(self, vi):  # noqa: N802
        if self._defaults['PoorlyNamedSimpleFunction']['return'] != 0:
            return self._defaults['PoorlyNamedSimpleFunction']['return']
        return self._defaults['PoorlyNamedSimpleFunction']['return']

    def niFake_Read(self, vi, maximum_time, reading):  # noqa: N802
        if self._defaults['Read']['return'] != 0:
            return self._defaults['Read']['return']
        # reading
        if self._defaults['Read']['reading'] is None:
            raise MockFunctionCallError("niFake_Read", param='reading')
        if reading is not None:
            reading.contents.value = self._defaults['Read']['reading']
        return self._defaults['Read']['return']

    def niFake_ReadFromChannel(self, vi, channel_name, maximum_time, reading):  # noqa: N802
        if self._defaults['ReadFromChannel']['return'] != 0:
            return self._defaults['ReadFromChannel']['return']
        # reading
        if self._defaults['ReadFromChannel']['reading'] is None:
            raise MockFunctionCallError("niFake_ReadFromChannel", param='reading')
        if reading is not None:
            reading.contents.value = self._defaults['ReadFromChannel']['reading']
        return self._defaults['ReadFromChannel']['return']

    def niFake_ReturnANumberAndAString(self, vi, a_number, a_string):  # noqa: N802
        if self._defaults['ReturnANumberAndAString']['return'] != 0:
            return self._defaults['ReturnANumberAndAString']['return']
        # a_number
        if self._defaults['ReturnANumberAndAString']['aNumber'] is None:
            raise MockFunctionCallError("niFake_ReturnANumberAndAString", param='aNumber')
        if a_number is not None:
            a_number.contents.value = self._defaults['ReturnANumberAndAString']['aNumber']
        # a_string
        if self._defaults['ReturnANumberAndAString']['aString'] is None:
            raise MockFunctionCallError("niFake_ReturnANumberAndAString", param='aString')
        test_value = self._defaults['ReturnANumberAndAString']['aString']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(a_string) >= len(test_value)
        for i in range(len(test_value)):
            a_string[i] = test_value[i]
        return self._defaults['ReturnANumberAndAString']['return']

    def niFake_ReturnDurationInSeconds(self, vi, timedelta):  # noqa: N802
        if self._defaults['ReturnDurationInSeconds']['return'] != 0:
            return self._defaults['ReturnDurationInSeconds']['return']
        # timedelta
        if self._defaults['ReturnDurationInSeconds']['timedelta'] is None:
            raise MockFunctionCallError("niFake_ReturnDurationInSeconds", param='timedelta')
        if timedelta is not None:
            timedelta.contents.value = self._defaults['ReturnDurationInSeconds']['timedelta']
        return self._defaults['ReturnDurationInSeconds']['return']

    def niFake_ReturnListOfDurationsInSeconds(self, vi, number_of_elements, timedeltas):  # noqa: N802
        if self._defaults['ReturnListOfDurationsInSeconds']['return'] != 0:
            return self._defaults['ReturnListOfDurationsInSeconds']['return']
        # timedeltas
        if self._defaults['ReturnListOfDurationsInSeconds']['timedeltas'] is None:
            raise MockFunctionCallError("niFake_ReturnListOfDurationsInSeconds", param='timedeltas')
        test_value = self._defaults['ReturnListOfDurationsInSeconds']['timedeltas']
        try:
            timedeltas_ref = timedeltas.contents
        except AttributeError:
            timedeltas_ref = timedeltas
        assert len(timedeltas_ref) >= len(test_value)
        for i in range(len(test_value)):
            timedeltas_ref[i] = test_value[i]
        return self._defaults['ReturnListOfDurationsInSeconds']['return']

    def niFake_ReturnMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, array_size, an_array, string_size, a_string):  # noqa: N802
        if self._defaults['ReturnMultipleTypes']['return'] != 0:
            return self._defaults['ReturnMultipleTypes']['return']
        # a_boolean
        if self._defaults['ReturnMultipleTypes']['aBoolean'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='aBoolean')
        if a_boolean is not None:
            a_boolean.contents.value = self._defaults['ReturnMultipleTypes']['aBoolean']
        # an_int32
        if self._defaults['ReturnMultipleTypes']['anInt32'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anInt32')
        if an_int32 is not None:
            an_int32.contents.value = self._defaults['ReturnMultipleTypes']['anInt32']
        # an_int64
        if self._defaults['ReturnMultipleTypes']['anInt64'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anInt64')
        if an_int64 is not None:
            an_int64.contents.value = self._defaults['ReturnMultipleTypes']['anInt64']
        # an_int_enum
        if self._defaults['ReturnMultipleTypes']['anIntEnum'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anIntEnum')
        if an_int_enum is not None:
            an_int_enum.contents.value = self._defaults['ReturnMultipleTypes']['anIntEnum']
        # a_float
        if self._defaults['ReturnMultipleTypes']['aFloat'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='aFloat')
        if a_float is not None:
            a_float.contents.value = self._defaults['ReturnMultipleTypes']['aFloat']
        # a_float_enum
        if self._defaults['ReturnMultipleTypes']['aFloatEnum'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='aFloatEnum')
        if a_float_enum is not None:
            a_float_enum.contents.value = self._defaults['ReturnMultipleTypes']['aFloatEnum']
        # an_array
        if self._defaults['ReturnMultipleTypes']['anArray'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anArray')
        test_value = self._defaults['ReturnMultipleTypes']['anArray']
        try:
            an_array_ref = an_array.contents
        except AttributeError:
            an_array_ref = an_array
        assert len(an_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            an_array_ref[i] = test_value[i]
        if self._defaults['ReturnMultipleTypes']['aString'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='aString')
        if string_size.value == 0:
            return len(self._defaults['ReturnMultipleTypes']['aString'])
        a_string.value = self._defaults['ReturnMultipleTypes']['aString'].encode('ascii')
        return self._defaults['ReturnMultipleTypes']['return']

    def niFake_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niFake_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niFake_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niFake_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niFake_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niFake_SetCustomType(self, vi, cs):  # noqa: N802
        if self._defaults['SetCustomType']['return'] != 0:
            return self._defaults['SetCustomType']['return']
        return self._defaults['SetCustomType']['return']

    def niFake_SetCustomTypeArray(self, vi, number_of_elements, cs):  # noqa: N802
        if self._defaults['SetCustomTypeArray']['return'] != 0:
            return self._defaults['SetCustomTypeArray']['return']
        return self._defaults['SetCustomTypeArray']['return']

    def niFake_StringValuedEnumInputFunctionWithDefaults(self, vi, a_mobile_os_name):  # noqa: N802
        if self._defaults['StringValuedEnumInputFunctionWithDefaults']['return'] != 0:
            return self._defaults['StringValuedEnumInputFunctionWithDefaults']['return']
        return self._defaults['StringValuedEnumInputFunctionWithDefaults']['return']

    def niFake_TwoInputFunction(self, vi, a_number, a_string):  # noqa: N802
        if self._defaults['TwoInputFunction']['return'] != 0:
            return self._defaults['TwoInputFunction']['return']
        return self._defaults['TwoInputFunction']['return']

    def niFake_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niFake_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niFake_Use64BitNumber(self, vi, input, output):  # noqa: N802
        if self._defaults['Use64BitNumber']['return'] != 0:
            return self._defaults['Use64BitNumber']['return']
        # output
        if self._defaults['Use64BitNumber']['output'] is None:
            raise MockFunctionCallError("niFake_Use64BitNumber", param='output')
        if output is not None:
            output.contents.value = self._defaults['Use64BitNumber']['output']
        return self._defaults['Use64BitNumber']['return']

    def niFake_WriteWaveform(self, vi, number_of_samples, waveform):  # noqa: N802
        if self._defaults['WriteWaveform']['return'] != 0:
            return self._defaults['WriteWaveform']['return']
        return self._defaults['WriteWaveform']['return']

    def niFake_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niFake_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niFake_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niFake_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niFake_self_test", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niFake_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niFake_Abort_cfunc.side_effect = MockFunctionCallError("niFake_Abort_cfunc")
        mock_library.niFake_Abort_cfunc.return_value = 0
        mock_library.niFake_AcceptListOfDurationsInSeconds_cfunc.side_effect = MockFunctionCallError("niFake_AcceptListOfDurationsInSeconds_cfunc")
        mock_library.niFake_AcceptListOfDurationsInSeconds_cfunc.return_value = 0
        mock_library.niFake_BoolArrayOutputFunction_cfunc.side_effect = MockFunctionCallError("niFake_BoolArrayOutputFunction_cfunc")
        mock_library.niFake_BoolArrayOutputFunction_cfunc.return_value = 0
        mock_library.niFake_DoubleAllTheNums_cfunc.side_effect = MockFunctionCallError("niFake_DoubleAllTheNums_cfunc")
        mock_library.niFake_DoubleAllTheNums_cfunc.return_value = 0
        mock_library.niFake_EnumArrayOutputFunction_cfunc.side_effect = MockFunctionCallError("niFake_EnumArrayOutputFunction_cfunc")
        mock_library.niFake_EnumArrayOutputFunction_cfunc.return_value = 0
        mock_library.niFake_EnumInputFunctionWithDefaults_cfunc.side_effect = MockFunctionCallError("niFake_EnumInputFunctionWithDefaults_cfunc")
        mock_library.niFake_EnumInputFunctionWithDefaults_cfunc.return_value = 0
        mock_library.niFake_ExportAttributeConfigurationBuffer_cfunc.side_effect = MockFunctionCallError("niFake_ExportAttributeConfigurationBuffer_cfunc")
        mock_library.niFake_ExportAttributeConfigurationBuffer_cfunc.return_value = 0
        mock_library.niFake_FetchWaveform_cfunc.side_effect = MockFunctionCallError("niFake_FetchWaveform_cfunc")
        mock_library.niFake_FetchWaveform_cfunc.return_value = 0
        mock_library.niFake_FunctionWithRepeatedCapabilityType_cfunc.side_effect = MockFunctionCallError("niFake_FunctionWithRepeatedCapabilityType_cfunc")
        mock_library.niFake_FunctionWithRepeatedCapabilityType_cfunc.return_value = 0
        mock_library.niFake_GetABoolean_cfunc.side_effect = MockFunctionCallError("niFake_GetABoolean_cfunc")
        mock_library.niFake_GetABoolean_cfunc.return_value = 0
        mock_library.niFake_GetANumber_cfunc.side_effect = MockFunctionCallError("niFake_GetANumber_cfunc")
        mock_library.niFake_GetANumber_cfunc.return_value = 0
        mock_library.niFake_GetAStringOfFixedMaximumSize_cfunc.side_effect = MockFunctionCallError("niFake_GetAStringOfFixedMaximumSize_cfunc")
        mock_library.niFake_GetAStringOfFixedMaximumSize_cfunc.return_value = 0
        mock_library.niFake_GetAStringUsingPythonCode_cfunc.side_effect = MockFunctionCallError("niFake_GetAStringUsingPythonCode_cfunc")
        mock_library.niFake_GetAStringUsingPythonCode_cfunc.return_value = 0
        mock_library.niFake_GetAnIviDanceString_cfunc.side_effect = MockFunctionCallError("niFake_GetAnIviDanceString_cfunc")
        mock_library.niFake_GetAnIviDanceString_cfunc.return_value = 0
        mock_library.niFake_GetAnIviDanceWithATwistString_cfunc.side_effect = MockFunctionCallError("niFake_GetAnIviDanceWithATwistString_cfunc")
        mock_library.niFake_GetAnIviDanceWithATwistString_cfunc.return_value = 0
        mock_library.niFake_GetArrayForPythonCodeCustomType_cfunc.side_effect = MockFunctionCallError("niFake_GetArrayForPythonCodeCustomType_cfunc")
        mock_library.niFake_GetArrayForPythonCodeCustomType_cfunc.return_value = 0
        mock_library.niFake_GetArrayForPythonCodeDouble_cfunc.side_effect = MockFunctionCallError("niFake_GetArrayForPythonCodeDouble_cfunc")
        mock_library.niFake_GetArrayForPythonCodeDouble_cfunc.return_value = 0
        mock_library.niFake_GetArraySizeForPythonCode_cfunc.side_effect = MockFunctionCallError("niFake_GetArraySizeForPythonCode_cfunc")
        mock_library.niFake_GetArraySizeForPythonCode_cfunc.return_value = 0
        mock_library.niFake_GetArrayUsingIviDance_cfunc.side_effect = MockFunctionCallError("niFake_GetArrayUsingIviDance_cfunc")
        mock_library.niFake_GetArrayUsingIviDance_cfunc.return_value = 0
        mock_library.niFake_GetAttributeViBoolean_cfunc.side_effect = MockFunctionCallError("niFake_GetAttributeViBoolean_cfunc")
        mock_library.niFake_GetAttributeViBoolean_cfunc.return_value = 0
        mock_library.niFake_GetAttributeViInt32_cfunc.side_effect = MockFunctionCallError("niFake_GetAttributeViInt32_cfunc")
        mock_library.niFake_GetAttributeViInt32_cfunc.return_value = 0
        mock_library.niFake_GetAttributeViInt64_cfunc.side_effect = MockFunctionCallError("niFake_GetAttributeViInt64_cfunc")
        mock_library.niFake_GetAttributeViInt64_cfunc.return_value = 0
        mock_library.niFake_GetAttributeViReal64_cfunc.side_effect = MockFunctionCallError("niFake_GetAttributeViReal64_cfunc")
        mock_library.niFake_GetAttributeViReal64_cfunc.return_value = 0
        mock_library.niFake_GetAttributeViString_cfunc.side_effect = MockFunctionCallError("niFake_GetAttributeViString_cfunc")
        mock_library.niFake_GetAttributeViString_cfunc.return_value = 0
        mock_library.niFake_GetCalDateAndTime_cfunc.side_effect = MockFunctionCallError("niFake_GetCalDateAndTime_cfunc")
        mock_library.niFake_GetCalDateAndTime_cfunc.return_value = 0
        mock_library.niFake_GetCalInterval_cfunc.side_effect = MockFunctionCallError("niFake_GetCalInterval_cfunc")
        mock_library.niFake_GetCalInterval_cfunc.return_value = 0
        mock_library.niFake_GetChannelNames_cfunc.side_effect = MockFunctionCallError("niFake_GetChannelNames_cfunc")
        mock_library.niFake_GetChannelNames_cfunc.return_value = 0
        mock_library.niFake_GetCustomType_cfunc.side_effect = MockFunctionCallError("niFake_GetCustomType_cfunc")
        mock_library.niFake_GetCustomType_cfunc.return_value = 0
        mock_library.niFake_GetCustomTypeArray_cfunc.side_effect = MockFunctionCallError("niFake_GetCustomTypeArray_cfunc")
        mock_library.niFake_GetCustomTypeArray_cfunc.return_value = 0
        mock_library.niFake_GetCustomTypeTypedef_cfunc.side_effect = MockFunctionCallError("niFake_GetCustomTypeTypedef_cfunc")
        mock_library.niFake_GetCustomTypeTypedef_cfunc.return_value = 0
        mock_library.niFake_GetEnumValue_cfunc.side_effect = MockFunctionCallError("niFake_GetEnumValue_cfunc")
        mock_library.niFake_GetEnumValue_cfunc.return_value = 0
        mock_library.niFake_GetError_cfunc.side_effect = MockFunctionCallError("niFake_GetError_cfunc")
        mock_library.niFake_GetError_cfunc.return_value = 0
        mock_library.niFake_ImportAttributeConfigurationBuffer_cfunc.side_effect = MockFunctionCallError("niFake_ImportAttributeConfigurationBuffer_cfunc")
        mock_library.niFake_ImportAttributeConfigurationBuffer_cfunc.return_value = 0
        mock_library.niFake_InitWithOptions_cfunc.side_effect = MockFunctionCallError("niFake_InitWithOptions_cfunc")
        mock_library.niFake_InitWithOptions_cfunc.return_value = 0
        mock_library.niFake_Initiate_cfunc.side_effect = MockFunctionCallError("niFake_Initiate_cfunc")
        mock_library.niFake_Initiate_cfunc.return_value = 0
        mock_library.niFake_LockSession_cfunc.side_effect = MockFunctionCallError("niFake_LockSession_cfunc")
        mock_library.niFake_LockSession_cfunc.return_value = 0
        mock_library.niFake_MultipleArrayTypes_cfunc.side_effect = MockFunctionCallError("niFake_MultipleArrayTypes_cfunc")
        mock_library.niFake_MultipleArrayTypes_cfunc.return_value = 0
        mock_library.niFake_MultipleArraysSameSize_cfunc.side_effect = MockFunctionCallError("niFake_MultipleArraysSameSize_cfunc")
        mock_library.niFake_MultipleArraysSameSize_cfunc.return_value = 0
        mock_library.niFake_OneInputFunction_cfunc.side_effect = MockFunctionCallError("niFake_OneInputFunction_cfunc")
        mock_library.niFake_OneInputFunction_cfunc.return_value = 0
        mock_library.niFake_ParametersAreMultipleTypes_cfunc.side_effect = MockFunctionCallError("niFake_ParametersAreMultipleTypes_cfunc")
        mock_library.niFake_ParametersAreMultipleTypes_cfunc.return_value = 0
        mock_library.niFake_PoorlyNamedSimpleFunction_cfunc.side_effect = MockFunctionCallError("niFake_PoorlyNamedSimpleFunction_cfunc")
        mock_library.niFake_PoorlyNamedSimpleFunction_cfunc.return_value = 0
        mock_library.niFake_Read_cfunc.side_effect = MockFunctionCallError("niFake_Read_cfunc")
        mock_library.niFake_Read_cfunc.return_value = 0
        mock_library.niFake_ReadFromChannel_cfunc.side_effect = MockFunctionCallError("niFake_ReadFromChannel_cfunc")
        mock_library.niFake_ReadFromChannel_cfunc.return_value = 0
        mock_library.niFake_ReturnANumberAndAString_cfunc.side_effect = MockFunctionCallError("niFake_ReturnANumberAndAString_cfunc")
        mock_library.niFake_ReturnANumberAndAString_cfunc.return_value = 0
        mock_library.niFake_ReturnDurationInSeconds_cfunc.side_effect = MockFunctionCallError("niFake_ReturnDurationInSeconds_cfunc")
        mock_library.niFake_ReturnDurationInSeconds_cfunc.return_value = 0
        mock_library.niFake_ReturnListOfDurationsInSeconds_cfunc.side_effect = MockFunctionCallError("niFake_ReturnListOfDurationsInSeconds_cfunc")
        mock_library.niFake_ReturnListOfDurationsInSeconds_cfunc.return_value = 0
        mock_library.niFake_ReturnMultipleTypes_cfunc.side_effect = MockFunctionCallError("niFake_ReturnMultipleTypes_cfunc")
        mock_library.niFake_ReturnMultipleTypes_cfunc.return_value = 0
        mock_library.niFake_SetAttributeViBoolean_cfunc.side_effect = MockFunctionCallError("niFake_SetAttributeViBoolean_cfunc")
        mock_library.niFake_SetAttributeViBoolean_cfunc.return_value = 0
        mock_library.niFake_SetAttributeViInt32_cfunc.side_effect = MockFunctionCallError("niFake_SetAttributeViInt32_cfunc")
        mock_library.niFake_SetAttributeViInt32_cfunc.return_value = 0
        mock_library.niFake_SetAttributeViInt64_cfunc.side_effect = MockFunctionCallError("niFake_SetAttributeViInt64_cfunc")
        mock_library.niFake_SetAttributeViInt64_cfunc.return_value = 0
        mock_library.niFake_SetAttributeViReal64_cfunc.side_effect = MockFunctionCallError("niFake_SetAttributeViReal64_cfunc")
        mock_library.niFake_SetAttributeViReal64_cfunc.return_value = 0
        mock_library.niFake_SetAttributeViString_cfunc.side_effect = MockFunctionCallError("niFake_SetAttributeViString_cfunc")
        mock_library.niFake_SetAttributeViString_cfunc.return_value = 0
        mock_library.niFake_SetCustomType_cfunc.side_effect = MockFunctionCallError("niFake_SetCustomType_cfunc")
        mock_library.niFake_SetCustomType_cfunc.return_value = 0
        mock_library.niFake_SetCustomTypeArray_cfunc.side_effect = MockFunctionCallError("niFake_SetCustomTypeArray_cfunc")
        mock_library.niFake_SetCustomTypeArray_cfunc.return_value = 0
        mock_library.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc.side_effect = MockFunctionCallError("niFake_StringValuedEnumInputFunctionWithDefaults_cfunc")
        mock_library.niFake_StringValuedEnumInputFunctionWithDefaults_cfunc.return_value = 0
        mock_library.niFake_TwoInputFunction_cfunc.side_effect = MockFunctionCallError("niFake_TwoInputFunction_cfunc")
        mock_library.niFake_TwoInputFunction_cfunc.return_value = 0
        mock_library.niFake_UnlockSession_cfunc.side_effect = MockFunctionCallError("niFake_UnlockSession_cfunc")
        mock_library.niFake_UnlockSession_cfunc.return_value = 0
        mock_library.niFake_Use64BitNumber_cfunc.side_effect = MockFunctionCallError("niFake_Use64BitNumber_cfunc")
        mock_library.niFake_Use64BitNumber_cfunc.return_value = 0
        mock_library.niFake_WriteWaveform_cfunc.side_effect = MockFunctionCallError("niFake_WriteWaveform_cfunc")
        mock_library.niFake_WriteWaveform_cfunc.return_value = 0
        mock_library.niFake_close_cfunc.side_effect = MockFunctionCallError("niFake_close_cfunc")
        mock_library.niFake_close_cfunc.return_value = 0
        mock_library.niFake_error_message_cfunc.side_effect = MockFunctionCallError("niFake_error_message_cfunc")
        mock_library.niFake_error_message_cfunc.return_value = 0
        mock_library.niFake_self_test_cfunc.side_effect = MockFunctionCallError("niFake_self_test_cfunc")
        mock_library.niFake_self_test_cfunc.return_value = 0
