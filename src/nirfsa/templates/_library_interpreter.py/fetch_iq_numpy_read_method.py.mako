<%page args="f, config, method_template"/>\
<%
    '''Renders a NIRFSA-specific LibraryInterpreter method for reading into a numpy.array.

    This variant intentionally skips generating intermediate size assignments for passed-in
    size parameters to avoid unused-variable lint errors in fetch_iq_single_record helpers.
    '''

    import build.helper as helper

    parameters = f['parameters']
    param_names_method = helper.get_params_snippet(f, helper.ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_DECLARATION)
    param_names_library = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL)

    full_func_name = f['interpreter_name'] + method_template['method_python_name_suffix']
    c_func_name = config['c_function_prefix'] + f['name']

    multi_record_func_names = ('fetch_iq_multi_record_complex_f32', 'fetch_iq_multi_record_complex_f64', 'fetch_iq_multi_record_complex_i16')
    is_multi_record = full_func_name in multi_record_func_names

    # For the multi-record fetches, the driver writes one wfmInfo struct per record. The default
    # code generation allocates a single struct, which the driver overruns (heap corruption) whenever
    # number_of_records > 1. Below we allocate an array of number_of_records structs and pass it
    # directly (ctypes accepts an array instance where a POINTER(struct) argument is expected).
    multi_record_library_call = param_names_library.replace(
        'None if wfm_info_ctype is None else (ctypes.pointer(wfm_info_ctype))',
        'wfm_info_ctype',
    )
%>\

    def ${full_func_name}(${param_names_method}):  # noqa: N802
    % if is_multi_record:
        samples_per_record = 0 if iq_data_arrays is None else (iq_data_arrays.shape[1] if hasattr(iq_data_arrays, 'shape') and len(iq_data_arrays.shape) > 1 else len(iq_data_arrays))
    % endif
% for p in helper.filter_parameters(parameters, helper.ParameterUsageOptions.LIBRARY_METHOD_CALL):
    %   if full_func_name in ('fetch_iq_multi_record_complex_f32', 'fetch_iq_multi_record_complex_f64') and p['python_name'] == 'number_of_samples':
        number_of_samples_ctype = _visatype.ViInt64(samples_per_record)  # case S160
    %   elif full_func_name == 'fetch_iq_multi_record_complex_i16' and p['python_name'] == 'number_of_samples':
        number_of_samples_ctype = _visatype.ViInt64(samples_per_record // 2)  # case S160
    %   elif is_multi_record and p['python_name'] == 'wfm_info':
        wfm_info_ctype = (waveform_info.struct_niRFSA_wfmInfo * number_of_records)()  # case S220
    %   else:
    %     for declaration in helper.get_ctype_variable_declaration_snippet(p, parameters, None, config, use_numpy_array=p['numpy']):
        ${declaration}
    %     endfor
    %   endif
% endfor
    % if is_multi_record:
        error_code = self._library.${c_func_name}(${multi_record_library_call})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(number_of_records)]
    % else:
        error_code = self._library.${c_func_name}(${param_names_library})
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=${f['is_error_handling']})
        ${helper.get_library_interpreter_method_return_snippet(parameters, config, use_numpy_array=True)}
    % endif
