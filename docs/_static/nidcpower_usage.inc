Usage
------

The following is a basic example of using the **nidcpower** module to open a session to a Source Meter Unit and measure voltage and current.

.. code-block:: python

    import nidcpower
    # Configure the session.

    with nidcpower.Session('dev1') as session:
        session.measure_record_length = 20
        session.measure_record_length_is_finite = True
        session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
        session.voltage_level = 5.0

        session.commit()
        print('Effective measurement rate: {0} S/s'.format(session.measure_record_delta_time / 1))

        samples_acquired = 0
        print('  #    Voltage    Current    In Compliance')
        row_format = '{0:3d}:   {1:8.6f}   {2:8.6f}   {3}'
        with session.initiate():
            while samples_acquired < 20:
                measurements = session.fetch_multiple(count=session.fetch_backlog)
                samples_acquired += len(measurements)
                for i in range(len(measurements)):
                    print(row_format.format(i, measurements[i].voltage, measurements[i].current, measurements[i].in_compliance))

Additional examples for NI-DCPower are located in src/nidcpower/examples/ directory.

