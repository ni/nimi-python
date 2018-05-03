<%page args="f, config, method_template"/>\
<%
    import build.helper as helper

    c_function_prefix = config['c_function_prefix']
%>\
    def unlock_session(self, caller_has_lock=None):
        '''unlock_session

        Releases a lock that you acquired on an device session using
        lock_session. Refer to lock_session for additional
        information on session locks.

        Args:
            caller_has_lock (bool): This parameter is optional. Default is None. If you do not want to use this parameter, pass None.

                Use this parameter in complex methods to keep track of whether you
                obtain a lock and therefore need to unlock the session. Pass False to the initial
                lock_session call and store the return value into a variable. Pass in the variable as well
                as putting the return value into the same variable for each call to lock_session or
                unlock_session.


        Returns:
            (bool): Use this parameter in complex methods to keep track of whether you
                obtain a lock and therefore need to unlock the session. Pass False to the initial
                lock_session call and store the return value into a variable. Pass in the variable as well
                as putting the return value into the same variable for each call to lock_session or
                unlock_session.

        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean(caller_has_lock) if caller_has_lock else None
        error_code = self._library.${c_function_prefix}UnlockSession(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return bool(caller_has_lock_ctype.value) if caller_has_lock else False

