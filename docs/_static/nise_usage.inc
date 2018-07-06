Usage
------

The following is a basic example of using the **nise** module to open a session to a Source Meter Unit and measure voltage and current.

.. code-block:: python

    import nise
    with nise.Session('SwitchExecutiveExample', '') as session:
        session.connect(connection)

Additional examples for NI Switch Executive are located in src/nise/examples/ directory.

