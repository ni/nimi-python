<%page args="f, config, method_template"/>\
    def ${f['session_name']}(self):
        '''${f['session_name']}

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._library.unlock()
