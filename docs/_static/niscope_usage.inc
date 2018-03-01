Usage
------

The following is a basic example of using the **niscope** module to open a session to a High Speed Digitizer and capture a single record of 1000 points.

.. code-block:: python

    import niscope
    with niscope.Session("Dev1") as session:
        session.configure_vertical(range=1.0, coupling=niscope.VerticalCoupling.AC)
        session.configure_horizontal_timing(min_sample_rate=50000000, min_num_pts=1000, ref_position=50.0, num_records=1, enforce_realtime=True)
        with session.initiate():
            waveforms = session[[0,1]].fetch()
        print('Number of samples acquired: {:,}\n'.format(len(waveforms.wfm)))

The waveform returned from fetch is a 1D list of Python objects

    - Attributes:

        -  **relative_initial_x** the time (in seconds) from the trigger to the first sample in the fetched waveform
        -  **absolute_initial_x** timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
        -  **x_increment** the time between points in the acquired waveform in seconds
        -  **actual_samples** the actual number of samples fetched and placed in the waveform array
        -  **gain** the gain factor of the given channel; useful for scaling binary data with the following formula:

            .. math::

                voltage = binary data * gain factor + offset

        -  **offset** the offset factor of the given channel; useful for scaling binary data with the following formula:

            .. math::

                voltage = binary data * gain factor + offset

        - **wfm** floating point array of samples

    - Such that all record 0 waveforms are first. For example, with a channel list of 0,1, you would have the following index values:

        - index 0 = record 0, channel 0
        - index 1 = record 0, channel 1
        - index 2 = record 1, channel 0
        - index 3 = record 1, channel 1
        - etc.




Additional examples for NI-SCOPE are located in src/niscope/examples/ directory.


