Usage
------

The following is a basic example of using the **niscope** module to open a session to a High Speed Digitizer and capture a single record of 1000 points.

.. code-block:: python

    import niscope
    with niscope.Session("Dev1") as session:
        session.channels[0].configure_vertical(range=1.0, coupling=niscope.VerticalCoupling.AC)
        session.channels[1].configure_vertical(range=10.0, coupling=niscope.VerticalCoupling.DC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=1000, ref_position=50.0, num_records=5, enforce_realtime=True)
        with session.initiate():
            waveforms = session.channels[0,1].fetch(num_records=5)
        for wfm in waveforms:
            print('Channel {0}, record {1} samples acquired: {2:,}\n'.format(wfm.channel, wfm.record, len(wfm.samples)))

        # Find all channel 1 records (Note channel name is always a string even if integers used in channel[])
        chan1 = [wfm for wfm in waveforms if wfm.channel == '0']

        # Find all record number 3
        rec3 = [wfm for wfm in waveforms if wfm.record == 3]

If you need more performance or need to work with `SciPy <https://www.scipy.org/>`_, you can use the **fetch_into**() method instead of **fetch**(). This
method takes an already allocated `numpy <http://www.numpy.org/>`_ array and puts the acquired samples in it.

.. code-block:: python

    voltage_range = 1.0
    record_length = 2000
    channels = [0, 1]
    num_channels = len(channels)
    num_records = 5
    wfm = numpy.ndarray(num_channels * record_length, dtype=numpy.int8)
    session.configure_vertical(voltage_range, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, record_length, 50.0, num_records, True)
    with session.initiate():
        waveform_infos = session.channels[channels].fetch_into(waveform=wfm, num_records=num_records)



`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/niscope/examples>`_


