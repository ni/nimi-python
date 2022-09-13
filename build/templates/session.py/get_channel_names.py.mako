<%page args="f, config, method_template"/>\
<%
    '''Some "fancy" methods in _SessionBase need to get channel names, but exposing
    get_channel_names() from _SessionBase as part of public API would allow
    users to call it with "channels" repeated capability which we want to avoid.
    For that reason, some modules code-generate _get_channel_names() as private in
    _SessionBase and then put this public wrapper in Session.
    '''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        return self._${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_PASSTHROUGH_CALL)})
