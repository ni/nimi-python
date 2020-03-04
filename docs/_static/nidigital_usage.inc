Usage
------

The following is a basic example of using the **nidigital** module to open a session to a ....

.. code-block:: python

    import nidigital
    with nidigital.Session(resource_name='PXI1Slot2', channels='0') as session:
        pass


Some repeated capabilities can be nested. This is useful for some methods that can be used with the `pins`
repeated capability. They can be nested with the `sites` repeated capability.

.. code-block:: python

    import nidigital
    # Configure the session.

    with nidigital.Session(resource_name='PXI1Slot2', channels='0') as session:
        session.sites[0, 1].pins[2, 3].burst_pattern(
                start_label='new_pattern',
                select_digital_function=False,
                wait_until_done=True,
                timeout=5)

This will expand the repeated capabilities string given to the driver as `'site0/2,site0/3,site1/2,site1/3'`

Additional examples for NI-Digital Pattern Driver are located in src/nidigital/examples/ directory.

