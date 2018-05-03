<%page args="f, config, method_template"/>\
<%
    import build.helper as helper

    c_function_prefix = config['c_function_prefix']
%>\
    def lock_session(self, caller_has_lock=None):
        '''lock_session

        | Obtains a multithread lock on the device session. Before doing so, the
          software waits until all other execution threads release their locks
          on the device session.
        | Other threads may have obtained a lock on this session for the
          following reasons:

        -  The application called the lock_session method.
        -  A call to NI-DCPower locked the session.
        -  A call to the IVI engine locked the session.
        -  After a call to the lock_session method returns
           successfully, no other threads can access the device session until
           you call the unlock_session method.
        -  Use the lock_session method and the
           unlock_session method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

        You can safely make nested calls to the lock_session method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock_session method with a call to
        the unlock_session method. If, however, you use
        **Caller_Has_Lock** in all calls to the lock_session and
        unlock_session method within a method, the IVI Library
        locks the session only once within the method regardless of the number
        of calls you make to the lock_session method. This behavior
        allows you to call the unlock_session method just once at
        the end of the method.

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
        caller_has_lock_ctype = _visatype.ViBoolean(caller_has_lock) if caller_has_lock is not None else None
        error_code = self._library.${c_function_prefix}LockSession(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return bool(caller_has_lock_ctype.value) if caller_has_lock else True

