<%page args="f, config, method_template"/>\
<%
    '''Renders ReadIQSingleRecordComplexF64 for gRPC.
    Uses INTERPRETER_NUMPY_INTO_METHOD_DECLARATION to match the library interpreter signature
    (channel_list, iq_data_array, timeout) — no separate number_of_samples parameter.
    The server allocates the buffer; we send data_array_size and fill iq_data_array in-place.
    WaveformInfo is constructed with keyword args to avoid reserved fields absent in the proto.'''
    import build.helper as helper

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
        import numpy
        response = self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(vi=self._vi, channel_list=channel_list, timeout=timeout, data_array_size=len(iq_data_array)),
        )
        iq_data_array[:] = numpy.array([complex(x.real, x.imaginary) for x in response.data], dtype=numpy.complex128)
        r = response.wfm_info
        return waveform_info.WaveformInfo(absolute_initial_x=r.absolute_initial_x, relative_initial_x=r.relative_initial_x, x_increment=r.x_increment, actual_samples=r.actual_samples, offset=r.offset, gain=r.gain)
