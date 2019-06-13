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

        # Find all channel 1 records (Note channel name is always a sting even if integers used in channel[])
        chan1 = [wfm for wfm in waveforms if wfm.channel == '0']

        # Find all record number 3
        rec3 = [wfm for wfm in waveforms if wfm.record == 3]

The waveform returned from `fetch <http://nimi-python.readthedocs.io/en/master/niscope/functions.html#niscope.Session.fetch>`_ is a flat list of Python objects

    - Attributes:

        -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
        -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
        -  **x_increment** (float) the time between points in the acquired waveform in seconds
        -  **channel** (str) channel name this waveform was asquire from
        -  **record** (int) record number of this waveform
        -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                voltage = binary data * gain factor + offset

        -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                voltage = binary data * gain factor + offset

        - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

    - Such that all record 0 waveforms are first. For example, with a channel list of 0,1, you would have the following index values:

        - index 0 = record 0, channel 0
        - index 1 = record 0, channel 1
        - index 2 = record 1, channel 0
        - index 3 = record 1, channel 1
        - etc.


If you need more performance or need to work with `SciPy <https://www.scipy.org/>`_, you can use the `fetch_into()` method instead of `fetch()`. This
method takes an already allocated `numpy <http://www.numpy.org/>`_ array and puts the acquired samples in it. Data types supported:

    - `numpy.float64`
    - `numpy.int8`
    - `numpy.in16`
    - `numpy.int32`

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
        waveform_infos = session.channels[channels].fetch_into(wfm=wfm, num_records=num_records)

The waveform_infos returned from `fetch_into <http://nimi-python.readthedocs.io/en/master/niscope/functions.html#niscope.Session.fetch_into>`_ is a 1D list of Python objects

    - Attributes:

        -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
        -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
        -  **x_increment** (float) the time between points in the acquired waveform in seconds
        -  **channel** (str) channel name this waveform was asquire from
        -  **record** (int) record number of this waveform
        -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                voltage = binary data * gain factor + offset

        -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                voltage = binary data * gain factor + offset

        - **samples** (numpy array of datatype used) floating point array of samples. Length will be of the actual samples acquired

            .. note::

                Python 3 only

    - Such that all record 0 waveforms are first. For example, with a channel list of 0,1, you would have the following index values:

        - index 0 = record 0, channel 0
        - index 1 = record 0, channel 1
        - index 2 = record 1, channel 0
        - index 3 = record 1, channel 1
        - etc.


.. note:: When using Python 2, the waveform_infos objects do not include the waveform for that record. Instead, samples are in the waveform passed into the function using the following layout:

    - index 0 = record 0, channel 0
    - index *x* = record 0, channel 1
    - index 2\ *x* = record 1, channel 0
    - index 3\ *x* = record 1, channel 1
    - etc.
    - Where *x* = the record length


Additional examples for NI-SCOPE are located in src/niscope/examples/ directory.


