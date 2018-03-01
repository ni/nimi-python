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

The waveform returned from `fetch <http://nimi-python.readthedocs.io/en/master/niscope/functions.html#niscope.Session.fetch>`_ is a 1D list of Python objects

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


If you need more performance, need to work with `SciPy <https://www.scipy.org/>`_, or are concerned about memory usage, you can use the `fetch_into()` method instead of `fetch()`. This
method takes an already allocated `numpy <http://www.numpy.org/>`_ array and puts the acquired samples in it. Data types supported:

    - `numpy.float64`
    - `numpy.int8`
    - `numpy.in16`
    - `numpy.int32`

.. code-block:: python

    voltage_range = 1.0
    record_length = 2000
    channels = [0,1]
    num_channels = len(channels)
    wfm = numpy.ndarray(num_channels * record_length, dtype=numpy.int8)
    session.configure_vertical(voltage_range, niscope.VerticalCoupling.AC)
    session.configure_horizontal_timing(50000000, record_length, 50.0, 1, True)
    with session.initiate():
        waveform_infos = session.channels[channels].fetch_into(wfm=wfm)

The waveform_infos returned from `fetch_into <http://nimi-python.readthedocs.io/en/master/niscope/functions.html#niscope.Session.fetch_into>`_ is a 1D list of Python objects

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

    - Such that all record 0 waveforms are first. For example, with a channel list of 0,1, you would have the following index values:

        - index 0 = record 0, channel 0
        - index 1 = record 0, channel 1
        - index 2 = record 1, channel 0
        - index 3 = record 1, channel 1
        - etc.


.. note:: Unlike the normal `fetch()` the waveform_infos objects do not include the waveform for that record. Instead, samples are in the waveform passed into the function using the following layout:

    - index 0 = record 0, channel 0
    - index *x* = record 0, channel 1
    - index 2\ *x* = record 1, channel 0
    - index 3\ *x* = record 1, channel 1
    - Where *x* = the record length


Additional examples for NI-SCOPE are located in src/niscope/examples/ directory.


