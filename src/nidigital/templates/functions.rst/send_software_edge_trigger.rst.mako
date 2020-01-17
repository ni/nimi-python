<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
%>\
    .. py:method:: send_software_edge_trigger()

        Sends a command to trigger the signal generator. This VI can act as an
        override for an external edge trigger.

        If called directly on the session, this will send a software start trigger.

        ..code:: python

            session.send_software_edge_trigger()

        If called using the script trigger repeated capability container, this will
        send a software trigger to the specified script trigger

        ..code:: python

            session.conditional_jump_triggers[1].send_software_edge_trigger()


