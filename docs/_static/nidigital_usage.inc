Usage
------

The following is a basic example of using the **nidigital** module to open a session to a ....

.. code-block:: python

    import nidigital
    with nidigital.Session(resource_name='PXI1Slot2', channels='0') as session:
        pass


Some repeated capabilities can be chained. This is useful for some methods that can be used with the `pins`
repeated capability. They can be chained with the `sites` repeated capability.

.. code-block:: python

    import nidigital
    # Configure the session.

    with nidigital.Session(resource_name='PXI1Slot2', channels='0') as session:
        session.sites[0, 1].pins['PinA', 'PinB'].ppmu_source()

This will apply the method/property to `'site0/PinA`, `site0/PinB`, `site1/PinA`, `site1/PinB'`

Additional examples for NI-Digital Pattern Driver are located in src/nidigital/examples/ directory.

