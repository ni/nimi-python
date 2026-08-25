<%page args="f, config, method_template"/>\
<%
    '''Renders ReadPowerSpectrumF32/F64 for gRPC.
    The proto request has no power_spectrum_data_array field — only data_array_size.
    The server returns the data as a repeated field; we fill the pre-allocated array in-place.
    SpectrumInfo is constructed with keyword args to avoid reserved fields absent in the proto.'''
    import build.helper as helper

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
        response = self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(vi=self._vi, channel_list=channel_list, timeout=timeout, data_array_size=len(power_spectrum_data_array)),
        )
        power_spectrum_data_array[:] = response.power_spectrum_data
        s = response.spectrum_info
        return spectrum_info_type.SpectrumInfo(initial_frequency=s.initial_frequency, frequency_increment=s.frequency_increment, number_of_spectral_lines=s.number_of_spectral_lines)
