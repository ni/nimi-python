<%page args="f, config, method_template"/>\
<%
    '''Overrides the default unlock template to use a threading.RLock instead of the driver lock.

    See GitHub issue [1596](https://github.com/ni/nimi-python/issues/1596) for more information.
    '''
    import build.helper as helper

    c_function_prefix = config['c_function_prefix']
%>\
    # TODO(smooresni): Replace with session lock per GitHub issue [1596](https://github.com/ni/nimi-python/issues/1596)
    def ${f['python_name']}(self):
        '''${f['python_name']}

        Releases a lock that you acquired on the driver using
        lock. Refer to lock for additional
        information on driver locks.
        '''
        self._pylock.release()
        return

