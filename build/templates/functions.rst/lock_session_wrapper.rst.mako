<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
%>\
.. py:method:: ${function['python_name']}()

    | Obtains a multithread lock on the device session. Before doing so, the
      software waits until all other execution threads release their locks
      on the device session.
    | Other threads may have obtained a lock on this session for the
      following reasons:

    -  The application called the :py:meth:`nidcpower.Session.lock_session` method.
    -  A call to NI-DCPower locked the session.
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
    the :py:meth:`nidcpower.Session.unlock_session` method. 
