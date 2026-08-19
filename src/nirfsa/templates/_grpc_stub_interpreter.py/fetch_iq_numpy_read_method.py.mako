<%page args="f, config, method_template"/>\
<%
    '''Renders a GrpcStubInterpreter method for fetch IQ numpy methods, implementing actual gRPC calls.'''

    import build.helper as helper

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])

    is_multi_record = 'multi_record' in full_func_name
    is_i16 = full_func_name.endswith('_i16')
    is_f32 = full_func_name.endswith('_f32')
    numpy_dtype = 'numpy.complex64' if is_f32 else 'numpy.complex128'
    samples_divisor = ' // 2' if is_i16 else ''
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
% if not is_i16:
        import numpy
% endif
% if is_multi_record:
        samples_per_record = (iq_data_arrays.shape[1]${samples_divisor}) if iq_data_arrays is not None and iq_data_arrays.ndim > 1 else 0
        response = self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(vi=self._vi, channel_list=channel_list, starting_record=starting_record, number_of_records=number_of_records, number_of_samples=samples_per_record, timeout=timeout),
        )
%   if is_i16:
        for rec in range(number_of_records):
            for i, x in enumerate(response.data[rec * samples_per_record:(rec + 1) * samples_per_record]):
                iq_data_arrays[rec, 2 * i] = x.real
                iq_data_arrays[rec, 2 * i + 1] = x.imaginary
%   else:
        data_flat = numpy.array([complex(x.real, x.imaginary) for x in response.data], dtype=${numpy_dtype})
        for rec in range(number_of_records):
            iq_data_arrays[rec] = data_flat[rec * samples_per_record:(rec + 1) * samples_per_record]
%   endif
        return [waveform_info.WaveformInfo(absolute_initial_x=r.absolute_initial_x, relative_initial_x=r.relative_initial_x, x_increment=r.x_increment, actual_samples=r.actual_samples, offset=r.offset, gain=r.gain) for r in response.wfm_info]
% else:
        response = self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(vi=self._vi, channel_list=channel_list, record_number=record_number, number_of_samples=len(iq_data_array)${samples_divisor}, timeout=timeout),
        )
%   if is_i16:
        for i, x in enumerate(response.data):
            iq_data_array[2 * i] = x.real
            iq_data_array[2 * i + 1] = x.imaginary
%   else:
        iq_data_array[:] = numpy.array([complex(x.real, x.imaginary) for x in response.data], dtype=${numpy_dtype})
%   endif
        r = response.wfm_info
        return waveform_info.WaveformInfo(absolute_initial_x=r.absolute_initial_x, relative_initial_x=r.relative_initial_x, x_increment=r.x_increment, actual_samples=r.actual_samples, offset=r.offset, gain=r.gain)
% endif
