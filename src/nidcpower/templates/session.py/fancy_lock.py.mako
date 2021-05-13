<%page args="f, config, method_template"/>\
<%
    '''Overrides the default lock template to use a threading.RLock instead of the driver lock.

    See GitHub issue [1596](https://github.com/ni/nimi-python/issues/1596) for more information.
    '''
    import build.helper as helper

    c_function_prefix = config['c_function_prefix']
%>\
    # TODO(smooresni): Replace with session lock per GitHub issue [1596](https://github.com/ni/nimi-python/issues/1596)
    def ${f['python_name']}(self):
        '''${f['python_name']}

        Obtains a multi-threaded lock on the instrument driver. Before doing so, the
        software waits until all other execution threads release their locks
        on the driver.

        Other threads may have obtained a lock on this driver for the
        following reasons:

            -  The application called the lock method.
            -  A call to ${config['driver_name']} locked the driver.
            -  After a call to the lock method returns
               successfully, no other threads can access the driver until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the driver, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, ${config['module_name']}.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._lock_session()  # We do not call _lock_session() in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    # create python lock class variable; it is important the variable has class scope since
    # new instances of _SessionBase are constructed in __getitem__ of _RepeatedCapabilities
    import threading
    _pylock = threading.RLock()

    def _lock_session(self):
        '''_lock_session

        Actual call to python lock
        '''
        self._pylock.acquire()
        return

