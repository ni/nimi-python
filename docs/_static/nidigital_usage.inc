Usage
------

The following is a basic example of using the **nidigital** module to open a session to a ....

.. code-block:: python

    import nidigital
    # Configure the session.

    with nidigital.Session(resource_name='PXI1Slot2', channels='0') as session:
        pass

Additional examples for NI-Digital Pattern Driver are located in src/nidigital/examples/ directory.

