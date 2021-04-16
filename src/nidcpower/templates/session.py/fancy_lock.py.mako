<%page args="f, config, method_template"/>\
<%
    '''
    Unsynchronized operation does not yet support session lock and unlock. To avoid errors from the unimplemented
    functions, we will temporarily use a native python lock until session locking is supported by the driver.
    This fancy function needs to be removed in a later release of NI-DCPower.
    '''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    import threading
    _pylock = threading.Lock()  # shared python thread lock that will be used in place of session lock

    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''

        self._pylock.acquire()

