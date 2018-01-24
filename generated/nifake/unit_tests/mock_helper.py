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
        self._defaults['BoolArrayOutputFunction'] = {}
        self._defaults['BoolArrayOutputFunction']['return'] = 0
        self._defaults['BoolArrayOutputFunction']['anArray'] = None
        self._defaults['EnumArrayOutputFunction'] = {}
        self._defaults['EnumArrayOutputFunction']['return'] = 0
        self._defaults['EnumArrayOutputFunction']['anArray'] = None
        self._defaults['EnumInputFunctionWithDefaults'] = {}
        self._defaults['EnumInputFunctionWithDefaults']['return'] = 0
        self._defaults['FetchWaveform'] = {}
        self._defaults['FetchWaveform']['return'] = 0
        self._defaults['FetchWaveform']['waveformData'] = None
        self._defaults['FetchWaveform']['actualNumberOfSamples'] = None
        self._defaults['GetABoolean'] = {}
        self._defaults['GetABoolean']['return'] = 0
        self._defaults['GetABoolean']['aBoolean'] = None
        self._defaults['GetANumber'] = {}
        self._defaults['GetANumber']['return'] = 0
        self._defaults['GetANumber']['aNumber'] = None
        self._defaults['GetAStringOfFixedMaximumSize'] = {}
        self._defaults['GetAStringOfFixedMaximumSize']['return'] = 0
        self._defaults['GetAStringOfFixedMaximumSize']['aString'] = None
        self._defaults['GetAnIviDanceString'] = {}
        self._defaults['GetAnIviDanceString']['return'] = 0
        self._defaults['GetAnIviDanceString']['aString'] = None
        self._defaults['GetArrayForPythonCodeCustomType'] = {}
        self._defaults['GetArrayForPythonCodeCustomType']['return'] = 0
        self._defaults['GetArrayForPythonCodeCustomType']['arrayOut'] = None
        self._defaults['GetArrayForPythonCodeDouble'] = {}
        self._defaults['GetArrayForPythonCodeDouble']['return'] = 0
        self._defaults['GetArrayForPythonCodeDouble']['arrayOut'] = None
        self._defaults['GetArraySizeForPythonCode'] = {}
        self._defaults['GetArraySizeForPythonCode']['return'] = 0
        self._defaults['GetArraySizeForPythonCode']['sizeOut'] = None
        self._defaults['GetArrayUsingIVIDance'] = {}
        self._defaults['GetArrayUsingIVIDance']['return'] = 0
        self._defaults['GetArrayUsingIVIDance']['arrayOut'] = None
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
        self._defaults['GetCalDateAndTime']['Month'] = None
        self._defaults['GetCalDateAndTime']['Day'] = None
        self._defaults['GetCalDateAndTime']['Year'] = None
        self._defaults['GetCalDateAndTime']['Hour'] = None
        self._defaults['GetCalDateAndTime']['Minute'] = None
        self._defaults['GetCustomType'] = {}
        self._defaults['GetCustomType']['return'] = 0
        self._defaults['GetCustomType']['cs'] = None
        self._defaults['GetCustomTypeArray'] = {}
        self._defaults['GetCustomTypeArray']['return'] = 0
        self._defaults['GetCustomTypeArray']['cs'] = None
        self._defaults['GetEnumValue'] = {}
        self._defaults['GetEnumValue']['return'] = 0
        self._defaults['GetEnumValue']['aQuantity'] = None
        self._defaults['GetEnumValue']['aTurtle'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['description'] = None
        self._defaults['GetLastCalDateAndTime'] = {}
        self._defaults['GetLastCalDateAndTime']['return'] = 0
        self._defaults['GetLastCalDateAndTime']['Month'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['MultipleArrayTypes'] = {}
        self._defaults['MultipleArrayTypes']['return'] = 0
        self._defaults['MultipleArrayTypes']['outputArray'] = None
        self._defaults['MultipleArrayTypes']['outputArrayOfFixedLength'] = None
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
        self._defaults['TwoInputFunction'] = {}
        self._defaults['TwoInputFunction']['return'] = 0
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

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niFake_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niFake_BoolArrayOutputFunction(self, vi, number_of_elements, an_array):  # noqa: N802
        if self._defaults['BoolArrayOutputFunction']['return'] != 0:
            return self._defaults['BoolArrayOutputFunction']['return']
        # an_array
        if self._defaults['BoolArrayOutputFunction']['anArray'] is None:
            raise MockFunctionCallError("niFake_BoolArrayOutputFunction", param='anArray')
        a = self._defaults['BoolArrayOutputFunction']['anArray']
        try:
            an_array_ref = an_array.contents
        except AttributeError:
            an_array_ref = an_array
        for i in range(min(len(an_array_ref), len(a))):
            an_array_ref[i] = a[i]
        return self._defaults['BoolArrayOutputFunction']['return']

    def niFake_EnumArrayOutputFunction(self, vi, number_of_elements, an_array):  # noqa: N802
        if self._defaults['EnumArrayOutputFunction']['return'] != 0:
            return self._defaults['EnumArrayOutputFunction']['return']
        # an_array
        if self._defaults['EnumArrayOutputFunction']['anArray'] is None:
            raise MockFunctionCallError("niFake_EnumArrayOutputFunction", param='anArray')
        a = self._defaults['EnumArrayOutputFunction']['anArray']
        try:
            an_array_ref = an_array.contents
        except AttributeError:
            an_array_ref = an_array
        for i in range(min(len(an_array_ref), len(a))):
            an_array_ref[i] = a[i]
        return self._defaults['EnumArrayOutputFunction']['return']

    def niFake_EnumInputFunctionWithDefaults(self, vi, a_turtle):  # noqa: N802
        if self._defaults['EnumInputFunctionWithDefaults']['return'] != 0:
            return self._defaults['EnumInputFunctionWithDefaults']['return']
        return self._defaults['EnumInputFunctionWithDefaults']['return']

    def niFake_FetchWaveform(self, vi, number_of_samples, waveform_data, actual_number_of_samples):  # noqa: N802
        if self._defaults['FetchWaveform']['return'] != 0:
            return self._defaults['FetchWaveform']['return']
        # waveform_data
        if self._defaults['FetchWaveform']['waveformData'] is None:
            raise MockFunctionCallError("niFake_FetchWaveform", param='waveformData')
        a = self._defaults['FetchWaveform']['waveformData']
        try:
            waveform_data_ref = waveform_data.contents
        except AttributeError:
            waveform_data_ref = waveform_data
        for i in range(min(len(waveform_data_ref), len(a))):
            waveform_data_ref[i] = a[i]
        # actual_number_of_samples
        if self._defaults['FetchWaveform']['actualNumberOfSamples'] is None:
            raise MockFunctionCallError("niFake_FetchWaveform", param='actualNumberOfSamples')
        actual_number_of_samples.contents.value = self._defaults['FetchWaveform']['actualNumberOfSamples']
        return self._defaults['FetchWaveform']['return']

    def niFake_GetABoolean(self, vi, a_boolean):  # noqa: N802
        if self._defaults['GetABoolean']['return'] != 0:
            return self._defaults['GetABoolean']['return']
        # a_boolean
        if self._defaults['GetABoolean']['aBoolean'] is None:
            raise MockFunctionCallError("niFake_GetABoolean", param='aBoolean')
        a_boolean.contents.value = self._defaults['GetABoolean']['aBoolean']
        return self._defaults['GetABoolean']['return']

    def niFake_GetANumber(self, vi, a_number):  # noqa: N802
        if self._defaults['GetANumber']['return'] != 0:
            return self._defaults['GetANumber']['return']
        # a_number
        if self._defaults['GetANumber']['aNumber'] is None:
            raise MockFunctionCallError("niFake_GetANumber", param='aNumber')
        a_number.contents.value = self._defaults['GetANumber']['aNumber']
        return self._defaults['GetANumber']['return']

    def niFake_GetAStringOfFixedMaximumSize(self, vi, a_string):  # noqa: N802
        if self._defaults['GetAStringOfFixedMaximumSize']['return'] != 0:
            return self._defaults['GetAStringOfFixedMaximumSize']['return']
        # a_string
        if self._defaults['GetAStringOfFixedMaximumSize']['aString'] is None:
            raise MockFunctionCallError("niFake_GetAStringOfFixedMaximumSize", param='aString')
        a = self._defaults['GetAStringOfFixedMaximumSize']['aString']
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(a_string), len(a))):
            a_string[i] = a[i]
        return self._defaults['GetAStringOfFixedMaximumSize']['return']

    def niFake_GetAnIviDanceString(self, vi, buffer_size, a_string):  # noqa: N802
        if self._defaults['GetAnIviDanceString']['return'] != 0:
            return self._defaults['GetAnIviDanceString']['return']
        if self._defaults['GetAnIviDanceString']['aString'] is None:
            raise MockFunctionCallError("niFake_GetAnIviDanceString", param='aString')
        if buffer_size.value == 0:
            return len(self._defaults['GetAnIviDanceString']['aString'])
        a_string.value = self._defaults['GetAnIviDanceString']['aString'].encode('ascii')
        return self._defaults['GetAnIviDanceString']['return']

    def niFake_GetArrayForPythonCodeCustomType(self, vi, number_of_elements, array_out):  # noqa: N802
        if self._defaults['GetArrayForPythonCodeCustomType']['return'] != 0:
            return self._defaults['GetArrayForPythonCodeCustomType']['return']
        # array_out
        if self._defaults['GetArrayForPythonCodeCustomType']['arrayOut'] is None:
            raise MockFunctionCallError("niFake_GetArrayForPythonCodeCustomType", param='arrayOut')
        a = self._defaults['GetArrayForPythonCodeCustomType']['arrayOut']
        try:
            array_out_ref = array_out.contents
        except AttributeError:
            array_out_ref = array_out
        for i in range(min(len(array_out_ref), len(a))):
            array_out_ref[i] = a[i]
        return self._defaults['GetArrayForPythonCodeCustomType']['return']

    def niFake_GetArrayForPythonCodeDouble(self, vi, number_of_elements, array_out):  # noqa: N802
        if self._defaults['GetArrayForPythonCodeDouble']['return'] != 0:
            return self._defaults['GetArrayForPythonCodeDouble']['return']
        # array_out
        if self._defaults['GetArrayForPythonCodeDouble']['arrayOut'] is None:
            raise MockFunctionCallError("niFake_GetArrayForPythonCodeDouble", param='arrayOut')
        a = self._defaults['GetArrayForPythonCodeDouble']['arrayOut']
        try:
            array_out_ref = array_out.contents
        except AttributeError:
            array_out_ref = array_out
        for i in range(min(len(array_out_ref), len(a))):
            array_out_ref[i] = a[i]
        return self._defaults['GetArrayForPythonCodeDouble']['return']

    def niFake_GetArraySizeForPythonCode(self, vi, size_out):  # noqa: N802
        if self._defaults['GetArraySizeForPythonCode']['return'] != 0:
            return self._defaults['GetArraySizeForPythonCode']['return']
        # size_out
        if self._defaults['GetArraySizeForPythonCode']['sizeOut'] is None:
            raise MockFunctionCallError("niFake_GetArraySizeForPythonCode", param='sizeOut')
        size_out.contents.value = self._defaults['GetArraySizeForPythonCode']['sizeOut']
        return self._defaults['GetArraySizeForPythonCode']['return']

    def niFake_GetArrayUsingIVIDance(self, vi, array_size, array_out):  # noqa: N802
        if self._defaults['GetArrayUsingIVIDance']['return'] != 0:
            return self._defaults['GetArrayUsingIVIDance']['return']
        if self._defaults['GetArrayUsingIVIDance']['arrayOut'] is None:
            raise MockFunctionCallError("niFake_GetArrayUsingIVIDance", param='arrayOut')
        if array_size.value == 0:
            return len(self._defaults['GetArrayUsingIVIDance']['arrayOut'])
        try:
            array_out_ref = array_out.contents
        except AttributeError:
            array_out_ref = array_out
        for i in range(len(self._defaults['GetArrayUsingIVIDance']['arrayOut'])):
            array_out_ref[i] = self._defaults['GetArrayUsingIVIDance']['arrayOut'][i]
        return self._defaults['GetArrayUsingIVIDance']['return']

    def niFake_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViBoolean", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niFake_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViInt32", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niFake_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt64']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViInt64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt64']['attributeValue']
        return self._defaults['GetAttributeViInt64']['return']

    def niFake_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViReal64", param='attributeValue')
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
        if self._defaults['GetCalDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='Month')
        month.contents.value = self._defaults['GetCalDateAndTime']['Month']
        # day
        if self._defaults['GetCalDateAndTime']['Day'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='Day')
        day.contents.value = self._defaults['GetCalDateAndTime']['Day']
        # year
        if self._defaults['GetCalDateAndTime']['Year'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='Year')
        year.contents.value = self._defaults['GetCalDateAndTime']['Year']
        # hour
        if self._defaults['GetCalDateAndTime']['Hour'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='Hour')
        hour.contents.value = self._defaults['GetCalDateAndTime']['Hour']
        # minute
        if self._defaults['GetCalDateAndTime']['Minute'] is None:
            raise MockFunctionCallError("niFake_GetCalDateAndTime", param='Minute')
        minute.contents.value = self._defaults['GetCalDateAndTime']['Minute']
        return self._defaults['GetCalDateAndTime']['return']

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
        a = self._defaults['GetCustomTypeArray']['cs']
        try:
            cs_ref = cs.contents
        except AttributeError:
            cs_ref = cs
        for i in range(min(len(cs_ref), len(a))):
            cs_ref[i] = a[i]
        return self._defaults['GetCustomTypeArray']['return']

    def niFake_GetEnumValue(self, vi, a_quantity, a_turtle):  # noqa: N802
        if self._defaults['GetEnumValue']['return'] != 0:
            return self._defaults['GetEnumValue']['return']
        # a_quantity
        if self._defaults['GetEnumValue']['aQuantity'] is None:
            raise MockFunctionCallError("niFake_GetEnumValue", param='aQuantity')
        a_quantity.contents.value = self._defaults['GetEnumValue']['aQuantity']
        # a_turtle
        if self._defaults['GetEnumValue']['aTurtle'] is None:
            raise MockFunctionCallError("niFake_GetEnumValue", param='aTurtle')
        a_turtle.contents.value = self._defaults['GetEnumValue']['aTurtle']
        return self._defaults['GetEnumValue']['return']

    def niFake_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niFake_GetError", param='errorCode')
        error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niFake_GetError", param='description')
        if buffer_size.value == 0:
            return len(self._defaults['GetError']['description'])
        description.value = self._defaults['GetError']['description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niFake_GetLastCalDateAndTime(self, vi, cal_type, month):  # noqa: N802
        if self._defaults['GetLastCalDateAndTime']['return'] != 0:
            return self._defaults['GetLastCalDateAndTime']['return']
        # month
        if self._defaults['GetLastCalDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niFake_GetLastCalDateAndTime", param='Month')
        month.contents.value = self._defaults['GetLastCalDateAndTime']['Month']
        return self._defaults['GetLastCalDateAndTime']['return']

    def niFake_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        # vi
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niFake_InitWithOptions", param='vi')
        vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niFake_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niFake_MultipleArrayTypes(self, vi, output_array_size, output_array, output_array_of_fixed_length, input_array_sizes, input_array_of_floats, input_array_of_integers):  # noqa: N802
        if self._defaults['MultipleArrayTypes']['return'] != 0:
            return self._defaults['MultipleArrayTypes']['return']
        # output_array
        if self._defaults['MultipleArrayTypes']['outputArray'] is None:
            raise MockFunctionCallError("niFake_MultipleArrayTypes", param='outputArray')
        a = self._defaults['MultipleArrayTypes']['outputArray']
        try:
            output_array_ref = output_array.contents
        except AttributeError:
            output_array_ref = output_array
        for i in range(min(len(output_array_ref), len(a))):
            output_array_ref[i] = a[i]
        # output_array_of_fixed_length
        if self._defaults['MultipleArrayTypes']['outputArrayOfFixedLength'] is None:
            raise MockFunctionCallError("niFake_MultipleArrayTypes", param='outputArrayOfFixedLength')
        a = self._defaults['MultipleArrayTypes']['outputArrayOfFixedLength']
        try:
            output_array_of_fixed_length_ref = output_array_of_fixed_length.contents
        except AttributeError:
            output_array_of_fixed_length_ref = output_array_of_fixed_length
        for i in range(min(len(output_array_of_fixed_length_ref), len(a))):
            output_array_of_fixed_length_ref[i] = a[i]
        return self._defaults['MultipleArrayTypes']['return']

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
        reading.contents.value = self._defaults['Read']['reading']
        return self._defaults['Read']['return']

    def niFake_ReadFromChannel(self, vi, channel_name, maximum_time, reading):  # noqa: N802
        if self._defaults['ReadFromChannel']['return'] != 0:
            return self._defaults['ReadFromChannel']['return']
        # reading
        if self._defaults['ReadFromChannel']['reading'] is None:
            raise MockFunctionCallError("niFake_ReadFromChannel", param='reading')
        reading.contents.value = self._defaults['ReadFromChannel']['reading']
        return self._defaults['ReadFromChannel']['return']

    def niFake_ReturnANumberAndAString(self, vi, a_number, a_string):  # noqa: N802
        if self._defaults['ReturnANumberAndAString']['return'] != 0:
            return self._defaults['ReturnANumberAndAString']['return']
        # a_number
        if self._defaults['ReturnANumberAndAString']['aNumber'] is None:
            raise MockFunctionCallError("niFake_ReturnANumberAndAString", param='aNumber')
        a_number.contents.value = self._defaults['ReturnANumberAndAString']['aNumber']
        # a_string
        if self._defaults['ReturnANumberAndAString']['aString'] is None:
            raise MockFunctionCallError("niFake_ReturnANumberAndAString", param='aString')
        a = self._defaults['ReturnANumberAndAString']['aString']
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(a_string), len(a))):
            a_string[i] = a[i]
        return self._defaults['ReturnANumberAndAString']['return']

    def niFake_ReturnMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, array_size, an_array, string_size, a_string):  # noqa: N802
        if self._defaults['ReturnMultipleTypes']['return'] != 0:
            return self._defaults['ReturnMultipleTypes']['return']
        # a_boolean
        if self._defaults['ReturnMultipleTypes']['aBoolean'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='aBoolean')
        a_boolean.contents.value = self._defaults['ReturnMultipleTypes']['aBoolean']
        # an_int32
        if self._defaults['ReturnMultipleTypes']['anInt32'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anInt32')
        an_int32.contents.value = self._defaults['ReturnMultipleTypes']['anInt32']
        # an_int64
        if self._defaults['ReturnMultipleTypes']['anInt64'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anInt64')
        an_int64.contents.value = self._defaults['ReturnMultipleTypes']['anInt64']
        # an_int_enum
        if self._defaults['ReturnMultipleTypes']['anIntEnum'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anIntEnum')
        an_int_enum.contents.value = self._defaults['ReturnMultipleTypes']['anIntEnum']
        # a_float
        if self._defaults['ReturnMultipleTypes']['aFloat'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='aFloat')
        a_float.contents.value = self._defaults['ReturnMultipleTypes']['aFloat']
        # a_float_enum
        if self._defaults['ReturnMultipleTypes']['aFloatEnum'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='aFloatEnum')
        a_float_enum.contents.value = self._defaults['ReturnMultipleTypes']['aFloatEnum']
        # an_array
        if self._defaults['ReturnMultipleTypes']['anArray'] is None:
            raise MockFunctionCallError("niFake_ReturnMultipleTypes", param='anArray')
        a = self._defaults['ReturnMultipleTypes']['anArray']
        try:
            an_array_ref = an_array.contents
        except AttributeError:
            an_array_ref = an_array
        for i in range(min(len(an_array_ref), len(a))):
            an_array_ref[i] = a[i]
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

    def niFake_TwoInputFunction(self, vi, a_number, a_string):  # noqa: N802
        if self._defaults['TwoInputFunction']['return'] != 0:
            return self._defaults['TwoInputFunction']['return']
        return self._defaults['TwoInputFunction']['return']

    def niFake_Use64BitNumber(self, vi, input, output):  # noqa: N802
        if self._defaults['Use64BitNumber']['return'] != 0:
            return self._defaults['Use64BitNumber']['return']
        # output
        if self._defaults['Use64BitNumber']['output'] is None:
            raise MockFunctionCallError("niFake_Use64BitNumber", param='output')
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
        a = self._defaults['error_message']['errorMessage']
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(error_message), len(a))):
            error_message[i] = a[i]
        return self._defaults['error_message']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niFake_Abort.side_effect = MockFunctionCallError("niFake_Abort")
        mock_library.niFake_Abort.return_value = 0
        mock_library.niFake_BoolArrayOutputFunction.side_effect = MockFunctionCallError("niFake_BoolArrayOutputFunction")
        mock_library.niFake_BoolArrayOutputFunction.return_value = 0
        mock_library.niFake_EnumArrayOutputFunction.side_effect = MockFunctionCallError("niFake_EnumArrayOutputFunction")
        mock_library.niFake_EnumArrayOutputFunction.return_value = 0
        mock_library.niFake_EnumInputFunctionWithDefaults.side_effect = MockFunctionCallError("niFake_EnumInputFunctionWithDefaults")
        mock_library.niFake_EnumInputFunctionWithDefaults.return_value = 0
        mock_library.niFake_FetchWaveform.side_effect = MockFunctionCallError("niFake_FetchWaveform")
        mock_library.niFake_FetchWaveform.return_value = 0
        mock_library.niFake_GetABoolean.side_effect = MockFunctionCallError("niFake_GetABoolean")
        mock_library.niFake_GetABoolean.return_value = 0
        mock_library.niFake_GetANumber.side_effect = MockFunctionCallError("niFake_GetANumber")
        mock_library.niFake_GetANumber.return_value = 0
        mock_library.niFake_GetAStringOfFixedMaximumSize.side_effect = MockFunctionCallError("niFake_GetAStringOfFixedMaximumSize")
        mock_library.niFake_GetAStringOfFixedMaximumSize.return_value = 0
        mock_library.niFake_GetAnIviDanceString.side_effect = MockFunctionCallError("niFake_GetAnIviDanceString")
        mock_library.niFake_GetAnIviDanceString.return_value = 0
        mock_library.niFake_GetArrayForPythonCodeCustomType.side_effect = MockFunctionCallError("niFake_GetArrayForPythonCodeCustomType")
        mock_library.niFake_GetArrayForPythonCodeCustomType.return_value = 0
        mock_library.niFake_GetArrayForPythonCodeDouble.side_effect = MockFunctionCallError("niFake_GetArrayForPythonCodeDouble")
        mock_library.niFake_GetArrayForPythonCodeDouble.return_value = 0
        mock_library.niFake_GetArraySizeForPythonCode.side_effect = MockFunctionCallError("niFake_GetArraySizeForPythonCode")
        mock_library.niFake_GetArraySizeForPythonCode.return_value = 0
        mock_library.niFake_GetArrayUsingIVIDance.side_effect = MockFunctionCallError("niFake_GetArrayUsingIVIDance")
        mock_library.niFake_GetArrayUsingIVIDance.return_value = 0
        mock_library.niFake_GetAttributeViBoolean.side_effect = MockFunctionCallError("niFake_GetAttributeViBoolean")
        mock_library.niFake_GetAttributeViBoolean.return_value = 0
        mock_library.niFake_GetAttributeViInt32.side_effect = MockFunctionCallError("niFake_GetAttributeViInt32")
        mock_library.niFake_GetAttributeViInt32.return_value = 0
        mock_library.niFake_GetAttributeViInt64.side_effect = MockFunctionCallError("niFake_GetAttributeViInt64")
        mock_library.niFake_GetAttributeViInt64.return_value = 0
        mock_library.niFake_GetAttributeViReal64.side_effect = MockFunctionCallError("niFake_GetAttributeViReal64")
        mock_library.niFake_GetAttributeViReal64.return_value = 0
        mock_library.niFake_GetAttributeViString.side_effect = MockFunctionCallError("niFake_GetAttributeViString")
        mock_library.niFake_GetAttributeViString.return_value = 0
        mock_library.niFake_GetCalDateAndTime.side_effect = MockFunctionCallError("niFake_GetCalDateAndTime")
        mock_library.niFake_GetCalDateAndTime.return_value = 0
        mock_library.niFake_GetCustomType.side_effect = MockFunctionCallError("niFake_GetCustomType")
        mock_library.niFake_GetCustomType.return_value = 0
        mock_library.niFake_GetCustomTypeArray.side_effect = MockFunctionCallError("niFake_GetCustomTypeArray")
        mock_library.niFake_GetCustomTypeArray.return_value = 0
        mock_library.niFake_GetEnumValue.side_effect = MockFunctionCallError("niFake_GetEnumValue")
        mock_library.niFake_GetEnumValue.return_value = 0
        mock_library.niFake_GetError.side_effect = MockFunctionCallError("niFake_GetError")
        mock_library.niFake_GetError.return_value = 0
        mock_library.niFake_GetLastCalDateAndTime.side_effect = MockFunctionCallError("niFake_GetLastCalDateAndTime")
        mock_library.niFake_GetLastCalDateAndTime.return_value = 0
        mock_library.niFake_InitWithOptions.side_effect = MockFunctionCallError("niFake_InitWithOptions")
        mock_library.niFake_InitWithOptions.return_value = 0
        mock_library.niFake_Initiate.side_effect = MockFunctionCallError("niFake_Initiate")
        mock_library.niFake_Initiate.return_value = 0
        mock_library.niFake_MultipleArrayTypes.side_effect = MockFunctionCallError("niFake_MultipleArrayTypes")
        mock_library.niFake_MultipleArrayTypes.return_value = 0
        mock_library.niFake_OneInputFunction.side_effect = MockFunctionCallError("niFake_OneInputFunction")
        mock_library.niFake_OneInputFunction.return_value = 0
        mock_library.niFake_ParametersAreMultipleTypes.side_effect = MockFunctionCallError("niFake_ParametersAreMultipleTypes")
        mock_library.niFake_ParametersAreMultipleTypes.return_value = 0
        mock_library.niFake_PoorlyNamedSimpleFunction.side_effect = MockFunctionCallError("niFake_PoorlyNamedSimpleFunction")
        mock_library.niFake_PoorlyNamedSimpleFunction.return_value = 0
        mock_library.niFake_Read.side_effect = MockFunctionCallError("niFake_Read")
        mock_library.niFake_Read.return_value = 0
        mock_library.niFake_ReadFromChannel.side_effect = MockFunctionCallError("niFake_ReadFromChannel")
        mock_library.niFake_ReadFromChannel.return_value = 0
        mock_library.niFake_ReturnANumberAndAString.side_effect = MockFunctionCallError("niFake_ReturnANumberAndAString")
        mock_library.niFake_ReturnANumberAndAString.return_value = 0
        mock_library.niFake_ReturnMultipleTypes.side_effect = MockFunctionCallError("niFake_ReturnMultipleTypes")
        mock_library.niFake_ReturnMultipleTypes.return_value = 0
        mock_library.niFake_SetAttributeViBoolean.side_effect = MockFunctionCallError("niFake_SetAttributeViBoolean")
        mock_library.niFake_SetAttributeViBoolean.return_value = 0
        mock_library.niFake_SetAttributeViInt32.side_effect = MockFunctionCallError("niFake_SetAttributeViInt32")
        mock_library.niFake_SetAttributeViInt32.return_value = 0
        mock_library.niFake_SetAttributeViInt64.side_effect = MockFunctionCallError("niFake_SetAttributeViInt64")
        mock_library.niFake_SetAttributeViInt64.return_value = 0
        mock_library.niFake_SetAttributeViReal64.side_effect = MockFunctionCallError("niFake_SetAttributeViReal64")
        mock_library.niFake_SetAttributeViReal64.return_value = 0
        mock_library.niFake_SetAttributeViString.side_effect = MockFunctionCallError("niFake_SetAttributeViString")
        mock_library.niFake_SetAttributeViString.return_value = 0
        mock_library.niFake_SetCustomType.side_effect = MockFunctionCallError("niFake_SetCustomType")
        mock_library.niFake_SetCustomType.return_value = 0
        mock_library.niFake_SetCustomTypeArray.side_effect = MockFunctionCallError("niFake_SetCustomTypeArray")
        mock_library.niFake_SetCustomTypeArray.return_value = 0
        mock_library.niFake_TwoInputFunction.side_effect = MockFunctionCallError("niFake_TwoInputFunction")
        mock_library.niFake_TwoInputFunction.return_value = 0
        mock_library.niFake_Use64BitNumber.side_effect = MockFunctionCallError("niFake_Use64BitNumber")
        mock_library.niFake_Use64BitNumber.return_value = 0
        mock_library.niFake_WriteWaveform.side_effect = MockFunctionCallError("niFake_WriteWaveform")
        mock_library.niFake_WriteWaveform.return_value = 0
        mock_library.niFake_close.side_effect = MockFunctionCallError("niFake_close")
        mock_library.niFake_close.return_value = 0
        mock_library.niFake_error_message.side_effect = MockFunctionCallError("niFake_error_message")
        mock_library.niFake_error_message.return_value = 0
