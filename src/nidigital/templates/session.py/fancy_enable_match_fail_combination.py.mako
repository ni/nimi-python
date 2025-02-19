<%page args="f, config, method_template"/>\
<%
    import build.helper as helper
%>\
    def ${f['python_name']}(self, sync_session):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        self._interpreter.enable_match_fail_combination([self._interpreter.get_session_handle()], sync_session.session_handle)
