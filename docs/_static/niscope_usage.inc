:orphan:

Usage
------

The following is a basic example of using the **niscope** module to open a session to a High Speed Digitizer and capture a single record of 1000 points.

.. code-block:: python

    import niscope
    with niscope.Session("Dev1") as session:
        session.configure_vertical(range=1.0, coupling=niscope.VerticalCoupling.AC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=1000, ref_position=50.0, num_records=1, enforce_realtime=True)
        with session.initiate():
            wfm, wfm_infos = session[args.channels].fetch(num_samples=args.length)
        print('Number of samples acquired: {:,}\n'.format(len(wfm)))

Additional examples for NI-SCOPE are located in src/niscope/examples/ directory.

