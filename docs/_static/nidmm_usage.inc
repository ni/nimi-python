Usage
------

The following is a basic example of using the **nidmm** module to open a session to a DMM and perform a 5.5 digits of resolution voltage measurement in the 10 V range.

.. code-block:: python

    import nidmm
    with nidmm.Session("Dev1") as session:
        session.configure_measurement_digits(nidmm.Function.DC_VOLTS, 10.0, 5.5)
        print("Measurement: " + str(session.read()))

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nidmm/examples>`_

