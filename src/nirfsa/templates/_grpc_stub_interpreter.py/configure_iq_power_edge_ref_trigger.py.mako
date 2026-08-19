<%page args="f, config, method_template"/>\
<%
    '''Renders configure_iq_power_edge_ref_trigger for gRPC.
    The proto ConfigureIQPowerEdgeRefTriggerRequest has no "source" field
    (the server always uses channel 0), so source is intentionally omitted.'''
    import build.helper as helper
    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    method_decl_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION)
    grpc_name = f.get('grpc_name', f['name'])
%>\

    def ${full_func_name}(${method_decl_params}):  # noqa: N802
        self._invoke(
            self._client.${grpc_name},
            grpc_types.${grpc_name}Request(vi=self._vi, level=level, slope_raw=slope.value, pretrigger_samples=pretrigger_samples),
        )
