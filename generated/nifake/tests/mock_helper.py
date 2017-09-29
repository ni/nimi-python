# This file was generated

import ctypes

import nifake.ctypes_types
import nifake.python_types


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
        self._defaults['EnumInputFunctionWithDefaults'] = {}
        self._defaults['EnumInputFunctionWithDefaults']['return'] = 0
        self._defaults['GetABoolean'] = {}
        self._defaults['GetABoolean']['return'] = 0
        self._defaults['GetABoolean']['aBoolean'] = None
        self._defaults['GetANumber'] = {}
        self._defaults['GetANumber']['return'] = 0
        self._defaults['GetANumber']['aNumber'] = None
        self._defaults['GetAStringOfFixedMaximumSize'] = {}
        self._defaults['GetAStringOfFixedMaximumSize']['return'] = 0
        self._defaults['GetAStringOfFixedMaximumSize']['aString'] = None
        self._defaults['GetAStringWithSpecifiedMaximumSize'] = {}
        self._defaults['GetAStringWithSpecifiedMaximumSize']['return'] = 0
        self._defaults['GetAStringWithSpecifiedMaximumSize']['aString'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViSession'] = {}
        self._defaults['GetAttributeViSession']['return'] = 0
        self._defaults['GetAttributeViSession']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetEnumValue'] = {}
        self._defaults['GetEnumValue']['return'] = 0
        self._defaults['GetEnumValue']['aQuantity'] = None
        self._defaults['GetEnumValue']['aTurtle'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['description'] = None
        self._defaults['GetErrorMessage'] = {}
        self._defaults['GetErrorMessage']['return'] = 0
        self._defaults['GetErrorMessage']['errorMessage'] = None
        self._defaults['InitWithOptions'] = {}
        self._defaults['InitWithOptions']['return'] = 0
        self._defaults['InitWithOptions']['vi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['OneInputFunction'] = {}
        self._defaults['OneInputFunction']['return'] = 0
        self._defaults['Read'] = {}
        self._defaults['Read']['return'] = 0
        self._defaults['Read']['reading'] = None
        self._defaults['ReadFromChannel'] = {}
        self._defaults['ReadFromChannel']['return'] = 0
        self._defaults['ReadFromChannel']['reading'] = None
        self._defaults['ReadMultiPoint'] = {}
        self._defaults['ReadMultiPoint']['return'] = 0
        self._defaults['ReadMultiPoint']['readingArray'] = None
        self._defaults['ReadMultiPoint']['actualNumberOfPoints'] = None
        self._defaults['ReturnANumberAndAString'] = {}
        self._defaults['ReturnANumberAndAString']['return'] = 0
        self._defaults['ReturnANumberAndAString']['aNumber'] = None
        self._defaults['ReturnANumberAndAString']['aString'] = None
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViSession'] = {}
        self._defaults['SetAttributeViSession']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SimpleFunction'] = {}
        self._defaults['SimpleFunction']['return'] = 0
        self._defaults['TwoInputFunction'] = {}
        self._defaults['TwoInputFunction']['return'] = 0
        self._defaults['Use64BitNumber'] = {}
        self._defaults['Use64BitNumber']['return'] = 0
        self._defaults['Use64BitNumber']['output'] = None
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niFake_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niFake_EnumInputFunctionWithDefaults(self, vi, a_turtle):  # noqa: N802
        if self._defaults['EnumInputFunctionWithDefaults']['return'] != 0:
            return self._defaults['EnumInputFunctionWithDefaults']['return']
        return self._defaults['EnumInputFunctionWithDefaults']['return']

    def niFake_GetABoolean(self, vi, a_boolean):  # noqa: N802
        if self._defaults['GetABoolean']['return'] != 0:
            return self._defaults['GetABoolean']['return']
        if self._defaults['GetABoolean']['aBoolean'] is None:
            raise MockFunctionCallError("niFake_GetABoolean", param='aBoolean')
        a_boolean.contents.value = self._defaults['GetABoolean']['aBoolean']
        return self._defaults['GetABoolean']['return']

    def niFake_GetANumber(self, vi, a_number):  # noqa: N802
        if self._defaults['GetANumber']['return'] != 0:
            return self._defaults['GetANumber']['return']
        if self._defaults['GetANumber']['aNumber'] is None:
            raise MockFunctionCallError("niFake_GetANumber", param='aNumber')
        a_number.contents.value = self._defaults['GetANumber']['aNumber']
        return self._defaults['GetANumber']['return']

    def niFake_GetAStringOfFixedMaximumSize(self, vi, a_string):  # noqa: N802
        if self._defaults['GetAStringOfFixedMaximumSize']['return'] != 0:
            return self._defaults['GetAStringOfFixedMaximumSize']['return']
        if self._defaults['GetAStringOfFixedMaximumSize']['aString'] is None:
            raise MockFunctionCallError("niFake_GetAStringOfFixedMaximumSize", param='aString')
        a_string.contents.value = self._defaults['GetAStringOfFixedMaximumSize']['aString']
        return self._defaults['GetAStringOfFixedMaximumSize']['return']

    def niFake_GetAStringWithSpecifiedMaximumSize(self, vi, a_string, buffer_size):  # noqa: N802
        if self._defaults['GetAStringWithSpecifiedMaximumSize']['return'] != 0:
            return self._defaults['GetAStringWithSpecifiedMaximumSize']['return']
        if self._defaults['GetAStringWithSpecifiedMaximumSize']['aString'] is None:
            raise MockFunctionCallError("niFake_GetAStringWithSpecifiedMaximumSize", param='aString')
        a_string.contents.value = self._defaults['GetAStringWithSpecifiedMaximumSize']['aString']
        return self._defaults['GetAStringWithSpecifiedMaximumSize']['return']

    def niFake_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViBoolean", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niFake_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViInt32", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niFake_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViReal64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niFake_GetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViSession']['return'] != 0:
            return self._defaults['GetAttributeViSession']['return']
        if self._defaults['GetAttributeViSession']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViSession", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViSession']['attributeValue']
        return self._defaults['GetAttributeViSession']['return']

    def niFake_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niFake_GetAttributeViString", param='attributeValue')
        if buffer_size == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        t = nifake.ctypes_types.ViString_ctype(self._defaults['GetAttributeViString']['attributeValue'].encode('ascii'))
        attribute_value.value = ctypes.cast(t, nifake.ctypes_types.ViString_ctype).value
        return self._defaults['GetAttributeViString']['return']

    def niFake_GetEnumValue(self, vi, a_quantity, a_turtle):  # noqa: N802
        if self._defaults['GetEnumValue']['return'] != 0:
            return self._defaults['GetEnumValue']['return']
        if self._defaults['GetEnumValue']['aQuantity'] is None:
            raise MockFunctionCallError("niFake_GetEnumValue", param='aQuantity')
        a_quantity.contents.value = self._defaults['GetEnumValue']['aQuantity']
        if self._defaults['GetEnumValue']['aTurtle'] is None:
            raise MockFunctionCallError("niFake_GetEnumValue", param='aTurtle')
        a_turtle.contents.value = self._defaults['GetEnumValue']['aTurtle']
        return self._defaults['GetEnumValue']['return']

    def niFake_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niFake_GetError", param='errorCode')
        error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niFake_GetError", param='description')
        if buffer_size == 0:
            return len(self._defaults['GetError']['description'])
        t = nifake.ctypes_types.ViString_ctype(self._defaults['GetError']['description'].encode('ascii'))
        description.value = ctypes.cast(t, nifake.ctypes_types.ViString_ctype).value
        return self._defaults['GetError']['return']

    def niFake_GetErrorMessage(self, vi, error_code, buffer_size, error_message):  # noqa: N802
        if self._defaults['GetErrorMessage']['return'] != 0:
            return self._defaults['GetErrorMessage']['return']
        if self._defaults['GetErrorMessage']['errorMessage'] is None:
            raise MockFunctionCallError("niFake_GetErrorMessage", param='errorMessage')
        if buffer_size == 0:
            return len(self._defaults['GetErrorMessage']['errorMessage'])
        t = nifake.ctypes_types.ViString_ctype(self._defaults['GetErrorMessage']['errorMessage'].encode('ascii'))
        error_message.value = ctypes.cast(t, nifake.ctypes_types.ViString_ctype).value
        return self._defaults['GetErrorMessage']['return']

    def niFake_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitWithOptions']['return'] != 0:
            return self._defaults['InitWithOptions']['return']
        if self._defaults['InitWithOptions']['vi'] is None:
            raise MockFunctionCallError("niFake_InitWithOptions", param='vi')
        vi.contents.value = self._defaults['InitWithOptions']['vi']
        return self._defaults['InitWithOptions']['return']

    def niFake_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niFake_OneInputFunction(self, vi, a_number):  # noqa: N802
        if self._defaults['OneInputFunction']['return'] != 0:
            return self._defaults['OneInputFunction']['return']
        return self._defaults['OneInputFunction']['return']

    def niFake_Read(self, vi, maximum_time, reading):  # noqa: N802
        if self._defaults['Read']['return'] != 0:
            return self._defaults['Read']['return']
        if self._defaults['Read']['reading'] is None:
            raise MockFunctionCallError("niFake_Read", param='reading')
        reading.contents.value = self._defaults['Read']['reading']
        return self._defaults['Read']['return']

    def niFake_ReadFromChannel(self, vi, channel_name, maximum_time, reading):  # noqa: N802
        if self._defaults['ReadFromChannel']['return'] != 0:
            return self._defaults['ReadFromChannel']['return']
        if self._defaults['ReadFromChannel']['reading'] is None:
            raise MockFunctionCallError("niFake_ReadFromChannel", param='reading')
        reading.contents.value = self._defaults['ReadFromChannel']['reading']
        return self._defaults['ReadFromChannel']['return']

    def niFake_ReadMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points):  # noqa: N802
        if self._defaults['ReadMultiPoint']['return'] != 0:
            return self._defaults['ReadMultiPoint']['return']
        if self._defaults['ReadMultiPoint']['readingArray'] is None:
            raise MockFunctionCallError("niFake_ReadMultiPoint", param='readingArray')
        reading_array.contents.value = self._defaults['ReadMultiPoint']['readingArray']
        if self._defaults['ReadMultiPoint']['actualNumberOfPoints'] is None:
            raise MockFunctionCallError("niFake_ReadMultiPoint", param='actualNumberOfPoints')
        actual_number_of_points.contents.value = self._defaults['ReadMultiPoint']['actualNumberOfPoints']
        return self._defaults['ReadMultiPoint']['return']

    def niFake_ReturnANumberAndAString(self, vi, a_number, a_string):  # noqa: N802
        if self._defaults['ReturnANumberAndAString']['return'] != 0:
            return self._defaults['ReturnANumberAndAString']['return']
        if self._defaults['ReturnANumberAndAString']['aNumber'] is None:
            raise MockFunctionCallError("niFake_ReturnANumberAndAString", param='aNumber')
        a_number.contents.value = self._defaults['ReturnANumberAndAString']['aNumber']
        if self._defaults['ReturnANumberAndAString']['aString'] is None:
            raise MockFunctionCallError("niFake_ReturnANumberAndAString", param='aString')
        a_string.contents.value = self._defaults['ReturnANumberAndAString']['aString']
        return self._defaults['ReturnANumberAndAString']['return']

    def niFake_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niFake_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niFake_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niFake_SetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViSession']['return'] != 0:
            return self._defaults['SetAttributeViSession']['return']
        return self._defaults['SetAttributeViSession']['return']

    def niFake_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niFake_SimpleFunction(self, vi):  # noqa: N802
        if self._defaults['SimpleFunction']['return'] != 0:
            return self._defaults['SimpleFunction']['return']
        return self._defaults['SimpleFunction']['return']

    def niFake_TwoInputFunction(self, vi, a_number, a_string):  # noqa: N802
        if self._defaults['TwoInputFunction']['return'] != 0:
            return self._defaults['TwoInputFunction']['return']
        return self._defaults['TwoInputFunction']['return']

    def niFake_Use64BitNumber(self, vi, input, output):  # noqa: N802
        if self._defaults['Use64BitNumber']['return'] != 0:
            return self._defaults['Use64BitNumber']['return']
        if self._defaults['Use64BitNumber']['output'] is None:
            raise MockFunctionCallError("niFake_Use64BitNumber", param='output')
        output.contents.value = self._defaults['Use64BitNumber']['output']
        return self._defaults['Use64BitNumber']['return']

    def niFake_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niFake_Abort.side_effect = MockFunctionCallError("niFake_Abort")
        mock_library.niFake_Abort.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_EnumInputFunctionWithDefaults.side_effect = MockFunctionCallError("niFake_EnumInputFunctionWithDefaults")
        mock_library.niFake_EnumInputFunctionWithDefaults.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetABoolean.side_effect = MockFunctionCallError("niFake_GetABoolean")
        mock_library.niFake_GetABoolean.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetANumber.side_effect = MockFunctionCallError("niFake_GetANumber")
        mock_library.niFake_GetANumber.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetAStringOfFixedMaximumSize.side_effect = MockFunctionCallError("niFake_GetAStringOfFixedMaximumSize")
        mock_library.niFake_GetAStringOfFixedMaximumSize.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetAStringWithSpecifiedMaximumSize.side_effect = MockFunctionCallError("niFake_GetAStringWithSpecifiedMaximumSize")
        mock_library.niFake_GetAStringWithSpecifiedMaximumSize.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetAttributeViBoolean.side_effect = MockFunctionCallError("niFake_GetAttributeViBoolean")
        mock_library.niFake_GetAttributeViBoolean.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetAttributeViInt32.side_effect = MockFunctionCallError("niFake_GetAttributeViInt32")
        mock_library.niFake_GetAttributeViInt32.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetAttributeViReal64.side_effect = MockFunctionCallError("niFake_GetAttributeViReal64")
        mock_library.niFake_GetAttributeViReal64.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetAttributeViSession.side_effect = MockFunctionCallError("niFake_GetAttributeViSession")
        mock_library.niFake_GetAttributeViSession.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetAttributeViString.side_effect = MockFunctionCallError("niFake_GetAttributeViString")
        mock_library.niFake_GetAttributeViString.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetEnumValue.side_effect = MockFunctionCallError("niFake_GetEnumValue")
        mock_library.niFake_GetEnumValue.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetError.side_effect = MockFunctionCallError("niFake_GetError")
        mock_library.niFake_GetError.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_GetErrorMessage.side_effect = MockFunctionCallError("niFake_GetErrorMessage")
        mock_library.niFake_GetErrorMessage.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_InitWithOptions.side_effect = MockFunctionCallError("niFake_InitWithOptions")
        mock_library.niFake_InitWithOptions.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_Initiate.side_effect = MockFunctionCallError("niFake_Initiate")
        mock_library.niFake_Initiate.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_OneInputFunction.side_effect = MockFunctionCallError("niFake_OneInputFunction")
        mock_library.niFake_OneInputFunction.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_Read.side_effect = MockFunctionCallError("niFake_Read")
        mock_library.niFake_Read.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_ReadFromChannel.side_effect = MockFunctionCallError("niFake_ReadFromChannel")
        mock_library.niFake_ReadFromChannel.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_ReadMultiPoint.side_effect = MockFunctionCallError("niFake_ReadMultiPoint")
        mock_library.niFake_ReadMultiPoint.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_ReturnANumberAndAString.side_effect = MockFunctionCallError("niFake_ReturnANumberAndAString")
        mock_library.niFake_ReturnANumberAndAString.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_SetAttributeViBoolean.side_effect = MockFunctionCallError("niFake_SetAttributeViBoolean")
        mock_library.niFake_SetAttributeViBoolean.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_SetAttributeViInt32.side_effect = MockFunctionCallError("niFake_SetAttributeViInt32")
        mock_library.niFake_SetAttributeViInt32.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_SetAttributeViReal64.side_effect = MockFunctionCallError("niFake_SetAttributeViReal64")
        mock_library.niFake_SetAttributeViReal64.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_SetAttributeViSession.side_effect = MockFunctionCallError("niFake_SetAttributeViSession")
        mock_library.niFake_SetAttributeViSession.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_SetAttributeViString.side_effect = MockFunctionCallError("niFake_SetAttributeViString")
        mock_library.niFake_SetAttributeViString.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_SimpleFunction.side_effect = MockFunctionCallError("niFake_SimpleFunction")
        mock_library.niFake_SimpleFunction.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_TwoInputFunction.side_effect = MockFunctionCallError("niFake_TwoInputFunction")
        mock_library.niFake_TwoInputFunction.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_Use64BitNumber.side_effect = MockFunctionCallError("niFake_Use64BitNumber")
        mock_library.niFake_Use64BitNumber.return_value = nifake.python_types.ViStatus(0)
        mock_library.niFake_close.side_effect = MockFunctionCallError("niFake_close")
        mock_library.niFake_close.return_value = nifake.python_types.ViStatus(0)
