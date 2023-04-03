<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
%>\
.. py:method:: ${function['python_name']}()

    Releases a lock that you acquired on an device session using
    :py:meth:`${config['module_name']}.Session.lock`. Refer to :py:meth:`${config['module_name']}.Session.unlock` for additional
    information on session locks.
