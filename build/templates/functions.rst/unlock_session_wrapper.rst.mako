.. py:method:: unlock_session(caller_has_lock=None)

    Releases a lock that you acquired on an device session using
    :py:meth:`nidcpower.Session.lock_session`. Refer to :py:meth:`nidcpower.Session.lock_session` for additional
    information on session locks.





    :param caller_has_lock:


        This parameter is optional. If you do not want to use this parameter, pass None.

        Use this parameter in complex methods to keep track of whether you
        obtain a lock and therefore need to unlock the session. Pass False to the initial
        lock_session call and store the return value into a variable. Pass in the variable as well
        as putting the return value into the same variable for each call to lock_session or
        unlock_session.




    :type caller_has_lock: bool

    :rtype: bool
    :return:


            This parameter is optional. If you do not want to use this parameter, pass None.

            Use this parameter in complex methods to keep track of whether you
            obtain a lock and therefore need to unlock the session. Pass False to the initial
            lock_session call and store the return value into a variable. Pass in the variable as well
            as putting the return value into the same variable for each call to lock_session or
            unlock_session.


