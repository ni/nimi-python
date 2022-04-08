Usage
------

The following is a basic example of using the **niswitch** module to open a session to a Switch and connect channels.

.. code-block:: python

    import niswitch
    with niswitch.Session("Dev1") as session:
        session.connect(channel1='r0', channel2='c0')

Additional examples for NI-SWITCH are located in src/niswitch/examples/ directory `on GitHub <https://github.com/ni/nimi-python/tree/master/src/niswitch/examples>`_.

