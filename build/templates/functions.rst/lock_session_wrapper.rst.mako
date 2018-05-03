.. py:method:: lock_session(caller_has_lock=None)

    | Obtains a multithread lock on the device session. Before doing so, the
      software waits until all other execution threads release their locks
      on the device session.
    | Other threads may have obtained a lock on this session for the
      following reasons:

    -  The application called the :py:meth:`nidcpower.Session.lock_session` method.
    -  A call to NI-DCPower locked the session.
    -  A call to the IVI engine locked the session.
    -  After a call to the :py:meth:`nidcpower.Session.lock_session` method returns
       successfully, no other threads can access the device session until
       you call the :py:meth:`nidcpower.Session.unlock_session` method.
    -  Use the :py:meth:`nidcpower.Session.lock_session` method and the
       :py:meth:`nidcpower.Session.unlock_session` method around a sequence of calls to
       instrument driver methods if you require that the device retain its
       settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nidcpower.Session.lock_session` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nidcpower.Session.lock_session` method with a call to
    the :py:meth:`nidcpower.Session.unlock_session` method. If, however, you use
    **Caller_Has_Lock** in all calls to the :py:meth:`nidcpower.Session.lock_session` and
    :py:meth:`nidcpower.Session.unlock_session` method within a method, the IVI Library
    locks the session only once within the method regardless of the number
    of calls you make to the :py:meth:`nidcpower.Session.lock_session` method. This behavior
    allows you to call the :py:meth:`nidcpower.Session.unlock_session` method just once at
    the end of the method.





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



