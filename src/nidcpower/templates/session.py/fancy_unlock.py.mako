<%page args="f, config, method_template"/>\
<%
    '''
    Unsynchronized operation does not yet support session lock and unlock as of DCPower 20.7. To avoid errors from the
    unimplemented functions, we will override the lock and unlock methods and only call into the super class method if
    independent channels isn't enabled. This fancy function needs to be removed in a later release of NI-DCPower.
    '''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    def ${f['python_name']}(self):
        '''${f['python_name']}

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''

        if not self._independent_channels:
            return super(Session, self).${f['python_name']}()
        return

