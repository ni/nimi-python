Usage
------

The following is a basic example of using the **nifgen** module to open a session to a Function Generator and generate a sine wave for 5 seconds.

.. code-block:: python

    import nifgen
    import time
    with nifgen.Session("Dev1") as session:
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(waveform=nifgen.Waveform.SINE, amplitude=1.0, frequency=10000000, dc_offset=0.0, start_phase=0.0)
        with session.initiate():
            time.sleep(5)

Additional examples for NI-FGEN are located in src/nifgen/examples/ directory `on GitHub <https://github.com/ni/nimi-python/tree/master/src/nifgen/examples>`_.

