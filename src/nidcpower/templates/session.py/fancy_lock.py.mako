<%page args="f, config, method_template"/>\
<%
    '''
    Unsynchronized operation does not yet support session lock and unlock as of DCPower 20.7. To avoid errors from the
    unimplemented functions, we will override the lock and unlock methods and only call into the super class method if
    independent channels isn't enabled. This fancy function needs to be removed in a later release of NI-DCPower.
    '''
%>\
    def _lock_session(self):
        '''_lock_session

        Overrides the lock session call of the SessionBase class.
        Only calls into super class method if _independent_channels is False.
        '''

        if not self._independent_channels:
            return super(Session, self)._lock_session()
        return

