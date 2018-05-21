<%page args="f, config, method_template"/>\
<%
    import build.helper as helper

    c_function_prefix = config['c_function_prefix']
%>\
    def ${f['python_name']}(self):
        '''${f['python_name']}

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.${c_function_prefix}UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

