<%page args="f, config, method_template"/>\
<%
    import build.helper as helper

    c_function_prefix = config['c_function_prefix']
%>\
    def ${f['python_name']}(self):
        '''lock_session

        | Obtains a multithread lock on the device session. Before doing so, the
          software waits until all other execution threads release their locks
          on the device session.
        | Other threads may have obtained a lock on this session for the
          following reasons:

        -  The application called the lock_session method.
        -  A call to ${config['driver_name']} locked the session.
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
        the unlock_session method.
        '''
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.${c_function_prefix}LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return

