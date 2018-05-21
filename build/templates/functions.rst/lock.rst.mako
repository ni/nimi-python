<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
%>\
.. py:method:: ${function['python_name']}()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`${config['module_name']}.Session.lock` method.
        -  A call to ${config['driver_name']} locked the session.
        -  After a call to the :py:meth:`${config['module_name']}.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`${config['module_name']}.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`${config['module_name']}.Session.lock` method and the
           :py:meth:`${config['module_name']}.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`${config['module_name']}.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`${config['module_name']}.Session.lock` method with a call to
    the :py:meth:`${config['module_name']}.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with ${config['module_name']}.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`${config['module_name']}.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited

