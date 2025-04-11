Usage
------

The following is a basic example of using the **nirfsg** module to open a session to an RF Signal Generator and generate a continuous wave (CW) signal.

.. code-block:: python

    import nirfsg

    # Configure the session
    with nirfsg.Session(resource_name='5841', id_query=False, reset_device=False, options='Simulate=1, DriverSetup=Model:5841') as session:
        # Configure RF settings
        session.configure_rf(
            frequency=1e9,  # Frequency in Hz
            power_level=-10.0  # Power level in dBm
        )
        session.generation_mode = nirfsg.GenerationMode.CW

        # Start signal generation
        with session.initiate():
            input("Press Enter to stop generation")

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nirfsg/examples>`_