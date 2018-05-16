<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
%>\
.. py:method:: ${function['python_name']}()

    Releases a lock that you acquired on an device session using
    :py:meth:`nidcpower.Session.lock_session`. Refer to :py:meth:`nidcpower.Session.lock_session` for additional
    information on session locks.


