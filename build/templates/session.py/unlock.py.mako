<%page args="f, config, method_template"/>\
<%
    import build.helper as helper
    func_params = helper.get_params_snippet(f, helper.ParameterUsageOptions.LIBRARY_INTERPRETER_METHOD_CALL, config)
%>\
    def ${f['python_name']}(self):
        '''${f['python_name']}

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._library_interpreter.unlock(${func_params})
