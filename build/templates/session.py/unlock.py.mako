<%page args="f, config, method_template"/>\
    def ${f['python_name']}(self):
        '''${f['python_name']}

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()
