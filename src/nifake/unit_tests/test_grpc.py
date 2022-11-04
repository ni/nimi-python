import array
import collections
import grpc
import math
import nifake
import nifake.errors
import numpy
import pytest
import warnings

from unittest.mock import MagicMock
from unittest.mock import patch

import _mock_helper

GRPC_SESSION_OBJECT_FOR_TEST = object()


Metadatum = collections.namedtuple('Metadatum', ('key', 'value'))


class MyRpcError(grpc.RpcError):
    def __init__(self, error_code, error_message, grpc_error=grpc.StatusCode.UNKNOWN):
        super().__init__()
        self._grpc_error = grpc_error
        self._error_code = error_code
        self._error_message = error_message

    def code(self):
        return self._grpc_error

    def details(self):
        return self._error_message

    def trailing_metadata(self):
        if self._error_code is None:
            return []
        else:
            return [Metadatum('ni-error', str(self._error_code))]


class TestGrpcStubInterpreter(object):

    class PatchedGrpcTypes:
        def __init__(self):
            for f in dir(nifake._grpc_stub_interpreter.grpc_types):
                if f.endswith('Request'):
                    real_func = getattr(nifake._grpc_stub_interpreter.grpc_types, f)
                    error_func = _mock_helper.MockFunctionCallError(f)
                    setattr(self, f, MagicMock(spec_set=real_func, side_effect=error_func))
                else:
                    setattr(self, f, getattr(nifake._grpc_stub_interpreter.grpc_types, f))

    class PatchedGrpcStub(nifake._grpc_stub_interpreter.nifake_grpc.NiFakeServicer):
        def _sample_func(self, request):
            pass

        def __init__(self):
            for f in dir(self):
                if not f.startswith('_'):
                    error_func = _mock_helper.MockFunctionCallError(f)
                    setattr(self, f, MagicMock(spec_set=self._sample_func, side_effect=error_func))

        def __call__(self, grpc_channel):
            self._grpc_channel = grpc_channel
            return self

    def setup_method(self, method):
        self.patched_grpc_types = self.PatchedGrpcTypes()
        self.patched_grpc_stub = self.PatchedGrpcStub()
        self.real_grpc_types = nifake._grpc_stub_interpreter.grpc_types
        self.grpc_types_patch = patch('nifake._grpc_stub_interpreter.grpc_types', self.patched_grpc_types)
        self.grpc_stub_patch = patch('nifake._grpc_stub_interpreter.nifake_grpc.NiFakeStub', side_effect=self.patched_grpc_stub)
        self.grpc_types_patch.start()
        self.grpc_stub_patch.start()

        self.get_ctypes_pointer_for_buffer_side_effect_count = 0
        self.get_ctypes_pointer_for_buffer_side_effect_items = []

    def teardown_method(self, method):
        self.grpc_stub_patch.stop()
        self.grpc_types_patch.stop()

    def _get_initialized_library_interpreter(self, grpc_channel=object()):
        session_options = nifake.GrpcSessionOptions(grpc_channel, "", nifake.SessionInitializationBehavior.AUTO)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(session_options)
        assert interpreter._client is self.patched_grpc_stub
        assert interpreter._vi == 0
        assert self.patched_grpc_stub._grpc_channel is grpc_channel
        interpreter._vi = GRPC_SESSION_OBJECT_FOR_TEST
        return interpreter

    def _check_fields(self, response_class, **kwargs):
        fields = dict(kwargs)
        response_fields = dict((x.name, x) for x in response_class.DESCRIPTOR.fields)

        unexpected_fields = set(fields) - set(response_fields)
        assert not unexpected_fields, 'Unexpected fields: ' + str(list(sorted(unexpected_fields)))

        for f in response_fields:
            if f.endswith('_raw') and f[:-4] in response_fields:
                fields.setdefault(f, fields[f[:-4]])
                fields.setdefault(f[:-4], fields[f])

        missing_fields = set(response_fields) - set(fields)
        assert not missing_fields, 'Missing fields: ' + str(list(sorted(missing_fields)))

        for field, value in fields.items():
            rf = response_fields[field]
            field_type = rf.type
            if field_type == rf.TYPE_ENUM:
                if (field + '_raw') not in fields:
                    assert field.endswith('_mapped')
                    raw_field = field.rpartition('_mapped')[0] + '_raw'
                    assert raw_field in fields
                    assert kwargs.get(raw_field)
                    if rf.label == rf.LABEL_REPEATED:
                        assert len(kwargs[raw_field]) == len(value)
                expected_py_type = int
            elif field_type == rf.TYPE_BOOL:
                expected_py_type = bool
            elif field_type == rf.TYPE_STRING:
                expected_py_type = str
            elif field_type == rf.TYPE_BYTES:
                expected_py_type = bytes
            elif field_type in {rf.TYPE_DOUBLE, rf.TYPE_FLOAT}:
                expected_py_type = float
            elif field_type in {rf.TYPE_INT32, rf.TYPE_INT64, rf.TYPE_FIXED64, rf.TYPE_FIXED32}:
                expected_py_type = int
            elif field_type in {rf.TYPE_UINT32, rf.TYPE_UINT64}:
                expected_py_type = int
            elif field_type in {rf.TYPE_SINT32, rf.TYPE_SINT64, rf.TYPE_SFIXED32, rf.TYPE_SFIXED64}:
                expected_py_type = int
            elif field_type == rf.TYPE_MESSAGE:
                expected_py_type = object
            elif field_type == rf.TYPE_GROUP:
                assert False, 'GROUP types not yet supported here'
            else:
                assert False, f'Unknown type {field_type}'

            if rf.label == rf.LABEL_REPEATED:
                for x in value:
                    assert isinstance(x, expected_py_type)
            else:
                assert isinstance(value, expected_py_type), (field, field_type)

        return fields

    def _set_side_effect(self, function_name, side_effect=None, **kwargs):
        if side_effect is None:
            kwargs.setdefault('status', 0)
            response_class = getattr(self.real_grpc_types, function_name + 'Response')
            kwargs = self._check_fields(response_class, **kwargs)
            side_effect = [response_class(**kwargs)]
        else:
            assert not kwargs, 'Do not use both side_effect and kwargs'

        request_object = object()
        getattr(self.patched_grpc_types, function_name + 'Request').side_effect = [request_object]
        getattr(self.patched_grpc_stub, function_name).side_effect = side_effect
        return request_object

    def _assert_call(self, function_name, request_object):
        getattr(self.patched_grpc_stub, function_name).assert_called_once_with(request_object)
        return getattr(self.patched_grpc_types, function_name + 'Request')

    # Methods

    def test_new_session_already_exists(self):
        library_func = 'InitWithOptions'
        session_name = 'existing_session'
        error_message = "Cannot initialize '" + session_name + "' when a session already exists."
        grpc_error = grpc.StatusCode.ALREADY_EXISTS
        self._set_side_effect(library_func, side_effect=MyRpcError(None, error_message, grpc_error=grpc_error))
        init_behavior = nifake.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
        grpc_options = nifake.GrpcSessionOptions(object(), session_name, init_behavior)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        try:
            interpreter.init_with_options('dev1', False, False, '')
            assert False
        except nifake.Error as e:
            assert e.rpc_code == grpc_error
            assert e.description == error_message
            assert str(e) == f'StatusCode.ALREADY_EXISTS: {error_message}'

    def test_attach_to_non_existent_session(self):
        library_func = 'InitWithOptions'
        session_name = 'non_existent_session'
        error_message = "Cannot attach to '" + session_name + "' because a session has not been initialized."
        grpc_error = grpc.StatusCode.FAILED_PRECONDITION
        self._set_side_effect(library_func, side_effect=MyRpcError(None, error_message, grpc_error=grpc_error))
        init_behavior = nifake.SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION
        grpc_options = nifake.GrpcSessionOptions(object(), session_name, init_behavior)
        interpreter = nifake._grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        try:
            interpreter.init_with_options('dev1', False, False, '')
            assert False
        except nifake.Error as e:
            assert e.rpc_code == grpc_error
            assert e.description == error_message
            assert str(e) == f'StatusCode.FAILED_PRECONDITION: {error_message}'

    @pytest.mark.timeout(2)
    def test_lock_unlock(self):
        # Note: this is purely local; don't set up any grpc mocks
        interpreter = self._get_initialized_library_interpreter()
        interpreter.lock()
        interpreter.lock()  # ensure recurive locking is allowed
        interpreter.unlock()
        interpreter.unlock()

    def test_simple_function(self):
        library_func = 'PoorlyNamedSimpleFunction'
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.simple_function() is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_a_number(self):
        library_func = 'GetANumber'
        test_number = 16
        response_object = self._set_side_effect(library_func, a_number=test_number)
        interpreter = self._get_initialized_library_interpreter()
        test_result = interpreter.get_a_number()
        assert isinstance(test_result, int)
        assert test_result == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_one_input_function(self):
        library_func = 'OneInputFunction'
        test_number = 1
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.one_input_function(test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, a_number=test_number
        )

    def test_vi_int_64_function(self):
        library_func = 'Use64BitNumber'
        input_value = 2 ** 40
        output_value = 2 ** 41
        response_object = self._set_side_effect(library_func, output=output_value)
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.use64_bit_number(input_value) == output_value
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, input=input_value
        )

    def test_two_input_function(self):
        library_func = 'TwoInputFunction'
        test_number = 1.5
        test_string = 'test'
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.two_input_function(test_number, test_string) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, a_number=test_number, a_string=test_string
        )

    def test_get_enum_value(self):
        library_func = 'GetEnumValue'
        test_number = 1
        test_turtle = nifake.Turtle.LEONARDO
        response_object = self._set_side_effect(library_func, a_quantity=test_number, a_turtle=test_turtle.value)
        interpreter = self._get_initialized_library_interpreter()
        test_result_number, test_result_enum = interpreter.get_enum_value()
        assert isinstance(test_result_number, int)
        assert test_result_number == test_number
        assert isinstance(test_result_enum, nifake.Turtle)
        assert test_result_enum == test_turtle
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_a_list_enums(self):
        library_func = 'EnumArrayOutputFunction'
        test_list = [1, 1, 0]
        response_object = self._set_side_effect(library_func, an_array=test_list)
        interpreter = self._get_initialized_library_interpreter()
        test_result = interpreter.enum_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert isinstance(actual_value, nifake.Turtle)
            assert actual_value.value == expected_value
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_elements=len(test_list)
        )

    def test_get_a_boolean(self):
        library_func = 'GetABoolean'
        response_object = self._set_side_effect(library_func, a_boolean=True)
        interpreter = self._get_initialized_library_interpreter()
        test_result = interpreter.get_a_boolean()
        assert test_result is True
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_a_list_booleans(self):
        library_func = 'BoolArrayOutputFunction'
        test_list = [True, True, False]
        response_object = self._set_side_effect(library_func, an_array=test_list)
        interpreter = self._get_initialized_library_interpreter()
        test_result = interpreter.bool_array_output_function(len(test_list))
        assert len(test_list) == len(test_result)
        for expected_value, actual_value in zip(test_list, test_result):
            assert actual_value is expected_value
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_elements=len(test_list)
        )

    def test_single_point_read_nan(self):
        library_func = 'Read'
        test_maximum_time_s = 10.0
        test_reading = float('NaN')
        response_object = self._set_side_effect(library_func, reading=test_reading)
        interpreter = self._get_initialized_library_interpreter()
        assert math.isnan(interpreter.read(test_maximum_time_s))
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, maximum_time=test_maximum_time_s
        )

    def test_fetch_waveform(self):
        library_func = 'FetchWaveform'
        expected_waveform_list = [1.0, 0.1, 42.0, 0.42]
        response_object = self._set_side_effect(library_func, waveform_data=expected_waveform_list, actual_number_of_samples=len(expected_waveform_list))
        interpreter = self._get_initialized_library_interpreter()
        actual_waveform = interpreter.fetch_waveform(len(expected_waveform_list))
        assert isinstance(actual_waveform[0], float)
        assert len(actual_waveform) == len(expected_waveform_list)
        for i in range(len(actual_waveform)):
            assert actual_waveform[i] == expected_waveform_list[i]
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_samples=len(expected_waveform_list)
        )

    def test_fetch_waveform_into(self):
        interpreter = self._get_initialized_library_interpreter()
        waveform = numpy.empty(4, numpy.float64)
        try:
            interpreter.fetch_waveform_into(waveform)
            assert False
        except NotImplementedError:
            pass

    def test_write_waveform(self):
        library_func = 'WriteWaveform'
        expected_waveform = [1.1, 2.2, 3.3, 4.4]
        expected_array = array.array('d', expected_waveform)
        interpreter = self._get_initialized_library_interpreter()
        response_object = self._set_side_effect(library_func)
        assert interpreter.write_waveform(expected_array) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, waveform=expected_array
        )

    def test_write_waveform_numpy(self):
        waveform = numpy.array([1.1, 2.2, 3.3, 4.4], order='C')
        interpreter = self._get_initialized_library_interpreter()
        try:
            interpreter.write_waveform_numpy(waveform)
            assert False
        except NotImplementedError:
            pass

    def test_return_multiple_types(self):
        library_func = 'ReturnMultipleTypes'
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        expected_enum_val = nifake.Turtle.LEONARDO
        enum_val = nifake._grpc_stub_interpreter.grpc_types.Turtle.TURTLE_LEONARDO
        float_val = 1.23
        expected_float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        float_enum_val = nifake._grpc_stub_interpreter.grpc_types.FloatEnum.FLOAT_ENUM_SIX_POINT_FIVE
        raw_float_enum_val = 6.5
        array_val = [0.0, 1.0, 2.0]
        array_size = len(array_val)
        string_val = 'Testing is fun?'
        response_object = self._set_side_effect(
            library_func,
            a_boolean=boolean_val,
            an_int32=int32_val,
            an_int64=int64_val,
            an_int_enum=enum_val,
            a_float=float_val,
            a_float_enum_mapped=float_enum_val,
            a_float_enum_raw=raw_float_enum_val,
            an_array=array_val,
            a_string=string_val,
        )
        interpreter = self._get_initialized_library_interpreter()
        result_boolean, result_int32, result_int64, result_enum, result_float, result_float_enum, result_array, result_string = interpreter.return_multiple_types(array_size)
        assert result_boolean == boolean_val
        assert isinstance(result_boolean, bool)
        assert result_int32 == int32_val
        assert isinstance(result_int32, int)
        assert result_int64 == int64_val
        assert isinstance(result_int64, int)
        assert result_enum == expected_enum_val
        assert isinstance(result_enum, nifake.Turtle)
        assert result_float == float_val
        assert isinstance(result_float, float)
        assert result_float_enum == expected_float_enum_val
        assert isinstance(result_float_enum, nifake.FloatEnum)
        assert result_array == array_val
        # assert `list` duck typing (in reality, it's a google._upb._message.RepeatedScalarContainer
        assert isinstance(result_array, collections.abc.Sequence)
        assert isinstance(result_array[0], float)
        assert result_string == string_val
        assert isinstance(result_string, str)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, array_size=array_size
        )

    def test_multiple_array_types(self):
        library_func = 'MultipleArrayTypes'
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6.0, -7.0, -8.0]
        output_array_size = len(expected_output_array)
        input_array_of_integers = [1, 2]
        input_array_of_floats = [-1.0, -2.0]
        response_object = self._set_side_effect(
            library_func,
            output_array=expected_output_array,
            output_array_of_fixed_length=expected_output_array_of_fixed_length,
        )
        interpreter = self._get_initialized_library_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, input_array_of_integers)
        assert output_array == output_array
        assert expected_output_array_of_fixed_length == output_array_of_fixed_length
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            output_array_size=output_array_size,
            input_array_of_floats=input_array_of_floats,
            input_array_of_integers=input_array_of_integers,
        )

    def test_multiple_array_types_none_input(self):
        library_func = 'MultipleArrayTypes'
        expected_output_array = [0.2, 0.4]
        expected_output_array_of_fixed_length = [-6.0, -7.0, -8.0]
        output_array_size = len(expected_output_array)
        input_array_of_floats = [0.1, 0.2]
        response_object = self._set_side_effect(
            library_func,
            output_array=expected_output_array,
            output_array_of_fixed_length=expected_output_array_of_fixed_length,
        )
        interpreter = self._get_initialized_library_interpreter()
        output_array, output_array_of_fixed_length = interpreter.multiple_array_types(output_array_size, input_array_of_floats, None)
        assert output_array == output_array
        assert expected_output_array_of_fixed_length == output_array_of_fixed_length
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            output_array_size=output_array_size,
            input_array_of_floats=input_array_of_floats,
            input_array_of_integers=None,
        )

    def test_multiple_arrays_same_size(self):
        library_func = 'MultipleArraysSameSize'
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430, 0.440]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        response_object = self._set_side_effect(library_func)
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            values1=input_array_of_floats1,
            values2=input_array_of_floats2,
            values3=input_array_of_floats3,
            values4=input_array_of_floats4,
        )

    def test_multiple_arrays_same_size_none_input(self):
        library_func = 'MultipleArraysSameSize'
        response_object = self._set_side_effect(library_func)
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.multiple_arrays_same_size(input_array_of_floats1, None, None, None) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            values1=input_array_of_floats1,
            values2=None,
            values3=None,
            values4=None,
        )

    def test_multiple_arrays_same_size_wrong_size(self):
        library_func = 'MultipleArraysSameSize'
        # grpc-device server checks this server-side and errors with ::grpc::INVALID_ARGUMENT
        self._set_side_effect(library_func, side_effect=MyRpcError(
            None,
            'The sizes of linked repeated fields [values1, values2, values3, values4] do not match',
            grpc_error=grpc.StatusCode.INVALID_ARGUMENT,
        ))
        input_array_of_floats1 = [0.041, 0.042, 0.043, 0.044]
        input_array_of_floats2 = [0.410, 0.420, 0.430]
        input_array_of_floats3 = [4.100, 4.200, 4.300, 4.400]
        input_array_of_floats4 = [41.00, 42.00, 43.00, 44.00]
        interpreter = self._get_initialized_library_interpreter()
        try:
            assert interpreter.multiple_arrays_same_size(input_array_of_floats1, input_array_of_floats2, input_array_of_floats3, input_array_of_floats4) is None  # no outputs
            assert False
        except ValueError:
            pass

    def test_parameters_are_multiple_types(self):
        library_func = 'ParametersAreMultipleTypes'
        response_object = self._set_side_effect(library_func)
        boolean_val = True
        int32_val = 32
        int64_val = 6000000000
        enum_val = nifake.Turtle.LEONARDO
        float_val = 1.23
        float_enum_val = nifake.FloatEnum.SIX_POINT_FIVE
        string_val = 'Testing is fun?'
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.parameters_are_multiple_types(boolean_val, int32_val, int64_val, enum_val, float_val, float_enum_val, string_val) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            a_boolean=boolean_val,
            an_int32=int32_val,
            an_int64=int64_val,
            an_int_enum_raw=enum_val.value,
            a_float=float_val,
            a_float_enum_raw=float_enum_val.value,
            a_string=string_val,
        )

    def test_method_with_error(self):
        library_func = 'PoorlyNamedSimpleFunction'
        test_error_code = -42
        test_error_desc = 'The answer to the ultimate question'
        self._set_side_effect(library_func, side_effect=MyRpcError(test_error_code, test_error_desc))
        interpreter = self._get_initialized_library_interpreter()
        try:
            assert interpreter.simple_function() is None  # no outputs
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_call_not_enough_parameters_error(self):
        interpreter = self._get_initialized_library_interpreter()
        try:
            assert interpreter.multiple_array_types(10) is None  # no outputs
            assert False
        except TypeError:
            pass

    def test_invalid_method_call_wrong_type_error(self):
        interpreter = self._get_initialized_library_interpreter()
        try:
            assert interpreter.multiple_array_types('potato', [0.0, 0.1, 0.2]) is None  # no outputs
            assert False
        except TypeError:
            pass

    def test_method_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings('always', category=nifake.DriverWarning)

        library_func = 'PoorlyNamedSimpleFunction'
        test_error_code = 42
        test_error_desc = 'The answer to the ultimate question, only positive'
        response_object = self._set_side_effect(library_func, status=test_error_code)
        error_response_object = self._set_side_effect('ErrorMessage', error_message=test_error_desc)
        interpreter = self._get_initialized_library_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert interpreter.simple_function() is None  # no outputs
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)
        self._assert_call('ErrorMessage', error_response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, error_code=test_error_code
        )

    def test_read_with_warning(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings('always', category=nifake.DriverWarning)

        library_func = 'Read'
        test_maximum_time_s = 10.0
        test_reading = float('nan')
        test_error_code = 42
        test_error_desc = 'The answer to the ultimate question, only positive'
        response_object = self._set_side_effect(library_func, status=test_error_code, reading=test_reading)
        error_response_object = self._set_side_effect('ErrorMessage', error_message=test_error_desc)
        interpreter = self._get_initialized_library_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert math.isnan(interpreter.read(test_maximum_time_s))
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert test_error_desc in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, maximum_time=test_maximum_time_s
        )
        self._assert_call('ErrorMessage', error_response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, error_code=test_error_code
        )

    # Retrieving buffers and strings

    def test_get_a_string_of_fixed_maximum_size(self):
        library_func = 'GetAStringOfFixedMaximumSize'
        test_string = 'A string no larger than the max size of 256 allowed by the function.'
        response_object = self._set_side_effect(library_func, a_string=test_string)
        interpreter = self._get_initialized_library_interpreter()
        returned_string = interpreter.get_a_string_of_fixed_maximum_size()
        assert returned_string == test_string
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_return_a_number_and_a_string(self):
        library_func = 'ReturnANumberAndAString'
        test_string = 'this string'
        test_number = 13
        response_object = self._set_side_effect(library_func, a_string=test_string, a_number=test_number)
        interpreter = self._get_initialized_library_interpreter()
        returned_number, returned_string = interpreter.return_a_number_and_a_string()
        assert (returned_string == test_string)
        assert (returned_number == test_number)
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_an_ivi_dance_string(self):
        library_func = 'GetAnIviDanceString'
        string_val = 'Testing is fun?'
        response_object = self._set_side_effect(library_func, a_string=string_val)
        interpreter = self._get_initialized_library_interpreter()
        result_string = interpreter.get_an_ivi_dance_string()
        assert result_string == string_val
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_string_ivi_dance_error(self):
        library_func = 'GetAttributeViString'
        read_write_string_attribute_id = 1000002
        test_error_code = -1234
        test_error_desc = 'ascending order'
        self._set_side_effect(library_func, side_effect=MyRpcError(test_error_code, test_error_desc))
        interpreter = self._get_initialized_library_interpreter()
        try:
            assert interpreter.get_attribute_vi_string('', read_write_string_attribute_id) is None  # no outputs
            assert False
        except nifake.Error as e:
            assert e.code == test_error_code
            assert e.description == test_error_desc

    def test_get_an_ivi_dance_with_a_twist_string(self):
        library_func = 'GetAnIviDanceWithATwistString'
        string_val = 'Testing is fun?'
        response_object = self._set_side_effect(library_func, a_string=string_val, actual_size=len(string_val))
        interpreter = self._get_initialized_library_interpreter()
        result_string = interpreter.get_an_ivi_dance_with_a_twist_string()
        assert result_string == string_val
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_get_array_using_ivi_dance(self):
        library_func = 'GetArrayUsingIviDance'
        response_object = self._set_side_effect(library_func, array_out=[1.1, 2.2])
        interpreter = self._get_initialized_library_interpreter()
        result_array = interpreter.get_array_using_ivi_dance()
        assert result_array == [1.1, 2.2]
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    # Attributes

    def test_get_attribute_int32(self):
        library_func = 'GetAttributeViInt32'
        attribute_id = 1000004
        test_number = 3
        response_object = self._set_side_effect(library_func, attribute_value=test_number)
        interpreter = self._get_initialized_library_interpreter()
        attr_int = interpreter.get_attribute_vi_int32('', attribute_id)
        assert(attr_int == test_number)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_int32(self):
        library_func = 'SetAttributeViInt32'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000004
        test_number = -10
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.set_attribute_vi_int32('', attribute_id, test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw=test_number,
        )

    def test_get_attribute_real64(self):
        library_func = 'GetAttributeViReal64'
        attribute_id = 1000001
        test_number = 1.5
        response_object = self._set_side_effect(library_func, attribute_value=test_number)
        interpreter = self._get_initialized_library_interpreter()
        attr_double = interpreter.get_attribute_vi_real64('', attribute_id)
        assert attr_double == test_number
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_real64(self):
        library_func = 'SetAttributeViReal64'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000001
        test_number = 10.1
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.set_attribute_vi_real64('', attribute_id, test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw=test_number,
        )

    def test_get_attribute_string(self):
        library_func = 'GetAttributeViString'
        attribute_id = 1000002
        string = 'Testing is fun?'
        response_object = self._set_side_effect(library_func, attribute_value=string)
        interpreter = self._get_initialized_library_interpreter()
        attr_string = interpreter.get_attribute_vi_string('', attribute_id)
        assert attr_string == string
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_string(self):
        library_func = 'SetAttributeViString'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000002
        attrib_string = 'This is test string'
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.set_attribute_vi_string('', attribute_id, attrib_string) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw='This is test string',
        )

    def test_get_attribute_boolean(self):
        library_func = 'GetAttributeViBoolean'
        attribute_id = 1000000
        response_object = self._set_side_effect(library_func, attribute_value=True)
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.get_attribute_vi_boolean('', attribute_id)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_boolean(self):
        library_func = 'SetAttributeViBoolean'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000000
        attrib_bool = True
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.set_attribute_vi_boolean('', attribute_id, attrib_bool) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id, attribute_value_raw=True
        )

    def test_get_attribute_int64(self):
        library_func = 'GetAttributeViInt64'
        attribute_id = 1000006
        test_number = 6000000000
        response_object = self._set_side_effect(library_func, attribute_value=test_number)
        interpreter = self._get_initialized_library_interpreter()
        attr_int = interpreter.get_attribute_vi_int64('', attribute_id)
        assert(attr_int == test_number)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, channel_name='', attribute_id=attribute_id
        )

    def test_set_attribute_int64(self):
        library_func = 'SetAttributeViInt64'
        response_object = self._set_side_effect(library_func)
        attribute_id = 1000006
        test_number = -6000000000
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.set_attribute_vi_int64('', attribute_id, test_number) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST,
            channel_name='',
            attribute_id=attribute_id,
            attribute_value_raw=test_number,
        )

    # Error descriptions

    def test_error_message_returns_error(self):
        # We want to capture all of our warnings, not just the first one
        warnings.filterwarnings('always', category=nifake.DriverWarning)

        test_error_code = 42
        library_func = 'PoorlyNamedSimpleFunction'
        response_object = self._set_side_effect(library_func, status=test_error_code)
        error_msg_response_object = self._set_side_effect('ErrorMessage', side_effect=MyRpcError(-3, 'ErrorMessage failed'))
        interpreter = self._get_initialized_library_interpreter()
        with warnings.catch_warnings(record=True) as w:
            assert interpreter.simple_function() is None  # no outputs
            assert len(w) == 1
            assert issubclass(w[0].category, nifake.DriverWarning)
            assert 'Failed to retrieve error description.' in str(w[0].message)
            assert f'Warning {test_error_code} occurred.' in str(w[0].message)
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)
        self._assert_call('ErrorMessage', error_msg_response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST, error_code=test_error_code)

    # Custom types

    def test_set_custom_type(self):
        library_func = 'SetCustomType'
        response_object = self._set_side_effect(library_func)
        cs = nifake.CustomStruct(struct_int=42, struct_double=4.2)
        grpc_cs = nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2)
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.set_custom_type(cs) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, cs=grpc_cs
        )

    def test_get_custom_type(self):
        library_func = 'GetCustomType'
        expected_cs = nifake.CustomStruct(struct_int=42, struct_double=4.2)
        grpc_cs = nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2)
        response_object = self._set_side_effect(library_func, cs=grpc_cs)
        interpreter = self._get_initialized_library_interpreter()
        cs = interpreter.get_custom_type()
        assert cs.struct_int == expected_cs.struct_int
        assert cs.struct_double == expected_cs.struct_double
        assert type(cs) == type(expected_cs)
        self._assert_call(library_func, response_object).assert_called_once_with(vi=GRPC_SESSION_OBJECT_FOR_TEST)

    def test_set_custom_type_array(self):
        library_func = 'SetCustomTypeArray'
        response_object = self._set_side_effect(library_func)
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        grpc_cs = [nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=43, struct_double=4.3), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.3)]
        interpreter = self._get_initialized_library_interpreter()
        assert interpreter.set_custom_type_array(cs) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, cs=grpc_cs
        )

    def test_get_custom_type_array(self):
        library_func = 'GetCustomTypeArray'
        cs = [nifake.CustomStruct(struct_int=42, struct_double=4.2), nifake.CustomStruct(struct_int=43, struct_double=4.3), nifake.CustomStruct(struct_int=42, struct_double=4.3)]
        grpc_cs = [nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.2), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=43, struct_double=4.3), nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=42, struct_double=4.3)]
        response_object = self._set_side_effect(library_func, cs=grpc_cs)
        interpreter = self._get_initialized_library_interpreter()
        cs_test = interpreter.get_custom_type_array(len(cs))
        assert len(cs_test) == len(cs)
        for actual, expected in zip(cs_test, cs):
            assert actual.struct_int == expected.struct_int
            assert actual.struct_double == expected.struct_double
            assert type(actual) == type(expected)
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, number_of_elements=len(cs)
        )

    def test_get_custom_type_typedef(self):
        library_func = 'CustomNestedStructRoundtrip'
        csnt = nifake.CustomStructNestedTypedef(
            struct_custom_struct=nifake.CustomStruct(struct_int=43, struct_double=4.3),
            struct_custom_struct_typedef=nifake.CustomStructTypedef(struct_int=44, struct_double=4.4)
        )
        grpc_csnt = nifake._grpc_stub_interpreter.grpc_types.CustomStructNestedTypedef(
            struct_custom_struct=nifake._grpc_stub_interpreter.grpc_types.FakeCustomStruct(struct_int=43, struct_double=4.3),
            struct_custom_struct_typedef=nifake._grpc_stub_interpreter.grpc_types.CustomStructTypedef(struct_int=44, struct_double=4.4)
        )
        response_object = self._set_side_effect(library_func, nested_custom_type_out=grpc_csnt)
        interpreter = self._get_initialized_library_interpreter()
        csnt_test = interpreter.custom_nested_struct_roundtrip(nested_custom_type_in=csnt)
        assert csnt_test.struct_custom_struct.struct_int == csnt.struct_custom_struct.struct_int
        assert csnt_test.struct_custom_struct.struct_double == csnt.struct_custom_struct.struct_double
        assert csnt_test.struct_custom_struct_typedef.struct_int == csnt.struct_custom_struct_typedef.struct_int
        assert csnt_test.struct_custom_struct_typedef.struct_double == csnt.struct_custom_struct_typedef.struct_double
        assert type(csnt_test.struct_custom_struct) == type(csnt.struct_custom_struct)  # noqa: E721
        assert type(csnt_test.struct_custom_struct_typedef) == type(csnt.struct_custom_struct_typedef)  # noqa: E721
        assert type(csnt_test) == type(csnt)
        request_object = self._assert_call(library_func, response_object)
        request_object.assert_called_once()
        call = request_object.call_args_list[0]
        assert len(call) == 2
        call_args, call_kwargs = call
        assert not call_args
        assert 'nested_custom_type_in' in call_kwargs
        sent_csnt = call_kwargs['nested_custom_type_in']
        assert sent_csnt.struct_custom_struct.struct_int == grpc_csnt.struct_custom_struct.struct_int
        assert sent_csnt.struct_custom_struct.struct_double == grpc_csnt.struct_custom_struct.struct_double
        assert sent_csnt.struct_custom_struct_typedef.struct_int == grpc_csnt.struct_custom_struct_typedef.struct_int
        assert sent_csnt.struct_custom_struct_typedef.struct_double == grpc_csnt.struct_custom_struct_typedef.struct_double
        assert type(sent_csnt.struct_custom_struct) == type(grpc_csnt.struct_custom_struct)  # noqa: E721
        assert type(sent_csnt.struct_custom_struct_typedef) == type(grpc_csnt.struct_custom_struct_typedef)  # noqa: E721
        assert type(sent_csnt) == type(grpc_csnt)

    def test_get_cal_date_time(self):
        library_func = 'GetCalDateAndTime'
        month = 12
        day = 30
        year = 1988
        hour = 10
        minute = 15
        response_object = self._set_side_effect(
            library_func, month=month, day=day, year=year, hour=hour, minute=minute
        )
        interpreter = self._get_initialized_library_interpreter()
        last_cal = interpreter.get_cal_date_and_time(0)
        assert (month, day, year, hour, minute) == last_cal
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, cal_type=0
        )

    # Import/Export functions

    def test_import_attribute_configuration_buffer(self):
        library_func = 'ImportAttributeConfigurationBuffer'
        configuration = b'abcd'
        interpreter = self._get_initialized_library_interpreter()
        response_object = self._set_side_effect(library_func)
        assert interpreter.import_attribute_configuration_buffer(configuration) is None  # no outputs
        self._assert_call(library_func, response_object).assert_called_once_with(
            vi=GRPC_SESSION_OBJECT_FOR_TEST, configuration=configuration
        )

    def test_missing_function(self):
        library_func = 'Abort'
        self._set_side_effect(library_func, side_effect=MyRpcError(None, 'not found', grpc_error=grpc.StatusCode.NOT_FOUND))
        interpreter = self._get_initialized_library_interpreter()
        try:
            interpreter.abort()
            assert False
        except nifake.errors.DriverTooOldError as e:
            message = e.args[0]
            assert message == 'A function was not found in the NI-FAKE runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.'
