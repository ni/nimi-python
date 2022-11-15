# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nifake_pb2 as grpc_types
from . import nifake_pb2_grpc as nifake_grpc
from . import session_pb2 as session_grpc_types

from . import custom_struct as custom_struct  # noqa: F401

from . import custom_struct_nested_typedef as custom_struct_nested_typedef  # noqa: F401

from . import custom_struct_typedef as custom_struct_typedef  # noqa: F401


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nifake_grpc.NiFakeStub(grpc_options.grpc_channel)
        self.set_session_handle()

    def set_session_handle(self, value=session_grpc_types.Session()):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def _invoke(self, func, request):
        try:
            response = func(request)
            error_code = response.status
            error_message = ''
        except grpc.RpcError as rpc_error:
            error_code = None
            error_message = rpc_error.details()
            for entry in rpc_error.trailing_metadata() or []:
                if entry.key == 'ni-error':
                    value = entry.value if isinstance(entry.value, str) else entry.value.decode('utf-8')
                    try:
                        error_code = int(value)
                    except ValueError:
                        error_message += f'\nError status: {value}'

            grpc_error = rpc_error.code()
            if grpc_error == grpc.StatusCode.NOT_FOUND:
                raise errors.DriverTooOldError() from None
            elif grpc_error == grpc.StatusCode.INVALID_ARGUMENT:
                raise ValueError(error_message) from None
            elif grpc_error == grpc.StatusCode.UNAVAILABLE:
                error_message = 'Failed to connect to server'
            elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
                )

            if error_code is None:
                raise errors.RpcError(grpc_error, error_message) from None

        if error_code < 0:
            raise errors.DriverError(error_code, error_message)
        elif error_code > 0:
            if not error_message:
                try:
                    error_message = self.error_message(error_code)
                except errors.Error:
                    error_message = 'Failed to retrieve error description.'
            warnings.warn(errors.DriverWarning(error_code, error_message))
        return response

    def abort(self):  # noqa: N802
        self._invoke(
            self._client.Abort,
            grpc_types.AbortRequest(vi=self._vi),
        )

    def accept_list_of_durations_in_seconds(self, delays):  # noqa: N802
        self._invoke(
            self._client.AcceptListOfDurationsInSeconds,
            grpc_types.AcceptListOfDurationsInSecondsRequest(vi=self._vi, delays=delays),
        )

    def bool_array_output_function(self, number_of_elements):  # noqa: N802
        response = self._invoke(
            self._client.BoolArrayOutputFunction,
            grpc_types.BoolArrayOutputFunctionRequest(vi=self._vi, number_of_elements=number_of_elements),
        )
        return response.an_array

    def configure_abc(self):  # noqa: N802
        self._invoke(
            self._client.ConfigureAbc,
            grpc_types.ConfigureAbcRequest(vi=self._vi),
        )

    def custom_nested_struct_roundtrip(self, nested_custom_type_in):  # noqa: N802
        response = self._invoke(
            self._client.CustomNestedStructRoundtrip,
            grpc_types.CustomNestedStructRoundtripRequest(nested_custom_type_in=nested_custom_type_in._create_copy(grpc_types.CustomStructNestedTypedef)),
        )
        return custom_struct_nested_typedef.CustomStructNestedTypedef(response.nested_custom_type_out)

    def double_all_the_nums(self, numbers):  # noqa: N802
        self._invoke(
            self._client.DoubleAllTheNums,
            grpc_types.DoubleAllTheNumsRequest(vi=self._vi, numbers=numbers),
        )

    def enum_array_output_function(self, number_of_elements):  # noqa: N802
        response = self._invoke(
            self._client.EnumArrayOutputFunction,
            grpc_types.EnumArrayOutputFunctionRequest(vi=self._vi, number_of_elements=number_of_elements),
        )
        return [enums.Turtle(x) for x in response.an_array]

    def enum_input_function_with_defaults(self, a_turtle):  # noqa: N802
        self._invoke(
            self._client.EnumInputFunctionWithDefaults,
            grpc_types.EnumInputFunctionWithDefaultsRequest(vi=self._vi, a_turtle_raw=a_turtle.value),
        )

    def export_attribute_configuration_buffer(self):  # noqa: N802
        response = self._invoke(
            self._client.ExportAttributeConfigurationBuffer,
            grpc_types.ExportAttributeConfigurationBufferRequest(vi=self._vi),
        )
        return response.configuration

    def fetch_waveform(self, number_of_samples):  # noqa: N802
        response = self._invoke(
            self._client.FetchWaveform,
            grpc_types.FetchWaveformRequest(vi=self._vi, number_of_samples=number_of_samples),
        )
        return response.waveform_data

    def fetch_waveform_into(self, number_of_samples):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def function_with_repeated_capability_type(self, site_list):  # noqa: N802
        raise NotImplementedError('function_with_repeated_capability_type is not supported over gRPC')

    def get_a_boolean(self):  # noqa: N802
        response = self._invoke(
            self._client.GetABoolean,
            grpc_types.GetABooleanRequest(vi=self._vi),
        )
        return response.a_boolean

    def get_a_number(self):  # noqa: N802
        response = self._invoke(
            self._client.GetANumber,
            grpc_types.GetANumberRequest(vi=self._vi),
        )
        return response.a_number

    def get_a_string_of_fixed_maximum_size(self):  # noqa: N802
        response = self._invoke(
            self._client.GetAStringOfFixedMaximumSize,
            grpc_types.GetAStringOfFixedMaximumSizeRequest(vi=self._vi),
        )
        return response.a_string

    def get_a_string_using_python_code(self, a_number):  # noqa: N802
        raise NotImplementedError('get_a_string_using_python_code is not supported over gRPC')

    def get_an_ivi_dance_string(self):  # noqa: N802
        response = self._invoke(
            self._client.GetAnIviDanceString,
            grpc_types.GetAnIviDanceStringRequest(vi=self._vi),
        )
        return response.a_string

    def get_an_ivi_dance_with_a_twist_string(self):  # noqa: N802
        response = self._invoke(
            self._client.GetAnIviDanceWithATwistString,
            grpc_types.GetAnIviDanceWithATwistStringRequest(vi=self._vi),
        )
        return response.a_string

    def get_array_for_python_code_custom_type(self):  # noqa: N802
        raise NotImplementedError('get_array_for_python_code_custom_type is not supported over gRPC')

    def get_array_for_python_code_double(self):  # noqa: N802
        raise NotImplementedError('get_array_for_python_code_double is not supported over gRPC')

    def get_array_size_for_python_code(self):  # noqa: N802
        raise NotImplementedError('get_array_size_for_python_code is not supported over gRPC')

    def get_array_using_ivi_dance(self):  # noqa: N802
        response = self._invoke(
            self._client.GetArrayUsingIviDance,
            grpc_types.GetArrayUsingIviDanceRequest(vi=self._vi),
        )
        return response.array_out

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_cal_date_and_time(self, cal_type):  # noqa: N802
        response = self._invoke(
            self._client.GetCalDateAndTime,
            grpc_types.GetCalDateAndTimeRequest(vi=self._vi, cal_type=cal_type),
        )
        return response.month, response.day, response.year, response.hour, response.minute

    def get_cal_interval(self):  # noqa: N802
        response = self._invoke(
            self._client.GetCalInterval,
            grpc_types.GetCalIntervalRequest(vi=self._vi),
        )
        return response.months

    def get_channel_names(self, indices):  # noqa: N802
        raise NotImplementedError('get_channel_names is not supported over gRPC')

    def get_custom_type(self):  # noqa: N802
        response = self._invoke(
            self._client.GetCustomType,
            grpc_types.GetCustomTypeRequest(vi=self._vi),
        )
        return custom_struct.CustomStruct(response.cs)

    def get_custom_type_array(self, number_of_elements):  # noqa: N802
        response = self._invoke(
            self._client.GetCustomTypeArray,
            grpc_types.GetCustomTypeArrayRequest(vi=self._vi, number_of_elements=number_of_elements),
        )
        return [custom_struct.CustomStruct(x) for x in response.cs]

    def get_custom_type_typedef(self):  # noqa: N802
        raise NotImplementedError('get_custom_type_typedef is not supported over gRPC')

    def get_enum_value(self):  # noqa: N802
        response = self._invoke(
            self._client.GetEnumValue,
            grpc_types.GetEnumValueRequest(vi=self._vi),
        )
        return response.a_quantity, enums.Turtle(response.a_turtle)

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.description

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        self._invoke(
            self._client.ImportAttributeConfigurationBuffer,
            grpc_types.ImportAttributeConfigurationBufferRequest(vi=self._vi, configuration=configuration),
        )

    def init_with_options(self, resource_name, id_query, reset_device, option_string):  # noqa: N802
        response = self._invoke(
            self._client.InitWithOptions,
            grpc_types.InitWithOptionsRequest(resource_name=resource_name, id_query=id_query, reset_device=reset_device, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initiate(self):  # noqa: N802
        raise NotImplementedError('initiate is not supported over gRPC')

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def method_using_whole_and_fractional_numbers(self):  # noqa: N802
        response = self._invoke(
            self._client.MethodUsingWholeAndFractionalNumbers,
            grpc_types.MethodUsingWholeAndFractionalNumbersRequest(),
        )
        return response.whole_number, response.fractional_number

    def method_with_grpc_only_param(self, simple_param):  # noqa: N802
        self._invoke(
            self._client.MethodWithGrpcOnlyParam,
            grpc_types.MethodWithGrpcOnlyParamRequest(simple_param=simple_param),
        )

    def method_with_proto_only_parameter(self, attribute_value):  # noqa: N802
        self._invoke(
            self._client.MethodWithProtoOnlyParameter,
            grpc_types.MethodWithProtoOnlyParameterRequest(attribute_value=attribute_value),
        )

    def multiple_array_types(self, output_array_size, input_array_of_floats, input_array_of_integers):  # noqa: N802
        response = self._invoke(
            self._client.MultipleArrayTypes,
            grpc_types.MultipleArrayTypesRequest(vi=self._vi, output_array_size=output_array_size, input_array_of_floats=input_array_of_floats, input_array_of_integers=input_array_of_integers),
        )
        return response.output_array, response.output_array_of_fixed_length

    def multiple_arrays_same_size(self, values1, values2, values3, values4):  # noqa: N802
        self._invoke(
            self._client.MultipleArraysSameSize,
            grpc_types.MultipleArraysSameSizeRequest(vi=self._vi, values1=values1, values2=values2, values3=values3, values4=values4),
        )

    def one_input_function(self, a_number):  # noqa: N802
        self._invoke(
            self._client.OneInputFunction,
            grpc_types.OneInputFunctionRequest(vi=self._vi, a_number=a_number),
        )

    def parameters_are_multiple_types(self, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string):  # noqa: N802
        self._invoke(
            self._client.ParametersAreMultipleTypes,
            grpc_types.ParametersAreMultipleTypesRequest(vi=self._vi, a_boolean=a_boolean, an_int32=an_int32, an_int64=an_int64, an_int_enum_raw=an_int_enum.value, a_float=a_float, a_float_enum_raw=a_float_enum.value, a_string=a_string),
        )

    def simple_function(self):  # noqa: N802
        self._invoke(
            self._client.PoorlyNamedSimpleFunction,
            grpc_types.PoorlyNamedSimpleFunctionRequest(vi=self._vi),
        )

    def read(self, maximum_time):  # noqa: N802
        response = self._invoke(
            self._client.Read,
            grpc_types.ReadRequest(vi=self._vi, maximum_time=maximum_time),
        )
        return response.reading

    def read_from_channel(self, channel_name, maximum_time):  # noqa: N802
        response = self._invoke(
            self._client.ReadFromChannel,
            grpc_types.ReadFromChannelRequest(vi=self._vi, channel_name=channel_name, maximum_time=maximum_time),
        )
        return response.reading

    def return_a_number_and_a_string(self):  # noqa: N802
        response = self._invoke(
            self._client.ReturnANumberAndAString,
            grpc_types.ReturnANumberAndAStringRequest(vi=self._vi),
        )
        return response.a_number, response.a_string

    def return_duration_in_seconds(self):  # noqa: N802
        response = self._invoke(
            self._client.ReturnDurationInSeconds,
            grpc_types.ReturnDurationInSecondsRequest(vi=self._vi),
        )
        return response.timedelta

    def return_list_of_durations_in_seconds(self, number_of_elements):  # noqa: N802
        response = self._invoke(
            self._client.ReturnListOfDurationsInSeconds,
            grpc_types.ReturnListOfDurationsInSecondsRequest(vi=self._vi, number_of_elements=number_of_elements),
        )
        return response.timedeltas

    def return_multiple_types(self, array_size):  # noqa: N802
        response = self._invoke(
            self._client.ReturnMultipleTypes,
            grpc_types.ReturnMultipleTypesRequest(vi=self._vi, array_size=array_size),
        )
        return response.a_boolean, response.an_int32, response.an_int64, enums.Turtle(response.an_int_enum), response.a_float, enums.FloatEnum(response.a_float_enum), response.an_array, response.a_string

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value=attribute_value),
        )

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value=attribute_value),
        )

    def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value=attribute_value),
        )

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_custom_type(self, cs):  # noqa: N802
        self._invoke(
            self._client.SetCustomType,
            grpc_types.SetCustomTypeRequest(vi=self._vi, cs=cs._create_copy(grpc_types.FakeCustomStruct)),
        )

    def set_custom_type_array(self, cs):  # noqa: N802
        self._invoke(
            self._client.SetCustomTypeArray,
            grpc_types.SetCustomTypeArrayRequest(vi=self._vi, cs=cs and [x._create_copy(grpc_types.FakeCustomStruct) for x in cs]),
        )

    def string_valued_enum_input_function_with_defaults(self, a_mobile_os_name):  # noqa: N802
        self._invoke(
            self._client.StringValuedEnumInputFunctionWithDefaults,
            grpc_types.StringValuedEnumInputFunctionWithDefaultsRequest(vi=self._vi, a_mobile_os_name_raw=a_mobile_os_name.value),
        )

    def two_input_function(self, a_number, a_string):  # noqa: N802
        self._invoke(
            self._client.TwoInputFunction,
            grpc_types.TwoInputFunctionRequest(vi=self._vi, a_number=a_number, a_string=a_string),
        )

    def unlock(self):  # noqa: N802
        self._lock.release()

    def use64_bit_number(self, input):  # noqa: N802
        response = self._invoke(
            self._client.Use64BitNumber,
            grpc_types.Use64BitNumberRequest(vi=self._vi, input=input),
        )
        return response.output

    def write_waveform(self, waveform):  # noqa: N802
        self._invoke(
            self._client.WriteWaveform,
            grpc_types.WriteWaveformRequest(vi=self._vi, waveform=waveform),
        )

    def write_waveform_numpy(self, waveform):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def error_message(self, error_code):  # noqa: N802
        response = self._invoke(
            self._client.ErrorMessage,
            grpc_types.ErrorMessageRequest(vi=self._vi, error_code=error_code),
        )
        return response.error_message

    def self_test(self):  # noqa: N802
        raise NotImplementedError('self_test is not supported over gRPC')
